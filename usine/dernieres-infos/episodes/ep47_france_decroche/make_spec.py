import json, sys, os
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep47_france_decroche'
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
IL = "HCOB / S&P Global via investingLive · 23 nov. 2026"
RT = "Reuters via Investing.com · 23 nov. 2026"
AFP = "AFP via Boursorama · 23 nov. 2026, 9h45"
BO = "Boursorama · 23 nov. 2026"

t = "L'Allemagne accélère. La France recule. Pourquoi un tel écart, du jamais vu depuis six ans ?"
beat(t, "L'Allemagne accélère... La France recule. Pourquoi un tel écart, du jamais vu depuis six ans ?",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "France"))]},
     [{"type": "date", "text": "Lundi 23 novembre 2026 · Zone euro", "until_beat": 1},
      {"type": "bigtitle", "lines": ["FRANCE – ALLEMAGNE :", "LE GRAND ÉCART ?"], "at_word": 0}])

t = "Et ce n'est pas le pire : le privé français recule au plus vite depuis six mois."
beat(t, "Et ce n'est pas le pire : le privé français recule au plus vite depuis six mois.",
     scr("1"),
     [{"type": "screen_counter", "kicker": "FRANCE · PMI COMPOSITE FLASH", "value_from": 50, "value_to": 46.2, "decimals": 1,
       "prefix": "", "suffix": "", "color": "red", "pill": "SOUS 50 = L'ACTIVITÉ RECULE",
       "desc": "Novembre 2026 · attendu 48,1 · " + IL}])

t = "L'industrie plonge sous les 48 points, bien en dessous des prévisions."
beat(t, "L'industrie plonge sous les quarante-huit points... bien en dessous des prévisions.",
     scr("2"),
     [{"type": "screen_duo",
       "a": {"kicker": "INDUSTRIE · ATTENDU", "value_to": 49.9, "decimals": 1, "prefix": "", "suffix": "", "color": "gold", "desc": "Consensus · PMI manufacturier France"},
       "b_at_word": w(t, "48"),
       "b": {"kicker": "INDUSTRIE · PUBLIÉ", "value_to": 47.9, "decimals": 1, "prefix": "", "suffix": "", "color": "red", "desc": "Novembre 2026 · " + IL}}])

t = "En face, l'Allemagne tourne à plein régime : sa croissance la plus rapide depuis quatre ans et demi."
beat(t, t, {"shots": [clip("3"), dict(clip("3b"), at_word=w(t, "croissance"))]},
     [{"type": "news", "at_word": w(t, "Allemagne"), "left": "ALLEMAGNE · PMI", "right": "23 NOV.", "tag": "ACCÉLÉRATION",
       "headline": "La croissance allemande au plus rapide depuis quatre ans et demi, selon S&P Global",
       "highlight": "quatre ans et demi", "sub": IL}])

t = "Résultat : la zone euro tient debout à 51,7… grâce à Berlin."
beat(t, "Résultat : la zone euro tient debout... grâce à Berlin.",
     scr("4"),
     [{"type": "screen_duo",
       "a": {"kicker": "FRANCE", "value_to": 46.2, "decimals": 1, "prefix": "", "suffix": "", "color": "red", "desc": "PMI composite flash · novembre"},
       "b_at_word": w(t, "zone"),
       "b": {"kicker": "ZONE EURO", "value_to": 51.7, "decimals": 1, "prefix": "", "suffix": "", "color": "gold", "desc": "5e mois de croissance d'affilée · " + RT}}])

t = "Alors, qu'est-ce qui bloque la France ?"
beat(t, "Alors... qu'est-ce qui bloque la France ?", clip("5"),
     [{"type": "bigtitle", "lines": ["QU'EST-CE QUI", "BLOQUE LA FRANCE ?"], "at_word": 1}])

