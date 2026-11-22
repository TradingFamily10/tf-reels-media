import json, sys
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep44_ia_argent_prive'
def w(text, word, n=0):
    t = tokens(text); k = 0
    for i, x in enumerate(t):
        if word.lower() in x.lower():
            if k == n: return i
            k += 1
    raise SystemExit(f"mot introuvable: {word} dans {text}")
def clip(n, ss=1, cx=0.5):
    return {"clip": f"b{n}.mp4", "ss": ss, "cx": cx}
def scr(n): return {"screen": True, "under": clip(n)}
B = []
def beat(text, say, bg, overlays, **kw):
    b = {"text": text, "say": say, "bg": bg, "overlays": overlays}; b.update(kw); B.append(b); return b
HC = "Hervé Cuviliez · Market News · 21 nov. 2026"
TP = "Ted Pillows · rapport marchés · 21 nov. 2026"
MC = "Marketcalls · bilan hebdo · 21 nov. 2026"
EM = "Emergent · 2 nov. 2026"
BI = "Brown Insights · The Weekender · 21 nov. 2026"

t = "Tout le monde regarde le Nasdaq plonger. Pendant ce temps, 300 milliards de dollars de valorisation se négocient en coulisses."
beat(t, "Tout le monde regarde le Nasdaq plonger... Pendant ce temps, trois cents milliards de dollars de valorisation se négocient en coulisses.",
     scr("0"),
     [{"type": "date", "text": "Dimanche 22 novembre 2026 · Intelligence artificielle", "until_beat": 0},
      {"type": "screen_logos", "kicker": "PENDANT LA CHUTE DE L'I.A.", "value_from": 0, "value_to": 300, "decimals": 0,
       "prefix": "", "suffix": " Md$", "color": "gold", "pill": "DATABRICKS 225 + COGNITION 75",
       "keys": ["NVDA", "ORCL", "PANW", "ANT", "AMD", "MSFT"],
       "desc": "Valorisations en discussion, non finalisées · " + HC}])

t = "Et ce n'est pas le pire : vendredi, le Nasdaq a encore perdu plus de 5 %. Il passe dans le rouge sur 2026."
beat(t, "Et ce n'est pas le pire : vendredi, le Nasdaq a encore perdu plus de cinq pour cent... Il passe dans le rouge sur deux mille vingt-six.",
     scr("1"),
     [{"type": "screen_counter", "kicker": "NASDAQ · VENDREDI 20 NOV.", "value_from": 0, "value_to": -5.3, "decimals": 1,
       "prefix": "", "suffix": " %", "color": "red", "pill": "NÉGATIF SUR 2026",
       "desc": "Clôture 22 618 pts · " + TP}])

t = "Sur cinq séances, le Nasdaq efface 10 %. L'Europe, près de 6 %."
beat(t, "Sur cinq séances, le Nasdaq efface dix pour cent... L'Europe, près de six pour cent.",
     {"shots": [clip("2"), dict(clip("2b"), at_word=w(t, "L'Europe"))]},
     [{"type": "tickers", "title": "LA SEMAINE DU 16 AU 20 NOV.",
       "rows": [{"name": "Nasdaq", "pct": "−10,02 %", "at_word": w(t, "Nasdaq"), "up": False},
                {"name": "S&P 500", "pct": "−8,61 %", "at_word": w(t, "efface"), "up": False},
                {"name": "Stoxx 600 (Europe)", "pct": "−5,8 %", "at_word": w(t, "L'Europe"), "up": False}]},
      {"type": "source", "text": MC + " · " + TP}])

t = "Pourtant, dans le privé, Databricks discute d'une levée à 225 milliards de dollars. Contre 190 milliards en août."
beat(t, "Pourtant, dans le privé, Databricks discute d'une levée à deux cent vingt-cinq milliards de dollars... Contre cent quatre-vingt-dix milliards en août.",
     scr("3"),
     [{"type": "screen_duo",
       "a": {"kicker": "DATABRICKS · AOÛT 2026", "value_to": 190, "decimals": 0, "prefix": "", "suffix": " Md$", "color": "gold", "desc": "Valorisation de la dernière levée · " + HC},
       "b_at_word": w(t, "Contre"),
       "b": {"kicker": "DATABRICKS · NOVEMBRE", "value_to": 225, "decimals": 0, "prefix": "", "suffix": " Md$", "color": "green", "desc": "Discussions préliminaires (WSJ) · " + HC}}])

