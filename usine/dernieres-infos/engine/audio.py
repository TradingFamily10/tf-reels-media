#!/usr/bin/env python3
"""Audio mix: voice beats + SFX cue sheet + tension bed -> EPISODE/mix.wav (48 kHz stereo, -14 LUFS).

SFX are synthesised (no external library needed). If EPISODE/../../assets/sfx/<kind>.wav exists,
that real file is used instead of the synthetic one (drop your kit SFX there).
"""
import json, os, sys, subprocess
import numpy as np
from scipy import signal
from scipy.io import wavfile

SR = 48000
KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rng = np.random.default_rng(7)


def env(n, a=0.005, r=0.2, curve=4.0):
    t = np.arange(n) / SR
    e = np.minimum(1, t / max(a, 1e-4)) * np.exp(-curve * np.maximum(0, t - a) / max(r, 1e-4))
    return e


def bp(x, lo, hi, order=2):
    b, a = signal.butter(order, [lo / (SR / 2), min(hi / (SR / 2), .99)], "band")
    return signal.lfilter(b, a, x)


def lp(x, f, order=2):
    b, a = signal.butter(order, min(f / (SR / 2), .99), "low")
    return signal.lfilter(b, a, x)


def sweep_noise(dur, f0, f1, f2=None):
    n = int(dur * SR); x = rng.standard_normal(n); out = np.zeros(n)
    blk = 512
    for i in range(0, n, blk):
        k = i / n
        f = f0 + (f1 - f0) * (k * 2 if f2 and k < .5 else k) if not f2 else (f0 + (f1 - f0) * k * 2 if k < .5 else f1 + (f2 - f1) * (k - .5) * 2)
        seg = x[max(0, i - 256):i + blk]
        y = bp(seg, max(60, f * .55), f * 1.6)
        out[i:i + blk] = y[-len(out[i:i + blk]):]
    return out


def stereo(x, pan_from=0.0, pan_to=0.0):
    n = len(x); p = np.linspace(pan_from, pan_to, n)
    return np.stack([x * np.sqrt((1 - p) / 2), x * np.sqrt((1 + p) / 2)], 1) * 1.41


def synth(kind):
    if kind == "pop":
        n = int(.16 * SR); t = np.arange(n) / SR
        f = 260 + 700 * np.exp(-t * 60)
        x = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, .001, .05, 3)
        x += .6 * np.sin(2 * np.pi * 85 * t) * env(n, .002, .07, 3)
        x += .25 * bp(rng.standard_normal(n), 2000, 7000) * env(n, .0005, .012, 3)
        return stereo(x * .8)
    if kind == "tick":
        n = int(.05 * SR); t = np.arange(n) / SR
        x = np.sin(2 * np.pi * 2300 * t) * env(n, .0005, .012, 3) + .5 * bp(rng.standard_normal(n), 3000, 9000) * env(n, .0003, .006, 3)
        return stereo(x * .45)
    if kind == "count":
        out = np.zeros((int(1.0 * SR), 2))
        k, tt = 0, 0.0
        while tt < .9:
            tk = synth("tick") * (1 - tt / 1.1) * .7
            i = int(tt * SR); out[i:i + len(tk)] += tk[:len(out) - i]
            tt += .035 + .06 * (tt / .9) ** 2; k += 1
        return out
    if kind == "swish":
        x = sweep_noise(.26, 1800, 6500) * np.hanning(int(.26 * SR)) ** 1.5
        return stereo(x * .9, -.4, .4)
    if kind in ("whoosh", "cut"):
        d = .5 if kind == "whoosh" else .28
        n = int(d * SR)
        x = sweep_noise(d, 250, 2600, 300)
        e = np.hanning(n) ** 2
        x = x * e
        x += .5 * lp(rng.standard_normal(n), 180) * e
        return stereo(x * (1.0 if kind == "whoosh" else .7), -.6, .6)
    if kind == "boom":
        n = int(1.6 * SR); t = np.arange(n) / SR
        f = 38 + 40 * np.exp(-t * 9)
        x = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, .003, .7, 3.2)
        x = np.tanh(2.2 * x) * .9
        x += .5 * lp(rng.standard_normal(n), 900) * env(n, .001, .06, 3)
        x += .25 * bp(rng.standard_normal(n), 120, 1200) * env(n, .01, .9, 4)
        return stereo(x * .95)
    if kind == "rise":
        d = .7; n = int(d * SR); t = np.arange(n) / SR
        x = sweep_noise(d, 400, 5000) * (t / d) ** 2.2
        x += .25 * signal.sawtooth(2 * np.pi * np.cumsum(120 + 500 * (t / d) ** 2) / SR) * (t / d) ** 2
        x = lp(x, 6000)
        return stereo(x * .7, -.3, .3)
    if kind == "ding":
        n = int(.45 * SR); t = np.arange(n) / SR
        x = (np.sin(2 * np.pi * 1318 * t) + .5 * np.sin(2 * np.pi * 1975 * t) + .2 * np.sin(2 * np.pi * 2637 * t)) * env(n, .002, .18, 3)
        return stereo(x * .35)
    raise ValueError(kind)


