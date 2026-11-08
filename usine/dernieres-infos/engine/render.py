#!/usr/bin/env python3
"""Render an episode: backgrounds + HTML overlay (Playwright) + audio -> MP4 1080x1920.

Usage: render.py EPISODE_DIR [--preview] [--frames a:b] [--still t1,t2,...]
"""
import json, os, sys, subprocess, time, argparse, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.dirname(HERE)
W, H = 1080, 1920
FONT = "/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf"


def sh(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(r.stderr[-3000:]); raise SystemExit("ffmpeg failed")
    return r


def find_broll(ep, seg):
    """B-roll file for a segment: EPISODE/broll/beat_XX.(mp4|mov|jpg|png) or explicit 'src'."""
    if seg.get("src") and os.path.exists(seg["src"]):
        return seg["src"]
    for ext in ("mp4", "mov", "webm", "jpg", "jpeg", "png"):
        p = os.path.join(ep, "broll", f"beat_{seg['beat']:02d}.{ext}")
        if os.path.exists(p):
            return p
    return None


def build_bg(ep, tl, out):
    """One clip per segment, then concat. Real b-roll: cover-crop + slow push-in.
    Missing b-roll: neutral placeholder card naming the shot to film/download."""
    tmp = os.path.join(ep, "_bg"); shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
    parts, prev_src = [], None
    fps = tl["fps"]
    for i, seg in enumerate(tl["bg"]):
        d = round(seg["end"] - seg["start"], 3)
        if i + 1 < len(tl["bg"]):
            d = round(tl["bg"][i + 1]["start"] - seg["start"], 3)
        o = os.path.join(tmp, f"{i:02d}.mp4")
        src = find_broll(ep, seg)
        blur = seg.get("blur_prev") or seg.get("blur")
        if seg.get("blur_prev") and prev_src:
            src = prev_src
        n = int(round(d * fps))
        cx = seg.get("cx", 0.5)          # horizontal framing of the 9:16 window (0 = left, 1 = right)
        push = seg.get("push", 0.03 if blur else 0.07)     # slow push-in over the shot
        punch = 0 if blur else seg.get("punch", 0.05)       # quick zoom-settle on the cut (dynamism)
        fz = f"(1+{push}*t/{max(d,0.1)}+{punch}*exp(-t*9))"
        inset = seg.get("inset", 0)      # remove letterbox bars baked into some stock clips
        pre = f"crop=iw:ih*{1-2*inset:.4f}:0:ih*{inset:.4f}," if inset else ""
        zoom = pre + (f"crop=w='min(iw,ih*9/16)':h='min(ih,iw*16/9)':x='(iw-min(iw,ih*9/16))*{cx}':y='(ih-min(ih,iw*16/9))/2',"
                f"scale=w='trunc({W}*{fz}/2)*2':h='trunc({H}*{fz}/2)*2':eval=frame,crop={W}:{H},setsar=1,fps={fps}")
        grade = (",eq=contrast=1.07:saturation=0.92:gamma=0.98,colorbalance=rs=-0.03:bs=0.035:rh=0.025:bh=-0.02,"
                 "unsharp=5:5:0.45:5:5:0.0")
        if src:
            is_img = src.lower().endswith((".jpg", ".jpeg", ".png"))
            ss = str(seg.get("ss", 0.4 if not blur else 0))
            inp = ["-loop", "1", "-t", str(d), "-i", src] if is_img else ["-stream_loop", "-1", "-ss", ss, "-t", str(d), "-i", src]
            vf = zoom + (",gblur=sigma=34,eq=brightness=-0.10:saturation=0.85" if blur else grade) + ",format=yuv420p"
            sh(["ffmpeg", "-y", "-v", "error", *inp, "-vf", vf, "-frames:v", str(n), "-r", str(fps), "-an",
                "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", o])
            if not blur:
                prev_src = src
        else:
            if seg.get("screen"):
                vf = "format=yuv420p"; col = "0x0b1c27"
            else:
                lab = (seg.get("label") or "").replace(":", r"\:").replace("'", "’")
                q = (seg.get("query") or "").replace(":", r"\:").replace("'", "’")
                dark = "0x14181d" if blur else "0x262c33"
                col = dark
                vf = (f"noise=alls=7:allf=t,"
                      f"drawbox=x=40:y=40:w={W-80}:h={H-80}:color=0x5b6672@0.6:t=3,"
                      f"drawtext=fontfile={FONT}:text='B-ROLL HD':fontcolor=0x8a95a1:fontsize=34:x=(w-tw)/2:y=500,"
                      f"drawtext=fontfile={FONT}:text='{lab}':fontcolor=0xc9d1d9:fontsize=40:x=(w-tw)/2:y=560,"
                      f"drawtext=fontfile={FONT}:text='{q}':fontcolor=0x6e7883:fontsize=26:x=(w-tw)/2:y=625,format=yuv420p")
            sh(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", f"color=c={col}:s={W}x{H}:r={fps}:d={d}",
                "-vf", vf, "-frames:v", str(n), "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", o])
        parts.append(o)
    lst = os.path.join(tmp, "list.txt")
    open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
    sh(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", out])


def cfg_for(ep):
    logo = None
    for cand in (os.path.join(ep, "logo.png"), os.path.join(KIT, "assets", "logo_tf.png")):
        if os.path.exists(cand):
            logo = "file://" + cand; break
    c = json.load(open(os.path.join(KIT, "assets", "brand.json")))
    c["logo"] = logo
    c["logos"] = json.load(open(os.path.join(KIT, "assets", "logos", "logos.json")))
    c["logo_dir"] = "file://" + os.path.join(KIT, "assets", "logos")
    c["tg_dir"] = "file://" + os.path.join(KIT, "assets", "telegram")
    return c


def overlay_frames(ep, tl, frame_range=None, stills=None, sink=None):
    from playwright.sync_api import sync_playwright
    fps = tl["fps"]; N = int(round(tl["duration"] * fps))
    a, b = (0, N) if not frame_range else frame_range
    with sync_playwright() as p:
        br = p.chromium.launch(args=["--force-color-profile=srgb", "--disable-lcd-text", "--font-render-hinting=none"])
        pg = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        pg.goto("file://" + os.path.join(HERE, "template.html"))
        pg.evaluate("document.fonts.ready")
        n = pg.evaluate("([tl,cfg]) => initTimeline(tl,cfg)", [tl, cfg_for(ep)])
        pg.wait_for_timeout(300)
        pg.evaluate("document.fonts.ready")
        if stills:
            out = []
            for t in stills:
                pg.evaluate(f"renderAt({t})")
                path = os.path.join(ep, f"still_{t:06.2f}.png")
                pg.screenshot(path=path, omit_background=True)
                out.append(path)
            br.close(); return out
        prev_k, prev_png, uniq, t0 = None, None, 0, time.time()
        for i in range(a, b):
            k = pg.evaluate(f"renderAt({i / fps:.5f})")
            if k != prev_k:
                prev_png = pg.screenshot(type="png", omit_background=True, animations="disabled", caret="hide")
                prev_k = k; uniq += 1
            sink(prev_png)
            if i % 150 == 0:
                print(f"  frame {i}/{b}  unique={uniq}  {time.time()-t0:.0f}s", flush=True)
        br.close()
        print(f"  overlay done: {b-a} frames, {uniq} unique, {time.time()-t0:.0f}s")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ep"); ap.add_argument("--preview", action="store_true")
    ap.add_argument("--still", default=None); ap.add_argument("--out", default=None)
    ap.add_argument("--best", action="store_true", help="max quality encode for publication")
    args = ap.parse_args()
    ep = os.path.abspath(args.ep)
    tl = json.load(open(os.path.join(ep, "timeline.json")))
    if args.still:
        ts = [float(x) for x in args.still.split(",")]
        print("\n".join(overlay_frames(ep, tl, stills=ts)))
        return
    bg = os.path.join(ep, "_bg.mp4")
    print("building backgrounds…"); build_bg(ep, tl, bg)
    audio = os.path.join(ep, "mix.wav")
    if not os.path.exists(audio):
        raise SystemExit("mix.wav missing: run audio.py first")
    out = args.out or os.path.join(ep, f"{tl.get('id', os.path.basename(ep))}{'_preview' if args.preview else ''}.mp4")
    enc = ["-c:v", "libx264", "-preset", "slow" if args.best else "veryfast", "-crf", "17" if args.best else "19",
           "-profile:v", "high", "-pix_fmt", "yuv420p", "-movflags", "+faststart"]
    vf = ("[0:v][1:v]overlay=0:0:format=auto:shortest=1,"
          "noise=alls=3:allf=t,vignette=PI/5.5,format=yuv420p[v]")
    cmd = ["ffmpeg", "-y", "-v", "error", "-i", bg, "-f", "image2pipe", "-framerate", str(tl["fps"]), "-c:v", "png", "-i", "-",
           "-i", audio, "-filter_complex", vf, "-map", "[v]", "-map", "2:a", *enc,
           "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-shortest", out]
    print("rendering overlay + encode…")
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    overlay_frames(ep, tl, sink=ff.stdin.write)
    ff.stdin.close(); ff.wait()
    print("OK ->", out)


if __name__ == "__main__":
    main()
