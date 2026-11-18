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

AB = "ABC Bourse · 17 nov. 2026"
CD = "CoinDesk · 17 nov. 2026"
QZ = "Quartz · 17 nov. 2026"
EM = "Économie Matin · 18 nov. 2026"

t = "Les chiffres sont records. Et pourtant, Nvidia n'a plus de patron."
beat(t, "Les chiffres sont records... Et pourtant, Nvidia n'a plus de patron.", {"shots": [C("B0"), {**C("B0b"), "at_word": W(t, "pourtant")}]}, [
    {"type": "date", "text": "Mardi 17 novembre 2026 · après la clôture de Wall Street", "until_beat": 0},
    {"type": "bigtitle", "lines": ["RÉSULTATS RECORDS", "MAIS SANS PATRON"], "at_word": 0},
    {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "NVDA · Nasdaq · 3e trimestre 2026-27", "size": "big", "y": 600, "at_word": W(t, "Nvidia")}])
t = "115,8 milliards de dollars de ventes en un trimestre : plus 103 % en un an."
beat(t, "Plus de cent quinze milliards de dollars de ventes en un trimestre... plus cent trois pour cent en un an.", {"screen": True, "under": C("B1")}, [
    {"type": "screen_counter", "kicker": "VENTES · EN MD$", "value_from": 0, "value_to": 115.8, "decimals": 1, "prefix": "", "suffix": "", "color": "gold",
     "pill": "+103 % SUR UN AN", "desc": "Trimestre clos le 25 oct. 2026 · " + AB}])
t = "Et ce n'est pas le plus fou : Wall Street n'en attendait que 109."
beat(t, "Et ce n'est pas le plus fou : Wall Street n'en attendait que cent neuf.", {"screen": True, "under": C("B2")}, [
    {"type": "screen_duo",
     "a": {"kicker": "ATTENDU · EN MD$", "value_to": 108.8, "decimals": 1, "prefix": "", "suffix": "", "color": "white", "desc": "Consensus · " + CD},
     "b_at_word": W(t, "attendait"),
     "b": {"kicker": "PUBLIÉ · EN MD$", "value_to": 115.8, "decimals": 1, "prefix": "", "suffix": "", "color": "green", "desc": "3e trimestre 2026-27 · " + AB}}])
t = "Les data centers pèsent à eux seuls 107 milliards. Plus de 9 dollars sur 10."
beat(t, "Les data centers pèsent à eux seuls cent sept milliards... Plus de neuf dollars sur dix.", {"screen": True, "under": C("B3")}, [
    {"type": "screen_counter", "kicker": "DATA CENTERS · EN MD$", "value_from": 0, "value_to": 107.6, "decimals": 1, "prefix": "", "suffix": "", "color": "gold",
     "pill": "≈ 93 % DES VENTES · +110 % SUR UN AN", "desc": AB + " · " + EM}])
t = "Le bénéfice net ? 65 milliards de dollars. Plus du double de l'an dernier."
beat(t, "Le bénéfice net ? Soixante-cinq milliards de dollars. Plus du double de l'an dernier.", {"screen": True, "under": C("B4")}, [
    {"type": "screen_duo",
     "a": {"kicker": "BÉNÉFICE NET · IL Y A UN AN", "value_to": 31.9, "decimals": 1, "prefix": "", "suffix": " Md$", "color": "white", "desc": "3e trimestre 2025-26 · " + AB},
     "b_at_word": W(t, "65"),
     "b": {"kicker": "BÉNÉFICE NET · CE TRIMESTRE", "value_to": 65.3, "decimals": 1, "prefix": "", "suffix": " Md$", "color": "green", "desc": "+105 % · " + AB}}])
