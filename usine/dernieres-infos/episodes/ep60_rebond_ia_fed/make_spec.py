import json, sys, os
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep60_rebond_ia_fed'
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
FB = "Forbes · 27 nov. 2026, 11 h 29 (Paris)"
TR = "TipRanks · 27 nov. 2026, 11 h 41 (Paris)"
PM = "PreMarket Daily · 27 nov. 2026, 10 h 11 (Paris)"

t = "Sandisk, Micron, AMD, Nvidia : ce matin, toute la tech américaine rebondit avant l'ouverture."
beat(t, "Sandisk, Micron, A.M.D., Nvidia... ce matin, toute la tech américaine rebondit avant l'ouverture.",
     scr("0"),
     [{"type": "date", "text": "Vendredi 27 novembre 2026 · Wall Street", "until_beat": 1},
      {"type": "screen_logos", "kicker": "NASDAQ 100 · FUTURES", "value_from": 0, "value_to": 2.35, "decimals": 2, "prefix": "+", "suffix": " %",
       "color": "green", "pill": "AVANT L'OUVERTURE", "keys": ["SNDK", "MU", "AMD", "NVDA"], "desc": "26 714 points · " + FB}])

t = "Tout le monde fête ce rebond. Le vrai danger est ailleurs."
beat(t, "Tout le monde fête ce rebond... Le vrai danger est ailleurs.", clip("1"),
     [{"type": "bigtitle", "lines": ["LE VRAI DANGER", "EST AILLEURS"], "at_word": w(t, "vrai")}])

t = "Sandisk bondit de 10,8 %, Micron de 6,4 %, AMD de 5 %."
beat(t, "Sandisk bondit de près de onze pour cent... Micron de plus de six pour cent, A.M.D. de cinq pour cent.",
     {"shots": [clip("3"), dict(clip("3b"), at_word=w(t, "Micron"))]},
     [{"type": "tickers", "title": "AVANT-BOURSE · VEN. 27 NOV.", "rows": [
        {"key": "SNDK", "name": "Sandisk", "pct": "+10,8 %", "at_word": 0},
        {"key": "MU", "name": "Micron", "pct": "+6,4 %", "at_word": w(t, "Micron")},
        {"key": "AMD", "name": "AMD", "pct": "+5,0 %", "at_word": w(t, "AMD")}]},
      {"type": "source", "text": FB}])

