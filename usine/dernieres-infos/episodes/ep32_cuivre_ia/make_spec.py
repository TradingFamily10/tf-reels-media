import json, sys
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
d = json.load(open('/home/claude/kit/assets/logos/logos.json'))
d['RIO'] = {"name": "Rio Tinto", "ticker": "RIO", "img": "RIO.png", "tile": "#FFFFFF", "fit": "84%"}
json.dump(d, open('/home/claude/kit/assets/logos/logos.json', 'w'), ensure_ascii=False, indent=1)

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

t = "Ce n'est pas la Chine qui fait plonger le cuivre. C'est l'intelligence artificielle."
beat(t, "Ce n'est pas la Chine qui fait plonger le cuivre... C'est l'intelligence artificielle.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "C'est"))]},
     [{"type": "date", "text": "Mercredi 18 novembre 2026 · métaux sous pression", "until_beat": 0},
      {"type": "news", "at_word": 0, "left": "MÉTAUX · LONDRES", "right": "18 NOV.", "tag": "ALERTE",
       "headline": "Le cuivre recule pour la 5e séance d'affilée, au plus bas depuis fin juin",
       "highlight": "5e séance d'affilée", "sub": "Reuters via Business Standard · 18 nov. 2026"}])

t = "Le cuivre vient d'enchaîner 5 séances de baisse. Au plus bas depuis fin juin."
beat(t, "Le cuivre vient d'enchaîner cinq séances de baisse... Au plus bas depuis fin juin.",
     {"screen": True, "under": clip("1")},
     [{"type": "screen_counter", "kicker": "CUIVRE LME · $ LA TONNE", "value_from": 14000, "value_to": 13078.5,
       "decimals": 0, "prefix": "", "suffix": "", "color": "red", "pill": "PLUS BAS DEPUIS FIN JUIN",
       "desc": "13 078,50 $ à 03h06 GMT · Reuters via Business Standard · 18 nov. 2026"}])

t = "Et ce n'est pas le pire : à New York, il a lâché près de 4 % en une matinée."
beat(t, "Et ce n'est pas le pire : à New York, il a lâché près de quatre pour cent en une matinée.",
     {"screen": True, "under": clip("2")},
     [{"type": "screen_counter", "kicker": "CUIVRE COMEX · EN %", "value_from": 0, "value_to": -3.8, "decimals": 1,
       "prefix": "", "suffix": " %", "color": "red", "pill": "5,76 $ LA LIVRE",
       "desc": "Contrat à terme · Investing.com · 18 nov. 2026"}])

t = "L'or plonge aussi : moins 2,4 % ce matin, à 3 778 dollars l'once."
beat(t, "L'or plonge aussi : plus de deux pour cent de baisse ce matin.",
     {"screen": True, "under": clip("3")},
     [{"type": "screen_duo",
       "a": {"kicker": "OR · RECORD DE JANVIER", "value_to": 5400, "decimals": 0, "prefix": "≈ ", "suffix": " $",
             "color": "white", "desc": "interactive investor · 17 nov. 2026"},
       "b_at_word": w(t, "moins"),
       "b": {"kicker": "OR · CE MATIN", "value_to": 3778, "decimals": 0, "prefix": "", "suffix": " $",
             "color": "red", "desc": "−2,4 % au comptant · Investing.com · 18 nov. 2026"}}])

t = "Résultat : près de 30 % sous son record de janvier. L'argent aussi décroche."
beat(t, "Résultat : près de trente pour cent sous son record de janvier... L'argent aussi décroche.",
     {"shots": [clip("4"), dict(clip("4b"), at_word=w(t, "L'argent"))]},
     [{"type": "tickers", "title": "L'OR ET L'ARGENT", "rows": [
          {"name": "Or · vs record", "pct": "−30 %", "at_word": 2, "up": False},
          {"name": "Or · ce matin", "pct": "−2,4 %", "at_word": 6, "up": False},
          {"name": "Argent", "pct": "−3,8 %", "at_word": w(t, "L'argent"), "up": False}]},
      {"type": "source", "text": "Investing.com · 18 nov. 2026 · interactive investor · 17 nov. 2026"}])

