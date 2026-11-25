import json, sys, os
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep53_europe_washington'
D = f'/home/claude/kit/episodes/{EP}'
def w(text, word, n=0):
    t = tokens(text); k = 0
    for i, x in enumerate(t):
        if word.lower() in x.lower():
            if k == n: return i
            k += 1
    raise SystemExit(f"mot introuvable: {word} dans {text}")
CX = json.load(open(f'{D}/cx.json')) if os.path.exists(f'{D}/cx.json') else {}
SS = json.load(open(f'{D}/ss.json')) if os.path.exists(f'{D}/ss.json') else {}
def clip(n, ss=None, cx=None):
    return {"clip": f"b{n}.mp4", "ss": SS.get(n, 1) if ss is None else ss, "cx": CX.get(n, 0.5) if cx is None else cx}
def scr(n): return {"screen": True, "under": clip(n)}
B = []
def beat(text, say, bg, overlays, **kw):
    b = {"text": text, "say": say, "bg": bg, "overlays": overlays}; b.update(kw); B.append(b); return b
RT = "Reuters via SRN News · 24 nov. 2026, 11 h 26 (Paris)"
YH = "Yahoo Finance (ADVFN) · 24 nov. 2026"
YH = "Yahoo Finance (Motley Fool) · 24 nov. 2026"
WS = "24/7 Wall St. · 24 nov. 2026, clôture"
SX = "Saxo · Asia Market Quick Take · 25 nov. 2026"
ED = "The Edge · Europe Market Wrap · 25 nov. 2026, 9 h 50 (Paris)"
RT = "Reuters (WHTC) · 25 nov. 2026, 9 h 19 (Paris)"
IV = "Investing.com (Reuters) · 25 nov. 2026"
ON = "Oninvest (Bloomberg) · 25 nov. 2026"
AP = "AP (OPB) · 25 nov. 2026"

t = "Les 9 grandes Bourses européennes montent ce matin. Pendant que la tech américaine saigne."
beat(t, "Les neuf grandes Bourses européennes montent ce matin... Pendant que la tech américaine saigne.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "Pendant"))]},
     [{"type": "date", "text": "Mercredi 25 novembre 2026 · Europe", "until_beat": 1},
      {"type": "screen_logos", "kicker": "EUROPE · INDICES EN HAUSSE", "value_from": 0, "value_to": 9, "decimals": 0, "prefix": "", "suffix": " / 9", "color": "green",
       "pill": "MERCREDI 25 NOV. · 9 H 50", "keys": ["VOW", "BMW", "MBG", "UHR", "CFR", "RCO"], "desc": "Nasdaq −1,48 % mardi soir · " + ED}])

t = "Mais ce n'est pas l'I.A. qui menace l'Europe. C'est Washington."
beat(t, "Mais ce n'est pas l'I.A. qui menace l'Europe... C'est Washington.", clip("1"),
     [{"type": "bigtitle", "lines": ["LA MENACE", "VIENT DE WASHINGTON"], "at_word": w(t, "Washington")}])

t = "À Paris, le CAC 40 grimpe de 1,20 %, à 8 137 points."
beat(t, "À Paris, le CAC quarante grimpe de plus d'un pour cent, à huit mille cent trente-sept points.",
     scr("2"),
     [{"type": "screen_duo", "a": {"kicker": "CAC 40 · 9 H 50", "value_to": 1.20, "decimals": 2, "prefix": "+", "suffix": " %", "color": "green", "desc": "8 137 points"},
       "b_at_word": w(t, "137"), "b": {"kicker": "STOXX 600 · 9 H 50", "value_to": 0.61, "decimals": 2, "prefix": "+", "suffix": " %", "color": "green", "desc": "636,63 points"}},
      {"type": "source", "text": ED}])

t = "En tête du DAX à Francfort : Volkswagen, BMW et Mercedes."
beat(t, "En tête du DAX, à Francfort : Volkswagen, B.M.W. et Mercedes.",
     scr("3"),
     [{"type": "screen_logos", "kicker": "DAX · FRANCFORT", "value_from": 0, "value_to": 0.40, "decimals": 2, "prefix": "+", "suffix": " %", "color": "green",
       "pill": "LES CONSTRUCTEURS EN TÊTE", "keys": ["VOW", "BMW", "MBG"], "desc": "25 117 points"},
      {"type": "source", "text": ED}])

