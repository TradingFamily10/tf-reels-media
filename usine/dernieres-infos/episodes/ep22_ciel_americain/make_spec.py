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
CBS = "CBS News · 14 nov. 2026"
AFP = "AFP via Boursorama · 15 nov. 2026"
FA = "FlightAware via CBS News · 14 nov. 2026"

t = "Ce n'est pas une cyberattaque qui a cloué l'Amérique au sol. C'est du matériel… vieux de 20 ans."
beat(t, "Ce n'est pas une cyberattaque qui a cloué l'Amérique au sol. C'est du matériel... vieux de vingt ans.",
     {"shots": [C("B0"), {**C("B0b"), "at_word": W(t, "C'est")}]}, [
    {"type": "date", "text": "Vendredi 13 novembre 2026 · États-Unis", "until_beat": 0},
    {"type": "news", "at_word": 0, "left": "ÉTATS-UNIS · FAA", "right": "13 NOV.", "tag": "ARRÊT NATIONAL",
     "headline": "Tous les décollages stoppés dans le pays pendant environ cinq heures", "highlight": "Tous les décollages stoppés",
     "sub": CBS + " · " + AFP}])
t = "Vendredi, plus de 9 000 vols ont été annulés aux États-Unis. En une seule journée."
beat(t, "Vendredi, plus de neuf mille vols ont été annulés aux États-Unis. En une seule journée.", {"screen": True, "under": C("B1")}, [
    {"type": "screen_counter", "kicker": "VOLS ANNULÉS · VENDREDI 13 NOV.", "value_from": 0, "value_to": 9159, "decimals": 0, "prefix": "", "suffix": "",
     "color": "red", "pill": "EN UNE SEULE JOURNÉE", "desc": FA}])
t = "Et ce n'est pas le pire : plus de 7 000 autres sont partis en retard."
beat(t, "Et ce n'est pas le pire : plus de sept mille autres sont partis en retard.", {"screen": True, "under": C("B2")}, [
    {"type": "screen_duo",
     "a": {"kicker": "ANNULÉS", "value_to": 9159, "decimals": 0, "prefix": "", "suffix": "", "color": "red", "desc": "Vendredi 13 nov."},
     "b_at_word": W(t, "7"),
     "b": {"kicker": "RETARDÉS", "value_to": 7190, "decimals": 0, "prefix": "", "suffix": "", "color": "gold", "desc": FA}}])
t = "Un arrêt national, du jamais-vu depuis janvier 2023. Le dernier grand avant ça ? Le 11 septembre."
beat(t, "Un arrêt national, du jamais-vu depuis janvier deux mille vingt-trois. Le dernier grand avant ça ? Le onze septembre.", C("B4"), [
    {"type": "news", "at_word": 0, "left": "PRÉCÉDENTS", "right": "FAA", "tag": "HISTORIQUE",
     "headline": "Premier arrêt national depuis janvier 2023. Le dernier grand : le 11 septembre 2001", "highlight": "11 septembre 2001",
     "sub": CBS}])
t = "Samedi matin, la casse continue : Delta, United et American annulent encore des centaines de vols."
beat(t, "Samedi matin, la casse continue : Delta, United et American annulent encore des centaines de vols.", C("B5"), [
    {"type": "tickers", "title": "VOLS ANNULÉS · SAMEDI MATIN", "rows": [
        {"name": "Delta", "pct": "640", "at_word": W(t, "Delta"), "key": "DAL", "up": False},
        {"name": "United", "pct": "530", "at_word": W(t, "United"), "key": "UAL", "up": False},
        {"name": "American", "pct": "488", "at_word": W(t, "American"), "key": "AAL", "up": False}]},
    {"type": "source", "text": FA}])
t = "Alors, qui a fait tomber le ciel américain ?"
beat(t, "Alors... qui a fait tomber le ciel américain ?",
     C("B6"), [
    {"type": "bigtitle", "lines": ["QUI A FAIT TOMBER", "LE CIEL AMÉRICAIN ?"], "at_word": W(t, "Alors")}])
t = "Les coulisses de cette panne, je les décortique sur mon Telegram. Lien en bio."
beat(t, "Les coulisses de cette panne, je les décortique sur mon Telegram. Lien en bio.", C("B7"), [
    {"type": "phone", "mode": "mini", "img": "tg_1eaa56f0.jpg", "bio_at_word": W(t, "bio")}])
t = "Selon les premières conclusions, des routeurs Cisco… fabriqués entre 2001 et 2006."
beat(t, "Selon les premières conclusions, des routeurs Cisco... fabriqués entre deux mille un et deux mille six.", C("B8"), [
    {"type": "stock", "key": "CSCO", "name": "Cisco", "sub": "Routeurs série 600 · enquête préliminaire", "pct": "20 ANS", "up": False,
     "size": "big", "y": 600, "at_word": W(t, "Cisco")},
    {"type": "source", "text": "Sources gouvernementales via CBS News · 14 nov. 2026"}])
t = "Saturés de données, ils envoyaient des infos incohérentes. Alors Washington a tout coupé."
beat(t, "Saturés de données, ils envoyaient des infos incohérentes. Alors Washington a tout coupé.", C("B9"), [
    {"type": "news", "at_word": 0, "left": "SEAN DUFFY · TRANSPORTS", "right": "13 NOV.", "tag": "CITATION",
     "headline": "« Les routeurs ont été surchargés de données. Alors nous avons coupé le système »", "highlight": "surchargés de données",
     "sub": "Traduction · " + CBS}])
