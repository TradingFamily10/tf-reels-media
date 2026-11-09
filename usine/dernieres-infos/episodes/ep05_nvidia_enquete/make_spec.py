import json,sys,os
sys.path.insert(0,'/home/claude/kit/engine')
from build_timeline import tokens
EP='/home/claude/kit/episodes/ep05_nvidia_enquete'
CL=json.load(open(EP+'/clips.json')) if os.path.exists(EP+'/clips.json') else {}
def idx(text,word):
    t=tokens(text)
    for i,w in enumerate(t):
        if word in w: return i
    raise SystemExit(f"{word} not in {t}")
B=[]
def beat(text,say=None,bg=None,ov=None,**kw):
    b={"text":text}
    if say: b["say"]=say
    b["bg"]=bg or {}; b["overlays"]=ov or []; b.update(kw); B.append(b); return b
def C(k,ss=1,cx=0.5):
    c=CL.get(k,{}); return {"clip":c.get("clip",k),"ss":c.get("ss",ss),"cx":c.get("cx",cx),**({"inset":c["inset"]} if "inset" in c else {})}

t="Et si l'homme le plus puissant de l'intelligence artificielle avait été la cible d'espions chinois ?"
beat(t,"Et si l'homme le plus puissant de l'intelligence artificielle... avait été la cible d'espions chinois ?",C("B0"),
 [{"type":"date","text":"Dimanche 8 novembre 2026","until_beat":1},
  {"type":"news","at_word":0,"left":"ACTUALITÉS","right":"ÉTATS-UNIS","tag":"NVIDIA","headline":"Nvidia ouvre une enquête sur son propre patron","highlight":"son propre patron","sub":"Communiqué du conseil d'administration · 8 novembre"},
  {"type":"stock","key":"NVDA","name":"Nvidia","sub":"NVDA · Nasdaq","y":1180,"at_word":idx(t,"cible")}])
beat("Et ce n'est pas un scénario de film.",None,C("B1",2))
t="Dimanche, Nvidia a lancé une enquête indépendante sur son propre fondateur, Jensen Huang."
beat(t,None,C("B2",2),
 [{"type":"stock","key":"NVDA","name":"Nvidia","sub":"Enquête indépendante · 8 nov.","size":"big","y":420,"at_word":idx(t,"Nvidia")},
  {"type":"source","text":"Communiqué Nvidia · CBS News · TechCrunch"}])
t="Selon la presse américaine, il aurait été visé par une opération de renseignement étrangère."
beat(t,None,C("B3",2),[{"type":"bigtitle","lines":["VISÉ PAR UN","SERVICE ÉTRANGER"],"at_word":idx(t,"opération")}])
t="Au cœur du dossier : une cadre de Megaspeed, un très gros client de Nvidia en Asie."
beat(t,"Au cœur du dossier : une cadre de Megaspeed... un très gros client de Nvidia en Asie.",C("B4",2),
 [{"type":"news","at_word":idx(t,"Megaspeed"),"left":"ACTUALITÉS","right":"SINGAPOUR","tag":"MEGASPEED","headline":"Un gros client de Nvidia au centre de l'affaire","highlight":"gros client","sub":"Fournisseur de cloud basé à Singapour"}])
t="Les services américains la soupçonnent de travailler pour Pékin. La Chine dément."
beat(t,None,{"shots":[C("B5",1),dict(C("B5b",1),at_word=idx(t,"Chine"))]},
 [{"type":"bigtitle","lines":["SOUPÇONNÉE DE","SERVIR PÉKIN"],"at_word":idx(t,"soupçonne")},
  {"type":"source","text":"New York Times · BBC"}])
t="Ce client a acheté pour plus de 4,8 milliards de dollars de puces Nvidia en deux ans."
beat(t,"Ce client a acheté pour plus de quatre milliards huit cents millions de dollars de puces Nvidia en deux ans.",
 {"screen":True,"under":C("B6")},
 [{"type":"screen_counter","kicker":"PUCES NVIDIA · MEGASPEED","value_from":0,"value_to":4.8,"decimals":1,"suffix":" Md$","color":"white","pill":"EN DEUX ANS","desc":"Selon le New York Times, cité par CBS News"}])
t="Alors… Nvidia est-elle en danger ?"
beat(t,"Alors... Nvidia est-elle en danger ?",C("B7",2),[{"type":"bigtitle","lines":["NVIDIA","EN DANGER ?"]}])
t="Ce dossier, je le décrypte en direct sur mon Telegram. Lien en bio."
beat(t,None,{"blur_prev":True},[{"type":"phone","mode":"mini","img":"tg_4b2fa9a8.jpg","bio_at_word":idx(t,"bio")}],cta="short")
t="Le conseil assure n'avoir aucune raison de croire à une fuite de secrets."
beat(t,None,C("B9",2),
 [{"type":"news","at_word":idx(t,"assure"),"left":"COMMUNIQUÉ","right":"NVIDIA","tag":"CONSEIL D'ADMINISTRATION","headline":"« Aucune raison de croire » à une fuite de secrets","highlight":"Aucune raison de croire","sub":"Enquête menée par des administrateurs indépendants et des avocats externes"}])