t = "Le luxe suit : Swatch bondit de 6 %, Richemont de 3 %."
beat(t, "Le luxe suit : Swatch bondit de six pour cent... Richemont, de trois pour cent.",
     {"shots": [clip("4"), dict(clip("4b"), at_word=w(t, "Richemont"))]},
     [{"type": "tickers", "title": "LUXE · MERCREDI 25 NOV.", "rows": [
        {"key": "UHR", "name": "Swatch Group", "pct": "+6 %", "at_word": w(t, "Swatch")},
        {"key": "CFR", "name": "Richemont", "pct": "+3 %", "at_word": w(t, "Richemont")}]},
      {"type": "source", "text": RT}])

t = "Et Rémy Cointreau s'envole de 10,2 %, avec de nouveaux objectifs jusqu'en 2032."
beat(t, "Et Rémy Cointreau s'envole de plus de dix pour cent... avec de nouveaux objectifs jusqu'en deux mille trente-deux.",
     {"shots": [clip("5"), dict(clip("5b"), at_word=w(t, "objectifs"))]},
     [{"type": "stock", "key": "RCO", "name": "Rémy Cointreau", "sub": "RCO · Euronext Paris · 25 nov.", "pct": "+10,2 %", "up": True, "size": "big", "y": 560, "at_word": 1},
      {"type": "source", "text": RT}])

t = "Pendant ce temps, le Nasdaq a lâché 1,48 % hier soir."
beat(t, "Pendant ce temps, le Nasdaq a lâché près d'un pour cent et demi hier soir.",
     scr("6"),
     [{"type": "screen_counter", "kicker": "NASDAQ · CLÔTURE", "value_from": 0, "value_to": -1.48, "decimals": 2, "prefix": "", "suffix": " %", "color": "red",
       "pill": "MARDI 24 NOV.", "desc": "Contrats futurs encore ≈ −1,5 % ce matin · " + ON}])

t = "Alors, pourquoi l'argent file-t-il vers l'Europe ?"
beat(t, "Alors... pourquoi l'argent file-t-il vers l'Europe ?", clip("7"),
     [{"type": "bigtitle", "lines": ["POURQUOI L'ARGENT", "FILE EN EUROPE ?"], "at_word": 1}])

