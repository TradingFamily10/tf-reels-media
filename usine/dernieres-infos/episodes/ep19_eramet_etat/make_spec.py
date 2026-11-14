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
GN = "Communiqué Eramet · 13 nov. 2026"
MV = "MoneyVox · 13 nov. 2026"
ZB = "Zonebourse · 13 nov. 2026"
OM = "Outremers 360 (AFP) · 13 nov. 2026"
BR = "Boursorama (Reuters) · 13 nov. 2026"

t = "Le jour où l'État est devenu le premier actionnaire d'un géant français des métaux."
beat(t, "Le jour où l'État est devenu le premier actionnaire... d'un géant français des métaux.", {"shots": [C("B0"), {**C("B0b"), "at_word": W(t, "géant")}]}, [
    {"type": "date", "text": "Vendredi 13 novembre 2026 · Bourse de Paris", "until_beat": 1},
    {"type": "bigtitle", "lines": ["L'ÉTAT", "1ER ACTIONNAIRE"], "at_word": W(t, "État")},
    {"type": "stock", "key": "ERA", "name": "Eramet", "sub": "ERA · Euronext Paris · vendredi", "pct": "−10,64 %", "up": False, "size": "big", "y": 560, "at_word": W(t, "géant")}])
t = "Et ce n'est pas le pire : l'action a chuté de plus de 10 % en une seule séance."
beat(t, "Et ce n'est pas le pire : l'action a chuté de plus de dix pour cent... en une seule séance.", {"screen": True, "under": C("B1")}, [
    {"type": "screen_counter", "kicker": "ERAMET · CLÔTURE DU 13 NOV.", "value_from": 0, "value_to": 10.64, "decimals": 2, "prefix": "− ", "suffix": " %", "color": "red",
     "pill": "32,92 € EN CLÔTURE", "desc": MV + " · " + ZB, "logo": "ERA"}])
t = "Son nom : Eramet. Manganèse au Gabon, nickel en Indonésie, lithium en Argentine."
beat(t, "Son nom : Eramet. Manganèse au Gabon... nickel en Indonésie... lithium en Argentine.", {"shots": [C("B2"), {**C("B2b"), "at_word": W(t, "nickel")}, {**C("B2c"), "at_word": W(t, "lithium")}]}, [
    {"type": "news", "at_word": W(t, "Eramet"), "left": "ERAMET · GROUPE MINIER", "right": "FRANCE", "tag": "LE PROFIL",
     "headline": "Manganèse au Gabon, nickel en Indonésie, sables minéralisés au Sénégal, lithium en Argentine", "highlight": "lithium", "sub": OM},
    {"type": "stock", "key": "ERA", "name": "Eramet", "sub": "Groupe minier français", "y": 1440, "at_word": W(t, "Eramet")}])
t = "Pour renforcer ses finances, il lance une augmentation de capital d'environ 500 millions d'euros."
beat(t, "Pour renforcer ses finances, il lance une augmentation de capital... d'environ cinq cents millions d'euros.", {"screen": True, "under": C("B4")}, [
    {"type": "screen_counter", "kicker": "AUGMENTATION DE CAPITAL", "value_from": 0, "value_to": 500, "decimals": 0, "suffix": " M€", "color": "gold",
     "pill": "34 506 054 ACTIONS NOUVELLES", "desc": "Objectif : renforcer la structure financière · " + GN + " · " + BR, "logo": "ERA"}])
t = "L'action nouvelle est vendue 14,49 €. 62 % sous le cours du 11 novembre."
beat(t, "L'action nouvelle est vendue moins de quinze euros. Soixante-deux pour cent sous le cours du onze novembre.", {"screen": True, "under": C("B5")}, [
    {"type": "screen_duo", "a": {"kicker": "CLÔTURE DU 11 NOV.", "value_to": 38.48, "decimals": 2, "suffix": " €", "color": "gold", "desc": "Cours de référence", "logo": "ERA"},
     "b_at_word": W(t, "14,49"), "b": {"kicker": "PRIX DE SOUSCRIPTION", "value_to": 14.49, "decimals": 2, "suffix": " €", "color": "red", "desc": "Décote de 62,34 %", "logo": "ERA"}},
    {"type": "source", "text": GN + " · " + MV}])
