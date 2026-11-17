import json, sys, os, subprocess
sys.path.insert(0, '/home/claude/kit/engine')
import voice_hedra as V
import numpy as np, difflib
spec = json.load(open('spec.json'))
says = [(b.get('say') or b['text']).replace('...', ' ').split() for b in spec['beats']]
x = V.load('voice_raw/full.mp3'); heard = V.transcribe(x)
json.dump(heard, open('voice_raw/heard.json', 'w'), ensure_ascii=False)
D = [V.norm(w) for s in says for w in s]; H = [V.norm(h[0]) for h in heard]
times = [None]*len(D)
for a, b, n in difflib.SequenceMatcher(a=D, b=H, autojunk=False).get_matching_blocks():
    for k in range(n): times[a+k] = (heard[b+k][1], heard[b+k][2])
k = 0; bounds = []
for s in says:
    idx = [t for t in times[k:k+len(s)] if t]
    bounds.append((idx[0][0], idx[-1][1]) if idx else None); k += len(s)
print(bounds)
cuts = [0.0]
for i in range(len(bounds)-1): cuts.append((bounds[i][1]+bounds[i+1][0])/2)
cuts.append(len(x)/V.SR)
for i in range(len(says)):
    seg = x[int(cuts[i]*V.SR): int(cuts[i+1]*V.SR)]
    p = f'voice_raw/beat_{i:02d}.wav'; V.save(p, seg)
    subprocess.run(['ffmpeg','-y','-v','error','-i',p,'-b:a','192k',f'voice_raw/beat_{i:02d}.mp3'],check=True); os.remove(p)
    print(i, round(cuts[i+1]-cuts[i],2))
