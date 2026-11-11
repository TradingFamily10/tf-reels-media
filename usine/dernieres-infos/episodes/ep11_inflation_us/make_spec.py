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


t = "0,4 %. Ce petit chiffre vient de casser l'élan de Wall Street."
beat(t, "Quatre dixièmes de point... Ce petit chiffre vient de casser l'élan de Wall Street.", {"screen": True, "under": C("B0")}, [
    {"type": "date", "text": "Mardi 10 novembre 2026 · Washington", "until_beat": 1},
    {"type": "screen_logos", "kicker": "INFLATION US · OCTOBRE", "value_from": 0, "value_to": 0.4, "decimals": 1, "prefix": "+", "suffix": " %", "color": "red",
     "pill": "EN UN MOIS · ATTENDU +0,3 %", "keys": ["NVDA", "MSFT", "AMD", "AVGO"], "desc": "Indice des prix à la consommation · BLS · 10 nov."}])
t = "Et ce n'est pas le pire : le taux à 10 ans américain frôle maintenant les 5 %."
beat(t, "Et ce n'est pas le pire... le taux à dix ans américain frôle maintenant les cinq pour cent.", {"screen": True, "under": C("B1")}, [
    {"type": "screen_counter", "kicker": "TAUX US À 10 ANS", "value_from": 4.89, "value_to": 4.986, "decimals": 3, "suffix": " %", "color": "red",
     "pill": "PLUS DE 9 POINTS DE BASE EN UNE SÉANCE", "desc": "Bon du Trésor américain · clôture du 10 nov. · TechFlow / KuCoin"}])
t = "Résultat : Wall Street stoppe net son rebond. Le Nasdaq et le S&P 500 finissent dans le rouge."
beat(t, "Résultat : Wall Street stoppe net son rebond. Le Nasdaq et le S and P cinq cents finissent dans le rouge.", {"screen": True, "under": C("B2")}, [
    {"type": "screen_duo", "a": {"kicker": "NASDAQ", "value_to": -0.74, "decimals": 2, "suffix": " %", "color": "red", "desc": "25 065 points"},
     "b_at_word": W(t, "S&P"), "b": {"kicker": "S&P 500", "value_to": -0.38, "decimals": 2, "suffix": " %", "color": "red", "desc": "7 520 points"}},
    {"type": "source", "text": "Clôture du 10 nov. · Reuters / Boursorama · KuCoin"}])
t = "Et au cœur de la chute, un géant : Nvidia, déjà secoué par l'enquête sur son patron, lâche environ 5,5 %."
beat(t, "Et au cœur de la chute, un géant : Nvidia, déjà secoué par l'enquête sur son patron, lâche environ cinq et demi pour cent.", {"shots": [C("B3"), {**C("B3b"), "at_word": W(t, "lâche")}]}, [
    {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "NVDA · Nasdaq · capitalisation ≈ 4 070 Md$", "pct": "≈ −5,5 %", "up": False, "size": "big", "y": 1420, "at_word": W(t, "Nvidia")}])
t = "Le problème : les prix américains ont pris 0,4 % en un mois, quand on attendait 0,3 %."
beat(t, "Le problème : les prix américains ont pris quatre dixièmes de point en un mois... quand on attendait trois dixièmes.", {"screen": True, "under": C("B4")}, [
    {"type": "screen_duo", "a": {"kicker": "ATTENDU", "value_to": 0.3, "decimals": 1, "prefix": "+", "suffix": " %", "color": "gold", "desc": "Consensus Dow Jones"},
     "b_at_word": W(t, "pris"), "b": {"kicker": "PUBLIÉ", "value_to": 0.4, "decimals": 1, "prefix": "+", "suffix": " %", "color": "red", "desc": "Prix à la consommation · octobre"}},
    {"type": "source", "text": "BLS · 10 nov. · TheStreet · KuCoin"}])
