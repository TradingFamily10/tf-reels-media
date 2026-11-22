import json, sys
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep43_semaine_decisive'
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
MC = "Marketcalls · bilan hebdo · 21 nov. 2026"
SP = "Focus Taiwan via The Morning Brief · 21 nov. 2026"

t = "Demain, les Bourses rouvrent. Et la semaine dernière a effacé 10 % du Nasdaq."
beat(t, "Demain, les Bourses rouvrent... Et la semaine dernière a effacé dix pour cent du Nasdaq.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "semaine"))]},
     [{"type": "date", "text": "Dimanche 22 novembre 2026 · La semaine qui vient", "until_beat": 0},
      {"type": "hook_bignum", "value_to": 10, "prefix": "−", "suffix": " %", "unit": "NASDAQ EN UNE SEMAINE",
       "label": "22 617,73 pts le 20 nov. · −10,02 % · " + MC, "logos": ["NVDA", "AMD", "ANT"],
       "reveal_at_word": w(t, "semaine"), "count_dur": 1.0}])

t = "Et ce n'est pas le pire : le CAC 40 a perdu plus de 5 % en cinq séances. Le DAX, 7 %."
beat(t, "Et ce n'est pas le pire : le CAC quarante a perdu plus de cinq pour cent en cinq séances... Le DAX, sept pour cent.",
     scr("1"),
     [{"type": "screen_duo",
       "a": {"kicker": "CAC 40 · SEMAINE", "value_to": -5.27, "decimals": 2, "prefix": "", "suffix": " %", "color": "red", "desc": "Clôture 7 927,75 pts · " + MC},
       "b_at_word": w(t, "DAX"),
       "b": {"kicker": "DAX · SEMAINE", "value_to": -7.28, "decimals": 2, "prefix": "", "suffix": " %", "color": "red", "desc": "Clôture 24 802,78 pts · " + MC}}])

t = "À Wall Street, le S&P 500 signe sa pire semaine depuis avril 2025. Tokyo et Séoul plongent aussi."
beat(t, "À Wall Street, le S. and P. cinq cents signe sa pire semaine depuis avril deux mille vingt-cinq... Tokyo et Séoul plongent aussi.",
     {"shots": [clip("3"), dict(clip("3b"), at_word=w(t, "Tokyo"))]},
     [{"type": "tickers", "title": "LA SEMAINE EN BOURSE",
       "rows": [{"name": "S&P 500", "pct": "−8,61 %", "at_word": w(t, "S&P"), "up": False},
                {"name": "Nikkei (Tokyo)", "pct": "−7,70 %", "at_word": w(t, "Tokyo"), "up": False},
                {"name": "Kospi (Séoul)", "pct": "−7,95 %", "at_word": w(t, "Séoul"), "up": False}]},
      {"type": "source", "text": MC}])

t = "Le thermomètre de la peur, le VIX, a presque doublé en une semaine."
beat(t, "Le thermomètre de la peur, le VIX, a presque doublé... en une semaine.",
     scr("4"),
     [{"type": "screen_counter", "kicker": "VIX · INDICE DE LA PEUR", "value_from": 19.3, "value_to": 35.89, "decimals": 2,
       "prefix": "", "suffix": "", "color": "red", "pill": "+86 % EN UNE SEMAINE",
       "desc": "19,30 le 13 nov. → 35,89 le 20 nov. 2026 · " + MC}])

t = "Au cœur du séisme : Nvidia, moins 23 % en cinq jours."
beat(t, "Au cœur du séisme : Nvidia... moins vingt-trois pour cent en cinq jours.",
     clip("5"),
     [{"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "125,53 $ le 20 nov. · −47,5 % vs record du 6 oct.",
       "pct": "−22,9 %", "up": False, "y": 560, "at_word": w(t, "Nvidia")},
      {"type": "source", "text": MC}])

t = "Alors, que peut-il se passer dès lundi ?"
beat(t, "Alors... que peut-il se passer dès lundi ?",
     clip("6"),
     [{"type": "bigtitle", "lines": ["ET DÈS", "LUNDI ?"], "at_word": 1}])