t = "En Europe, les minières chutent de 3 %, au plus bas depuis près de 9 mois."
beat(t, "En Europe, les minières chutent de trois pour cent... au plus bas depuis près de neuf mois.",
     {"shots": [clip("5"), dict(clip("5b"), at_word=w(t, "bas"))]},
     [{"type": "news", "at_word": 2, "left": "STOXX 600 · MINES", "right": "18 NOV.", "tag": "SECTEUR",
       "headline": "Le secteur minier européen recule de 3 %, au plus bas depuis près de 9 mois",
       "highlight": "−3 %".replace("−", "") if False else "3 %", "sub": "Reuters via Investing.com · 18 nov. 2026"}])

t = "Rio Tinto a encore perdu 112 pence hier à Londres."
beat(t, "Rio Tinto a encore perdu cent douze pence hier à Londres.",
     {"clip": "b6.mp4", "ss": 1, "cx": 0.5},
     [{"type": "stock", "key": "RIO", "name": "Rio Tinto", "sub": "Londres · 6 038 pence · 17 nov.", "pct": "−1,8 %",
       "up": False, "size": "big", "y": 600, "at_word": 0},
      {"type": "source", "text": "interactive investor · 17 nov. 2026"}])

t = "Alors, qui a tiré le premier ?"
beat(t, "Alors... qui a tiré le premier ?", {"clip": "b7.mp4", "ss": 1, "cx": 0.5},
     [{"type": "bigtitle", "lines": ["QUI A TIRÉ", "LE PREMIER ?"], "at_word": 1}])

