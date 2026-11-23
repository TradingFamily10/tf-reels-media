import json, sys, os
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep48_wall_street_rebond'
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
YF = "Yahoo Finance · 23 nov. 2026"
BI = "Reuters via Beinsure · 23 nov. 2026"
FW = "Reuters via Finwire · 23 nov. 2026"
CC = "CoinCentral · 23 nov. 2026, 5h21 heure de New York"

t = "Dans 35 minutes, Wall Street rouvre. Et Nvidia bondit déjà de 8 % avant la cloche."
beat(t, "Dans trente-cinq minutes, Wall Street rouvre... Et Nvidia bondit déjà de huit pour cent, avant la cloche.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "Nvidia"))]},
     [{"type": "date", "text": "Lundi 23 novembre 2026 · Wall Street", "until_beat": 1},
      {"type": "hook_bignum", "value_to": 8, "prefix": "+", "suffix": " %", "unit": "NVIDIA · AVANT L'OUVERTURE",
       "label": "après une semaine noire", "logos": ["NVDA", "AMD", "GOOGL", "META", "MSFT", "AMZN"],
       "reveal_at_word": w(t, "Nvidia"), "count_dur": 1.0}])

t = "Et ce n'est pas tout : tout le Nasdaq 100 grimpe de 3,3 % avant l'ouverture."
beat(t, "Et ce n'est pas tout : tout le Nasdaq cent grimpe de plus de trois pour cent avant l'ouverture.",
     scr("1"),
     [{"type": "screen_counter", "kicker": "NASDAQ 100 · AVANT-BOURSE", "value_from": 0, "value_to": 3.3, "decimals": 1,
       "prefix": "+", "suffix": " %", "color": "green", "pill": "LUNDI · AVANT L'OUVERTURE",
       "desc": "S&P 500 +2,5 % · Dow Jones ≈ +1,9 % · " + FW}])

t = "Il faut dire que la semaine dernière, le Nasdaq a perdu 10 %. Sa pire semaine depuis mars 2020."
beat(t, "Il faut dire que la semaine dernière, le Nasdaq a perdu dix pour cent... Sa pire semaine depuis mars deux mille vingt.",
     scr("2"),
     [{"type": "screen_counter", "kicker": "NASDAQ · 16-20 NOV.", "value_from": 0, "value_to": -10, "decimals": 0,
       "prefix": "≈ ", "suffix": " %", "color": "red", "pill": "PIRE SEMAINE DEPUIS MARS 2020",
       "desc": BI}])

t = "Vendredi, les trois grands indices américains sont tous passés en correction."
beat(t, t, {"shots": [clip("3"), dict(clip("3b"), at_word=w(t, "correction"))]},
     [{"type": "tickers", "title": "WALL STREET · CLÔTURE DU VENDREDI 20 NOV.", "rows": [
        {"key": "NDAQ", "name": "Nasdaq · 22 618", "pct": "−5,3 %", "at_word": w(t, "trois")},
        {"name": "S&P 500 · 6 910", "pct": "−3,7 %", "at_word": w(t, "indices")},
        {"name": "Dow Jones · 48 147", "pct": "−1,9 %", "at_word": w(t, "tous")}]},
      {"type": "source", "text": BI}])

t = "Et Nvidia ? −14 % vendredi. Près de la moitié de sa valeur envolée depuis début octobre."
beat(t, "Et Nvidia ? Moins quatorze pour cent vendredi... Près de la moitié de sa valeur envolée depuis début octobre.",
     {"shots": [clip("4"), dict(clip("4b"), at_word=w(t, "moitié"))]},
     [{"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "NVDA · Nasdaq · vendredi 20 nov.", "pct": "−14 %", "up": False,
       "size": "big", "y": 560, "at_word": 1, "strike_at_word": w(t, "moitié")},
      {"type": "source", "text": BI}])

t = "Alors, qui revient sur le marché ce matin ?"
beat(t, "Alors... qui revient sur le marché ce matin ?", clip("5"),
     [{"type": "bigtitle", "lines": ["QUI REVIENT", "CE MATIN ?"], "at_word": 1}])

