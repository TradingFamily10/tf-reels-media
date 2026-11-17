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
QZ = "AFP via Quartz · 16 nov. 2026"
EB = "Eurasia Business News · 16 nov. 2026"
NV = "Communiqué Nvidia · 12 nov. 2026"
TR = "TipRanks · 16 nov. 2026"

t = "Ce n'est pas Nvidia qui a le plus chuté lundi à Wall Street. C'est Micron : −7,6 %."
beat(t, "Ce n'est pas Nvidia qui a le plus chuté lundi à Wall Street... C'est Micron : presque moins huit pour cent.", {"screen": True, "under": C("B0")}, [
    {"type": "date", "text": "Lundi 16 novembre 2026 · Wall Street", "until_beat": 1},
    {"type": "screen_logos", "kicker": "MICRON · SÉANCE DU 16 NOV.", "value_from": 0, "value_to": -7.62, "decimals": 2, "prefix": "", "suffix": " %", "color": "red",
     "pill": "PIRE QUE NVIDIA", "keys": ["MU", "NVDA", "AMD", "AVGO"], "desc": QZ}])
t = "Et ce n'est pas le pire : le Nasdaq a perdu 2,5 % en une seule séance."
beat(t, "Et ce n'est pas le pire : le Nasdaq a perdu deux pour cent et demi... en une seule séance.", {"screen": True, "under": C("B1")}, [
    {"type": "screen_counter", "kicker": "NASDAQ · CLÔTURE 16 NOV.", "value_from": 0, "value_to": -2.49, "decimals": 2, "prefix": "", "suffix": " %", "color": "red",
     "pill": "24 509 POINTS", "desc": QZ + " · " + EB}])
t = "Le S&P 500 recule de près de 2 %. Le Dow Jones lâche plus de 700 points."
beat(t, "Le S. and P. cinq cents recule de près de deux pour cent. Le Dow Jones lâche plus de sept cents points.", {"screen": True, "under": C("B2")}, [
    {"type": "screen_duo",
     "a": {"kicker": "S&P 500", "value_to": -1.92, "decimals": 2, "prefix": "", "suffix": " %", "color": "red", "desc": "7 416 points · " + EB},
     "b_at_word": W(t, "Dow"),
     "b": {"kicker": "DOW JONES", "value_to": -739, "decimals": 0, "prefix": "", "suffix": " pts", "color": "red", "desc": "51 608 points · " + EB}}])
t = "Dans les puces, c'est la déroute : AMD −5,6 %, Broadcom −3,9 %, Nvidia −4,1 %."
beat(t, "Dans les puces, c'est la déroute : A.M.D. presque moins six pour cent, Broadcom moins quatre, Nvidia aussi.", C("B3"), [
    {"type": "tickers", "title": "PUCES · LUNDI 16 NOV.", "rows": [
        {"name": "AMD", "pct": "−5,58 %", "at_word": W(t, "AMD"), "key": "AMD", "up": False},
        {"name": "Broadcom", "pct": "−3,92 %", "at_word": W(t, "Broadcom"), "key": "AVGO", "up": False},
        {"name": "Nvidia", "pct": "−4,12 %", "at_word": W(t, "Nvidia"), "key": "NVDA", "up": False}]},
    {"type": "source", "text": QZ}])
t = "Nvidia termine à 156 dollars, cinq jours après le départ de Jensen Huang."
beat(t, "Nvidia termine à cent cinquante-six dollars, cinq jours après le départ de Jensen Huang.", C("B4"), [
    {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "NVDA · 156,14 $ · −4,12 %", "y": 560, "at_word": 0},
    {"type": "source", "text": EB + " · " + NV}])
t = "Et ce soir, le géant publie ses résultats… avec une dirigeante par intérim, Colette Kress."
beat(t, "Et ce soir, le géant publie ses résultats... avec une dirigeante par intérim, Colette Kress.", C("B5"), [
    {"type": "news", "at_word": W(t, "soir"), "left": "NVIDIA · NASDAQ", "right": "17 NOV.", "tag": "RÉSULTATS",
     "headline": "Résultats du 3e trimestre ce mardi, Colette Kress PDG par intérim", "highlight": "ce mardi", "sub": NV}])
t = "Alors, qui a vraiment déclenché cette chute ?"
beat(t, "Alors... qui a vraiment déclenché cette chute ?", C("B6"), [
    {"type": "bigtitle", "lines": ["QUI A DÉCLENCHÉ", "LA CHUTE ?"], "at_word": W(t, "qui")}])
