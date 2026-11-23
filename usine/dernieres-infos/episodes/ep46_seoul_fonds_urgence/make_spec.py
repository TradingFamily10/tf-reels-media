import json, sys
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep46_seoul_fonds_urgence'
def w(text, word, n=0):
    t = tokens(text); k = 0
    for i, x in enumerate(t):
        if word.lower() in x.lower():
            if k == n: return i
            k += 1
    raise SystemExit(f"mot introuvable: {word} dans {text}")
CX = json.load(open(f'/home/claude/kit/episodes/{EP}/cx.json')) if __import__('os').path.exists(f'/home/claude/kit/episodes/{EP}/cx.json') else {}
SS = json.load(open(f'/home/claude/kit/episodes/{EP}/ss.json')) if __import__('os').path.exists(f'/home/claude/kit/episodes/{EP}/ss.json') else {}
def clip(n, ss=None, cx=None):
    return {"clip": f"b{n}.mp4", "ss": SS.get(n, 1) if ss is None else ss, "cx": CX.get(n, 0.5) if cx is None else cx}
def scr(n): return {"screen": True, "under": clip(n)}
B = []
def beat(text, say, bg, overlays, **kw):
    b = {"text": text, "say": say, "bg": bg, "overlays": overlays}; b.update(kw); B.append(b); return b
AJ = "Al Jazeera · 23 nov. 2026"
KH = "Kaohoon International · 23 nov. 2026"
SE = "Seoul Economic Daily · 23 nov. 2026"
SBS = "SBS · 23 nov. 2026"
FO = "Fortune · 22 nov. 2026, 19h13 (New York)"

t = "Wall Street promet un rebond. Et pourtant, la Bourse de Séoul plonge de plus de 5 % ce lundi."
beat(t, "Wall Street promet un rebond... Et pourtant, la Bourse de Séoul plonge de plus de cinq pour cent ce lundi.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "pourtant"))]},
     [{"type": "date", "text": "Lundi 23 novembre 2026 · Corée du Sud", "until_beat": 1},
      {"type": "news", "at_word": w(t, "pourtant"), "left": "SÉOUL · KOSPI", "right": "23 NOV.", "tag": "PARADOXE",
       "headline": "Le Kospi chute jusqu'à 5,8 % malgré le rebond des contrats à terme américains",
       "highlight": "jusqu'à 5,8 %", "sub": AJ}])

t = "Et ce n'est pas le pire : depuis son record de juin, le Kospi a perdu 46 %."
beat(t, "Et ce n'est pas le pire : depuis son record de juin, le Kospi a perdu quarante-six pour cent.",
     scr("1"),
     [{"type": "screen_counter", "kicker": "KOSPI · DEPUIS LE RECORD", "value_from": 0, "value_to": -46, "decimals": 0,
       "prefix": "", "suffix": " %", "color": "red", "pill": "RECORD ≈ 9 100 PTS · MI-JUIN",
       "desc": "Clôture du 20 nov. : 4 869,96 pts (−5,21 %) · " + SE + " · " + KH}])

t = "Près de 2 400 milliards de dollars de capitalisation, partis en fumée."
beat(t, "Près de deux mille quatre cents milliards de dollars de capitalisation... partis en fumée.",
     scr("2"),
     [{"type": "screen_counter", "kicker": "BOURSE DE SÉOUL · VALEUR EFFACÉE", "value_from": 0, "value_to": 2400, "decimals": 0,
       "prefix": "≈ ", "suffix": " Md$", "color": "red", "pill": "≈ 3 300 000 MILLIARDS DE WONS",
       "desc": "Depuis le record de juin · " + KH}])

t = "Les géants de la puce trinquent : Samsung et SK Hynix reculent d'environ 6 %."
beat(t, "Les géants de la puce trinquent : Samsung et S.K. Hynix reculent d'environ six pour cent.",
     {"shots": [clip("3"), dict(clip("3b"), at_word=w(t, "Samsung"))]},
     [{"type": "tickers", "title": "SÉOUL · 23 NOV. · MI-SÉANCE",
       "rows": [{"key": "SSU", "name": "Samsung", "pct": "−6 %", "at_word": w(t, "Samsung")},
                {"key": "SKH", "name": "SK hynix", "pct": "−6 %", "at_word": w(t, "SK")}]},
      {"type": "source", "text": SBS}])

