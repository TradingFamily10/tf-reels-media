import json, sys, os
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep55_seoul_taux'
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
RT = "Reuters · 26 nov. 2026"
SBS = "SBS News · 26 nov. 2026"
SX = "Saxo · Asia Quick Take · 26 nov. 2026"
TK = "TradingKey · 26 nov. 2026"
YH = "Yahoo Finance / Motley Fool · 25 nov. 2026"

t = "Sa Bourse vient de plonger de près de 6 %. Et pourtant, la Corée du Sud relève ses taux."
beat(t, "Sa Bourse vient de plonger de près de six pour cent... Et pourtant, la Corée du Sud relève ses taux.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "pourtant"))]},
     [{"type": "date", "text": "Jeudi 26 novembre 2026 · Séoul", "until_beat": 1},
      {"type": "news", "at_word": 1, "left": "CORÉE DU SUD · BANQUE CENTRALE", "right": "26 NOV.", "tag": "CONTRE-COURANT",
       "headline": "La Banque de Corée relève son taux directeur à 3,25 %, au lendemain d'une chute de 5,8 % de la Bourse de Séoul",
       "highlight": "3,25 %", "sub": RT + " · " + SX}])

t = "Et ce n'est pas le pire : c'est déjà sa troisième hausse de l'année."
beat(t, "Et ce n'est pas le pire... c'est déjà sa troisième hausse de l'année.", clip("1"),
     [{"type": "bigtitle", "lines": ["3E HAUSSE", "DEPUIS JUILLET"], "at_word": w(t, "troisième")}])

t = "Le taux directeur passe de 3 % à 3,25 %, du jamais vu depuis deux ans."
beat(t, "Le taux directeur passe de trois pour cent à trois et quart... du jamais vu depuis deux ans.", scr("2"),
     [{"type": "screen_duo", "a": {"kicker": "TAUX DIRECTEUR · AVANT", "value_to": 3.0, "decimals": 2, "prefix": "", "suffix": " %", "color": "white", "desc": "Inchangé le 22 octobre"},
       "b_at_word": w(t, "3,25"), "b": {"kicker": "TAUX DIRECTEUR · 26 NOV.", "value_to": 3.25, "decimals": 2, "prefix": "", "suffix": " %", "color": "red", "desc": "Plus haut depuis nov. 2024 · +75 pb en 2026"}},
      {"type": "source", "text": RT}])

t = "La veille, le Kospi s'effondrait de 5,8 %. Taïwan, de 7,6 %."
beat(t, "La veille, le Kospi s'effondrait de près de six pour cent. Taïwan, de près de huit pour cent.", scr("3"),
     [{"type": "screen_duo", "a": {"kicker": "CORÉE DU SUD · MER. 25 NOV.", "value_to": -5.8, "decimals": 1, "prefix": "", "suffix": " %", "color": "red", "desc": "Kospi"},
       "b_at_word": w(t, "Taïwan"), "b": {"kicker": "TAÏWAN · MER. 25 NOV.", "value_to": -7.6, "decimals": 1, "prefix": "", "suffix": " %", "color": "red", "desc": "Indice de Taipei"}},
      {"type": "source", "text": SX}])

t = "Alors, pourquoi serrer la vis en pleine tempête ?"
beat(t, "Alors... pourquoi serrer la vis en pleine tempête ?", clip("5"),
     [{"type": "bigtitle", "lines": ["POURQUOI MONTER", "SES TAUX ?"], "at_word": 1}])

