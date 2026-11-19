import json, sys
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep35_anthropic_ipo'
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
AP = "AP (PBS NewsHour) · 18 nov. 2026"
RT = "Reuters (Boursorama) · 19 nov. 2026"
RT2 = "Reuters (Boursorama) · 19 nov. 2026, 09:47"

t = "Dans quelques heures, la plus grosse entrée en Bourse de l'histoire démarre à Wall Street."
beat(t, "Dans quelques heures... la plus grosse entrée en Bourse de l'histoire démarre à Wall Street.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "plus"))]},
     [{"type": "date", "text": "Jeudi 19 novembre 2026 · Nasdaq", "until_beat": 0},
      {"type": "breaking", "label": "DERNIÈRES INFOS", "lines": ["81 MILLIARDS", "LA PLUS GROSSE", "IPO DE L'HISTOIRE"]},
      {"type": "stock", "key": "ANT", "name": "Anthropic", "sub": "ANT · Nasdaq · 1re cotation ce jeudi", "y": 560, "at_word": w(t, "Wall")}])

t = "81 milliards de dollars levés par Anthropic, le créateur de l'I.A. Claude."
beat(t, "Quatre-vingt-un milliards de dollars levés par Anthropic, le créateur de l'I.A. Claude.",
     {"screen": True, "under": clip("1")},
     [{"type": "screen_counter", "kicker": "ANTHROPIC · IPO", "value_from": 0, "value_to": 81, "decimals": 0,
       "prefix": "", "suffix": " Md$", "color": "gold", "pill": "980 MILLIONS D'ACTIONS", "desc": AP + " · " + RT}])

t = "Et ce n'est pas tout : le prix final, 83 dollars, dépasse la fourchette prévue."
beat(t, "Et ce n'est pas tout : le prix final, quatre-vingt-trois dollars... dépasse la fourchette prévue.",
     {"screen": True, "under": clip("2", cx=0.72)},
     [{"type": "screen_duo",
       "a": {"kicker": "FOURCHETTE PRÉVUE · HAUT", "value_to": 78, "decimals": 0, "prefix": "", "suffix": " $", "color": "gold", "desc": "Fourchette initiale : 70 – 78 $"},
       "b_at_word": w(t, "83"),
       "b": {"kicker": "PRIX FINAL PAR ACTION", "value_to": 83, "decimals": 0, "prefix": "", "suffix": " $", "color": "green", "desc": "AP · Reuters · 18-19 nov."}}])

t = "Résultat : une valorisation de 1 500 milliards de dollars."
beat(t, "Résultat : une valorisation de mille cinq cents milliards de dollars.",
     {"shots": [clip("3"), dict(clip("3b"), at_word=w(t, "milliards"))]},
     [{"type": "hook_bignum", "value_to": 1500, "prefix": "", "suffix": " Md$", "unit": "DE VALORISATION",
       "label": "Au prix de 83 $ par action · AP", "logos": ["ANT"], "reveal_at_word": w(t, "valorisation"), "count_dur": 1.0}])

t = "Le record de SpaceX, environ 75 milliards levés en juin, est déjà battu."
beat(t, "Le record de SpaceX, environ soixante-quinze milliards levés en juin... est déjà battu.",
     {"shots": [clip("4"), dict(clip("4b", ss=4, cx=0.22), at_word=w(t, "battu"))]},
     [{"type": "tickers", "title": "PLUS GROSSES IPO · MONTANT LEVÉ", "rows": [
         {"name": "SpaceX · juin 2026", "pct": "≈ 75 Md$", "at_word": w(t, "SpaceX"), "key": "SPCX", "up": True},
         {"name": "Anthropic · nov. 2026", "pct": "81 Md$", "at_word": w(t, "battu"), "key": "ANT", "up": True}]},
      {"type": "source", "text": AP}])

