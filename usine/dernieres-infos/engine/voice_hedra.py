#!/usr/bin/env python3
"""Hedra "Clément 2" voice -> per-beat WAVs + word timings (Whisper) for the episode.

Two input modes (EPISODE/voice_raw/):
  * full.mp3            one TTS call for the whole script (cheapest): split into beats with Whisper word times
  * beat_XX.mp3         one TTS call per beat
Output: EPISODE/voice/beat_XX.wav (44.1 kHz mono, trimmed, pauses tightened, warm EQ)
        EPISODE/voice/align.json  {beat: [[word, start, end], ...]} relative to each beat wav
Usage: voice_hedra.py EPISODE_DIR [--max-gap 0.14]
"""
import json, os, re, subprocess, sys, unicodedata, difflib, argparse, glob
import numpy as np
from scipy.io import wavfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_timeline import tokens  # noqa: E402

SR = 44100
_model = None


def model():
    global _model
    if _model is None:
        from faster_whisper import WhisperModel
        _model = WhisperModel("small", device="cpu", compute_type="int8", cpu_threads=2)
    return _model


def load(path, sr=SR):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768


def transcribe(x, sr=SR):
    import scipy.signal as ss
    x16 = ss.resample_poly(x, 16000, sr).astype(np.float32)
    segs, _ = model().transcribe(x16, language="fr", word_timestamps=True, beam_size=5)
    return [(w.word.strip(), float(w.start), float(w.end)) for s in segs for w in s.words]


def norm(w):
    w = unicodedata.normalize("NFKD", w.lower())
    w = "".join(c for c in w if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]", "", w)


def align(display, heard):
    """map display tokens -> (start, end) using whisper words; unmatched tokens interpolated."""
    D = [norm(t) for t in display]; H = [norm(h[0]) for h in heard]
    times = [None] * len(display)
    sm = difflib.SequenceMatcher(a=D, b=H, autojunk=False)
    for a, b, n in sm.get_matching_blocks():
        for k in range(n):
            times[a + k] = (heard[b + k][1], heard[b + k][2])
    # fuzzy pass for near matches (Mazdaq ~ Nasdaq)
    for i, t in enumerate(times):
        if t is None and D[i]:
            best, bj = 0, None
            for j, h in enumerate(H):
                r = difflib.SequenceMatcher(a=D[i], b=h).ratio()
                if r > best: best, bj = r, j
            if best >= .6:
                lo = max([k for k in range(i) if times[k]] or [-1])
                if lo < 0 or heard[bj][1] >= times[lo][0]:
                    times[i] = (heard[bj][1], heard[bj][2])
    # interpolate the rest by character weight
    t0 = heard[0][1] if heard else 0.0; t1 = heard[-1][2] if heard else 1.0
    i = 0
    while i < len(times):
        if times[i] is None:
            j = i
            while j < len(times) and times[j] is None: j += 1
            a = times[i - 1][1] if i > 0 else t0
            b = times[j][0] if j < len(times) else t1
            w = [max(1, len(display[k])) for k in range(i, j)]; tot = sum(w); c = a
            for k, ww in zip(range(i, j), w):
                d = (b - a) * ww / tot; times[k] = (c, c + d); c += d
            i = j
        else:
            i += 1
    return [[display[k], round(times[k][0], 3), round(times[k][1], 3)] for k in range(len(display))]


def trim(x, thr_db=-42, keep=.05):
    a = np.abs(x); win = int(.01 * SR)
    env = np.convolve(a, np.ones(win) / win, mode="same"); thr = a.max() * 10 ** (thr_db / 20)
    idx = np.where(env > thr)[0]
    if not len(idx): return x
    return x[max(0, idx[0] - int(keep * SR)): min(len(x), idx[-1] + int(keep * SR))]


def tighten(x, max_gap=.14, thr_db=-38):
    a = np.abs(x); win = int(.012 * SR)
    env = np.convolve(a, np.ones(win) / win, mode="same"); quiet = env < a.max() * 10 ** (thr_db / 20)
    out, i, n = [], 0, len(x)
    while i < n:
        j = i
        q = quiet[i]
        while j < n and quiet[j] == q: j += 1
        seg = x[i:j]
        if q and (j - i) > max_gap * SR:
            h = int(max_gap * SR / 2); f = np.linspace(1, 0, min(h, 300))
            a1, a2 = seg[:h].copy(), seg[-h:].copy(); a1[-len(f):] *= f; a2[:len(f)] *= f[::-1]
            seg = np.concatenate([a1, a2])
        out.append(seg); i = j
    return np.concatenate(out)


def polish(path):
    tmp = path + ".tmp.wav"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", path, "-af",
                    "highpass=f=70,equalizer=f=140:t=q:w=0.9:g=2,equalizer=f=3000:t=q:w=1.2:g=1.2,"
                    "acompressor=threshold=-20dB:ratio=2.5:attack=6:release=90:makeup=2", tmp], check=True)
    os.replace(tmp, path)


def save(path, x):
    x = x / (np.abs(x).max() or 1) * .92
    wavfile.write(path, SR, (x * 32767).astype(np.int16))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("ep"); ap.add_argument("--max-gap", type=float, default=.14)
    a = ap.parse_args(); ep = os.path.abspath(a.ep)
    spec = json.load(open(os.path.join(ep, "spec.json")))
    raw = os.path.join(ep, "voice_raw"); out = os.path.join(ep, "voice"); os.makedirs(out, exist_ok=True)
    disp = [tokens(b["text"]) for b in spec["beats"]]
    pieces = []
    full = os.path.join(raw, "full.mp3")
    if os.path.exists(full):
        x = load(full); heard = transcribe(x)
        flat = [t for d in disp for t in d]
        al = align(flat, heard)
        k, bounds = 0, []
        for d in disp:
            bounds.append((al[k][1], al[k + len(d) - 1][2])); k += len(d)
        cuts = [0.0]
        for i in range(len(bounds) - 1):
            cuts.append((bounds[i][1] + bounds[i + 1][0]) / 2)
        cuts.append(len(x) / SR)
        for i in range(len(disp)):
            pieces.append(x[int(cuts[i] * SR): int(cuts[i + 1] * SR)])
    else:
        for i in range(len(disp)):
            pieces.append(load(os.path.join(raw, f"beat_{i:02d}.mp3")))
    result = {}
    for i, x in enumerate(pieces):
        y = tighten(trim(x), a.max_gap)
        p = os.path.join(out, f"beat_{i:02d}.wav"); save(p, y); polish(p)
        y2 = load(p); heard = transcribe(y2)
        result[str(i)] = align(disp[i], heard)
        print(f"beat {i:02d} {len(y2)/SR:5.2f}s | {' '.join(h[0] for h in heard)[:90]}")
    json.dump(result, open(os.path.join(out, "align.json"), "w"), ensure_ascii=False, indent=0)


if __name__ == "__main__":
    main()