t = "Ses nouvelles puces Vera Rubin tournent déjà chez Microsoft, Google, Oracle et CoreWeave."
beat(t, "Ses nouvelles puces Véra Rubine tournent déjà chez Microsoft, Google, Oracle et CoreWeave.", {"screen": True, "under": C("B5")}, [
    {"type": "screen_logos", "kicker": "VERA RUBIN DÉJÀ EN SERVICE", "value_from": 0, "value_to": 4, "decimals": 0, "suffix": " GÉANTS", "color": "gold",
     "pill": "DU CLOUD ET DE L'I.A.", "keys": ["MSFT", "GOOGL", "ORCL", "CRWV"], "desc": AB}])
t = "Alors, où est le problème ?"
beat(t, "Alors... où est le problème ?", C("B6"), [
    {"type": "bigtitle", "lines": ["OÙ EST", "LE PROBLÈME ?"], "at_word": W(t, "où")}])
t = "Ces résultats, je les décortique en direct sur mon Telegram. Lien en bio."
beat(t, None, C("B7"), [
    {"type": "phone", "mode": "mini", "img": "tg_4b2fa9a8.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "Le problème, c'est le fauteuil vide. Jensen Huang a démissionné le 12 novembre, après 33 ans aux commandes."
beat(t, "Le problème, c'est le fauteuil vide... Jensen Huang a démissionné le douze novembre, après trente-trois ans aux commandes.", {"shots": [C("B8"), {**C("B8b"), "at_word": W(t, "Jensen")}]}, [
    {"type": "news", "at_word": W(t, "Jensen"), "left": "NVIDIA · DIRECTION", "right": "12 NOV. 2026", "tag": "DÉMISSION",
     "headline": "Jensen Huang quitte la direction de Nvidia après 33 ans à sa tête", "highlight": "33 ans", "sub": QZ + " · " + AB}])
t = "C'est Colette Kress, la directrice financière, qui assure l'intérim."
beat(t, "C'est Colette Kress, la directrice financière, qui assure l'intérim.", C("B9"), [
    {"type": "stock", "key": "NVDA", "name": "Colette Kress", "sub": "PDG par intérim + directrice financière", "y": 560, "at_word": W(t, "Kress")},
    {"type": "source", "text": CD + " · " + QZ}])
t = "Et hier soir, le conseil a fermé la porte : pas question de faire revenir Huang."
beat(t, "Et hier soir, le conseil a fermé la porte : pas question de faire revenir Huang.", C("B10"), [
    {"type": "news", "at_word": W(t, "conseil"), "left": "CONSEIL D'ADMINISTRATION", "right": "17 NOV.", "tag": "CITATION",
     "headline": "Aucune intention de réintégrer Jensen Huang, selon le président du conseil Harvey Jones", "highlight": "Aucune intention", "sub": CD + " · " + QZ}])
t = "Autre ombre : la Chine. Nvidia y a vendu 2,4 milliards de dollars de puces ce trimestre, puis a tout stoppé."
beat(t, "Autre ombre : la Chine. Nvidia y a vendu plus de deux milliards de dollars de puces ce trimestre... puis a tout stoppé.", {"screen": True, "under": C("B11")}, [
    {"type": "screen_counter", "kicker": "VENTES DE PUCES EN CHINE", "value_from": 0, "value_to": 2.4, "decimals": 1, "prefix": "", "suffix": " Md$", "color": "red",
     "pill": "LIVRAISONS ARRÊTÉES", "desc": "Selon Colette Kress (CNN) · " + QZ}])
t = "Lundi, Washington a encore durci les exportations de puces d'I.A."
beat(t, "Lundi, Washington a encore durci les exportations de puces d'I.A.", C("B12"), [
    {"type": "news", "at_word": W(t, "Washington"), "left": "ÉTATS-UNIS · COMMERCE", "right": "16 NOV.", "tag": "EXPORTATIONS",
     "headline": "Le département du Commerce resserre les restrictions sur les puces d'IA", "highlight": "resserre", "sub": QZ}])
t = "Pourtant, sa prévision de 130 milliards se fait sans la Chine. Et elle dépasse encore les 125 attendus."
beat(t, "Pourtant, sa prévision de cent trente milliards se fait sans la Chine... Et elle dépasse encore les cent vingt-cinq attendus.", {"screen": True, "under": C("B13")}, [
    {"type": "screen_duo",
     "a": {"kicker": "PRÉVISION T4 · EN MD$", "value_to": 130, "decimals": 0, "prefix": "≈ ", "suffix": "", "color": "gold", "desc": "± 3 %, hors Chine · " + AB},
     "b_at_word": W(t, "dépasse"),
     "b": {"kicker": "ATTENDU · EN MD$", "value_to": 125.3, "decimals": 1, "prefix": "", "suffix": "", "color": "white", "desc": "Consensus · " + CD}}])
t = "Prochaine étape : le conseil cherche un patron permanent. Et ce nom-là, tout le marché l'attend."
beat(t, "Prochaine étape : le conseil cherche un patron permanent... Et ce nom-là, tout le marché l'attend.", C("B14"), [
    {"type": "tickers", "title": "À SURVEILLER", "rows": [
        {"name": "Nvidia · ouverture de Wall Street", "pct": "MER. 15H30", "at_word": W(t, "conseil"), "key": "NVDA", "up": True},
        {"name": "Nouveau PDG permanent", "pct": "EN RECHERCHE", "at_word": W(t, "patron"), "key": "NVDA", "up": True}]},
    {"type": "source", "text": QZ}])
t = "Alors, Nvidia peut-elle rester le roi des puces sans son fondateur ? Dis-le en commentaire."
beat(t, "Alors... Nvidia peut-elle rester le roi des puces... sans son fondateur ? Dis-le en commentaire.", C("B15"), [
    {"type": "bigtitle", "lines": ["ROI DES PUCES", "SANS FONDATEUR ?"], "at_word": W(t, "roi")}])
t = "Chaque matin, je fais le tri dans le bruit pour toi sur mon canal Telegram gratuit : l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées et les opportunités en temps réel. Plus de 22 000 personnes sont déjà là. Lien en bio."
beat(t, "Chaque matin, je fais le tri dans le bruit pour toi sur mon canal Telegram gratuit : l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées et les opportunités en temps réel. Plus de vingt-deux mille personnes sont déjà là. Lien en bio.", {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Nvidia : records et fauteuil vide, l'analyse",
     "imgs": ["tg_1eaa56f0.jpg", "tg_3435c02c.jpg", "tg_38e4f34b.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
    cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})
d = os.path.dirname(os.path.abspath(__file__))
clips = json.load(open(os.path.join(d, "clips.json"))) if os.path.exists(os.path.join(d, "clips.json")) else {}
def sub(bg):
    if isinstance(bg, dict):
        if "clip" in bg and bg["clip"] in clips: bg.update(clips[bg["clip"]])
        if "under" in bg: sub(bg["under"])
        for s in bg.get("shots", []): sub(s)
for b in B: sub(b["bg"])
spec = {"id": "ep31_nvidia_resultats", "date_label": "18 novembre 2026", "brand": "Invest Family Fr", "hook_type": "chip", "hook_formula": "contre-intuitif",
        "cta_angle": "Chaque matin, je fais le tri dans le bruit pour toi", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.abcbourse.com/marches/nvidia-devoile-des-resultats-records-son-chiffre-d-affaires-bondit-de-103-en_706262",
 "https://www.coindesk.com/fr/markets/2026/11/17/nvidia-tops-estimates-issues-strong-guidance-adds-usd150-billion-to-buyback-authorization",
 "https://fr.qz.com/revenus-troisime-trimestre-nvidia-conseil-huang-retour-111726",
 "https://www.economiematin.fr/nvidia-resultats-trimestre-115-8-milliards-tresorerie-novembre-2026",
 "https://fr.qz.com/bnfice-de-nvidia-dpasse-les-estimations-jensen-huang-sortie-111726"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
open(os.path.join(d, "voice_text.txt"), "w").write("\n".join(b.get("say") or b["text"] for b in B))
