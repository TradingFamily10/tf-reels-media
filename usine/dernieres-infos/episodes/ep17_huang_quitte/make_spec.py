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
ST = "StockTitan · 12 nov. 2026"

t = "Jensen Huang quitte Nvidia. L'action plonge de 14 %… et pourtant, ce sont ses rivaux qui s'envolent."
beat(t, "Jensen Huang quitte Nvidia. L'action plonge de quatorze pour cent... et pourtant, ce sont ses rivaux qui s'envolent.", C("B0"), [
    {"type": "date", "text": "Vendredi 13 novembre 2026 · avant l'Europe", "until_beat": 0},
    {"type": "hook_bignum", "value_to": 14, "prefix": "−", "suffix": " %", "unit": "EN UNE MINUTE", "label": "Nvidia, à l'ouverture jeudi",
     "logos": ["NVDA", "AMD", "AVGO", "NVDA"], "reveal_at_word": W(t, "rivaux"), "count_dur": 1.0}])
t = "Et ce n'est pas le pire : il lâche tout, avec effet immédiat. Patron, président, administrateur."
beat(t, "Et ce n'est pas le pire : il lâche tout, avec effet immédiat. Patron... président... administrateur.", C("B1"), [
    {"type": "news", "at_word": W(t, "lâche"), "left": "NVIDIA · DÉPÔT SEC", "right": "12 NOV.", "tag": "DÉMISSION",
     "headline": "Jensen Huang quitte la direction et le conseil de Nvidia, avec effet immédiat", "highlight": "effet immédiat", "sub": "Annonce à 14 h 48 (Paris) · " + ST},
    {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "Fondateur parti", "y": 1440, "at_word": W(t, "Patron")}])
t = "C'est sa directrice financière, Colette Kress, qui prend la barre par intérim."
beat(t, "C'est sa directrice financière, Colette Kress, qui prend la barre par intérim.", C("B2"), [
    {"type": "bigtitle", "lines": ["NOUVELLE PATRONNE", "PAR INTÉRIM"], "at_word": W(t, "Kress")},
    {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "PDG par intérim : Colette Kress", "y": 1440, "at_word": W(t, "barre")},
    {"type": "source", "text": "StockTitan · Investopedia · 12 nov. 2026"}])
t = "Le motif ? Nvidia n'en donne aucun. Mais depuis une semaine, sa vie privée faisait la une, et le conseil enquêtait."
beat(t, "Le motif ? Nvidia n'en donne aucun. Mais depuis une semaine, sa vie privée faisait la une... et le conseil enquêtait.", C("B3"), [
    {"type": "news", "at_word": W(t, "semaine"), "left": "LE CONTEXTE", "right": "NOV. 2026", "tag": "AUCUN MOTIF OFFICIEL",
     "headline": "Le conseil de Nvidia avait ouvert une enquête après des révélations sur la vie privée de son patron", "highlight": "une enquête", "sub": "Investopedia via Yahoo Finance · 12 nov. 2026"}])
t = "À l'ouverture, l'action tombe à 148,80 dollars. Moins 14 % en une minute."
beat(t, "À l'ouverture, l'action tombe sous les cent cinquante dollars. Moins quatorze pour cent... en une minute.", {"screen": True, "under": C("B4")}, [
    {"type": "screen_counter", "kicker": "NVIDIA · JEUDI 15 H 31 (PARIS)", "value_from": 173.73, "value_to": 148.8, "decimals": 2, "suffix": " $", "color": "red",
     "pill": "−14,35 % AU PIRE", "desc": "Clôture de la veille : 173,73 $ · " + ST, "logo": "NVDA"}])
t = "Alors, comment Nvidia a-t-il pu effacer l'essentiel de cette chute ?"
beat(t, "Alors... comment Nvidia a-t-il pu effacer l'essentiel de cette chute ?", C("B5"), [
    {"type": "bigtitle", "lines": ["COMMENT ÇA", "REMONTE ?"], "at_word": W(t, "comment")}])
