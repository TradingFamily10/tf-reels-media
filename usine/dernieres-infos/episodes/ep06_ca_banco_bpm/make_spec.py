import json, sys, os
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
def W(text, word, n=0):
    t = tokens(text); hits = [i for i, w in enumerate(t) if word in w]
    return hits[n]
B = []
def beat(text, say=None, bg=None, ov=None, **kw):
    b = {"text": text}
    if say: b["say"] = say
    b["bg"] = bg or {}; b["overlays"] = ov or []; b.update(kw); B.append(b); return text
C = lambda clip, ss=1, cx=0.5, **k: dict(clip=clip, ss=ss, cx=cx, **k)

t = "1 milliard d'euros sur la table… et une banque italienne bondit de près de 10 % en une matinée."
beat(t, "Un milliard d'euros sur la table... et une banque italienne bondit de près de dix pour cent en une matinée.",
     C("B0"), [
       {"type": "date", "text": "Lundi 9 novembre 2026", "until_beat": 1},
       {"type": "bigtitle", "lines": ["1 MILLIARD €", "SUR LA TABLE"], "at_word": 0},
       {"type": "stock", "key": "BAMI", "name": "Banco BPM", "sub": "BAMI · Bourse de Milan · ce matin", "pct": "+9,7 %", "up": True, "size": "big", "y": 560, "at_word": W(t, "bondit")}])
t = "Derrière ce coup, une banque bien française."
beat(t, None, C("B1"), [{"type": "stock", "key": "ACA", "name": "Crédit Agricole", "sub": "ACA · Euronext Paris", "size": "big", "y": 560, "at_word": W(t, "française")}])
t = "Ce matin, le Crédit Agricole a proposé de fusionner sa filiale italienne avec Banco BPM."
beat(t, None, C("B2"), [
       {"type": "news", "at_word": W(t, "proposé"), "left": "COMMUNIQUÉ", "right": "ITALIE", "tag": "CRÉDIT AGRICOLE · BANCO BPM",
        "headline": "Le Crédit Agricole propose une fusion à Banco BPM", "highlight": "une fusion", "sub": "Proposition amicale · 9 novembre 2026"},
       {"type": "source", "text": "Communiqué Crédit Agricole · Boursorama"}])
t = "Objectif : le troisième groupe bancaire d'Italie. 6,5 millions de clients, plus de 2 300 agences."
beat(t, "Objectif : le troisième groupe bancaire d'Italie. Six millions et demi de clients... plus de deux mille trois cents agences.",
     {"screen": True, "under": C("B3")}, [
       {"type": "screen_duo", "a": {"kicker": "CLIENTS", "value_to": 6.5, "decimals": 1, "prefix": "", "suffix": " M", "color": "white", "desc": "3e groupe bancaire italien", "logo": "BAMI"},
        "b_at_word": W(t, "plus"), "b": {"kicker": "AGENCES", "value_to": 2300, "prefix": "+ de ", "suffix": "", "color": "gold", "desc": "Partout en Italie", "logo": "ACA"}}])
t = "Pour convaincre : une prime de 20 % et un dividende exceptionnel d'un milliard d'euros."
beat(t, "Pour convaincre : une prime de vingt pour cent... et un dividende exceptionnel d'un milliard d'euros.",
     {"screen": True, "under": C("B4")}, [
       {"type": "screen_counter", "kicker": "DIVIDENDE EXCEPTIONNEL", "value_from": 0, "value_to": 1, "decimals": 0, "suffix": " Md€", "color": "gold",
        "pill": "+ PRIME DE 20 %", "desc": "Pour les actionnaires actuels de Banco BPM", "logo": "BAMI"}])
t = "Il détient déjà 29,6 % de Banco BPM. Demain, ce serait environ 45 %."
beat(t, "Il détient déjà près de trente pour cent de Banco BPM. Demain... ce serait environ quarante-cinq pour cent.",
     {"screen": True, "under": C("B5")}, [
       {"type": "screen_duo", "a": {"kicker": "SA PART AUJOURD'HUI", "value_to": 29.6, "decimals": 1, "prefix": "", "suffix": " %", "color": "white", "desc": "Dans Banco BPM", "logo": "ACA"},
        "b_at_word": W(t, "Demain"), "b": {"kicker": "APRÈS LA FUSION", "value_to": 45, "prefix": "≈ ", "suffix": " %", "color": "green", "desc": "Du nouveau groupe", "logo": "ACA"}}])
