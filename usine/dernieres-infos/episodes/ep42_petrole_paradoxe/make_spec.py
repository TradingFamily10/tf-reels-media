import json, sys
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep42_petrole_paradoxe'
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
TE = "Trading Economics · 20 nov. 2026"
OP = "OilPrice.com · 20 nov. 2026"
OP19 = "OilPrice.com · 19 nov. 2026"
IL = "investingLive · 20 nov. 2026"

t = "L'Iran attaque des pétroliers. Les Houthis menacent l'Arabie saoudite. Et pourtant, le pétrole s'effondre."
beat(t, "L'Iran attaque des pétroliers. Les Houthis menacent l'Arabie saoudite... Et pourtant, le pétrole s'effondre.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "pourtant"))]},
     [{"type": "date", "text": "Vendredi 20 novembre 2026 · Pétrole", "until_beat": 1},
      {"type": "news", "at_word": 0, "left": "PÉTROLE", "right": "20 NOV.", "tag": "PARADOXE",
       "headline": "Le pétrole file vers une troisième semaine de baisse, au plus bas depuis près de trois mois",
       "highlight": "troisième semaine de baisse", "sub": TE}])

t = "Vendredi, le baril américain est tombé autour de 82 dollars, au plus bas depuis près de trois mois."
beat(t, "Vendredi, le baril américain est tombé autour de quatre-vingt-deux dollars... au plus bas depuis près de trois mois.",
     {"screen": True, "under": clip("1")},
     [{"type": "screen_counter", "kicker": "PÉTROLE WTI · 20 NOV.", "value_from": 95, "value_to": 82, "decimals": 0,
       "prefix": "≈ ", "suffix": " $", "color": "red", "pill": "PLUS BAS DEPUIS PRÈS DE 3 MOIS", "desc": "Le baril de brut américain · " + TE}])

t = "Et ce n'est pas le pire : sur un mois, le baril a perdu 14 %."
beat(t, "Et ce n'est pas le pire : sur un mois, le baril a perdu quatorze pour cent.",
     {"screen": True, "under": clip("2")},
     [{"type": "screen_counter", "kicker": "PÉTROLE WTI · SUR UN MOIS", "value_from": 0, "value_to": -14, "decimals": 0,
       "prefix": "", "suffix": " %", "color": "red", "pill": "3e SEMAINE DE BAISSE D'AFFILÉE", "desc": TE}])

t = "Pourtant, l'Iran multiplie les attaques contre les pétroliers dans le détroit d'Ormuz."
beat(t, "Pourtant, l'Iran multiplie les attaques contre les pétroliers dans le détroit d'Ormuz.",
     {"shots": [clip("3"), dict(clip("3b"), at_word=w(t, "pétroliers"))]},
     [{"type": "news", "at_word": 1, "left": "DÉTROIT D'ORMUZ", "right": "20 NOV.", "tag": "IRAN",
       "headline": "L'Iran a intensifié ses attaques contre les pétroliers dans le détroit d'Ormuz ces dernières semaines",
       "highlight": "intensifié ses attaques", "sub": OP}])

t = "Les Houthis menacent de frapper Djeddah et les autres ports saoudiens de la mer Rouge."
beat(t, "Les Houthis menacent de frapper Djeddah... et les autres ports saoudiens de la mer Rouge.",
     {"shots": [clip("4"), dict(clip("4b"), at_word=w(t, "ports"))]},
     [{"type": "news", "at_word": 1, "left": "MER ROUGE", "right": "20 NOV.", "tag": "MENACE",
       "headline": "Les Houthis menacent Djeddah et les ports saoudiens si la coalition frappe le port yéménite d'Hodeïda",
       "highlight": "Djeddah et les ports saoudiens", "sub": IL}])

t = "Et Washington promet de durcir son blocus naval des ports iraniens."
beat(t, "Et Washington promet de durcir son blocus naval des ports iraniens.",
     {"shots": [clip("5"), dict(clip("5b"), at_word=w(t, "blocus"))]},
     [{"type": "news", "at_word": 1, "left": "ÉTATS-UNIS / IRAN", "right": "20 NOV.", "tag": "BLOCUS",
       "headline": "Les États-Unis vont durcir le blocus naval des ports iraniens, pendant que Téhéran veut relancer ses exportations",
       "highlight": "durcir le blocus naval", "sub": OP}])

