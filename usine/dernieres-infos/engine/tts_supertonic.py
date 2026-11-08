#!/usr/bin/env python3
"""Free offline French TTS with Supertonic 3 (MIT, ONNX, CPU) — own minimal runner.

Model folder = sherpa-onnx packaging of Supertonic 3:
  duration_predictor / text_encoder / vector_estimator / vocoder (.int8.onnx),
  tts.json, unicode_indexer.bin (int32 per code point), voice.bin (6×int64 dims + ttl + dp float32).

Usage:
  tts_supertonic.py --model DIR --sid 7 --text "Bonjour" --out a.wav
  tts_supertonic.py --model DIR --sid 7 --episode EPISODE_DIR     (one wav per beat, from spec.json "say"/"text")
"""
import argparse, json, os, re, sys, unicodedata
import numpy as np
import onnxruntime as ort
from scipy.io import wavfile

LANGS = {"en", "ko", "ja", "ar", "bg", "cs", "da", "de", "el", "es", "et", "fi", "fr", "hi", "hr", "hu", "id", "it",
         "lt", "lv", "nl", "pl", "pt", "ro", "ru", "sk", "sl", "sv", "tr", "uk", "vi", "na"}


class Supertonic:
    def __init__(self, d, threads=2):
        self.cfg = json.load(open(os.path.join(d, "tts.json")))
        self.idx = np.fromfile(os.path.join(d, "unicode_indexer.bin"), dtype=np.int32)
        buf = open(os.path.join(d, "voice.bin"), "rb").read()
        dims = np.frombuffer(buf[:48], dtype=np.int64)
        nt = int(np.prod(dims[:3])); nd = int(np.prod(dims[3:]))
        data = np.frombuffer(buf[48:], dtype=np.float32)
        self.ttl = data[:nt].reshape(dims[:3]); self.dp = data[nt:nt + nd].reshape(dims[3:])
        self.n_speakers = int(dims[0])
        so = ort.SessionOptions(); so.intra_op_num_threads = threads; so.inter_op_num_threads = 1
        f = lambda n: ort.InferenceSession(os.path.join(d, n), sess_options=so, providers=["CPUExecutionProvider"])
        self.dp_s = f("duration_predictor.int8.onnx"); self.te_s = f("text_encoder.int8.onnx")
        self.ve_s = f("vector_estimator.int8.onnx"); self.vo_s = f("vocoder.int8.onnx")
        self.sr = self.cfg["ae"]["sample_rate"]; self.base = self.cfg["ae"]["base_chunk_size"]
        self.ccf = self.cfg["ttl"]["chunk_compress_factor"]; self.ldim = self.cfg["ttl"]["latent_dim"]

    @staticmethod
    def prep(text, lang):
        t = unicodedata.normalize("NFKD", text)
        for k, v in {"–": "-", "‑": "-", "—": "-", "_": " ", "“": '"', "”": '"', "‘": "'", "’": "'",
                     "´": "'", "`": "'", "[": " ", "]": " ", "|": " ", "/": " ", "#": " ", "→": " ", "←": " ",
                     " ": " ", " ": " ", "«": '"', "»": '"'}.items():
            t = t.replace(k, v)
        t = re.sub(r"[♥☆♡©\\]", "", t)
        for p in [",", ".", "!", "?", ";", ":"]:
            t = t.replace(" " + p, p)
        t = re.sub(r"\s+", " ", t).strip()
        if not re.search(r"[.!?;:,'\"')\]}…»]$", t):
            t += "."
        assert lang in LANGS
        return f"<{lang}>{t}</{lang}>"

    def ids(self, text, lang):
        s = self.prep(text, lang)
        cps = [ord(c) for c in s]
        ids = np.array([[self.idx[c] if c < len(self.idx) else -1 for c in cps]], dtype=np.int64)
        bad = [s[i] for i, v in enumerate(ids[0]) if v < 0]
        if bad:
            keep = [i for i, v in enumerate(ids[0]) if v >= 0]
            print("  [warn] unknown chars dropped:", set(bad), file=sys.stderr)
            ids = ids[:, keep]
        mask = np.ones((1, 1, ids.shape[1]), dtype=np.float32)
        return ids, mask

    def synth(self, text, sid=0, lang="fr", steps=10, speed=1.05, seed=1234):
        rng = np.random.default_rng(seed)
        ids, tmask = self.ids(text, lang)
        ttl = self.ttl[sid:sid + 1].astype(np.float32); dp = self.dp[sid:sid + 1].astype(np.float32)
        dur, *_ = self.dp_s.run(None, {"text_ids": ids, "style_dp": dp, "text_mask": tmask})
        dur = dur / speed
        emb, *_ = self.te_s.run(None, {"text_ids": ids, "style_ttl": ttl, "text_mask": tmask})
        wav_len = (dur * self.sr).astype(np.int64)
        chunk = self.base * self.ccf
        L = int((wav_len.max() + chunk - 1) // chunk)
        lmask = (np.arange(L) < (wav_len[:, None] + chunk - 1) // chunk).astype(np.float32).reshape(1, 1, L)
        xt = rng.standard_normal((1, self.ldim * self.ccf, L)).astype(np.float32) * lmask
        tot = np.array([steps], dtype=np.float32)
        for s in range(steps):
            xt, *_ = self.ve_s.run(None, {"noisy_latent": xt, "text_emb": emb, "style_ttl": ttl, "text_mask": tmask,
                                          "latent_mask": lmask, "current_step": np.array([s], dtype=np.float32),
                                          "total_step": tot})
        wav, *_ = self.vo_s.run(None, {"latent": xt})
        w = wav[0][: int(wav_len[0])]
        return w.astype(np.float32)


def trim(w, sr, thr_db=-42, keep=0.04):
    """cut leading/trailing silence, keep `keep` s of margin."""
    a = np.abs(w)
    if a.max() == 0: return w
    win = int(.01 * sr)
    env = np.convolve(a, np.ones(win) / win, mode="same")
    thr = a.max() * 10 ** (thr_db / 20)
    idx = np.where(env > thr)[0]
    if not len(idx): return w
    s = max(0, idx[0] - int(keep * sr)); e = min(len(w), idx[-1] + int(keep * sr))
    return w[s:e]


def tighten(w, sr, max_gap=0.17, thr_db=-38):
    """shorten internal pauses longer than max_gap (blancs coupés) without touching words."""
    a = np.abs(w); win = int(.012 * sr)
    env = np.convolve(a, np.ones(win) / win, mode="same")
    quiet = env < a.max() * 10 ** (thr_db / 20)
    out, i, n = [], 0, len(w)
    while i < n:
        if quiet[i]:
            j = i
            while j < n and quiet[j]: j += 1
            seg = w[i:j]
            if (j - i) > max_gap * sr:
                h = int(max_gap * sr / 2); fade = np.linspace(1, 0, min(h, 200))
                a1 = seg[:h].copy(); a2 = seg[-h:].copy()
                a1[-len(fade):] *= fade; a2[:len(fade)] *= fade[::-1]
                seg = np.concatenate([a1, a2])
            out.append(seg); i = j
        else:
            j = i
            while j < n and not quiet[j]: j += 1
            out.append(w[i:j]); i = j
    return np.concatenate(out) if out else w


def polish(path):
    """voice colour: rumble cut, warm lows, a bit of presence, gentle compression."""
    import subprocess
    tmp = path + ".tmp.wav"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", path, "-af",
                    "highpass=f=65,equalizer=f=130:t=q:w=0.9:g=2.5,equalizer=f=3200:t=q:w=1.2:g=1.5,"
                    "equalizer=f=7500:t=q:w=1.5:g=-1.5,acompressor=threshold=-20dB:ratio=2.5:attack=6:release=90:makeup=2",
                    tmp], check=True)
    os.replace(tmp, path)