t = "Alors, pourquoi un tel appétit pour ces actions ?"
beat(t, "Alors... pourquoi un tel appétit pour ces actions ?", clip("5"),
     [{"type": "bigtitle", "lines": ["POURQUOI UN TEL", "APPÉTIT ?"], "at_word": w(t, "pourquoi")}])

t = "Cette cotation, je la suis en direct sur mon Telegram. Lien en bio."
beat(t, t, clip("6"),
     [{"type": "phone", "mode": "mini", "img": "tg_3435c02c_top.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "Parce que l'I.A. reste le grand pari de Wall Street, malgré le départ du patron de Nvidia."
beat(t, "Parce que l'I.A. reste le grand pari de Wall Street... malgré le départ du patron de Nvidia.",
     {"shots": [clip("7"), dict(clip("7b"), at_word=w(t, "malgré"))]},
     [{"type": "news", "at_word": 2, "left": "WALL STREET · I.A.", "right": "18 NOV.", "tag": "CITATION",
       "headline": "« Le prix montre une forte demande des investisseurs » — Dan Ives, Yorkville Ives & Co.",
       "highlight": "forte demande", "sub": AP, "until_word": w(t, "malgré")},
      {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "Incertitude sur la direction", "y": 1380, "at_word": w(t, "Nvidia")}])

t = "Mais dans son dossier, Anthropic a déjà 6,2 milliards de dollars de dettes."
beat(t, "Mais dans son dossier, Anthropic a déjà plus de six milliards de dollars de dettes.",
     {"screen": True, "under": clip("8")},
     [{"type": "screen_counter", "kicker": "DETTE DÉJÀ CONTRACTÉE", "value_from": 0, "value_to": 6.2, "decimals": 1,
       "prefix": "", "suffix": " Md$", "color": "red", "pill": "« SUBSTANTIELLE » SELON LE DOSSIER", "desc": AP}])

t = "Et elle s'engage à dépenser 900 milliards en puissance de calcul dans les prochaines années."
beat(t, "Et elle s'engage à dépenser neuf cents milliards en puissance de calcul dans les prochaines années.",
     {"screen": True, "under": clip("9")},
     [{"type": "screen_counter", "kicker": "ENGAGEMENTS CALCUL & INFRASTRUCTURES", "value_from": 0, "value_to": 900, "decimals": 0,
       "prefix": "", "suffix": " Md$", "color": "gold", "pill": "DANS LES PROCHAINES ANNÉES", "desc": AP}])

t = "Dont 70 milliards rien que sur les douze prochains mois."
beat(t, "Dont soixante-dix milliards... rien que sur les douze prochains mois.",
     {"shots": [clip("10", cx=0.6), dict(clip("10b"), at_word=w(t, "douze"))]},
     [{"type": "news", "at_word": 0, "left": "ANTHROPIC · DOSSIER D'IPO", "right": "18 NOV.", "tag": "CHIFFRE CLÉ",
       "headline": "70 milliards de dollars d'engagements sur les 12 prochains mois",
       "highlight": "70 milliards de dollars", "sub": AP}])

t = "Pendant ce temps, l'Europe respire : le Stoxx 600 rebondit après quatre séances dans le rouge."
beat(t, "Pendant ce temps, l'Europe respire : le Stoxx six cents rebondit après quatre séances dans le rouge.",
     {"screen": True, "under": clip("11")},
     [{"type": "screen_counter", "kicker": "STOXX 600 · JEU. 19 NOV. MATIN", "value_from": 0, "value_to": 0.3, "decimals": 2,
       "prefix": "+", "suffix": " %", "color": "green", "pill": "APRÈS 4 SÉANCES DE BAISSE", "desc": "Boursenews · 19 nov. 2026 · " + RT2}])

t = "La tech européenne mène la danse : ASML et Infineon gagnent environ 3 %. Soitec bondit de près de 16 %."
beat(t, "La tech européenne mène la danse : A.S.M.L. et Infineon gagnent environ trois pour cent. Soitec bondit de près de seize pour cent.",
     {"shots": [clip("12"), dict(clip("12b"), at_word=w(t, "Soitec"))]},
     [{"type": "tickers", "title": "TECH EUROPÉENNE · JEU. MATIN", "rows": [
         {"name": "ASML", "pct": "≈ +3 %", "at_word": w(t, "ASML"), "key": "ASML", "up": True},
         {"name": "Infineon", "pct": "≈ +3 %", "at_word": w(t, "Infineon"), "key": "IFX", "up": True},
         {"name": "Soitec", "pct": "+15,9 %", "at_word": w(t, "Soitec"), "key": "SOI", "up": True}]},
      {"type": "source", "text": RT2 + " · Soitec : objectif de croissance ≈ 40 %"}])

t = "Le vrai test, c'est cet après-midi : la première cotation sur le Nasdaq, sous le code ANT."
beat(t, "Le vrai test, c'est cet après-midi : la première cotation sur le Nasdaq... sous le code A.N.T.",
     clip("14"),
     [{"type": "tickers", "title": "À SURVEILLER CET APRÈS-MIDI", "rows": [
         {"name": "Anthropic · 1re cotation", "pct": "NASDAQ", "at_word": w(t, "première"), "key": "ANT", "up": True},
         {"name": "Prix d'introduction", "pct": "83 $", "at_word": w(t, "Nasdaq"), "up": True},
         {"name": "Nvidia · réaction", "pct": "À SUIVRE", "at_word": w(t, "code"), "key": "NVDA", "up": True}]},
      {"type": "source", "text": AP + " · " + RT}])

t = "Alors, bulle de l'I.A.… ou début d'une nouvelle ère pour la Bourse ? Dis-le en commentaire."
beat(t, "Alors... bulle de l'I.A.... ou début d'une nouvelle ère pour la Bourse ? Dis-le en commentaire.", clip("15"),
     [{"type": "bigtitle", "lines": ["BULLE DE L'I.A.", "OU NOUVELLE ÈRE ?"], "at_word": w(t, "bulle")}])

t = ("Ce que je viens de te montrer, mes abonnés l'ont lu avant tout le monde. Mon canal Telegram gratuit, plus de 22 000 personnes : "
     "l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées, les opportunités en temps réel. Lien en bio.")
say = t.replace("plus de 22 000", "plus de vingt-deux mille")
beat(t, say, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "IPO Anthropic : ce qu'il faut regarder", "imgs": ["tg_3435c02c_top.jpg", "tg_1eaa56f0.jpg"],
       "subs": 22760, "subs_at_word": w(t, "22"), "bio_at_word": w(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
     cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "19 novembre 2026", "brand": "Invest Family Fr",
        "hook_type": "breaking", "hook_formula": "compte à rebours",
        "cta_angle": "Ce que je viens de te montrer, mes abonnés l'ont lu avant tout le monde", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad",
                  "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.pbs.org/newshour/economy/anthropic-prices-its-ipo-at-83-per-share-valuing-the-ai-giant-at-1-5-trillion",
                    "https://www.boursorama.com/bourse/actualites/l-europe-tente-de-rebondir-avec-la-cotation-d-anthropic-acbd003719d0a72ace7d4f52dbccd501",
                    "https://www.boursorama.com/bourse/actualites/hausse-prudente-en-vue-en-europe-avant-l-ipo-d-anthropic-actualise-a337ca97967f579cd00357e9d532cbac",
                    "https://www.boursorama.com/bourse/actualites/les-valeurs-a-suivre-a-paris-et-en-europe-actualise-9088e4723d449758f908eee3a8f7e125",
                    "https://boursenews.ma/article/marches/marches-europeens-rebond-stoxx-50-600-19-novembre"],
        "beats": B}
json.dump(spec, open(f'/home/claude/kit/episodes/{EP}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'/home/claude/kit/episodes/{EP}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), sum(len(b["say"].split()) for b in B), "mots")
