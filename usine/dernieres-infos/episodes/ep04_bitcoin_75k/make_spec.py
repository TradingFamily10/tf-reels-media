import json,sys,re
sys.path.insert(0,'/home/claude/kit/engine')
from build_timeline import tokens
def idx(text,word):
    t=tokens(text)
    for i,w in enumerate(t):
        if word in w: return i
    raise SystemExit(f"{word} not in {t}")
B=[]
def beat(text,say=None,bg=None,ov=None,**kw):
    b={"text":text}
    if say: b["say"]=say
    b["bg"]=bg or {}
    b["overlays"]=ov or []
    b.update(kw); B.append(b); return b
C=lambda c,ss=1,cx=0.5:{"clip":c,"ss":ss,"cx":cx}
t0="Dans 48 heures, un seul chiffre peut faire replonger le bitcoin. Et il est déjà tombé sous les 75 000 dollars."
beat(t0,"Dans quarante-huit heures... un seul chiffre peut faire replonger le bitcoin. Et il est déjà tombé sous les soixante-quinze mille dollars.",
 {"screen":True,"under":C("B0")},
 [{"type":"date","text":"Vendredi 6 novembre 2026","until_beat":1},
  {"type":"screen_logos","kicker":"BITCOIN · PLUS BAS DEPUIS LE 21 AOÛT","value_from":81004,"value_to":74762,"decimals":0,"suffix":" $","color":"red","pill":"PLUS BAS DE 11 SEMAINES","keys":["BTC","BLK","MSTR","COIN","DJT"],"desc":"Bitcoin · BlackRock · Strategy · Coinbase · Trump Media"}])
beat("Et ce n'est même pas le pire.",None,C("B1",2))
t="Vendredi, plus d'un milliard de dollars de positions ont été liquidées en 24 heures."
beat(t,"Vendredi, plus d'un milliard de dollars de positions ont été liquidées en vingt-quatre heures.",
 {"screen":True,"under":C("B2")},
 [{"type":"screen_counter","kicker":"LIQUIDATIONS · 24 H","value_from":0,"value_to":1.05,"decimals":2,"suffix":" Md$","color":"red","pill":"SURTOUT DES PARIS À LA HAUSSE","desc":"Données CoinGlass · vendredi 6 novembre","drop":True}])
t="Mercredi, il valait encore plus de 81 000 dollars."
beat(t,"Mercredi, il valait encore plus de quatre-vingt-un mille dollars.",C("B3",2),
 [{"type":"stock","key":"BTC","name":"Bitcoin","sub":"81 004 $ → 74 762 $ · 4 au 6 nov.","pct":"−7,7 %","size":"big","y":440,"at_word":0},
  {"type":"source","text":"Cours CoinGecko"}])
t="Et les gros investisseurs, eux, sortent par la grande porte."
beat(t,None,C("B4",2),[{"type":"bigtitle","lines":["LES GROS INVESTISSEURS","SORTENT"],"at_word":idx(t,"sortent")}])
t="Cette semaine, les ETF bitcoin américains ont vu fuir près de 1,3 milliard de dollars."
beat(t,"Cette semaine, les E.T.F. bitcoin américains ont vu fuir près d'un milliard trois cents millions de dollars.",
 {"screen":True,"under":C("B5")},
 [{"type":"screen_counter","kicker":"ETF BITCOIN AMÉRICAINS","value_from":0,"value_to":-1.28,"decimals":2,"suffix":" Md$","color":"red","pill":"SORTIES NETTES · 2 AU 6 NOV.","desc":"Données Farside · TFTC","drop":True}])
t="Rien que vendredi, le fonds de BlackRock a subi 403 millions de dollars de retraits."
beat(t,"Rien que vendredi, le fonds de BlackRock a subi quatre cent trois millions de dollars de retraits.",
 {"screen":True,"under":C("B6")},
 [{"type":"screen_duo","a":{"kicker":"IBIT · BLACKROCK","value_to":-403,"prefix":"","suffix":" M$","color":"red","desc":"Retraits du vendredi 6 novembre","logo":"BLK"},"b_at_word":idx(t,"retraits"),"b":{"kicker":"TOUS LES ETF BITCOIN","value_to":-412,"prefix":"","suffix":" M$","color":"white","desc":"Même séance · données Farside"}}])
t="Alors… qui a appuyé sur le bouton panique ?"
beat(t,"Alors... qui a appuyé sur le bouton panique ?",C("B7",2),[{"type":"bigtitle","lines":["QUI A APPUYÉ SUR","LE BOUTON PANIQUE ?"]}])
t="Ce dossier, je le suis en direct sur mon Telegram. Lien en bio."
beat(t,None,{"blur_prev":True},[{"type":"phone","mode":"mini","img":"tg_38e4f34b.jpg","bio_at_word":idx(t,"bio")}],cta="short")
t="Le coupable, c'est l'emploi américain : 165 000 postes créés en octobre, contre 65 000 attendus."
beat(t,"Le coupable... c'est l'emploi américain : cent soixante-cinq mille postes créés en octobre, contre soixante-cinq mille attendus.",
 {"screen":True,"under":C("B9")},
 [{"type":"screen_duo","a":{"kicker":"EMPLOIS CRÉÉS · OCTOBRE","value_to":165000,"prefix":"+","suffix":"","color":"cyan","desc":"États-Unis · chiffre officiel (BLS)"},"b_at_word":idx(t,"contre"),"b":{"kicker":"ATTENDUS","value_to":65000,"prefix":"","suffix":"","color":"white","desc":"Consensus des économistes"}}])
