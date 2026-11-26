import json, sys, os
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep57_petrole_ras_tanura'
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
NAT = "The National · 26 nov. 2026"
RT = "Reuters / Arab News · 26 nov. 2026"
PIQ = "Reuters / PiQ · 26 nov. 2026"
UBH = "Kpler via Reuters · 26 nov. 2026"

t = "Ton plein va-t-il encore grimper ? Le Brent a pris près de 6 % en deux séances."
beat(t, "Ton plein va-t-il encore grimper ? Le Brent a pris près de six pour cent... en deux séances.",
     {"shots": [clip("1"), dict(clip("0b"), at_word=w(t, "Brent"))]},
     [{"type": "date", "text": "JEUDI 26 NOVEMBRE 2026"},
      {"type": "bigtitle", "lines": ["TON PLEIN VA-T-IL", "ENCORE GRIMPER ?"], "at_word": 0}])

t = "Et ce n'est pas le pire : la cible, c'est Ras Tanura, la plus grande raffinerie saoudienne, opérée par Aramco."
beat(t, "Et ce n'est pas le pire... la cible, c'est Ras Tanura, la plus grande raffinerie saoudienne, opérée par Aramco.",
     {"shots": [clip("5"), dict(clip("1b"), at_word=w(t, "raffinerie"))]},
     [{"type": "bigtitle", "lines": ["RAS TANURA", "N°1 DU ROYAUME"], "at_word": w(t, "Ras")},
      {"type": "stock", "key": "ARAMCO", "name": "Saudi Aramco", "sub": "Opérateur de Ras Tanura", "y": 1480, "at_word": w(t, "Aramco")},
      {"type": "source", "text": RT}])

t = "Elle raffine 550 000 barils chaque jour."
beat(t, "Elle raffine cinq cent cinquante mille barils... chaque jour.", scr("2"),
     [{"type": "screen_counter", "kicker": "RAS TANURA · RAFFINAGE", "value_from": 0, "value_to": 550000, "decimals": 0, "prefix": "", "suffix": "", "color": "white", "pill": "BARILS PAR JOUR", "desc": "Aussi un grand terminal d'exportation · " + NAT}])

t = "Les Houthis revendiquent une frappe « précise et directe », avec des incendies."
beat(t, "Les Houthis revendiquent une frappe... précise et directe, avec des incendies.", clip("9"),
     [{"type": "news", "at_word": w(t, "revendiquent"), "left": "YÉMEN · HOUTHIS", "right": "25 NOV.", "tag": "REVENDICATION", "headline": "Le porte-parole Yahya Saree parle d'une frappe « précise et directe » sur Ras Tanura, qui aurait provoqué des incendies", "highlight": "précise et directe", "sub": "Revendication non confirmée · " + PIQ}])

t = "Riyad, elle, affirme avoir détruit quatre drones."
beat(t, "Riyad, elle, affirme avoir détruit... quatre drones.", {"shots": [clip("4"), dict(clip("4b"), at_word=w(t, "quatre"))]},
     [{"type": "bigtitle", "lines": ["4 DRONES", "INTERCEPTÉS"], "at_word": w(t, "quatre")},
      {"type": "source", "text": NAT}])

t = "Pourtant, le Brent a bondi de 3,5 % mercredi, puis touché 95,31 $ ce matin."
beat(t, "Pourtant, le Brent a bondi de plus de trois pour cent mercredi... puis touché quatre-vingt-quinze dollars ce matin.", {"screen": True, "under": clip("0b", ss=8)},
     [{"type": "screen_duo", "a": {"kicker": "BRENT · MERCREDI 25 NOV.", "value_to": 3.5, "decimals": 1, "prefix": "+", "suffix": " %", "color": "green", "desc": "Clôture à 94,61 $"},
       "b_at_word": w(t, "puis"), "b": {"kicker": "BRENT · JEUDI 26 NOV.", "value_to": 95.31, "decimals": 2, "prefix": "", "suffix": " $", "color": "green", "desc": "+0,74 % · 9h13 heure des Émirats"}},
      {"type": "source", "text": NAT}])

t = "Alors, pourquoi le marché s'affole pour une raffinerie qui tient debout ?"
beat(t, "Alors... pourquoi le marché s'affole pour une raffinerie qui tient debout ?", clip("6"),
     [{"type": "bigtitle", "lines": ["POURQUOI", "CETTE PANIQUE ?"], "at_word": 1}])

