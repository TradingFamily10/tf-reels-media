import json, sys, os
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep50_sanofi_insmed'
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
FO = "Motley Fool · clôture du 23 nov. 2026"
FX = "Fox Business · 23 nov. 2026"
AF = "AFP via Boursorama · 24 nov. 2026, 9 h 50"
IV = "Investing.com · 24 nov. 2026"
II = "Ideal Investisseur · 24 nov. 2026"
YS = "Stocktwits via Yahoo Finance · 24 nov. 2026"

t = "41 milliards de dollars, en cash. Sanofi vient de signer le plus gros rachat de la pharma depuis des années."
beat(t, "Quarante et un milliards de dollars... en cash. Sanofi vient de signer le plus gros rachat de la pharma depuis des années.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "Sanofi"))]},
     [{"type": "date", "text": "Mardi 24 novembre 2026 · Bourse de Paris", "until_beat": 1},
      {"type": "bigtitle", "lines": ["41 MILLIARDS $", "EN CASH"], "at_word": 0},
      {"type": "stock", "key": "SNY", "name": "Sanofi", "sub": "SAN · Euronext Paris · mardi 9 h 50", "pct": "+5,00 %", "up": True, "size": "big", "y": 560, "at_word": w(t, "Sanofi")}])

t = "Et à Paris, l'action s'envole : +5 %, la plus forte hausse du CAC 40."
beat(t, "Et à Paris, l'action s'envole : plus cinq pour cent... la plus forte hausse du CAC quarante.",
     scr("1"),
     [{"type": "screen_counter", "kicker": "SANOFI · MARDI 24 NOV.", "value_from": 0, "value_to": 5.00, "decimals": 2, "prefix": "+", "suffix": " %", "color": "green",
       "pill": "PLUS FORTE HAUSSE DU CAC 40", "desc": "89,52 € · plus haut depuis nov. 2025 · " + AF}])

t = "La cible : Insmed, un labo américain spécialiste des poumons. Prix : 175 $ par action."
beat(t, "La cible : Insmed, un labo américain spécialiste des poumons. Prix : cent soixante-quinze dollars par action.",
     {"shots": [clip("2"), dict(clip("2b"), at_word=w(t, "Prix"))]},
     [{"type": "stock", "key": "INSM", "name": "Insmed", "sub": "INSM · Nasdaq · 175 $ par action", "pct": "+14 % avant-Bourse", "up": True, "y": 560, "at_word": w(t, "Insmed")},
      {"type": "source", "text": IV}])

t = "C'est 46 % de plus que son cours d'avant les rumeurs."
beat(t, "C'est quarante-six pour cent de plus que son cours d'avant les rumeurs.",
     scr("3"),
     [{"type": "screen_duo", "a": {"kicker": "OFFRE DE SANOFI", "value_to": 175, "prefix": "", "suffix": " $", "color": "cyan", "desc": "Par action Insmed, en numéraire", "logo": "SNY"},
       "b_at_word": w(t, "46"), "b": {"kicker": "PRIME", "value_to": 46, "prefix": "+", "suffix": " %", "color": "green", "desc": "Vs cours d'avant les rumeurs (18 nov.)", "logo": "INSM"}},
      {"type": "source", "text": IV + " · " + YS}])

t = "Alors pourquoi un géant français paie-t-il aussi cher ? Il y a une raison… et elle a un nom."
beat(t, "Alors... pourquoi un géant français paie-t-il aussi cher ? Il y a une raison... et elle a un nom.", clip("4"),
     [{"type": "bigtitle", "lines": ["POURQUOI PAYER", "AUSSI CHER ?"], "at_word": 1}])