t = "Les résultats de ce soir, je les décortique en direct sur mon Telegram. Lien en bio."
beat(t, None, C("B7"), [
    {"type": "phone", "mode": "mini", "img": "tg_3435c02c.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "Le coupable vient de Washington : une nouvelle autorisation obligatoire pour exporter des puces américaines."
beat(t, None, C("B8"), [
    {"type": "news", "at_word": W(t, "Washington"), "left": "WASHINGTON · COMMERCE", "right": "16 NOV.", "tag": "PUCES",
     "headline": "Nouvelle autorisation exigée pour exporter des semi-conducteurs américains", "highlight": "autorisation exigée", "sub": QZ + " · " + EB}])
t = "Le but : couper l'accès de la Chine aux puces américaines, même via des data centers à l'étranger."
beat(t, "Le but : couper l'accès de la Chine aux puces américaines... même via des data centers à l'étranger.", {"shots": [C("B9"), {**C("B9b"), "at_word": W(t, "data")}]}, [
    {"type": "bigtitle", "lines": ["LA CHINE", "DANS LE VISEUR"], "at_word": W(t, "Chine")},
    {"type": "source", "text": EB}])
t = "Malaisie, Thaïlande, Indonésie, Singapour, Brésil : cinq pays sous licence."
beat(t, "Malaisie, Thaïlande, Indonésie, Singapour, Brésil : cinq pays... sous licence.", {"screen": True, "under": C("B10")}, [
    {"type": "screen_counter", "kicker": "NOUVELLES RESTRICTIONS", "value_from": 0, "value_to": 5, "decimals": 0, "prefix": "", "suffix": " pays", "color": "gold",
     "pill": "LICENCE OBLIGATOIRE", "desc": "Malaisie · Thaïlande · Indonésie · Singapour · Brésil · " + EB}])
t = "Résultat : l'indice de la peur, le VIX, bondit d'environ 19 %."
beat(t, "Résultat : l'indice de la peur, le V.I.X., bondit d'environ dix-neuf pour cent.", {"screen": True, "under": C("B11")}, [
    {"type": "screen_counter", "kicker": "VIX · INDICE DE LA PEUR", "value_from": 0, "value_to": 19, "decimals": 0, "prefix": "+", "suffix": " %", "color": "red",
     "pill": "EN UNE SÉANCE", "desc": "Environ · CNN via " + EB}])
t = "Premier rendez-vous : ce soir, vers 22 h 20, heure de Paris. Puis jeudi, l'entrée en Bourse d'Anthropic."
beat(t, "Premier rendez-vous : ce soir, vers vingt-deux heures vingt, heure de Paris. Puis jeudi... l'entrée en Bourse d'Anthropic.", C("B13"), [
    {"type": "tickers", "title": "LES DATES À SURVEILLER", "rows": [
        {"name": "Nvidia · résultats", "pct": "MAR. 22H20", "at_word": W(t, "soir"), "key": "NVDA", "up": True},
        {"name": "Anthropic · entrée en Bourse", "pct": "JEU. 19/11", "at_word": W(t, "jeudi"), "up": True}]},
    {"type": "source", "text": NV + " · " + QZ + " · " + TR}])
t = "Alors, simple trou d'air… ou début d'une vraie correction des puces ? Dis-le en commentaire."
beat(t, "Alors... simple trou d'air... ou début d'une vraie correction des puces ? Dis-le en commentaire.", C("B14"), [
    {"type": "bigtitle", "lines": ["TROU D'AIR", "OU CORRECTION ?"], "at_word": W(t, "trou")}])
t = "Quand Wall Street tremble, tout se joue sur l'info. Sur mon canal Telegram gratuit : l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées et les opportunités en temps réel. Plus de 22 000 personnes nous ont déjà rejoints. Lien en bio."
beat(t, "Quand Wall Street tremble... tout se joue sur l'info. Sur mon canal Telegram gratuit : l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées et les opportunités en temps réel. Plus de vingt-deux mille personnes nous ont déjà rejoints. Lien en bio.", {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Nasdaq −2,5 % : les puces décrochent avant Nvidia",
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
spec = {"id": "ep28_puces_micron", "date_label": "17 novembre 2026", "brand": "Invest Family Fr", "hook_type": "logowall", "hook_formula": "coupable inattendu",
        "cta_angle": "Quand Wall Street tremble, tout se joue sur l'info", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://fr.qz.com/wall-street-cloture-baisse-nasdaq-nvidia-anthropic-111626",
 "https://eurasiabusinessnews.com/2026/11/17/stock-market-today-nasdaq-slides-2-5-as-nvidia-turmoil-and-chip-restrictions-hit-tech/",
 "https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition",
 "https://nvidianews.nvidia.com/news/nvidia-sets-conference-call-for-third-quarter-financial-results-6928873",
 "https://www.tipranks.com/news/stock-market-today-nov-16-u-s-stocks-mixed-ahead-of-nvidia-results-and-anthropic-ipo"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
open(os.path.join(d, "voice_text.txt"), "w").write("\n".join(b.get("say") or b["text"] for b in B))