t = "Cette semaine décisive, je la suis en direct sur mon Telegram. Lien en bio."
beat(t, t, clip("7"),
     [{"type": "phone", "mode": "mini", "img": "tg_38e4f34b.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "Premier test : Taïwan durcit encore les règles de vente à découvert, après une semaine à moins 17 %."
beat(t, "Premier test : Taïwan durcit encore les règles de vente à découvert... après une semaine à moins dix-sept pour cent.",
     {"shots": [clip("8"), dict(clip("8b"), at_word=w(t, "après"))]},
     [{"type": "news", "at_word": w(t, "Taïwan"), "left": "TAÏWAN · FSC", "right": "LUN. 23 NOV.", "tag": "RÉGULATION",
       "headline": "Le régulateur taïwanais resserre à nouveau les règles de marge sur la vente à découvert",
       "highlight": "resserre à nouveau", "sub": SP},
      {"type": "stock", "key": "TSM", "name": "TSMC", "sub": "Le 20 nov. · Taïex −17,5 % sur la semaine", "pct": "−9,48 %",
       "up": False, "y": 1380, "at_word": w(t, "après")}])

t = "Lundi, les indices d'activité PMI tombent en Europe et aux États-Unis. Mercredi, croissance et inflation américaines. Jeudi, Wall Street fermée."
beat(t, "Lundi, les indices d'activité P.M.I. tombent en Europe et aux États-Unis... Mercredi, croissance et inflation américaines. Jeudi, Wall Street fermée pour Thanksgiving.",
     {"shots": [clip("9"), dict(clip("9b"), at_word=w(t, "Mercredi"))]},
     [{"type": "tickers", "title": "L'AGENDA DE LA SEMAINE",
       "rows": [{"name": "PMI flash Europe, USA", "pct": "LUN. 23", "at_word": w(t, "Lundi"), "up": True},
                {"name": "PIB et inflation PCE (USA)", "pct": "MER. 25", "at_word": w(t, "croissance"), "up": True},
                {"name": "Wall Street fermée", "pct": "JEU. 26", "at_word": w(t, "Jeudi"), "up": False}]},
      {"type": "source", "text": MC}])

t = "Le vrai juge, c'est la Fed : une hausse de ses taux le 9 décembre est jouée à 92 %."
beat(t, "Le vrai juge, c'est la Fed : une hausse de ses taux le neuf décembre... est jouée à quatre-vingt-douze pour cent.",
     scr("11"),
     [{"type": "screen_counter", "kicker": "FED · HAUSSE LE 9 DÉC.", "value_from": 0, "value_to": 92, "decimals": 0,
       "prefix": "", "suffix": " %", "color": "white", "pill": "PROBABILITÉ (CME FEDWATCH)",
       "desc": "Vendredi 20 nov. au soir · Reuters / Schwab via Nocta · 21 nov. 2026", "at_word": w(t, "hausse")}])

t = "Pourtant, les obligations attirent : le taux américain à 10 ans retombe à 4,91 %."
beat(t, "Pourtant, les obligations attirent : le taux américain à dix ans... retombe sous les cinq pour cent.",
     scr("12"),
     [{"type": "screen_counter", "kicker": "TAUX US À 10 ANS", "value_from": 5.15, "value_to": 4.91, "decimals": 2,
       "prefix": "", "suffix": " %", "color": "green", "pill": "−24 POINTS DE BASE EN UNE SEMAINE",
       "desc": "Clôture du 20 nov. 2026 · " + MC, "at_word": w(t, "taux")}])

t = "Le twist : l'Europe entre dans l'hiver avec ses stocks de gaz au plus bas depuis 2013, selon l'AIE."
beat(t, "Le twist : l'Europe entre dans l'hiver avec ses stocks de gaz... au plus bas depuis deux mille treize, selon l'A.I.E.",
     {"shots": [clip("13"), dict(clip("13b"), at_word=w(t, "stocks"))]},
     [{"type": "news", "at_word": w(t, "Europe"), "left": "ÉNERGIE · AIE", "right": "21 NOV.", "tag": "GAZ",
       "headline": "Les stocks de gaz de l'UE abordent l'hiver à leur plus bas niveau depuis 2013",
       "highlight": "plus bas niveau depuis 2013", "sub": "AIE via The Morning Brief · 21 nov. 2026"}])

t = "Alors, simple rebond lundi, ou nouvelle vague de baisse ? Dis-le en commentaire."
beat(t, "Alors... simple rebond lundi, ou nouvelle vague de baisse ? Dis-le en commentaire.",
     clip("14"),
     [{"type": "bigtitle", "lines": ["REBOND OU", "NOUVELLE VAGUE ?"], "at_word": w(t, "rebond")}])

t = ("Lundi, tu peux découvrir les dégâts en ouvrant ton appli... ou être prêt avant l'ouverture. Mon Telegram gratuit : "
     "actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. "
     "Plus de 22 000 personnes y sont déjà. Lien en bio.")
say = ("Lundi, tu peux découvrir les dégâts en ouvrant ton appli... ou être prêt avant l'ouverture. Mon Telegram gratuit : "
       "actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. "
       "Plus de vingt-deux mille personnes y sont déjà. Lien en bio.")
beat(t, say, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Lundi : ce qu'il faut surveiller dès l'ouverture",
       "imgs": ["tg_4b2fa9a8.jpg", "tg_38e4f34b.jpg", "tg_3435c02c_top.jpg"], "subs": 22760,
       "subs_at_word": w(t, "22"), "bio_at_word": w(t, "bio"), "button": "ACCÈS GRATUIT"}],
     cta="long", endcard={"duration": 1.8, "button": "ACCÈS GRATUIT", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "22 novembre 2026", "brand": "Invest Family Fr", "hook_type": "bignum",
        "hook_formula": "compte à rebours",
        "cta_angle": "Lundi, découvrir les dégâts en ouvrant ton appli… ou être prêt avant l'ouverture",
        "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad",
                  "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.marketcalls.in/futures-and-options/weekly-market-roundup-21-november-2026.html",
                    "https://specterworks.substack.com/p/the-morning-brief-2026-11-21",
                    "https://no1sdailydigest.substack.com/p/daily-digest-2026-11-21",
                    "https://noctaaa.substack.com/p/daily-brief-saturday-21-november-2026"],
        "beats": B}
json.dump(spec, open(f'/home/claude/kit/episodes/{EP}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'/home/claude/kit/episodes/{EP}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), sum(len(b["say"].split()) for b in B), "mots")