t = "Et l'inflation de fond, sans énergie ni alimentation, monte de 0,3 % au lieu de 0,2 %."
beat(t, "Et l'inflation de fond, sans énergie ni alimentation, monte de trois dixièmes... au lieu de deux.", {"screen": True, "under": C("B5")}, [
    {"type": "screen_counter", "kicker": "INFLATION DE FOND · OCTOBRE", "value_from": 0, "value_to": 0.3, "decimals": 1, "prefix": "+", "suffix": " %", "color": "red",
     "pill": "ATTENDU : +0,2 %", "desc": "Hors énergie et alimentation · BLS · TheStreet"}])
t = "Les coupables : l'énergie, l'alimentation… et le logement, à lui seul plus d'un tiers de la hausse."
beat(t, None, {"shots": [C("B6"), {**C("B6b"), "at_word": W(t, "logement")}]}, [
    {"type": "news", "at_word": W(t, "coupables"), "left": "DÉTAIL", "right": "OCTOBRE", "tag": "INFLATION AMÉRICAINE",
     "headline": "Énergie +0,7 %, alimentation +0,5 %, logement +0,3 %", "highlight": "logement +0,3 %", "sub": "Le logement pèse plus d'un tiers de la hausse · BLS via TechFlow"}])
t = "Alors, qui va payer l'addition ?"
beat(t, "Alors... qui va payer l'addition ?", C("B7"), [
    {"type": "bigtitle", "lines": ["QUI VA PAYER", "L'ADDITION ?"], "at_word": 1}])