t = "Ce rebond, je le suis en direct sur mon Telegram. Lien en bio."
beat(t, t, clip("6"),
     [{"type": "phone", "mode": "mini", "img": "tg_3435c02c_top.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "Réponse : les chasseurs de rabais, après sept séances de baisse d'affilée sur le S&P 500, du jamais vu depuis le krach du Covid."
beat(t, "Réponse : les chasseurs de rabais... après sept séances de baisse d'affilée sur le S. and P. cinq cents, du jamais vu depuis le krach du Covid.",
     {"shots": [clip("7"), dict(clip("7b"), at_word=w(t, "sept"))]},
     [{"type": "news", "at_word": w(t, "sept"), "left": "WALL STREET · S&P 500", "right": "23 NOV.", "tag": "REBOND",
       "headline": "Après sept baisses d'affilée, la plus longue série depuis le krach de 2020, les acheteurs reviennent",
       "highlight": "sept baisses d'affilée", "sub": YF}])

t = "Derrière Nvidia, toute l'I.A. se redresse : AMD, Alphabet et Meta grimpent de 4 à 6 %."
beat(t, "Derrière Nvidia, toute l'I.A. se redresse : A.M.D., Alphabet et Meta grimpent de quatre à six pour cent.",
     {"shots": [clip("8")]},
     [{"type": "tickers", "title": "AVANT L'OUVERTURE · LUNDI 23 NOV.", "rows": [
        {"key": "AMD", "name": "AMD", "pct": "+5,77 %", "at_word": w(t, "AMD")},
        {"key": "GOOGL", "name": "Alphabet", "pct": "+4,98 %", "at_word": w(t, "Alphabet")},
        {"key": "META", "name": "Meta", "pct": "+4,36 %", "at_word": w(t, "Meta")}]},
      {"type": "source", "text": CC}])

t = "Même Anthropic, introduite en Bourse jeudi, reprend 3 % après sa chute de 8,5 % vendredi."
beat(t, "Même Anthropic, introduite en Bourse jeudi, reprend trois pour cent... après sa chute de plus de huit pour cent vendredi.",
     {"shots": [clip("9"), dict(clip("9b"), at_word=w(t, "chute"))]},
     [{"type": "stock", "key": "ANT", "name": "Anthropic", "sub": "ANT · Nasdaq · avant l'ouverture · " + YF, "pct": "+3 %", "up": True,
       "y": 560, "at_word": 1, "until_word": w(t, "chute")},
      {"type": "stock", "key": "ANT", "name": "Anthropic", "sub": "Vendredi 20 nov. · 88,91 $", "pct": "−8,5 %", "up": False,
       "y": 560, "at_word": w(t, "chute")}])

t = "L'Asie a aussi calmé le jeu : Taïwan durcit la vente à découvert, la Chine assouplit le crédit boursier, et Séoul se dit prêt à agir."
beat(t, "L'Asie a aussi calmé le jeu : Taïwan durcit la vente à découvert... la Chine assouplit le crédit boursier... et Séoul se dit prêt à agir.",
     {"shots": [clip("10"), dict(clip("10b"), at_word=w(t, "Chine")), dict(clip("10c"), at_word=w(t, "Séoul"))]},
     [{"type": "news", "at_word": w(t, "Taïwan"), "left": "ASIE · AUTORITÉS", "right": "23 NOV.", "tag": "SOUTIEN",
       "headline": "Taïwan durcit la vente à découvert, la Chine assouplit le crédit sur marge, la Corée du Sud se dit prête à agir",
       "highlight": "prête à agir", "sub": FW}])

t = "Mais le vrai danger arrive : le marché voit à 91 % une hausse des taux de la Fed le 9 décembre."
beat(t, "Mais le vrai danger arrive : le marché voit à quatre-vingt-onze pour cent une hausse des taux de la Fed... le neuf décembre.",
     scr("11"),
     [{"type": "screen_counter", "kicker": "HAUSSE DES TAUX FED", "value_from": 0, "value_to": 91, "decimals": 0,
       "prefix": "≈ ", "suffix": " %", "color": "red", "pill": "RÉUNION DE LA FED · 9 DÉCEMBRE",
       "desc": "Polymarket · 98 % le 12 nov. · " + YF}])

t = "Résultat : le taux américain à 10 ans remonte déjà, à 4,96 %."
beat(t, "Résultat : le taux américain à dix ans remonte déjà... à près de cinq pour cent.",
     scr("12"),
     [{"type": "screen_duo",
       "a": {"kicker": "10 ANS US · AVANT", "value_to": 4.91, "decimals": 2, "prefix": "", "suffix": " %", "color": "gold", "desc": "Niveau précédent"},
       "b_at_word": w(t, "4,96"),
       "b": {"kicker": "10 ANS US · CE LUNDI", "value_to": 4.96, "decimals": 2, "prefix": "", "suffix": " %", "color": "red", "desc": "+5 points de base · " + FW}}])

t = "À surveiller cette semaine : les résultats de Dell mardi, puis Wall Street fermée jeudi pour Thanksgiving."
beat(t, "À surveiller cette semaine : les résultats de Dell mardi... puis Wall Street fermée jeudi, pour Thanksgiving.",
     {"shots": [clip("13"), dict(clip("13b"), at_word=w(t, "Wall"))]},
     [{"type": "stock", "key": "DELL", "name": "Dell", "sub": "Résultats · mardi 24 novembre", "y": 560, "at_word": w(t, "Dell"), "until_word": w(t, "Wall")},
      {"type": "news", "at_word": w(t, "Wall"), "left": "AGENDA · WALL STREET", "right": "CETTE SEMAINE", "tag": "À SURVEILLER",
       "headline": "Résultats de Dell mardi, marchés fermés jeudi 26 pour Thanksgiving, séance écourtée vendredi",
       "highlight": "fermés jeudi 26", "sub": BI}])

t = "Alors, simple rebond technique, ou vrai retour de la confiance ? Dis-le en commentaire."
beat(t, "Alors... simple rebond technique, ou vrai retour de la confiance ? Dis-le en commentaire.", clip("14"),
     [{"type": "bigtitle", "lines": ["SIMPLE REBOND", "OU VRAI RETOUR ?"], "at_word": 1}])

t = "La prochaine secousse, tu veux la subir ou la voir venir ? Sur mon Telegram gratuit : l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées et mes opportunités en temps réel. Plus de 22 000 personnes y sont déjà. Accès gratuit, lien en bio."
say = "La prochaine secousse, tu veux la subir... ou la voir venir ? Sur mon Telegram gratuit : l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées et mes opportunités en temps réel. Plus de vingt-deux mille personnes y sont déjà... Accès gratuit, lien en bio."
beat(t, say, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Wall Street rebondit : ce qu'il faut surveiller", "imgs": ["tg_1eaa56f0.jpg", "tg_3435c02c_top.jpg"],
       "subs": 22760, "subs_at_word": w(t, "22"), "bio_at_word": w(t, "bio"), "button": "ACCÈS GRATUIT"}],
     cta="long", endcard={"duration": 1.8, "button": "ACCÈS GRATUIT", "small": "Telegram gratuit · lien en bio"})

CUT = [int(x) for x in sys.argv[1:]]
B = [b for i, b in enumerate(B) if i not in CUT]
spec = {"id": EP, "date_label": "23 novembre 2026", "brand": "Invest Family Fr", "hook_type": "bignum",
        "hook_formula": "compte à rebours",
        "cta_angle": "La prochaine secousse, tu veux la subir ou la voir venir ?",
        "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://finance.yahoo.com/markets/live/stock-market-today-monday-november-23-dow-sp-500-nasdaq-091118583.html",
                    "https://beinsure.com/news/dow-jones-and-us-stock-futures-surge-as-nasdaq-100-rebounds/",
                    "https://finwire.io/news/stock-markets-news/premarket-us-futures-rally-as-ai-rout-pauses",
                    "https://coincentral.com/nvidia-anthropic-and-alphabet-shares-bounce-back-as-investors-buy-the-dip",
                    "https://www.tipranks.com/news/stock-market-today-nov-23-markets-see-a-boost-after-last-weeks-ai-selloff"],
        "beats": B}
json.dump(spec, open(f'{D}/spec.json', 'w'), ensure_ascii=False, indent=1)
txt = "\n".join(b["say"] for b in B)
open(f'{D}/voice_text.txt', 'w').write(txt)
print(len(B), "beats", len(txt.split()), "mots")
