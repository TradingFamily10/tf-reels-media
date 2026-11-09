# same as engine/voice_hedra.py main(), but beats are split using the spoken text ("say") instead of "text"
import sys,os,json
sys.path.insert(0,'/home/claude/kit/engine')
import voice_hedra as V
ep=os.path.abspath(sys.argv[1]); OVR={int(k):v for k,v in (a.split('=') for a in sys.argv[2:])}
spec=json.load(open(ep+'/spec.json')); raw=ep+'/voice_raw'; out=ep+'/voice'; os.makedirs(out,exist_ok=True)
disp=[V.tokens(b["text"]) for b in spec["beats"]]
says=[V.tokens(b.get("say",b["text"])) for b in spec["beats"]]
x=V.load(raw+'/full.mp3'); heard=V.transcribe(x)
json.dump(heard,open(ep+'/heard_full.json','w'),ensure_ascii=False)
flat=[t for d in says for t in d]; al=V.align(flat,heard); k=0; bounds=[]
for d in says: bounds.append((al[k][1],al[k+len(d)-1][2])); k+=len(d)
cuts=[0.0]+[(bounds[i][1]+bounds[i+1][0])/2 for i in range(len(bounds)-1)]+[len(x)/V.SR]
for i,c in OVR.items(): cuts[i]=float(c)
print("cuts",[round(c,2) for c in cuts])
SR=V.SR; result={}
for i in range(len(disp)):
    y=V.tighten(V.trim(x[int(cuts[i]*SR):int(cuts[i+1]*SR)]),.14)
    p=f"{out}/beat_{i:02d}.wav"; V.save(p,y); V.polish(p)
    y2=V.load(p); h=V.transcribe(y2); result[str(i)]=V.align(disp[i],h)
    print(f"beat {i:02d} {len(y2)/SR:5.2f}s | {' '.join(w[0] for w in h)}")
json.dump(result,open(out+'/align.json','w'),ensure_ascii=False,indent=0)
