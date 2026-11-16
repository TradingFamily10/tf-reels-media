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
RT = "Cabinet Office via Reuters (The Star) · 16 nov. 2026"
BG = "Cabinet Office via BigGo Finance · 16 nov. 2026"
IL = "investingLive · 16 nov. 2026"

t = "Tout le monde attend Nvidia. Mais cette nuit, le vrai signal d'alarme est venu du Japon."
beat(t, "Tout le monde attend Nvidia. Mais cette nuit... le vrai signal d'alarme est venu du Japon.", {"shots": [C("B0"), {**C("B0b"), "at_word": W(t, "signal")}]}, [
    {"type": "date", "text": "Lundi 16 novembre 2026 · Tokyo", "until_beat": 0},
    {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "NVDA · Nasdaq · résultats le 17 nov.", "y": 560, "at_word": W(t, "Nvidia"), "until_word": W(t, "signal")},
    {"type": "breaking", "label": "DERNIÈRES INFOS", "lines": ["CETTE NUIT", "LE JAPON", "RECULE"]}])
t = "La quatrième économie du monde a reculé cet été. Une première depuis un an."
beat(t, "La quatrième économie du monde a reculé cet été. Une première... depuis un an.", {"screen": True, "under": C("B1")}, [
    {"type": "screen_counter", "kicker": "PIB JAPON · JUIL.-SEPT. 2026", "value_from": 0, "value_to": 0.1, "decimals": 1, "prefix": "− ", "suffix": " %",
     "color": "red", "pill": "1RE CONTRACTION EN 4 TRIMESTRES", "desc": "Rythme annualisé · " + RT}])
t = "Les économistes attendaient une hausse. Le chiffre tombe dans le rouge."
beat(t, "Les économistes attendaient une hausse. Le chiffre tombe... dans le rouge.", {"screen": True, "under": C("B2")}, [
    {"type": "screen_duo",
     "a": {"kicker": "ATTENDU", "value_to": 0.3, "decimals": 1, "prefix": "+ ", "suffix": " %", "color": "green", "desc": "Médiane du sondage Reuters"},
     "b_at_word": W(t, "chiffre"),
     "b": {"kicker": "PUBLIÉ", "value_to": 0.1, "decimals": 1, "prefix": "− ", "suffix": " %", "color": "red", "desc": "PIB annualisé · " + RT}}])
t = "Et ce n'est pas le pire : les Japonais dépensent moins, pour le deuxième trimestre d'affilée."
beat(t, "Et ce n'est pas le pire : les Japonais dépensent moins... pour le deuxième trimestre d'affilée.", {"screen": True, "under": C("B3")}, [
    {"type": "screen_counter", "kicker": "CONSOMMATION · T3 2026", "value_from": 0, "value_to": 0.3, "decimals": 1, "prefix": "− ", "suffix": " %",
     "color": "red", "pill": "2E BAISSE D'AFFILÉE", "desc": "Plus de la moitié du PIB · " + BG}])
t = "Riz, climatiseurs, vêtements : même le panier du quotidien recule."
beat(t, "Riz, climatiseurs, vêtements : même le panier du quotidien... recule.", C("B4"), [
    {"type": "bigtitle", "lines": ["RIZ, CLIM,", "VÊTEMENTS"], "at_word": 0},
    {"type": "source", "text": BG}])
t = "En face, les importations grimpent, gonflées par le pétrole et l'aluminium."
beat(t, "En face, les importations grimpent... gonflées par le pétrole et l'aluminium.", C("B5"), [
    {"type": "ticket", "at_word": W(t, "importations"), "title": "JAPON · T3 2026", "subtitle": "Variation sur le trimestre · Cabinet Office",
     "rows": [["Consommation", "−0,3 %"], ["Exportations", "−0,2 %"], ["Importations", "+2,5 %"]],
     "total": ["PIB annualisé", "−0,1 %"]},
    {"type": "source", "text": BG}])
t = "Résultat : le commerce extérieur ampute la croissance de 0,6 point."
beat(t, "Résultat : le commerce extérieur ampute la croissance... de plus d'un demi-point.", {"screen": True, "under": C("B6")}, [
    {"type": "screen_counter", "kicker": "COMMERCE EXTÉRIEUR · PIB", "value_from": 0, "value_to": 0.6, "decimals": 1, "prefix": "− ", "suffix": " pt",
     "color": "red", "pill": "LES ÉCONOMISTES ATTENDAIENT − 0,4 PT", "desc": RT}])
t = "Alors, qui va devoir bouger le premier ?"
beat(t, "Alors... qui va devoir bouger le premier ?", C("B7"), [
    {"type": "bigtitle", "lines": ["QUI BOUGE", "LE PREMIER ?"], "at_word": 0}])
