#!/usr/bin/env python3
"""Pre-render guard: measures the mean brightness of every clip segment the timeline actually uses.
A segment that is nearly black reads as an empty screen on a phone -> exit 1 so the run swaps the clip.
Usage: check_broll.py EPISODE_DIR   (run after build_timeline.py, before render.py)
Thresholds: luma < 18 = FAIL (too dark), luma < 28 = WARN (only OK under a blurred data screen).
"""
import json, os, subprocess, sys

ep = sys.argv[1]
kit = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tl = json.load(open(os.path.join(ep, "timeline.json")))
bad = 0
for seg in tl["bg"]:
    src = seg.get("src")
    if not src:
        continue
    path = src if os.path.isabs(src) else os.path.join(kit, src)
    dur = max(0.5, seg["end"] - seg["start"])
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(seg.get("ss", 0)), "-t", f"{dur:.2f}", "-i", path, "-vf",
                        "fps=2,scale=96:-2,signalstats,metadata=print:key=lavfi.signalstats.YAVG:file=-", "-f", "null", "-"],
                       capture_output=True, text=True)
    vals = [float(l.split("=")[1]) for l in r.stdout.splitlines() if "YAVG=" in l]
    if not vals:
        print(f"FAIL beat {seg['beat']:>2} {seg.get('clip')}: unreadable"); bad += 1; continue
    y = sum(vals) / len(vals)
    screen = seg.get("screen") or seg.get("blur")
    tag = "OK  "
    if y < 18:
        tag = "FAIL"; bad += 1
    elif y < 28 and not screen:
        tag = "WARN"
    print(f"{tag} beat {seg['beat']:>2} {seg.get('clip')}  ss={seg.get('ss', 0)}  luma={y:.0f}")
if bad:
    print(f"\n{bad} segment(s) too dark: pick another clip or another ss, then rebuild the timeline.")
    sys.exit(1)
print("broll luma OK")
