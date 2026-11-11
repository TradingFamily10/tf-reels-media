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


t = "Même matin, même secteur : Siemens Energy bondit de près de 8 %… Vestas plonge de près de 9 %."
beat(t, "Même matin, même secteur : Siemens Energy bondit de près de huit pour cent... Vestas plonge de près de neuf pour cent.", C("B0"), [
    {"type": "date", "text": "Mercredi 11 novembre 2026 · Francfort · Copenhague", "until_beat": 0},
    {"type": "breaking", "label": "DERNIÈRES INFOS", "lines": ["LE GAZ S'ENVOLE", "LE VENT", "S'EFFONDRE"]},
    {"type": "tickers", "title": "ÉNERGIE · MERCREDI MATIN", "rows": [
        {"name": "Siemens Energy", "pct": "+7,9 %", "at_word": W(t, "Siemens"), "key": "ENR"},
        {"name": "Vestas", "pct": "−8,7 %", "at_word": W(t, "Vestas"), "key": "VWS", "down": True}]}])
t = "Et ce n'est pas le pire pour l'éolien : les commandes de Vestas reculent, à 4,1 milliards d'euros."
beat(t, "Et ce n'est pas le pire pour l'éolien : les commandes de Vestas reculent, à un peu plus de quatre milliards d'euros.", {"screen": True, "under": C("B1")}, [
    {"type": "screen_duo", "a": {"kicker": "COMMANDES T3 2025", "value_to": 4.6, "decimals": 1, "suffix": " Md€", "color": "gold", "desc": "Vestas · un an plus tôt"},
     "b_at_word": W(t, "reculent"), "b": {"kicker": "COMMANDES T3 2026", "value_to": 4.1, "decimals": 1, "suffix": " Md€", "color": "red", "desc": "3 377 MW contre 4 606 MW"}},
    {"type": "source", "text": "Vestas · rapport du 3e trimestre · RTTNews · 11 nov."}])
t = "Pourtant, Vestas a vendu plus : 5,68 milliards d'euros au trimestre. Mais le marché en attendait 6."
beat(t, "Pourtant, Vestas a vendu plus : près de cinq milliards sept cents millions d'euros au trimestre. Mais le marché en attendait six.", {"screen": True, "under": C("B2")}, [
    {"type": "screen_duo", "a": {"kicker": "ATTENDU", "value_to": 6.0, "decimals": 1, "suffix": " Md€", "color": "gold", "desc": "Consensus · chiffre d'affaires T3"},
     "b_at_word": W(t, "Mais"), "b": {"kicker": "PUBLIÉ", "value_to": 5.68, "decimals": 2, "suffix": " Md€", "color": "red", "desc": "+6 % sur un an · encore raté"}},
    {"type": "source", "text": "Investing.com · Sweden Herald (TT) · 11 nov."}])
t = "Le coupable : un chantier éolien en mer, en Europe, qui coûte bien plus cher que prévu."
beat(t, None, {"shots": [C("B3"), {**C("B3b"), "at_word": W(t, "coûte")}]}, [
    {"type": "news", "at_word": W(t, "coupable"), "left": "VESTAS", "right": "11 NOV.", "tag": "ÉOLIEN EN MER",
     "headline": "Résultat du trimestre sous les attentes, plombé par des coûts en hausse sur un projet offshore européen", "highlight": "projet offshore européen", "sub": "Boursorama · Investing.com"},
    {"type": "stock", "key": "VWS", "name": "Vestas", "sub": "VWS · Copenhague · à l'ouverture", "pct": "−8,7 %", "up": False, "y": 1420, "at_word": W(t, "chantier")}])
t = "En face, Siemens Energy affiche un carnet de commandes record : 164 milliards d'euros."
beat(t, "En face, Siemens Energy affiche un carnet de commandes record : cent soixante-quatre milliards d'euros.", {"screen": True, "under": C("B4")}, [
    {"type": "screen_logos", "kicker": "CARNET DE COMMANDES · RECORD", "value_from": 0, "value_to": 164, "decimals": 0, "suffix": " Md€", "color": "green",
     "pill": "AU 30 SEPTEMBRE 2026", "keys": ["ENR"], "desc": "Siemens Energy · exercice 2026 · France Épargne · Boursorama"}])
t = "Plus de trois ans et demi de chiffre d'affaires… déjà signés."
beat(t, None, C("B5"), [
    {"type": "bigtitle", "lines": ["3 ANS ET DEMI", "DÉJÀ SIGNÉS"], "at_word": 1}])
