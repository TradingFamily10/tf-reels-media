#!/usr/bin/env python3
"""Search Pixabay for several queries per beat, save thumbnails + a contact sheet per beat for visual picking.
Usage: broll_candidates.py EPISODE_DIR QUERIES.json   ({"5": ["microchip", "semiconductor"], ...})
"""
import json, os, sys, urllib.parse, urllib.request, subprocess
KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
key = open(os.path.join(KIT, "assets", "pixabay_key.txt")).read().strip()
def get(u, t=60):
    with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "TF-kit"}), timeout=t) as r: return r.read()
ep, qf = sys.argv[1], sys.argv[2]
Q = json.load(open(qf)); out = os.path.join(ep, "cand"); os.makedirs(out, exist_ok=True)
allc = {}
for beat, qs in Q.items():
    seen, cands = set(), []
    for q in qs:
        u = "https://pixabay.com/api/videos/?" + urllib.parse.urlencode({"key": key, "q": q, "per_page": 12, "safesearch": "true", "video_type": "film"})
        for h in json.loads(get(u)).get("hits", []):
            if h["id"] in seen: continue
            v = h["videos"]; big = v["large"] if v.get("large", {}).get("url") else v["medium"]
            if big.get("height", 0) < 1080: continue
            seen.add(h["id"]); cands.append({"id": h["id"], "q": q, "dur": h["duration"], "w": big["width"], "h": big["height"], "url": big["url"],
                                             "thumb": v["medium"].get("thumbnail") or v["small"].get("thumbnail"), "tags": h["tags"], "user": h["user"], "page": h["pageURL"]})
            if len([c for c in cands if c["q"] == q]) >= 6: break
    cands = cands[:12]
    files = []
    for c in cands:
        p = os.path.join(out, f"b{beat}_{c['id']}.jpg")
        try:
            open(p, "wb").write(get(c["thumb"]))
            subprocess.run(["convert", p, "-resize", "320x180^", "-gravity", "center", "-extent", "320x180", "-fill", "yellow", "-undercolor", "#000a",
                            "-pointsize", "16", "-annotate", "+0+70", f"{c['id']} {c['dur']}s {c['h']}p", p], check=True)
            files.append(p)
        except Exception as e:
            print("thumb fail", c["id"], e)
    if files:
        subprocess.run(["montage", *files, "-tile", "4x", "-geometry", "+3+3", "-background", "black", os.path.join(out, f"sheet_b{beat}.jpg")], check=True)
    allc[beat] = cands
    print(beat, len(cands), [ (c['id'], c['q']) for c in cands][:12])
json.dump(allc, open(os.path.join(out, "candidates.json"), "w"), indent=1)