t = "Cognition, la start-up du codeur automatique Devin, vise 75 milliards. Elle en valait 48 en septembre."
beat(t, "Cognition, la start-up du codeur automatique Devin, vise soixante-quinze milliards... Elle en valait quarante-huit en septembre.",
     scr("4"),
     [{"type": "screen_counter", "kicker": "COGNITION · VALORISATION VISÉE", "value_from": 48, "value_to": 75, "decimals": 0,
       "prefix": "", "suffix": " Md$", "color": "green", "pill": "+56 % EN DEUX MOIS",
       "desc": "48 Md$ en sept. → 75 Md$ en discussion, levée de plus de 2 Md$ non finalisée · " + HC}])

t = "Alors, qui a raison : la Bourse qui décroche, ou les fonds qui misent encore ?"
beat(t, "Alors... qui a raison : la Bourse qui décroche, ou les fonds qui misent encore ?",
     clip("5"),
     [{"type": "bigtitle", "lines": ["QUI A", "RAISON ?"], "at_word": 1}])

t = "Ce bras de fer, je le décortique en direct sur mon Telegram. Lien en bio."
beat(t, t, clip("6"),
     [{"type": "phone", "mode": "mini", "img": "tg_1eaa56f0.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "Regarde Oracle. Vendredi soir, le groupe assure que son contrat avec OpenAI est entièrement financé."
beat(t, "Regarde Oracle... Vendredi soir, le groupe assure que son contrat avec OpenAI est entièrement financé.",
     {"shots": [clip("7"), dict(clip("7b"), at_word=w(t, "Vendredi"))]},
     [{"type": "stock", "key": "ORCL", "name": "Oracle", "sub": "Déclaration du 20 nov. 2026", "y": 520, "at_word": w(t, "Oracle")},
      {"type": "news", "at_word": w(t, "assure"), "left": "ORACLE · COMMUNIQUÉ", "right": "20 NOV.", "tag": "OPENAI",
       "headline": "Oracle affirme que son contrat avec OpenAI est « entièrement financé »",
       "highlight": "« entièrement financé »", "sub": HC}])

t = "Mais pour y arriver, Oracle a levé 20 milliards de dollars ce mois-ci. La moitié en dette."
beat(t, "Mais pour y arriver, Oracle a levé vingt milliards de dollars ce mois-ci... La moitié en dette.",
     {"screen": True, "under": clip("8", ss=4)},
     [{"type": "screen_counter", "kicker": "ORACLE · LEVÉE DE NOVEMBRE", "value_from": 0, "value_to": 20, "decimals": 0,
       "prefix": "", "suffix": " Md$", "color": "gold", "pill": "10 EN ACTIONS · 10 EN OBLIGATIONS",
       "desc": "Lancée le 2 nov. 2026 · " + EM + " · " + HC}])

t = "Et les rachats continuent : Palo Alto Networks paie 4,5 milliards en actions pour Applied Compute, une équipe née il y a dix-huit mois."
beat(t, "Et les rachats continuent : Palo Alto Networks paie quatre milliards et demi en actions pour Applied Compute... une équipe née il y a dix-huit mois.",
     {"shots": [clip("9"), dict(clip("9b"), at_word=w(t, "Applied"))]},
     [{"type": "stock", "key": "PANW", "name": "Palo Alto Networks", "sub": "Rachat d'Applied Compute · 4,5 Md$ en actions", "y": 560, "at_word": w(t, "Palo")},
      {"type": "source", "text": "Communiqué Palo Alto Networks via " + HC}])

t = "Nvidia, elle, négocie le rachat d'Inception pour plus de 500 millions. En pleine chute de son action."
beat(t, "Nvidia, elle, négocie le rachat d'Inception pour plus de cinq cents millions... En pleine chute de son action.",
     clip("10"),
     [{"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "125,53 $ le 20 nov. · sur la semaine", "pct": "−22,9 %", "up": False, "y": 560, "at_word": w(t, "Nvidia")},
      {"type": "source", "text": "The Decoder via " + HC + " · " + MC}])

t = "Même Anthropic, introduite à 83 dollars, a perdu 8,5 % dès sa deuxième séance."
beat(t, "Même Anthropic, introduite à quatre-vingt-trois dollars, a perdu plus de huit pour cent dès sa deuxième séance.",
     scr("11"),
     [{"type": "stock", "key": "ANT", "name": "Anthropic", "sub": "88,91 $ le 20 nov. · introduite à 83 $", "pct": "−8,5 %", "up": False, "y": 520, "at_word": w(t, "Anthropic")},
      {"type": "source", "text": BI + " · " + TP}])

t = "Le twist : sur CNBC, Ed Zitron prévient que l'argent qui tourne en rond entre Nvidia, Oracle et les labos d'I.A. pourrait gonfler la demande."
beat(t, "Le twist : sur C.N.B.C., Ed Zitron prévient que l'argent qui tourne en rond entre Nvidia, Oracle et les labos d'I.A.... pourrait gonfler la demande.",
     {"shots": [clip("12"), dict(clip("12b"), at_word=w(t, "tourne"))]},
     [{"type": "news", "at_word": w(t, "CNBC"), "left": "CNBC · ED ZITRON", "right": "20 NOV.", "tag": "MISE EN GARDE",
       "headline": "Le financement circulaire entre Nvidia, Oracle, les géants du cloud et les labos d'I.A. pourrait gonfler la demande",
       "highlight": "financement circulaire", "sub": HC}])

t = "Prochain test : mercredi, l'inflation PCE et la croissance américaine. Puis la Fed, le 9 décembre."
beat(t, "Prochain test : mercredi, l'inflation P.C.E. et la croissance américaine... Puis la Fed, le neuf décembre.",
     {"shots": [clip("13"), dict(clip("13b"), at_word=w(t, "Fed"))]},
     [{"type": "news", "at_word": w(t, "mercredi"), "left": "AGENDA · ÉTATS-UNIS", "right": "25 NOV.", "tag": "À SURVEILLER",
       "headline": "Mercredi 25 novembre : inflation PCE d'octobre et PIB du 3e trimestre. Mercredi 9 décembre : décision de la Fed",
       "highlight": "9 décembre", "sub": TP}])

t = "Alors, bulle qui se dégonfle, ou simple trou d'air ? Dis-le en commentaire."
beat(t, "Alors... bulle qui se dégonfle, ou simple trou d'air ? Dis-le en commentaire.",
     clip("14"),
     [{"type": "bigtitle", "lines": ["BULLE OU", "TROU D'AIR ?"], "at_word": 2}])

t = "Ces chiffres, mes abonnés les ont lus avant tout le monde. Mon Telegram gratuit : actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. Plus de 22 000 personnes. Il ne manque que toi. Lien en bio."
say = "Ces chiffres, mes abonnés les ont lus avant tout le monde. Mon Telegram gratuit : actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. Plus de vingt-deux mille personnes... Il ne manque que toi. Lien en bio."
beat(t, say, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Databricks, Oracle, Nvidia : l'argent de l'I.A. décrypté", "imgs": ["tg_3435c02c_top.jpg", "tg_3435c02c.jpg"],
       "subs": 22760, "subs_at_word": w(t, "22"), "bio_at_word": w(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
     cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})

B = [b for i, b in enumerate(B) if i not in (2, 11)]  # coupés au montage (durée)
spec = {"id": EP, "date_label": "22 novembre 2026", "brand": "Invest Family Fr", "hook_type": "logowall",
        "hook_formula": "personne n'en parle",
        "cta_angle": "Ces chiffres, mes abonnés les ont lus avant tout le monde. Il ne manque que toi.",
        "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://hervecuviliez.substack.com/p/market-news-saturday-21-november",
                    "https://tedpillows.substack.com/p/crypto-and-finance-market-report-13a",
                    "https://www.marketcalls.in/futures-and-options/weekly-market-roundup-21-november-2026.html",
                    "https://emergent.sh/news/oracle-raises-20b-debt-equity-fund-ai",
                    "https://www.browninsights.com/p/the-weekender-november-21-2026"],
        "beats": B}
json.dump(spec, open(f'/home/claude/kit/episodes/{EP}/spec.json', 'w'), ensure_ascii=False, indent=1)
txt = "\n".join(b["say"] for b in B)
open(f'/home/claude/kit/episodes/{EP}/voice_text.txt', 'w').write(txt)
print(len(B), "beats", len(txt.split()), "mots")