t = "Ce décrochage, je le décortique chaque jour sur mon Telegram. Lien en bio."
beat(t, t, clip("6"),
     [{"type": "phone", "mode": "mini", "img": "tg_3435c02c_top.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "Réponse : l'attente. Les clients repoussent leurs projets avant une présidentielle 2027 très incertaine."
beat(t, "Réponse : l'attente. Les clients repoussent leurs projets... avant une présidentielle très incertaine.",
     {"shots": [clip("7"), dict(clip("7b"), at_word=w(t, "clients"))]},
     [{"type": "news", "at_word": w(t, "clients"), "left": "FRANCE · S&P GLOBAL", "right": "23 NOV.", "tag": "ANALYSE",
       "headline": "Des clients qui hésitent à s'engager avant une période électorale très incertaine l'an prochain",
       "highlight": "période électorale très incertaine", "sub": "Joe Hayes, S&P Global · " + IL}])

t = "Le moral des chefs d'entreprise tombe au plus bas depuis fin 2012, hors Covid."
beat(t, "Le moral des chefs d'entreprise tombe au plus bas depuis fin deux mille douze... hors Covid.",
     scr("8"),
     [{"type": "screen_gauge", "kicker": "MORAL DES ENTREPRISES FRANÇAISES", "pill": "AU PLUS BAS DEPUIS FIN 2012 (HORS COVID)",
       "desc": "Indice d'activité future · " + IL}])

t = "S&P Global prévient : le risque de récession technique au quatrième trimestre augmente."
beat(t, "S. and P. Global prévient : le risque de récession technique au quatrième trimestre augmente.",
     {"shots": [clip("9"), dict(clip("9b"), at_word=w(t, "récession"))]},
     [{"type": "news", "at_word": w(t, "risque"), "left": "FRANCE · CONJONCTURE", "right": "T4 2026", "tag": "ALERTE",
       "headline": "Les données de novembre augmentent le risque d'une récession technique en France au 4e trimestre",
       "highlight": "récession technique", "sub": "Joe Hayes, S&P Global · " + IL}])

t = "Les marchés le voient aussi : à 10 ans, la France paie désormais 1,5 point de plus que l'Allemagne pour emprunter."
beat(t, "Les marchés le voient aussi : à dix ans, la France paie désormais un point et demi de plus que l'Allemagne pour emprunter.",
     scr("10"),
     [{"type": "screen_duo",
       "a": {"kicker": "FRANCE · TAUX À 10 ANS", "value_to": 4.82, "decimals": 2, "prefix": "", "suffix": " %", "color": "red", "desc": "Contre 4,87 % vendredi · " + AFP},
       "b_at_word": w(t, "point"),
       "b": {"kicker": "ALLEMAGNE · TAUX À 10 ANS", "value_to": 3.32, "decimals": 2, "prefix": "", "suffix": " %", "color": "gold", "desc": "Référence en Europe · " + AFP}}])

t = "Un écart de 150 points de base : Paris paie bien plus cher pour s'endetter."
beat(t, "Un écart de cent cinquante points de base : Paris paie bien plus cher pour s'endetter.",
     scr("11"),
     [{"type": "screen_counter", "kicker": "ÉCART FRANCE – ALLEMAGNE · 10 ANS", "value_from": 0, "value_to": 150, "decimals": 0,
       "prefix": "", "suffix": " pb", "color": "red", "pill": "4,82 % − 3,32 % · CALCUL",
       "desc": "Taux à 9h45 · " + AFP}])

t = "Le paradoxe : ce lundi, le CAC 40 rebondit quand même, et STMicro repart après un plongeon de 10,81 % vendredi."
beat(t, "Le paradoxe : ce lundi, le CAC quarante rebondit quand même... et S.T. Micro repart, après un plongeon de près de onze pour cent vendredi.",
     {"shots": [clip("12"), dict(clip("12b"), at_word=w(t, "STMicro"))]},
     [{"type": "tickers", "title": "PARIS · LUNDI 23 NOV. · 9H45",
       "rows": [{"name": "CAC 40", "pct": "+0,62 %", "at_word": w(t, "CAC")},
                {"key": "STM", "name": "STMicroelectronics", "pct": "+1,76 %", "at_word": w(t, "STMicro")},
                {"key": "STM", "name": "STMicro · vendredi", "pct": "−10,81 %", "at_word": w(t, "plongeon")}]},
      {"type": "source", "text": AFP}])

t = "À surveiller cette semaine : le PIB français et l'indice Ifo allemand, avant la BCE à la mi-décembre."
beat(t, "À surveiller cette semaine : le P.I.B. français et l'indice Ifo allemand... avant la B.C.E., à la mi-décembre.",
     {"shots": [clip("13"), dict(clip("13b"), at_word=w(t, "BCE"))]},
     [{"type": "news", "at_word": w(t, "PIB"), "left": "AGENDA · ZONE EURO", "right": "CETTE SEMAINE", "tag": "À SURVEILLER",
       "headline": "PIB français, indice Ifo allemand, puis la réunion de la BCE à la mi-décembre",
       "highlight": "PIB français", "sub": BO}])

t = "Alors, la France peut-elle encore éviter la récession ? Dis-le en commentaire."
beat(t, "Alors... la France peut-elle encore éviter la récession ? Dis-le en commentaire.",
     clip("14"),
     [{"type": "bigtitle", "lines": ["LA FRANCE PEUT-ELLE", "ÉVITER LA RÉCESSION ?"], "at_word": w(t, "France")}])

t = "Chaque matin, je fais le tri dans le bruit pour toi : actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. Tout est sur mon Telegram gratuit, et plus de 22 000 personnes y sont déjà. Entre dans le canal, lien en bio."
say = "Chaque matin, je fais le tri dans le bruit pour toi : actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. Tout est sur mon Telegram gratuit, et plus de vingt-deux mille personnes y sont déjà... Entre dans le canal, lien en bio."
beat(t, say, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "France vs Allemagne : le décrochage expliqué", "imgs": ["tg_3435c02c_top.jpg", "tg_1eaa56f0.jpg"],
       "subs": 22760, "subs_at_word": w(t, "22"), "bio_at_word": w(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
     cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})

CUT = [int(x) for x in sys.argv[1:]]
B = [b for i, b in enumerate(B) if i not in CUT]
spec = {"id": EP, "date_label": "23 novembre 2026", "brand": "Invest Family Fr", "hook_type": "question",
        "hook_formula": "question directe",
        "cta_angle": "Chaque matin, je fais le tri dans le bruit pour toi",
        "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://investinglive.com/news/france-november-flash-services-pmi-46-6-vs-47-5-expected/",
                    "https://investinglive.com/news/eurozone-november-flash-services-pmi-51-2-vs-51-8-expected/",
                    "https://www.investing.com/news/economic-indicators/euro-zone-growth-holds-steady-but-frances-deepening-downturn-clouds-outlook-pmi-shows-5044744",
                    "https://www.boursorama.com/bourse/actualites/la-bourse-de-paris-tente-un-rebond-apres-une-semaine-de-secousses-sur-l-ia-88db1f584f9ff6950397c4f4d6e677be",
                    "https://www.boursorama.com/bourse/actualites/du-vert-pour-les-bourses-europeennes-avec-un-indice-pmi-plutot-rassurant-a8b39cd3f76d248a2bbf0a318b6aa8ad",
                    "https://www.boursorama.com/bourse/actualites/zone-euro-la-croissance-du-secteur-prive-se-poursuit-en-novembre-507cb3973b1f01d920e6beae147fcd1e"],
        "beats": B}
json.dump(spec, open(f'{D}/spec.json', 'w'), ensure_ascii=False, indent=1)
txt = "\n".join(b["say"] for b in B)
open(f'{D}/voice_text.txt', 'w').write(txt)
print(len(B), "beats", len(txt.split()), "mots")
