import json, sys, os
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep59_france_inflation_pib'
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
def clip0(n, ss=None, cx=None):
    return {"clip": f"b{n}.mp4", "ss": SS.get(n, 1) if ss is None else ss, "cx": CX.get(n, 0.5) if cx is None else cx}
def clip(n, ss=None, cx=None):
    d = clip0(n, ss, cx)
    if n == "14": d["inset"] = 0.05
    return d
def scr(n): return {"screen": True, "under": clip(n)}
B = []
def beat(text, say, bg, overlays, **kw):
    b = {"text": text, "say": say, "bg": bg, "overlays": overlays}; b.update(kw); B.append(b); return b
INV = "Investing.com · 26 nov. 2026"
FE = "France Épargne / Insee · 27 nov. 2026"
XTB = "XTB · 27 nov. 2026"
EP_ = "Echos Plus / Insee · 27 nov. 2026"
AFP = "AFP / Boursorama · 27 nov. 2026 · 10h27"
ZB = "Zonebourse / Boursorama · 27 nov. 2026"
EN = "Euronews · 31 oct. 2026"

t = "L'inflation française chute bien plus que prévu. Et pourtant, la France a de quoi s'inquiéter."
beat(t, "L'inflation française chute... bien plus que prévu. Et pourtant, la France a de quoi s'inquiéter.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "pourtant"))]},
     [{"type": "date", "text": "Vendredi 27 novembre 2026 · Paris", "until_beat": 0},
      {"type": "news", "at_word": 0, "left": "INSEE · ESTIMATION PROVISOIRE", "right": "27 NOV.", "tag": "CONTRE-INTUITIF",
       "headline": "L'inflation ralentit à 2,9 % sur un an en novembre, alors que les économistes attendaient 3,2 %",
       "highlight": "2,9 %", "sub": FE + " · " + XTB}])

t = "2,9 % sur un an en novembre. Les économistes attendaient 3,2 %."
beat(t, "Moins de trois pour cent sur un an en novembre... Les économistes attendaient plus de trois pour cent.", scr("1"),
     [{"type": "screen_duo", "a": {"kicker": "CONSENSUS · NOVEMBRE", "value_to": 3.2, "decimals": 1, "prefix": "", "suffix": " %", "color": "white", "desc": "Prévision des économistes"},
       "b_at_word": w(t, "économistes"), "b": {"kicker": "INSEE · NOVEMBRE", "value_to": 2.9, "decimals": 1, "prefix": "", "suffix": " %", "color": "green", "desc": "Contre 3,4 % en octobre"}},
      {"type": "source", "text": FE}])

t = "Et ce n'est pas le plus important : le même matin, l'Insee annonce que l'économie a reculé."
beat(t, "Et ce n'est pas le plus important... le même matin, l'Insee annonce un recul de l'économie.",
     {"shots": [clip("2"), dict(clip("3"), at_word=w(t, "Insee"))]},
     [{"type": "bigtitle", "lines": ["LE MÊME MATIN", "L'ÉCONOMIE RECULE"], "at_word": w(t, "matin")}])

t = "Le PIB du troisième trimestre recule de 0,2 %. Pire que la première estimation."
beat(t, "Le P.I.B. du troisième trimestre recule... Et c'est pire que la première estimation.", scr("3"),
     [{"type": "screen_counter", "kicker": "FRANCE · PIB · T3 2026", "value_from": 0, "value_to": -0.2, "decimals": 1, "prefix": "", "suffix": " %", "color": "red", "pill": "RÉVISÉ EN BAISSE", "desc": "Première estimation : −0,1 % · " + EP_}])

t = "Les exportations plongent de 1,6 %. L'investissement recule de 0,9 %."
beat(t, "Les exportations plongent... L'investissement recule, lui aussi.", scr("4"),
     [{"type": "screen_duo", "a": {"kicker": "EXPORTATIONS · T3", "value_to": -1.6, "decimals": 1, "prefix": "", "suffix": " %", "color": "red", "desc": "Après +2,9 % au T2"},
       "b_at_word": w(t, "investissement"), "b": {"kicker": "INVESTISSEMENT · T3", "value_to": -0.9, "decimals": 1, "prefix": "", "suffix": " %", "color": "red", "desc": "Après −0,5 % au T2"}},
      {"type": "source", "text": EP_}])

