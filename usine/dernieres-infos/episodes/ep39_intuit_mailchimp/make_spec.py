import json, sys
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep39_intuit_mailchimp'
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
SA = "SiliconANGLE · 19 nov. 2026"
TB = "tbreak · 20 nov. 2026"
INV = "Investing.com · 20 nov. 2026"
IC = "IC Markets · 20 nov. 2026"

t = "12 milliards en 2021. À peine 3,7 milliards aujourd'hui."
beat(t, "Douze milliards de dollars en deux mille vingt et un... À peine trois milliards sept cents millions aujourd'hui.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "peine"))]},
     [{"type": "date", "text": "Vendredi 20 novembre 2026 · Wall Street", "until_beat": 0},
      {"type": "breaking", "label": "DERNIÈRES INFOS", "lines": ["12 MD$ → 3,7 MD$", "INTUIT REVEND", "MAILCHIMP"]},
      {"type": "stock", "key": "INTU", "name": "Intuit", "sub": "INTU · Nasdaq · 20 nov. 2026", "y": 560, "at_word": w(t, "peine")}])

t = "C'est le prix auquel Intuit, le géant américain de la compta, revend Mailchimp."
beat(t, "C'est le prix auquel Intuit, le géant américain de la compta, revend Mailchimp.",
     {"screen": True, "under": clip("1")},
     [{"type": "screen_duo",
       "a": {"kicker": "RACHAT DE MAILCHIMP · 2021", "value_to": 12, "decimals": 0, "prefix": "", "suffix": " Md$", "color": "white", "desc": "Plus gros rachat d'Intuit à l'époque", "logo": "INTU"},
       "b_at_word": w(t, "revend"),
       "b": {"kicker": "REVENTE · NOV. 2026", "value_to": 3.68, "decimals": 2, "prefix": "", "suffix": " Md$", "color": "red", "desc": SA}}])

t = "Moins d'un tiers de ce qu'il l'avait payé, il y a cinq ans."
beat(t, "Moins d'un tiers de ce qu'il l'avait payé... il y a cinq ans.",
     {"shots": [clip("2"), dict(clip("2b"), at_word=w(t, "payé"))]},
     [{"type": "news", "at_word": 1, "left": "SILICONANGLE", "right": "19 NOV.", "tag": "DEAL",
       "headline": "Intuit vend Mailchimp à Bending Spoons pour 3,68 Md$, moins d'un tiers de ce qu'il avait payé",
       "highlight": "moins d'un tiers", "sub": SA}])

t = "Et ce n'est pas le pire : après l'annonce, l'action Intuit a plongé de plus de 10 %."
beat(t, "Et ce n'est pas le pire : après l'annonce, l'action Intuit a plongé de plus de dix pour cent.",
     {"shots": [clip("3"), dict(clip("3b"), at_word=w(t, "plongé"))]},
     [{"type": "stock", "key": "INTU", "name": "Intuit", "sub": "Hors séance, jeudi soir · " + SA, "pct": "> −10 %", "up": False,
       "y": 560, "at_word": w(t, "Intuit")},
      {"type": "source", "text": SA + " · " + INV}])

t = "Pourtant, ses résultats battent les attentes : 4,35 milliards de chiffre d'affaires, en hausse de 12 %."
beat(t, "Pourtant, ses résultats battent les attentes : plus de quatre milliards de chiffre d'affaires... en hausse de douze pour cent.",
     {"screen": True, "under": clip("4")},
     [{"type": "screen_duo",
       "a": {"kicker": "CHIFFRE D'AFFAIRES ATTENDU", "value_to": 4.31, "decimals": 2, "prefix": "", "suffix": " Md$", "color": "white", "desc": "Consensus LSEG"},
       "b_at_word": w(t, "4,35"),
       "b": {"kicker": "PUBLIÉ · TRIMESTRE AU 31 OCT.", "value_to": 4.35, "decimals": 2, "prefix": "", "suffix": " Md$", "color": "green", "desc": "+12 % sur un an · " + SA, "logo": "INTU"}}])

