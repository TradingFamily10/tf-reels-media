import json, sys, os
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep51_hpe_paradoxe'
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
RT = "Reuters via SRN News · 24 nov. 2026, 11 h 26 (Paris)"
YH = "Yahoo Finance (ADVFN) · 24 nov. 2026"
YL = "Yahoo Finance · 24 nov. 2026"

t = "Des résultats au-dessus des attentes. Des commandes qui doublent. Et pourtant, HPE chute de 11 % avant l'ouverture."
beat(t, "Des résultats au-dessus des attentes. Des commandes qui doublent... Et pourtant, H.P.E. chute de onze pour cent avant l'ouverture.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "pourtant"))]},
     [{"type": "date", "text": "Mardi 24 novembre 2026 · Avant Wall Street", "until_beat": 1},
      {"type": "news", "at_word": 1, "left": "WALL STREET · HPE", "right": "24 NOV.", "tag": "PARADOXE",
       "headline": "HPE recule de 11,1 % en avant-Bourse malgré des résultats supérieurs aux attentes",
       "highlight": "11,1 %", "sub": RT + " · " + YH},
      {"type": "stock", "key": "HPE", "name": "Hewlett Packard Enterprise", "sub": "HPE · NYSE · avant-Bourse", "pct": "−11,1 %", "up": False, "y": 1480, "at_word": w(t, "HPE")}])

t = "Et ce n'est pas le pire : la veille, l'action avait pris plus de 17 %."
beat(t, "Et ce n'est pas le pire... la veille, l'action avait pris plus de dix-sept pour cent.",
     scr("1"),
     [{"type": "screen_duo", "a": {"kicker": "LUNDI 23 NOV.", "value_to": 17, "prefix": "+", "suffix": " %", "color": "green", "desc": "Séance de lundi, plus de +17 %", "logo": "HPE"},
       "b_at_word": w(t, "17"), "b": {"kicker": "MARDI · AVANT-BOURSE", "value_to": -11.1, "decimals": 1, "prefix": "", "suffix": " %", "color": "red", "desc": "Vers 5 h 26 à New York", "logo": "HPE"}},
      {"type": "source", "text": YH + " · " + RT}])

t = "Les chiffres sont solides : 14,55 milliards de dollars de chiffre d'affaires sur le trimestre, mieux que prévu."
beat(t, "Les chiffres sont solides : plus de quatorze milliards et demi de dollars de chiffre d'affaires sur le trimestre... mieux que prévu.",
     scr("2"),
     [{"type": "screen_counter", "kicker": "HPE · 4e TRIMESTRE FISCAL", "logo": "HPE", "value_from": 0, "value_to": 14.55, "decimals": 2, "prefix": "", "suffix": "", "color": "cyan",
       "pill": "MILLIARDS DE $ · AU-DESSUS DU CONSENSUS", "desc": "Chiffre d'affaires · " + YH + " (CNBC)"}])

t = "Les ventes cloud et IA grimpent d'environ 69 %, et le groupe ajoute 5 milliards de rachats d'actions."
beat(t, "Les ventes cloud et I.A. grimpent d'environ soixante-neuf pour cent... et le groupe ajoute cinq milliards de rachats d'actions.",
     {"shots": [clip("3"), dict(clip("3b"), at_word=w(t, "rachats"))]},
     [{"type": "ticket", "at_word": 0, "title": "HPE · LE BULLETIN", "subtitle": "4e trimestre fiscal 2026", "rows": [["Cloud & IA", "≈ +69 %"], ["Commandes IA", "× 2"], ["Rachats d'actions", "+5 Md$"]],
       "total": ["PRÉVISIONS", "AU-DESSUS"]},
      {"type": "source", "text": YH}])

t = "Alors pourquoi Wall Street sanctionne-t-elle les bonnes nouvelles ?"
beat(t, "Alors... pourquoi Wall Street sanctionne-t-elle les bonnes nouvelles ?", clip("4"),
     [{"type": "bigtitle", "lines": ["POURQUOI CETTE", "SANCTION ?"], "at_word": 1}])

