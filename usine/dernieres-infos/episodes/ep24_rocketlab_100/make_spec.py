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
NS = "NewSpace Economy · 14 nov. 2026"
SL = "Starlust · 14 nov. 2026"
RL = "Rocket Lab · communiqué du 12 nov. 2026"
NS13 = "NewSpace Economy · 13 nov. 2026"

t = "100 lancements. En neuf ans à peine."
beat(t, "Cent lancements. En neuf ans... à peine.", {"shots": [C("B0"), {**C("B0b"), "at_word": W(t, "neuf")}]}, [
    {"type": "date", "text": "Samedi 14 novembre 2026 · Espace", "until_beat": 0},
    {"type": "bigtitle", "lines": ["100 LANCEMENTS", "EN 9 ANS"], "at_word": W(t, "100")},
    {"type": "stock", "key": "RKLB", "name": "Rocket Lab", "sub": "RKLB · Nasdaq", "size": "big", "y": 600, "at_word": W(t, "neuf")}])
t = "Samedi, le lanceur Electron de Rocket Lab a décollé pour la centième fois, depuis la Nouvelle-Zélande."
beat(t, "Samedi, le lanceur Electron de Rocket Lab a décollé pour la centième fois... depuis la Nouvelle-Zélande.", {"screen": True, "under": C("B1")}, [
    {"type": "screen_counter", "kicker": "ELECTRON · LANCEMENTS DEPUIS 2017", "value_from": 0, "value_to": 100, "decimals": 0, "prefix": "", "suffix": "",
     "color": "gold", "pill": "14 NOV. 2026 · PÉNINSULE DE MĀHIA", "desc": NS, "logo": "RKLB"}])
t = "Aucun lanceur développé par une entreprise privée n'avait atteint ce cap aussi vite."
beat(t, "Aucun lanceur développé par une entreprise privée... n'avait atteint ce cap aussi vite.", C("B2"), [
    {"type": "bigtitle", "lines": ["PLUS VITE QUE", "TOUS LES AUTRES"], "at_word": W(t, "cap")},
    {"type": "source", "text": RL}])
t = "Et ce n'est pas tout : 100 autres lancements sont déjà réservés."
beat(t, "Et ce n'est pas tout : cent autres lancements... sont déjà réservés.", {"screen": True, "under": C("B3")}, [
    {"type": "screen_counter", "kicker": "ELECTRON · LANCEMENTS DÉJÀ RÉSERVÉS", "value_from": 0, "value_to": 100, "decimals": 0, "prefix": "+ ", "suffix": "",
     "color": "gold", "pill": "SELON PETER BECK, PDG", "desc": NS + " · " + SL}])
t = "À bord : un satellite radar japonais, capable d'observer la Terre à travers les nuages."
beat(t, "À bord : un satellite radar japonais... capable d'observer la Terre à travers les nuages.", C("B4"), [
    {"type": "news", "at_word": W(t, "satellite"), "left": "MISSION « THE MOUNTAIN GOD RISES »", "right": "JAPON", "tag": "LA CHARGE",
     "headline": "Satellite radar YAMATSUMI-II (QPS-SAR-19), placé sur une orbite à 575 km", "highlight": "radar", "sub": NS}])
t = "Son client, iQPS, en est à sa onzième mission. Onze sur onze, toutes réussies."
beat(t, "Son client, i.Q.P.S., en est à sa onzième mission. Onze sur onze... toutes réussies.", {"screen": True, "under": C("B5")}, [
    {"type": "screen_counter", "kicker": "MISSIONS iQPS SUR ELECTRON", "value_from": 0, "value_to": 11, "decimals": 0, "prefix": "", "suffix": " / 11",
     "color": "green", "pill": "7 AUTRES LANCEMENTS PRÉVUS D'ICI 2030", "desc": NS}])
t = "Alors, comment un lanceur de 18 mètres a-t-il fait ce que même SpaceX n'avait pas fait ?"
beat(t, "Alors... comment un lanceur de dix-huit mètres a-t-il fait ce que même SpaceX n'avait pas fait ?", C("B6"), [
    {"type": "bigtitle", "lines": ["18 MÈTRES", "FACE À SPACEX ?"], "at_word": W(t, "Alors")},
    {"type": "source", "text": SL}])