t = "Nvidia reprend 4,2 %, à 155 dollars."
beat(t, "Nvidia reprend plus de quatre pour cent... à cent cinquante-cinq dollars.",
     clip("4"),
     [{"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "NVDA · avant-bourse · 155,20 $", "pct": "+4,2 %", "up": True, "size": "big", "y": 560, "at_word": 0},
      {"type": "source", "text": FB}])

t = "Même Anthropic repasse au-dessus de son prix d'introduction, 83 dollars."
beat(t, "Même Anthropic repasse au-dessus de son prix d'introduction, quatre-vingt-trois dollars.",
     clip("5"),
     [{"type": "stock", "key": "ANT", "name": "Anthropic", "sub": "Avant-bourse · 85,73 $ · IPO à 83 $", "pct": "+3,6 %", "up": True, "size": "big", "y": 560, "at_word": 1},
      {"type": "source", "text": FB}])

t = "Mais ce rebond part de très bas : le Nasdaq 100 a perdu environ 8 % en novembre."
beat(t, "Mais ce rebond part de très bas : le Nasdaq cent a perdu environ huit pour cent en novembre.",
     scr("6"),
     [{"type": "screen_counter", "kicker": "NASDAQ 100 · NOVEMBRE 2026", "value_from": 0, "value_to": -8, "decimals": 0, "prefix": "≈ ", "suffix": " %",
       "color": "red", "pill": "JUSQU'À MERCREDI", "desc": "Pire mois depuis décembre 2022 · " + FB}])

t = "Nvidia reste 37 % sous son record d'octobre. Sandisk a perdu près de la moitié de sa valeur."
beat(t, "Nvidia reste plus d'un tiers sous son record... Sandisk a perdu près de la moitié de sa valeur.",
     scr("7"),
     [{"type": "screen_duo", "a": {"kicker": "NVIDIA · VS RECORD", "value_to": -37, "decimals": 0, "prefix": "", "suffix": " %", "color": "red", "desc": "À la clôture de mercredi", "logo": "NVDA"},
       "b_at_word": w(t, "Sandisk"), "b": {"kicker": "SANDISK · NOV.", "value_to": -50, "decimals": 0, "prefix": "≈ ", "suffix": " %", "color": "red", "desc": "« Près de la moitié de sa valeur »", "logo": "SNDK"}},
      {"type": "source", "text": FB}])

t = "Alors, pourquoi ce rebond ne rassure personne ?"
beat(t, "Alors... pourquoi ce rebond ne rassure personne ?", clip("8"),
     [{"type": "bigtitle", "lines": ["UN REBOND", "QUI NE RASSURE PAS"], "at_word": 1}])

t = "Cette demi-séance, je la commente en direct sur mon Telegram. Lien en bio."
beat(t, "Cette demi-séance, je la commente en direct sur mon Telegram. Lien en bio.", clip("9"),
     [{"type": "phone", "mode": "mini", "img": "tg_3435c02c_top.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "Parce que la Fed ne change pas de cap : le marché voit à 98,9 % une hausse des taux en décembre."
beat(t, "Parce que la Fed ne change pas de cap : le marché voit à presque cent pour cent... une hausse des taux en décembre.",
     scr("10"),
     [{"type": "screen_gauge", "kicker": "HAUSSE DE LA FED EN DÉCEMBRE ?", "pill": "98,9 % SELON LE CME FEDWATCH", "desc": "Hausse de 0,25 point attendue · " + FB}])

t = "Et le taux américain à 10 ans grimpe à 4,92 %."
beat(t, "Et le taux américain à dix ans grimpe... à près de cinq pour cent.",
     scr("11"),
     [{"type": "screen_counter", "kicker": "TAUX US À 10 ANS", "value_from": 4.86, "value_to": 4.92, "decimals": 2, "prefix": "", "suffix": " %",
       "color": "red", "pill": "+6 POINTS DE BASE", "desc": "Le 30 ans à 5,305 % · " + PM}])

t = "Pendant ce temps, l'or reprend 4 %, deux jours après son plus bas sur un an."
beat(t, "Pendant ce temps, l'or reprend quatre pour cent... deux jours après son plus bas sur un an.",
     scr("12"),
     [{"type": "screen_duo", "a": {"kicker": "OR · PLUS BAS SUR 52 SEMAINES", "value_to": 3425, "decimals": 0, "prefix": "", "suffix": " $", "color": "red", "desc": "Mercredi 25 nov. · contrat de février"},
       "b_at_word": w(t, "reprend"), "b": {"kicker": "OR · VENDREDI MATIN", "value_to": 3708, "decimals": 0, "prefix": "", "suffix": " $", "color": "green", "desc": "+4 % · COMEX"}},
      {"type": "source", "text": PM}])

t = "En Asie, Shanghai gagne 3,7 % : Pékin promet d'agir pour freiner la chute de ses marchés."
beat(t, "En Asie, Shanghai gagne presque quatre pour cent : Pékin promet d'agir pour freiner la chute de ses marchés.",
     {"shots": [clip("13"), dict(clip("13b"), at_word=w(t, "Pékin"))]},
     [{"type": "news", "at_word": 2, "left": "ASIE · MARCHÉS", "right": "27 NOV.", "tag": "PÉKIN INTERVIENT",
       "headline": "Shanghai +3,73 %, Shenzhen +6,3 % : le gouvernement chinois promet de nouvelles mesures pour enrayer la baisse",
       "highlight": "nouvelles mesures", "sub": TR + " · Kospi +4,34 % (Forbes)"}])

t = "À surveiller : Wall Street ouvre à 15 h 30 et ferme dès 19 h, heure de Paris."
beat(t, "À surveiller : Wall Street ouvre à quinze heures trente... et ferme dès dix-neuf heures, heure de Paris.",
     clip("14"),
     [{"type": "news", "at_word": 2, "left": "AGENDA · WALL STREET", "right": "VEN. 27 NOV.", "tag": "DEMI-SÉANCE",
       "headline": "Séance raccourcie du Black Friday : ouverture 15 h 30, clôture 19 h (Paris), aucune statistique majeure",
       "highlight": "clôture 19 h", "sub": TR + " · " + PM}])

t = "Alors, vrai rebond… ou simple respiration avant la Fed ? Dis-le en commentaire."
beat(t, "Alors... vrai rebond... ou simple respiration avant la Fed ? Dis-le en commentaire.", clip("15"),
     [{"type": "bigtitle", "lines": ["VRAI REBOND", "OU RESPIRATION ?"], "at_word": 1}])

t = ("Pendant que les marchés s'affolent, sur mon Telegram gratuit on garde la tête froide : l'actu géopolitique et financière décortiquée, "
     "mes analyses d'actions détaillées et mes opportunités en temps réel. Plus de 22 000 personnes sont déjà avec nous. Rejoins la famille, lien en bio.")
s = ("Pendant que les marchés s'affolent... sur mon Telegram gratuit, on garde la tête froide : l'actu géopolitique et financière décortiquée, "
     "mes analyses d'actions détaillées et mes opportunités en temps réel. Plus de vingt-deux mille personnes sont déjà avec nous... Rejoins la famille, lien en bio.")
beat(t, s, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Rebond de la tech : ce que la Fed prépare", "imgs": ["tg_1eaa56f0.jpg", "tg_3435c02c.jpg"], "subs": 22760,
       "subs_at_word": w(t, "personnes"), "bio_at_word": w(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
     cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "27 novembre 2026", "brand": "Invest Family Fr", "hook_type": "logowall", "hook_formula": "personne n'en parle",
        "cta_angle": "Pendant que les marchés s'affolent, sur mon Telegram on garde la tête froide", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.forbes.com/sites/siladityaray/2026/11/27/stock-futures-surge-as-battered-ai-shares-rebound-ahead-of-shorterned-friday-trading/",
                    "https://www.tipranks.com/news/stock-market-today-nov-27-markets-reopen-for-shortened-black-friday-trading",
                    "https://premarketdaily.com/2026/11/27/nvidia-and-gold-surge-together-as-black-friday-cuts-the-session-short/"],
        "beats": B}
json.dump(spec, open(f'{D}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'{D}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), "beats", sum(len(b["say"].split()) for b in B), "mots")