t = "Alors, pourquoi de bons chiffres font-ils chuter l'action ?"
beat(t, "Alors... pourquoi de bons chiffres font-ils chuter l'action ?", clip("5"),
     [{"type": "bigtitle", "lines": ["DE BONS CHIFFRES", "ET L'ACTION CHUTE ?"], "at_word": w(t, "bons")}])

t = "Ce genre de coup de théâtre, je le décortique en direct sur mon Telegram. Lien en bio."
beat(t, t, clip("6"),
     [{"type": "phone", "mode": "mini", "img": "tg_1eaa56f0.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "Premier problème : Mailchimp recule. 313 millions de dollars sur le trimestre, en baisse de 1 %."
beat(t, "Premier problème : Mailchimp recule. Trois cent treize millions de dollars sur le trimestre... en baisse de un pour cent.",
     {"screen": True, "under": clip("7")},
     [{"type": "screen_counter", "kicker": "MAILCHIMP · CHIFFRE D'AFFAIRES DU TRIMESTRE", "value_from": 0, "value_to": 313, "decimals": 0,
       "prefix": "", "suffix": " M$", "color": "red", "pill": "−1 % SUR UN AN", "desc": SA + " · " + TB}])

t = "Deuxième problème : Intuit abaisse sa prévision de croissance pour toute l'année."
beat(t, "Deuxième problème : Intuit abaisse sa prévision de croissance pour toute l'année.",
     {"screen": True, "under": clip("8")},
     [{"type": "screen_duo",
       "a": {"kicker": "CROISSANCE PRÉVUE · AVANT", "value_to": 10, "decimals": 0, "prefix": "9 à ", "suffix": " %", "color": "white", "desc": "Exercice 2027", "logo": "INTU"},
       "b_at_word": w(t, "abaisse"),
       "b": {"kicker": "CROISSANCE PRÉVUE · MAINTENANT", "value_to": 9, "decimals": 0, "prefix": "8 à ", "suffix": " %", "color": "red", "desc": "23,08 à 23,37 Md$ · " + TB}}])

t = "En cause : Credit Karma, dont la croissance attendue est ramenée entre 3 et 7 %, contre 11 à 13 % avant."
beat(t, "En cause : Credit Karma, dont la croissance attendue est ramenée entre trois et sept pour cent... contre onze à treize avant.",
     {"shots": [clip("9"), dict(clip("9b"), at_word=w(t, "contre"))]},
     [{"type": "news", "at_word": 2, "left": "INTUIT", "right": "19 NOV.", "tag": "PRÉVISIONS",
       "headline": "Credit Karma : croissance attendue ramenée à 3-7 %, contre 11-13 % auparavant",
       "highlight": "3-7 %", "sub": SA}])

t = "Et l'acheteur ? Bending Spoons, un groupe italien coté au Nasdaq depuis juillet."
beat(t, "Et l'acheteur ? Bending Spoons... un groupe italien coté au Nasdaq depuis juillet.",
     {"shots": [clip("10"), dict(clip("10b"), at_word=w(t, "italien"))]},
     [{"type": "stock", "key": "BSP", "name": "Bending Spoons", "sub": "BSP · Nasdaq · Milan · " + TB, "y": 560, "at_word": w(t, "Bending")}])

t = "Il a déjà avalé Evernote, WeTransfer, Vimeo et Eventbrite."
beat(t, "Il a déjà avalé Evernote, WeTransfer, Vimeo... et Eventbrite.",
     {"screen": True, "under": clip("11")},
     [{"type": "tickers", "title": "DÉJÀ RACHETÉS PAR BENDING SPOONS", "rows": [
         {"name": "Evernote", "pct": "NOTES", "at_word": w(t, "Evernote"), "up": True},
         {"name": "WeTransfer", "pct": "FICHIERS", "at_word": w(t, "WeTransfer"), "up": True},
         {"name": "Vimeo", "pct": "VIDÉO", "at_word": w(t, "Vimeo"), "up": True},
         {"name": "Eventbrite", "pct": "BILLETS", "at_word": w(t, "Eventbrite"), "up": True}]},
      {"type": "source", "text": SA + " · " + TB}])

t = "Et ce matin, toute la tech flanche encore : Anthropic perd plus de 6 % avant l'ouverture."
beat(t, "Et ce matin, toute la tech flanche encore : Anthropic perd plus de six pour cent avant l'ouverture.",
     {"screen": True, "under": clip("12")},
     [{"type": "tickers", "title": "AVANT L'OUVERTURE · CE VENDREDI", "rows": [
         {"name": "Anthropic", "pct": "> −6 %", "at_word": w(t, "Anthropic"), "key": "ANT", "up": False},
         {"name": "AMD", "pct": "> −5 %", "at_word": w(t, "perd"), "key": "AMD", "up": False},
         {"name": "Intel", "pct": "> −4 %", "at_word": w(t, "avant"), "key": "INTC", "up": False}]},
      {"type": "source", "text": INV}])

t = "Le Dow Jones a déjà perdu plus de 6 % cette semaine, sa pire depuis avril 2025."
beat(t, "Le Dow Jones a déjà perdu plus de six pour cent cette semaine... sa pire depuis avril deux mille vingt-cinq.",
     {"screen": True, "under": clip("13")},
     [{"type": "screen_counter", "kicker": "DOW JONES · SUR LA SEMAINE", "value_from": 0, "value_to": -6.2, "decimals": 1,
       "prefix": "", "suffix": " %", "color": "red", "pill": "PIRE SEMAINE DEPUIS AVRIL 2025", "desc": IC}])

t = "À surveiller : la confiance des consommateurs américains, à 16 h, heure de Paris."
beat(t, "À surveiller : la confiance des consommateurs américains, à seize heures, heure de Paris.",
     {"shots": [clip("14"), dict(clip("14b"), at_word=w(t, "16"))]},
     [{"type": "tickers", "title": "À SURVEILLER", "rows": [
         {"name": "Confiance Michigan", "pct": "16H00", "at_word": w(t, "confiance"), "up": True},
         {"name": "Vente de Mailchimp", "pct": "DÉBUT 2027", "at_word": w(t, "16"), "up": True}]},
      {"type": "source", "text": "Agenda (heure de Paris) · " + IC + " · " + SA}])

t = "Alors, Intuit a-t-il raison de couper la branche qui ne pousse plus ? Dis-le en commentaire."
beat(t, "Alors... Intuit a-t-il raison de couper la branche qui ne pousse plus ? Dis-le en commentaire.", clip("15"),
     [{"type": "bigtitle", "lines": ["BONNE DÉCISION", "OU AVEU D'ÉCHEC ?"], "at_word": w(t, "raison")}])

t = ("Les gros titres, tout le monde les voit. Ce qu'il y a derrière, on le décortique sur mon Telegram gratuit : "
     "actu géopolitique et financière, analyses d'actions détaillées, opportunités en temps réel. "
     "Plus de 22 000 personnes déjà. Entre dans le canal, lien en bio.")
say = t.replace("Plus de 22 000", "Plus de vingt-deux mille").replace("voit.", "voit...")
beat(t, say, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Intuit brade Mailchimp : ce qu'il faut comprendre", "imgs": ["tg_3435c02c_top.jpg", "tg_1eaa56f0.jpg"],
       "subs": 22760, "subs_at_word": w(t, "22"), "bio_at_word": w(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
     cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "20 novembre 2026", "brand": "Invest Family Fr",
        "hook_type": "breaking", "hook_formula": "chiffre choc",
        "cta_angle": "Les gros titres, tout le monde les voit. Ce qu'il y a derrière, on le décortique", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad",
                  "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://siliconangle.com/2026/11/19/intuit-sells-mailchimp-to-bending-spoons-for-3-68b-less-than-a-third-of-what-it-paid/",
                    "https://tbreak.com/intuit-sells-mailchimp-bending-spoons/",
                    "https://www.investing.com/news/stock-market-news/premarket-movers-anthropic-slides-after-debut-intuit-tumbles-on-mailchimp-sale-5041130",
                    "https://www.icmarkets-vno.com/blog/stock-futures-fall-as-global-markets-extend-losses-20-november-ic/"],
        "beats": B}
json.dump(spec, open(f'/home/claude/kit/episodes/{EP}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'/home/claude/kit/episodes/{EP}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), sum(len(b["say"].split()) for b in B), "mots")
