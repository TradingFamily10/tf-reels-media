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


t = "Russes et Ukrainiens se reparlent ce matin… et la défense européenne grimpe ?"
beat(t, "Russes et Ukrainiens se reparlent ce matin... et la défense européenne grimpe ?", C("B0"), [
    {"type": "bigtitle", "lines": ["LA PAIX SE NÉGOCIE…", "LA DÉFENSE GRIMPE ?"], "at_word": 0},
    {"type": "stock", "key": "SAF", "name": "Safran", "sub": "SAF · Euronext Paris · ce matin", "pct": "+4 %", "up": True, "size": "big", "y": 1470, "at_word": W(t, "défense")}])
t = "Et pendant ce temps, l'Europe frôle son record historique."
beat(t, None, {"screen": True, "under": C("B1")}, [
    {"type": "screen_counter", "kicker": "STOXX 600 · MARDI MATIN", "value_from": 600, "value_to": 661, "decimals": 0, "suffix": " pts", "color": "green", "pill": "TOUT PRÈS DU RECORD D'AOÛT", "desc": "+0,73 % · Reuters via Boursorama · 10 nov."}])
t = "À Abou Dhabi, Américains, Russes et Ukrainiens négocient aujourd'hui et demain."
beat(t, "À Abou Dhabi, Américains, Russes et Ukrainiens négocient aujourd'hui... et demain.", C("B2"), [
    {"type": "date", "text": "Mardi 10 et mercredi 11 novembre · Abou Dhabi", "until_beat": 3},
    {"type": "news", "at_word": W(t, "Abou"), "left": "ACTUALITÉS", "right": "ÉMIRATS ARABES UNIS", "tag": "GUERRE EN UKRAINE",
     "headline": "Pourparlers à trois à Abou Dhabi", "highlight": "à trois", "sub": "États-Unis · Russie · Ukraine — sans les Européens à la table (AFP)"}])
t = "Une première depuis février : plus de huit mois sans négociation directe."
beat(t, "Une première depuis février : plus de huit mois sans négociation directe.", {"screen": True, "under": C("B3")}, [
    {"type": "screen_counter", "kicker": "SANS NÉGOCIATION DIRECTE", "value_from": 0, "value_to": 8, "decimals": 0, "prefix": "+ de ", "suffix": " mois", "color": "gold", "pill": "PREMIÈRE DEPUIS FÉVRIER", "desc": "The National · AFP · 10 nov."}])
t = "Pour Washington, Steve Witkoff et Jared Kushner. Au centre : les garanties de sécurité."
beat(t, None, C("B4"), [
    {"type": "bigtitle", "lines": ["GARANTIES", "DE SÉCURITÉ"], "at_word": W(t, "garanties")},
    {"type": "source", "text": "The National · AFP"}])
t = "Trump promet même un très grand accord, qui pourrait englober toute l'Europe."
beat(t, None, C("B5"), [
    {"type": "news", "at_word": W(t, "promet"), "left": "ÉTATS-UNIS", "right": "10 NOV.", "tag": "LA PROMESSE DE TRUMP",
     "headline": "« Un très grand accord » avec la Russie", "highlight": "très grand accord", "sub": "Qui pourrait « englober toute l'Europe » (RFI)"}])
t = "Alors, pourquoi les valeurs de la défense ne chutent-elles pas ?"
beat(t, "Alors... pourquoi les valeurs de la défense ne chutent-elles pas ?", C("B6"), [
    {"type": "bigtitle", "lines": ["POURQUOI ÇA", "NE CHUTE PAS ?"], "at_word": 1}])
