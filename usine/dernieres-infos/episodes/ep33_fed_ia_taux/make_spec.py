import json, sys
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep33_fed_ia_taux'

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

t = "Et si l'I.A. obligeait la Fed à remonter ses taux ?"
beat(t, "Et si l'I.A.... obligeait la Fed à remonter ses taux ?",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "Fed"))]},
     [{"type": "date", "text": "Mercredi 18 novembre 2026 · avant Wall Street", "until_beat": 1},
      {"type": "bigtitle", "lines": ["L'I.A. VA FAIRE", "MONTER LES TAUX ?"], "at_word": 0},
      {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "NVDA · avant-Bourse · Reuters", "pct": "+3,7 %",
       "up": True, "y": 1420, "at_word": w(t, "remonter")}])

t = "Ce matin, Wall Street respire : le Nasdaq 100 gagne plus de 1 % avant l'ouverture."
beat(t, "Ce matin, Wall Street respire : le Nasdaq cent gagne plus d'un pour cent avant l'ouverture.",
     {"screen": True, "under": clip("1")},
     [{"type": "screen_counter", "kicker": "NASDAQ 100 · AVANT-BOURSE", "value_from": 0, "value_to": 1.17,
       "decimals": 2, "prefix": "+", "suffix": " %", "color": "green", "pill": "APRÈS DEUX SÉANCES DE BAISSE",
       "desc": "+315,5 points à 4h53 (New York) · Reuters · 18 nov. 2026"}])

t = "Nvidia rebondit de 3,7 % après ses résultats. CoreWeave, plus de 6 %. Micron, plus de 3 %."
beat(t, "Nvidia rebondit de près de quatre pour cent après ses résultats. CoreWeave, plus de six pour cent. Micron, plus de trois pour cent.",
     {"shots": [clip("2"), dict(clip("2b"), at_word=w(t, "CoreWeave"))]},
     [{"type": "tickers", "title": "AVANT-BOURSE · 18 NOV.", "rows": [
          {"name": "Nvidia", "pct": "+3,7 %", "at_word": 0, "key": "NVDA", "up": True},
          {"name": "CoreWeave", "pct": "+6,5 %", "at_word": w(t, "CoreWeave"), "key": "CRWV", "up": True},
          {"name": "Micron", "pct": "+3,4 %", "at_word": w(t, "Micron"), "key": "MU", "up": True},
          {"name": "AMD", "pct": "+3 %", "at_word": w(t, "Micron") + 2, "key": "AMD", "up": True}]},
      {"type": "source", "text": "Reuters via Yahoo Finance · 18 nov. 2026"}])

t = "Mais derrière ce rebond, un signal bien plus inquiétant vient de tomber."
beat(t, "Mais derrière ce rebond... un signal bien plus inquiétant vient de tomber.",
     {"clip": "b3.mp4", "ss": 1, "cx": 0.5},
     [{"type": "bigtitle", "lines": ["UN SIGNAL", "INQUIÉTANT"], "at_word": w(t, "signal")}])

t = "Hier, le patron de la Fed de New York, John Williams, a lâché cette phrase."
beat(t, "Hier, le patron de la Fed de New York, John Williams, a lâché cette phrase.",
     {"shots": [clip("4"), dict(clip("4b", ss=3), at_word=w(t, "John"))]},
     [{"type": "news", "at_word": w(t, "John"), "left": "FED DE NEW YORK · JOHN WILLIAMS", "right": "17 NOV.", "tag": "CITATION",
       "headline": "« L'inflation, malheureusement, ne va pas dans la bonne direction »",
       "highlight": "pas dans la bonne direction", "sub": "Sommet Axios, New York · Reuters · 17 nov. 2026"}])

t = "Selon lui, la Fed devra sans doute remonter ses taux. Pas de façon brutale. Mais encore."
beat(t, "Selon lui, la Fed devra sans doute remonter ses taux... Pas de façon brutale. Mais encore.",
     {"clip": "b5.mp4", "ss": 1, "cx": 0.5},
     [{"type": "news", "at_word": 0, "left": "REUTERS · FED", "right": "17 NOV.", "tag": "ALERTE",
       "headline": "Williams : la Fed devra probablement relever encore ses taux, sans « action spectaculaire »",
       "highlight": "relever encore ses taux", "sub": "Reuters · 17 nov. 2026"}])

