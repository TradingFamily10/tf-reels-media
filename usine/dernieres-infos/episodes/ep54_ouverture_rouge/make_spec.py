import json, sys, os
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep54_ouverture_rouge'
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
UP = "Upstox · 25 nov. 2026, 16 h 31 IST"
PQ = "PiQ Markets · 25 nov. 2026, 11 h 08 (Paris)"
OX = "Oxford Economics · nowcast PCE · 16 nov. 2026"

t = "Dans 35 minutes, Wall Street ouvre. Et le Nasdaq chute déjà de plus de 2 %."
beat(t, "Dans trente-cinq minutes, Wall Street ouvre... Et le Nasdaq chute déjà de plus de deux pour cent.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "Nasdaq"))]},
     [{"type": "date", "text": "Mercredi 25 novembre 2026 · avant Wall Street", "until_beat": 0},
      {"type": "breaking", "label": "DERNIÈRES INFOS", "lines": ["NASDAQ −2,5 %", "AVANT L'OUVERTURE", "WALL STREET 15 H 30"]},
      {"type": "stock", "key": "NDAQ", "name": "Nasdaq 100", "sub": "Contrats à terme · avant-Bourse", "pct": "−2,5 %", "up": False, "size": "big", "y": 1180, "at_word": w(t, "Nasdaq")}])

t = "Et ce n'est pas le pire : hier soir encore, le Dow Jones fêtait un record à 50 000 points."
beat(t, "Et ce n'est pas le pire... hier soir encore, le Dow Jones fêtait un record à cinquante mille points.", clip("1"),
     [{"type": "bigtitle", "lines": ["HIER, UN RECORD", "AUJOURD'HUI, LA CHUTE"], "at_word": w(t, "Dow")}])

t = "Ce matin, les contrats sur le Dow reculent de 0,82 %, ceux du S&P 500 de 1,5 %."
beat(t, "Ce matin, les contrats sur le Dow reculent de près d'un pour cent... ceux du S. and P. cinq cents, d'un pour cent et demi.", scr("2"),
     [{"type": "screen_duo", "a": {"kicker": "DOW JONES · CONTRATS", "value_to": -0.82, "decimals": 2, "prefix": "", "suffix": " %", "color": "red", "desc": "≈ 49 651 pts · mardi 50 019", "logo": "NDAQ"},
       "b_at_word": w(t, "S&P"), "b": {"kicker": "S&P 500 · CONTRATS", "value_to": -1.5, "decimals": 1, "prefix": "", "suffix": " %", "color": "red", "desc": "≈ 7 109 pts · mardi 7 201", "logo": "NDAQ"}},
      {"type": "source", "text": UP}])

t = "Nvidia perd 4,9 % avant-Bourse. Micron, AMD et Marvell, plus de 5 %."
beat(t, "Nvidia perd près de cinq pour cent avant-Bourse... Micron, A.M.D. et Marvell, plus de cinq pour cent.",
     {"shots": [clip("3"), dict(clip("3b"), at_word=w(t, "Micron"))]},
     [{"type": "tickers", "title": "AVANT-BOURSE · MER. 25 NOV.", "rows": [
        {"key": "NVDA", "name": "Nvidia", "pct": "−4,9 %", "at_word": 0},
        {"key": "MU", "name": "Micron", "pct": "> −5 %", "at_word": w(t, "Micron")},
        {"key": "AMD", "name": "AMD", "pct": "> −5 %", "at_word": w(t, "AMD")},
        {"key": "MRVL", "name": "Marvell", "pct": "> −5 %", "at_word": w(t, "Marvell")}]},
      {"type": "source", "text": PQ}])

