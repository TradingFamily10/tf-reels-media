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

t = "Dans 6 jours, Nvidia rend sa copie. Et 430 milliards de dollars se sont déjà évaporés."
beat(t, "Dans six jours, Nvidia rend sa copie... Et quatre cent trente milliards de dollars se sont déjà évaporés.", C("B0"), [
    {"type": "date", "text": "Mercredi 11 novembre 2026 · avant Wall Street", "until_beat": 0},
    {"type": "hook_bignum", "value_to": 430, "unit": "MILLIARDS DE $", "label": "évaporés en 2 séances", "logos": ["NVDA", "NVDA", "NVDA", "NVDA"],
     "reveal_at_word": W(t, "430"), "count_dur": 1.0}])
t = "Et ce n'est pas le pire : en deux séances, l'action a perdu 9,5 %."
beat(t, "Et ce n'est pas le pire : en deux séances, l'action a perdu près de dix pour cent.", {"screen": True, "under": C("B1")}, [
    {"type": "screen_counter", "kicker": "NVIDIA · LUNDI + MARDI", "value_from": 0, "value_to": 9.5, "decimals": 1, "prefix": "− ", "suffix": " %", "color": "red",
     "pill": "2 SÉANCES", "desc": "TokenPost · Reuters · 11 nov. 2026", "logo": "NVDA"}])
t = "En cause : une enquête qui vise son patron… puis une inflation américaine plus forte que prévu."
beat(t, "En cause : une enquête qui vise son patron... puis une inflation américaine plus forte que prévu.", {"shots": [C("B2"), {**C("B2b"), "at_word": W(t, "inflation")}]}, [
    {"type": "news", "at_word": W(t, "enquête"), "left": "NVIDIA", "right": "9-10 NOV.", "tag": "DOUBLE CHOC",
     "headline": "Le patron de Nvidia visé par une enquête, puis une inflation US au-dessus des attentes", "highlight": "enquête", "sub": "Reuters · Finwire · 11 nov. 2026"},
    {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "NVDA · Nasdaq", "pct": "−9,5 %", "up": False, "y": 1440, "at_word": W(t, "inflation")}])
t = "Résultat : le taux américain à 10 ans touche les 5 %, et une hausse de la Fed en décembre est quasi certaine."
beat(t, "Résultat : le taux américain à dix ans touche les cinq pour cent... et une hausse de la Fed en décembre est quasi certaine.", {"screen": True, "under": C("B3")}, [
    {"type": "screen_duo", "a": {"kicker": "TAUX US À 10 ANS", "value_to": 5, "decimals": 0, "prefix": "≈ ", "suffix": " %", "color": "red", "desc": "Remonté jusqu'à 5 % · Upstox"},
     "b_at_word": W(t, "hausse"), "b": {"kicker": "HAUSSE DE 25 PB EN DÉC.", "value_to": 86.5, "decimals": 1, "suffix": " %", "color": "gold", "desc": "Probabilité · CME FedWatch"}},
    {"type": "source", "text": "Upstox · CME FedWatch · 11 nov. 2026"}])
t = "Alors pourquoi, ce matin, la tech américaine repart-elle à l'attaque ?"
beat(t, "Alors... pourquoi, ce matin, la tech américaine repart-elle à l'attaque ?", C("B4"), [
    {"type": "bigtitle", "lines": ["POURQUOI ÇA", "REPART ?"], "at_word": W(t, "pourquoi")}])