t = "Aujourd'hui, ses taux directeurs sont entre 3,75 et 4 %."
beat(t, "Aujourd'hui, ses taux directeurs vont jusqu'à quatre pour cent.",
     {"screen": True, "under": clip("6")},
     [{"type": "screen_counter", "kicker": "TAUX DE LA FED · PLAFOND", "value_from": 0, "value_to": 4,
       "decimals": 0, "prefix": "", "suffix": " %", "color": "gold", "pill": "FOURCHETTE : 3,75 % À 4 %",
       "desc": "Reuters · 17 nov. 2026"}])

t = "Et les marchés misent à 93 % sur une hausse dès décembre."
beat(t, "Et les marchés misent à plus de quatre-vingt-dix pour cent sur une hausse dès décembre.",
     {"screen": True, "under": clip("7", cx=0.78)},
     [{"type": "screen_counter", "kicker": "PROBABILITÉ D'UNE HAUSSE DE 0,25 PT", "value_from": 0, "value_to": 93,
       "decimals": 0, "prefix": "", "suffix": " %", "color": "red", "pill": "RÉUNION DES 8 ET 9 DÉCEMBRE",
       "desc": "CME FedWatch via TheStreet · 15 nov. 2026"}])

t = "Alors, pourquoi monter les taux quand la Bourse vacille ?"
beat(t, "Alors... pourquoi monter les taux quand la Bourse vacille ?",
     {"clip": "b8.mp4", "ss": 1, "cx": 0.5},
     [{"type": "bigtitle", "lines": ["POURQUOI MONTER", "LES TAUX ?"], "at_word": 1}])

