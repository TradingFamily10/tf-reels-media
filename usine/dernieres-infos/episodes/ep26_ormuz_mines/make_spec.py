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

BL = "Bloomberg via Rigzone · 16 nov. 2026"
AJ = "Al Jazeera · 15 nov. 2026"
IV = "ISNA via Investing.com · 15-16 nov. 2026"
BO = "Reuters via Boursorama · 16 nov. 2026"
TK = "Tickmill · 16 nov. 2026"
NQ = "Newsquawk · 16 nov. 2026"

t = "Six navires en feu dans le détroit d'Ormuz. Et pourtant, le pétrole baisse. Pourquoi ?"
beat(t, "Six navires en feu dans le détroit d'Ormuz. Et pourtant... le pétrole baisse. Pourquoi ?", {"shots": [C("B0"), {**C("B0b"), "at_word": W(t, "pourtant")}]}, [
    {"type": "date", "text": "Lundi 16 novembre 2026 · Golfe persique", "until_beat": 0},
    {"type": "hook_bignum", "value_to": 6, "prefix": "", "suffix": "", "unit": "NAVIRES EN FEU", "label": "Détroit d'Ormuz, depuis dimanche, selon l'Iran",
     "logos": ["TTE", "SHEL", "BP", "XOM"], "reveal_at_word": W(t, "pétrole"), "count_dur": 1.0}])
t = "Selon la télévision iranienne, deux pétroliers ont encore sauté sur des mines ce lundi."
beat(t, "Selon la télévision iranienne, deux pétroliers ont encore sauté sur des mines... ce lundi.", C("B1"), [
    {"type": "news", "at_word": W(t, "pétroliers"), "left": "DÉTROIT D'ORMUZ", "right": "16 NOV.", "tag": "MINES",
     "headline": "Deux nouveaux pétroliers touchés : six navires en feu depuis dimanche, selon la télévision iranienne", "highlight": "six navires en feu",
     "sub": BL}])
t = "L'un d'eux, un superpétrolier, transportait plus de 2 millions de barils. Il aurait coulé."
beat(t, "L'un d'eux, un superpétrolier, transportait plus de deux millions de barils. Il aurait... coulé.", {"screen": True, "under": C("B2")}, [
    {"type": "screen_counter", "kicker": "SUPERPÉTROLIER TOUCHÉ", "value_from": 0, "value_to": 2, "decimals": 0, "prefix": "+ ", "suffix": " M",
     "color": "gold", "pill": "BARILS DE BRUT À BORD", "desc": "6 navires en feu depuis dimanche selon la TV iranienne · " + IV}])
t = "Et ce n'est pas le pire : dimanche, les Gardiens de la révolution ont visé Bahreïn."
beat(t, "Et ce n'est pas le pire : dimanche, les Gardiens de la révolution ont visé Bahreïn.", C("B3"), [
    {"type": "bigtitle", "lines": ["CIBLE :", "BAHREÏN"], "at_word": W(t, "visé")},
    {"type": "source", "text": AJ}])
t = "Six drones lancés sur la base de Riffa. Bahreïn affirme avoir déjoué plusieurs attaques."
beat(t, "Six drones lancés sur la base de Riffa. Bahreïn affirme avoir déjoué... plusieurs attaques.", {"screen": True, "under": C("B4")}, [
    {"type": "screen_counter", "kicker": "RIFFA · BAHREÏN", "value_from": 0, "value_to": 6, "decimals": 0, "prefix": "", "suffix": " drones",
     "color": "red", "pill": "2E REVENDICATION EN 3 JOURS", "desc": "Revendication des Gardiens · " + AJ}])
t = "Washington muscle sa présence : un troisième porte-avions arrive dans la région. Du jamais vu depuis 2003."
beat(t, "Washington muscle sa présence : un troisième porte-avions arrive dans la région. Du jamais vu... depuis deux mille trois.", {"screen": True, "under": C("B5")}, [
    {"type": "screen_counter", "kicker": "PORTE-AVIONS US", "value_from": 0, "value_to": 3, "decimals": 0, "prefix": "", "suffix": "",
     "color": "gold", "pill": "DU JAMAIS-VU DEPUIS 2003", "desc": "USS Theodore Roosevelt · " + BL}])