t = "Alors, qui achète toutes ces machines ?"
beat(t, "Alors... qui achète toutes ces machines ?", C("B6"), [
    {"type": "bigtitle", "lines": ["QUI ACHÈTE", "TOUT ÇA ?"], "at_word": 1}])
t = "Ce genre de bascule, je la décortique en direct sur mon Telegram. Lien en bio."
beat(t, None, {"blur_prev": True}, [
    {"type": "phone", "mode": "mini", "img": "tg_3435c02c_top.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "Réponse : les centres de données américains de l'IA. Ils réclament des turbines à gaz et des réseaux électriques."
beat(t, "Réponse : les centres de données américains de l'I.A. Ils réclament des turbines à gaz... et des réseaux électriques.", {"shots": [C("B8"), {**C("B8b"), "at_word": W(t, "turbines")}]}, [
    {"type": "news", "at_word": W(t, "centres"), "left": "SIEMENS ENERGY", "right": "11 NOV.", "tag": "DATA CENTERS · ÉTATS-UNIS",
     "headline": "L'expansion des centres de données américains alimente la demande en turbines et en équipements de réseau", "highlight": "turbines", "sub": "Boursorama · 11 nov. 2026"}])
t = "Certains clients versent même des acomptes, juste pour réserver leur place dans la file."
beat(t, None, C("B9"), [
    {"type": "bigtitle", "lines": ["DES ACOMPTES", "POUR RÉSERVER"], "at_word": W(t, "acomptes")},
    {"type": "source", "text": "France Épargne · 11 nov. 2026"}])
t = "Résultat : le dividende passe de 0,70 à 2,30 euros par action. Plus du triple."
beat(t, "Résultat : le dividende passe de soixante-dix centimes... à deux euros trente par action. Plus du triple.", {"screen": True, "under": C("B10")}, [
    {"type": "screen_duo", "a": {"kicker": "DIVIDENDE 2025", "value_to": 0.70, "decimals": 2, "suffix": " €", "color": "gold", "desc": "Par action"},
     "b_at_word": W(t, "2,30"), "b": {"kicker": "DIVIDENDE 2026", "value_to": 2.30, "decimals": 2, "suffix": " €", "color": "green", "desc": "Proposé à l'assemblée générale"}},
    {"type": "source", "text": "Siemens Energy · France Épargne · Boursorama"}])
t = "Et jusqu'à 9 milliards d'euros de rachats d'actions d'ici 2030."
beat(t, "Et jusqu'à neuf milliards d'euros de rachats d'actions d'ici deux mille trente.", {"screen": True, "under": C("B11")}, [
    {"type": "screen_counter", "kicker": "RACHATS D'ACTIONS", "value_from": 0, "value_to": 9, "decimals": 0, "prefix": "jusqu'à ", "suffix": " Md€", "color": "green",
     "pill": "D'ICI FIN 2030", "desc": "Nouveau programme · Siemens Energy · France Épargne"}])
t = "Et la fièvre gagne toute la chaîne : CoreWeave annonce un chiffre d'affaires en hausse de 168 %."
beat(t, "Et la fièvre gagne toute la chaîne : CoreWeave annonce un chiffre d'affaires en hausse de cent soixante-huit pour cent.", {"shots": [C("B12"), {**C("B12b"), "at_word": W(t, "CoreWeave")}]}, [
    {"type": "stock", "key": "CRWV", "name": "CoreWeave", "sub": "Cloud de l'IA · chiffre d'affaires trimestriel", "pct": "+168 %", "up": True, "size": "big", "y": 1420, "at_word": W(t, "CoreWeave")}])
t = "Les puces européennes s'envolent : Soitec plus de 9 %, Infineon plus de 5 %, STMicro autour de 4 %."
beat(t, "Les puces européennes s'envolent : Soitec, plus de neuf pour cent... Infineon, plus de cinq... S.T. Micro, autour de quatre.", C("B13"), [
    {"type": "tickers", "title": "PUCES · OUVERTURE MERCREDI", "rows": [
        {"name": "Soitec", "pct": "+9,2 %", "at_word": W(t, "Soitec"), "key": "SOI"},
        {"name": "Infineon", "pct": "+5,6 %", "at_word": W(t, "Infineon"), "key": "IFX"},
        {"name": "STMicro", "pct": "≈ +4 %", "at_word": W(t, "STMicro"), "key": "STM", "up": True}]},
    {"type": "source", "text": "Boursorama · ouverture du 11 nov."}])
t = "Le paradoxe : l'Europe parie sur le vent, mais la course à l'IA, elle, fait tourner les turbines à gaz."
beat(t, "Le paradoxe : l'Europe parie sur le vent... mais la course à l'I.A., elle, fait tourner les turbines à gaz.", {"shots": [C("B14"), {**C("B14b"), "at_word": W(t, "course")}]}, [
    {"type": "bigtitle", "lines": ["LE VENT", "OU LE GAZ ?"], "at_word": W(t, "paradoxe")}])
t = "Prochain juge de paix : Nvidia publie ses résultats le 17 novembre."
beat(t, "Prochain juge de paix : Nvidia publie ses résultats le dix-sept novembre.", C("B15"), [
    {"type": "date", "text": "Résultats Nvidia : mardi 17 novembre"},
    {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "Le thermomètre de toute la chaîne de l'IA", "size": "big", "y": 1420, "at_word": W(t, "Nvidia")}])
t = "Et toi, tu mises sur le vent… ou sur le gaz ? Dis-le-moi en commentaire."
beat(t, "Et toi, tu mises sur le vent... ou sur le gaz ? Dis-le-moi en commentaire.", {"shots": [C("B16"), {**C("B16b"), "at_word": W(t, "gaz")}]}, [
    {"type": "bigtitle", "lines": ["LE VENT", "OU LE GAZ ?"], "at_word": W(t, "mises")}])
t = "Chaque matin, je fais le tri dans le bruit pour toi. Sur mon Telegram gratuit, plus de 22 000 personnes reçoivent l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées et mes opportunités en temps réel. Lien en bio."
beat(t, "Chaque matin, je fais le tri dans le bruit pour toi. Sur mon Telegram gratuit, plus de vingt-deux mille personnes reçoivent l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées, et mes opportunités en temps réel. Lien en bio.",
     {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Siemens Energy vs Vestas : ce que personne ne t'a dit",
     "imgs": ["tg_1eaa56f0.jpg", "tg_3435c02c_top.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "ACCÈS GRATUIT"}],
    cta="long", endcard={"duration": 1.8, "button": "ACCÈS GRATUIT", "small": "Telegram gratuit · lien en bio"})
DROP = [int(x) for x in os.environ.get("DROP", "").split(",") if x]
B = [b for i, b in enumerate(B) if i not in DROP]
d = os.path.dirname(os.path.abspath(__file__))
clips = json.load(open(os.path.join(d, "clips.json"))) if os.path.exists(os.path.join(d, "clips.json")) else {}
def sub(bg):
    if isinstance(bg, dict):
        if "clip" in bg and bg["clip"] in clips:
            bg.update(clips[bg["clip"]])
        if "under" in bg: sub(bg["under"])
        for s in bg.get("shots", []): sub(s)
for b in B: sub(b["bg"])
spec = {"id": "ep12_siemens_vestas", "date_label": "11 novembre 2026", "brand": "Invest Family Fr", "hook_type": "breaking", "hook_formula": "contre-intuitif", "cta_angle": "Chaque matin, je fais le tri dans le bruit pour toi", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.boursorama.com/bourse/actualites/les-valeurs-a-suivre-a-paris-et-en-europe-actualise-7701ce64aa6e5d85331bfe0785830627",
 "https://www.boursorama.com/bourse/actualites/l-europe-ouvre-dans-le-vert-la-tech-se-distingue-3eddfc2905b363fd2315553efd0d0d52",
 "https://www.boursorama.com/bourse/actualites/siemens-energy-vise-une-hausse-des-marges-en-2027-avec-la-demande-en-equipements-de-reseau-cf190d052f322a66e79663cad7143379",
 "https://www.france-epargne.fr/news/siemens-energy-vise-20-a-22-de-marge-en-2030-et-porte-son-dividende-a-2-30-euros",
 "https://au.investing.com/news/stock-market-news/why-is-vestas-wind-stock-sliding-today-93CH-4761354",
 "https://www.rttnews.com/3712919/vestas-wind-systems-q3-profit-rises-orders-down-narrows-fy26-outlook.aspx",
 "https://swedenherald.com/article/vestas-third-quarter-profit-and-sales-fall-short-of-forecasts-as-company-narrows-full-year-outlook"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