t = "La suite de ce feuilleton, je la publie en temps réel sur mon Telegram. Lien en bio."
beat(t, None, {"blur_prev": True}, [
    {"type": "phone", "mode": "mini", "img": "tg_3435c02c.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "La réponse est à Washington : une hausse des taux d'un quart de point en décembre est désormais entièrement intégrée par le marché."
beat(t, "La réponse est à Washington : une hausse des taux d'un quart de point en décembre... est désormais entièrement intégrée par le marché.", {"screen": True, "under": C("B9")}, [
    {"type": "screen_counter", "kicker": "FED · 8-9 DÉCEMBRE", "value_from": 0, "value_to": 25, "decimals": 0, "prefix": "+", "suffix": " pb", "color": "gold",
     "pill": "HAUSSE ENTIÈREMENT INTÉGRÉE", "desc": "Contrats à terme · CME FedWatch · TechFlow / KuCoin"}])
t = "Et le scénario d'un demi-point d'un coup pèse déjà près de 14 %."
beat(t, "Et le scénario d'un demi-point d'un coup... pèse déjà près de quatorze pour cent.", {"screen": True, "under": C("B10")}, [
    {"type": "screen_counter", "kicker": "PROBA. HAUSSE DE 50 PB", "value_from": 0, "value_to": 13.6, "decimals": 1, "suffix": " %", "color": "red",
     "pill": "DÉCEMBRE", "desc": "CME FedWatch · après l'inflation d'octobre"}])
t = "Car mardi matin, juste avant le chiffre, Christopher Waller avait fixé la ligne rouge : 0,3 % d'inflation de fond."
beat(t, "Car mardi matin, juste avant le chiffre, Christopher Ouôleur avait fixé la ligne rouge : trois dixièmes d'inflation de fond.", C("B11"), [
    {"type": "news", "at_word": W(t, "Christopher"), "left": "FED", "right": "10 NOV.", "tag": "CHRISTOPHER WALLER",
     "headline": "À 0,3 % ou plus d'inflation de fond, une hausse de 50 pb « devrait être envisagée »", "highlight": "50 pb", "sub": "Gouverneur de la Fed · TheStreet"}])
t = "Et c'est pile le chiffre tombé à 14 h 30."
beat(t, "Et c'est pile le chiffre tombé à quatorze heures trente.", C("B12"), [
    {"type": "bigtitle", "lines": ["LIGNE ROUGE", "ATTEINTE"], "at_word": W(t, "pile")}])
t = "Le paradoxe : le même jour, AMD et Broadcom s'envolent de plus de 7 %, pendant que Nvidia plonge."
beat(t, "Le paradoxe : le même jour, A.M.D. et Broadcom s'envolent de plus de sept pour cent... pendant que Nvidia plonge.", C("B13"), [
    {"type": "tickers", "title": "PUCES · MARDI 10 NOV.", "rows": [
        {"name": "AMD", "pct": "+7,25 %", "at_word": W(t, "AMD"), "key": "AMD"},
        {"name": "Broadcom", "pct": "+7,86 %", "at_word": W(t, "Broadcom"), "key": "AVGO"},
        {"name": "Nvidia", "pct": "≈ −5,5 %", "at_word": W(t, "Nvidia"), "key": "NVDA", "down": True}]},
    {"type": "source", "text": "TechFlow / KuCoin · 10 nov."}])
t = "Seule détente : le Brent retombe vers 91 dollars, après que Trump a dit que le conflit avec l'Iran pourrait finir vite."
beat(t, "Seule détente : le Brent retombe vers quatre-vingt-onze dollars... après que Trump a dit que le conflit avec l'Iran pourrait finir vite.", {"screen": True, "under": C("B14")}, [
    {"type": "screen_counter", "kicker": "BRENT · CLÔTURE 10 NOV.", "value_from": 92.57, "value_to": 91.49, "decimals": 2, "suffix": " $", "color": "red",
     "pill": "−1,17 % SUR LA SÉANCE", "desc": "Plus bas depuis fin août en séance · TechFlow / KuCoin · TheStreet"}])
t = "Prochain rendez-vous : vendredi, les prix à la production. Puis Nvidia publie ses résultats le 17 novembre."
beat(t, "Prochain rendez-vous : vendredi, les prix à la production... Puis Nvidia publie ses résultats le dix-sept novembre.", {"shots": [C("B15"), {**C("B15b"), "at_word": W(t, "Puis")}]}, [
    {"type": "date", "text": "Prix à la production US : ven. 13 nov. · Résultats Nvidia : 17 nov."},
    {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "Résultats du trimestre · 17 novembre", "size": "big", "y": 1420, "at_word": W(t, "Nvidia")}])
t = "Et toi, tu crois que la Fed osera frapper d'un demi-point ? Dis-le-moi en commentaire."
beat(t, None, {"shots": [C("B16"), {**C("B16b"), "at_word": W(t, "Dis-le-moi")}]}, [
    {"type": "bigtitle", "lines": ["LA FED OSERA-T-ELLE", "UN DEMI-POINT ?"], "at_word": W(t, "Fed")}])
t = "Plus de 22 000 personnes ont déjà une longueur d'avance. Il ne manque que toi. Sur mon Telegram gratuit : l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées et mes opportunités en temps réel. Lien en bio."
beat(t, "Plus de vingt-deux mille personnes ont déjà une longueur d'avance... Il ne manque que toi. Sur mon Telegram gratuit : l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées, et mes opportunités en temps réel. Lien en bio.",
     {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Inflation US : le scénario Fed qui change tout",
     "imgs": ["tg_1eaa56f0.jpg", "tg_3435c02c.jpg", "tg_4b2fa9a8.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
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
spec = {"id": "ep11_inflation_us", "date_label": "11 novembre 2026", "brand": "Invest Family Fr", "hook_type": "logowall", "hook_formula": "chiffre choc", "cta_angle": "22 000 personnes ont déjà une longueur d avance, il ne manque que toi", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.boursorama.com/bourse/actualites/wall-street-termine-en-baisse-apres-l-inflation-92e8bcdebdd4c2537adc34ddd331d364",
 "https://www.kucoin.com/news/flash/u-s-stocks-drop-as-october-cpi-exceeds-expectations-nvidia-falls-5-5",
 "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-nov-10-2026"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
