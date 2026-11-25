import json, sys, os
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep52_dow_50000'
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
YH = "Yahoo Finance (Motley Fool) · 24 nov. 2026"
WS = "24/7 Wall St. · 24 nov. 2026, clôture"
SX = "Saxo · Asia Market Quick Take · 25 nov. 2026"
IL = "investingLive · 25 nov. 2026"
TK = "TradingKey · 25 nov. 2026"

t = "50 000 points. Pour la première fois de son histoire, le Dow Jones clôture au-dessus."
beat(t, "Cinquante mille points... Pour la première fois de son histoire, le Dow Jones clôture au-dessus.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "Dow"))]},
     [{"type": "date", "text": "Mardi 24 novembre 2026 · Wall Street", "until_beat": 1},
      {"type": "hook_bignum", "value_to": 50000, "prefix": "", "suffix": "", "unit": "DOW JONES · CLÔTURE", "label": "une première historique",
       "logos": ["SNY", "NVDA", "HPE", "DELL", "ADI", "CRWV"], "reveal_at_word": w(t, "première"), "count_dur": 1.2}])

t = "Tout le monde regarde ce record. Le vrai danger est ailleurs."
beat(t, "Tout le monde regarde ce record... Le vrai danger est ailleurs.", clip("1"),
     [{"type": "bigtitle", "lines": ["LE VRAI DANGER", "EST AILLEURS"], "at_word": w(t, "vrai")}])

t = "Le même soir, le Nasdaq recule de 1,48 %."
beat(t, "Le même soir, le Nasdaq recule de près d'un pour cent et demi.",
     scr("2"),
     [{"type": "screen_duo", "a": {"kicker": "DOW JONES · CLÔTURE", "value_to": 0.85, "decimals": 2, "prefix": "+", "suffix": " %", "color": "green", "desc": "50 019 points", "logo": "NDAQ"},
       "b_at_word": w(t, "Nasdaq"), "b": {"kicker": "NASDAQ · CLÔTURE", "value_to": -1.48, "decimals": 2, "prefix": "", "suffix": " %", "color": "red", "desc": "23 734 points · S&P 500 −0,50 %", "logo": "NDAQ"}},
      {"type": "source", "text": YH}])

