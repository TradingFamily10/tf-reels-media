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
PB = "Prixdubaril.com · 13 nov. 2026"
GC = "Le Grand Continent (rapport AIE) · 13 nov. 2026"
MV = "MoneyVox · 13 nov. 2026"
LN = "Libnanews (BLS) · 13 nov. 2026"
TS = "TheStreet (CME FedWatch) · 13 nov. 2026"
VA = "VARO Energy · 13 nov. 2026"

t = "Trois sites pétroliers saoudiens visés en une seule nuit. Et tout le monde regarde ailleurs."
beat(t, "Trois sites pétroliers saoudiens visés... en une seule nuit. Et tout le monde regarde ailleurs.", {"shots": [C("B0"), {**C("B0b"), "at_word": W(t, "tout")}]}, [
    {"type": "date", "text": "Samedi 14 novembre 2026 · Golfe & mer Rouge", "until_beat": 0},
    {"type": "breaking", "label": "DERNIÈRES INFOS", "lines": ["3 SITES PÉTROLIERS", "SAOUDIENS", "VISÉS EN 1 NUIT"]}])
t = "Jeudi soir, les rebelles houthis du Yémen revendiquent trois frappes."
beat(t, "Jeudi soir, les rebelles houthis du Yémen revendiquent trois frappes.", C("B1"), [
    {"type": "news", "at_word": W(t, "houthis"), "left": "YÉMEN · ARABIE SAOUDITE", "right": "12 NOV.", "tag": "REVENDICATION",
     "headline": "Les Houthis affirment avoir frappé trois sites pétroliers saoudiens", "highlight": "trois sites pétroliers",
     "sub": "Revendication non vérifiée · la coalition dit avoir intercepté un drone · " + PB}])
t = "Un oléoduc, le terminal de Yanbu sur la mer Rouge, et un site pétrolier à Riyad."
beat(t, "Un oléoduc... le terminal de Yanbou sur la mer Rouge... et un site pétrolier à Riyad.", {"shots": [C("B2"), {**C("B2b"), "at_word": W(t, "terminal")}, {**C("B2c"), "at_word": W(t, "Riyad")}]}, [
    {"type": "bigtitle", "lines": ["OLÉODUC, YANBU", "ET RIYAD"], "at_word": W(t, "oléoduc")},
    {"type": "source", "text": "Selon les Houthis · " + PB}])
t = "Depuis le 28 février, l'Iran verrouille Ormuz, par où passaient 20 % des hydrocarbures du monde."
beat(t, "Depuis le vingt-huit février, l'Iran verrouille Ormuz... par où passait un cinquième des hydrocarbures du monde.", {"screen": True, "under": C("B3")}, [
    {"type": "screen_counter", "kicker": "VIA ORMUZ AVANT LA GUERRE", "value_from": 0, "value_to": 20, "decimals": 0, "prefix": "≈ ", "suffix": " %", "color": "gold",
     "pill": "VERROUILLÉ DEPUIS LE 28 FÉVRIER", "desc": "Part des hydrocarbures mondiaux · " + PB}])
t = "Or cet oléoduc, c'est la porte de secours : il contourne Ormuz."
beat(t, "Or cet oléoduc, c'est la porte de secours : il contourne Ormuz.", C("B4"), [
    {"type": "bigtitle", "lines": ["LA PORTE", "DE SECOURS"], "at_word": W(t, "porte")},
    {"type": "source", "text": "Oléoduc Est-Ouest · " + PB}])
t = "Résultat : le Brent bondit de 92 à 96 dollars en deux séances."
beat(t, "Résultat : le Brent bondit de quatre-vingt-douze à quatre-vingt-seize dollars... en deux séances.", {"screen": True, "under": C("B5")}, [
    {"type": "screen_duo", "a": {"kicker": "BRENT · CLÔTURE MER. 11 NOV.", "value_to": 92.76, "decimals": 2, "suffix": " $", "color": "gold", "desc": "Contrat de janvier"},
     "b_at_word": W(t, "96"), "b": {"kicker": "VENDREDI 13 NOV., 7 H", "value_to": 96.13, "decimals": 2, "suffix": " $", "color": "green", "desc": "Le baril de Brent"}},
    {"type": "source", "text": PB}])
t = "Mais sur la semaine, il recule. Alors, pourquoi le pétrole n'explose-t-il pas ?"
beat(t, "Mais sur la semaine... il recule. Alors, pourquoi le pétrole n'explose-t-il pas ?", C("B6"), [
    {"type": "bigtitle", "lines": ["POURQUOI ÇA", "N'EXPLOSE PAS ?"], "at_word": W(t, "pourquoi")},
    {"type": "source", "text": "Brent −2,38 % sur la semaine · " + PB}])