t = "Alors, qui va mettre l'argent sur la table ?"
beat(t, "Alors... qui va mettre l'argent sur la table ?", C("B6"), [
    {"type": "bigtitle", "lines": ["QUI MET", "L'ARGENT ?"], "at_word": W(t, "qui")}])
t = "Ce dossier, je le suis en direct sur mon Telegram. Lien en bio."
beat(t, None, {"blur_prev": True}, [
    {"type": "phone", "mode": "mini", "img": "tg_38e4f34b.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "Réponse : l'État français. Environ 64 % de l'opération, soit près de 322 millions d'euros."
beat(t, "Réponse : l'État français. Environ soixante-quatre pour cent de l'opération... soit près de trois cent vingt-deux millions d'euros.", {"screen": True, "under": C("B8")}, [
    {"type": "screen_counter", "kicker": "PART PRISE PAR L'ÉTAT", "value_from": 0, "value_to": 64, "decimals": 0, "suffix": " %", "color": "gold",
     "pill": "≈ 322 M€", "desc": GN + " · " + OM, "logo": "ERA"}])
t = "Il passe premier actionnaire… mais s'interdit de dépasser 49 % des droits de vote."
beat(t, "Il passe premier actionnaire... mais s'interdit de dépasser quarante-neuf pour cent des droits de vote.", {"screen": True, "under": C("B9")}, [
    {"type": "screen_duo", "a": {"kicker": "L'ÉTAT AVANT L'OPÉRATION", "value_to": 27.1, "decimals": 1, "suffix": " %", "color": "gold", "desc": "du capital", "logo": "ERA"},
     "b_at_word": W(t, "49"), "b": {"kicker": "PLAFOND EN ASSEMBLÉE", "value_to": 49, "decimals": 0, "suffix": " %", "color": "gold", "desc": "des droits de vote effectifs", "logo": "ERA"}},
    {"type": "source", "text": GN + " · " + OM}])
t = "Et les petits porteurs ? Un actionnaire à 1 % qui ne suit pas voit sa part fondre de plus de moitié."
beat(t, "Et les petits porteurs ? Un actionnaire à un pour cent qui ne suit pas... voit sa part fondre de plus de moitié.", {"screen": True, "under": C("B10")}, [
    {"type": "screen_duo", "a": {"kicker": "AVANT", "value_to": 1, "decimals": 2, "suffix": " %", "color": "gold", "desc": "du capital", "logo": "ERA"},
     "b_at_word": W(t, "fondre"), "b": {"kicker": "APRÈS, SANS SOUSCRIRE", "value_to": 0.45, "decimals": 2, "suffix": " %", "color": "red", "desc": "Dilution : 1 % → 0,45 %", "logo": "ERA"}},
    {"type": "source", "text": "Exemple du prospectus · " + GN}])
t = "Le mot clé est dans le communiqué : une décision « stratégique » de l'État."
beat(t, "Le mot clé est dans le communiqué : une décision... stratégique... de l'État.", C("B12"), [
    {"type": "news", "at_word": W(t, "communiqué"), "left": "COMMUNIQUÉ ERAMET", "right": "13 NOV.", "tag": "CITATION",
     "headline": "« L'État français a pris la décision stratégique de renforcer sa participation »", "highlight": "décision stratégique", "sub": OM}])
t = "Des métaux au cœur de l'acier, des batteries… et de la bataille avec la Chine."
beat(t, "Des métaux au cœur de l'acier, des batteries... et de la bataille avec la Chine.", {"shots": [C("B13"), {**C("B13b"), "at_word": W(t, "batteries")}, {**C("B13c"), "at_word": W(t, "Chine")}]}, [
    {"type": "bigtitle", "lines": ["DES MÉTAUX", "STRATÉGIQUES"], "at_word": W(t, "métaux")}])
t = "À surveiller : la souscription s'ouvre le 18 novembre. Verdict le 2 décembre."
beat(t, "À surveiller : la souscription s'ouvre le dix-huit novembre. Verdict... le deux décembre.", {"screen": True, "under": C("B14")}, [
    {"type": "date", "text": "Souscription : 18 → 27 novembre · résultats le 2 décembre"},
    {"type": "screen_logos", "kicker": "JOURS AVANT L'OUVERTURE", "value_from": 0, "value_to": 4, "decimals": 0, "suffix": "", "color": "gold",
     "pill": "MERCREDI 18 NOVEMBRE", "keys": ["ERA"], "desc": "Résultats le 2 déc. · " + GN}])
t = "Alors : sauvetage réussi… ou nationalisation qui ne dit pas son nom ? Dis-le-moi en commentaire."
beat(t, "Alors : sauvetage réussi... ou nationalisation qui ne dit pas son nom ? Dis-le-moi en commentaire.", C("B15"), [
    {"type": "bigtitle", "lines": ["SAUVETAGE OU", "NATIONALISATION ?"], "at_word": W(t, "sauvetage")}])
t = "22 000 personnes ont déjà la longueur d'avance. Il ne manque plus que toi. Sur mon canal Telegram gratuit : l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées et mes opportunités en temps réel. Plus de 22 000 personnes, lien en bio."
t = "Plus de 22 000 personnes ont déjà la longueur d'avance. Il ne manque plus que toi. Sur mon canal Telegram gratuit : l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées et mes opportunités en temps réel. Lien en bio."
beat(t, "Plus de vingt-deux mille personnes ont déjà la longueur d'avance. Il ne manque plus que toi. Sur mon canal Telegram gratuit : l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées, et mes opportunités en temps réel. Lien en bio.",
     {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Eramet : ce que l'arrivée de l'État change vraiment",
     "imgs": ["tg_3435c02c_top.jpg", "tg_4b2fa9a8.jpg", "tg_1eaa56f0.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "ACCÈS GRATUIT"}],
    cta="long", endcard={"duration": 1.8, "button": "ACCÈS GRATUIT", "small": "Telegram gratuit · lien en bio"})
d = os.path.dirname(os.path.abspath(__file__))
clips = json.load(open(os.path.join(d, "clips.json"))) if os.path.exists(os.path.join(d, "clips.json")) else {}
def sub(bg):
    if isinstance(bg, dict):
        if "clip" in bg and bg["clip"] in clips: bg.update(clips[bg["clip"]])
        if "under" in bg: sub(bg["under"])
        for s in bg.get("shots", []): sub(s)
for b in B: sub(b["bg"])
spec = {"id": "ep19_eramet_etat", "date_label": "14 novembre 2026", "brand": "Invest Family Fr", "hook_type": "chip", "hook_formula": "le jour où", "cta_angle": "22 000 personnes ont déjà la longueur d'avance. Il ne manque plus que toi.", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.globenewswire.com/news-release/2026/11/13/3402390/0/fr/eramet-lance-une-augmentation-de-capital-avec-maintien-du-droit-pr%C3%A9f%C3%A9rentiel-de-souscription-d-un-montant-d-environ-500-m-pour-renforcer-sa-structure-financi%C3%A8re.html",
 "https://outremers360.com/bassin-pacifique-appli/nickel-caledonien-eramet-lance-son-augmentation-de-capital-au-terme-de-laquelle-letat-va-devenir-premier-actionnaire",
 "https://www.moneyvox.fr/bourse/actualites/111240/le-cac-40-totalenergies-en-forme-le-journal-de-la-bourse-du-vendredi-13-novembre-2026",
 "https://www.zonebourse.com/actualite-bourse/cinq-sur-cinq-pour-le-cac-40-sur-la-semaine-ce785ed9d08df327",
 "https://www.boursorama.com/bourse/actualites/eramet-lance-son-augmentation-de-capital-d-environ-500-millions-d-euros-1ed934fa68a37d171390e18b22595d36"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
open(os.path.join(d, "voice_text.txt"), "w").write("\n".join(b.get("say") or b["text"] for b in B))
