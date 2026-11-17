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


ST = "StockTwits (13F) · 16 nov. 2026"
CC = "CoinCentral (13F) · 17 nov. 2026"
YF = "Yahoo Finance · 17 nov. 2026"
TR = "TipRanks · 17 nov. 2026"

t = "Tout le monde regarde Nvidia ce soir. Le vrai signal est ailleurs : 130 millions d'actions SpaceX."
beat(t, "Tout le monde regarde Nvidia ce soir... Le vrai signal est ailleurs : cent trente millions d'actions SpaceX.", {"shots": [C("B0"), {**C("B0b"), "at_word": W(t, "signal")}]}, [
    {"type": "date", "text": "Mardi 17 novembre 2026 · Wall Street", "until_beat": 0},
    {"type": "hook_bignum", "value_to": 130, "prefix": "", "suffix": " M", "unit": "D'ACTIONS SPACEX", "label": "Détenues par Nvidia au 30 sept. · déclaration 13F du 16 nov.",
     "logos": ["NVDA", "SPCX", "INTC"], "reveal_at_word": W(t, "130"), "count_dur": 1.0}])
t = "Près de 20 milliards de dollars : c'est désormais sa plus grosse ligne en Bourse, devant Intel."
beat(t, "Près de vingt milliards de dollars : c'est désormais sa plus grosse ligne en Bourse... devant Intel.", {"screen": True, "under": C("B1")}, [
    {"type": "screen_duo",
     "a": {"kicker": "LIGNE SPACEX DE NVIDIA", "value_to": 19.7, "decimals": 1, "prefix": "", "suffix": " Md$", "color": "gold", "desc": "N°1 au 30 sept. · " + ST},
     "b_at_word": W(t, "ligne"),
     "b": {"kicker": "LIGNE INTEL DE NVIDIA", "value_to": 19.4, "decimals": 1, "prefix": "", "suffix": " Md$", "color": "red", "desc": "N°2 · " + CC}}])
t = "Et ce n'est pas le pire pour Intel : Nvidia a vendu un quart de ses actions."
beat(t, "Et ce n'est pas le pire pour Intel : Nvidia a vendu un quart de ses actions.", {"screen": True, "under": C("B2")}, [
    {"type": "screen_counter", "kicker": "ACTIONS INTEL DÉTENUES", "value_from": 0, "value_to": -25, "decimals": 0, "prefix": "", "suffix": " %", "color": "red",
     "pill": "214,8 M → 161,1 M D'ACTIONS", "desc": "3e trimestre 2026 · " + CC},
    {"type": "stock", "key": "INTC", "name": "Intel", "sub": "≈ 30 Md$ fin juin → 19,4 Md$ fin sept.", "y": 1380, "at_word": W(t, "quart")}])
t = "Dans le même temps, Nvidia a ajouté près de 8 millions d'actions SpaceX."
beat(t, "Dans le même temps, Nvidia a ajouté près de huit millions d'actions SpaceX.", {"screen": True, "under": C("B4")}, [
    {"type": "screen_counter", "kicker": "ACTIONS SPACEX ACHETÉES PAR NVIDIA", "value_from": 0, "value_to": 7.7, "decimals": 1, "prefix": "+", "suffix": " M", "color": "green",
     "pill": "122,8 M → 130,5 M D'ACTIONS", "desc": "3e trimestre 2026 · " + CC}])
t = "Alors, pourquoi le roi des puces mise-t-il autant sur la fusée d'Elon Musk ?"
beat(t, "Alors... pourquoi le roi des puces mise-t-il autant sur la fusée d'Elon Musk ?", C("B6"), [
    {"type": "bigtitle", "lines": ["POURQUOI", "SPACEX ?"], "at_word": W(t, "pourquoi")}])
