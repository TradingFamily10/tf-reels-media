import json, sys, os
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep63_bitcoin_peur'
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
    d = {"clip": f"b{n}.mp4", "ss": SS.get(n, 1) if ss is None else ss, "cx": CX.get(n, 0.5) if cx is None else cx}
    if n == "3": d["inset"] = 0.075
    return d
def scr(n): return {"screen": True, "under": clip(n)}
B = []
def beat(text, say, bg, overlays, **kw):
    b = {"text": text, "say": say, "bg": bg, "overlays": overlays}; b.update(kw); B.append(b); return b
CT = "CryptoTicker (CoinGecko, SoSoValue) · 28 nov. 2026"
BG = "BigGo Finance · 28 nov. 2026"
JA = "JournalArta · 28 nov. 2026"
FQ = "Forex Québec · 28 nov. 2026"

# 0 — accroche (chip, formule « contre-intuitif »)
t = "Wall Street vient de signer sa meilleure semaine depuis avril 2025. Et pourtant, le bitcoin passe sous 60 000 $."
beat(t, "Wall Street vient de signer sa meilleure semaine depuis avril deux mille vingt-cinq... Et pourtant, le bitcoin passe sous les soixante mille dollars.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "pourtant"))]},
     [{"type": "date", "text": "Samedi 28 novembre 2026 · crypto & Wall Street", "until_beat": 1},
      {"type": "bigtitle", "lines": ["BITCOIN", "SOUS 60 000 $"], "at_word": w(t, "pourtant")},
      {"type": "stock", "key": "BTC", "name": "Bitcoin", "sub": "≈ 59 600 $ · samedi matin", "pct": "−3,5 % en 24 h",
       "up": False, "size": "big", "y": 560, "at_word": w(t, "bitcoin")}])

t = "Et ce n'est pas le pire : l'indice de la peur crypto est tombé à 10 sur 100."
beat(t, "Et ce n'est pas le pire... l'indice de la peur crypto est tombé à dix sur cent.",
     scr("1"),
     [{"type": "screen_gauge", "kicker": "INDICE FEAR & GREED · CRYPTO", "pill": "10 / 100 · PEUR EXTRÊME",
       "desc": "Samedi 28 nov. · " + BG + " · " + CT}])

t = "Côté actions, c'est la fête : le S&P 500 a pris 5,6 % en une semaine."
beat(t, "Côté actions, c'est la fête... le S&P cinq cents a pris plus de cinq pour cent en une semaine.",
     scr("2"),
     [{"type": "screen_counter", "kicker": "S&P 500 · SEMAINE AU 27 NOV.", "value_from": 0, "value_to": 5.6, "decimals": 1,
       "prefix": "+", "suffix": " %", "color": "green", "pill": "CLÔTURE 7 297 PTS", "desc": "Meilleure semaine depuis avril 2025 · " + BG}])

t = "Le Nasdaq bondit de 6,7 %, porté par les puces : Marvell, TSMC."
beat(t, "Le Nasdaq bondit de près de sept pour cent, porté par les puces... Marvell, T.S.M.C.",
     clip("3"),
     [{"type": "tickers", "title": "VENDREDI 27 NOV. · PUCES", "rows": [
        {"key": "MRVL", "name": "Marvell", "pct": "+7,34 %", "up": True, "at_word": w(t, "Marvell")},
        {"key": "TSM", "name": "TSMC", "pct": "+3,21 %", "up": True, "at_word": w(t, "TSMC")}]},
      {"type": "source", "text": "Nasdaq +6,7 % sur la semaine · " + BG + " · " + JA}])

t = "Mais vendredi, à l'ouverture de Wall Street, le bitcoin a perdu 2 300 $ en 35 minutes."
beat(t, "Mais vendredi, à l'ouverture de Wall Street, le bitcoin a perdu deux mille trois cents dollars... en trente-cinq minutes.",
     scr("4"),
     [{"type": "screen_duo",
       "a": {"kicker": "BITCOIN · 15 H 30 (PARIS)", "value_to": 61359, "decimals": 0, "prefix": "", "suffix": " $", "color": "gold",
             "desc": "Ouverture de Wall Street · ven. 27 nov."},
       "b_at_word": w(t, "35"),
       "b": {"kicker": "BITCOIN · 16 H 05", "value_to": 59033, "decimals": 0, "prefix": "", "suffix": " $", "color": "red",
             "desc": "−3,8 % en 35 min · " + CT}}])