t = "Alors… pourquoi maintenant ? Et qui peut encore tout bloquer ?"
beat(t, "Alors... pourquoi maintenant ? Et qui peut encore tout bloquer ?", C("B6"), [
       {"type": "bigtitle", "lines": ["POURQUOI", "MAINTENANT ?"]}])
t = "Ce bras de fer bancaire, je le suis en direct sur mon Telegram. Lien en bio."
beat(t, None, {"blur_prev": True}, [{"type": "phone", "mode": "mini", "img": "tg_38e4f34b.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "Il y a onze jours, les actionnaires de Banco BPM ont dit non à un rival italien. À 91 %."
beat(t, "Il y a onze jours, les actionnaires de Banco BPM ont dit non à un rival italien... À quatre-vingt-onze pour cent.",
     {"shots": [C("B7"), {**C("B7b"), "at_word": W(t, "non")}]}, [
       {"type": "stock", "key": "BAMI", "name": "Banco BPM", "sub": "Offre rivale rejetée · 29 octobre", "pct": "91 % de NON", "size": "big", "y": 560, "at_word": 4},
       {"type": "source", "text": "France Épargne · 9 novembre"}])
t = "Et le timing n'a rien d'un hasard : en Europe, les banques gagnent des fortunes."
beat(t, None, C("B9"), [{"type": "bigtitle", "lines": ["LES BANQUES", "GAGNENT GROS"], "at_word": W(t, "Europe")}])
t = "Ce matin, UniCredit annonce 3,3 milliards d'euros de bénéfice en un seul trimestre. +24 % en un an."
beat(t, "Ce matin, UniCredit annonce plus de trois milliards d'euros de bénéfice en un seul trimestre... Plus vingt-quatre pour cent en un an.",
     {"screen": True, "under": C("B10")}, [
       {"type": "screen_duo", "a": {"kicker": "BÉNÉFICE NET T3", "value_to": 3.3, "decimals": 1, "prefix": "", "suffix": " Md€", "color": "white", "desc": "Juillet à septembre 2026", "logo": "UCG"},
        "b_at_word": W(t, "+24"), "b": {"kicker": "SUR UN AN", "value_to": 24, "prefix": "+", "suffix": " %", "color": "green", "desc": "Au-dessus des attentes", "logo": "UCG"}},
       {"type": "source", "text": "RTÉ · UniCredit, résultats du 3e trimestre"}])
t = "Résultat : à l'ouverture, les banques européennes grimpent."
beat(t, None, C("B11"), [
       {"type": "tickers", "title": "LES BANQUES CE MATIN", "rows": [
          {"name": "Banco BPM", "pct": "+9,7 %", "at_word": 0, "key": "BAMI"},
          {"name": "UniCredit", "pct": "+5,2 %", "at_word": W(t, "banques"), "key": "UCG"},
          {"name": "Crédit Agricole", "pct": "−0,9 %", "at_word": W(t, "grimpent"), "key": "ACA"}]},
       {"type": "source", "text": "Zonebourse · Boursorama · lundi matin"}])
t = "Derrière, un chiffre : l'inflation de la zone euro monte à 4 %, au plus haut depuis trois ans."
beat(t, "Derrière, un chiffre : l'inflation de la zone euro monte à quatre pour cent... au plus haut depuis trois ans.",
     {"screen": True, "under": C("B12")}, [
       {"type": "screen_counter", "kicker": "INFLATION · ZONE EURO", "value_from": 0, "value_to": 4.0, "decimals": 1, "suffix": " %", "color": "red",
        "pill": "OCTOBRE 2026", "desc": "Plus haut depuis trois ans · énergie : +20,8 % sur un an"},
       {"type": "source", "text": "Eurostat (estimation rapide) · Boursorama"}])
t = "Et des taux hauts, c'est du carburant pour les marges des banques."
beat(t, None, C("B13"), [{"type": "bigtitle", "lines": ["TAUX HAUTS", "MARGES GONFLÉES"], "at_word": W(t, "marges")}])
t = "Mais rien n'est joué : il faut le feu vert de la BCE… et de Rome, qui peut tout bloquer."
beat(t, "Mais rien n'est joué : il faut le feu vert de la B.C.E.... et de Rome, qui peut tout bloquer.",
     {"shots": [C("B14"), {**C("B14b"), "at_word": W(t, "Rome")}]}, [
       {"type": "news", "at_word": W(t, "feu"), "left": "CONDITIONS", "right": "ITALIE", "tag": "GOLDEN POWER",
        "headline": "Feu vert de la BCE et de Rome obligatoire", "highlight": "obligatoire", "sub": "Vote des actionnaires de Banco BPM · finalisation visée au 2nd semestre 2027"}])
t = "Coup de maître… ou nouvel échec ? Dis-le-moi en commentaire."
beat(t, "Coup de maître... ou nouvel échec ? Dis-le-moi en commentaire.", {"shots": [C("B15"), {**C("B15b"), "at_word": W(t, "Dis-le-moi")}]}, [
       {"type": "bigtitle", "lines": ["COUP DE MAÎTRE…", "OU NOUVEL ÉCHEC ?"], "at_word": 0}])
t = "La prochaine grande manœuvre, tu veux la subir… ou la voir venir ? Sur mon Telegram gratuit, plus de 22 000 personnes reçoivent l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées et mes opportunités en temps réel. Lien en bio."
beat(t, "La prochaine grande manœuvre, tu veux la subir... ou la voir venir ? Sur mon Telegram gratuit, plus de vingt-deux mille personnes reçoivent l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées, et mes opportunités en temps réel. Lien en bio.",
     {"blur_prev": True}, [
       {"type": "cta_telegram", "notif": "Crédit Agricole, Banco BPM, UniCredit : qui gagne la bataille des banques ?",
        "imgs": ["tg_4b2fa9a8.jpg", "tg_1eaa56f0.jpg", "tg_3435c02c.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
     cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})


# --- durée : on retire 3 phrases (voix brute 92 s) ---
DROP = [8, 11, 13]
tk = [o for o in B[11]["overlays"] if o["type"] == "tickers"][0]
t9 = B[9]["text"]
tk["rows"][0]["at_word"] = W(t9, "Europe"); tk["rows"][1]["at_word"] = W(t9, "banques"); tk["rows"][2]["at_word"] = W(t9, "fortunes")
B[9]["overlays"] = [o for o in B[9]["overlays"] if o["type"] != "bigtitle"] + [tk, {"type": "source", "text": "Zonebourse · Boursorama · lundi matin"}]
B = [b for i, b in enumerate(B) if i not in DROP]
clips = json.load(open(os.path.join(os.path.dirname(__file__), "clips.json"))) if os.path.exists(os.path.join(os.path.dirname(__file__), "clips.json")) else {}
def sub(bg):
    if isinstance(bg, dict):
        if "clip" in bg and bg["clip"] in clips:
            c = clips[bg["clip"]]; bg.update({k: v for k, v in c.items()})
        for k in ("under",):
            if k in bg: sub(bg[k])
        for s in bg.get("shots", []): sub(s)
for b in B: sub(b["bg"])
for b in B:
    sy=(b.get("say") or b["text"])
    if "Banco BPM" in sy: b["say"]=sy.replace("Banco BPM","Banco B.P.M.").replace("B.P.M..","B.P.M.")
spec = {"id": "ep06_ca_banco_bpm", "date_label": "9 novembre 2026", "brand": "Invest Family Fr", "hook_type": "chip", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.globenewswire.com/news-release/2026/11/09/3398046/0/fr/credit-agricole-sa-cr%C3%A9dit-agricole-propose-%C3%A0-banco-bpm-de-cr%C3%A9er-ensemble-un-nouveau-champion-bancaire-italien.html",
                    "https://www.boursorama.com/bourse/actualites/credit-agricole-propose-une-fusion-entre-banco-bpm-et-credit-agricole-italia-9fe33f10b6115541188fe19237c20be2",
                    "https://www.france-epargne.fr/news/credit-agricole-propose-une-fusion-entre-banco-bpm-et-sa-filiale-italienne-avec-une-prime-de-20",
                    "https://www.rte.ie/news/business/2026/1109/1598480-unicredit-posts-24-rise-in-third-quarter-earnings/",
                    "https://www.zonebourse.com/actualite-bourse/l-europe-ouvre-dans-le-vert-l-action-nvidia-souffre-a-francfort-ce785fd3db8af121",
                    "https://www.boursorama.com/bourse/actualites/zone-euro-l-inflation-annuelle-atteint-4-en-octobre-4de7bf40199c62a24dcf263094646a88"],
        "beats": B}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