t = "Ce paradoxe, je le suis en direct sur mon Telegram. Lien en bio."
beat(t, t, clip("5"), [{"type": "phone", "mode": "mini", "img": "tg_3435c02c.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "La réponse : toute l'IA reprend son souffle. Nvidia recule de plus de 4 % avant l'ouverture."
beat(t, "La réponse : toute l'I.A. reprend son souffle. Nvidia recule de plus de quatre pour cent avant l'ouverture.",
     {"shots": [clip("6"), dict(clip("6b"), at_word=w(t, "Nvidia"))]},
     [{"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "NVDA · Nasdaq · avant-Bourse", "pct": "−4,4 %", "up": False, "y": 560, "at_word": w(t, "Nvidia")},
      {"type": "source", "text": RT}])

t = "Lundi, elle avait bondi de 31 %, portée par le retour de son patron, Jensen Huang."
beat(t, "Lundi, elle avait bondi de trente et un pour cent... portée par le retour de son patron, Jensen Huang.",
     scr("7"),
     [{"type": "screen_counter", "kicker": "NVIDIA · LUNDI 23 NOV.", "logo": "NVDA", "value_from": 0, "value_to": 31.5, "decimals": 1, "prefix": "+", "suffix": " %", "color": "green",
       "pill": "PRÈS DE 1 000 MD$ GAGNÉS", "desc": RT}])

t = "Micron, AMD et Marvell perdent jusqu'à 4 %."
beat(t, "Micron, A.M.D. et Marvell perdent jusqu'à quatre pour cent.",
     scr("8"),
     [{"type": "screen_logos", "kicker": "PUCES · AVANT-BOURSE", "value_from": 0, "value_to": -4.3, "decimals": 1, "prefix": "", "suffix": " %", "color": "red",
       "pill": "DE −3,3 % À −4,3 %", "keys": ["MU", "AMD", "MRVL"], "desc": "Micron · AMD · Marvell · " + RT}])

t = "Et les contrats sur le Nasdaq 100 cèdent plus de 1 %."
beat(t, "Et les contrats sur le Nasdaq cent cèdent plus d'un pour cent.",
     scr("9"),
     [{"type": "screen_counter", "kicker": "NASDAQ 100 · CONTRATS À TERME", "value_from": 0, "value_to": -1.11, "decimals": 2, "prefix": "", "suffix": " %", "color": "red",
       "pill": "MARDI · 5 H 26 À NEW YORK", "desc": "S&P 500 −0,46 % · Dow −0,14 % · " + RT}])

t = "Mais le vrai poids lourd, il est ailleurs : la Fed."
beat(t, "Mais le vrai poids lourd... il est ailleurs : la Fed.", clip("10"),
     [{"type": "bigtitle", "lines": ["LE VRAI POIDS LOURD :", "LA FED"], "at_word": 2}])

t = "Les marchés voient désormais à 95 % une hausse de ses taux d'un quart de point en décembre."
beat(t, "Les marchés voient désormais à quatre-vingt-quinze pour cent... une hausse de ses taux d'un quart de point en décembre.",
     scr("11"),
     [{"type": "screen_counter", "kicker": "FED · RÉUNION DE DÉCEMBRE", "value_from": 0, "value_to": 95, "decimals": 0, "prefix": "", "suffix": " %", "color": "red",
       "pill": "PROBABILITÉ D'UNE HAUSSE DE 0,25 PT", "desc": YL + " · CME FedWatch"}])

t = "Et certains envisagent même un demi-point."
beat(t, "Et certains envisagent même... un demi-point.",
     {"shots": [clip("12")]},
     [{"type": "news", "at_word": 1, "left": "FED · TAUX", "right": "DÉCEMBRE", "tag": "SCÉNARIO",
       "headline": "Une faible probabilité d'une hausse d'un demi-point, contre zéro la veille", "highlight": "un demi-point", "sub": RT + " · CME FedWatch"}])

t = "Des taux plus hauts, c'est de l'argent plus cher… et des valorisations de l'IA plus dures à justifier."
beat(t, "Des taux plus hauts, c'est de l'argent plus cher... et des valorisations de l'I.A. plus dures à justifier.",
     {"shots": [clip("13"), dict(clip("13b"), at_word=w(t, "valorisations"))]},
     [{"type": "bigtitle", "lines": ["ARGENT PLUS CHER", "= IA SOUS PRESSION"], "at_word": 3}])

t = "Prochain rendez-vous : demain, l'inflation PCE, la dernière grosse statistique avant la Fed."
beat(t, "Prochain rendez-vous : demain, l'inflation P.C.E., la dernière grosse statistique avant la Fed.",
     {"shots": [clip("14")]},
     [{"type": "news", "at_word": 2, "left": "AGENDA · ÉTATS-UNIS", "right": "MER. 25 NOV.", "tag": "À SURVEILLER",
       "headline": "L'indice PCE, dernière statistique majeure avant la dernière réunion de la Fed de l'année", "highlight": "dernière statistique majeure", "sub": RT}])

t = "Alors, simple pause après un rebond historique… ou début d'une nouvelle secousse ? Dis-le en commentaire."
beat(t, "Alors... simple pause après un rebond historique... ou début d'une nouvelle secousse ? Dis-le en commentaire.", clip("15"),
     [{"type": "bigtitle", "lines": ["SIMPLE PAUSE OU", "NOUVELLE SECOUSSE ?"], "at_word": 1}])

t = ("Si tu veux comprendre avant les autres au lieu de subir, rejoins plus de 22 000 personnes sur mon Telegram gratuit : l'actu géopolitique et financière décortiquée, "
     "mes analyses d'actions détaillées et mes opportunités en temps réel. Entre dans le canal, lien en bio.")
s = ("Si tu veux comprendre avant les autres... au lieu de subir, rejoins plus de vingt-deux mille personnes sur mon Telegram gratuit : l'actu géopolitique et financière décortiquée, "
     "mes analyses d'actions détaillées et mes opportunités en temps réel. Entre dans le canal, lien en bio.")
beat(t, s, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "HPE, Nvidia, Fed : le paradoxe décrypté", "imgs": ["tg_1eaa56f0.jpg", "tg_3435c02c_top.jpg", "tg_4b2fa9a8.jpg"], "subs": 22760,
       "subs_at_word": w(t, "personnes"), "bio_at_word": w(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
     cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "24 novembre 2026", "brand": "Invest Family Fr", "hook_type": "headline", "hook_formula": "contre-intuitif",
        "cta_angle": "Si tu veux comprendre avant les autres au lieu de subir…", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://srnnews.com/wall-st-futures-dip-as-chip-stocks-cool-after-nvidia-fueled-rally/",
                    "https://finance.yahoo.com/markets/stocks/articles/us-stock-futures-mixed-nvidia-101442654.html",
                    "https://finance.yahoo.com/markets/live/stock-market-today-tuesday-november-24-dow-sp-500-nasdaq-rebound-090614276.html"],
        "beats": B}
json.dump(spec, open(f'{D}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'{D}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), "beats", sum(len(b["say"].split()) for b in B), "mots")
