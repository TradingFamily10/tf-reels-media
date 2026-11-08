#!/usr/bin/env python3
"""Put a finished reel on the public media repo (branch `videos-dernieres-infos`, same method as the other
Trading Family factories) and print its public URL for Metricool.

  python3 engine/publish_media.py episodes/<id>/<file>.mp4     -> prints the raw URL, writes <dir>/media_url.txt

The branch is rewritten each run as one orphan commit and keeps only the last 3 days of files.
URL pinned to the commit sha (the CDN can serve a stale copy of a re-published name).
Files over 90 MB get a transparent re-encode (GitHub refuses files over 100 MB).
"""
import datetime, os, re, shutil, subprocess, sys, time

REPO = "TradingFamily10/tf-reels-media"
BRANCH = "videos-dernieres-infos"
WORK = "/home/claude/tf-reels-media-dernieres-infos"
KEEP_DAYS = 3


def run(cmd, cwd=None, check=True):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0:
        print(r.stdout[-2000:], r.stderr[-2000:])
        raise SystemExit(f"échec : {' '.join(cmd)}")
    return r


src = os.path.abspath(sys.argv[1])
name = datetime.date.today().isoformat() + "_" + os.path.basename(src)
if os.path.getsize(src) > 90e6:
    small = src[:-4] + "_web.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-i", src, "-c:v", "libx264", "-preset", "slow", "-crf", "18",
         "-maxrate", "7500k", "-bufsize", "15000k", "-pix_fmt", "yuv420p", "-c:a", "copy", "-movflags", "+faststart", small])
    print(f"[media] ré-encodé {os.path.getsize(src)/1e6:.0f} -> {os.path.getsize(small)/1e6:.0f} Mo")
    src = small

if os.path.exists(WORK):
    shutil.rmtree(WORK)
r = run(["git", "clone", "-q", "--depth", "1", "--branch", BRANCH, f"https://github.com/{REPO}", WORK], check=False)
if r.returncode != 0:
    os.makedirs(WORK)
    run(["git", "init", "-q", "-b", BRANCH], cwd=WORK)
    run(["git", "remote", "add", "origin", f"https://github.com/{REPO}"], cwd=WORK)
limit = (datetime.date.today() - datetime.timedelta(days=KEEP_DAYS)).isoformat()
for f in os.listdir(WORK):
    if f == ".git":
        continue
    m = re.match(r"(\d{4}-\d{2}-\d{2})", f)
    if not m or m.group(1) < limit:
        p = os.path.join(WORK, f)
        shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
shutil.copy(src, os.path.join(WORK, name))
run(["git", "checkout", "-q", "--orphan", "_new"], cwd=WORK)
run(["git", "add", "-A"], cwd=WORK)
run(["git", "-c", "user.email=tradingfamily001@gmail.com", "-c", "user.name=Trading Family",
     "commit", "-qm", f"Reels récents ({name})"], cwd=WORK)
run(["git", "push", "-q", "-f", "origin", f"_new:{BRANCH}"], cwd=WORK)
sha = run(["git", "rev-parse", "HEAD"], cwd=WORK).stdout.strip()
url = f"https://raw.githubusercontent.com/{REPO}/{sha}/{name}"
code = "?"
for _ in range(10):
    code = run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-I", url], check=False).stdout.strip()
    if code == "200":
        break
    time.sleep(5)
print(f"[media] {code} {url}")
open(os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), "media_url.txt"), "w").write(url)
sys.exit(0 if code == "200" else 3)