def save(path, w, sr):
    w = w / (np.abs(w).max() or 1) * 0.92
    wavfile.write(path, sr, (w * 32767).astype(np.int16))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--sid", type=int, default=0)
    ap.add_argument("--text"); ap.add_argument("--out"); ap.add_argument("--episode")
    ap.add_argument("--steps", type=int, default=10); ap.add_argument("--speed", type=float, default=1.05)
    ap.add_argument("--seed", type=int, default=1234)
    a = ap.parse_args()
    tts = Supertonic(a.model)
    if a.text:
        w = trim(tts.synth(a.text, a.sid, "fr", a.steps, a.speed, a.seed), tts.sr)
        save(a.out, w, tts.sr); print(a.out, f"{len(w)/tts.sr:.2f}s"); return
    spec = json.load(open(os.path.join(a.episode, "spec.json")))
    vd = os.path.join(a.episode, "voice"); os.makedirs(vd, exist_ok=True)
    for i, b in enumerate(spec["beats"]):
        txt = b.get("say") or b["text"]
        w = tighten(trim(tts.synth(txt, a.sid, "fr", a.steps, a.speed, a.seed + i), tts.sr), tts.sr, max_gap=0.12)
        out = os.path.join(vd, f"beat_{i:02d}.wav")
        save(out, w, tts.sr); polish(out)
        print(f"beat {i:02d}  {len(w)/tts.sr:5.2f}s  {txt[:60]}")


if __name__ == "__main__":
    main()