t = "Selon l'AFP, tout serait parti du remplacement de vieux câbles en cuivre."
beat(t, "Selon l'A.F.P., tout serait parti du remplacement de vieux câbles en cuivre.", C("B10"), [
    {"type": "bigtitle", "lines": ["DE VIEUX CÂBLES", "EN CUIVRE"], "at_word": W(t, "vieux")},
    {"type": "source", "text": AFP}])
t = "Et ce réseau de communication, c'est L3Harris qui l'exploite pour l'aviation civile."
beat(t, "Et ce réseau de communication, c'est L. trois Harris qui l'exploite pour l'aviation civile.", C("B11"), [
    {"type": "stock", "key": "LHX", "name": "L3Harris", "sub": "Opérateur du réseau FTI de la FAA", "pct": "", "up": False,
     "size": "big", "y": 600, "at_word": W(t, "L3Harris")},
    {"type": "source", "text": CBS}])
t = "Pas de cyberattaque, jure Washington. Et aucun lien avec la panne géante de Microsoft."
beat(t, "Pas de cyberattaque, jure Washington. Et aucun lien avec la panne géante de Microsoft.", C("B12"), [
    {"type": "stock", "key": "MSFT", "name": "Microsoft", "sub": "Panne mondiale du 12-13 nov. · aucun lien", "pct": "", "up": False,
     "y": 600, "at_word": W(t, "aucun")},
    {"type": "source", "text": "Markwayne Mullin, sécurité intérieure · " + CBS}])
t = "Mais la facture tombe : 50 milliards de dollars pour remplacer tout le contrôle aérien."
beat(t, "Mais la facture tombe : cinquante milliards de dollars pour remplacer tout le contrôle aérien.", {"screen": True, "under": C("B13")}, [
    {"type": "screen_logos", "kicker": "MILLIARDS DE DOLLARS DEMANDÉS", "value_from": 0, "value_to": 50, "decimals": 0, "suffix": " Md$", "color": "gold",
     "pill": "REMPLACER TOUT LE SYSTÈME", "keys": ["LHX", "CSCO", "DAL", "UAL"], "desc": CBS + " · " + AFP}])
t = "Et l'horloge tourne : le 26 novembre, c'est Thanksgiving, et toute l'Amérique reprend l'avion."
beat(t, "Et l'horloge tourne : le vingt-six novembre, c'est Thanksgiving... et toute l'Amérique reprend l'avion.", C("B14"), [
    {"type": "date", "text": "Jeudi 26 novembre 2026 · Thanksgiving"},
    {"type": "bigtitle", "lines": ["J-11", "AVANT THANKSGIVING"], "at_word": W(t, "Thanksgiving")}])
t = "Alors, le ciel américain tiendra-t-il jusqu'aux fêtes ? Dis-le-moi en commentaire."
beat(t, "Alors... le ciel américain tiendra-t-il jusqu'aux fêtes ? Dis-le-moi en commentaire.", C("B15"), [
    {"type": "bigtitle", "lines": ["IL TIENDRA", "OU PAS ?"], "at_word": W(t, "tiendra")}])
t = "Les infos qui comptent arrivent toujours en vrac. Sur mon Telegram gratuit, je les remets dans l'ordre : actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. Plus de 22 000 personnes y sont déjà. Lien en bio."
beat(t, "Les infos qui comptent arrivent toujours en vrac. Sur mon Telegram gratuit, je les remets dans l'ordre : actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. Plus de vingt-deux mille personnes y sont déjà. Lien en bio.",
     {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Panne géante aux États-Unis : ce qu'il faut retenir",
     "imgs": ["tg_3435c02c_top.jpg", "tg_1eaa56f0.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "REJOINS LA FAMILLE"}],
    cta="long", endcard={"duration": 1.8, "button": "REJOINS LA FAMILLE", "small": "Telegram gratuit · lien en bio"})
d = os.path.dirname(os.path.abspath(__file__))
clips = json.load(open(os.path.join(d, "clips.json"))) if os.path.exists(os.path.join(d, "clips.json")) else {}
def sub(bg):
    if isinstance(bg, dict):
        if "clip" in bg and bg["clip"] in clips: bg.update(clips[bg["clip"]])
        if "under" in bg: sub(bg["under"])
        for s in bg.get("shots", []): sub(s)
for b in B: sub(b["bg"])
spec = {"id": "ep22_ciel_americain", "date_label": "15 novembre 2026", "brand": "Invest Family Fr", "hook_type": "headline", "hook_formula": "coupable inattendu",
        "cta_angle": "Les infos qui comptent arrivent toujours en vrac, je les remets dans l'ordre", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.cbsnews.com/news/faa-ground-stop-canceled-flights-travelers-what-we-know/",
                    "https://www.cbsnews.com/news/faa-issues-nationwide-ground-stop/",
                    "https://www.boursorama.com/bourse/actualites/etats-unis-des-cables-en-cuivre-vetustes-a-l-origine-des-perturbations-de-vols-95fcde80bf9d1770b858f29c8d10bbf6"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
open(os.path.join(d, "voice_text.txt"), "w").write("\n".join(b.get("say") or b["text"] for b in B))
