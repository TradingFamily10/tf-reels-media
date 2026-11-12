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


t = "Tout le monde regardait l'inflation. Le vrai danger pour Nvidia était… dans sa propre salle du conseil."
beat(t, "Tout le monde regardait l'inflation... Le vrai danger pour Nvidia était... dans sa propre salle du conseil.", C("B0"), [
    {"type": "date", "text": "Jeudi 12 novembre 2026 · avant l'ouverture", "until_beat": 1},
    {"type": "news", "at_word": 0, "left": "NVIDIA", "right": "ÉTATS-UNIS", "tag": "COUP DE TONNERRE",
     "headline": "Le conseil de Nvidia envisagerait d'écarter son patron, Jensen Huang", "highlight": "écarter son patron", "sub": "Wall Street Journal · soir du 11 nov."}])
t = "Et ce n'est pas le pire : après la clôture, l'action a plongé de 8 %, à 160 dollars."
beat(t, "Et ce n'est pas le pire : après la clôture, l'action a plongé de huit pour cent... à cent soixante dollars.", {"screen": True, "under": C("B1")}, [
    {"type": "screen_counter", "kicker": "NVIDIA · APRÈS LA CLÔTURE", "value_from": 0, "value_to": 8, "decimals": 0, "prefix": "− ", "suffix": " %", "color": "red",
     "pill": "≈ 160 $", "desc": "Jusqu'à −10 % au plus bas · Saxo · StockTitan", "logo": "NVDA"}])
t = "Quelques minutes plus tôt, elle finissait pourtant la séance en hausse de près de 3 %."
beat(t, "Quelques minutes plus tôt, elle finissait pourtant la séance en hausse de près de trois pour cent.", C("B2"), [
    {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "Clôture · mercredi 11 novembre · 173,73 $", "pct": "+2,9 %", "up": True, "size": "big", "y": 1420, "at_word": W(t, "hausse")},
    {"type": "source", "text": "Yahoo Finance · 11 nov. 2026"}])
t = "Selon le Wall Street Journal, le conseil se réunit pour décider s'il écarte Jensen Huang, son patron."
beat(t, "Selon le Wall Street Journal, le conseil se réunit pour décider s'il écarte Jensen Huang, son patron.", {"shots": [C("B3"), {**C("B5"), "at_word": W(t, "conseil")}]}, [
    {"type": "news", "at_word": W(t, "Wall"), "left": "WALL STREET JOURNAL", "right": "11 NOV.", "tag": "CONSEIL D'ADMINISTRATION",
     "headline": "Le conseil se réunit pour décider s'il écarte Jensen Huang", "highlight": "écarte Jensen Huang", "sub": "Rapporté par Yahoo Finance · CNBC · Saxo"}])
t = "Le New York Times évoque une deuxième relation cachée, cette fois avec une dirigeante du groupe."
beat(t, "Le New York Times évoque une deuxième relation cachée... cette fois avec une dirigeante du groupe.", C("B4"), [
    {"type": "news", "at_word": W(t, "New"), "left": "NEW YORK TIMES", "right": "11 NOV.", "tag": "RÉVÉLATIONS",
     "headline": "Une deuxième relation cachée, avec une dirigeante de Nvidia", "highlight": "deuxième relation", "sub": "D'après Yahoo Finance · Saxo · 11 nov. 2026"},
    {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "NVDA · Nasdaq · après-Bourse", "pct": "−8 %", "up": False, "y": 1440, "at_word": W(t, "dirigeante")}])
t = "Et Bloomberg affirme que le conseil cherche déjà un remplaçant… peut-être un patron par intérim."
beat(t, "Et Bloomberg affirme que le conseil cherche déjà un remplaçant... peut-être un patron par intérim.", C("B10"), [
    {"type": "bigtitle", "lines": ["UN PATRON", "PAR INTÉRIM ?"], "at_word": W(t, "intérim")},
    {"type": "source", "text": "Bloomberg, cité par Saxo · 12 nov. 2026"}])