t = "Ces paris des grands fonds, je les décortique en direct sur mon Telegram. Lien en bio."
beat(t, None, C("B7"), [
    {"type": "phone", "mode": "mini", "img": "tg_3435c02c.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "Indice : SpaceX est devenu un gros client de l'I.A. : environ 40 milliards de dollars de puces Nvidia en location."
beat(t, "Indice : SpaceX est devenu un gros client de l'I.A.... environ quarante milliards de dollars de puces Nvidia en location.", {"shots": [C("B8"), {**C("B8b"), "at_word": W(t, "40")}]}, [
    {"type": "news", "at_word": W(t, "40"), "left": "SPACEX · I.A.", "right": "OCTOBRE 2026", "tag": "CONTRAT",
     "headline": "Un engagement de location d'environ 40 milliards de dollars pour des puces Nvidia Vera Rubin", "highlight": "40 milliards de dollars", "sub": "Via une entité gérée par Apollo · " + ST}])
t = "La semaine dernière, SpaceX a présenté plus de 74 milliards de dollars de sites d'I.A. au Texas et en Arizona."
beat(t, "La semaine dernière, SpaceX a présenté plus de soixante-quatorze milliards de dollars de sites d'I.A.... au Texas et en Arizona.", {"screen": True, "under": C("B9")}, [
    {"type": "screen_counter", "kicker": "PROJETS I.A. DE SPACEX", "value_from": 0, "value_to": 74, "decimals": 0, "prefix": "+", "suffix": " Md$", "color": "gold",
     "pill": "TEXAS · ARIZONA", "desc": ST}])
t = "Le gérant David Tepper a multiplié sa ligne SpaceX par plus de 17."
beat(t, "Le gérant David Tepper a multiplié sa ligne SpaceX... par plus de dix-sept.", {"screen": True, "under": C("B10")}, [
    {"type": "screen_duo",
     "a": {"kicker": "APPALOOSA · FIN JUIN", "value_to": 225, "decimals": 0, "prefix": "", "suffix": " 000", "color": "gold", "desc": "Actions SpaceX · " + ST},
     "b_at_word": W(t, "multiplié"),
     "b": {"kicker": "APPALOOSA · FIN SEPT.", "value_to": 3.88, "decimals": 2, "prefix": "", "suffix": " M", "color": "green", "desc": "≈ 556 M$ · " + ST}}])
t = "Mais Citadel, le fonds de Ken Griffin, a fait l'inverse : 95 % de ses actions SpaceX vendues."
beat(t, "Mais Citadel, le fonds de Ken Griffin, a fait l'inverse : quatre-vingt-quinze pour cent de ses actions SpaceX... vendues.", {"screen": True, "under": C("B12")}, [
    {"type": "screen_counter", "kicker": "CITADEL · ACTIONS SPACEX", "value_from": 0, "value_to": -95, "decimals": 0, "prefix": "", "suffix": " %", "color": "red",
     "pill": "5,13 M → 283 822 ACTIONS", "desc": "Fin juin → fin sept. · " + ST}])
t = "En Bourse, SpaceX ne fait pas de miracle : 137 dollars lundi, à peine 2 % au-dessus de son prix d'introduction."
beat(t, "En Bourse, SpaceX ne fait pas de miracle : cent trente-sept dollars lundi... à peine deux pour cent au-dessus de son prix d'introduction.", C("B13"), [
    {"type": "stock", "key": "SPCX", "name": "SpaceX", "sub": "SPCX · 137,36 $ lundi 16 nov. · −1 %", "y": 520, "at_word": W(t, "SpaceX")},
    {"type": "news", "at_word": W(t, "2"), "left": "SPCX · NASDAQ", "right": "16 NOV.", "tag": "BOURSE",
     "headline": "+1,7 % seulement au-dessus du prix d'introduction de juin", "highlight": "+1,7 %", "sub": ST}])
t = "Prochain test ce soir : les résultats de Nvidia, après la clôture de Wall Street."
beat(t, "Prochain test ce soir : les résultats de Nvidia... après la clôture de Wall Street.", C("B14"), [
    {"type": "tickers", "title": "À SURVEILLER CE SOIR", "rows": [
        {"name": "Nvidia · résultats", "pct": "MAR. SOIR", "at_word": W(t, "Nvidia"), "key": "NVDA", "up": True},
        {"name": "SpaceX · réaction", "pct": "À SUIVRE", "at_word": W(t, "clôture"), "key": "SPCX", "up": True},
        {"name": "Intel · réaction", "pct": "À SUIVRE", "at_word": W(t, "Wall"), "key": "INTC", "up": False}]},
    {"type": "source", "text": TR}])
t = "Alors, pari visionnaire ou bulle de l'espace ? Dis-le en commentaire."
beat(t, "Alors... pari visionnaire... ou bulle de l'espace ? Dis-le en commentaire.", C("B15"), [
    {"type": "bigtitle", "lines": ["PARI VISIONNAIRE", "OU BULLE ?"], "at_word": W(t, "visionnaire")}])
t = "Les grands fonds dévoilent leurs paris avec des semaines de retard. Sur mon canal Telegram gratuit : l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées et les opportunités en temps réel. Plus de 22 000 personnes sont déjà là. Lien en bio."
beat(t, "Les grands fonds dévoilent leurs paris avec des semaines de retard. Sur mon canal Telegram gratuit : l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées et les opportunités en temps réel. Plus de vingt-deux mille personnes sont déjà là. Lien en bio.", {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Nvidia mise 20 Md$ sur SpaceX : l'analyse",
     "imgs": ["tg_38e4f34b.jpg", "tg_1eaa56f0.jpg", "tg_4b2fa9a8.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "ACCÈS GRATUIT"}],
    cta="long", endcard={"duration": 1.8, "button": "ACCÈS GRATUIT", "small": "Telegram gratuit · lien en bio"})
d = os.path.dirname(os.path.abspath(__file__))
clips = json.load(open(os.path.join(d, "clips.json"))) if os.path.exists(os.path.join(d, "clips.json")) else {}
def sub(bg):
    if isinstance(bg, dict):
        if "clip" in bg and bg["clip"] in clips: bg.update(clips[bg["clip"]])
        if "under" in bg: sub(bg["under"])
        for s in bg.get("shots", []): sub(s)
for b in B: sub(b["bg"])
spec = {"id": "ep30_spacex_nvidia", "date_label": "17 novembre 2026", "brand": "Invest Family Fr", "hook_type": "bignum", "hook_formula": "personne n'en parle",
        "cta_angle": "Les grands fonds dévoilent leurs paris avec des semaines de retard", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://stocktwits.com/news-articles/markets/equity/spcx-stock-dethrones-intel-nvidia-biggest-holding-druckenmiller-buys-in-tepper-ups-stake/cNba0UWR9gq",
 "https://coincentral.com/nvidia-nvda-stock-spacex-overtakes-intel-as-chipmakers-biggest-disclosed-bet",
 "https://finance.yahoo.com/markets/stocks/articles/us-stock-futures-edge-lower-102414813.html",
 "https://www.tipranks.com/news/stock-market-today-nov-17-u-s-stocks-jittery-ahead-of-nvidia-results"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
open(os.path.join(d, "voice_text.txt"), "w").write("\n".join(b.get("say") or b["text"] for b in B))
