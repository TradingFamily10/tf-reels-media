# wrapper: same as engine/voice_hedra.py main(), with manual cut override for beat 0/1
import sys,os,json
sys.path.insert(0,'/home/claude/kit/engine')
import voice_hedra as V
ep=os.path.abspath(sys.argv[1]); OVR={1:6.0}
spec=json.load(open(ep+'/spec_full.json')); raw=ep+'/voice_raw'; out=ep+'/voice'; os.makedirs(out,exist_ok=True)
disp=[V.tokens(b["text"]) for b in spec["beats"]]
x=V.load(raw+'/full.mp3'); heard=V.transcribe(x)
flat=[t for d in disp for t in d]; al=V.align(flat,heard); k=0; bounds=[]
for d in disp: bounds.append((al[k][1],al[k+len(d)-1][2])); k+=len(d)
cuts=[0.0]+[(bounds[i][1]+bounds[i+1][0])/2 for i in range(len(bounds)-1)]+[len(x)/V.SR]
for i,c in OVR.items(): cuts[i]=c
SR=V.SR; result={}; DROP={11}; j=0
for i in range(len(disp)):
    if i in DROP: continue
    y=V.tighten(V.trim(x[int(cuts[i]*SR):int(cuts[i+1]*SR)]),.10)
    p=f"{out}/beat_{j:02d}.wav"; V.save(p,y); V.polish(p)
    y2=V.load(p); h=V.transcribe(y2); result[str(j)]=V.align(disp[i],h)
    print(f"beat {j:02d} {len(y2)/SR:5.2f}s | {' '.join(w[0] for w in h)}"); j+=1
import glob
for f in glob.glob(out+'/beat_*.wav'):
    if int(f[-6:-4])>=j: os.remove(f)
json.dump(result,open(out+'/align.json','w'),ensure_ascii=False,indent=0)
