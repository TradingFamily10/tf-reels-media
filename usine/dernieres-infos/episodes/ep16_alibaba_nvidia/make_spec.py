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
MS = "MarketScreener (Dow Jones) · 12 nov. 2026"
INV = "Investing.com · 12 nov. 2026"

t = "Ce n'est pas Pékin qui a fait plonger Alibaba de près de 7 %. C'est… le scandale Nvidia."
beat(t, "Ce n'est pas Pékin qui a fait plonger Alibaba de près de sept pour cent. C'est... le scandale Nvidia.", C("B0"), [
    {"type": "date", "text": "Jeudi 12 novembre 2026 · avant Wall Street", "until_beat": 0},
    {"type": "breaking", "label": "DERNIÈRES INFOS", "lines": ["L'AFFAIRE NVIDIA", "FAIT PLONGER", "LA CHINE"]},
    {"type": "stock", "key": "BABA", "name": "Alibaba", "sub": "Hong Kong · clôture du 12 nov.", "pct": "−6,8 %", "up": False, "size": "big", "y": 1420, "at_word": W(t, "Alibaba")}])
t = "Et ce n'est pas le pire : toute la tech chinoise décroche à Hong Kong."
beat(t, "Et ce n'est pas le pire : toute la tech chinoise décroche à Hong Kong.", {"screen": True, "under": C("B1")}, [
    {"type": "tickers", "title": "HONG KONG · JEUDI", "rows": [
        {"name": "Hang Seng Tech", "pct": "−2,4 %", "at_word": W(t, "tech"), "up": False},
        {"name": "MiniMax", "pct": "−7,8 %", "at_word": W(t, "décroche"), "up": False},
        {"name": "Knowledge Atlas", "pct": "−9,1 %", "at_word": W(t, "Hong"), "up": False}]},
    {"type": "source", "text": MS}])
t = "Clôture à 93,80 dollars de Hong Kong, après une chute de plus de 7 % en séance."
beat(t, "Clôture sous les quatre-vingt-quatorze dollars de Hong Kong... après une chute de plus de sept pour cent en séance.", {"screen": True, "under": C("B2")}, [
    {"type": "screen_counter", "kicker": "ALIBABA · CLÔTURE EN HK$", "value_from": 100.6, "value_to": 93.8, "decimals": 1, "prefix": "", "suffix": " $", "color": "red",
     "pill": "−7,3 % AU PIRE DE LA SÉANCE", "desc": MS, "logo": "BABA"}])
t = "À l'origine : selon le Wall Street Journal, le conseil de Nvidia prépare l'éviction de son patron, Jensen Huang."
beat(t, "À l'origine : selon le Wall Street Journal, le conseil de Nvidia prépare l'éviction de son patron, Jensen Huang.", C("B3"), [
    {"type": "news", "at_word": 2, "left": "WALL STREET JOURNAL", "right": "12 NOV.", "tag": "L'ÉTINCELLE", "headline": "Le conseil de Nvidia préparerait l'éviction de Jensen Huang",
     "highlight": "l'éviction", "sub": "Information de presse, non confirmée · " + INV},
    {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "Crise de gouvernance", "y": 1420, "at_word": W(t, "Nvidia")}])
t = "Dans ce dossier, un nom revient : Megaspeed. Une société de Singapour qui aurait fourni du calcul Nvidia… à Alibaba."
beat(t, "Dans ce dossier, un nom revient : Mégaspide. Une société de Singapour qui aurait fourni du calcul Nvidia... à Alibaba.", {"screen": True, "under": C("B4")}, [
    {"type": "news", "at_word": 6, "left": "SINGAPOUR", "right": "12 NOV.", "tag": "LE LIEN", "headline": "Megaspeed aurait fourni de la puissance de calcul Nvidia à Alibaba",
     "highlight": "Megaspeed", "sub": "Selon le WSJ · lien non vérifié · " + MS},
    {"type": "stock", "key": "BABA", "name": "Alibaba", "sub": "Client présumé de Megaspeed", "y": 1420, "at_word": W(t, "Alibaba")}])
