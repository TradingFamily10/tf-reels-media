import json, sys
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep37_tokyo_seisme'
def w(text, word):
    t = tokens(text)
    for i, x in enumerate(t):
        if word.lower() in x.lower():
            return i
    raise SystemExit(f"mot introuvable: {word} dans {text}")
def clip(n, ss=1, cx=0.5):
    return {"clip": f"b{n}.mp4", "ss": ss, "cx": cx}
B = []
def beat(text, say, bg, overlays, **kw):
    b = {"text": text, "say": say, "bg": bg, "overlays": overlays}; b.update(kw); B.append(b); return b
IL = "investingLive · 20 nov. 2026"
CC = "ChainCatcher · 20 nov. 2026"
FO = "Motley Fool · 19 nov. 2026, clôture"
STT = "StockTitan · 19 nov. 2026, clôture"

t = "Tout le monde regarde Anthropic. Le vrai séisme, il est à Tokyo."
beat(t, "Tout le monde regarde Anthropic... Le vrai séisme, il est à Tokyo.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "séisme"))]},
     [{"type": "date", "text": "Vendredi 20 novembre 2026 · Bourse de Tokyo", "until_beat": 0},
      {"type": "news", "at_word": 0, "left": "BOURSE DE TOKYO", "right": "20 NOV.", "tag": "ALERTE",
       "headline": "Le Nikkei chute jusqu'à 4,5 % et passe sous les 57 000 points",
       "highlight": "jusqu'à 4,5 %", "sub": IL},
      {"type": "stock", "key": "ANT", "name": "Anthropic", "sub": "ANT · Nasdaq · 1re séance hier", "y": 1380, "at_word": w(t, "Anthropic"), "until_word": w(t, "séisme")}])

t = "Le Nikkei a plongé jusqu'à 4,5 % ce matin."
beat(t, "Le Nikkei a plongé jusqu'à quatre pour cent et demi ce matin.",
     {"screen": True, "under": clip("1")},
     [{"type": "screen_counter", "kicker": "NIKKEI 225 · EN SÉANCE", "value_from": 0, "value_to": 4.5, "decimals": 1,
       "prefix": "− ", "suffix": " %", "color": "red", "pill": "PLUS BAS DEPUIS 2 SEMAINES", "desc": IL}])

t = "Et ce n'est pas le pire : à Séoul, le Kospi lâche plus de 4 %."
beat(t, "Et ce n'est pas le pire : à Séoul, le Kospi lâche plus de quatre pour cent.",
     {"shots": [clip("2"), dict(clip("2b"), at_word=w(t, "Séoul"))]},
     [{"type": "tickers", "title": "ASIE · CE VENDREDI MATIN", "rows": [
         {"name": "Nikkei 225", "pct": "−4,5 %", "at_word": 1, "up": False},
         {"name": "Topix", "pct": "−2,7 %", "at_word": w(t, "pire"), "up": False},
         {"name": "Kospi", "pct": "> −4 %", "at_word": w(t, "Kospi"), "up": False}]},
      {"type": "source", "text": IL}])

t = "SoftBank et Samsung chutent de plus de 5 % chacun."
beat(t, "SoftBank et Samsung chutent de plus de cinq pour cent chacun.",
     {"screen": True, "under": clip("3")},
     [{"type": "screen_logos", "kicker": "LES PUCES ET L'I.A. SANCTIONNÉES", "value_from": 0, "value_to": 5, "decimals": 0,
       "prefix": "> −", "suffix": " %", "color": "red", "pill": "CHACUNE", "keys": ["SFTBY", "SSU"],
       "desc": CC + " · " + IL}])

t = "Hier matin, le Nasdaq gagnait plus de 2 %. À la clôture, il en perdait plus de 2."
beat(t, "Hier matin, le Nasdaq gagnait plus de deux pour cent... À la clôture, il en perdait plus de deux.",
     {"screen": True, "under": clip("5")},
     [{"type": "screen_duo",
       "a": {"kicker": "NASDAQ · LE MATIN", "value_to": 2, "prefix": "> +", "suffix": " %", "color": "green", "desc": "Hausse en début de séance"},
       "b_at_word": w(t, "clôture"),
       "b": {"kicker": "NASDAQ · CLÔTURE", "value_to": -2.23, "decimals": 2, "prefix": "", "suffix": " %", "color": "red", "desc": "23 886 points · " + FO}}])