t = "Cette nuit, l'Asie a déjà craqué : le Kospi coréen termine en baisse de 6,16 %."
beat(t, "Cette nuit, l'Asie a déjà craqué : le Kospi coréen termine en baisse de plus de six pour cent.", scr("4"),
     [{"type": "screen_counter", "kicker": "KOSPI · SÉOUL", "value_from": 0, "value_to": -6.16, "decimals": 2, "prefix": "", "suffix": " %", "color": "red",
       "pill": "MERCREDI 25 NOV. · CLÔTURE", "desc": "Nikkei −2,78 % · Hang Seng −1,14 % · " + UP}])

t = "Alors, qui appuie sur le bouton rouge ?"
beat(t, "Alors... qui appuie sur le bouton rouge ?", clip("5"),
     [{"type": "bigtitle", "lines": ["QUI APPUIE SUR", "LE BOUTON ROUGE ?"], "at_word": 1}])

t = "Cette séance, je la suis minute par minute sur mon Telegram. Lien en bio."
beat(t, "Cette séance, je la suis minute par minute sur mon Telegram. Lien en bio.", clip("6"),
     [{"type": "phone", "mode": "mini", "img": "tg_1eaa56f0.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "Premier suspect : Washington. Les États-Unis préparent de nouveaux droits de douane contre 16 grands partenaires."
beat(t, "Premier suspect : Washington. Les États-Unis préparent de nouveaux droits de douane... contre seize grands partenaires.",
     {"shots": [clip("7"), dict(clip("7b"), at_word=w(t, "droits"))]},
     [{"type": "news", "at_word": w(t, "États-Unis"), "left": "ÉTATS-UNIS · COMMERCE", "right": "25 NOV.", "tag": "DROITS DE DOUANE",
       "headline": "L'administration Trump pourrait dévoiler des droits de douane sur les importations de 16 grands partenaires commerciaux",
       "highlight": "16 grands partenaires", "sub": PQ}])

t = "Deuxième suspect : la Fed. Une hausse de taux en décembre est jouée à 97 %."
beat(t, "Deuxième suspect : la Fed. Une hausse de taux en décembre est jouée à quatre-vingt-dix-sept pour cent.", scr("8"),
     [{"type": "screen_counter", "kicker": "FED · HAUSSE EN DÉCEMBRE", "value_from": 0, "value_to": 97, "decimals": 0, "prefix": "", "suffix": " %", "color": "white",
       "pill": "PROBABILITÉ · CONTRATS FED FUNDS", "desc": PQ}])

t = "Une deuxième hausse en janvier est vue à 63 %, et le taux américain à 10 ans approche les 5 %."
beat(t, "Une deuxième hausse en janvier est vue à soixante-trois pour cent... et le taux américain à dix ans approche les cinq pour cent.", scr("9"),
     [{"type": "screen_duo", "a": {"kicker": "FED · HAUSSE EN JANVIER", "value_to": 63, "decimals": 0, "prefix": "", "suffix": " %", "color": "white", "desc": "Probabilité · " + PQ, "logo": "NDAQ"},
       "b_at_word": w(t, "taux"), "b": {"kicker": "TAUX US À 10 ANS", "value_to": 4.85, "decimals": 2, "prefix": "", "suffix": " %", "color": "red", "desc": "≈ 11 h 24 (Paris) · 4,90 % la veille · Upstox", "logo": "NDAQ"}}])

t = "Le juge de paix, c'est l'inflation PCE, la mesure préférée de la Fed, publiée à 14 h 30."
beat(t, "Le juge de paix, c'est l'inflation P.C.E.... la mesure préférée de la Fed, publiée à quatorze heures trente.", clip("10"),
     [{"type": "news", "at_word": w(t, "PCE"), "left": "AGENDA · ÉTATS-UNIS", "right": "MER. 25 NOV.", "tag": "INFLATION",
       "headline": "Inflation PCE d'octobre et PIB du 3e trimestre publiés à 14 h 30, juste avant l'ouverture", "highlight": "14 h 30", "sub": PQ}])

t = "Oxford Economics l'attendait en accélération : 3,8 % sur un an, contre 3,6 % en septembre."
beat(t, "Oxford Economics l'attendait en accélération... près de quatre pour cent sur un an.", scr("11"),
     [{"type": "screen_duo", "a": {"kicker": "INFLATION PCE · SEPTEMBRE", "value_to": 3.6, "decimals": 1, "prefix": "", "suffix": " %", "color": "white", "desc": "Sur un an", "logo": "NDAQ"},
       "b_at_word": w(t, "accélération"), "b": {"kicker": "OCTOBRE · PRÉVISION", "value_to": 3.8, "decimals": 1, "prefix": "", "suffix": " %", "color": "red", "desc": OX, "logo": "NDAQ"}}])

t = "Et le calendrier n'aide pas : demain, Wall Street sera fermée pour Thanksgiving."
beat(t, "Et le calendrier n'aide pas... demain, Wall Street sera fermée pour Thanksgiving.",
     {"shots": [clip("12"), dict(clip("12b"), at_word=w(t, "Wall"))]},
     [{"type": "bigtitle", "lines": ["JEUDI 26 NOV.", "MARCHÉS US FERMÉS"], "at_word": w(t, "demain")}])

t = "Prochain rendez-vous : la dernière réunion de la Fed de l'année, en décembre."
beat(t, "Prochain rendez-vous : la dernière réunion de la Fed de l'année, en décembre.", clip("13"),
     [{"type": "news", "at_word": 1, "left": "FED · AGENDA", "right": "DÉC. 2026", "tag": "À SURVEILLER",
       "headline": "Dernière réunion de l'année du FOMC en décembre : une hausse de 25 points de base est attendue", "highlight": "hausse de 25 points de base", "sub": OX}])

t = "Alors, simple coup de froid… ou début d'une vraie correction ? Dis-le en commentaire."
beat(t, "Alors... simple coup de froid... ou début d'une vraie correction ? Dis-le en commentaire.", clip("14"),
     [{"type": "bigtitle", "lines": ["COUP DE FROID", "OU CORRECTION ?"], "at_word": 1}])

t = ("La prochaine secousse, tu veux l'apprendre ici ou la voir venir ? Sur mon Telegram gratuit : l'actu géopolitique et financière décortiquée, "
     "mes analyses d'actions détaillées et mes opportunités en temps réel. Plus de 22 000 personnes y sont déjà. Entre dans le canal, lien en bio.")
s = ("La prochaine secousse... tu veux l'apprendre ici, ou la voir venir ? Sur mon Telegram gratuit : l'actu géopolitique et financière décortiquée, "
     "mes analyses d'actions détaillées et mes opportunités en temps réel. Plus de vingt-deux mille personnes y sont déjà... Entre dans le canal, lien en bio.")
beat(t, s, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Nasdaq −2,5 % avant l'ouverture : le point en direct", "imgs": ["tg_38e4f34b.jpg", "tg_3435c02c.jpg", "tg_4b2fa9a8.jpg"], "subs": 22760,
       "subs_at_word": w(t, "personnes"), "bio_at_word": w(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
     cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "25 novembre 2026", "brand": "Invest Family Fr", "hook_type": "breaking", "hook_formula": "compte à rebours",
        "cta_angle": "La prochaine secousse, tu veux l'apprendre ici ou la voir venir ?", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://upstox.com/news/market-news/us-stocks/dow-jones-s-and-p-500-nasdaq-futures-hint-gap-down-open-ahead-of-us-pce-inflation-data-release-stocks-to-watch/article-203963/",
                    "https://piqmarkets.com/story/nasdaq-futures-fall-over-2-on-reports-of-new-us-tariff-plans",
                    "https://www.oxfordeconomics.com/resource/us-pce-nowcast-broadening-pressures-lock-in-december-rate-hike/"],
        "beats": B}
json.dump(spec, open(f'{D}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'{D}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), "beats", sum(len(b["say"].split()) for b in B), "mots")