t = "Le gouvernement vise 0,5 % de croissance en 2026. L'acquis n'est que de 0,1 %."
beat(t, "Le gouvernement vise un demi-point de croissance cette année... L'acquis, lui, est presque nul.", scr("5"),
     [{"type": "screen_duo", "a": {"kicker": "OBJECTIF DU GOUVERNEMENT · 2026", "value_to": 0.5, "decimals": 1, "prefix": "", "suffix": " %", "color": "white", "desc": "Rapport annexé au PLF 2027"},
       "b_at_word": w(t, "acquis"), "b": {"kicker": "ACQUIS FIN SEPTEMBRE", "value_to": 0.1, "decimals": 1, "prefix": "", "suffix": " %", "color": "red", "desc": "Acquis de croissance 2026"}},
      {"type": "source", "text": EP_}])

t = "Alors, pourquoi les prix ralentissent-ils, si l'économie cale ?"
beat(t, "Alors... pourquoi les prix ralentissent-ils, si l'économie cale ?", clip("6"),
     [{"type": "bigtitle", "lines": ["LES PRIX FREINENT", "L'ÉCONOMIE CALE"], "at_word": 1}])

t = "Ce dossier France, je le suis en direct sur mon Telegram. Lien en bio."
beat(t, t, clip("7"),
     [{"type": "phone", "mode": "mini", "img": "tg_38e4f34b.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "La réponse, c'est l'énergie : sa hausse sur un an passe de 24,1 % à 19,2 %."
beat(t, "La réponse, c'est l'énergie... sa hausse sur un an passe de vingt-quatre à dix-neuf pour cent.", scr("8"),
     [{"type": "screen_duo", "a": {"kicker": "ÉNERGIE · OCTOBRE", "value_to": 24.1, "decimals": 1, "prefix": "+", "suffix": " %", "color": "red", "desc": "Sur un an"},
       "b_at_word": w(t, "19,2"), "b": {"kicker": "ÉNERGIE · NOVEMBRE", "value_to": 19.2, "decimals": 1, "prefix": "+", "suffix": " %", "color": "white", "desc": "Toujours en hausse, mais moins vite"}},
      {"type": "source", "text": FE}])

t = "Sur un seul mois, les prix baissent même de 0,7 %."
beat(t, "Sur un seul mois, les prix baissent même... de presque un pour cent.", scr("9"),
     [{"type": "screen_counter", "kicker": "PRIX À LA CONSOMMATION · NOVEMBRE", "value_from": 0, "value_to": -0.7, "decimals": 1, "prefix": "", "suffix": " %", "color": "green", "pill": "SUR UN MOIS", "desc": "Après +0,4 % en octobre · " + FE}])

t = "Mais ton Livret A, à 1,7 %, reste 1,2 point sous l'inflation."
beat(t, "Mais ton Livret A... reste encore plus d'un point sous l'inflation.", scr("10"),
     [{"type": "screen_duo", "a": {"kicker": "LIVRET A", "value_to": 1.7, "decimals": 1, "prefix": "", "suffix": " %", "color": "white", "desc": "Taux actuel"},
       "b_at_word": w(t, "reste"), "b": {"kicker": "INFLATION · NOVEMBRE", "value_to": 2.9, "decimals": 1, "prefix": "", "suffix": " %", "color": "red", "desc": "Écart : 1,2 point"}},
      {"type": "source", "text": FE}])

t = "À Paris, le CAC 40 grappille 0,3 %, porté par STMicro. Sanofi recule."
beat(t, "À Paris, le CAC quarante grappille un peu de terrain, porté par S.T. Micro. Sanofi recule.", scr("11"),
     [{"type": "tickers", "title": "BOURSE DE PARIS · VENDREDI 27 NOV. · 10H15", "rows": [
         {"key": "STM", "name": "STMicroelectronics", "pct": "+4,77 %", "up": True, "at_word": w(t, "CAC")},
         {"key": "SOI", "name": "Soitec", "pct": "+5,78 %", "up": True, "at_word": w(t, "grappille")},
         {"key": "SNY", "name": "Sanofi", "pct": "−2,08 %", "up": False, "at_word": w(t, "Sanofi")}]},
      {"type": "source", "text": "CAC 40 +0,29 % à 8 132 pts · " + AFP}])

t = "Mais le vrai test tombe ce soir : S&P doit se prononcer sur la note de la France."
beat(t, "Mais le vrai test tombe ce soir... Standard and Poor's doit se prononcer sur la note de la France.", clip("13"),
     [{"type": "news", "at_word": w(t, "S&P"), "left": "DETTE FRANÇAISE", "right": "CE SOIR", "tag": "NOTATION",
       "headline": "La décision de S&P sur la note de la France, « A+ » perspective stable, est attendue après la clôture",
       "highlight": "après la clôture", "sub": AFP}])

t = "Fin octobre, Fitch avait déjà passé sa perspective en négatif."
beat(t, "Fin octobre, Fitch avait déjà passé sa perspective... en négatif.", clip("14"),
     [{"type": "news", "at_word": 1, "left": "FITCH", "right": "30 OCT.", "tag": "PERSPECTIVE",
       "headline": "Fitch maintient la note A+ de la France mais abaisse sa perspective à « négative »",
       "highlight": "négative", "sub": EN}])

t = "Et la France emprunte déjà à 4,73 % sur dix ans, contre 3,28 % pour l'Allemagne."
beat(t, "Et la France emprunte déjà bien plus cher que l'Allemagne... sur dix ans.", scr("15"),
     [{"type": "screen_duo", "a": {"kicker": "FRANCE · OAT 10 ANS", "value_to": 4.73, "decimals": 2, "prefix": "", "suffix": " %", "color": "red", "desc": "Taux d'emprunt"},
       "b_at_word": w(t, "Allemagne"), "b": {"kicker": "ALLEMAGNE · BUND 10 ANS", "value_to": 3.28, "decimals": 2, "prefix": "", "suffix": " %", "color": "white", "desc": "Taux d'emprunt"}},
      {"type": "source", "text": AFP}])

t = "Moins d'inflation, mais moins de croissance : bonne nouvelle, ou signal d'alarme ?"
beat(t, "Moins d'inflation, mais moins de croissance... bonne nouvelle, ou signal d'alarme ?", clip("17"),
     [{"type": "bigtitle", "lines": ["BONNE NOUVELLE", "OU SIGNAL D'ALARME ?"], "at_word": w(t, "bonne")}])

t = ("Ce soir, pendant que S&P tranche, mes abonnés auront l'analyse dans la minute. Rejoins plus de 22 000 personnes sur mon Telegram gratuit : "
     "actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. Lien en bio.")
s = ("Ce soir, pendant que Standard and Poor's tranche... mes abonnés auront l'analyse dans la minute. Rejoins plus de vingt-deux mille personnes sur mon Telegram gratuit : "
     "actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. Lien en bio.")
beat(t, s, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Note de la France : la décision de S&P décryptée en direct",
       "imgs": ["tg_3435c02c.jpg", "tg_1eaa56f0.jpg", "tg_4b2fa9a8.jpg"], "subs": 22760,
       "subs_at_word": w(t, "22"), "bio_at_word": w(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
     cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "27 novembre 2026", "brand": "Invest Family Fr", "hook_type": "headline",
        "hook_formula": "contre-intuitif", "cta_angle": "Ce soir, pendant que S&P tranche, mes abonnés auront l'analyse dans la minute",
        "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": [
            "https://www.france-epargne.fr/news/linflation-francaise-ralentit-bien-plus-que-prevu-en-novembre-freinee-par-lenergie",
            "https://www.xtb.com/int/market-analysis/news-and-research/economic-calendar-inflation-in-europe-surprises-to-the-downside-27-11-2026",
            "https://echosplus.com/2026/11/27/france-le-pib-recule-de-02-au-troisieme-trimestre-la-prevision-de-croissance-fragilisee/",
            "https://www.boursorama.com/bourse/actualites/bourse-de-paris-hausse-timide-avant-le-retour-de-wall-street-8018d81d7734ab5fa10def645e72679c",
            "https://www.boursorama.com/bourse/actualites/l-attrait-pour-le-risque-revient-sur-les-places-europeennes-901debe20470f41dcb36d9fb64f8adca",
            "https://fr.euronews.com/2026/10/31/dette-fitch-degrade-la-perspective-de-la-france-a-negative"],
        "beats": B}
json.dump(spec, open(f'{D}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'{D}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), "beats", sum(len(b["say"].split()) for b in B), "mots")