t = "La conquête spatiale, je la suis de près sur mon Telegram. Lien en bio."
beat(t, "La conquête spatiale, je la suis de près sur mon Telegram. Lien en bio.", C("B7"), [
    {"type": "phone", "mode": "mini", "img": "tg_3435c02c_top.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "Première arme, la précision : ses satellites arrivent à 8 mètres de l'orbite visée. La moyenne du secteur : 15 kilomètres."
beat(t, "Première arme, la précision : ses satellites arrivent à huit mètres de l'orbite visée. La moyenne du secteur... quinze kilomètres.", {"screen": True, "under": C("B8")}, [
    {"type": "screen_duo",
     "a": {"kicker": "ELECTRON", "value_to": 8, "decimals": 0, "prefix": "", "suffix": " m", "color": "gold", "desc": "Écart avec l'orbite visée"},
     "b_at_word": W(t, "moyenne"),
     "b": {"kicker": "MOYENNE DU SECTEUR", "value_to": 15, "decimals": 0, "prefix": "≈ ", "suffix": " km", "color": "red", "desc": "Selon Rocket Lab · " + SL}}])
t = "Deuxième arme, la vitesse : pour l'armée américaine, Electron a décollé 16 h 42 après la commande."
beat(t, "Deuxième arme, la vitesse : pour l'armée américaine, Electron a décollé seize heures quarante-deux... après la commande.", {"screen": True, "under": C("B9")}, [
    {"type": "screen_counter", "kicker": "MISSION VICTUS HAZE · U.S. SPACE FORCE", "value_from": 0, "value_to": 16, "decimals": 0, "prefix": "", "suffix": " h 42",
     "color": "gold", "pill": "ENTRE LA COMMANDE ET LE DÉCOLLAGE", "desc": SL + " · " + RL}])
t = "Troisième arme, la cadence : plus de 270 satellites lancés, avec 999 moteurs Rutherford."
beat(t, "Troisième arme, la cadence : plus de deux cent soixante-dix satellites lancés... avec neuf cent quatre-vingt-dix-neuf moteurs.", {"screen": True, "under": C("B10")}, [
    {"type": "screen_duo",
     "a": {"kicker": "SATELLITES LANCÉS", "value_to": 270, "decimals": 0, "prefix": "+ de ", "suffix": "", "color": "gold", "desc": "En 100 vols d'Electron"},
     "b_at_word": W(t, "999"),
     "b": {"kicker": "MOTEURS RUTHERFORD", "value_to": 999, "decimals": 0, "prefix": "", "suffix": "", "color": "gold", "desc": SL}}])
t = "Et Rocket Lab revendique plus d'un milliard de dollars de lancements réservés, sur ses trois programmes."
beat(t, "Et Rocket Lab revendique plus d'un milliard de dollars de lancements réservés... sur ses trois programmes.", {"screen": True, "under": C("B11")}, [
    {"type": "screen_counter", "kicker": "LANCEMENTS RÉSERVÉS · ELECTRON, HASTE, NEUTRON", "value_from": 0, "value_to": 1, "decimals": 0, "prefix": "+ de ", "suffix": " Md$",
     "color": "gold", "pill": "+ DE 55 SATELLITES MAISON EN PRODUCTION", "desc": SL, "logo": "RKLB"}])
t = "Le vrai enjeu est ailleurs : iQPS veut 24 satellites radar d'ici mai 2028, pour revoir une même zone toutes les dix minutes environ."
beat(t, "Le vrai enjeu est ailleurs : i.Q.P.S. veut vingt-quatre satellites radar d'ici mai deux mille vingt-huit... pour revoir une même zone toutes les dix minutes environ.", {"shots": [C("B12"), {**C("B12b"), "at_word": W(t, "revoir")}]}, [
    {"type": "bigtitle", "lines": ["24 SATELLITES", "D'ICI MAI 2028"], "at_word": W(t, "24")},
    {"type": "source", "text": NS13}])
t = "Prochaine étape : Neutron, son lanceur bien plus gros, dont le premier vol a glissé à 2027."
beat(t, "Prochaine étape : Neutron, son lanceur bien plus gros... dont le premier vol a glissé à deux mille vingt-sept.", C("B14"), [
    {"type": "date", "text": "2027 · Premier vol de Neutron"},
    {"type": "bigtitle", "lines": ["NEUTRON", "RENDEZ-VOUS EN 2027"], "at_word": W(t, "Neutron")},
    {"type": "source", "text": "NewSpace Economy · 15 oct. 2026"}])
t = "Alors, Rocket Lab peut-il devenir le prochain SpaceX ? Dis-le-moi en commentaire."
beat(t, "Alors... Rocket Lab peut-il devenir le prochain SpaceX ? Dis-le-moi en commentaire.", C("B15"), [
    {"type": "bigtitle", "lines": ["LE PROCHAIN", "SPACEX ?"], "at_word": W(t, "prochain")}])
t = "Si tu veux comprendre avant les autres au lieu de subir, rejoins mon canal Telegram gratuit : actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. Plus de 22 000 personnes y sont déjà. Lien en bio."
beat(t, "Si tu veux comprendre avant les autres au lieu de subir, rejoins mon canal Telegram gratuit : actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. Plus de vingt-deux mille personnes y sont déjà. Lien en bio.",
     {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Espace : la course aux lanceurs s'accélère",
     "imgs": ["tg_1eaa56f0.jpg", "tg_3435c02c_top.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "ACCÈS GRATUIT"}],
    cta="long", endcard={"duration": 1.8, "button": "ACCÈS GRATUIT", "small": "Telegram gratuit · lien en bio"})
d = os.path.dirname(os.path.abspath(__file__))
clips = json.load(open(os.path.join(d, "clips.json"))) if os.path.exists(os.path.join(d, "clips.json")) else {}
def sub(bg):
    if isinstance(bg, dict):
        if "clip" in bg and bg["clip"] in clips: bg.update(clips[bg["clip"]])
        if "under" in bg: sub(bg["under"])
        for s in bg.get("shots", []): sub(s)
for b in B: sub(b["bg"])
spec = {"id": "ep24_rocketlab_100", "date_label": "15 novembre 2026", "brand": "Invest Family Fr", "hook_type": "chip", "hook_formula": "chiffre choc",
        "cta_angle": "Si tu veux comprendre avant les autres au lieu de subir", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://newspaceeconomy.ca/2026/11/14/electron-100th-launch-iqps-yamatsumi-ii/",
                    "https://starlust.org/rocket-lab-completes-100th-mission-of-electron-rocket-faster-than-any-commercial-launch-vehicle/",
                    "https://newspaceeconomy.ca/2026/11/13/rocket-lab-electron-100th-launch-november-14-2026/",
                    "https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-launch-milestone-100th-electron-rocket-week"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
open(os.path.join(d, "voice_text.txt"), "w").write("\n".join(b.get("say") or b["text"] for b in B))