t = "Ce bras de fer, je le suis en direct sur mon Telegram. Lien en bio."
beat(t, None, {"blur_prev": True}, [
    {"type": "phone", "mode": "mini", "img": "tg_1eaa56f0.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "Le nom qui a tout rallumé : CoreWeave, qui loue des puces Nvidia aux géants de l'IA."
beat(t, "Le nom qui a tout rallumé : CoreWeave... qui loue des puces Nvidia aux géants de l'I.A.", C("B6"), [
    {"type": "stock", "key": "CRWV", "name": "CoreWeave", "sub": "CRWV · Nasdaq · cloud de l'IA", "size": "big", "y": 560, "at_word": W(t, "CoreWeave")},
    {"type": "source", "text": "Reuters · Upstox · Stocktwits"}])
t = "Au trimestre, ses ventes battent les attentes : 3,66 milliards de dollars, contre 3,55 espérés."
beat(t, "Au trimestre, ses ventes battent les attentes... près de trois milliards sept cents millions de dollars.", {"screen": True, "under": C("B7")}, [
    {"type": "screen_duo", "a": {"kicker": "ATTENDU", "value_to": 3.55, "decimals": 2, "suffix": " Md$", "color": "white", "desc": "Consensus · 3e trimestre", "logo": "CRWV"},
     "b_at_word": W(t, "3,66"), "b": {"kicker": "PUBLIÉ", "value_to": 3.66, "decimals": 2, "suffix": " Md$", "color": "green", "desc": "Chiffre d'affaires T3 2026", "logo": "CRWV"}},
    {"type": "source", "text": "Upstox · 11 nov. 2026"}])
t = "Il relève ses prévisions pour l'année. Et l'action bondit de 16 % avant l'ouverture."
beat(t, "Il relève ses prévisions pour l'année... Et l'action bondit de seize pour cent avant l'ouverture.", C("B8"), [
    {"type": "stock", "key": "CRWV", "name": "CoreWeave", "sub": "Avant-Bourse · mercredi 11 novembre", "pct": "+16 %", "up": True, "size": "big", "y": 1420, "at_word": W(t, "bondit")},
    {"type": "source", "text": "Reuters · Finwire · 11 nov. 2026"}])
t = "Dans son sillage : Nvidia gagne 3 %, Intel 5 %, et le Nasdaq 100 plus de 1,5 %."
beat(t, "Dans son sillage : Nvidia gagne trois pour cent, Intel cinq... et le Nasdaq cent, plus d'un et demi.", {"screen": True, "under": C("B9")}, [
    {"type": "tickers", "title": "AVANT-BOURSE · MERCREDI", "rows": [
        {"name": "Nvidia", "pct": "≈ +3 %", "at_word": W(t, "Nvidia"), "key": "NVDA", "up": True},
        {"name": "Intel", "pct": "+5 %", "at_word": W(t, "Intel"), "key": "INTC"},
        {"name": "Nasdaq 100 · futures", "pct": "+1,6 %", "at_word": W(t, "Nasdaq"), "up": True}]},
    {"type": "source", "text": "TokenPost · Reuters · 11 nov. 2026"}])
t = "Même Michael Burry, le parieur à la baisse, y voit « un sacré coup à jouer »."
beat(t, "Même Michael Burry, le parieur à la baisse, y voit un sacré coup à jouer.", C("B10"), [
    {"type": "news", "at_word": W(t, "Burry"), "left": "MICHAEL BURRY", "right": "11 NOV.", "tag": "LE PARIEUR À LA BAISSE",
     "headline": "Après la chute, Nvidia pourrait devenir « un sacré coup à jouer »", "highlight": "sacré coup à jouer", "sub": "Stocktwits · « a heck of a trade »"},
    {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "NVDA · Nasdaq", "pct": "≈ +3 %", "up": True, "y": 1440, "at_word": W(t, "coup")}])
t = "Mais attention : CoreWeave ne prévoit d'être rentable… qu'en 2028."
beat(t, "Mais attention : CoreWeave ne prévoit d'être rentable... qu'en deux mille vingt-huit.", C("B11"), [
    {"type": "bigtitle", "lines": ["RENTABLE…", "EN 2028"], "at_word": W(t, "rentable")},
    {"type": "source", "text": "Reuters · Finwire · 11 nov. 2026"}])
t = "Et pendant ce temps, un pétrolier aurait heurté une mine près d'Ormuz. Le pétrole remonte."
beat(t, "Et pendant ce temps, un pétrolier aurait heurté une mine près d'Ormuz... Le pétrole remonte.", {"screen": True, "under": C("B13")}, [
    {"type": "screen_counter", "kicker": "BRENT · BARIL", "value_from": 91.5, "value_to": 93.1, "decimals": 1, "suffix": " $", "color": "red",
     "pill": "+1,7 % MERCREDI", "desc": "+42 % sur un an · Upstox · 11 nov. 2026"}])
t = "Prochain verdict : mardi 17 novembre. Nvidia vise 108 milliards de dollars de ventes sur le trimestre."
beat(t, "Prochain verdict : mardi dix-sept novembre. Nvidia vise cent huit milliards de dollars de ventes sur le trimestre.", {"screen": True, "under": C("B14")}, [
    {"type": "date", "text": "Résultats Nvidia : mardi 17 novembre"},
    {"type": "screen_logos", "kicker": "OBJECTIF DE VENTES · TRIMESTRE", "value_from": 0, "value_to": 108, "decimals": 0, "suffix": " Md$", "color": "gold",
     "pill": "± 2 % · PUBLICATION LE 17/11", "keys": ["NVDA"], "desc": "Nvidia · prévision de la société · TIKR"}])
t = "Alors : simple rebond… ou vrai retour de l'IA ? Dis-le-moi en commentaire."
beat(t, "Alors : simple rebond... ou vrai retour de l'I.A. ? Dis-le-moi en commentaire.", C("B15"), [
    {"type": "bigtitle", "lines": ["REBOND", "OU RETOUR ?"], "at_word": W(t, "rebond")}])
t = "La prochaine secousse, tu veux la subir… ou la voir venir ? Sur mon Telegram gratuit, plus de 22 000 personnes reçoivent l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées et mes opportunités en temps réel. Lien en bio."
beat(t, "La prochaine secousse, tu veux la subir... ou la voir venir ? Sur mon Telegram gratuit, plus de vingt-deux mille personnes reçoivent l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées, et mes opportunités en temps réel. Lien en bio.",
     {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Nvidia : le verdict du 17 novembre, décrypté",
     "imgs": ["tg_3435c02c_top.jpg", "tg_1eaa56f0.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
    cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})
d = os.path.dirname(os.path.abspath(__file__))
clips = json.load(open(os.path.join(d, "clips.json")))
def sub(bg):
    if isinstance(bg, dict):
        if "clip" in bg and bg["clip"] in clips: bg.update(clips[bg["clip"]])
        if "under" in bg: sub(bg["under"])
        for s in bg.get("shots", []): sub(s)
for b in B: sub(b["bg"])
spec = {"id": "ep13_nvidia_coreweave", "date_label": "11 novembre 2026", "brand": "Invest Family Fr", "hook_type": "bignum", "hook_formula": "compte à rebours", "cta_angle": "La prochaine secousse, tu veux la subir ou la voir venir ?", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://finwire.io/news/stock-markets-news/premarket-stocks-gain-as-coreweave-reignites-ai-trade",
 "https://stocktwits.com/news-articles/markets/equity/s-and-p-500-nasdaq-futures-rise-premarket-crwv-gpro-spcx-nvda-nlst-stocks-in-focus/cNGDlb9R9B7",
 "https://upstox.com/news/market-news/us-stocks/dow-jones-s-and-p-500-nasdaq-futures-hint-positive-opening-on-nov-11-core-weave-tech-stocks-in-focus/article-203309/",
 "https://www.tokenpost.com/news/investing/53733",
 "https://www.tikr.com/blog/nvidia-sinks-9-as-midterm-data-center-fears-deepen-ai-chip-rout-absolute-slaughter"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
open(os.path.join(d, "voice_text.txt"), "w").write("\n".join(b.get("say") or b["text"] for b in B))
