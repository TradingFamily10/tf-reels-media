#!/usr/bin/env python3
"""spec.json (+ optional voice/beat_XX.wav) -> timeline.json

Usage: build_timeline.py EPISODE_DIR
If EPISODE_DIR/voice/beat_XX.wav exist, real durations are used (silences already trimmed),
otherwise durations are estimated from syllables (preview / animatic mode).
"""
import json, re, sys, os, subprocess

FPS = 30
RATE = 5.6           # syllables / second (news delivery, blancs coupés)
GAP_BEAT = 0.06      # silence kept between two beats
PAUSE = {",": .14, ":": .22, ";": .2, ".": .26, "?": .3, "!": .26, "…": .34}
ATTACH = {"%", "$", "€", "?", "!", ":", ";", "…", "»"}

VOW = "aeiouyàâäéèêëîïôöùûüœæ"


def tokens(text):
    raw = text.replace("...", "…").split()
    out = []
    for w in raw:
        if out and re.fullmatch(r"\d{3}[.,…]?", w) and re.search(r"\d$", out[-1]):   # "59 000" stays one word
            out[-1] = out[-1] + "\u00a0" + w
        elif out and w[0] in ATTACH:
            out[-1] = out[-1] + " " + w
        elif out and out[-1] == "«":
            out[-1] = out[-1] + " " + w
        else:
            out.append(w)
    return out


def syl(w):
    s = w.lower().replace(" ", " ")
    n = 0.0
    digits = re.findall(r"\d+", s)
    for d in digits:
        n += 1.6 * len(d.replace(",", "")) + 0.4
    if "%" in s:
        n += 2
    letters = re.sub(r"[^a-zàâäéèêëîïôöùûüœæç'’-]", "", s)
    if letters:
        core = re.sub(r"[^a-zàâäéèêëîïôöùûüœæç]", "", w.replace(" ", ""))
        if core.isupper() and len(core) <= 4 and core.isalpha():
            n += max(1, len(core) * 0.9)      # acronym spelled
        else:
            groups = re.findall(f"[{VOW}]+", letters)
            g = len(groups)
            if g > 1 and re.search(r"(e|es|ent)$", letters) and not letters.endswith(("ée", "ées")):
                g -= 1
            n += max(1, g)
    return max(n, 0.6)


def wav_dur(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                         capture_output=True, text=True).stdout.strip()
    return float(out)


STOP = {"de", "du", "des", "le", "la", "les", "l'", "un", "une", "en", "à", "au", "aux", "et", "ou", "son", "sa", "ses",
        "sur", "dans", "par", "pour", "ce", "cet", "cette", "qui", "que", "mon", "ma", "mes", "plus", "très", "près"}


def paginate(words, idx0):
    """group word indices into subtitle pages (1-2 lines, max 4 words / ~24 chars)."""
    pages, cur = [], []
    for i, w in enumerate(words):
        cur.append(idx0 + i)
        chars = sum(len(words[j - idx0]) + 1 for j in cur)
        end_sent = w[-1] in ".?!…:"
        comma = w.endswith(",")
        nxt = words[i + 1] if i + 1 < len(words) else None
        if (len(cur) >= 4 or chars >= 22 or end_sent or (comma and len(cur) >= 2)
                or (nxt and chars + len(nxt) > 26)):
            carry = []
            if not end_sent and not comma and len(cur) >= 3 and words[cur[-1] - idx0].lower() in STOP:
                carry = [cur.pop()]
            pages.append(cur); cur = carry
    if cur:
        if pages and len(cur) == 1 and len(words[cur[0] - idx0]) <= 4:
            pages[-1].extend(cur)
        else:
            pages.append(cur)
    out = []
    for pg in pages:
        txt = [words[j - idx0] for j in pg]
        total = sum(len(x) for x in txt) + len(txt) - 1
        if total <= 13 or len(pg) == 1 or (len(pg) == 2 and total <= 18):
            out.append([pg])
        else:
            best, bs = None, 1e9
            for k in range(1, len(pg)):
                a = sum(len(x) for x in txt[:k]) + k - 1
                b = sum(len(x) for x in txt[k:]) + len(txt) - k - 1
                if max(a, b) < bs:
                    bs, best = max(a, b), k
            out.append([pg[:best], pg[best:]])
    return out