def load_sfx(kind):
    p = os.path.join(KIT, "assets", "sfx", f"{kind}.wav")
    if os.path.exists(p):
        sr, x = wavfile.read(p); x = x.astype(np.float32)
        x /= (np.abs(x).max() or 1)
        if x.ndim == 1: x = np.stack([x, x], 1)
        if sr != SR: x = signal.resample(x, int(len(x) * SR / sr))
        return x * .8
    return synth(kind)


def bed(dur):
    """low tension bed: dark drone + heartbeat pulse every 1.3 s + air."""
    n = int(dur * SR); t = np.arange(n) / SR
    drone = .5 * np.sin(2 * np.pi * 55 * t) + .3 * lp(signal.sawtooth(2 * np.pi * 82.4 * t), 260) + .2 * lp(signal.sawtooth(2 * np.pi * 110.3 * t + 1), 220)
    drone *= .75 + .25 * np.sin(2 * np.pi * t / 7.0)
    pulse = np.zeros(n); beat = 1.3
    th = synth("boom")[:, 0][: int(.35 * SR)] * np.hanning(int(.7 * SR))[int(.35 * SR):]
    k = 0.0
    while k < dur:
        for off, g in ((0, 1), (.2, .6)):
            i = int((k + off) * SR)
            if i < n: pulse[i:i + len(th)] += th[:n - i] * g
        k += beat
    air = .08 * bp(rng.standard_normal(n), 3000, 9000)
    # news-style ticking: soft closed-hat clicks on 8th notes (~120 BPM), accent on the beat
    tick = np.zeros(n); step = 0.25; kk = 0
    click = bp(rng.standard_normal(int(.03 * SR)), 5000, 12000) * np.exp(-np.arange(int(.03 * SR)) / (.004 * SR))
    tt = 0.0
    while tt < dur:
        i = int(tt * SR); g = 1.0 if kk % 2 == 0 else .55
        if i < n: tick[i:i + len(click)] += click[:n - i] * g
        tt += step; kk += 1
    x = .55 * drone + .35 * lp(pulse, 160) + air + .22 * tick
    fade = np.ones(n); f = int(1.2 * SR); fade[:f] = np.linspace(0, 1, f); fade[-f:] = np.linspace(1, 0, f)
    return stereo(x * fade * .5)


def main(ep):
    tl = json.load(open(os.path.join(ep, "timeline.json")))
    dur = tl["duration"] + .3
    n = int(dur * SR)
    voice = np.zeros((n, 2)); fx = np.zeros((n, 2))
    for b in tl["beats"]:
        if b.get("voice") and os.path.exists(b["voice"]):
            sr, v = wavfile.read(b["voice"]); v = v.astype(np.float32)
            if v.ndim > 1: v = v.mean(1)
            v /= (np.abs(v).max() or 1)
            if sr != SR: v = signal.resample(v, int(len(v) * SR / sr))
            i = int(b["start"] * SR); v2 = np.stack([v, v], 1) * .9
            voice[i:i + len(v2)] += v2[: n - i]
    cache = {}
    for c in tl["sfx"]:
        k = c["k"]
        if k not in cache: cache[k] = load_sfx(k)
        s = cache[k] * c["g"]
        i = int(c["t"] * SR)
        if i < n: fx[i:i + len(s)] += s[: n - i]
    # short synthetic room reverb on the effects bus (less "dry/cheap")
    ir_n = int(.7 * SR); ir = rng.standard_normal(ir_n) * np.exp(-np.arange(ir_n) / (.16 * SR)); ir = lp(ir, 5000); ir /= np.abs(ir).sum() / 6
    wet = np.stack([signal.fftconvolve(fx[:, 0], ir)[:n], signal.fftconvolve(fx[:, 1], ir[::-1].copy())[:n]], 1)
    fx = fx + .18 * wet / (np.abs(wet).max() or 1) * (np.abs(fx).max() or 1)
    bg = bed(dur)
    has_voice = np.abs(voice).max() > 0
    if has_voice:   # duck the bed under the voice
        e = lp(np.abs(voice[:, 0]), 6)
        e = e / (e.max() or 1)
        bg = bg * (1 - .55 * np.clip(e * 4, 0, 1))[:, None]
        mix = voice * 1.0 + fx * .32 + bg * .22
    else:
        mix = fx * .45 + bg * .35
    mix = np.tanh(mix * 1.1) / 1.1
    raw = os.path.join(ep, "_mix_raw.wav")
    wavfile.write(raw, SR, (mix / (np.abs(mix).max() or 1) * .9 * 32767).astype(np.int16))
    out = os.path.join(ep, "mix.wav")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", raw, "-af", "loudnorm=I=-14:TP=-1.2:LRA=9", "-ar", str(SR), out], check=True)
    print("mix ->", out, f"({dur:.1f}s, voice={'yes' if has_voice else 'no'})")


if __name__ == "__main__":
    main(os.path.abspath(sys.argv[1]))
