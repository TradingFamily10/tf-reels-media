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


t = "Ce n'est pas l'inflation qui fait trembler Wall Street ce matin. C'est un homme de la Fed."
beat(t, "Ce n'est pas l'inflation qui fait trembler Wall Street ce matin... C'est un homme de la Fed.", C("B0"), [
    {"type": "date", "text": "Mardi 10 novembre 2026 · Londres", "until_beat": 1},
    {"type": "news", "at_word": 0, "left": "ACTUALITÉS", "right": "ÉTATS-UNIS", "tag": "RÉSERVE FÉDÉRALE",
     "headline": "Fed : Waller ouvre la porte à un demi-point de hausse", "highlight": "un demi-point", "sub": "Discours au Bank of England Watchers Conference · 10 nov."}])
t = "Et le pire : il ne veut pas baisser les taux. Il veut les monter."
beat(t, "Et le pire : il ne veut pas baisser les taux... Il veut les monter.", C("B1"), [
    {"type": "bigtitle", "lines": ["PAS UNE BAISSE.", "UNE HAUSSE."], "at_word": W(t, "baisser")}])
t = "Christopher Waller veut au moins un quart de point de hausse en décembre."
beat(t, "Christopher Ouôleur veut au moins un quart de point de hausse en décembre.", {"screen": True, "under": C("B2")}, [
    {"type": "screen_counter", "kicker": "HAUSSE DE TAUX · DÉCEMBRE", "value_from": 0, "value_to": 0.25, "decimals": 2, "prefix": "+", "suffix": " pt", "color": "gold", "pill": "AU MINIMUM", "desc": "Christopher Waller · discours de Londres · American Banker"}])
t = "Et si l'inflation reste chaude, il veut frapper deux fois plus fort : un demi-point."
beat(t, "Et si l'inflation reste chaude... il veut frapper deux fois plus fort : un demi-point.", {"screen": True, "under": C("B3")}, [
    {"type": "screen_duo", "a": {"kicker": "SCÉNARIO DE BASE", "value_to": 0.25, "decimals": 2, "prefix": "+", "suffix": " pt", "color": "gold", "desc": "Hausse en décembre"},
     "b_at_word": W(t, "frapper"), "b": {"kicker": "SI L'INFLATION RESTE CHAUDE", "value_to": 0.5, "decimals": 2, "prefix": "+", "suffix": " pt", "color": "red", "desc": "« Devrait être envisagée »"}},
    {"type": "source", "text": "Discours de C. Waller · 10 nov. · StockTwits · ActionForex"}])
t = "Sa phrase choc : un simple quart de point mettrait la crédibilité de la Fed en danger."
beat(t, None, C("B4"), [
    {"type": "news", "at_word": W(t, "phrase"), "left": "CITATION", "right": "10 NOV.", "tag": "CHRISTOPHER WALLER",
     "headline": "« Monter de 25 points de base seulement mettrait notre crédibilité en danger »", "highlight": "notre crédibilité", "sub": "Gouverneur de la Fed · American Banker"}])
t = "Et les marchés y croient : plus de 84 % de chances d'une hausse en décembre."
beat(t, "Et les marchés y croient : plus de quatre-vingt-quatre pour cent de chances d'une hausse en décembre.", {"screen": True, "under": C("B5")}, [
    {"type": "screen_gauge", "kicker": "PROBABILITÉ D'UNE HAUSSE EN DÉCEMBRE", "pill": "PLUS DE 84 %", "desc": "Contrats à terme · CME FedWatch · clôture du 9 nov."}])
t = "Alors, pourquoi la Fed a-t-elle aussi peur ?"
beat(t, "Alors... pourquoi la Fed a-t-elle aussi peur ?", C("B6"), [
    {"type": "bigtitle", "lines": ["POURQUOI LA FED", "A-T-ELLE PEUR ?"], "at_word": 1}])
