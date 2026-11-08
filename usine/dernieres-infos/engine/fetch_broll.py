#!/usr/bin/env python3
"""Download one HD Pixabay video per beat (bg.query in spec.json) -> EPISODE/broll/beat_XX.mp4

Picks the sharpest rendition (4K 'large' when available, else 1920 'medium'), long enough for the beat,
never the same video twice in an episode. Credits saved to broll/credits.json.
Key: env PIXABAY_KEY or assets/pixabay_key.txt
Usage: fetch_broll.py EPISODE_DIR
"""
import json, os, sys, urllib.parse, urllib.request

KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def key():
    k = os.environ.get("PIXABAY_KEY")
    if k: return k.strip()
    return open(os.path.join(KIT, "assets", "pixabay_key.txt")).read().strip()


def get(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": "TF-kit/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def search(q, k, n=30):
    u = "https://pixabay.com/api/videos/?" + urllib.parse.urlencode(
        {"key": k, "q": q, "per_page": n, "safesearch": "true", "video_type": "film", "order": "popular"})
    return json.loads(get(u)).get("hits", [])


def pick(hits, need_s, used):
    best, bs = None, -1
    for h in hits:
        if h["id"] in used: continue
        v = h["videos"]
        for size in ("large", "medium"):
            r = v.get(size) or {}
            if not r.get("url"): continue
            w, ht = r.get("width", 0), r.get("height", 0)
            score = min(ht, 2160) / 1080 * 2 + (1 if h.get("duration", 0) >= need_s else 0) + h.get("likes", 0) / 500
            if ht >= 1080 and score > bs:
                bs, best = score, (h, size, r)
            break
    return best


def main(ep):
    spec = json.load(open(os.path.join(ep, "spec.json")))
    tl_path = os.path.join(ep, "timeline.json")
    durs = {}
    if os.path.exists(tl_path):
        for b in json.load(open(tl_path))["bg"]:
            durs[b["beat"]] = b["end"] - b["start"]
    out = os.path.join(ep, "broll"); os.makedirs(out, exist_ok=True)
    k = key(); used, credits = set(), {}
    for i, b in enumerate(spec["beats"]):
        q = (b.get("bg") or {}).get("query")
        if not q: continue
        dst = os.path.join(out, f"beat_{i:02d}.mp4")
        if os.path.exists(dst): continue
        hits = search(q, k)
        if not hits and " " in q:
            hits = search(" ".join(q.split()[:2]), k)
        p = pick(hits, durs.get(i, 4), used)
        if not p:
            print(f"beat {i:02d}: nothing for '{q}'"); continue
        h, size, r = p
        open(dst, "wb").write(get(r["url"], timeout=300))
        used.add(h["id"])
        credits[f"beat_{i:02d}"] = {"id": h["id"], "page": h.get("pageURL"), "user": h.get("user"), "size": f"{r['width']}x{r['height']}", "query": q}
        print(f"beat {i:02d}: {q!r} -> #{h['id']} {r['width']}x{r['height']} {h.get('duration')}s")
    json.dump(credits, open(os.path.join(out, "credits.json"), "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main(os.path.abspath(sys.argv[1]))