t = "Alors, pourquoi un scandale américain fait-il trembler la Chine ?"
beat(t, "Alors... pourquoi un scandale américain fait-il trembler la Chine ?", C("B5"), [
    {"type": "bigtitle", "lines": ["POURQUOI LA CHINE", "TREMBLE ?"], "at_word": 1}])
t = "Cette affaire, je la suis heure par heure sur mon Telegram. Lien en bio."
beat(t, None, {"blur_prev": True}, [{"type": "phone", "mode": "mini", "img": "tg_3435c02c.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "Parce qu'à Washington, des élus réclament déjà de serrer encore les exportations de puces vers la Chine."
beat(t, "Parce qu'à Washington, des élus réclament déjà de serrer encore les exportations de puces vers la Chine.", C("B7"), [
    {"type": "news", "at_word": 1, "left": "WASHINGTON", "right": "12 NOV.", "tag": "LA MENACE", "headline": "Des élus américains réclament des restrictions plus dures sur les puces vendues à la Chine",
     "highlight": "restrictions plus dures", "sub": MS}])
t = "Pékin a aussitôt répondu : pas question que ce scandale serve de prétexte."
beat(t, "Pékin a aussitôt répondu : pas question que ce scandale serve de prétexte.", C("B8"), [
    {"type": "bigtitle", "lines": ["PÉKIN RIPOSTE :", "PAS DE PRÉTEXTE"], "at_word": 0},
    {"type": "source", "text": "Bloomberg, via " + INV}])
t = "À Wall Street, l'onde de choc arrive : les contrats sur le Nasdaq 100 reculent de près de 1 %."
beat(t, "À Wall Street, l'onde de choc arrive : les contrats sur le Nasdaq cent reculent de près d'un pour cent.", {"screen": True, "under": C("B9")}, [
    {"type": "screen_counter", "kicker": "CONTRATS NASDAQ 100", "value_from": 0, "value_to": 0.9, "decimals": 1, "prefix": "− ", "suffix": " %", "color": "red",
     "pill": "≈ −240 POINTS", "desc": "À 9 h 09 (Paris) · " + INV}])
t = "Nvidia a déjà perdu plus de 6 % après la clôture. Alibaba, 4 % à New York."
beat(t, "Nvidia a déjà perdu plus de six pour cent après la clôture. Alibaba, quatre pour cent à New York.", C("B10"), [
    {"type": "tickers", "title": "AVANT WALL STREET", "rows": [
        {"name": "Nvidia (soir)", "pct": "−6 %", "at_word": W(t, "Nvidia"), "key": "NVDA", "up": False},
        {"name": "Alibaba (NY)", "pct": "−4,2 %", "at_word": W(t, "Alibaba"), "key": "BABA", "up": False}]},
    {"type": "source", "text": INV + " · MarketScreener"}])
t = "Un analyste estime que Nvidia pourrait perdre un quart de sa valeur si son patron partait."
beat(t, "Un analyste estime que Nvidia pourrait perdre un quart de sa valeur... si son patron partait.", {"screen": True, "under": C("B11")}, [
    {"type": "screen_counter", "kicker": "NVIDIA · SCÉNARIO DU PIRE", "value_from": 0, "value_to": 25, "decimals": 0, "prefix": "− ", "suffix": " %", "color": "red",
     "pill": "HYPOTHÈSE D'ANALYSTE", "desc": "Si Jensen Huang quittait Nvidia · " + INV, "logo": "NVDA"}])
t = "En toile de fond : le taux américain à 10 ans colle aux 5 %, et même l'or recule."
beat(t, "En toile de fond : le taux américain à dix ans colle aux cinq pour cent... et même l'or recule.", {"screen": True, "under": C("B12")}, [
    {"type": "screen_duo", "a": {"kicker": "TAUX US À 10 ANS", "value_to": 5.00, "decimals": 2, "suffix": " %", "color": "red", "desc": "Investing.com"},
     "b_at_word": W(t, "l'or"), "b": {"kicker": "OR · ONCE", "value_to": 1.2, "decimals": 1, "prefix": "− ", "suffix": " %", "color": "red", "desc": "≈ 3 950 $ · Investing.com"}},
    {"type": "source", "text": INV + " · Yahoo Finance"}])
t = "La suite arrive vite : ce soir Cisco et Applied Materials, mardi Nvidia, mercredi Alibaba."
beat(t, "La suite arrive vite : ce soir, Cisco et Applied Materials... mardi, Nvidia... mercredi, Alibaba.", {"screen": True, "under": C("B13")}, [
    {"type": "date", "text": "Résultats : jeu. 12/11 soir · mar. 17/11 · mer. 18/11"},
    {"type": "tickers", "title": "LES RÉSULTATS À SURVEILLER", "rows": [
        {"name": "Cisco · ce soir", "pct": "12/11", "at_word": W(t, "Cisco"), "key": "CSCO", "up": True},
        {"name": "Applied Materials · ce soir", "pct": "12/11", "at_word": W(t, "Applied"), "key": "AMAT", "up": True},
        {"name": "Nvidia", "pct": "17/11", "at_word": W(t, "Nvidia"), "key": "NVDA", "up": True},
        {"name": "Alibaba", "pct": "18/11", "at_word": W(t, "Alibaba"), "key": "BABA", "up": True}]}])
t = "Alors, ce scandale va-t-il rallumer la guerre des puces ? Dis-le-moi en commentaire."
beat(t, "Alors... ce scandale va-t-il rallumer la guerre des puces ? Dis-le-moi en commentaire.", C("B14"), [
    {"type": "bigtitle", "lines": ["GUERRE DES PUCES :", "LE RETOUR ?"], "at_word": 4}])
t = "Une info comme celle-là, il faut l'avoir le matin, pas trois jours après. Sur mon Telegram gratuit, plus de 22 000 personnes reçoivent l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées et mes opportunités en temps réel. Entre dans le canal : lien en bio."
beat(t, "Une info comme celle-là, il faut l'avoir le matin... pas trois jours après. Sur mon Telegram gratuit, plus de vingt-deux mille personnes reçoivent l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées, et mes opportunités en temps réel. Entre dans le canal : lien en bio.",
     {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Alibaba plonge : l'affaire Nvidia déborde sur la Chine",
     "imgs": ["tg_1eaa56f0.jpg", "tg_38e4f34b.jpg", "tg_4b2fa9a8.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
    cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})

B = [b for i, b in enumerate(B) if i not in (11, 12)]  # retirés pour tenir 70-85 s
d = os.path.dirname(os.path.abspath(__file__))
cp = os.path.join(d, "clips.json")
clips = json.load(open(cp)) if os.path.exists(cp) else {}
def sub(bg):
    if isinstance(bg, dict):
        if "clip" in bg and bg["clip"] in clips: bg.update(clips[bg["clip"]])
        if "under" in bg: sub(bg["under"])
        for s in bg.get("shots", []): sub(s)
for b in B: sub(b["bg"])
spec = {"id": "ep16_alibaba_nvidia", "date_label": "12 novembre 2026", "brand": "Invest Family Fr", "hook_type": "breaking", "hook_formula": "coupable inattendu",
        "cta_angle": "Une info comme celle-là, il faut l'avoir le matin, pas trois jours après", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.marketscreener.com/news/alibaba-shares-fall-as-nvidia-turmoil-stokes-chip-access-fears-ce785ed8da8df225",
                    "https://www.investing.com/news/economy-news/nvidia-said-to-preparing-huang-ouster-alibaba-slumps--whats-moving-markets-5020685",
                    "https://uk.finance.yahoo.com/news/nasdaq-futures-fall-nvidia-leadership-100447985.html",
                    "https://finance.yahoo.com/markets/stocks/articles/us-stock-futures-decline-nvidia-100323595.html",
                    "https://sg.finance.yahoo.com/news/live/stock-market-today-thursday-november-12-sp-500-nasdaq-dow-nvidia-invest-110027430.html"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
open(os.path.join(d, "voice_text.txt"), "w").write("\n".join(b.get("say") or b["text"] for b in B))
