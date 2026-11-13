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
FF = "FinanceFeeds · 13 nov. 2026"
AJ = "Al Jazeera · 13 nov. 2026"
TK = "TradingKey · 13 nov. 2026"

t = "Plus de 100 milliards de dollars envolés… à cause d'une boîte mail."
beat(t, "Plus de cent milliards de dollars envolés... à cause d'une boîte mail.", {"shots": [C("B0"), {**C("B0b"), "at_word": W(t, "cause")}]}, [
    {"type": "date", "text": "Vendredi 13 novembre 2026 · avant Wall Street", "until_beat": 0},
    {"type": "news", "at_word": 0, "left": "MICROSOFT 365", "right": "12-13 NOV.", "tag": "PANNE MONDIALE",
     "headline": "Outlook, Teams et Copilot tombent en panne dans le monde entier", "highlight": "en panne", "sub": "Al Jazeera · FinanceFeeds · TradingKey"},
    {"type": "stock", "key": "MSFT", "name": "Microsoft", "sub": "Avant-Bourse, vendredi", "pct": "−2,77 %", "up": False, "y": 1440, "at_word": W(t, "boîte")}])
t = "Et ce n'est pas le pire : la panne dure depuis plus de 12 heures."
beat(t, "Et ce n'est pas le pire : la panne dure depuis plus de douze heures.", C("B1"), [
    {"type": "bigtitle", "lines": ["PLUS DE 12 H", "DE PANNE"], "at_word": W(t, "dure")},
    {"type": "source", "text": AJ + " · " + TK}])
t = "Outlook, Teams, Copilot : touchés dans 74 pays."
beat(t, "Outlook, Teams, Copilot : touchés dans soixante-quatorze pays.", {"screen": True, "under": C("B2")}, [
    {"type": "screen_counter", "kicker": "PAYS ET TERRITOIRES TOUCHÉS", "value_from": 0, "value_to": 74, "decimals": 0, "suffix": "", "color": "gold",
     "pill": "OUTLOOK · TEAMS · COPILOT", "desc": "Signalements Downdetector · " + AJ, "logo": "MSFT"}])
t = "Au pic, des dizaines de milliers de signalements, rien que pour Outlook."
beat(t, "Au pic, des dizaines de milliers de signalements... rien que pour Outlook.", {"screen": True, "under": C("B3")}, [
    {"type": "screen_counter", "kicker": "SIGNALEMENTS OUTLOOK AU PIC", "value_from": 0, "value_to": 138000, "decimals": 0, "suffix": "", "color": "red",
     "pill": "JEUDI ≈ 13 H (NEW YORK)", "desc": "Downdetector · " + TK, "logo": "MSFT"}])
t = "Même des États sont coupés : le Japon, Singapour, la Cour suprême des Philippines."
beat(t, "Même des États sont coupés : le Japon... Singapour... la Cour suprême des Philippines.", {"shots": [C("B4"), {**C("B4b"), "at_word": W(t, "Singapour")}, {**C("B4c"), "at_word": W(t, "Cour")}]}, [
    {"type": "news", "at_word": W(t, "Japon"), "left": "ADMINISTRATIONS TOUCHÉES", "right": "12-13 NOV.", "tag": "ASIE",
     "headline": "Le gouvernement japonais, l'agence tech de Singapour et la Cour suprême des Philippines perturbés", "highlight": "Cour suprême", "sub": "AP via " + FF}])
t = "Microsoft l'assure : aucune trace de cyberattaque."
beat(t, "Microsoft l'assure : aucune trace de cyberattaque.", C("B5"), [
    {"type": "news", "at_word": W(t, "assure"), "left": "MICROSOFT · SUR X", "right": "12 NOV.", "tag": "CITATION",
     "headline": "« Aucun signe d'une activité malveillante ou d'une cyberattaque »", "highlight": "cyberattaque", "sub": "Charles Lamanna, vice-président exécutif · " + AJ},
    {"type": "stock", "key": "MSFT", "name": "Microsoft", "sub": "Un changement réseau annulé", "y": 1440, "at_word": W(t, "trace")}])