t = "Nvidia lâche 5,86 %, au lendemain d'un bond historique de 31 %."
beat(t, "Nvidia lâche près de six pour cent... au lendemain d'un bond historique de trente et un pour cent.",
     {"shots": [clip("3"), dict(clip("3b"), at_word=w(t, "lendemain"))]},
     [{"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "NVDA · Nasdaq · mardi 24 nov.", "pct": "−5,86 %", "up": False, "size": "big", "y": 560, "at_word": 0},
      {"type": "source", "text": TK + " · +31,48 % lundi (Motley Fool)"}])

t = "Et les puces trinquent : l'indice des semi-conducteurs perd près de 8 %."
beat(t, "Et les puces trinquent : l'indice des semi-conducteurs perd près de huit pour cent.",
     scr("4"),
     [{"type": "screen_logos", "kicker": "SEMI-CONDUCTEURS · SOX", "value_from": 0, "value_to": -8, "decimals": 0, "prefix": "≈ ", "suffix": " %", "color": "red",
       "pill": "MARDI 24 NOV. · CLÔTURE", "keys": ["NVDA", "MU", "AMD"], "desc": "Micron ≈ −11 % · " + SX}])

t = "Alors, où est passé tout cet argent ?"
beat(t, "Alors... où est passé tout cet argent ?", clip("5"),
     [{"type": "bigtitle", "lines": ["OÙ EST PASSÉ", "TOUT CET ARGENT ?"], "at_word": 1}])

t = "Cette grande rotation, je la décortique en direct sur mon Telegram. Lien en bio."
beat(t, "Cette grande rotation, je la décortique en direct sur mon Telegram. Lien en bio.", clip("6"),
     [{"type": "phone", "mode": "mini", "img": "tg_38e4f34b.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "Réponse : dans la santé. Le secteur gagne 3 %, pendant que la tech perd 3,3 %."
beat(t, "Réponse : dans la santé. Le secteur gagne trois pour cent... pendant que la tech perd plus de trois pour cent.",
     scr("7"),
     [{"type": "screen_duo", "a": {"kicker": "SANTÉ · S&P 500", "value_to": 3.0, "decimals": 1, "prefix": "+", "suffix": " %", "color": "green", "desc": "Meilleur secteur de la séance", "logo": "SNY"},
       "b_at_word": w(t, "tech"), "b": {"kicker": "TECHNOLOGIE · S&P 500", "value_to": -3.3, "decimals": 1, "prefix": "", "suffix": " %", "color": "red", "desc": "Pire secteur de la séance", "logo": "NVDA"}},
      {"type": "source", "text": WS}])

t = "Sanofi bondit de près de 11 %, portée par le rachat d'Insmed."
beat(t, "Sanofi bondit de près de onze pour cent... portée par le rachat d'Insmed.",
     {"shots": [clip("8"), dict(clip("8b"), at_word=w(t, "rachat"))]},
     [{"type": "stock", "key": "SNY", "name": "Sanofi", "sub": "SNY · Nasdaq · mardi 24 nov.", "pct": "+10,9 %", "up": True, "size": "big", "y": 560, "at_word": 0},
      {"type": "source", "text": WS}])

t = "Mais côté I.A., c'est la purge : Analog Devices, HPE et Dell perdent entre 12 et 17 %."
beat(t, "Mais côté I.A., c'est la purge : Analog Devices, H.P.E. et Dell perdent entre douze et dix-sept pour cent.",
     {"shots": [clip("10")]},
     [{"type": "tickers", "title": "WALL STREET · MARDI 24 NOV.", "rows": [
        {"key": "ADI", "name": "Analog Dev.", "pct": "−17,3 %", "at_word": w(t, "Analog")},
        {"key": "HPE", "name": "HPE", "pct": "−17,1 %", "at_word": w(t, "HPE")},
        {"key": "DELL", "name": "Dell", "pct": "−12,0 %", "at_word": w(t, "Dell")}]},
      {"type": "source", "text": WS}])

t = "Et cette nuit, l'Asie prend le relais : le Kospi coréen chute de près de 6 %."
beat(t, "Et cette nuit, l'Asie prend le relais : le Kospi coréen chute de près de six pour cent.",
     scr("11"),
     [{"type": "screen_counter", "kicker": "KOSPI · SÉOUL", "value_from": 0, "value_to": -6, "decimals": 0, "prefix": "≈ ", "suffix": " %", "color": "red",
       "pill": "MERCREDI 25 NOV. · EN SÉANCE", "desc": "Vers 4 710 points · Nikkei −3 % · " + IL}])

t = "Samsung et SK hynix décrochent de plus de 6 %, SoftBank de près de 10 % à Tokyo."
beat(t, "Samsung et S.K. Hynix décrochent de plus de six pour cent... SoftBank, de près de dix pour cent à Tokyo.",
     {"shots": [clip("12"), dict(clip("12b"), at_word=w(t, "SoftBank"))]},
     [{"type": "tickers", "title": "ASIE · MERCREDI 25 NOV.", "rows": [
        {"key": "SSU", "name": "Samsung", "pct": "−6,60 %", "at_word": 0},
        {"key": "SKH", "name": "SK hynix", "pct": "−6,30 %", "at_word": w(t, "hynix")},
        {"key": "SFTBY", "name": "SoftBank", "pct": "−9,76 %", "at_word": w(t, "SoftBank")}]},
      {"type": "source", "text": TK + ", en séance"}])

t = "En cause : le retour des doutes sur l'I.A., et des dépenses financées à crédit."
beat(t, "En cause : le retour des doutes sur l'I.A.... et des dépenses financées à crédit.",
     {"shots": [clip("13"), dict(clip("13b"), at_word=w(t, "dépenses"))]},
     [{"type": "news", "at_word": 1, "left": "ASIE · MARCHÉS", "right": "25 NOV.", "tag": "DOUTES",
       "headline": "Les doutes sur l'IA reviennent, sur fond d'inquiétude autour des dépenses financées par la dette",
       "highlight": "financées par la dette", "sub": IL}])

t = "À surveiller aujourd'hui à 14 h 30 : l'inflation PCE et le PIB américain."
beat(t, "À surveiller aujourd'hui, à quatorze heures trente : l'inflation P.C.E. et le P.I.B. américain.",
     {"shots": [clip("14")]},
     [{"type": "news", "at_word": 2, "left": "AGENDA · ÉTATS-UNIS", "right": "MER. 25 NOV.", "tag": "À SURVEILLER",
       "headline": "Inflation PCE d'octobre et PIB du 3e trimestre à 14 h 30, marchés fermés jeudi pour Thanksgiving",
       "highlight": "14 h 30", "sub": IL}])

t = "Alors, record historique… ou arbre qui cache la forêt ? Dis-le en commentaire."
beat(t, "Alors... record historique... ou arbre qui cache la forêt ? Dis-le en commentaire.", clip("15"),
     [{"type": "bigtitle", "lines": ["RECORD OU", "TROMPE-L'ŒIL ?"], "at_word": 1}])

t = ("Pendant que tout le monde fête un record, sur mon Telegram gratuit on regarde ce qui se cache derrière : l'actu géopolitique et financière décortiquée, "
     "mes analyses d'actions détaillées et mes opportunités en temps réel. Plus de 22 000 personnes nous ont déjà rejoints. Rejoins la famille, lien en bio.")
s = ("Pendant que tout le monde fête un record... sur mon Telegram gratuit, on regarde ce qui se cache derrière : l'actu géopolitique et financière décortiquée, "
     "mes analyses d'actions détaillées et mes opportunités en temps réel. Plus de vingt-deux mille personnes nous ont déjà rejoints... Rejoins la famille, lien en bio.")
beat(t, s, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Dow à 50 000 : ce que le record ne dit pas", "imgs": ["tg_4b2fa9a8.jpg", "tg_38e4f34b.jpg", "tg_1eaa56f0.jpg"], "subs": 22760,
       "subs_at_word": w(t, "personnes"), "bio_at_word": w(t, "bio"), "button": "REJOINS LA FAMILLE"}],
     cta="long", endcard={"duration": 1.8, "button": "REJOINS LA FAMILLE", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "25 novembre 2026", "brand": "Invest Family Fr", "hook_type": "bignum", "hook_formula": "personne n'en parle",
        "cta_angle": "Pendant que tout le monde fête un record, sur mon Telegram on regarde ce qui se cache derrière", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://finance.yahoo.com/markets/stocks/articles/stock-market-today-nov-24-221148355.html",
                    "https://247wallst.com/cards/the-dow-closed-above-50-000-for-the-first-time-while-the-nas-gspc-market-bell-01m87nyn7mshvn15b2vdser41w",
                    "https://www.home.saxo/en-sg/content/articles/macro/asia-market-quick-take-25-november-2026-25112026",
                    "https://investinglive.com/stock-market-update/asian-stocks-slide-as-ai-doubts-return-kospi-down-nearly-6-and-nikkei-more-than-3/",
                    "https://www.tradingkey.com/analysis/stocks/more/262320970-japan-south-korea-stocks-kospi-nikkei-softbank-sk-hynix-samsung-kioxia-tradingkey"],
        "beats": B}
json.dump(spec, open(f'{D}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'{D}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), "beats", sum(len(b["say"].split()) for b in B), "mots")