t = "Les marchés d'Asie, je les décrypte chaque matin sur mon Telegram. Lien en bio."
beat(t, "Les marchés d'Asie, je les décrypte chaque matin sur mon Telegram. Lien en bio.", C("B8"), [
    {"type": "phone", "mode": "mini", "img": "tg_3435c02c_top.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "Réponse : la Banque du Japon. Elle a déjà monté ses taux en juin, puis en septembre."
beat(t, "Réponse : la Banque du Japon. Elle a déjà monté ses taux en juin... puis en septembre.", C("B9"), [
    {"type": "news", "at_word": W(t, "Banque"), "left": "BANQUE DU JAPON", "right": "2026", "tag": "TAUX",
     "headline": "La Banque du Japon a relevé ses taux en juin et en septembre", "highlight": "relevé ses taux", "sub": "Reuters (The Star) · 16 nov. 2026"}])
t = "Fin octobre, un de ses membres réclamait déjà une nouvelle hausse. Seul contre huit."
beat(t, "Fin octobre, un de ses membres réclamait déjà une nouvelle hausse. Seul... contre huit.", {"screen": True, "under": C("B10")}, [
    {"type": "screen_vote", "kicker": "VOTE DU 30 OCTOBRE 2026", "groups": [{"n": 8, "label": "TAUX À 1,25 %", "color": "gold"}, {"n": 1, "label": "HAUSSE À 1,5 %", "color": "red"}],
     "desc": "3e désaccord d'affilée de Naoki Takata · " + IL}])
t = "Prochain rendez-vous : les 17 et 18 décembre. Les économistes y voient une hausse à 1,5 %."
beat(t, "Prochain rendez-vous : les dix-sept et dix-huit décembre. Les économistes y voient une hausse... à un et demi pour cent.", {"screen": True, "under": C("B11")}, [
    {"type": "screen_counter", "kicker": "BANQUE DU JAPON · 17-18 DÉC.", "value_from": 1.25, "value_to": 1.5, "decimals": 2, "prefix": "", "suffix": " %",
     "color": "gold", "pill": "SCÉNARIO DU SONDAGE REUTERS", "desc": IL}])
t = "Mais le vrai coup dur est ailleurs : selon le FMI, le Japon glisserait au sixième rang mondial en 2027."
beat(t, "Mais le vrai coup dur est ailleurs : selon le F.M.I., le Japon glisserait au sixième rang mondial... en deux mille vingt-sept.", C("B12"), [
    {"type": "bigtitle", "lines": ["4E → 6E", "ÉCONOMIE EN 2027"], "at_word": W(t, "sixième")},
    {"type": "source", "text": "Projection du FMI, PIB nominal en dollars · Reuters (The Star) · 16 nov. 2026"}])
t = "Doublé par l'Inde, puis par le Royaume-Uni."
beat(t, "Doublé par l'Inde... puis par le Royaume-Uni.", {"shots": [C("B13"), {**C("B13b"), "at_word": W(t, "Royaume")}]}, [
    {"type": "bigtitle", "lines": ["INDE", "ROYAUME-UNI"], "at_word": W(t, "Inde")},
    {"type": "source", "text": "FMI via Reuters (The Star) · 16 nov. 2026"}])
t = "Et pendant que l'Asie encaisse, Wall Street attend mardi les comptes de Nvidia."
beat(t, "Et pendant que l'Asie encaisse, Wall Street attend mardi... les comptes de Nvidia.", C("B14"), [
    {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "NVDA · Nasdaq · résultats le 17 nov.", "size": "big", "y": 600, "at_word": W(t, "Wall")},
    {"type": "source", "text": "InsiderFinance · nov. 2026"}])
t = "Alors, le Japon peut-il encore monter ses taux sans casser sa croissance ? Dis-le-moi en commentaire."
beat(t, "Alors... le Japon peut-il encore monter ses taux sans casser sa croissance ? Dis-le-moi en commentaire.", C("B15"), [
    {"type": "bigtitle", "lines": ["MONTER LES TAUX", "SANS TOUT CASSER ?"], "at_word": W(t, "taux")}])
t = "Chaque nuit, pendant que tu dors, l'Asie fait bouger les marchés. Moi, je veille : sur mon canal Telegram gratuit, l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées et les opportunités en temps réel. Plus de 22 000 personnes y sont déjà. Lien en bio."
beat(t, "Chaque nuit, pendant que tu dors, l'Asie fait bouger les marchés. Moi, je veille : sur mon canal Telegram gratuit, l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées et les opportunités en temps réel. Plus de vingt-deux mille personnes y sont déjà. Lien en bio.",
     {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Japon : le PIB recule, la Banque du Japon sous pression",
     "imgs": ["tg_3435c02c_top.jpg", "tg_1eaa56f0.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
    cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})
d = os.path.dirname(os.path.abspath(__file__))
clips = json.load(open(os.path.join(d, "clips.json"))) if os.path.exists(os.path.join(d, "clips.json")) else {}
def sub(bg):
    if isinstance(bg, dict):
        if "clip" in bg and bg["clip"] in clips: bg.update(clips[bg["clip"]])
        if "under" in bg: sub(bg["under"])
        for s in bg.get("shots", []): sub(s)
for b in B: sub(b["bg"])
spec = {"id": "ep25_japon_recul", "date_label": "16 novembre 2026", "brand": "Invest Family Fr", "hook_type": "breaking", "hook_formula": "personne n'en parle",
        "cta_angle": "Chaque nuit, pendant que tu dors, l'Asie fait bouger les marchés. Moi, je veille", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.thestar.com.my/business/business-news/2026/11/16/japan039s-economy-unexpectedly-shrinks-in-july-september-as-consumption-falters",
                    "https://finance.biggo.com/news/4a06c79e-a90f-4681-9939-d5e7a80e19ff",
                    "https://www.local10.com/business/2026/11/15/japans-economy-contracts-slightly-in-the-latest-quarter-as-oil-prices-remain-high/",
                    "https://www.swingfish.trade/blog/market-news/economic-and-event-calendar-in-asia-monday-november-16-2026-boj-china-data-japan-gdp-442235/",
                    "https://www.insiderfinance.io/news/nvidia-stock-nov-17-earnings"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
open(os.path.join(d, "voice_text.txt"), "w").write("\n".join(b.get("say") or b["text"] for b in B))