t = "Alors, qui paie la note… et qui en profite ?"
beat(t, "Alors... qui paie la note... et qui en profite ?", C("B6"), [
    {"type": "bigtitle", "lines": ["QUI PAIE ?", "QUI EN PROFITE ?"], "at_word": W(t, "qui")}])
t = "Cette panne, je la suis en direct sur mon Telegram. Lien en bio."
beat(t, None, {"blur_prev": True}, [
    {"type": "phone", "mode": "mini", "img": "tg_4b2fa9a8.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "Avant Wall Street, Microsoft recule de près de 3 %. Environ 108 milliards de dollars effacés."
beat(t, "Avant Wall Street, Microsoft recule de près de trois pour cent. Environ cent huit milliards de dollars effacés.", {"screen": True, "under": C("B8")}, [
    {"type": "screen_counter", "kicker": "MICROSOFT · AVANT-BOURSE", "value_from": 523.00, "value_to": 508.51, "decimals": 2, "suffix": " $", "color": "red",
     "pill": "−2,77 % · ≈ 108 MD$", "desc": "Clôture jeudi : 523,00 $ · " + FF, "logo": "MSFT"}])
t = "Le plus fou ? Jeudi, en pleine panne, l'action avait fini dans le vert."
beat(t, "Le plus fou ? Jeudi, en pleine panne, l'action avait fini dans le vert.", {"screen": True, "under": C("B9")}, [
    {"type": "screen_duo", "a": {"kicker": "JEUDI · CLÔTURE", "value_to": 0.36, "decimals": 2, "prefix": "+ ", "suffix": " %", "color": "green", "desc": "523,00 $", "logo": "MSFT"},
     "b_at_word": W(t, "vert"), "b": {"kicker": "VENDREDI · AVANT-BOURSE", "value_to": 2.77, "decimals": 2, "prefix": "− ", "suffix": " %", "color": "red", "desc": "508,51 $", "logo": "MSFT"}},
    {"type": "source", "text": FF + " · " + TK}])
t = "Pendant ce temps, Alphabet, maison mère de Google Workspace, grimpe d'environ 1 %."
beat(t, "Pendant ce temps, Alphabet, maison mère de Google Workspace, grimpe d'environ un pour cent.", C("B10"), [
    {"type": "tickers", "title": "AVANT-BOURSE · 13 NOV.", "rows": [
        {"name": "Microsoft", "pct": "−2,77 %", "at_word": W(t, "Pendant"), "key": "MSFT", "up": False},
        {"name": "Alphabet", "pct": "+0,98 %", "at_word": W(t, "Alphabet"), "key": "GOOGL", "up": True},
        {"name": "Nvidia", "pct": "+2,8 %", "at_word": W(t, "grimpe"), "key": "NVDA", "up": True}]},
    {"type": "source", "text": FF + " · Stocktwits"}])
t = "Et Cisco bat les attentes… mais perd quand même près de 3 %."
beat(t, "Et Cisco bat les attentes... mais perd quand même près de trois pour cent.", C("B11"), [
    {"type": "stock", "key": "CSCO", "name": "Cisco", "sub": "CA 18,5 Md$ vs 18,14 attendus", "pct": "−2,7 %", "up": False, "size": "big", "y": 1440, "at_word": W(t, "Cisco")},
    {"type": "source", "text": "Stocktwits via Yahoo Finance · 13 nov. 2026"}])
t = "En Europe, ça relance un vieux débat : dépendre des géants américains du numérique."
beat(t, "En Europe, ça relance un vieux débat : dépendre des géants américains du numérique.", C("B12"), [
    {"type": "news", "at_word": W(t, "débat"), "left": "SOUVERAINETÉ NUMÉRIQUE", "right": "FRANCE", "tag": "LE DÉBAT",
     "headline": "Sébastien Lecornu veut que l'administration lâche Zoom et les outils de visio américains", "highlight": "outils de visio américains", "sub": AJ}])
t = "Le problème ? Pour l'instant, aucune alternative européenne vraiment crédible."
beat(t, "Le problème ? Pour l'instant... aucune alternative européenne vraiment crédible.", C("B13"), [
    {"type": "bigtitle", "lines": ["AUCUNE ALTERNATIVE", "EUROPÉENNE ?"], "at_word": W(t, "aucune")},
    {"type": "source", "text": "Walter Pasquarelli, expert IA · " + AJ}])
t = "Prochaine étape : le rapport d'incident promis par Microsoft. Et mardi 17, les résultats de Nvidia."
beat(t, "Prochaine étape : le rapport d'incident promis par Microsoft. Et mardi dix-sept, les résultats de Nvidia.", {"screen": True, "under": C("B14")}, [
    {"type": "date", "text": "Résultats Nvidia : mardi 17 novembre"},
    {"type": "screen_logos", "kicker": "JOURS AVANT LES RÉSULTATS NVIDIA", "value_from": 0, "value_to": 4, "decimals": 0, "suffix": "", "color": "gold",
     "pill": "MARDI 17 NOVEMBRE", "keys": ["MSFT", "NVDA", "GOOGL"], "desc": "Rapport d'incident Microsoft attendu après rétablissement · " + FF}])
t = "Alors : simple panne… ou vraie faille dans le cloud ? Dis-le-moi en commentaire."
beat(t, "Alors : simple panne... ou vraie faille dans le cloud ? Dis-le-moi en commentaire.", C("B15"), [
    {"type": "bigtitle", "lines": ["SIMPLE PANNE", "OU VRAIE FAILLE ?"], "at_word": W(t, "simple")}])
t = "Quand tout tombe en panne, mon Telegram, lui, reste allumé. Plus de 22 000 personnes y reçoivent gratuitement l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées et mes opportunités en temps réel. Lien en bio."
beat(t, "Quand tout tombe en panne, mon Telegram, lui, reste allumé. Plus de vingt-deux mille personnes y reçoivent gratuitement l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées, et mes opportunités en temps réel. Lien en bio.",
     {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Panne Microsoft : ce que ça change pour les marchés",
     "imgs": ["tg_1eaa56f0.jpg", "tg_3435c02c_top.jpg", "tg_38e4f34b.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
    cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})
d = os.path.dirname(os.path.abspath(__file__))
clips = json.load(open(os.path.join(d, "clips.json"))) if os.path.exists(os.path.join(d, "clips.json")) else {}
def sub(bg):
    if isinstance(bg, dict):
        if "clip" in bg and bg["clip"] in clips: bg.update(clips[bg["clip"]])
        if "under" in bg: sub(bg["under"])
        for s in bg.get("shots", []): sub(s)
for b in B: sub(b["bg"])
spec = {"id": "ep18_microsoft_panne", "date_label": "13 novembre 2026", "brand": "Invest Family Fr", "hook_type": "headline", "hook_formula": "chiffre choc", "cta_angle": "Quand tout tombe en panne, mon Telegram, lui, reste allumé", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://financefeeds.com/msft-stock-microsoft-365-outage-day-two/",
 "https://www.aljazeera.com/news/2026/11/13/microsoft-hit-by-global-outages-what-happened-and-why",
 "https://www.tradingkey.com/analysis/stocks/us-stocks/262304391-microsoft-outage-msft-outlook-teams-microsoft-365-tradingkey",
 "https://finance.yahoo.com/markets/stocks/articles/futures-edge-lower-nvda-fallout-110121361.html"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
open(os.path.join(d, "voice_text.txt"), "w").write("\n".join(b.get("say") or b["text"] for b in B))
