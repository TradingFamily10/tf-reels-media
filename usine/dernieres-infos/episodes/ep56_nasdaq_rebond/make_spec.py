import json, sys, os
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep56_nasdaq_rebond'
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
SX = "Saxo · Market Quick Take · 26 nov. 2026"
AFP = "AFP / Boursorama · 26 nov. 2026"
MV = "AFP / MoneyVox · 26 nov. 2026"
RT = "Reuters / Boursorama · 26 nov. 2026"

t = "−20 % : hier, le Nasdaq 100 a touché le marché baissier. Puis tout s'est retourné."
beat(t, "Moins vingt pour cent... Hier, le Nasdaq cent a touché le marché baissier. Puis tout s'est retourné.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "Puis"))]},
     [{"type": "hook_bignum", "value_to": -20, "prefix": "", "suffix": " %", "unit": "NASDAQ 100 · DEPUIS LE RECORD D'OCTOBRE", "label": "marché baissier touché",
       "logos": ["NVDA", "NDAQ", "STM", "SAF", "AIR", "HO"], "reveal_at_word": w(t, "Puis"), "count_dur": 1.1}])

t = "Et ce n'est pas le plus fou : en pleine séance, le Nasdaq a plongé de plus de 4 %."
beat(t, "Et ce n'est pas le plus fou... en pleine séance, le Nasdaq a plongé de plus de quatre pour cent.", clip("1"),
     [{"type": "bigtitle", "lines": ["−4 %", "EN PLEINE SÉANCE"], "at_word": w(t, "plongé")}])

t = "Mais à la clôture, il ne perdait plus que 0,62 %."
beat(t, "Mais à la clôture... il perdait moins d'un pour cent.", scr("2"),
     [{"type": "screen_duo", "a": {"kicker": "NASDAQ · EN SÉANCE", "value_to": -4, "decimals": 0, "prefix": "", "suffix": " %", "color": "red", "desc": "Plus de 4 % de baisse au pire de la séance · mer. 25 nov.", "logo": "NDAQ"},
       "b_at_word": w(t, "clôture"), "b": {"kicker": "NASDAQ · CLÔTURE", "value_to": -0.62, "decimals": 2, "prefix": "", "suffix": " %", "color": "red", "desc": "23 585,80 points", "logo": "NDAQ"}},
      {"type": "source", "text": MV}])