t = "Alors, pourquoi le pétrole ne flambe-t-il pas ?"
beat(t, "Alors... pourquoi le pétrole ne flambe-t-il pas ?", clip("6"),
     [{"type": "bigtitle", "lines": ["POURQUOI ÇA", "NE FLAMBE PAS ?"], "at_word": w(t, "pourquoi")}])

t = "Ce paradoxe, je le décortique en direct sur mon Telegram. Lien en bio."
beat(t, "Ce paradoxe, je le décortique en direct sur mon Telegram. Lien en bio.", clip("7"),
     [{"type": "phone", "mode": "mini", "img": "tg_38e4f34b.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "La réponse : il y a trop de pétrole. L'Agence internationale de l'énergie voit un surplus d'environ 2 millions de barils par jour."
beat(t, "La réponse : il y a trop de pétrole. L'Agence internationale de l'énergie voit un surplus... d'environ deux millions de barils par jour.",
     {"screen": True, "under": clip("8")},
     [{"type": "screen_counter", "kicker": "SURPLUS MONDIAL", "value_from": 0, "value_to": 2, "decimals": 0,
       "prefix": "≈ ", "suffix": " M b/j", "color": "white", "pill": "PRÉVISION DE L'AIE", "desc": "Millions de barils par jour en trop · " + TE, "at_word": w(t, "Agence")}])

t = "Le brut passe quand même : selon le ministre américain de l'Énergie, les flux d'Ormuz sont à des niveaux records."
beat(t, "Le brut passe quand même : selon le ministre américain de l'Énergie... les flux d'Ormuz sont à des niveaux records.",
     {"shots": [clip("9"), dict(clip("9b"), at_word=w(t, "flux"))]},
     [{"type": "news", "at_word": 1, "left": "ÉNERGIE", "right": "20 NOV.", "tag": "ORMUZ",
       "headline": "Chris Wright, secrétaire américain à l'Énergie : les flux de pétrole par Ormuz atteignent des records",
       "highlight": "atteignent des records", "sub": TE}])

t = "Et aux États-Unis, les stocks de brut ont encore grimpé de 3,4 millions de barils, à près de 418 millions."
beat(t, "Et aux États-Unis, les stocks de brut ont encore grimpé de plus de trois millions de barils... à près de quatre cent dix-huit millions.",
     {"screen": True, "under": clip("10")},
     [{"type": "screen_duo",
       "a": {"kicker": "STOCKS US · 1 SEMAINE", "value_to": 3.38, "decimals": 2, "prefix": "+ ", "suffix": " M b", "color": "green", "desc": "Semaine au 13 nov. · EIA, via " + TE},
       "b_at_word": w(t, "418"),
       "b": {"kicker": "STOCKS US · TOTAL", "value_to": 417.8, "decimals": 1, "prefix": "", "suffix": " M b", "color": "white", "desc": "Millions de barils · EIA, via " + TE}}])

t = "Jeudi, États-Unis, Chine et Russie se sont même entendus pour produire plus de carburants."
beat(t, "Jeudi, États-Unis, Chine et Russie se sont même entendus pour produire plus de carburants.",
     {"shots": [clip("11"), dict(clip("11b"), at_word=w(t, "produire"))]},
     [{"type": "news", "at_word": 1, "left": "ACCORD À TROIS", "right": "19 NOV.", "tag": "OFFRE",
       "headline": "États-Unis, Chine et Russie d'accord pour augmenter la production et l'offre de produits pétroliers raffinés",
       "highlight": "augmenter la production", "sub": TE}])

t = "Pour Exxon, Chevron, TotalEnergies ou Shell, le Brent tient encore au-dessus de 92 dollars."
beat(t, "Pour Exxon, Chevron, TotalEnergies ou Shell, le Brent tient encore au-dessus de quatre-vingt-douze dollars.",
     {"screen": True, "under": clip("12")},
     [{"type": "screen_logos", "kicker": "GÉANTS DU PÉTROLE", "value_from": 0, "value_to": 92.57, "decimals": 2, "suffix": " $",
       "color": "white", "pill": "BRENT · 20 NOV.", "keys": ["XOM", "CVX", "TTE", "SHEL"], "desc": "ExxonMobil · Chevron · TotalEnergies · Shell · " + TE}])

t = "Le twist ? Un pétrole qui baisse en pleine guerre, c'est un signal : les marchés parient sur un ralentissement de l'économie d'ici 6 à 12 mois."
beat(t, "Le twist ? Un pétrole qui baisse en pleine guerre, c'est un signal : les marchés parient sur un ralentissement de l'économie... d'ici six à douze mois.",
     {"shots": [clip("13"), dict(clip("13b"), at_word=w(t, "marchés"))]},
     [{"type": "news", "at_word": w(t, "signal"), "left": "MARCHÉS", "right": "20 NOV.", "tag": "RALENTISSEMENT",
       "headline": "Les marchés continuent d'anticiper un ralentissement économique dans les 6 à 12 prochains mois",
       "highlight": "ralentissement économique", "sub": IL}])

t = "Car sur un an, le baril reste encore en hausse de 44 %."
beat(t, "Car sur un an, le baril reste encore en hausse de quarante-quatre pour cent.",
     {"screen": True, "under": clip("14")},
     [{"type": "screen_counter", "kicker": "PÉTROLE WTI · SUR UN AN", "value_from": 0, "value_to": 44, "decimals": 0,
       "prefix": "+ ", "suffix": " %", "color": "green", "pill": "MALGRÉ LA CHUTE DU MOIS", "desc": TE}])

t = "À surveiller : Donald Trump, qui se dit « pas pressé » de trancher sur l'Iran, puis la Fed, les 8 et 9 décembre."
beat(t, "À surveiller : Donald Trump, qui se dit « pas pressé » de trancher sur l'Iran... puis la Fed, les huit et neuf décembre.",
     {"shots": [clip("15"), dict(clip("15b"), at_word=w(t, "Fed"))]},
     [{"type": "tickers", "title": "À SURVEILLER", "rows": [
        {"name": "Décision sur l'Iran", "pct": "EN ATTENTE", "at_word": w(t, "Trump"), "up": True},
        {"name": "Réunion de la Fed", "pct": "8-9 DÉC.", "at_word": w(t, "Fed"), "up": True}]},
      {"type": "source", "text": TE + " · calendrier de la Fed"}])

t = "Alors, l'Iran peut-il encore faire flamber le pétrole ? Dis-le en commentaire."
beat(t, "Alors... l'Iran peut-il encore faire flamber le pétrole ? Dis-le en commentaire.", clip("16"),
     [{"type": "bigtitle", "lines": ["L'IRAN PEUT-IL", "TOUT RALLUMER ?"], "at_word": w(t, "flamber")}])

t = ("Un baril qui baisse en pleine guerre, personne ne te l'explique. Sur mon Telegram gratuit, si : "
     "actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. "
     "Plus de 22 000 personnes nous ont déjà rejoints. Lien en bio.")
say = ("Un baril qui baisse en pleine guerre, personne ne te l'explique... Sur mon Telegram gratuit, si : "
       "actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. "
       "Plus de vingt-deux mille personnes nous ont déjà rejoints. Lien en bio.")
beat(t, say, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Pétrole : le paradoxe Iran expliqué", "imgs": ["tg_4b2fa9a8.jpg", "tg_38e4f34b.jpg", "tg_3435c02c_top.jpg"],
       "subs": 22760, "subs_at_word": w(t, "22"), "bio_at_word": len(tokens(t)) - 1, "button": "ACCÈS GRATUIT"}],
     cta="long", endcard={"duration": 1.8, "button": "ACCÈS GRATUIT", "small": "Telegram gratuit · lien en bio"})

DROP = set(int(x) for x in sys.argv[1:])
B = [b for i, b in enumerate(B) if i not in DROP]
spec = {"id": EP, "date_label": "21 novembre 2026", "brand": "Invest Family Fr",
        "hook_type": "headline", "hook_formula": "contre-intuitif",
        "cta_angle": "Un baril qui baisse en pleine guerre, personne ne te l'explique. Mon Telegram, si.",
        "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad",
                  "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://tradingeconomics.com/commodity/crude-oil",
                    "https://oilprice.com/Latest-Energy-News/World-News/",
                    "https://investinglive.com/news/investinglive-european-news-wrap-stock-markets-remain-under-pressure-bonds-rally-on-slowdown-expectations"],
        "beats": B}
json.dump(spec, open(f'/home/claude/kit/episodes/{EP}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'/home/claude/kit/episodes/{EP}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), "beats", sum(len(tokens(b["text"])) for b in B), "mots")