t = "Cette rotation, je la suis en temps réel sur mon Telegram. Lien en bio."
beat(t, "Cette rotation, je la suis en temps réel sur mon Telegram. Lien en bio.", clip("8"),
     [{"type": "phone", "mode": "mini", "img": "tg_3435c02c_top.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "Réponse : l'Europe a moins de tech et plus de valeurs défensives. Ceux qui doutent de l'I.A. viennent s'y abriter."
beat(t, "Réponse : l'Europe a moins de tech, et plus de valeurs défensives. Ceux qui doutent de l'I.A. viennent s'y abriter.",
     {"shots": [clip("9"), dict(clip("9b"), at_word=w(t, "Ceux"))]},
     [{"type": "news", "at_word": 1, "left": "BLOOMBERG · MARCHÉS", "right": "25 NOV.", "tag": "ROTATION",
       "headline": "Les actions européennes profitent des investisseurs qui parient contre l'IA",
       "highlight": "parient contre l'IA", "sub": ON + " · Citi a relevé sa recommandation en novembre"}])

t = "Mais Washington prépare de nouveaux droits de douane sur la Chine, l'Union européenne et 14 autres économies."
beat(t, "Mais Washington prépare de nouveaux droits de douane... sur la Chine, l'Union européenne, et quatorze autres économies.",
     {"shots": [clip("10"), dict(clip("10b"), at_word=w(t, "Chine"))]},
     [{"type": "news", "at_word": 2, "left": "ÉTATS-UNIS · COMMERCE", "right": "25 NOV.", "tag": "DOUANE",
       "headline": "Les États-Unis prêts à taxer la Chine, l'UE et 14 autres économies pour surcapacités industrielles",
       "highlight": "l'UE et 14 autres économies", "sub": AP}])

t = "16 économies visées, avec des taxes qui s'ajouteraient à celles de 10 à 12,5 % déjà en place."
beat(t, "Seize économies visées... avec des taxes qui s'ajouteraient à celles de dix à plus de douze pour cent déjà en place.",
     scr("11"),
     [{"type": "screen_counter", "kicker": "ENQUÊTE « SECTION 301 »", "value_from": 0, "value_to": 16, "decimals": 0, "prefix": "", "suffix": "", "color": "red",
       "pill": "ÉCONOMIES VISÉES", "desc": "En plus des droits de 10 à 12,5 % de 2026 · " + AP}])

t = "Le motif : des surcapacités industrielles, des voitures jusqu'à l'acier."
beat(t, "Le motif : des surcapacités industrielles... des voitures jusqu'à l'acier.",
     {"shots": [clip("12"), dict(clip("12b"), at_word=w(t, "acier"))]},
     [{"type": "tickers", "title": "EN PREMIÈRE LIGNE ?", "rows": [
        {"key": "VOW", "name": "Volkswagen", "pct": "⚠", "at_word": w(t, "voitures")},
        {"key": "BMW", "name": "BMW", "pct": "⚠", "at_word": w(t, "voitures")},
        {"key": "MBG", "name": "Mercedes", "pct": "⚠", "at_word": w(t, "acier")}]},
      {"type": "source", "text": AP + " · calendrier encore incertain"}])

t = "Et à 14 h 30, l'inflation PCE américaine tombe : 3,8 % attendus, contre 3,6 % le mois dernier."
beat(t, "Et à quatorze heures trente, l'inflation P.C.E. américaine tombe : près de quatre pour cent attendus... contre un peu plus de trois et demi le mois dernier.",
     scr("13"),
     [{"type": "screen_duo", "a": {"kicker": "PCE · SEPTEMBRE", "value_to": 3.6, "decimals": 1, "prefix": "", "suffix": " %", "color": "red", "desc": "Sur un an"},
       "b_at_word": w(t, "3,8"), "b": {"kicker": "PCE · OCTOBRE · ATTENDU", "value_to": 3.8, "decimals": 1, "prefix": "", "suffix": " %", "color": "red", "desc": "Publication 14 h 30 (Paris)"}},
      {"type": "source", "text": IV}])

t = "Une hausse des taux de la Fed le 9 décembre est déjà jouée à plus de 96 %."
beat(t, "Une hausse des taux de la Fed le neuf décembre... est déjà jouée à plus de quatre-vingt-seize pour cent.",
     scr("14"),
     [{"type": "screen_counter", "kicker": "FED · HAUSSE DE 0,25 POINT", "value_from": 0, "value_to": 96.4, "decimals": 1, "prefix": "", "suffix": " %", "color": "red",
       "pill": "RÉUNION DES 8-9 DÉC.", "desc": "Probabilité intégrée par les marchés · " + IV}])

t = "Alors, l'Europe : refuge… ou prochaine cible ? Dis-le en commentaire."
beat(t, "Alors, l'Europe : refuge... ou prochaine cible ? Dis-le en commentaire.", clip("15"),
     [{"type": "bigtitle", "lines": ["REFUGE OU", "PROCHAINE CIBLE ?"], "at_word": 2}])

t = ("Les marchés bougent plus vite que les journaux. Sur mon Telegram gratuit, tu as l'actu géopolitique et financière décortiquée, "
     "mes analyses d'actions détaillées et mes opportunités en temps réel. Plus de 22 000 personnes y sont déjà. Entre dans le canal, lien en bio.")
s = ("Les marchés bougent plus vite que les journaux... Sur mon Telegram gratuit, tu as l'actu géopolitique et financière décortiquée, "
     "mes analyses d'actions détaillées, et mes opportunités en temps réel. Plus de vingt-deux mille personnes y sont déjà... Entre dans le canal, lien en bio.")
beat(t, s, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Droits de douane : ce que l'Europe risque", "imgs": ["tg_3435c02c_top.jpg", "tg_1eaa56f0.jpg"], "subs": 22760,
       "subs_at_word": w(t, "personnes"), "bio_at_word": w(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
     cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})

DROP = [6, 11, 12]  # beats coupés au montage (durée)
B = [b for i, b in enumerate(B) if i not in DROP]
spec = {"id": EP, "date_label": "25 novembre 2026", "brand": "Invest Family Fr", "hook_type": "logowall", "hook_formula": "coupable inattendu",
        "cta_angle": "Les marchés bougent plus vite que les journaux : sur mon Telegram tu as l'info au moment où elle tombe", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://edgeconsultancykw.com/europe-market-wrap-25-november-2026/",
                    "https://whtc.com/2026/11/25/european-shares-rise-on-consumer-boost-markets-await-us-tariffs-inflation/",
                    "https://www.investing.com/news/stock-market-news/europe-stocks-climb-as-autos-luxury-rally-eyes-on-us-pce-fed-hike-bets-5049961",
                    "https://en.oninvest.com/article/stocks-in-europe-rose-in-contrast-to-declines-in-the-u-s-and-asia-what-makes-them-attractive",
                    "https://opb.org/article/2026/11/24/us-ready-to-slap-tariffs-on-china-eu-and-others-over-subsidized-production-ap-sources-say",
                    "https://newslantern.com/news/25381/2026-11-25/us-prepares-to-announce-tariffs-on-china-eu-and-14-other-economies"],
        "beats": B}
json.dump(spec, open(f'{D}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'{D}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), "beats", sum(len(b["say"].split()) for b in B), "mots")