t = "Alors, avec des mines dans le détroit, pourquoi le baril ne s'envole-t-il pas ?"
beat(t, "Alors... avec des mines dans le détroit, pourquoi le baril ne s'envole-t-il pas ?", C("B6"), [
    {"type": "bigtitle", "lines": ["POURQUOI LE BARIL", "NE S'ENVOLE PAS ?"], "at_word": W(t, "baril")}])
t = "Ce bras de fer, je le suis heure par heure sur mon Telegram. Lien en bio."
beat(t, "Ce bras de fer, je le suis heure par heure sur mon Telegram. Lien en bio.", C("B7"), [
    {"type": "phone", "mode": "mini", "img": "tg_3435c02c_top.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "Réponse : le marché croule sous les barils. Les signaux d'offre excédentaire pèsent plus lourd que la peur."
beat(t, "Réponse : le marché croule sous les barils. Les signaux d'offre excédentaire... pèsent plus lourd que la peur.", C("B8"), [
    {"type": "bigtitle", "lines": ["TROP DE BARILS", "SUR LE MARCHÉ"], "at_word": W(t, "croule")},
    {"type": "source", "text": TK}])
t = "La semaine dernière, le Brent a perdu plus de 2 %. Ce lundi matin, il recule encore, sous les 95 dollars."
beat(t, "La semaine dernière, le Brent a perdu plus de deux pour cent. Ce lundi matin, il recule encore... sous les quatre-vingt-quinze dollars.", {"screen": True, "under": C("B9")}, [
    {"type": "screen_duo",
     "a": {"kicker": "BRENT · SEMAINE DERNIÈRE", "value_to": 2, "decimals": 0, "prefix": "− ", "suffix": " %", "color": "red", "desc": "Plus de 2 % · " + BL},
     "b_at_word": W(t, "lundi"),
     "b": {"kicker": "BRENT · LUNDI MATIN", "value_to": 94.87, "decimals": 2, "prefix": "", "suffix": " $", "color": "red", "desc": "− 1,13 % · " + BO}}])
t = "Pour les majors comme TotalEnergies, Shell ou BP, c'est ce prix du baril qui fait la loi."
beat(t, "Pour les majors comme TotalEnergies, Shell ou B.P., c'est ce prix du baril qui fait la loi.", C("B10"), [
    {"type": "stock", "key": "TTE", "name": "TotalEnergies", "sub": "TTE · Euronext Paris", "y": 480, "at_word": W(t, "TotalEnergies")},
    {"type": "stock", "key": "SHEL", "name": "Shell", "sub": "SHEL · Londres", "y": 680, "at_word": W(t, "Shell")},
    {"type": "stock", "key": "BP", "name": "BP", "sub": "BP · Londres", "y": 880, "at_word": W(t, "BP")}])
t = "Mais Téhéran souffle le chaud et le froid : l'Iran a transmis 7 conditions pour la paix, via le Qatar."
beat(t, "Mais Téhéran souffle le chaud et le froid : l'Iran a transmis sept conditions pour la paix... via le Qatar.", {"screen": True, "under": C("B11")}, [
    {"type": "screen_counter", "kicker": "CONDITIONS DE L'IRAN", "value_from": 0, "value_to": 7, "decimals": 0, "prefix": "", "suffix": "",
     "color": "gold", "pill": "LEVÉE DU BLOCUS ET DES SANCTIONS", "desc": "Présentées par Mohammad Ghalibaf, président du Parlement · " + AJ}])
t = "En face, Donald Trump envisagerait de suspendre ses frappes, sauf nouvelle provocation."
beat(t, "En face, Donald Trump envisagerait de suspendre ses frappes... sauf nouvelle provocation.", C("B12"), [
    {"type": "news", "at_word": W(t, "Trump"), "left": "MAISON-BLANCHE", "right": "16 NOV.", "tag": "IRAN",
     "headline": "Trump envisage de ne pas frapper l'Iran en l'absence de nouvelles provocations", "highlight": "ne pas frapper l'Iran",
     "sub": "Reuters, repris par " + BL}])
t = "Prochain rendez-vous : jeudi, Trump, Xi et Poutine se retrouvent en marge du sommet de l'APEC."
beat(t, "Prochain rendez-vous : jeudi, Trump, Xi et Poutine se retrouvent en marge du sommet de l'A.P.E.C.", {"shots": [C("B13"), {**C("B13b"), "at_word": W(t, "Poutine")}]}, [
    {"type": "bigtitle", "lines": ["JEUDI :", "TRUMP · XI · POUTINE"], "at_word": W(t, "jeudi")},
    {"type": "source", "text": "Sommet de l'APEC à Shenzhen · " + NQ}])
t = "Alors, les mines ou les barils en trop : qui va gagner la bataille du prix ? Dis-le-moi en commentaire."
beat(t, "Alors... les mines, ou les barils en trop : qui va gagner la bataille du prix ? Dis-le-moi en commentaire.", C("B14"), [
    {"type": "bigtitle", "lines": ["MINES OU BARILS", "QUI GAGNE ?"], "at_word": W(t, "mines")}])
t = "Le pétrole raconte la géopolitique avant les journaux. Sur mon canal Telegram gratuit, je te la traduis : l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées et les opportunités en temps réel. Plus de 22 000 personnes lisent déjà. Lien en bio."
beat(t, "Le pétrole raconte la géopolitique avant les journaux. Sur mon canal Telegram gratuit, je te la traduis : l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées et les opportunités en temps réel. Plus de vingt-deux mille personnes lisent déjà. Lien en bio.",
     {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Ormuz : six navires en feu, et le baril qui recule",
     "imgs": ["tg_1eaa56f0.jpg", "tg_3435c02c_top.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "ACCÈS GRATUIT"}],
    cta="long", endcard={"duration": 1.8, "button": "ACCÈS GRATUIT", "small": "Telegram gratuit · lien en bio"})
DROP = {1, 12}  # coupées après la voix (durée > 85 s)
B[:] = [b for i, b in enumerate(B) if i not in DROP]
d = os.path.dirname(os.path.abspath(__file__))
clips = json.load(open(os.path.join(d, "clips.json"))) if os.path.exists(os.path.join(d, "clips.json")) else {}
def sub(bg):
    if isinstance(bg, dict):
        if "clip" in bg and bg["clip"] in clips: bg.update(clips[bg["clip"]])
        if "under" in bg: sub(bg["under"])
        for s in bg.get("shots", []): sub(s)
for b in B: sub(b["bg"])
spec = {"id": "ep26_ormuz_mines", "date_label": "16 novembre 2026", "brand": "Invest Family Fr", "hook_type": "bignum", "hook_formula": "question directe",
        "cta_angle": "Le pétrole raconte la géopolitique avant les journaux", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.rigzone.com/news/wire/iran_says_door_to_peace_still_open_after_strikes_on_bahrain-16-nov-2026-185086-article/",
 "https://www.aljazeera.com/news/2026/11/15/iran-says-it-targets-us-radar-in-bahrain-what-do-we-know",
 "https://ng.investing.com/news/economy-news/iran-claims-fresh-strike-on-us-base-as-hormuz-shipping-crisis-deepens-2808258",
 "https://www.boursorama.com/bourse/actualites/l-europe-ouvre-hesitante-nvidia-pese-toujours-sur-les-echanges-cc5f3f33e4e74fb1959a96ce49690064",
 "https://www.tickmill.com/blog/daily-market-outlook-november-16-2026",
 "https://www.newsquawk.com/headlines/newsquawk-daily-european-opening-news---16th-november-2026"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
open(os.path.join(d, "voice_text.txt"), "w").write("\n".join(b.get("say") or b["text"] for b in B))