t = "L'étincelle est partie de New York : vendredi, le Nasdaq a chuté de 5,3 % et effacé tous ses gains de 2026."
beat(t, "L'étincelle est partie de New York : vendredi, le Nasdaq a chuté de plus de cinq pour cent... et effacé tous ses gains de l'année.",
     {"shots": [clip("4"), dict(clip("4b"), at_word=w(t, "vendredi"))]},
     [{"type": "stock", "key": "NDAQ", "name": "Nasdaq Composite", "sub": "Vendredi 20 nov. · gains de 2026 effacés", "pct": "−5,3 %",
       "y": 560, "at_word": w(t, "Nasdaq")},
      {"type": "source", "text": AJ}])

t = "La peur d'une bulle de l'I.A. a traversé le Pacifique. Et la Corée, championne des puces, prend le choc de plein fouet."
beat(t, "La peur d'une bulle de l'I.A. a traversé le Pacifique... Et la Corée, championne des puces, prend le choc de plein fouet.",
     {"shots": [clip("5"), dict(clip("5b"), at_word=w(t, "Corée"))]},
     [{"type": "bigtitle", "lines": ["LA PEUR D'UNE", "BULLE DE L'I.A."], "at_word": w(t, "peur")}])

t = "Alors, qui va arrêter l'hémorragie ?"
beat(t, "Alors... qui va arrêter l'hémorragie ?",
     clip("6"),
     [{"type": "bigtitle", "lines": ["QUI VA ARRÊTER", "L'HÉMORRAGIE ?"], "at_word": w(t, "qui")}])