t = "Cette chute des métaux, je la suis en direct sur mon Telegram. Lien en bio."
beat(t, t, {"clip": "b8.mp4", "ss": 1, "cx": 0.5},
     [{"type": "phone", "mode": "mini", "img": "tg_38e4f34b.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "Le coupable, c'est le doute sur l'I.A. Moins de data centers, c'est moins de réseaux électriques. Donc moins de cuivre."
beat(t, "Le coupable, c'est le doute sur l'I.A.... Moins de data centers, c'est moins de réseaux électriques. Donc moins de cuivre.",
     {"shots": [clip("9"), dict(clip("9b"), at_word=w(t, "Moins"))]},
     [{"type": "news", "at_word": w(t, "Moins"), "left": "TD SECURITIES · ANALYSE", "right": "18 NOV.", "tag": "CITATION",
       "headline": "L'incertitude sur les investissements dans les data centers d'IA affaiblit un pilier de la demande de cuivre",
       "highlight": "data centers d'IA", "sub": "Reuters via Business Standard · 18 nov. 2026"}])

t = "Le baromètre de l'I.A., Nvidia, a perdu 35 % depuis son record d'octobre."
beat(t, "Le baromètre de l'I.A., Nvidia, a perdu trente-cinq pour cent depuis son record d'octobre.",
     {"clip": "b10.mp4", "ss": 1, "cx": 0.5},
     [{"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "Nasdaq · depuis le record d'octobre", "pct": "≈ −35 %",
       "up": False, "size": "big", "y": 600, "at_word": w(t, "Nvidia")},
      {"type": "source", "text": "interactive investor · 17 nov. 2026"}])

t = "Deuxième coupable : le dollar, tout près de son plus haut depuis 19 mois."
beat(t, "Deuxième coupable : le dollar, tout près de son plus haut depuis dix-neuf mois.",
     {"screen": True, "under": clip("11")},
     [{"type": "screen_counter", "kicker": "DOLLAR · PLUS HAUT DEPUIS", "value_from": 0, "value_to": 19, "decimals": 0,
       "prefix": "", "suffix": " MOIS", "color": "gold", "pill": "UN DOLLAR FORT PÈSE SUR LES MÉTAUX",
       "desc": "Reuters via Business Standard · 18 nov. 2026"}])

t = "Car la Fed parle de remonter ses taux. Christopher Waller a même évoqué un demi-point en décembre."
beat(t, "Car la Fed parle de remonter ses taux... Christopher Waller a même évoqué un demi-point en décembre.",
     {"shots": [clip("12"), dict(clip("12b"), at_word=w(t, "Christopher"))]},
     [{"type": "news", "at_word": w(t, "Christopher"), "left": "FED · CHRISTOPHER WALLER", "right": "10 NOV.", "tag": "CITATION",
       "headline": "« Monter de 25 points de base seulement mettrait notre crédibilité en danger »",
       "highlight": "crédibilité", "sub": "Une hausse de 50 points « devrait être envisagée » · Kitco · 10 nov. 2026"}])

t = "Même à Londres, l'inflation remonte à 3,6 %. Et une hausse de taux est attendue en décembre."
beat(t, "Même à Londres, l'inflation remonte à plus de trois et demi pour cent... Et une hausse de taux est attendue en décembre.",
     {"screen": True, "under": clip("13")},
     [{"type": "screen_counter", "kicker": "INFLATION R.-U. · OCTOBRE", "value_from": 0, "value_to": 3.6, "decimals": 1,
       "prefix": "", "suffix": " %", "color": "red", "pill": "≈ 90 % DE CHANCES D'UNE HAUSSE EN DÉCEMBRE",
       "desc": "3,5 % en septembre · Investing.com · 18 nov. 2026"}])

t = "À surveiller ce soir : les minutes de la Fed. Un mot de trop, et les métaux peuvent encore bouger."
beat(t, "À surveiller ce soir : les minutes de la Fed... Un mot de trop, et les métaux peuvent encore bouger.",
     {"clip": "b14.mp4", "ss": 1, "cx": 0.5},
     [{"type": "tickers", "title": "À SURVEILLER", "rows": [
         {"name": "Minutes Fed", "pct": "CE SOIR", "at_word": w(t, "minutes"), "up": True},
         {"name": "Rio Tinto", "pct": "−1,8 %", "at_word": w(t, "métaux"), "key": "RIO", "up": False},
         {"name": "Nvidia", "pct": "15H30", "at_word": w(t, "bouger"), "key": "NVDA", "up": True}]},
      {"type": "source", "text": "Agenda Newsquawk · 18 nov. 2026"}])

t = "Alors, le cuivre est-il le premier à sentir la fin de la fête de l'I.A. ? Dis-le en commentaire."
beat(t, "Alors... le cuivre est-il le premier à sentir la fin de la fête de l'I.A. ? Dis-le en commentaire.",
     {"clip": "b15.mp4", "ss": 1, "cx": 0.5},
     [{"type": "bigtitle", "lines": ["LA FIN DE LA FÊTE", "DE L'I.A. ?"], "at_word": w(t, "fin")}])

t = ("Plus de 22 000 personnes ont déjà une longueur d'avance sur mon canal Telegram gratuit : l'actu géopolitique et "
     "financière décortiquée, des analyses d'actions détaillées et les opportunités en temps réel. Il ne manque plus que toi. Lien en bio.")
say = t.replace("Plus de 22 000", "Plus de vingt-deux mille")
beat(t, say, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Cuivre, or, I.A. : ce qui se joue vraiment", "imgs": ["tg_3435c02c.jpg", "tg_4b2fa9a8.jpg", "tg_1eaa56f0.jpg"],
       "subs": 22760, "subs_at_word": w(t, "22"), "bio_at_word": w(t, "bio"), "button": "ACCÈS GRATUIT"}],
     cta="long", endcard={"duration": 1.8, "button": "ACCÈS GRATUIT", "small": "Telegram gratuit · lien en bio"})

spec = {"id": "ep32_cuivre_ia", "date_label": "18 novembre 2026", "brand": "Invest Family Fr",
        "hook_type": "headline", "hook_formula": "coupable inattendu",
        "cta_angle": "22 000 personnes ont déjà la longueur d'avance. Il manque toi.", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad",
                  "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.business-standard.com/markets/commodities/copper-falls-to-near-five-month-low-as-firm-dollar-ai-concerns-weigh-126111800283_1.html",
                    "https://www.investing.com/news/stock-market-news/ftse-100-today-stocks-slip-as-miners-sink-on-metals-rout-cpi-at-36-5035095",
                    "https://www.investing.com/news/stock-market-news/european-shares-muted-as-tech-offsets-mining-weakness-5035128",
                    "https://www.ii.co.uk/analysis-commentary/another-tech-slump-ai-confusion-and-big-ftse-100-losses-ii540918",
                    "https://www.kitco.com/news/article/2026-11-10/feds-waller-and-logan-signal-readiness-hike-higher-and-faster-50-bps-table",
                    "https://www.newsquawk.com/headlines/newsquawk-daily-european-opening-news---18th-november-2026"],
        "beats": B}
json.dump(spec, open('/home/claude/kit/episodes/ep32_cuivre_ia/spec.json', 'w'), ensure_ascii=False, indent=1)
open('/home/claude/kit/episodes/ep32_cuivre_ia/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), sum(len(b["say"].split()) for b in B), "mots")
