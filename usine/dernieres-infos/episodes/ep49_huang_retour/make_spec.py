import json, sys, os
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep49_huang_retour'
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
YF = "Yahoo Finance · 23 nov. 2026"
AP = "AP via WSLS · 24 nov. 2026"
BZ = "Benzinga via AOL · 24 nov. 2026"

t = "Le jour où le retour d'un seul homme a fait gagner près de 1 000 milliards de dollars à Nvidia."
beat(t, "Le jour où le retour d'un seul homme... a fait gagner près de mille milliards de dollars à Nvidia.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "milliards"))]},
     [{"type": "date", "text": "Lundi 23 novembre 2026 · Wall Street", "until_beat": 0},
      {"type": "breaking", "label": "DERNIÈRES INFOS", "lines": ["NVIDIA +31 %", "≈ 1 000 MD$ GAGNÉS", "HUANG REVIENT"]},
      {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "NVDA · Nasdaq · lundi 23 nov.", "pct": "+31,48 %", "up": True, "size": "big", "y": 1180, "at_word": w(t, "Nvidia")}])

t = "+31 % en un jour : sa plus forte hausse depuis plus de vingt ans."
beat(t, "Plus trente et un pour cent en un jour... sa plus forte hausse depuis plus de vingt ans.",
     scr("1"),
     [{"type": "screen_counter", "kicker": "NVIDIA · SÉANCE DU 23 NOV.", "value_from": 0, "value_to": 31.48, "decimals": 2, "prefix": "+", "suffix": " %", "color": "green",
       "pill": "PLUS FORTE HAUSSE DEPUIS 20 ANS", "desc": "Clôture 165,05 $ · " + FO}])

t = "Il y a douze jours, son fondateur Jensen Huang démissionnait. La semaine dernière, l'action perdait près de 23 %."
beat(t, "Il y a douze jours, son fondateur Jensen Huang démissionnait... La semaine dernière, l'action perdait près de vingt-trois pour cent.",
     {"shots": [clip("2"), dict(clip("2b"), at_word=w(t, "semaine"))]},
     [{"type": "news", "at_word": 1, "until_word": w(t, "semaine"), "left": "NVIDIA · DIRECTION", "right": "12 NOV.", "tag": "DÉMISSION",
       "headline": "Jensen Huang quitte la direction de Nvidia, le groupe qu'il a fondé", "highlight": "quitte la direction", "sub": FX},
      {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "Semaine du 16 au 20 nov.", "pct": "≈ −23 %", "up": False, "y": 560, "at_word": w(t, "semaine")}])

t = "Alors, qu'est-ce qui a tout fait basculer en quelques jours ?"
beat(t, "Alors... qu'est-ce qui a tout fait basculer, en quelques jours ?", clip("4"),
     [{"type": "bigtitle", "lines": ["QU'EST-CE QUI A", "TOUT FAIT BASCULER ?"], "at_word": 1}])