t = "Ce dossier, je le décortique en direct sur mon Telegram. Lien en bio."
beat(t, t, clip("5"), [{"type": "phone", "mode": "mini", "img": "tg_4b2fa9a8.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "Ce nom, c'est Dupixent, le médicament vedette de Sanofi. Il perd son exclusivité à partir de 2031… et les copies arriveront."
beat(t, "Ce nom, c'est Dupixènte, le médicament vedette de Sanofi. Il perd son exclusivité... à partir de deux mille trente et un. Et les copies arriveront.",
     {"shots": [clip("6"), dict(clip("6b"), at_word=w(t, "perd"))]},
     [{"type": "news", "at_word": 2, "left": "SANOFI · DUPIXENT", "right": "2031-2032", "tag": "FIN D'EXCLUSIVITÉ",
       "headline": "Dupixent, approuvé dans 9 indications, perd son exclusivité en 2031 et 2032", "highlight": "perd son exclusivité", "sub": "Jefferies via Investing.com · STAT News · 24 nov. 2026"}])

t = "Insmed apporte deux médicaments déjà commercialisés. Brinsupri a dépassé 1 milliard de dollars de ventes depuis son lancement en août 2025."
beat(t, "Insmed apporte deux médicaments déjà commercialisés. Brinsupri a dépassé un milliard de dollars de ventes... depuis son lancement en août deux mille vingt-cinq.",
     scr("8"),
     [{"type": "screen_counter", "kicker": "BRINSUPRI · INSMED", "logo": "INSM", "value_from": 0, "value_to": 1.09, "decimals": 2, "prefix": "", "suffix": " MD$", "color": "cyan",
       "pill": "VENTES AOÛT 2025 → 30 SEPT. 2026", "desc": "Dilatation des bronches · " + IV, "at_word": w(t, "Brinsupri")}])

t = "Le second, Arikayce : 434 millions de dollars de ventes en 2025."
beat(t, "Le second, Arikèce : quatre cent trente-quatre millions de dollars de ventes en deux mille vingt-cinq.",
     {"shots": [clip("9"), dict(clip("9b"), at_word=w(t, "ventes"))]},
     [{"type": "ticket", "at_word": 0, "title": "INSMED · 2 MÉDICAMENTS", "subtitle": "Brinsupri : août 2025 → sept. 2026", "rows": [["Brinsupri", "1,09 Md$"], ["Arikayce · 2025", "434 M$"]], "total": ["DÉJÀ", "COMMERCIALISÉS"]},
      {"type": "source", "text": IV + " · AFP via Daily Sabah"}])

t = "Le prix reste salé : environ 22 fois leurs ventes attendues cette année."
beat(t, "Le prix reste salé : environ vingt-deux fois... leurs ventes attendues cette année.",
     scr("10"),
     [{"type": "screen_counter", "kicker": "PRIX PAYÉ", "value_from": 0, "value_to": 22, "decimals": 0, "prefix": "≈ ", "suffix": " ×", "color": "red",
       "pill": "LES VENTES 2026 ATTENDUES", "desc": "Brinsupri + Arikayce · " + II}])

t = "Un chèque du même ordre que le rachat de Seagen par Pfizer en 2023 : 43 milliards."
beat(t, "Un chèque du même ordre que le rachat de Sigène par Pfizer en deux mille vingt-trois... quarante-trois milliards.",
     {"shots": [clip("11")]},
     [{"type": "ticket", "at_word": 2, "title": "MÉGA-RACHATS PHARMA", "subtitle": "Montants annoncés", "rows": [["Pfizer → Seagen · 2023", "43 Md$"], ["Sanofi → Insmed · 2026", "41 Md$"]],
       "total": ["MÊME ORDRE", "DE GRANDEUR"], "stamp": "PHARMA"},
      {"type": "stock", "key": "PFE", "name": "Pfizer", "sub": "Rachat de Seagen · 2023", "pct": "43 Md$", "up": True, "y": 1560, "at_word": w(t, "Pfizer")},
      {"type": "source", "text": IV + " · valeurs mesurées différemment"}])

t = "Prochaine étape : le feu vert des actionnaires d'Insmed et des régulateurs, pour boucler au 1er semestre 2027."
beat(t, "Prochaine étape : le feu vert des actionnaires d'Insmed et des régulateurs... pour boucler au premier semestre deux mille vingt-sept.",
     {"shots": [clip("13"), dict(clip("13b"), at_word=w(t, "régulateurs"))]},
     [{"type": "news", "at_word": 2, "left": "AGENDA · SANOFI × INSMED", "right": "S1 2027", "tag": "À SURVEILLER",
       "headline": "Finalisation attendue au 1er semestre 2027, sous réserve du vote des actionnaires d'Insmed et des autorités", "highlight": "1er semestre 2027", "sub": IV + " · " + YS}])

t = "Alors, pari malin pour l'après-Dupixent… ou chèque trop cher ? Dis-le en commentaire."
beat(t, "Alors... pari malin pour l'après-Dupixènte... ou chèque trop cher ? Dis-le en commentaire.", clip("14"),
     [{"type": "bigtitle", "lines": ["PARI MALIN OU", "CHÈQUE TROP CHER ?"], "at_word": 1}])

t = ("Plus de 22 000 personnes ont déjà une longueur d'avance. Il ne manque que toi. Sur mon Telegram gratuit : l'actu géopolitique et financière décortiquée, "
     "mes analyses d'actions détaillées et mes opportunités en temps réel. Accès gratuit, lien en bio.")
s = ("Plus de vingt-deux mille personnes ont déjà une longueur d'avance... Il ne manque que toi. Sur mon Telegram gratuit : l'actu géopolitique et financière décortiquée, "
     "mes analyses d'actions détaillées et mes opportunités en temps réel. Accès gratuit, lien en bio.")
beat(t, s, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Sanofi × Insmed : le rachat décrypté", "imgs": ["tg_38e4f34b.jpg", "tg_1eaa56f0.jpg", "tg_3435c02c_top.jpg"], "subs": 22760,
       "subs_at_word": w(t, "personnes"), "bio_at_word": w(t, "bio"), "button": "ACCÈS GRATUIT"}],
     cta="long", endcard={"duration": 1.8, "button": "ACCÈS GRATUIT", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "24 novembre 2026", "brand": "Invest Family Fr", "hook_type": "chip", "hook_formula": "chiffre choc",
        "cta_angle": "22 000 personnes ont déjà une longueur d'avance. Il ne manque que toi.", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.boursorama.com/bourse/actualites/la-bourse-de-paris-en-hausse-soutenue-par-sanofi-491980a9107add034212c4677d687d15",
                    "https://www.ideal-investisseur.fr/bourse-cryptos/cac-40-sanofi-senvole-de-5-a-louverture-et-porte-lindice-apres-un-mega-rachat-a-41-milliards-34065.html",
                    "https://investing.com/news/stock-market-news/sanofi-to-acquire-insmed-in-41-billion-cash-deal-5047167",
                    "https://statnews.com/2026/11/24/sanofi-insmed-acquisition-dupixent-rare-disease-inflammation",
                    "https://www.dailysabah.com/business/economy/french-pharma-giant-sanofi-to-buy-us-group-insmed-for-41b",
                    "https://finance.yahoo.com/markets/stocks/articles/why-insm-stock-surging-13-081942750.html"],
        "beats": B}
json.dump(spec, open(f'{D}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'{D}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), "beats", sum(len(b["say"].split()) for b in B), "mots")