t="Et Jensen Huang reste aux commandes."
beat(t,None,C("B10",2),[{"type":"bigtitle","lines":["IL RESTE","AUX COMMANDES"],"at_word":idx(t,"reste")}])
t="Mais l'action arrive fragilisée : 186 dollars vendredi soir, 22 % sous son record."
beat(t,"Mais l'action arrive fragilisée : cent quatre-vingt-six dollars vendredi soir... vingt-deux pour cent sous son record.",
 {"screen":True,"under":C("B11")},
 [{"type":"screen_duo","a":{"kicker":"NVIDIA · CLÔTURE DU 6 NOV.","value_to":186.64,"decimals":2,"prefix":"","suffix":" $","color":"white","desc":"Vendredi soir à Wall Street","logo":"NVDA"},
   "b_at_word":idx(t,"22"),"b":{"kicker":"DEPUIS SON RECORD","value_to":-22,"prefix":"","suffix":" %","color":"red","desc":"Avant même l'annonce de l'enquête"}}])
t="Jeudi, elle avait déjà plongé de plus de 9 % en une séance."
beat(t,"Jeudi, elle avait déjà plongé de plus de neuf pour cent en une séance.",C("B12",2),
 [{"type":"stock","key":"NVDA","name":"Nvidia","sub":"Jeudi 5 novembre","pct":"−9,26 %","size":"big","y":440,"at_word":idx(t,"plongé")},
  {"type":"source","text":"24/7 Wall St. · Yahoo Finance"}])
t="Et l'histoire envoie deux signaux. En 2018, Wynn Resorts perd 10 % le jour où son patron est mis en cause."
beat(t,"Et l'histoire envoie deux signaux. En deux mille dix-huit, Wynn Resorts perd dix pour cent... le jour où son patron est mis en cause.",C("B13",2),
 [{"type":"stock","key":"WYNN","name":"Wynn Resorts","sub":"1er jour après la mise en cause · 2018","pct":"−10,1 %","size":"big","y":440,"at_word":idx(t,"Wynn")}])
t="Mais en 2006, Apple garde Steve Jobs après une enquête interne… et l'action prend 49 % en six mois."
beat(t,"Mais en deux mille six, Apple garde Steve Jobs après une enquête interne... et l'action prend quarante-neuf pour cent en six mois.",
 {"screen":True,"under":C("B14")},
 [{"type":"screen_duo","a":{"kicker":"WYNN RESORTS · 2018","value_to":-10.1,"decimals":1,"prefix":"","suffix":" %","color":"red","desc":"Premier jour après la mise en cause du patron","logo":"WYNN"},
   "b_at_word":idx(t,"Apple"),"b":{"kicker":"APPLE · 2006","value_to":49.1,"decimals":1,"prefix":"+","suffix":" %","color":"green","desc":"Six mois après l'enquête interne","logo":"AAPL"}},
  {"type":"source","text":"Historique compilé par 24/7 Wall St."}])
t="Prochains tests : l'inflation américaine mardi, puis les résultats de Nvidia le 17 novembre."
beat(t,"Prochains tests : l'inflation américaine mardi... puis les résultats de Nvidia le dix-sept novembre.",C("B15",2),
 [{"type":"date","text":"Mardi 10 nov. · 14 h 30 (Paris)"},
  {"type":"bigtitle","lines":["RÉSULTATS NVIDIA","MARDI 17 NOVEMBRE"],"at_word":idx(t,"résultats")}])
t="Tempête passagère… ou vraie crise de confiance ? Dis-le-moi en commentaire."
beat(t,"Tempête passagère... ou vraie crise de confiance ? Dis-le-moi en commentaire.",
 {"shots":[C("B16",1),dict(C("B16b",1),at_word=idx(t,"vraie"))]},
 [{"type":"bigtitle","lines":["TEMPÊTE PASSAGÈRE…","OU VRAIE CRISE ?"],"at_word":idx(t,"vraie")}])
t="Chaque matin, je fais le tri dans le bruit pour toi. Sur mon Telegram gratuit, plus de 22 000 personnes reçoivent l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées et mes opportunités en temps réel. Lien en bio."
beat(t,"Chaque matin, je fais le tri dans le bruit pour toi. Sur mon Telegram gratuit, plus de vingt-deux mille personnes reçoivent l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées, et mes opportunités en temps réel. Lien en bio.",
 {"blur_prev":True},
 [{"type":"cta_telegram","notif":"Nvidia, inflation, Fed : ce qui compte ce matin","imgs":["tg_1eaa56f0.jpg","tg_3435c02c.jpg","tg_38e4f34b.jpg"],"subs":22760,"subs_at_word":idx(t,"22"),"bio_at_word":idx(t,"bio"),"button":"ACCÈS GRATUIT"}],
 cta="long",endcard={"duration":1.8,"button":"ACCÈS GRATUIT","small":"Telegram gratuit · lien en bio"})
spec={"id":"ep05_nvidia_enquete","date_label":"9 novembre 2026","brand":"Invest Family Fr","hook_type":"headline","cta_type":"notif_scroll",
 "voice":{"engine":"hedra","voice":"Clément 2","voice_id":"voice_ed52485f-b64d-4dc4-8080-0847ae629dad","model":"elevenlabs-v3","speed":1.08,"stability":0.5},
 "beats":B,"sources":["https://www.cbsnews.com/news/nvidia-jensen-huang-investigation-china-intelligence/","https://techcrunch.com/2026/11/08/nvidia-says-its-investigating-ceo-jensen-huangs-relationship-with-possible-chinese-spy/","https://finance.yahoo.com/markets/stocks/articles/nvidia-board-just-opened-investigation-010700633.html","https://www.techflowpost.com/fr-FR/article/35194"]}
json.dump(spec,open(EP+'/spec.json','w'),ensure_ascii=False,indent=1)
says=[b.get("say",b["text"]) for b in B]
open(EP+'/full_say.txt','w').write("\n".join(says))
json.dump([[b["text"],b.get("say")] for b in B],open(EP+'/script.json','w'),ensure_ascii=False,indent=1)
print(len(B), sum(len(s.split()) for s in says))
