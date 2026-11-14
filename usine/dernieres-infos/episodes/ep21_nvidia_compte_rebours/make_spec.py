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
RT = "Reuters via Boursorama · 13 nov. 2026"
YF = "Yahoo Finance · 13 nov. 2026"
MV = "MoneyVox · 13 nov. 2026"
BO = "Boursorama · 13 nov. 2026"

t = "Dans 3 jours, Nvidia publie ses résultats. Et pour la première fois, sans patron."
beat(t, "Dans trois jours, Nvidia publie ses résultats. Et pour la première fois... sans patron.", {"shots": [C("B0"), {**C("B0b"), "at_word": W(t, "pour")}]}, [
    {"type": "date", "text": "Samedi 14 novembre 2026 · Wall Street", "until_beat": 0},
    {"type": "hook_bignum", "value_to": 6, "prefix": "", "suffix": "", "unit": "SEMAINES DE BAISSE", "label": "Nvidia, d'affilée, avant ses résultats",
     "logos": ["NVDA", "AMD", "AVGO", "NVDA"], "reveal_at_word": W(t, "sans"), "count_dur": 1.0}])
t = "Cette semaine, l'action a perdu 12,8 %. Sa sixième semaine de baisse d'affilée."
beat(t, "Cette semaine, l'action a perdu près de treize pour cent. Sa sixième semaine de baisse... d'affilée.", {"screen": True, "under": C("B1")}, [
    {"type": "screen_counter", "kicker": "NVIDIA · 9-13 NOV.", "value_from": 0, "value_to": 12.8, "decimals": 1, "prefix": "− ", "suffix": " %", "color": "red",
     "pill": "6e SEMAINE DE BAISSE D'AFFILÉE", "desc": RT}])
t = "Vendredi, elle repasse sous les 4 000 milliards de dollars en Bourse."
beat(t, "Vendredi, elle repasse sous les quatre mille milliards de dollars... en Bourse.", C("B2"), [
    {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "NVDA · Nasdaq · clôture 162,85 $", "pct": "−2,01 %", "up": False, "size": "big", "y": 600, "at_word": 1},
    {"type": "source", "text": "Capitalisation sous 4 000 Md$ · " + YF}])
t = "Jensen Huang est parti jeudi. Et HSBC vient de couper son objectif de 365 à 170 dollars."
beat(t, "Jensen Huang est parti jeudi. Et H.S.B.C. vient de couper son objectif... de trois cent soixante-cinq à cent soixante-dix dollars.", C("B3"), [
    {"type": "news", "at_word": W(t, "HSBC"), "left": "NVIDIA · ANALYSTES", "right": "13 NOV.", "tag": "DÉGRADATION",
     "headline": "HSBC passe Nvidia à « conserver » et abaisse son objectif à 170 $", "highlight": "abaisse son objectif",
     "sub": "Objectif précédent : 365 $ · " + YF}])
t = "Et ce n'est pas le pire : vendredi, tout le secteur des semi-conducteurs a plongé."
beat(t, "Et ce n'est pas le pire : vendredi, tout le secteur des semi-conducteurs a plongé.", C("B5"), [
    {"type": "tickers", "title": "PUCES · VENDREDI 13 NOV.", "rows": [
        {"name": "Indice des semi-conducteurs", "pct": "−3,4 %", "at_word": W(t, "secteur"), "up": False},
        {"name": "AMD", "pct": "−8,8 %", "at_word": W(t, "semi"), "key": "AMD", "up": False},
        {"name": "Nvidia", "pct": "−2 %", "at_word": W(t, "plongé"), "key": "NVDA", "up": False}]},
    {"type": "source", "text": RT}])
t = "AMD lâche près de 9 %, après cinq hausses de suite."
beat(t, "A.M.D. lâche près de neuf pour cent... après cinq hausses de suite.", C("B6"), [
    {"type": "stock", "key": "AMD", "name": "AMD", "sub": "AMD · Nasdaq · vendredi 13 nov.", "pct": "−8,8 %", "up": False, "size": "big", "y": 600, "at_word": 0},
    {"type": "source", "text": RT}])
t = "Pourtant, Wall Street signe sa meilleure semaine depuis août. Alors, qui a ramassé la mise ?"
beat(t, "Pourtant, Wall Street signe sa meilleure semaine depuis août. Alors... qui a ramassé la mise ?", {"screen": True, "under": C("B7")}, [
    {"type": "screen_duo",
     "a": {"kicker": "S&P 500 · SEMAINE", "value_to": 2.5, "decimals": 1, "prefix": "+ ", "suffix": " %", "color": "green", "desc": "Meilleure semaine depuis août"},
     "b_at_word": W(t, "août"),
     "b": {"kicker": "NASDAQ · SEMAINE", "value_to": 2.6, "decimals": 1, "prefix": "+ ", "suffix": " %", "color": "green", "desc": "Fin de 4 semaines de baisse"}},
    {"type": "source", "text": RT + " · " + YF}])
