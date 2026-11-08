#!/usr/bin/env python3
"""Verification sheet: one frame every N seconds of a rendered MP4 -> PNG grid to look at before publishing.
Usage: contact_sheet.py VIDEO.mp4 OUT.png [step_seconds]
"""
import subprocess, sys, os, tempfile

video, out = sys.argv[1], sys.argv[2]
step = float(sys.argv[3]) if len(sys.argv) > 3 else 2.5
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", video],
                           capture_output=True, text=True).stdout)
tmp = tempfile.mkdtemp()
t, i, files = 0.5, 0, []
font = "/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf"
while t < dur:
    f = os.path.join(tmp, f"{i:03d}.png")
    subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", video, "-frames:v", "1", "-vf",
                    f"scale=216:384,drawtext=fontfile={font}:text='{t:.1f}':fontcolor=yellow:fontsize=16:x=4:y=4", "-y", f])
    files.append(f); t += step; i += 1
subprocess.run(["montage", *files, "-tile", "12x", "-geometry", "+2+2", "-background", "black", out], check=True)
print(out, len(files), "frames")