t = "Ce bras de fer avec la Fed, je le suis en direct sur mon Telegram. Lien en bio."
beat(t, None, {"blur_prev": True}, [{"type": "phone", "mode": "mini", "img": "tg_38e4f34b.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "En septembre, les prix américains ont bondi de 0,6 % en un seul mois."
beat(t, "En septembre, les prix américains ont bondi de plus d'un demi pour cent... en un seul mois.", {"screen": True, "under": C("B8")}, [
    {"type": "screen_counter", "kicker": "INFLATION US · SEPTEMBRE", "value_from": 0, "value_to": 0.6, "decimals": 1, "prefix": "+", "suffix": " %", "color": "red", "pill": "EN UN SEUL MOIS", "desc": "Indice des prix à la consommation · TipRanks · StockTwits"}])
t = "Waller ne cache rien : ces chiffres étaient mauvais, sans la moindre éclaircie."
beat(t, "Ouôleur ne cache rien : ces chiffres étaient mauvais... sans la moindre éclaircie.", C("B9"), [
    {"type": "news", "at_word": W(t, "cache"), "left": "CITATION", "right": "10 NOV.", "tag": "INFLATION DE SEPTEMBRE",
     "headline": "« Les chiffres étaient mauvais. Aucune éclaircie. »", "highlight": "Aucune éclaircie", "sub": "Christopher Waller · ActionForex"}])
t = "Le coupable : le pétrole. Assurances et transferts en mer ajoutent 20 à 30 dollars par baril."
beat(t, "Le coupable : le pétrole. Assurances et transferts en mer ajoutent vingt à trente dollars par baril.", {"screen": True, "under": C("B10")}, [
    {"type": "screen_counter", "kicker": "SURCOÛT SUR LE BARIL", "value_from": 20, "value_to": 30, "decimals": 0, "prefix": "+20 à ", "suffix": " $", "color": "red", "pill": "GUERRE AVEC L'IRAN", "desc": "Assurances maritimes · transferts de navire à navire · C. Waller"}])
t = "Le deuxième : le chantier géant de l'IA, qui fait grimper les coûts de la tech."
beat(t, "Le deuxième : le chantier géant de l'I.A., qui fait grimper les coûts de la tech.", C("B11"), [
    {"type": "bigtitle", "lines": ["L'IA FAIT", "MONTER LES PRIX"], "at_word": W(t, "chantier")},
    {"type": "source", "text": "Recherche de la Fed citée par C. Waller · ActionForex"}])
t = "Pourtant hier, Wall Street a signé sa meilleure séance depuis avril : plus de 2 % pour le S&P 500."
beat(t, "Pourtant hier, Wall Street a signé sa meilleure séance depuis avril : plus de deux pour cent pour le S and P cinq cents.", {"screen": True, "under": C("B12")}, [
    {"type": "screen_counter", "kicker": "S&P 500 · LUNDI 9 NOV.", "value_from": 0, "value_to": 2.35, "decimals": 2, "prefix": "+", "suffix": " %", "color": "green", "pill": "MEILLEURE SÉANCE DEPUIS AVRIL", "desc": "7 549,94 points · Saxo · TipRanks"}])
t = "Meta prend 5 %, Microsoft près de 3 %… mais Nvidia chute de 4 %."
beat(t, "Meta prend cinq pour cent, Microsoft près de trois pour cent... mais Nvidia chute de quatre pour cent.", C("B13"), [
    {"type": "tickers", "title": "WALL STREET · LUNDI", "rows": [
        {"name": "Meta", "pct": "+5,1 %", "at_word": W(t, "Meta"), "key": "META"},
        {"name": "Microsoft", "pct": "+2,8 %", "at_word": W(t, "Microsoft"), "key": "MSFT"},
        {"name": "Nvidia", "pct": "−4,3 %", "at_word": W(t, "Nvidia"), "key": "NVDA", "down": True}]},
    {"type": "source", "text": "Saxo · 10 nov."}])
t = "Ce matin, l'or recule sous 4 100 dollars, le bitcoin sous 75 000."
beat(t, "Ce matin, l'or recule sous quatre mille cent dollars... le bitcoin sous soixante-quinze mille.", {"screen": True, "under": C("B14")}, [
    {"type": "screen_duo", "a": {"kicker": "OR · L'ONCE", "value_to": 4100, "decimals": 0, "prefix": "< ", "suffix": " $", "color": "red", "desc": "Sous 4 100 $"},
     "b_at_word": W(t, "bitcoin"), "b": {"kicker": "BITCOIN", "value_to": 75000, "decimals": 0, "prefix": "< ", "suffix": " $", "color": "red", "desc": "Sous 75 000 $"}},
    {"type": "source", "text": "TipRanks · 10 nov."}])
t = "À 14 h 30, si l'inflation de fond atteint 0,3 % sur un mois, le demi-point revient sur la table."
beat(t, "À quatorze heures trente, si l'inflation de fond atteint trois dixièmes de point sur un mois... le demi-point revient sur la table.", {"shots": [C("B15"), {**C("B15b"), "at_word": W(t, "demi-point")}]}, [
    {"type": "date", "text": "Inflation US d'octobre · publiée le 10 nov. à 14 h 30 (Paris)"},
    {"type": "bigtitle", "lines": ["0,3 % OU PLUS :", "DEMI-POINT ?"], "at_word": W(t, "inflation")}])
t = "Dernière réunion de la Fed de l'année en décembre : un quart de point… ou un demi ? Dis-le-moi en commentaire."
beat(t, "Dernière réunion de la Fed de l'année en décembre : un quart de point... ou un demi ? Dis-le-moi en commentaire.", {"shots": [C("B16"), {**C("B16b"), "at_word": W(t, "Dis-le-moi")}]}, [
    {"type": "bigtitle", "lines": ["UN QUART…", "OU UN DEMI ?"], "at_word": W(t, "quart")}])
t = "Tu veux comprendre avant les autres au lieu de subir ? Sur mon Telegram gratuit, plus de 22 000 personnes lisent l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées et mes opportunités en temps réel. Lien en bio."
beat(t, "Tu veux comprendre avant les autres... au lieu de subir ? Sur mon Telegram gratuit, plus de vingt-deux mille personnes lisent l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées, et mes opportunités en temps réel. Lien en bio.",
     {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Fed : ce que change le chiffre de 14 h 30",
     "imgs": ["tg_4b2fa9a8.jpg", "tg_1eaa56f0.jpg", "tg_3435c02c.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "ACCÈS GRATUIT"}],
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
spec = {"id": "ep10_fed_demi_point", "date_label": "10 novembre 2026", "brand": "Invest Family Fr", "hook_type": "headline", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.americanbanker.com/news/waller-calls-for-raising-interest-rates-25-basis-points-at-least",
 "https://stocktwits.com/news-articles/markets/equity/cpi-report-today-fed-s-waller-says-50-basis-point-rate-hike-should-be-considered-if-core-inflation-remains-elevated/cNGuW4pR97v",
 "https://www.actionforex.com/live-comments/660413-feds-waller-backs-december-hike-says-50bps-should-be-considered-if-inflation-stays-hot/",
 "https://www.tipranks.com/news/feds-largest-rate-hike-since-2022-hinges-on-todays-unusual-october-inflation-report",
 "https://www.tipranks.com/news/stock-market-today-nov-10-markets-await-the-consumer-inflation-report",
 "https://www.home.saxo/en-sg/content/articles/macro/market-quick-take---wall-street-rebounds-and-brent-slides-below-usd-92---10-november-2026-10112026"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