t = "Cette crise du pétrole, je la suis en direct sur mon Telegram. Lien en bio."
beat(t, "Cette crise du pétrole, je la suis en direct sur mon Telegram. Lien en bio.", clip("7"),
     [{"type": "phone", "mode": "mini", "img": "tg_3435c02c.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "La vraie réponse est ailleurs : dans le détroit d'Ormuz."
beat(t, "La vraie réponse est ailleurs... dans le détroit d'Ormuz.", clip("3"),
     [{"type": "bigtitle", "lines": ["LE VRAI DANGER", "ORMUZ"], "at_word": w(t, "détroit")}])

t = "Mercredi, un pétrolier y a heurté une mine et pris feu."
beat(t, "Mercredi, un pétrolier y a heurté une mine... et pris feu.", clip("8"),
     [{"type": "news", "at_word": w(t, "heurté"), "left": "DÉTROIT D'ORMUZ", "right": "25 NOV.", "tag": "MINE NAVALE", "headline": "Un pétrolier heurte une mine et prend feu dans une « zone restreinte » du détroit", "highlight": "prend feu", "sub": "Armée iranienne via Fars · " + RT}])

t = "D'après Kpler, 12 attaques de pétroliers dans le Golfe en novembre, après 17 en octobre."
beat(t, "D'après Kpler, douze attaques de pétroliers dans le Golfe en novembre... après dix-sept en octobre.", scr("10"),
     [{"type": "screen_duo", "a": {"kicker": "ATTAQUES · OCTOBRE", "value_to": 17, "decimals": 0, "prefix": "", "suffix": "", "color": "red", "desc": "Golfe persique"},
       "b_at_word": w(t, "novembre"), "b": {"kicker": "NOVEMBRE · DÉJÀ", "value_to": 12, "decimals": 0, "prefix": "", "suffix": "", "color": "red", "desc": "Et le mois n'est pas fini"}},
      {"type": "source", "text": UBH}])

t = "Et le trafic fond : plus de 20 millions de barils par jour mi-octobre, moins de 14 millions en novembre."
beat(t, "Et le trafic fond : plus de vingt millions de barils par jour mi-octobre... moins de quatorze millions en novembre.", scr("11"),
     [{"type": "screen_duo", "a": {"kicker": "ORMUZ · MI-OCTOBRE", "value_to": 20, "decimals": 0, "prefix": "> ", "suffix": " M b/j", "color": "white", "desc": "Pétroliers en transit"},
       "b_at_word": w(t, "moins"), "b": {"kicker": "ORMUZ · NOVEMBRE", "value_to": 13.96, "decimals": 2, "prefix": "", "suffix": " M b/j", "color": "red", "desc": "2e semaine de novembre · Kpler"}},
      {"type": "source", "text": UBH}])

t = "Le paradoxe : selon l'AIE, les stocks de brut ont gonflé de 1,7 million de barils par jour en octobre."
beat(t, "Le paradoxe... selon l'A.I.E., les stocks de brut ont gonflé de près de deux millions de barils par jour en octobre.", scr("14b"),
     [{"type": "screen_counter", "kicker": "AIE · STOCKS · OCTOBRE", "value_from": 0, "value_to": 1.7, "decimals": 1, "prefix": "+", "suffix": " M b/j", "color": "green", "pill": "TROP-PLEIN ?", "desc": "Les exportations du Golfe ont repris plus vite que la demande · " + NAT}])

t = "Verdict dimanche : l'OPEP+ fixe sa production pour 2027, sans les Émirats."
beat(t, "Verdict dimanche : l'OPEP plus fixe sa production pour deux mille vingt-sept... sans les Émirats.", clip("15"),
     [{"type": "bigtitle", "lines": ["DIMANCHE 29/11", "L'OPEP+ TRANCHE"], "at_word": w(t, "dimanche")},
      {"type": "source", "text": RT}])

t = "Alors, géopolitique ou trop-plein : qui va l'emporter ? Dis-le en commentaire."
beat(t, "Alors... géopolitique ou trop-plein : qui va l'emporter ? Dis-le en commentaire.", {"shots": [clip("14"), dict(clip("16"), at_word=w(t, "qui"))]},
     [{"type": "bigtitle", "lines": ["GÉOPOLITIQUE", "OU TROP-PLEIN ?"], "at_word": 1}])

t = ("Plus de 22 000 personnes ont déjà une longueur d'avance. Il manque toi. Sur mon Telegram gratuit : l'actu géopolitique et financière décortiquée, "
     "mes analyses d'actions détaillées et mes opportunités en temps réel. Rejoins la famille, lien en bio.")
s = ("Plus de vingt-deux mille personnes ont déjà une longueur d'avance... Il manque toi. Sur mon Telegram gratuit : l'actu géopolitique et financière décortiquée, "
     "mes analyses d'actions détaillées et mes opportunités en temps réel. Rejoins la famille, lien en bio.")
beat(t, s, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Pétrole : Ras Tanura, Ormuz et l'OPEP+ dimanche, mon décryptage", "imgs": ["tg_4b2fa9a8.jpg", "tg_1eaa56f0.jpg", "tg_38e4f34b.jpg"], "subs": 22760,
       "subs_at_word": w(t, "personnes"), "bio_at_word": w(t, "bio"), "button": "REJOINS LA FAMILLE"}],
     cta="long", endcard={"duration": 1.8, "button": "REJOINS LA FAMILLE", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "26 novembre 2026", "brand": "Invest Family Fr", "hook_type": "question", "hook_formula": "question directe",
        "cta_angle": "22 000 personnes ont déjà la longueur d'avance. Il manque toi.", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.thenationalnews.com/business/energy/2026/11/26/oil-rebounds-to-95-per-barrel-after-saudi-refinery-attack/",
                    "https://www.arabnews.com/energy/oil-rises-on-supply-concerns-as-iran-claims-9-strikes-on-ships-3014091",
                    "https://piqmarkets.com/story/brent-holds-near-94-71-after-houthi-claim-on-ras-tanura-refinery",
                    "https://unbiasedheadlines.com/article/brent-rises-to-9471-thursday-for-a-third-straight-gain-as-houthis-claim-ras",
                    "https://wisevoter.com/world/2026/11/26/houthis-attack-saudi-ras-tanura-refinery-oil-prices",
                    "https://www.boursorama.com/bourse/actualites/l-europe-ouvre-dans-le-vert-thanksgiving-fait-oublier-les-craintes-sur-la-tech-e468ceb8481cf4c8fa3f4fbf745caf86"],
        "beats": B}
json.dump(spec, open(f'{D}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'{D}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), "beats", sum(len(b["say"].split()) for b in B), "mots")