t = "Ce conflit, je le suis en direct sur mon Telegram. Lien en bio."
beat(t, None, {"blur_prev": True}, [
    {"type": "phone", "mode": "mini", "img": "tg_3435c02c.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "Vendredi, l'Agence internationale de l'énergie a tranché : l'offre de pétrole dépasse la demande."
beat(t, "Vendredi, l'Agence internationale de l'énergie a tranché : l'offre de pétrole... dépasse la demande.", C("B8"), [
    {"type": "news", "at_word": W(t, "Agence"), "left": "AIE · RAPPORT MENSUEL", "right": "13 NOV.", "tag": "LA RÉPONSE",
     "headline": "Pour la première fois depuis février, l'offre de pétrole dépasse la demande", "highlight": "dépasse la demande", "sub": GC}])
t = "Une première depuis la guerre : 52 millions de barils en plus dans les stocks en octobre."
beat(t, "Une première depuis la guerre : cinquante-deux millions de barils en plus dans les stocks en octobre.", {"screen": True, "under": C("B9")}, [
    {"type": "screen_counter", "kicker": "STOCKS MONDIAUX · OCT.", "value_from": 0, "value_to": 52, "decimals": 0, "prefix": "+ ", "suffix": " M", "color": "gold",
     "pill": "MILLIONS DE BARILS EN PLUS", "desc": "Surtout du pétrole en mer · " + GC}])
t = "En Bourse, TotalEnergies a quand même pris près de 2 % vendredi."
beat(t, "En Bourse, TotalEnergies a quand même pris près de deux pour cent... vendredi.", C("B10"), [
    {"type": "stock", "key": "TTE", "name": "TotalEnergies", "sub": "TTE · Euronext Paris · vendredi 13 nov.", "pct": "+1,9 %", "up": True, "size": "big", "y": 600, "at_word": W(t, "TotalEnergies")},
    {"type": "source", "text": "CAC 40 : 8 369 pts (+0,09 %) · " + MV}])
t = "Mais à la pompe, le gazole reste 32 % plus cher qu'avant la guerre en Europe."
beat(t, "Mais à la pompe, le gazole reste près d'un tiers plus cher qu'avant la guerre en Europe.", {"screen": True, "under": C("B11")}, [
    {"type": "screen_counter", "kicker": "GAZOLE UE VS AVANT-GUERRE", "value_from": 0, "value_to": 32, "decimals": 0, "prefix": "+ ", "suffix": " %", "color": "red",
     "pill": "FRANCE : 2,156 € LE LITRE", "desc": GC + " · " + PB}])
t = "Aux États-Unis, les prix à la production grimpent de 6,5 % sur un an, un record depuis 2022."
beat(t, "Aux États-Unis, les prix à la production grimpent de plus de six pour cent sur un an... un record depuis deux mille vingt-deux.", {"screen": True, "under": C("B12")}, [
    {"type": "screen_counter", "kicker": "PRIX PRODUCTION US · OCT.", "value_from": 0, "value_to": 6.5, "decimals": 1, "prefix": "+ ", "suffix": " %", "color": "red",
     "pill": "SUR UN AN · PLUS HAUT DEPUIS NOV. 2022", "desc": LN}])
t = "Prochain rendez-vous : la Fed, les 8 et 9 décembre, avec une hausse de taux attendue."
beat(t, "Prochain rendez-vous : la Fed, les huit et neuf décembre... avec une hausse de taux attendue.", C("B13"), [
    {"type": "date", "text": "Réunion de la Fed : 8 et 9 décembre 2026"},
    {"type": "bigtitle", "lines": ["8-9 DÉCEMBRE", "LA FED"], "at_word": W(t, "Fed")},
    {"type": "source", "text": "Hausse de 0,25 point anticipée · " + TS}])
t = "Alors, la mer Rouge va-t-elle tenir ? Dis-le-moi en commentaire."
beat(t, "Alors... la mer Rouge va-t-elle tenir ? Dis-le-moi en commentaire.", C("B14"), [
    {"type": "bigtitle", "lines": ["LA MER ROUGE", "VA-T-ELLE TENIR ?"], "at_word": W(t, "mer")}])
t = "La prochaine secousse, tu veux l'apprendre ici… ou la voir venir ? Sur mon Telegram gratuit, plus de 22 000 personnes ont l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées et mes opportunités en temps réel. Lien en bio."
beat(t, "La prochaine secousse, tu veux l'apprendre ici... ou la voir venir ? Sur mon Telegram gratuit, plus de vingt-deux mille personnes ont l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées, et mes opportunités en temps réel. Lien en bio.",
     {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Pétrole : ce que les frappes houthies changent vraiment",
     "imgs": ["tg_4b2fa9a8.jpg", "tg_1eaa56f0.jpg", "tg_3435c02c_top.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "REJOINS LA FAMILLE"}],
    cta="long", endcard={"duration": 1.8, "button": "REJOINS LA FAMILLE", "small": "Telegram gratuit · lien en bio"})
d = os.path.dirname(os.path.abspath(__file__))
clips = json.load(open(os.path.join(d, "clips.json"))) if os.path.exists(os.path.join(d, "clips.json")) else {}
def sub(bg):
    if isinstance(bg, dict):
        if "clip" in bg and bg["clip"] in clips: bg.update(clips[bg["clip"]])
        if "under" in bg: sub(bg["under"])
        for s in bg.get("shots", []): sub(s)
for b in B: sub(b["bg"])
spec = {"id": "ep20_houthis_petrole", "date_label": "14 novembre 2026", "brand": "Invest Family Fr", "hook_type": "breaking", "hook_formula": "personne n'en parle",
        "cta_angle": "La prochaine secousse, tu veux l'apprendre ici ou la voir venir ?", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://prixdubaril.com/news-petrole/75209-le-brent-au-dessus-de-96-dollars-les-houthis-visent-le-petrole-saoudien.html",
 "https://legrandcontinent.eu/fr/2026/11/13/la-crise-petroliere-est-elle-terminee/",
 "https://france.varoenergy.com/actualites-france/flash-marche-du-13-novembre-2026-a-09h40/",
 "https://www.moneyvox.fr/bourse/actualites/111240/le-cac-40-totalenergies-en-forme-le-journal-de-la-bourse-du-vendredi-13-novembre-2026",
 "https://libnanews.com/marches-du-13-novembre-inflation-et-financement-de-lia/",
 "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-nov-13-2026"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
open(os.path.join(d, "voice_text.txt"), "w").write("\n".join(b.get("say") or b["text"] for b in B))