t = "Résultat : 228 millions de dollars de positions liquidées en une heure."
beat(t, "Résultat... deux cent vingt-huit millions de dollars de positions liquidées en une heure.",
     scr("5"),
     [{"type": "screen_counter", "kicker": "LIQUIDATIONS · 1RE HEURE", "value_from": 0, "value_to": 228, "decimals": 0,
       "prefix": "", "suffix": " M$", "color": "red", "pill": "407 M$ SUR 24 H", "desc": "Coinglass via " + CT}])

t = "Alors, qui vend ?"
beat(t, "Alors... qui vend ?",
     clip("6"),
     [{"type": "bigtitle", "lines": ["ALORS,", "QUI VEND ?"], "at_word": 1}])

t = "Lundi, la suite, je la suis en direct sur mon Telegram. Lien en bio."
beat(t, t, clip("7"),
     [{"type": "phone", "mode": "mini", "img": "tg_3435c02c_top.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "Les ETF bitcoin américains. Huit jours de retraits d'affilée."
beat(t, "Les E.T.F. bitcoin américains... Huit jours de retraits d'affilée.",
     clip("8"),
     [{"type": "news", "at_word": w(t, "Huit"), "left": "ETF BITCOIN SPOT · US", "right": "VEN. 27 NOV.", "tag": "FLUX",
       "headline": "ETF bitcoin : huitième journée consécutive de sorties nettes",
       "highlight": "huitième journée", "sub": "SoSoValue via " + CT}])

t = "Vendredi encore, 389 millions de dollars sont sortis. Dont 327 millions du seul fonds de BlackRock."
beat(t, "Vendredi encore, trois cent quatre-vingt-neuf millions de dollars sont sortis... Dont trois cent vingt-sept millions du seul fonds de BlackRock.",
     scr("9"),
     [{"type": "screen_counter", "kicker": "SORTIES DES ETF · VEN. 27 NOV.", "value_from": 0, "value_to": 389, "decimals": 0,
       "prefix": "−", "suffix": " M$", "color": "red", "pill": "8E JOUR DE RETRAITS", "desc": CT},
      {"type": "stock", "key": "BLK", "name": "BlackRock · IBIT", "sub": "iShares Bitcoin Trust", "pct": "−327 M$",
       "up": False, "y": 1500, "at_word": w(t, "BlackRock")}])

t = "Sur le seul mois de novembre, plus de 5 milliards de dollars ont quitté ces fonds. Un record."
beat(t, "Sur le seul mois de novembre, plus de cinq milliards de dollars ont quitté ces fonds... Un record.",
     scr("10"),
     [{"type": "screen_counter", "kicker": "SORTIES DES ETF · NOVEMBRE", "value_from": 0, "value_to": 5.39, "decimals": 2,
       "prefix": "−", "suffix": " MDS $", "color": "red", "pill": "RECORD : 4,51 MDS $ EN JUIN", "desc": "Crypto Briefing via " + CT}])

t = "Pendant ce temps, les capitaux filent vers les métaux : l'or a pris 2,9 % vendredi, l'argent 7,8 %."
beat(t, "Pendant ce temps, les capitaux filent vers les métaux... l'or a pris près de trois pour cent vendredi, l'argent, près de huit.",
     scr("11"),
     [{"type": "screen_duo",
       "a": {"kicker": "OR · VEN. 27 NOV.", "value_to": 2.9, "decimals": 1, "prefix": "+", "suffix": " %", "color": "green",
             "desc": "3 668,50 $ l'once (contrat à terme)"},
       "b_at_word": w(t, "7,8"),
       "b": {"kicker": "ARGENT · VEN. 27 NOV.", "value_to": 7.8, "decimals": 1, "prefix": "+", "suffix": " %", "color": "green",
             "desc": "43,70 $ l'once · " + JA}}])

t = "Et le taux américain à 10 ans remonte à 4,94 %. De quoi faire de l'ombre au bitcoin."
beat(t, "Et le taux américain à dix ans remonte à près de cinq pour cent... De quoi faire de l'ombre au bitcoin.",
     clip("12"),
     [{"type": "bigtitle", "lines": ["TAUX US 10 ANS", "4,94 %"], "at_word": w(t, "taux")},
      {"type": "source", "text": "Contre 4,85 % la veille · " + JA}])

t = "Prochain rendez-vous : vendredi 4 décembre, le rapport sur l'emploi américain."
beat(t, "Prochain rendez-vous... vendredi quatre décembre, le rapport sur l'emploi américain.",
     clip("13"),
     [{"type": "news", "at_word": w(t, "vendredi"), "left": "AGENDA · ÉTATS-UNIS", "right": "VEN. 4 DÉC. · 14 H 30", "tag": "EMPLOI",
       "headline": "Rapport sur l'emploi de novembre : le chiffre qui peut tout faire bouger",
       "highlight": "emploi de novembre", "sub": FQ}])

t = "Et mardi, on saura si les ETF enchaînent un neuvième jour de retraits."
beat(t, "Et mardi, on saura si les E.T.F. enchaînent un neuvième jour de retraits.",
     clip("14"),
     [{"type": "stock", "key": "COIN", "name": "Crypto · ETF spot", "sub": "Séance US lundi 15 h 30 (Paris)", "pct": "9E JOUR ?",
       "up": False, "y": 560, "at_word": w(t, "neuvième")},
      {"type": "source", "text": CT}])

t = "Et toi : simple trou d'air, ou début d'un hiver crypto ? Dis-le en commentaire."
beat(t, "Et toi... simple trou d'air, ou début d'un hiver crypto ? Dis-le en commentaire.",
     clip("15"),
     [{"type": "bigtitle", "lines": ["TROU D'AIR", "OU HIVER CRYPTO ?"], "at_word": 2}])

t = ("Ce que je viens de te montrer, mes abonnés l'ont lu avant tout le monde. Sur mon Telegram gratuit : "
     "l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées et mes opportunités en temps réel. "
     "Plus de 22 000 personnes y sont déjà. Le lien est en bio.")
say = ("Ce que je viens de te montrer... mes abonnés l'ont lu avant tout le monde. Sur mon Telegram gratuit : "
       "l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées et mes opportunités en temps réel. "
       "Plus de vingt-deux mille personnes y sont déjà... Le lien est en bio.")
beat(t, say, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Bitcoin sous 60 000 $ : qui vend, et pourquoi", "imgs": ["tg_38e4f34b.jpg", "tg_4b2fa9a8.jpg", "tg_1eaa56f0.jpg"],
       "subs": 22760, "subs_at_word": w(t, "22"), "bio_at_word": w(t, "bio"), "button": "ACCÈS GRATUIT"}],
     cta="long", endcard={"duration": 1.8, "button": "ACCÈS GRATUIT", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "28 novembre 2026", "brand": "Invest Family Fr", "hook_type": "chip",
        "hook_formula": "contre-intuitif",
        "cta_angle": "Ce que je viens de te montrer, mes abonnés l'ont lu avant tout le monde",
        "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad",
                  "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://cryptoticker.io/en/bitcoin-price-59600-eighth-day-etf-outflows-wall-street/",
                    "https://finance.biggo.com/news/9734619a-1d11-4592-8cd3-f8faebdcbb04",
                    "https://journalarta.com/en/2026/11/28/nasdaq-jumps-2-31-and-sp-500-gains-1-61-as-chipmakers-lead-black-friday-rally/",
                    "https://forex.quebec/revue-hebdomadaire-24-28-novembre-2026/",
                    "https://www.riotimesonline.com/global-economy-briefing-november-28-2026/"],
        "broll_credits": "broll/credits.json"}
DROP = set(int(x) for x in os.environ.get("DROP", "").split(",") if x)
spec["beats"] = [b for i, b in enumerate(B) if i not in DROP]
json.dump(spec, open(f'{D}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'{D}/voice_text.txt', 'w').write("\n".join(b["say"] for b in spec["beats"]))
print(len(spec["beats"]), "beats,", sum(len(b["say"].split()) for b in spec["beats"]), "mots")