def main(ep):
    spec = json.load(open(os.path.join(ep, "spec.json")))
    voice_dir = os.path.join(ep, "voice")
    t = 0.0
    words, beats, pages, overlays, bg, sfx, hide = [], [], [], [], [], [], []
    has_voice = True
    apath = os.path.join(voice_dir, "align.json")
    ALIGN = json.load(open(apath)) if os.path.exists(apath) else {}
    for bi, b in enumerate(spec["beats"]):
        ws = tokens(b["text"])
        sy = [syl(w) for w in ws]
        pz = [PAUSE.get(w[-1], 0) if j < len(ws) - 1 else 0 for j, w in enumerate(ws)]
        est = sum(sy) / RATE + sum(pz)
        vpath = os.path.join(voice_dir, f"beat_{bi:02d}.wav")
        if os.path.exists(vpath):
            dur = wav_dur(vpath)
        else:
            dur = est; has_voice = False
        scale = dur / est
        start = t
        i0 = len(words)
        cur = t
        al = ALIGN.get(str(bi))
        if al and len(al) == len(ws) and os.path.exists(vpath):
            for w, (_, ws_, we_) in zip(ws, al):     # real word times from Whisper
                words.append({"w": w, "start": round(start + ws_, 3), "end": round(start + we_, 3), "beat": bi})
        else:
            for w, s, p in zip(ws, sy, pz):
                d = s / RATE * scale
                words.append({"w": w, "start": round(cur, 3), "end": round(cur + d, 3), "beat": bi})
                cur += d + p * scale
        end = start + dur
        beats.append({"i": bi, "start": round(start, 3), "end": round(end, 3), "w0": i0, "w1": len(words) - 1,
                      "voice": vpath if os.path.exists(vpath) else None})
        for pg in paginate(ws, i0):
            flat = [j for ln in pg for j in ln]
            pages.append({"start": words[flat[0]]["start"], "lines": pg, "beat": bi})
        t = end + GAP_BEAT
    for k, pg in enumerate(pages):
        nxt = pages[k + 1]["start"] if k + 1 < len(pages) else beats[-1]["end"] + 0.2
        pg["end"] = round(nxt, 3)

    def wt(bi, wi):            # absolute start time of word wi inside beat bi
        b = beats[bi]
        j = min(b["w0"] + wi, b["w1"])
        return words[j]["start"]

    for bi, b in enumerate(spec["beats"]):
        B = beats[bi]
        for o in b.get("overlays", []):
            o = dict(o)
            st = B["start"]
            if "at_word" in o: st = wt(bi, o["at_word"])
            if "at_s" in o: st = B["start"] + o["at_s"]
            en = B["end"] + GAP_BEAT
            if "until_beat" in o: en = beats[min(bi + o["until_beat"], len(beats) - 1)]["end"] + GAP_BEAT
            if "until_word" in o: en = wt(bi, o["until_word"])
            if "until_s" in o: en = B["start"] + o["until_s"]
            o["start"], o["end"] = round(st, 3), round(en, 3)
            if o["type"] == "tickers":
                for r in o["rows"]:
                    r["t"] = round(wt(bi, r.get("at_word", 0)) - .05, 3)
            if o["type"] == "screen_duo":
                o["b_t"] = round(wt(bi, o.get("b_at_word", 0)), 3)
            if o["type"] == "phone":
                bl = o.get("bullets")
                if bl:
                    o["msg_t"] = [round(wt(bi, x["at_word"]), 3) for x in bl]
                if "bio_at_word" in o:
                    o["bio_t"] = round(wt(bi, o["bio_at_word"]), 3)
                else:
                    o["bio_t"] = round(wt(bi, max(0, B["w1"] - B["w0"] - 2)), 3)
            if o["type"] == "stock" and "strike_at_word" in o:
                o["strike_t"] = round(wt(bi, o["strike_at_word"]), 3)
            if o["type"] == "hook_bignum" and "reveal_at_word" in o:
                o["reveal_t"] = round(wt(bi, o["reveal_at_word"]), 3)
            if o["type"] == "cta_telegram":
                if "subs_at_word" in o: o["subs_t"] = round(wt(bi, o["subs_at_word"]), 3)
                if "bio_at_word" in o: o["bio_t"] = round(wt(bi, o["bio_at_word"]), 3)
            if o["type"] in ("breaking", "hook_bignum"):
                hide.append([o["start"], o["end"] + 0.05])
            overlays.append(o)
        # backgrounds: one shot, several shots cut on given words, or a blurred clip under a data screen
        gb = dict(b.get("bg", {}))
        shots = gb.pop("shots", None) or [{}]
        for k, sh_ in enumerate(shots):
            g = {**gb, **sh_}
            if gb.get("screen") and gb.get("under"):
                g.update(gb["under"]); g["blur"] = g.get("blur", True)
            if g.get("clip"):
                g["src"] = os.path.join(ep, "broll", g["clip"])
            st = B["start"] if k == 0 else wt(bi, sh_["at_word"]) - 0.04
            g["start"], g["end"] = round(st, 3), round(B["end"] + GAP_BEAT, 3)
            g["beat"] = bi
            bg.append(g)

    # screens chained back-to-back cut in hard
    scr = [o for o in overlays if o["type"].startswith("screen_")]
    for a in scr:
        for b2 in scr:
            if b2 is not a and abs(b2["end"] - a["start"]) < .2:
                a["cut_in"] = True

    total = beats[-1]["end"] + GAP_BEAT
    endcard = None
    last = spec["beats"][-1]
    if last.get("endcard"):
        ec = last["endcard"]
        endcard = {"start": round(total + 0.05, 3), "button": ec["button"], "small": ec["small"]}
        total = endcard["start"] + ec["duration"]
        hide.append([endcard["start"], total + 1])
    # extend last overlays to the end card
    for o in overlays:
        if o["end"] >= beats[-1]["end"]:
            o["end"] = round(endcard["start"] if endcard else total, 3)
    for i in range(len(bg) - 1):
        bg[i]["end"] = bg[i + 1]["start"]
    bg[-1]["end"] = round(total, 3)

    # ---------- SFX cue sheet ----------
    def cue(t0, kind, gain=1.0): sfx.append({"t": round(max(0, t0), 3), "k": kind, "g": gain})
    cue(0.0, "boom", 1.0)
    for o in overlays:
        ty = o["type"]
        if ty == "breaking":
            for i in range(len(o["lines"])): cue(o["start"] + .1 + i * .11, "swish", .55)
        elif ty in ("ticket", "news", "photo"): cue(o["start"], "pop", .9)
        elif ty == "hook_bignum":
            cue(o["start"] + .02, "count", .6)
            cue(o["start"] + o.get("count_dur", 1.0), "boom", 1.0)
            for i in range(len(o.get("logos", []))): cue(o["start"] + .15 + i * .07, "tick", .6)
            if o.get("reveal_t"): cue(o["reveal_t"] - .05, "swish", .8)
        elif ty == "screen_logos":
            cue(o["start"] - .05, "whoosh", .8); cue(o["start"] + .1, "count", .55)
            for i in range(len(o["keys"])): cue(o["start"] + .3 + i * .09, "pop", .55)
        elif ty == "cta_telegram":
            cue(o["start"] + .05, "ding", .9); cue(o["start"] + .35, "whoosh", .7)
            if o.get("subs_t"): cue(o["subs_t"], "count", .6)
            if o.get("bio_t"): cue(o["bio_t"], "pop", 1.0)
        elif ty == "stock":
            cue(o["start"], "pop", 1.0)
            if o.get("strike_t"): cue(o["strike_t"], "swish", .7)
        elif ty == "tickers":
            cue(o["start"], "pop", .9)
            for r in o["rows"]: cue(r["t"], "tick", .9)
        elif ty.startswith("screen_"):
            if not o.get("cut_in"): cue(o["start"] - .06, "whoosh", .8)
            else: cue(o["start"] - .03, "swish", .6)
            if ty in ("screen_counter", "screen_duo"): cue(o["start"] + .12, "count", .55)
            if ty == "screen_duo": cue(o["b_t"] + .05, "count", .55); cue(o["b_t"], "pop", .7)
            if ty == "screen_vote":
                n = sum(g["n"] for g in o["groups"])
                for i in range(n): cue(o["start"] + .1 + i * .07, "tick", .7)
            if ty == "screen_gauge": cue(o["start"] + .15, "rise", .6)
        elif ty == "bigtitle": cue(o["start"], "boom", .9)
        elif ty == "phone":
            cue(o["start"], "whoosh", .7)
            for tt in o.get("msg_t", []): cue(tt, "ding", .45)
            cue(o["bio_t"], "pop", .8)
        elif ty == "source": pass
    # soft cuts between filmed backgrounds
    for a, b2 in zip(bg, bg[1:]):
        if not b2.get("screen") and not a.get("screen"):
            cue(b2["start"] - .05, "cut", .35)
    if endcard:
        cue(endcard["start"] - .6, "rise", .7)
        cue(endcard["start"], "boom", .9)
    sfx.sort(key=lambda c: c["t"])

    tl = {"fps": FPS, "duration": round(total, 3), "has_voice": has_voice, "beats": beats, "words": words,
          "pages": pages, "overlays": overlays, "bg": bg, "sfx": sfx, "hide_subs": hide, "endcard": endcard,
          "date_label": spec.get("date_label")}
    json.dump(tl, open(os.path.join(ep, "timeline.json"), "w"), ensure_ascii=False, indent=1)
    print(f"duration {total:.2f}s  beats {len(beats)}  words {len(words)}  pages {len(pages)}  voice={'yes' if has_voice else 'ESTIMATED'}")
    for B in beats:
        print(f"  beat {B['i']:02d} {B['start']:6.2f} -> {B['end']:6.2f}")


if __name__ == "__main__":
    main(sys.argv[1])