t = "Ces négociations, je les suis heure par heure sur mon Telegram. Lien en bio."
beat(t, None, {"blur_prev": True}, [{"type": "phone", "mode": "mini", "img": "tg_1eaa56f0.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "Ce matin, l'aéronautique et la défense prennent plus de 2 % en Europe."
beat(t, "Ce matin, l'aéronautique et la défense prennent plus de deux pour cent en Europe.", {"screen": True, "under": C("B8")}, [
    {"type": "screen_logos", "kicker": "AÉRO & DÉFENSE · EUROPE", "value_from": 0, "value_to": 2.24, "decimals": 2, "prefix": "+", "suffix": " %", "color": "green", "pill": "MARDI 10 NOV. · 10 H", "keys": ["SAF", "LDO"], "desc": "Safran · Leonardo · Reuters via Boursorama"}])
t = "Safran gagne 4 %, Leonardo près de 2 %."
beat(t, "Safran gagne quatre pour cent... Leonardo près de deux pour cent.", C("B9"), [
    {"type": "tickers", "title": "DÉFENSE · MARDI MATIN", "rows": [
        {"name": "Safran", "pct": "+4,09 %", "at_word": W(t, "Safran"), "key": "SAF"},
        {"name": "Leonardo", "pct": "+1,98 %", "at_word": W(t, "Leonardo"), "key": "LDO"}]},
    {"type": "source", "text": "Boursorama · 10 nov., en séance"}])
t = "Parce que rien n'est signé : Moscou exige des territoires, Kiev refuse."
beat(t, "Parce que rien n'est signé : Moscou exige des territoires... Kiev refuse.", C("B10"), [
    {"type": "news", "at_word": W(t, "Moscou"), "left": "ACTUALITÉS", "right": "RUSSIE · UKRAINE", "tag": "LE BLOCAGE",
     "headline": "Moscou veut du territoire, Kiev dit non", "highlight": "Kiev dit non", "sub": "Kiev n'a « pas d'attentes particulières » (AFP)"}])
t = "Le vrai moteur est ailleurs : le Brent passe sous 90 dollars, une première depuis août."
beat(t, "Le vrai moteur est ailleurs : le Brent passe sous quatre-vingt-dix dollars... une première depuis août.", {"screen": True, "under": C("B11")}, [
    {"type": "screen_counter", "kicker": "BRENT · MARDI MATIN", "value_from": 92, "value_to": 89.9, "decimals": 2, "suffix": " $", "color": "red", "pill": "SOUS 90 $ POUR LA 1RE FOIS DEPUIS AOÛT", "desc": "Baril de Brent · Reuters via Boursorama", "drop": True}])
t = "À Paris, le CAC 40 prend 1 %, les banques européennes plus de 2 %."
beat(t, "À Paris, le CAC quarante prend un pour cent... les banques européennes, plus de deux pour cent.", {"screen": True, "under": C("B12")}, [
    {"type": "screen_duo", "a": {"kicker": "CAC 40 · VERS 10 H", "value_to": 1.01, "decimals": 2, "prefix": "+", "suffix": " %", "color": "green", "desc": "8 316 points"},
     "b_at_word": W(t, "banques"), "b": {"kicker": "BANQUES · STOXX", "value_to": 2.26, "decimals": 2, "prefix": "+", "suffix": " %", "color": "green", "desc": "Secteur bancaire européen"}},
    {"type": "source", "text": "Reuters · AFP via Boursorama · 10 nov."}])
t = "Même la dette française respire : le taux à 10 ans retombe à 4,67 %, contre plus de 5 % en octobre."
beat(t, "Même la dette française respire : son taux à dix ans repasse sous les cinq pour cent dépassés en octobre.", {"screen": True, "under": C("B13")}, [
    {"type": "screen_counter", "kicker": "OAT FRANÇAISE · 10 ANS", "value_from": 5.0, "value_to": 4.67, "decimals": 2, "suffix": " %", "color": "green", "pill": "PLUS DE 5 % EN OCTOBRE", "desc": "4,73 % lundi soir · AFP via Boursorama", "drop": True}])
t = "Mais à 14 h 30, l'inflation américaine peut tout casser : les marchés parient à 84 % sur une hausse de la Fed en décembre."
beat(t, "Mais à quatorze heures trente, l'inflation américaine peut tout casser : les marchés parient à quatre-vingt-quatre pour cent sur une hausse de la Fed en décembre.", {"shots": [C("B14"), {**C("B14b"), "at_word": W(t, "marchés")}]}, [
    {"type": "date", "text": "Aujourd'hui 14 h 30 · inflation US · hausse Fed en déc. : 84 % (Reuters)"},
    {"type": "bigtitle", "lines": ["14 H 30 :", "INFLATION US"], "at_word": W(t, "inflation")},
    ])
t = "Demain, deuxième round à Abou Dhabi. Vraie paix en vue… ou simple pause ? Dis-le-moi en commentaire."
beat(t, "Demain, deuxième round à Abou Dhabi. Alors... vraie paix en vue... ou simple pause ? Dis-le-moi en commentaire.", {"shots": [C("B16"), {**C("B16b"), "at_word": W(t, "Dis-le-moi")}]}, [
    {"type": "bigtitle", "lines": ["VRAIE PAIX…", "OU SIMPLE PAUSE ?"], "at_word": W(t, "Vraie")}])
t = "Les marchés réagissent en quelques minutes. Sur mon Telegram, je décortique chaque secousse dès qu'elle arrive. Plus de 22 000 personnes y reçoivent gratuitement l'actu géopolitique et financière, des analyses d'actions détaillées et mes opportunités en temps réel. Entre dans le canal, le lien est en bio."
beat(t, "Les marchés réagissent en quelques minutes. Sur mon Telegram, je décortique chaque secousse dès qu'elle arrive. Plus de vingt-deux mille personnes y reçoivent gratuitement l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées, et mes opportunités en temps réel. Entre dans le canal, le lien est en bio.",
     {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Abou Dhabi, jour 1 : mon analyse",
     "imgs": ["tg_3435c02c.jpg", "tg_38e4f34b.jpg", "tg_4b2fa9a8.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
    cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})
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
spec = {"id": "ep09_abou_dhabi", "date_label": "10 novembre 2026", "brand": "Invest Family Fr", "hook_type": "question", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.boursorama.com/bourse/actualites/le-stoxx-en-passe-de-battre-un-record-c3ff914c4c14b208ce9d3fd53a678932",
 "https://boursorama.com/bourse/actualites/la-bourse-de-paris-profite-d-un-recul-des-prix-du-petrole-et-d-un-rebond-de-l-ia-b32e0611178cc638749315a68e233e9d",
 "https://www.boursorama.com/bourse/actualites/l-europe-vue-en-hausse-avec-le-recul-du-petrole-l-inflation-americaine-au-programme-5ab40174fd1b4d08c21cfafec98a380b",
 "https://www.boursorama.com/bourse/actualites/presse-actualites-economiques-britanniques-10-novembre-540dd7ff25a824ca593e13449718cc7f",
 "https://www.thenationalnews.com/news/mena/2026/11/10/russia-and-ukraine-security-focused-talks-start-in-abu-dhabi/",
 "https://fr.qz.com/ukraine-russie-reprennent-negociations-abou-dhabi-mediation-americaine-111026"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