t = "Les banques centrales, je les décrypte en direct sur mon Telegram. Lien en bio."
beat(t, "Les banques centrales, je les décrypte en direct sur mon Telegram. Lien en bio.", clip("6"),
     [{"type": "phone", "mode": "mini", "img": "tg_3435c02c.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "La réponse : l'économie coréenne tourne à plein régime, portée par les puces."
beat(t, "La réponse : l'économie coréenne tourne à plein régime... portée par les puces.",
     {"shots": [clip("7"), dict(clip("7b"), at_word=w(t, "puces"))]},
     [{"type": "tickers", "title": "LES MOTEURS DE SÉOUL", "rows": [
        {"key": "SSU", "name": "Samsung Electronics", "pct": "Puces mémoire", "at_word": w(t, "économie")},
        {"key": "SKH", "name": "SK hynix", "pct": "Puces mémoire", "at_word": w(t, "puces")}]}])

t = "Ses exportations ont dépassé 1 000 milliards de dollars cette année. Une première historique."
beat(t, "Ses exportations ont dépassé mille milliards de dollars cette année... Une première historique.", scr("8"),
     [{"type": "screen_counter", "kicker": "EXPORTATIONS · MD$ · 2026", "value_from": 0, "value_to": 1000, "decimals": 0, "prefix": "", "suffix": "+", "color": "green",
       "pill": "PREMIÈRE HISTORIQUE", "desc": "Puces, chantiers navals, défense, nucléaire · " + SBS}])

t = "La banque relève sa prévision de croissance 2027 de 2,9 % à 4,1 %."
beat(t, "La banque relève sa prévision de croissance pour deux mille vingt-sept... de près de trois à plus de quatre pour cent.", scr("9"),
     [{"type": "screen_duo", "a": {"kicker": "CROISSANCE 2027 · AOÛT", "value_to": 2.9, "decimals": 1, "prefix": "", "suffix": " %", "color": "white", "desc": "Ancienne prévision"},
       "b_at_word": w(t, "4,1"), "b": {"kicker": "CROISSANCE 2027 · NOV.", "value_to": 4.1, "decimals": 1, "prefix": "", "suffix": " %", "color": "green", "desc": "Plus forte depuis 2021"}},
      {"type": "source", "text": RT + " · Banque de Corée"}])

t = "Et l'inflation reste bloquée à 2,8 %, bien au-dessus de la cible de 2 %."
beat(t, "Et l'inflation reste bloquée près de trois pour cent... bien au-dessus de la cible de deux pour cent.", scr("10"),
     [{"type": "screen_duo", "a": {"kicker": "INFLATION · OCTOBRE", "value_to": 2.8, "decimals": 1, "prefix": "", "suffix": " %", "color": "red", "desc": "Sur un an · Corée du Sud"},
       "b_at_word": w(t, "cible"), "b": {"kicker": "CIBLE DE LA BANQUE", "value_to": 2.0, "decimals": 1, "prefix": "", "suffix": " %", "color": "white", "desc": "Banque de Corée"}},
      {"type": "source", "text": RT}])

t = "Mais le vrai danger vient de Washington : l'inflation PCE accélère, plus que prévu."
beat(t, "Mais le vrai danger vient de Washington : l'inflation P.C.E. accélère... plus que prévu.", clip("12"),
     [{"type": "news", "at_word": w(t, "PCE"), "left": "ÉTATS-UNIS · INFLATION", "right": "25 NOV.", "tag": "PLUS QUE PRÉVU",
       "headline": "L'inflation PCE de base atteint 3,3 % sur un an en octobre, contre 3,2 % attendu",
       "highlight": "3,3 %", "sub": SX}])

t = "Résultat : une hausse de la Fed en décembre est jouée à 98 %. Et Nvidia a encore perdu 3,9 %."
beat(t, "Résultat : une hausse de la Fed en décembre est jouée à quatre-vingt-dix-huit pour cent... Et Nvidia a encore perdu près de quatre pour cent.", scr("13"),
     [{"type": "screen_counter", "kicker": "FED · HAUSSE EN DÉCEMBRE", "value_from": 0, "value_to": 98, "decimals": 0, "prefix": "", "suffix": " %", "color": "white",
       "pill": "PROBABILITÉ · CME FEDWATCH", "desc": SBS},
      {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "Clôture mer. 25 nov. · 149,30 $", "pct": "−3,9 %", "up": False, "y": 1480, "at_word": w(t, "Nvidia")}])

t = "Et Washington menace 14 économies de nouveaux droits de douane, dont la Corée."
beat(t, "Et Washington menace quatorze économies de nouveaux droits de douane... dont la Corée.",
     {"shots": [clip("14"), dict(clip("14b"), at_word=w(t, "Corée"))]},
     [{"type": "news", "at_word": w(t, "menace"), "left": "ÉTATS-UNIS · COMMERCE", "right": "25 NOV.", "tag": "PROPOSITION",
       "headline": "Les États-Unis proposent des droits de douane sur 14 économies, dont l'UE, le Japon et la Corée du Sud ; 15 % envisagés pour l'UE",
       "highlight": "14 économies", "sub": "TradingKey · USTR, section 301 · 25 nov. 2026"}])

t = "Prochain rendez-vous : la Fed, en décembre."
beat(t, "Prochain rendez-vous : la Fed, en décembre.", clip("15"),
     [{"type": "bigtitle", "lines": ["PROCHAIN CHOC", "LA FED EN DÉCEMBRE"], "at_word": 0}])

t = "Alors, Séoul a raison… ou joue avec le feu ? Dis-le en commentaire."
beat(t, "Alors... Séoul a raison... ou joue avec le feu ? Dis-le en commentaire.", clip("16"),
     [{"type": "bigtitle", "lines": ["BONNE DÉCISION", "OU JEU DANGEREUX ?"], "at_word": 2}])

t = ("Pendant que tu dormais, Séoul a changé la donne. Sur mon Telegram gratuit : l'actu géopolitique et financière décortiquée, "
     "mes analyses d'actions détaillées et mes opportunités en temps réel. Plus de 22 000 personnes y sont déjà. Rejoins la famille, lien en bio.")
s = ("Pendant que tu dormais, Séoul a changé la donne... Sur mon Telegram gratuit : l'actu géopolitique et financière décortiquée, "
     "mes analyses d'actions détaillées et mes opportunités en temps réel. Plus de vingt-deux mille personnes y sont déjà... Rejoins la famille, lien en bio.")
beat(t, s, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Séoul relève ses taux en pleine tempête : mon analyse", "imgs": ["tg_4b2fa9a8.jpg", "tg_1eaa56f0.jpg", "tg_38e4f34b.jpg"], "subs": 22760,
       "subs_at_word": w(t, "personnes"), "bio_at_word": w(t, "bio"), "button": "REJOINS LA FAMILLE"}],
     cta="long", endcard={"duration": 1.8, "button": "REJOINS LA FAMILLE", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "26 novembre 2026", "brand": "Invest Family Fr", "hook_type": "headline", "hook_formula": "contre-intuitif",
        "cta_angle": "Pendant que tu dormais, Séoul a changé la donne.", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.aol.com/articles/south-koreas-central-bank-raises-010435000.html",
                    "https://news.sbs.co.kr/english/article.do?news_id=N1008864381",
                    "https://news.sbs.co.kr/english/article.do?news_id=N1008864699",
                    "https://news.sbs.co.kr/english/article.do?news_id=N1008864801",
                    "https://www.home.saxo/en-sg/content/articles/macro/asia-market-quick-take--26-november-2026-26112026",
                    "https://www.tradingkey.com/analysis/stocks/more/262322889-japan-south-korea-stocks-kospi-nikkei-softbank-sk-hynix-samsung-kioxia-tradingkey",
                    "https://www.tradingkey.com/analysis/stocks/us-stocks/262322956-market-recap-sp-nasdaq-nvidia-pce-gold-breaks-3500-tradingkey",
                    "https://finance.yahoo.com/markets/stocks/articles/stock-market-today-nov-25-220645995.html"],
        "beats": B}
json.dump(spec, open(f'{D}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'{D}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), "beats", sum(len(b["say"].split()) for b in B), "mots")