t = "Cette saga, je la décortique chaque jour sur mon Telegram. Lien en bio."
beat(t, None, {"blur_prev": True}, [
    {"type": "phone", "mode": "mini", "img": "tg_38e4f34b.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "Clôture à 166,19 dollars. Moins 4 % seulement, après un plongeon de 14."
beat(t, "Clôture au-dessus des cent soixante-six dollars. Moins quatre pour cent seulement... après un plongeon de quatorze.", {"screen": True, "under": C("B7")}, [
    {"type": "screen_duo", "a": {"kicker": "AU PIRE DE LA SÉANCE", "value_to": 14.35, "decimals": 2, "prefix": "− ", "suffix": " %", "color": "red", "desc": "148,80 $ à 15 h 31", "logo": "NVDA"},
     "b_at_word": W(t, "Moins"), "b": {"kicker": "À LA CLÔTURE", "value_to": 4.34, "decimals": 2, "prefix": "− ", "suffix": " %", "color": "gold", "desc": "166,19 $", "logo": "NVDA"}},
    {"type": "source", "text": "Motley Fool · " + ST}])
t = "Les grands gagnants : A.M.D. prend près de 6 %. Broadcom aussi. Le marché parie sur ses concurrents."
beat(t, "Les grands gagnants : A.M.D. prend près de six pour cent. Broadcom aussi. Le marché parie sur ses concurrents.",
     {"shots": [C("B8"), {**C("B8b"), "at_word": W(t, "marché")}]}, [
    {"type": "tickers", "title": "CLÔTURE · JEUDI 12 NOV.", "rows": [
        {"name": "AMD", "pct": "+5,86 %", "at_word": W(t, "A.M.D."), "key": "AMD", "up": True},
        {"name": "Broadcom", "pct": "+5,54 %", "at_word": W(t, "Broadcom"), "key": "AVGO", "up": True},
        {"name": "Nvidia", "pct": "−4,34 %", "at_word": W(t, "concurrents"), "key": "NVDA", "up": False}]},
    {"type": "source", "text": "Motley Fool · 12 nov. 2026"}])
t = "Au total, Wall Street limite la casse : le Nasdaq et le Dow Jones cèdent moins d'un demi pour cent."
beat(t, "Au total, Wall Street limite la casse : le Nasdaq et le Dow Jones cèdent moins d'un demi pour cent.", {"screen": True, "under": C("B9")}, [
    {"type": "tickers", "title": "WALL STREET · JEUDI", "rows": [
        {"name": "Nasdaq", "pct": "−0,39 %", "at_word": W(t, "Nasdaq"), "up": False},
        {"name": "S&P 500", "pct": "−0,36 %", "at_word": W(t, "Dow"), "up": False},
        {"name": "Dow Jones", "pct": "−0,36 %", "at_word": W(t, "Jones"), "up": False}]},
    {"type": "source", "text": "Motley Fool · 12 nov. 2026"}])
t = "Cette nuit en Asie, Tokyo grimpe de plus de 1 %. Hong Kong, lui, recule."
beat(t, "Cette nuit en Asie, Tokyo grimpe de plus d'un pour cent. Hong Kong, lui, recule.", {"screen": True, "under": C("B10")}, [
    {"type": "screen_duo", "a": {"kicker": "NIKKEI · TOKYO", "value_to": 1.4, "decimals": 1, "prefix": "+ ", "suffix": " %", "color": "green", "desc": "≈ 61 650 points"},
     "b_at_word": W(t, "Hong"), "b": {"kicker": "HANG SENG · HONG KONG", "value_to": 0.9, "decimals": 1, "prefix": "− ", "suffix": " %", "color": "red", "desc": "≈ 23 800 points"}},
    {"type": "source", "text": "investingLive · 13 nov. 2026, mi-séance"}])
t = "Et le bitcoin décroche : moins 6 %, sous les 70 000 dollars."
beat(t, "Et le bitcoin décroche : moins six pour cent... sous les soixante-dix mille dollars.", C("B11"), [
    {"type": "stock", "key": "BTC", "name": "Bitcoin", "sub": "Sous 70 000 $ · nuit du 12 au 13 nov.", "pct": "≈ −6 %", "up": False, "size": "big", "y": 1500, "at_word": W(t, "décroche")},
    {"type": "source", "text": "investingLive · 13 nov. 2026"}])
t = "Et mardi 17 novembre, Nvidia publie ses résultats. Sans son fondateur aux commandes."
beat(t, "Et mardi dix-sept novembre, Nvidia publie ses résultats... sans son fondateur aux commandes.", {"screen": True, "under": C("B13")}, [
    {"type": "date", "text": "Résultats Nvidia : mardi 17 novembre"},
    {"type": "screen_logos", "kicker": "JOURS AVANT LES RÉSULTATS", "value_from": 0, "value_to": 4, "decimals": 0, "suffix": "", "color": "gold",
     "pill": "MARDI 17 NOVEMBRE", "keys": ["NVDA", "AMD", "AVGO"], "desc": "Publication maintenue à la date prévue · " + ST}])
t = "Alors : Nvidia sans Jensen Huang, nouvelle ère… ou début du déclin ? Dis-le-moi en commentaire."
beat(t, "Alors : Nvidia sans Jensen Huang... nouvelle ère, ou début du déclin ? Dis-le-moi en commentaire.", C("B14"), [
    {"type": "bigtitle", "lines": ["NOUVELLE ÈRE", "OU DÉCLIN ?"], "at_word": W(t, "nouvelle")}])
t = "Chaque matin, je fais le tri dans le bruit pour toi. Sur mon Telegram gratuit, plus de 22 000 personnes reçoivent l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées et mes opportunités en temps réel. Lien en bio."
beat(t, "Chaque matin, je fais le tri dans le bruit pour toi. Sur mon Telegram gratuit, plus de vingt-deux mille personnes reçoivent l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées, et mes opportunités en temps réel. Lien en bio.",
     {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Nvidia sans Jensen Huang : ce qui change vraiment",
     "imgs": ["tg_3435c02c_top.jpg", "tg_4b2fa9a8.jpg", "tg_38e4f34b.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "REJOINS LA FAMILLE"}],
    cta="long", endcard={"duration": 1.8, "button": "REJOINS LA FAMILLE", "small": "Telegram gratuit · lien en bio"})
d = os.path.dirname(os.path.abspath(__file__))
clips = json.load(open(os.path.join(d, "clips.json"))) if os.path.exists(os.path.join(d, "clips.json")) else {}
def sub(bg):
    if isinstance(bg, dict):
        if "clip" in bg and bg["clip"] in clips: bg.update(clips[bg["clip"]])
        if "under" in bg: sub(bg["under"])
        for s in bg.get("shots", []): sub(s)
for b in B: sub(b["bg"])
spec = {"id": "ep17_huang_quitte", "date_label": "13 novembre 2026", "brand": "Invest Family Fr", "hook_type": "bignum", "hook_formula": "contre-intuitif", "cta_angle": "Chaque matin, je fais le tri dans le bruit pour toi", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.stocktitan.net/articles/stock-market-today-live-november-12-2026",
 "https://www.fool.com/coverage/stock-market-today/2026/11/12/stock-market-today-nov-12-nvidia-ceo-s-stunning-exit-sends-wall-street-lower-as-rivals-surge/",
 "https://finance.yahoo.com/markets/stocks/articles/stock-market-today-nasdaq-p-131805045.html",
 "https://investinglive.com/stock-market-update/asian-stocks-steady-as-nikkei-gains-1-4-hang-seng-slips-on-nvidia-leadership-fallout/"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
open(os.path.join(d, "voice_text.txt"), "w").write("\n".join(b.get("say") or b["text"] for b in B))