t = "Au cœur de la tempête : Nvidia, encore −3,9 % à 149,30 $."
beat(t, "Au cœur de la tempête : Nvidia... encore près de quatre pour cent de baisse.", clip("3"),
     [{"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "Clôture mer. 25 nov. · 149,30 $", "pct": "−3,9 %", "up": False, "y": 1480, "at_word": w(t, "Nvidia")},
      {"type": "source", "text": RT}])

t = "En octobre, elle valait 243 $. Et S&P menace sa note de crédit."
beat(t, "En octobre, elle valait deux cent quarante-trois dollars... Et l'agence S. and P. menace sa note de crédit.", scr("4"),
     [{"type": "screen_duo", "a": {"kicker": "NVIDIA · PIC D'OCTOBRE", "value_to": 243.37, "decimals": 2, "prefix": "", "suffix": " $", "color": "white", "desc": "Plus haut de 2026", "logo": "NVDA"},
       "b_at_word": w(t, "S&P"), "b": {"kicker": "NVIDIA · 25 NOV.", "value_to": 149.30, "decimals": 2, "prefix": "", "suffix": " $", "color": "red", "desc": "Note de crédit sous surveillance (S&P)", "logo": "NVDA"}},
      {"type": "source", "text": RT + " · " + SX}])

t = "Alors, qui profite de ce retournement ?"
beat(t, "Alors... qui profite de ce retournement ?", clip("5"),
     [{"type": "bigtitle", "lines": ["QUI PROFITE DU", "RETOURNEMENT ?"], "at_word": 1}])

t = "Ces retournements, je les suis en direct sur mon Telegram. Lien en bio."
beat(t, "Ces retournements, je les suis en direct sur mon Telegram. Lien en bio.", clip("6"),
     [{"type": "phone", "mode": "mini", "img": "tg_1eaa56f0.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "Ce matin, l'Europe rebondit : le CAC 40 gagne 1,79 %."
beat(t, "Ce matin, l'Europe rebondit : le CAC quarante gagne près de deux pour cent.", scr("7"),
     [{"type": "screen_counter", "kicker": "CAC 40 · JEUDI 26 NOV. · 9H45", "value_from": 7980, "value_to": 8123, "decimals": 0, "prefix": "", "suffix": " pts", "color": "green",
       "pill": "+1,79 %", "desc": "Clôture mercredi : 7 980,57 pts · " + AFP}])

t = "Le secteur qui mène la danse ? La défense européenne, +3,6 %."
beat(t, "Le secteur qui mène la danse ? La défense européenne... plus de trois pour cent et demi.",
     {"shots": [clip("8"), dict(clip("8b"), at_word=w(t, "défense"))]},
     [{"type": "bigtitle", "lines": ["DÉFENSE EUROPÉENNE", "+3,6 %"], "at_word": w(t, "défense")},
      {"type": "source", "text": RT}])

t = "Safran, Thales, Airbus, Dassault Aviation : tous en nette hausse."
beat(t, "Safran, Thalès, Airbus, Dassault Aviation : tous en nette hausse.", scr("9"),
     [{"type": "tickers", "title": "PARIS · JEUDI 26 NOV. · 9H45", "rows": [
        {"key": "SAF", "name": "Safran", "pct": "+3,78 %", "at_word": w(t, "Safran")},
        {"key": "HO", "name": "Thales", "pct": "+3,03 %", "at_word": w(t, "Thales")},
        {"key": "AIR", "name": "Airbus", "pct": "+2,78 %", "at_word": w(t, "Airbus")},
        {"key": "AM", "name": "Dassault Aviation", "pct": "+2,67 %", "at_word": w(t, "Dassault")}]},
      {"type": "source", "text": AFP}])

t = "Et les puces se réveillent : STMicroelectronics prend 4,84 %."
beat(t, "Et les puces se réveillent : S.T. Micro... prend près de cinq pour cent.", clip("10"),
     [{"type": "stock", "key": "STM", "name": "STMicroelectronics", "sub": "Paris · jeu. 26 nov. · 39,36 €", "pct": "+4,84 %", "up": True, "y": 1480, "at_word": w(t, "STMicroelectronics")},
      {"type": "source", "text": AFP}])

t = "Le soulagement vient de Washington : ses nouveaux droits de douane attendront février."
beat(t, "Le soulagement vient de Washington : ses nouveaux droits de douane... attendront février.", clip("11"),
     [{"type": "news", "at_word": w(t, "droits"), "left": "ÉTATS-UNIS · COMMERCE", "right": "26 NOV.", "tag": "MOINS PIRE QUE PRÉVU",
       "headline": "Taux de 20 % à 40 % proposés sur 14 partenaires, dont la Chine, le Japon et l'UE, pas appliqués avant février ou mars",
       "highlight": "février ou mars", "sub": RT}])

t = "Mais le pétrole s'enflamme : le Brent frôle les 95 $ après une attaque houthie en Arabie saoudite."
beat(t, "Mais le pétrole s'enflamme : le Brent frôle les quatre-vingt-quinze dollars... après une attaque houthie en Arabie saoudite.",
     {"screen": True, "under": clip("12")},
     [{"type": "screen_counter", "kicker": "BRENT · $ LE BARIL", "value_from": 89, "value_to": 94.33, "decimals": 2, "prefix": "", "suffix": " $", "color": "red",
       "pill": "+5 $ EN DEUX JOURS", "desc": "Attaque houthie revendiquée · mines dans le détroit d'Ormuz · " + SX}])

t = "Et Swissquote prévient : ce rebond peut encore raconter la même histoire, la panique."
beat(t, "Et Swissquote prévient : ce rebond peut encore raconter la même histoire... la panique.", clip("13"),
     [{"type": "news", "at_word": w(t, "prévient"), "left": "SWISSQUOTE · CITATION", "right": "26 NOV.", "tag": "PRUDENCE",
       "headline": "« Un rebond de 3 % après une chute de 5 % peut encore raconter la même histoire : la panique. »",
       "highlight": "la panique", "sub": "Ipek Ozkardeskaya · " + MV}])

t = "Prochain test : Wall Street rouvre demain, et l'OPEP+ se réunit dimanche 29 novembre."
beat(t, "Prochain test : Wall Street rouvre demain... et l'OPEP plus se réunit dimanche vingt-neuf novembre.",
     {"shots": [clip("14"), dict(clip("14b"), at_word=w(t, "OPEP+"))]},
     [{"type": "bigtitle", "lines": ["PROCHAIN TEST", "OPEP+ · 29 NOVEMBRE"], "at_word": w(t, "OPEP+")}])

t = "Alors, vrai rebond… ou simple pause dans la panique ? Dis-le en commentaire."
beat(t, "Alors... vrai rebond... ou simple pause dans la panique ? Dis-le en commentaire.", clip("15"),
     [{"type": "bigtitle", "lines": ["VRAI REBOND", "OU SIMPLE PAUSE ?"], "at_word": 1}])

t = ("Chaque matin, je fais le tri dans le bruit pour toi. Sur mon Telegram gratuit : l'actu géopolitique et financière décortiquée, "
     "mes analyses d'actions détaillées et mes opportunités en temps réel. Plus de 22 000 personnes y sont déjà. Entre dans le canal, lien en bio.")
s = ("Chaque matin, je fais le tri dans le bruit pour toi... Sur mon Telegram gratuit : l'actu géopolitique et financière décortiquée, "
     "mes analyses d'actions détaillées et mes opportunités en temps réel. Plus de vingt-deux mille personnes y sont déjà... Entre dans le canal, lien en bio.")
beat(t, s, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Nasdaq au bord du marché baissier, l'Europe rebondit : mon décryptage", "imgs": ["tg_38e4f34b.jpg", "tg_3435c02c.jpg", "tg_4b2fa9a8.jpg"], "subs": 22760,
       "subs_at_word": w(t, "personnes"), "bio_at_word": w(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
     cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "26 novembre 2026", "brand": "Invest Family Fr", "hook_type": "bignum", "hook_formula": "chiffre choc",
        "cta_angle": "Chaque matin, je fais le tri dans le bruit pour toi.", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.home.saxo/en-mena/content/articles/macro/market-quick-take---nasdaq-briefly-hits-bear-market-territory-before-paring-losses---26-november-2026-26112026",
                    "https://www.boursorama.com/bourse/actualites/la-bourse-de-paris-rattrape-le-sursaut-americain-4be1e2a9af2b9792d2b96d4dca7c4042",
                    "https://www.boursorama.com/bourse/actualites/l-europe-ouvre-dans-le-vert-thanksgiving-fait-oublier-les-craintes-sur-la-tech-ce56615f60183078645c4d5e90f545b1",
                    "https://www.boursorama.com/bourse/actualites/fort-rebond-en-vue-en-europe-les-droits-de-douane-us-inquietent-moins-f4c17d2b11bcf3e17150476bb16e9b67",
                    "https://www.zonebourse.com/actualite-bourse/cac-40-la-bourse-de-paris-progresse-nettement-soutenue-par-le-compartiment-technologique-ce7851d8df80f223",
                    "https://www.moneyvox.fr/bourse/actualites/111426/le-cac-40-en-forte-hausse-a-ouverture-ce-jeudi-26-novembre-lvmh-a-suivre"],
        "beats": B}
json.dump(spec, open(f'{D}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'{D}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), "beats", sum(len(b["say"].split()) for b in B), "mots")