t="Résultat : les marchés voient désormais à 77 % une hausse des taux de la Fed en décembre."
beat(t,"Résultat : les marchés voient désormais à soixante-dix-sept pour cent une hausse des taux de la Fed en décembre.",
 {"screen":True,"under":C("B10")},
 [{"type":"screen_counter","kicker":"HAUSSE DES TAUX EN DÉCEMBRE ?","value_from":0,"value_to":76.8,"decimals":1,"suffix":" %","color":"white","pill":"66,9 % IL Y A UNE SEMAINE","desc":"Probabilité CME FedWatch · réunion des 8 et 9 décembre"}])
t="Et des taux plus hauts, c'est du poison pour les actifs risqués comme le bitcoin."
beat(t,None,{"shots":[C("B11",2),dict(C("B11b",1),at_word=idx(t,"poison"))]},
 [{"type":"bigtitle","lines":["TAUX EN HAUSSE","ACTIFS RISQUÉS EN DANGER"],"at_word":idx(t,"poison")}])
t="Jeudi, Trump Media a même transféré 4 259 bitcoins vers la plateforme Crypto.com."
beat(t,"Jeudi, Trump Média a même transféré plus de quatre mille bitcoins vers la plateforme Crypto point com.",C("B12",2),
 [{"type":"stock","key":"DJT","name":"Trump Media","sub":"4 259 BTC transférés · 5 nov.","y":420,"at_word":idx(t,"Trump")},
  {"type":"news","at_word":idx(t,"bitcoins"),"left":"ACTUALITÉS","right":"ÉTATS-UNIS","tag":"TRUMP MEDIA","headline":"4 259 bitcoins envoyés vers Crypto.com","highlight":"4 259 bitcoins","sub":"Transfert repéré le jeudi 5 novembre"}])
t="Et Strategy, la star du bitcoin en Bourse, risque d'être sortie des indices MSCI mercredi soir."
beat(t,"Et Strategy, la star du bitcoin en Bourse, risque d'être sortie des indices M.S.C.I. mercredi soir.",C("B13",2),
 [{"type":"stock","key":"MSTR","name":"Strategy","sub":"MSTR · Nasdaq","y":420,"at_word":idx(t,"Strategy")},
  {"type":"news","at_word":idx(t,"risque"),"left":"ACTUALITÉS","right":"MSCI","tag":"REVUE DES INDICES","headline":"Strategy candidate à une exclusion","highlight":"exclusion","sub":"Annonce le 11 novembre · effet après le 30 novembre"}])
t="Mais le vrai rendez-vous, c'est mardi à 14 h 30 : l'inflation américaine."
beat(t,"Mais le vrai rendez-vous... c'est mardi à quatorze heures trente : l'inflation américaine.",C("B14",2),
 [{"type":"date","text":"Mardi 10 novembre · 14 h 30 (Paris)"},
  {"type":"bigtitle","lines":["INFLATION US","MARDI · 14 H 30"],"at_word":idx(t,"mardi")}])
t="Rebond vers les 80 000 dollars… ou nouvelle glissade ? Toi, tu paries sur quoi ?"
beat(t,"Rebond vers les quatre-vingt mille dollars... ou nouvelle glissade ? Toi, tu paries sur quoi ?",
 {"shots":[C("B15",1),dict(C("B15b",1),at_word=idx(t,"nouvelle"))]},
 [{"type":"bigtitle","lines":["REBOND…","OU NOUVELLE GLISSADE ?"],"at_word":idx(t,"nouvelle")}])
t="Plus de 22 000 personnes ont déjà une longueur d'avance. Il ne manque que toi. Sur mon canal Telegram gratuit, je décortique chaque jour l'actu géopolitique et financière, avec des analyses d'actions détaillées et mes opportunités en temps réel. Le lien est dans ma bio."
beat(t,"Plus de vingt-deux mille personnes ont déjà une longueur d'avance. Il ne manque que toi. Sur mon canal Telegram gratuit, je décortique chaque jour l'actu géopolitique et financière, avec des analyses d'actions détaillées, et mes opportunités en temps réel. Le lien est dans ma bio.",
 {"blur_prev":True},
 [{"type":"cta_telegram","notif":"Bitcoin, Fed, inflation : le plan de la semaine","imgs":["tg_4b2fa9a8.jpg","tg_38e4f34b.jpg","tg_1eaa56f0.jpg"],"subs":22760,"subs_at_word":idx(t,"22"),"bio_at_word":idx(t,"bio"),"button":"ENTRE DANS LE CANAL"}],
 cta="long",endcard={"duration":1.8,"button":"ENTRE DANS LE CANAL","small":"Telegram gratuit · lien en bio"})
spec={"id":"ep04_bitcoin_75k","date_label":"8 novembre 2026","brand":"Invest Family Fr","hook_type":"logowall","cta_type":"notif_scroll",
 "voice":{"engine":"hedra","voice":"Clément 2","voice_id":"voice_ed52485f-b64d-4dc4-8080-0847ae629dad","model":"elevenlabs-v3","speed":1.08,"stability":0.5},
 "beats":B,"sources":["https://journalducoin.com/bitcoin/bitcoin-75000-dollars-plus-bas-11-semaines","https://secureshift.io/blog/crypto-market-today-november-7-2026-weekly-recap","https://cryptoticker.io/en/crypto-news-this-week-recap-key-dates-november-2026/","https://cryptoactu.com/lecture-marche-2026-11-07/","https://cryptoticker.io/fr/cours-ethereum-2000-euros-sorties-etf-7-novembre-2026/"]}
json.dump(spec,open('/home/claude/kit/episodes/ep04_bitcoin_75k/spec.json','w'),ensure_ascii=False,indent=1)
says=[b.get("say",b["text"]) for b in B]
open('/home/claude/kit/episodes/ep04_bitcoin_75k/full_say.txt','w').write("\n".join(says))
print(len(B), sum(len(s.split()) for s in says))