t = "Cette bataille de la Fed, je la décortique en direct sur mon Telegram. Lien en bio."
beat(t, t, {"clip": "b9.mp4", "ss": 1, "cx": 0.5},
     [{"type": "phone", "mode": "mini", "img": "tg_1eaa56f0.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "La réponse, c'est l'I.A. elle-même. Williams le dit : la force de l'économie vient de la vague d'investissements dans l'I.A."
beat(t, "La réponse... c'est l'I.A. elle-même. Williams le dit : la force de l'économie vient de la vague d'investissements dans l'I.A.",
     {"shots": [clip("10"), dict(clip("10b"), at_word=w(t, "Williams"))]},
     [{"type": "news", "at_word": w(t, "Williams"), "left": "JOHN WILLIAMS · FED DE NEW YORK", "right": "17 NOV.", "tag": "CITATION",
       "headline": "« Une grande partie de la vigueur de l'économie américaine vient de la vague d'investissements dans l'I.A. »",
       "highlight": "investissements dans l'I.A.", "sub": "Stocktwits · 17 nov. 2026"}])

t = "Des data centers, de l'électricité, des puces : l'économie tourne fort. Et l'inflation ne baisse plus."
beat(t, "Des data centers, de l'électricité, des puces : l'économie tourne fort... Et l'inflation ne baisse plus.",
     {"shots": [clip("11"), dict(clip("11b"), at_word=w(t, "l'électricité")), dict(clip("11c", cx=0.3), at_word=w(t, "puces"))]},
     [{"type": "screen_logos", "kicker": "LES GÉANTS DE L'I.A.", "value_to": 5, "suffix": "", "keys": ["NVDA", "MSFT", "GOOGL", "ORCL", "CRWV"],
       "at_word": 0, "desc": "Clients des puces Nvidia Vera Rubin · résultats Nvidia · 17 nov. 2026"}]
     if False else
     [{"type": "source", "text": "Inflation d'octobre plus forte que prévu · TheStreet · 15 nov. 2026"}])

t = "Résultat : le taux américain à 10 ans grimpe à 5,10 %. Et l'or recule de plus de 2 %."
beat(t, "Résultat : le taux américain à dix ans dépasse cinq pour cent... Et l'or recule de plus de deux pour cent.",
     {"screen": True, "under": clip("12")},
     [{"type": "screen_duo",
       "a": {"kicker": "TAUX US À 10 ANS", "value_to": 5.10, "decimals": 2, "prefix": "", "suffix": " %",
             "color": "red", "desc": "Yahoo Finance · 18 nov. 2026"},
       "b_at_word": w(t, "l'or"),
       "b": {"kicker": "OR · CE MATIN", "value_to": 3772, "decimals": 0, "prefix": "", "suffix": " $",
             "color": "red", "desc": "−2,4 % · Yahoo Finance · 18 nov. 2026"}}])

t = "Et en octobre, deux membres de la Fed voulaient déjà monter les taux. Vote : 10 contre 2."
beat(t, "Et en octobre, deux membres de la Fed voulaient déjà monter les taux. Vote : dix contre deux.",
     {"screen": True, "under": clip("13")},
     [{"type": "screen_vote", "kicker": "VOTE FED · OCTOBRE",
       "groups": [{"n": 10, "label": "PAUSE", "color": "gold"}, {"n": 2, "label": "HAUSSE", "color": "red"}],
       "desc": "Dont Beth Hammack (Fed de Cleveland) · TheStreet · 15 nov. 2026"}])

t = "À surveiller : ce soir, les minutes de la Fed. Puis le verdict, le 9 décembre."
beat(t, "À surveiller : ce soir, les minutes de la Fed... Puis le verdict, le neuf décembre.",
     {"clip": "b14.mp4", "ss": 1, "cx": 0.5},
     [{"type": "tickers", "title": "À SURVEILLER", "rows": [
         {"name": "Nvidia", "pct": "15H30", "at_word": 0, "key": "NVDA", "up": True},
         {"name": "Minutes Fed", "pct": "CE SOIR", "at_word": w(t, "minutes"), "up": True},
         {"name": "Décision Fed", "pct": "9 DÉC.", "at_word": w(t, "verdict"), "up": False}]},
      {"type": "source", "text": "Yahoo Finance · Reuters · 17-18 nov. 2026"}])

t = "Alors, l'I.A. va-t-elle porter la Bourse… ou la faire trébucher ? Dis-le en commentaire."
beat(t, "Alors... l'I.A. va-t-elle porter la Bourse... ou la faire trébucher ? Dis-le en commentaire.",
     {"clip": "b15.mp4", "ss": 1, "cx": 0.5},
     [{"type": "bigtitle", "lines": ["PORTER LA BOURSE", "OU LA COULER ?"], "at_word": w(t, "porter")}])

t = ("Si tu veux comprendre avant les autres au lieu de subir, rejoins mon canal Telegram gratuit. Plus de 22 000 personnes y lisent "
     "l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées et les opportunités en temps réel. Lien en bio.")
say = t.replace("Plus de 22 000", "Plus de vingt-deux mille")
beat(t, say, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Fed, I.A., taux : ce qui t'attend en décembre", "imgs": ["tg_38e4f34b.jpg", "tg_4b2fa9a8.jpg", "tg_3435c02c_top.jpg"],
       "subs": 22760, "subs_at_word": w(t, "22"), "bio_at_word": w(t, "bio"), "button": "REJOINS LA FAMILLE"}],
     cta="long", endcard={"duration": 1.8, "button": "REJOINS LA FAMILLE", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "18 novembre 2026", "brand": "Invest Family Fr",
        "hook_type": "question", "hook_formula": "question directe",
        "cta_angle": "Si tu veux comprendre avant les autres au lieu de subir", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad",
                  "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://finance.yahoo.com/markets/stocks/articles/nasdaq-futures-jump-nvidia-forecast-103531610.html",
                    "https://finance.yahoo.com/markets/live/stock-market-today-wednesday-november-18-dow-sp-500-nasdaq-nvidia-anthropic-ipo-090613569.html",
                    "https://www.1049thewolf.com/2026/11/17/feds-williams-still-favors-tighter-monetary-policy-but-says-now-is-not-the-time-for-dramatic-action/",
                    "https://www.thestreet.com/fed/fed-rate-hike-fears-december-inflation-2027",
                    "https://stocktwits.com/news-articles/markets/equity/new-york-fed-s-john-williams-hints-towards-more-rate-hikes-amid-ai-boom/cNbOBFMR9hX"],
        "beats": B}
json.dump(spec, open(f'/home/claude/kit/episodes/{EP}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'/home/claude/kit/episodes/{EP}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), sum(len(b["say"].split()) for b in B), "mots")