t = "Les comptes de Nvidia, je les décortique en direct sur mon Telegram. Lien en bio."
beat(t, "Les comptes de Nvidia, je les décortique en direct sur mon Telegram. Lien en bio.", {"blur_prev": True}, [
    {"type": "phone", "mode": "mini", "img": "tg_3435c02c_top.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "Réponse : les valeurs du quotidien. Vendredi, la consommation gagne 1,4 %, la tech perd 1,7 %."
beat(t, "Réponse : les valeurs du quotidien. Vendredi, la consommation gagne plus d'un pour cent... la tech en perd presque deux.", {"screen": True, "under": C("B9")}, [
    {"type": "screen_duo",
     "a": {"kicker": "CONSO DE BASE", "value_to": 1.4, "decimals": 1, "prefix": "+ ", "suffix": " %", "color": "green", "desc": "Meilleur secteur vendredi"},
     "b_at_word": W(t, "tech"),
     "b": {"kicker": "TECH · S&P 500", "value_to": 1.7, "decimals": 1, "prefix": "− ", "suffix": " %", "color": "red", "desc": "Pire secteur vendredi"}},
    {"type": "source", "text": RT}])
t = "Meta, elle, prend 2,9 %. Le marché fait le tri."
beat(t, "Meta, elle, prend près de trois pour cent. Le marché... fait le tri.", C("B10"), [
    {"type": "stock", "key": "META", "name": "Meta", "sub": "META · Nasdaq · vendredi 13 nov.", "pct": "+2,9 %", "up": True, "size": "big", "y": 600, "at_word": 0},
    {"type": "source", "text": RT}])
t = "Et à Paris ? Le CAC 40 aligne cinq hausses en cinq séances : plus 2,8 % sur la semaine."
beat(t, "Et à Paris ? Le CAC quarante aligne cinq hausses en cinq séances : presque trois pour cent sur la semaine.", {"screen": True, "under": C("B11")}, [
    {"type": "screen_counter", "kicker": "CAC 40 · 9-13 NOV.", "value_from": 0, "value_to": 2.8, "decimals": 1, "prefix": "+ ", "suffix": " %", "color": "green",
     "pill": "5 SÉANCES · 5 HAUSSES · 8 369 PTS", "desc": MV + " · " + BO}])
t = "Mais un chiffre inquiète : le taux américain à 10 ans touche 5,17 %, au plus haut depuis octobre."
beat(t, "Mais un chiffre inquiète : le taux américain à dix ans touche plus de cinq pour cent... au plus haut depuis octobre.", {"screen": True, "under": C("B13")}, [
    {"type": "screen_counter", "kicker": "TAUX US 10 ANS", "value_from": 4.5, "value_to": 5.17, "decimals": 2, "suffix": " %", "color": "red",
     "pill": "PLUS HAUT DEPUIS OCTOBRE", "desc": YF}])
t = "Les marchés parient sur une hausse des taux de la Fed le 9 décembre."
beat(t, "Les marchés parient sur une hausse des taux de la Fed... le neuf décembre.", C("B14"), [
    {"type": "bigtitle", "lines": ["HAUSSE DE TAUX", "LE 9 DÉC. ?"], "at_word": W(t, "hausse")},
    {"type": "source", "text": "Prix à la production US : +6,5 % sur un an · " + YF + " · " + MV}])
t = "Mardi soir, les résultats de Nvidia. Mercredi, le compte rendu de la Fed."
beat(t, "Mardi soir, les résultats de Nvidia. Mercredi, le compte rendu de la Fed.", C("B15"), [
    {"type": "date", "text": "Mardi 17 nov. : Nvidia · Mercredi 18 nov. : minutes de la Fed"},
    {"type": "tickers", "title": "LA SEMAINE QUI VIENT", "rows": [
        {"name": "Nvidia · résultats", "pct": "MAR. 17/11", "at_word": W(t, "Nvidia"), "key": "NVDA", "up": True},
        {"name": "Fed · compte rendu", "pct": "MER. 18/11", "at_word": W(t, "Fed"), "up": True}]},
    {"type": "source", "text": MV}])
t = "Alors, Nvidia peut-elle rebondir sans Jensen Huang ? Dis-le-moi en commentaire."
beat(t, "Alors... Nvidia peut-elle rebondir sans Jensen Huang ? Dis-le-moi en commentaire.", C("B16"), [
    {"type": "bigtitle", "lines": ["REBOND OU", "CHUTE LIBRE ?"], "at_word": W(t, "rebondir")}])
t = "Mardi soir, certains liront les chiffres le lendemain. Toi, tu les auras en direct. Sur mon Telegram gratuit, plus de 22 000 personnes suivent l'actu géopolitique et financière, mes analyses d'actions détaillées et mes opportunités en temps réel. Lien en bio."
beat(t, "Mardi soir, certains liront les chiffres le lendemain. Toi... tu les auras en direct. Sur mon Telegram gratuit, plus de vingt-deux mille personnes suivent l'actu géopolitique et financière, mes analyses d'actions détaillées, et mes opportunités en temps réel. Lien en bio.",
     {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Nvidia : les résultats décortiqués en direct ce soir",
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
spec = {"id": "ep21_nvidia_compte_rebours", "date_label": "14 novembre 2026", "brand": "Invest Family Fr", "hook_type": "bignum", "hook_formula": "compte à rebours",
        "cta_angle": "Mardi soir, certains liront les chiffres le lendemain. Toi, tu les auras en direct", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.boursorama.com/bourse/actualites/wall-street-clot-une-semaine-en-forte-hausse-par-une-baisse-journaliere-847b582b43c1dff6a6d87e196d4f67be",
 "https://finance.yahoo.com/markets/live/stock-market-today-friday-november-13-dow-sp-500-nasdaq-nvidia-ppi-141451558.html",
 "https://www.moneyvox.fr/bourse/actualites/111240/le-cac-40-totalenergies-en-forme-le-journal-de-la-bourse-du-vendredi-13-novembre-2026",
 "https://www.boursorama.com/bourse/actualites/cinq-sur-cinq-pour-le-cac-40-sur-la-semaine-de2fcbec62e3ccc0a2e58f1c60018d85"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
open(os.path.join(d, "voice_text.txt"), "w").write("\n".join(b.get("say") or b["text"] for b in B))