t = "Plus de 1 100 points effacés sur le Dow Jones. Et le S&P 500 aligne six séances de baisse d'affilée."
beat(t, "Plus de mille cent points effacés sur le Dow Jones... Et le S&P cinq cents aligne six séances de baisse d'affilée.",
     {"shots": [clip("6"), dict(clip("6b"), at_word=w(t, "S&P"))]},
     [{"type": "tickers", "title": "CLÔTURE DU 19 NOV.", "rows": [
         {"name": "Dow Jones", "pct": "−2,19 %", "at_word": w(t, "Dow"), "up": False},
         {"name": "S&P 500", "pct": "−2 %", "at_word": w(t, "S&P"), "up": False},
         {"name": "Série record", "pct": "6 SÉANCES", "at_word": w(t, "six"), "up": False}]},
      {"type": "source", "text": FO + " · plus longue série de baisse du S&P 500 depuis avril 2024"}])

t = "Alors, qui a gâché la fête ?"
beat(t, "Alors... qui a gâché la fête ?", clip("7"),
     [{"type": "bigtitle", "lines": ["QUI A GÂCHÉ", "LA FÊTE ?"], "at_word": w(t, "qui")}])

t = "Cette secousse, je la décortique en direct sur mon Telegram. Lien en bio."
beat(t, t, clip("8"),
     [{"type": "phone", "mode": "mini", "img": "tg_4b2fa9a8.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "La réponse : la plus grosse introduction en Bourse de l'histoire, Anthropic."
beat(t, "La réponse : la plus grosse introduction en Bourse de l'histoire... Anthropic.",
     clip("9"),
     [{"type": "stock", "key": "ANT", "name": "Anthropic", "sub": "ANT · Nasdaq · 1re séance le 19 nov.", "size": "big", "y": 600, "at_word": w(t, "Anthropic")},
      {"type": "source", "text": STT}])

t = "Premier cours : 111 dollars, pour un prix d'introduction fixé à 83."
beat(t, "Premier cours : cent onze dollars... pour un prix d'introduction fixé à quatre-vingt-trois.",
     {"screen": True, "under": clip("10")},
     [{"type": "screen_duo",
       "a": {"kicker": "1ER COURS · 11H48 NY", "value_to": 111.5, "decimals": 2, "prefix": "", "suffix": " $", "color": "green", "desc": STT, "logo": "ANT"},
       "b_at_word": w(t, "83"),
       "b": {"kicker": "PRIX D'INTRODUCTION", "value_to": 83, "prefix": "", "suffix": " $", "color": "gold", "desc": "Au-dessus de la fourchette 70-78 $", "logo": "ANT"}}])

t = "Mais à la clôture, le gain n'est plus que de 17 %."
beat(t, "Mais à la clôture, le gain n'est plus que de dix-sept pour cent.",
     {"screen": True, "under": clip("11")},
     [{"type": "screen_counter", "kicker": "ANTHROPIC · CLÔTURE 97,17 $", "value_from": 0, "value_to": 17, "decimals": 0,
       "prefix": "+", "suffix": " %", "color": "green", "pill": "CONTRE +34 % AU 1ER COURS", "desc": STT + " · " + FO},
      {"type": "stock", "key": "ANT", "name": "Anthropic", "sub": "Plus haut 114,99 $ · plus bas 92,72 $", "y": 1380, "at_word": w(t, "clôture")}])

t = "Pour s'offrir Anthropic, certains ont vendu leurs autres valeurs tech."
beat(t, "Pour s'offrir Anthropic... certains ont vendu leurs autres valeurs tech.",
     clip("12"),
     [{"type": "tickers", "title": "LES VICTIMES DU 19 NOV.", "rows": [
         {"name": "Anthropic", "pct": "+17,07 %", "at_word": w(t, "Anthropic"), "key": "ANT", "up": True},
         {"name": "Nvidia", "pct": "−3,30 %", "at_word": w(t, "certains"), "key": "NVDA", "up": False},
         {"name": "Alphabet", "pct": "−3,46 %", "at_word": w(t, "autres"), "key": "GOOGL", "up": False},
         {"name": "AMD", "pct": "−7,72 %", "at_word": w(t, "tech"), "key": "AMD", "up": False}]},
      {"type": "source", "text": IL + " · " + STT + " · " + FO}])

t = "Et le vrai danger est ailleurs : le taux américain à 10 ans tient au-dessus de 5 %."
beat(t, "Et le vrai danger est ailleurs : le taux américain à dix ans tient au-dessus de cinq pour cent.",
     {"screen": True, "under": clip("13")},
     [{"type": "screen_counter", "kicker": "TAUX US À 10 ANS", "value_from": 0, "value_to": 5.05, "decimals": 2,
       "prefix": "", "suffix": " %", "color": "red", "pill": "AU-DESSUS DE 5 %", "desc": FO + " · " + IL}])

t = "Les grandes banques attendent de nouvelles hausses de la Fed : décembre, janvier, mars."
beat(t, "Les grandes banques attendent de nouvelles hausses de la Fed : décembre, janvier, mars.",
     {"shots": [clip("14"), dict(clip("14b"), at_word=w(t, "Fed"))]},
     [{"type": "news", "at_word": 1, "left": "RÉSERVE FÉDÉRALE", "right": "20 NOV.", "tag": "TAUX",
       "headline": "Plusieurs grandes banques attendent des hausses de la Fed en décembre, janvier et mars",
       "highlight": "décembre, janvier et mars", "sub": IL}])

t = "Le VIX, l'indice de la peur, a frôlé 29, au plus haut depuis mars."
beat(t, "Le VIX, l'indice de la peur, a frôlé vingt-neuf... au plus haut depuis mars.",
     {"screen": True, "under": clip("15")},
     [{"type": "screen_gauge", "kicker": "VIX · PRÈS DE 29", "pill": "INDICE DE LA PEUR", "desc": "Au plus haut depuis mars · CNBC via " + STT}])

t = "Prochain test : Wall Street ce vendredi. Puis Tokyo, fermée lundi, rouvre mardi."
beat(t, "Prochain test : Wall Street ce vendredi... Puis Tokyo, fermée lundi, rouvre mardi.",
     clip("16"),
     [{"type": "tickers", "title": "À SURVEILLER", "rows": [
         {"name": "Wall Street", "pct": "VENDREDI", "at_word": w(t, "vendredi"), "up": True},
         {"name": "Tokyo · férié lundi", "pct": "MARDI", "at_word": w(t, "Tokyo"), "up": False}]},
      {"type": "source", "text": IL}])

t = "Alors, simple coup de froid, ou vrai retournement de l'IA ? Dis-le en commentaire."
beat(t, "Alors... simple coup de froid, ou vrai retournement de l'I.A. ? Dis-le en commentaire.", clip("17"),
     [{"type": "bigtitle", "lines": ["COUP DE FROID", "OU RETOURNEMENT ?"], "at_word": w(t, "simple")}])

t = ("Chaque matin, je fais le tri dans le bruit pour toi, sur mon Telegram gratuit : actu géopolitique et financière décortiquée, "
     "analyses d'actions détaillées, opportunités en temps réel. Plus de 22 000 personnes déjà. Entre dans le canal, lien en bio.")
say = t.replace("Plus de 22 000", "Plus de vingt-deux mille")
beat(t, say, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Tokyo −4,5 % : ce que ça change, mon analyse", "imgs": ["tg_38e4f34b.jpg", "tg_4b2fa9a8.jpg", "tg_1eaa56f0.jpg"],
       "subs": 22760, "subs_at_word": w(t, "22"), "bio_at_word": w(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
     cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "20 novembre 2026", "brand": "Invest Family Fr",
        "hook_type": "headline", "hook_formula": "personne n'en parle",
        "cta_angle": "Chaque matin, je fais le tri dans le bruit pour toi", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad",
                  "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://investinglive.com/stock-market-update/nikkei-slides-4-5-and-kospi-tumbles-as-wall-street-s-ai-reversal-hits-asian-chipmakers/",
                    "https://www.chaincatcher.com/en/article/2306529",
                    "https://www.stocktitan.net/articles/stock-market-today-live-november-19-2026",
                    "https://www.fool.com/coverage/stock-market-today/2026/11/19/stock-market-today-nov-19-stock-market-today-nov-19-alphabet-shares-fall-as-anthropic-nasdaq-debut-puts-fresh-value-on-google-s-stake/"],
        "beats": B}
json.dump(spec, open(f'/home/claude/kit/episodes/{EP}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'/home/claude/kit/episodes/{EP}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), sum(len(b["say"].split()) for b in B), "mots")