t = "Alors, qui d'autre va payer l'addition ?"
beat(t, "Alors... qui d'autre va payer l'addition ?", C("B6"), [
    {"type": "bigtitle", "lines": ["QUI VA PAYER", "L'ADDITION ?"], "at_word": W(t, "qui")}])
t = "Cette crise, je la suis heure par heure sur mon Telegram. Lien en bio."
beat(t, None, {"blur_prev": True}, [
    {"type": "phone", "mode": "mini", "img": "tg_3435c02c_top.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "Premier touché : CoreWeave, qui loue des puces Nvidia aux géants de l'IA."
beat(t, "Premier touché : CoreWeave... qui loue des puces Nvidia aux géants de l'I.A.", C("B8"), [
    {"type": "stock", "key": "CRWV", "name": "CoreWeave", "sub": "CRWV · Nasdaq · cloud de l'IA", "size": "big", "y": 560, "at_word": W(t, "CoreWeave")},
    {"type": "source", "text": "StockTitan · Yahoo Finance"}])
t = "Mercredi, il venait de s'envoler de près de 25 %, sa meilleure séance depuis juin 2025."
beat(t, "Mercredi, il venait de s'envoler de près de vingt-cinq pour cent... sa meilleure séance depuis juin deux mille vingt-cinq.", {"screen": True, "under": C("B9")}, [
    {"type": "screen_counter", "kicker": "COREWEAVE · SÉANCE DU 11/11", "value_from": 0, "value_to": 24.7, "decimals": 1, "prefix": "+ ", "suffix": " %", "color": "green",
     "pill": "RECORD DEPUIS JUIN 2025", "desc": "Clôture 60,77 $ · Yahoo Finance · Saxo", "logo": "CRWV"}])
t = "Cette nuit, les contrats sur le Nasdaq 100 reculent de près de 1 %."
beat(t, "Cette nuit, les contrats sur le Nasdaq cent reculent de près d'un pour cent.", {"screen": True, "under": C("B11")}, [
    {"type": "tickers", "title": "CONTRATS À TERME · CETTE NUIT", "rows": [
        {"name": "Nasdaq 100 · futures", "pct": "−0,9 %", "at_word": W(t, "Nasdaq"), "up": False},
        {"name": "S&P 500 · futures", "pct": "−0,4 %", "at_word": W(t, "reculent"), "up": False},
        {"name": "Nvidia · après-Bourse", "pct": "−8 %", "at_word": W(t, "1"), "key": "NVDA", "up": False}]},
    {"type": "source", "text": "Saxo · Yahoo Finance · 12 nov. 2026"}])
t = "À Tokyo, la Bourse tient bon, mais SoftBank, grand parieur de l'IA, perd 2 %."
beat(t, "À Tokyo, la Bourse tient bon... mais SoftBank, grand parieur de l'I.A., perd deux pour cent.", C("B12"), [
    {"type": "tickers", "title": "TOKYO · JEUDI MATIN", "rows": [
        {"name": "Nikkei 225", "pct": "+0,1 %", "at_word": W(t, "Tokyo"), "up": True},
        {"name": "SoftBank Group", "pct": "−2 %", "at_word": W(t, "SoftBank"), "key": "SFTBY", "up": False}]},
    {"type": "source", "text": "TradingKey · 12 nov. 2026"}])
t = "Et la Fed n'aide pas : une hausse des taux en décembre est jugée probable à 90 %."
beat(t, "Et la Fed n'aide pas : une hausse des taux en décembre est jugée probable à quatre-vingt-dix pour cent.", {"screen": True, "under": C("B13")}, [
    {"type": "screen_duo", "a": {"kicker": "TAUX US À 10 ANS", "value_to": 4.99, "decimals": 2, "suffix": " %", "color": "red", "desc": "Juste sous les 5 % · Saxo"},
     "b_at_word": W(t, "hausse"), "b": {"kicker": "HAUSSE EN DÉCEMBRE", "value_to": 90, "decimals": 0, "prefix": "≈ ", "suffix": " %", "color": "gold", "desc": "Probabilité · CME FedWatch"}},
    {"type": "source", "text": "StockTitan · CME FedWatch · 11 nov. 2026"}])
t = "Depuis début novembre, Nvidia a perdu environ 14 %… près de 700 milliards de dollars."
beat(t, "Depuis début novembre, Nvidia a perdu environ quatorze pour cent... près de sept cents milliards de dollars.", {"screen": True, "under": C("B14")}, [
    {"type": "screen_logos", "kicker": "VALEUR EFFACÉE EN NOVEMBRE", "value_from": 0, "value_to": 700, "decimals": 0, "prefix": "≈ ", "suffix": " Md$", "color": "red",
     "pill": "≈ −14 % CE MOIS-CI", "keys": ["NVDA"], "desc": "Yahoo Finance · 11 nov. 2026"}])
t = "Prochain rendez-vous : mardi 17 novembre, les résultats. Mais avec quel patron aux commandes ?"
beat(t, "Prochain rendez-vous : mardi dix-sept novembre, les résultats... Mais avec quel patron aux commandes ?", C("B15"), [
    {"type": "date", "text": "Résultats Nvidia : mardi 17 novembre"},
    {"type": "bigtitle", "lines": ["QUEL PATRON", "LE 17/11 ?"], "at_word": W(t, "patron")}])
t = "Alors : Nvidia sans Jensen Huang, coup dur… ou nouveau départ ? Dis-le-moi en commentaire."
beat(t, "Alors : Nvidia sans Jensen Huang, coup dur... ou nouveau départ ? Dis-le-moi en commentaire.", C("B16"), [
    {"type": "bigtitle", "lines": ["COUP DUR OU", "NOUVEAU DÉPART ?"], "at_word": W(t, "coup")}])
t = "Ce que je viens de te montrer, mes abonnés l'ont lu avant tout le monde. Sur mon Telegram gratuit, plus de 22 000 personnes reçoivent l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées et mes opportunités en temps réel. Lien en bio."
beat(t, "Ce que je viens de te montrer, mes abonnés l'ont lu avant tout le monde. Sur mon Telegram gratuit, plus de vingt-deux mille personnes reçoivent l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées, et mes opportunités en temps réel. Lien en bio.",
     {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Nvidia : le conseil peut-il vraiment écarter Jensen Huang ?",
     "imgs": ["tg_1eaa56f0.jpg", "tg_3435c02c_top.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "ACCÈS GRATUIT"}],
    cta="long", endcard={"duration": 1.8, "button": "ACCÈS GRATUIT", "small": "Telegram gratuit · lien en bio"})
d = os.path.dirname(os.path.abspath(__file__))
clips = json.load(open(os.path.join(d, "clips.json")))
def sub(bg):
    if isinstance(bg, dict):
        if "clip" in bg and bg["clip"] in clips: bg.update(clips[bg["clip"]])
        if "under" in bg: sub(bg["under"])
        for s in bg.get("shots", []): sub(s)
for b in B: sub(b["bg"])
spec = {"id": "ep14_nvidia_conseil", "date_label": "12 novembre 2026", "brand": "Invest Family Fr", "hook_type": "headline", "hook_formula": "personne n'en parle", "cta_angle": "Ce que je viens de te montrer, mes abonnés l'ont lu avant tout le monde", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.stocktitan.net/articles/stock-market-today-live-november-11-2026",
 "https://finance.yahoo.com/markets/live/stock-market-today-wednesday-november-11-dow-sp-500-nasdaq-nvidia-treasurys-veterans-day-140638547.html",
 "https://www.home.saxo/en-mena/content/articles/macro/asia-market-quick-take--12-november-2026-12112026",
 "https://www.tradingkey.com/analysis/stocks/more/262301592-japan-korea-stocks-skhy-kospi-nikkei-samsung-skhynix-softbank-kioxia-nvda-nvidia-tradingkey"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
open(os.path.join(d, "voice_text.txt"), "w").write("\n".join(b.get("say") or b["text"] for b in B))