t = "Cette chute, je la suis en direct sur mon Telegram. Lien en bio."
beat(t, t, clip("7"),
     [{"type": "phone", "mode": "mini", "img": "tg_3435c02c.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "Réponse : l'État. Dimanche, Séoul a réuni ses autorités en urgence et prépare un fonds de 10 000 milliards de wons."
beat(t, "Réponse : l'État. Dimanche, Séoul a réuni ses autorités en urgence... et prépare un fonds de dix mille milliards de wons.",
     {"screen": True, "under": clip("8")},
     [{"type": "screen_counter", "kicker": "FONDS · MILLIARDS DE WONS", "value_from": 0, "value_to": 10000, "decimals": 0,
       "prefix": "", "suffix": "", "color": "gold", "pill": "RÉUNION D'URGENCE · DIMANCHE 22 NOV.",
       "desc": "Prêt à être activé · ministre des Finances Lee Hyoung-il · " + SE}])

t = "Près de 7 milliards de dollars, pour racheter des fonds indiciels du Kospi 200."
beat(t, "Près de sept milliards de dollars... pour racheter des fonds indiciels du Kospi deux cents.",
     {"shots": [clip("9"), dict(clip("9b"), at_word=w(t, "racheter"))]},
     [{"type": "news", "at_word": 0, "left": "CORÉE DU SUD · FONDS", "right": "22 NOV.", "tag": "SAUVETAGE",
       "headline": "Un fonds d'environ 6,8 milliards de dollars, investi en produits indiciels du Kospi 200",
       "highlight": "6,8 milliards de dollars", "sub": SE + " · " + KH}])

t = "C'est environ 20 fois la somme mobilisée en 2008."
beat(t, "C'est environ vingt fois la somme mobilisée en deux mille huit.",
     {"screen": True, "under": clip("10")},
     [{"type": "screen_duo",
       "a": {"kicker": "FONDS DE 2008", "value_to": 515, "decimals": 0, "prefix": "", "suffix": " Md₩", "color": "gold", "desc": "Montant déployé pendant la crise financière · " + KH},
       "b_at_word": w(t, "2008"),
       "b": {"kicker": "FONDS DE 2026", "value_to": 10760, "decimals": 0, "prefix": "", "suffix": " Md₩", "color": "gold", "desc": "Engagements totaux du secteur financier · " + KH}}])

t = "En renfort : rachats d'actions facilités pendant trois mois, et chasse à la vente à découvert illégale."
beat(t, "En renfort : rachats d'actions facilités pendant trois mois... et chasse à la vente à découvert illégale.",
     {"shots": [clip("11"), dict(clip("11b"), at_word=w(t, "chasse"))]},
     [{"type": "news", "at_word": w(t, "rachats"), "left": "SÉOUL · MESURES", "right": "DÈS LE 24 NOV.", "tag": "URGENCE",
       "headline": "Plafonds de rachat d'actions assouplis pour trois mois, contrôles renforcés contre la vente à découvert illégale",
       "highlight": "trois mois", "sub": KH}])

t = "Le paradoxe : au même moment, les contrats sur le Nasdaq bondissent de près de 3 %."
beat(t, "Le paradoxe : au même moment, les contrats sur le Nasdaq bondissent de près de trois pour cent.",
     {"shots": [clip("12"), dict(clip("12b"), at_word=w(t, "Nasdaq"))]},
     [{"type": "tickers", "title": "CONTRATS À TERME US · DIM. 22 NOV. SOIR",
       "rows": [{"name": "Nasdaq", "pct": "+2,89 %", "at_word": w(t, "Nasdaq")},
                {"name": "S&P 500", "pct": "+2,1 %", "at_word": w(t, "bondissent")},
                {"name": "Dow Jones", "pct": "+1,41 %", "at_word": w(t, "près")}]},
      {"type": "source", "text": FO}])

t = "Prochaine date à surveiller : jeudi 26 novembre. La Banque de Corée pourrait relever ses taux, en pleine tempête."
beat(t, "Prochaine date à surveiller : jeudi vingt-six novembre... La Banque de Corée pourrait relever ses taux, en pleine tempête.",
     {"shots": [clip("13"), dict(clip("13b"), at_word=w(t, "Banque"))]},
     [{"type": "news", "at_word": w(t, "26"), "left": "AGENDA · CORÉE", "right": "26 NOV.", "tag": "À SURVEILLER",
       "headline": "Jeudi 26 novembre : la Banque de Corée devrait relever son taux directeur",
       "highlight": "26 novembre", "sub": SE}])

t = "Alors, un fonds d'État peut-il vraiment arrêter une chute pareille ? Dis-le en commentaire."
beat(t, "Alors... un fonds d'État peut-il vraiment arrêter une chute pareille ? Dis-le en commentaire.",
     clip("14"),
     [{"type": "bigtitle", "lines": ["L'ÉTAT PEUT-IL", "ARRÊTER LA CHUTE ?"], "at_word": w(t, "fonds")}])

t = "Pendant que les marchés paniquent, sur mon Telegram on garde la tête froide : actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. C'est gratuit, et plus de 22 000 personnes y sont déjà. Rejoins la famille, lien en bio."
say = "Pendant que les marchés paniquent, sur mon Telegram on garde la tête froide : actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. C'est gratuit, et plus de vingt-deux mille personnes y sont déjà... Rejoins la famille, lien en bio."
beat(t, say, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Séoul sort son fonds d'urgence : ce que ça change", "imgs": ["tg_1eaa56f0.jpg", "tg_3435c02c_top.jpg", "tg_4b2fa9a8.jpg"],
       "subs": 22760, "subs_at_word": w(t, "22"), "bio_at_word": w(t, "bio"), "button": "REJOINS LA FAMILLE"}],
     cta="long", endcard={"duration": 1.8, "button": "REJOINS LA FAMILLE", "small": "Telegram gratuit · lien en bio"})

CUT = [int(x) for x in sys.argv[1:]]
B = [b for i, b in enumerate(B) if i not in CUT]
spec = {"id": EP, "date_label": "23 novembre 2026", "brand": "Invest Family Fr", "hook_type": "headline",
        "hook_formula": "contre-intuitif",
        "cta_angle": "Pendant que les marchés paniquent, sur mon Telegram on garde la tête froide",
        "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.aljazeera.com/news/2026/11/23/south-koreas-stock-market-tumbles-as-ai-bubble-fears-mount",
                    "https://en.sedaily.com/market/2026/11/23/kospi-opens-down-28-percent-as-emergency-measures-blunt",
                    "https://en.sedaily.com/opinion/2026/11/23/seoul-readies-stock-stabilization-fund-as-markets-plunge",
                    "https://news.sbs.co.kr/english/article.do?news_id=N1008858894",
                    "https://www.kaohooninternational.com/markets/595209",
                    "https://fortune.com/2026/11/22/stock-market-today-dow-futures-sp500-nasdaq-correction-ai-bust/"],
        "beats": B}
json.dump(spec, open(f'/home/claude/kit/episodes/{EP}/spec.json', 'w'), ensure_ascii=False, indent=1)
txt = "\n".join(b["say"] for b in B)
open(f'/home/claude/kit/episodes/{EP}/voice_text.txt', 'w').write(txt)
print(len(B), "beats", len(txt.split()), "mots")
