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
SF = "Spaceflight Now · 15 nov. 2026"
SC = "Space.com · 15 nov. 2026"
SA = "StockAnalysis · 16 nov. 2026"
TN = "The Next Web · 16 nov. 2026"
TR = "TipRanks · 16 nov. 2026"

t = "Le jour où la fusée de Boeing et Lockheed Martin a perdu 40 satellites d'Amazon… en 10 minutes."
beat(t, "Le jour où la fusée de Boeing et Lockheed Martin a perdu quarante satellites d'Amazon... en dix minutes.", {"shots": [C("B0"), {**C("B0b"), "at_word": W(t, "satellites")}]}, [
    {"type": "date", "text": "Dimanche 15 novembre 2026 · Cap Canaveral", "until_beat": 0},
    {"type": "news", "at_word": 0, "left": "CAP CANAVERAL · ULA", "right": "15 NOV.", "tag": "ÉCHEC",
     "headline": "La fusée Vulcan échoue : les 40 satellites Amazon Leo n'atteignent pas l'orbite", "highlight": "40 satellites Amazon Leo",
     "sub": SF + " · " + SC}])
t = "Dimanche, en Floride, la fusée Vulcan décolle. Dix minutes plus tard : l'anomalie."
beat(t, "Dimanche, en Floride, la fusée Vulcan décolle. Dix minutes plus tard... l'anomalie.", {"shots": [C("B1"), {**C("B1b"), "at_word": W(t, "Dix")}]}, [
    {"type": "bigtitle", "lines": ["T + 10 MIN :", "ANOMALIE"], "at_word": W(t, "Dix")},
    {"type": "source", "text": "Communiqué de ULA · " + SF}])
t = "Et ce n'est pas le pire : c'est le premier échec total de ULA depuis sa création, en 2006."
beat(t, "Et ce n'est pas le pire : c'est le premier échec total de U.L.A. depuis sa création, en deux mille six.", {"screen": True, "under": C("B2")}, [
    {"type": "screen_logos", "kicker": "ULA · BOEING + LOCKHEED MARTIN", "value_from": 0, "value_to": 20, "decimals": 0, "suffix": " ans", "color": "gold",
     "pill": "PREMIER ÉCHEC TOTAL", "keys": ["BA", "LMT"], "desc": "ULA créée en 2006 · " + SF + " · " + SA}])
t = "Ces 40 satellites devaient renforcer Amazon Leo, le réseau internet spatial d'Amazon."
beat(t, "Ces quarante satellites devaient renforcer Amazon Léo, le réseau internet spatial d'Amazon.", C("B3"), [
    {"type": "stock", "key": "AMZN", "name": "Amazon", "sub": "AMZN · Nasdaq", "y": 560, "at_word": W(t, "Amazon")},
    {"type": "source", "text": SC}])
t = "Amazon n'en a qu'environ 400 en orbite. Il lui en faut plus de 3 200."
beat(t, "Amazon n'en a qu'environ quatre cents en orbite. Il lui en faut... plus de trois mille deux cents.", {"screen": True, "under": C("B4")}, [
    {"type": "screen_duo",
     "a": {"kicker": "AMAZON LEO · EN ORBITE", "value_to": 400, "decimals": 0, "prefix": "≈ ", "suffix": "", "color": "gold", "desc": "Avant le vol de dimanche · " + SC},
     "b_at_word": W(t, "faut"),
     "b": {"kicker": "OBJECTIF · 1RE GÉNÉRATION", "value_to": 3200, "decimals": 0, "prefix": "+ de ", "suffix": "", "color": "gold", "desc": SC + " · " + TN}}])
t = "En face, Starlink, le réseau de SpaceX, en aligne déjà plus de 11 000."
beat(t, "En face, Starlink, le réseau de SpaceX, en aligne déjà... plus de onze mille.", {"screen": True, "under": C("B5")}, [
    {"type": "screen_counter", "kicker": "SATELLITES STARLINK", "value_from": 0, "value_to": 11000, "decimals": 0, "prefix": "+ de ", "suffix": "",
     "color": "gold", "pill": "ET DES MILLIONS DE CLIENTS", "desc": SA}])
t = "Alors, qui paie vraiment l'addition de cet échec ?"
beat(t, "Alors... qui paie vraiment l'addition de cet échec ?", C("B6"), [
    {"type": "bigtitle", "lines": ["QUI PAIE", "L'ADDITION ?"], "at_word": W(t, "paie")}])