t = "Ce retournement, je le suis en direct sur mon Telegram. Lien en bio."
beat(t, t, clip("5"), [{"type": "phone", "mode": "mini", "img": "tg_3435c02c_top.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "Réponse : lundi, le conseil l'a réintégré à l'unanimité, après avis du gouvernement américain, sans risque selon lui pour la sécurité nationale."
beat(t, "Réponse : lundi, le conseil l'a réintégré à l'unanimité... après avis du gouvernement américain, sans risque selon lui pour la sécurité nationale.",
     {"shots": [clip("6"), dict(clip("6b"), at_word=w(t, "avis"))]},
     [{"type": "news", "at_word": 2, "left": "NVIDIA · CONSEIL", "right": "23 NOV.", "tag": "RETOUR",
       "headline": "Le conseil réintègre Jensen Huang à l'unanimité : « la bonne personne pour diriger Nvidia »", "highlight": "à l'unanimité", "sub": YF}])

t = "Wall Street s'envole : le Nasdaq +6,5 %, le S&P 500 près de +5 %, sa meilleure séance depuis avril 2025."
beat(t, "Wall Street s'envole : le Nasdaq plus de six pour cent, le S. and P. cinq cents près de cinq pour cent... sa meilleure séance depuis avril deux mille vingt-cinq.",
     {"shots": [clip("8"), dict(clip("8b"), at_word=w(t, "meilleure"))]},
     [{"type": "ticket", "at_word": 2, "title": "WALL STREET · CLÔTURE", "subtitle": "Lundi 23 novembre 2026", "rows": [["Nasdaq · 24 090", "+6,51 %"], ["S&P 500 · 7 237", "+4,73 %"], ["Dow Jones · 49 595", "+3,01 %"]],
       "total": ["MEILLEURE SÉANCE DEPUIS", "AVRIL 2025"], "stamp": "NEW YORK"}, {"type": "source", "text": "Fox Business, Motley Fool, AP · 23-24 nov. 2026"}])

t = "Toutes les puces suivent : Micron +19 %, AMD +7 %, Broadcom +3 %."
beat(t, "Toutes les puces suivent : Micron, plus dix-neuf pour cent... A.M.D., plus sept... Broadcom, plus trois.",
     {"shots": [clip("9")]},
     [{"type": "tickers", "title": "PUCES · LUNDI 23 NOV.", "rows": [{"key": "MU", "name": "Micron", "pct": "+19 %", "at_word": w(t, "Micron")},
       {"key": "AMD", "name": "AMD", "pct": "+6,85 %", "at_word": w(t, "AMD")}, {"key": "AVGO", "name": "Broadcom", "pct": "+3,00 %", "at_word": w(t, "Broadcom")}]},
      {"type": "source", "text": "Fox Business, Motley Fool · 23 nov. 2026"}])

t = "Et cette nuit, l'Asie a pris le relais : Séoul +6,5 %, Taïwan plus de 9 %."
beat(t, "Et cette nuit, l'Asie a pris le relais : Séoul, plus de six pour cent... Taïwan, plus de neuf pour cent.",
     {"shots": [clip("10"), dict(clip("10b"), at_word=w(t, "Taïwan"))]},
     [{"type": "ticket", "at_word": w(t, "Asie"), "title": "ASIE · MARDI 24 NOV.", "subtitle": "En cours de séance", "rows": [["Kospi · Séoul", "+6,5 %"], ["Taiex · Taïwan", "+9,1 %"], ["Nikkei · Tokyo", "+3,9 %"]],
       "total": ["TAÏWAN EN TÊTE", "+9,1 %"], "stamp": "ASIE"}, {"type": "source", "text": AP + " · SBS News"}])

t = "Mais le vrai test arrive : le marché voit à plus de 90 % une hausse des taux de la Fed le 9 décembre."
beat(t, "Mais le vrai test arrive : le marché voit à plus de quatre-vingt-dix pour cent une hausse des taux de la Fed... le neuf décembre.",
     scr("12"),
     [{"type": "screen_counter", "kicker": "HAUSSE DES TAUX FED", "value_from": 0, "value_to": 96, "decimals": 0, "prefix": "≈ ", "suffix": " %", "color": "red",
       "pill": "RÉUNION DE LA FED · 9 DÉCEMBRE", "desc": "CME FedWatch via Fox Business · Polymarket ≈ 91 % via Yahoo · 23 nov. 2026"}])

t = "Avant ça, mercredi à 14 h 30, l'inflation PCE américaine. Et jeudi, Wall Street fermée pour Thanksgiving."
beat(t, "Avant ça, mercredi à quatorze heures trente, l'inflation P.C.E. américaine... Et jeudi, Wall Street fermée pour Thanksgiving.",
     {"shots": [clip("13"), dict(clip("13b"), at_word=w(t, "jeudi"))]},
     [{"type": "news", "at_word": 2, "left": "AGENDA · ÉTATS-UNIS", "right": "CETTE SEMAINE", "tag": "À SURVEILLER",
       "headline": "Inflation PCE d'octobre mercredi 25 à 14 h 30 (heure de Paris), marchés fermés jeudi pour Thanksgiving", "highlight": "mercredi 25 à 14 h 30", "sub": FX}])

t = "Alors, un seul homme peut-il vraiment valoir 1 000 milliards ? Dis-le en commentaire."
beat(t, "Alors... un seul homme peut-il vraiment valoir mille milliards ? Dis-le en commentaire.", clip("14"),
     [{"type": "bigtitle", "lines": ["UN SEUL HOMME", "= 1 000 MILLIARDS ?"], "at_word": 1}])

t = ("Le marché peut basculer en une nuit. Sur mon Telegram gratuit : l'actu géopolitique et financière décortiquée, "
     "mes analyses d'actions détaillées et mes opportunités en temps réel. Plus de 22 000 personnes nous ont déjà rejoints. Entre dans le canal, lien en bio.")
s = ("Le marché peut basculer en une nuit... Sur mon Telegram gratuit : l'actu géopolitique et financière décortiquée, "
     "mes analyses d'actions détaillées et mes opportunités en temps réel. Plus de vingt-deux mille personnes nous ont déjà rejoints... Entre dans le canal, lien en bio.")
beat(t, s, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Nvidia : le retour de Huang décrypté", "imgs": ["tg_1eaa56f0.jpg", "tg_3435c02c_top.jpg"], "subs": 22760,
       "subs_at_word": w(t, "personnes"), "bio_at_word": w(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
     cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "24 novembre 2026", "brand": "Invest Family Fr", "hook_type": "breaking", "hook_formula": "le jour où",
        "cta_angle": "Le marché peut basculer en une nuit. Sur mon Telegram, tu le vois en direct.", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.fool.com/coverage/stock-market-today/2026/11/23/stock-market-today-nov-23-nvidia-surges-31-adding-nearly-usd1-trillion-in-market-value-as-jensen-huang-reclaims-ceo-role/",
                    "https://sg.finance.yahoo.com/news/live/stock-market-today-monday-november-23-dow-sp-500-nasdaq-surge-after-nvidia-reinstates-jensen-huang-182039397.html",
                    "https://www.foxbusiness.com/markets/stocks-november-23-2026",
                    "https://www.wsls.com/business/2026/11/24/asian-stocks-rally-after-wall-street-rebound-as-jensen-huang-returns-as-nvidias-ceo/",
                    "https://www.aol.com/articles/nvidia-asian-suppliers-rally-jensen-032213000.html",
                    "https://news.sbs.co.kr/english/article.do?news_id=N1008860722"],
        "beats": B}
json.dump(spec, open(f'{D}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'{D}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), "beats", sum(len(b["say"].split()) for b in B), "mots")