t = "Cette course à l'espace, je la décrypte en direct sur mon Telegram. Lien en bio."
beat(t, "Cette course à l'espace, je la décrypte en direct sur mon Telegram. Lien en bio.", C("B7"), [
    {"type": "phone", "mode": "mini", "img": "tg_38e4f34b.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "Premier touché : Amazon. Le groupe a réservé 38 vols sur cette fusée… qui reste au sol jusqu'à la fin de l'enquête."
beat(t, "Premier touché : Amazon. Le groupe a réservé trente-huit vols sur cette fusée... qui reste au sol jusqu'à la fin de l'enquête.", {"screen": True, "under": C("B8")}, [
    {"type": "screen_logos", "kicker": "VOLS VULCAN ACHETÉS PAR AMAZON", "value_from": 0, "value_to": 38, "decimals": 0, "suffix": "", "color": "red",
     "pill": "ENQUÊTE EN COURS", "keys": ["AMZN"], "desc": SF + " · " + SA}])
t = "Ce lundi, l'action Amazon recule avant l'ouverture de Wall Street."
beat(t, "Ce lundi, l'action Amazon recule avant l'ouverture de Wall Street.", C("B9"), [
    {"type": "news", "at_word": W(t, "action"), "left": "WALL STREET · AMZN", "right": "16 NOV.", "tag": "AVANT-BOURSE",
     "headline": "L'action Amazon recule après la perte de 40 satellites Leo", "highlight": "recule", "sub": TR}])
t = "Deuxième touché : le Pentagone. Il attendait ce vol pour confier de nouveau ses missions militaires à Vulcan."
beat(t, "Deuxième touché : le Pentagone. Il attendait ce vol pour confier de nouveau ses missions militaires... à Vulcan.", C("B10"), [
    {"type": "bigtitle", "lines": ["LE PENTAGONE", "EN ATTENTE"], "at_word": W(t, "Pentagone")},
    {"type": "source", "text": "Reuters via " + SA}])
t = "Et l'enquête touche aussi Blue Origin : ses moteurs BE-4 font voler Vulcan… et sa propre fusée, New Glenn, au sol depuis mai."
beat(t, "Et l'enquête touche aussi Blue Origin : ses moteurs B.E. quatre font voler Vulcan... et sa propre fusée, New Glenn, au sol depuis mai.", {"shots": [C("B11"), {**C("B11b"), "at_word": W(t, "New")}]}, [
    {"type": "bigtitle", "lines": ["MOTEURS BE-4", "SOUS LA LOUPE"], "at_word": W(t, "moteurs")},
    {"type": "source", "text": "Blue Origin aide l'enquête · " + SF + " · " + TN}])
t = "Prochain test : pas avant le 23 novembre, une Ariane 6 doit emporter 36 satellites Amazon."
beat(t, "Prochain test : pas avant le vingt-trois novembre, une Ariane six doit emporter trente-six satellites Amazon.", C("B12"), [
    {"type": "bigtitle", "lines": ["23 NOVEMBRE :", "ARIANE 6"], "at_word": W(t, "23")},
    {"type": "source", "text": "36 satellites Amazon Leo · GeekWire via " + TN}])
t = "Alors, Amazon peut-il encore rattraper Starlink ? Dis-le-moi en commentaire."
beat(t, "Alors... Amazon peut-il encore rattraper Starlink ? Dis-le-moi en commentaire.", C("B13"), [
    {"type": "bigtitle", "lines": ["AMAZON PEUT-IL", "RATTRAPER STARLINK ?"], "at_word": W(t, "Amazon")}])
t = "La prochaine secousse, tu veux la subir ou la voir venir ? Sur mon canal Telegram gratuit : l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées et les opportunités en temps réel. Plus de 22 000 personnes y sont déjà. Lien en bio."
beat(t, "La prochaine secousse, tu veux la subir... ou la voir venir ? Sur mon canal Telegram gratuit : l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées et les opportunités en temps réel. Plus de vingt-deux mille personnes y sont déjà. Lien en bio.",
     {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Vulcan : 40 satellites Amazon perdus en 10 minutes",
     "imgs": ["tg_4b2fa9a8.jpg", "tg_3435c02c_top.jpg", "tg_1eaa56f0.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
    cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})
DROP = set(json.loads(os.environ.get("DROP", "[]")))
B[:] = [b for i, b in enumerate(B) if i not in DROP]
d = os.path.dirname(os.path.abspath(__file__))
clips = json.load(open(os.path.join(d, "clips.json"))) if os.path.exists(os.path.join(d, "clips.json")) else {}
def sub(bg):
    if isinstance(bg, dict):
        if "clip" in bg and bg["clip"] in clips: bg.update(clips[bg["clip"]])
        if "under" in bg: sub(bg["under"])
        for s in bg.get("shots", []): sub(s)
for b in B: sub(b["bg"])
spec = {"id": "ep27_vulcan_amazon", "date_label": "16 novembre 2026", "brand": "Invest Family Fr", "hook_type": "headline", "hook_formula": "le jour où",
        "cta_angle": "La prochaine secousse, tu veux la subir ou la voir venir ?", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://spaceflightnow.com/2026/11/15/ula-suffers-first-total-mission-failure-with-loss-of-vulcan-rocket-carrying-40-amazon-leo-satellites/",
 "https://www.space.com/space-exploration/launches-spacecraft/ula-vulcan-centaur-return-to-flight-amazon-leo-internet-satellite-launch",
 "https://stockanalysis.com/news/ula-vulcan-rocket-fails-amazon-leo-satellites-lost/",
 "https://thenextweb.com/news/vulcan-rocket-failure-amazon-leo-satellites-ula",
 "https://www.tipranks.com/news/stock-market-today-nov-16-u-s-stocks-mixed-ahead-of-nvidia-results-and-anthropic-ipo"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
open(os.path.join(d, "voice_text.txt"), "w").write("\n".join(b.get("say") or b["text"] for b in B))
