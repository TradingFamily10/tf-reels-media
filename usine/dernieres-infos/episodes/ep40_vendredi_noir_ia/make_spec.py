import json, sys
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep40_vendredi_noir_ia'
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
ST = "StockTitan · 20 nov. 2026"
CN = "CappNotes · 20 nov. 2026, clôture"
AP = "AP via BNN Bloomberg · 20 nov. 2026"

t = "Le jour où Nvidia a perdu 14 % en une seule séance."
beat(t, "Le jour où Nvidia a perdu quatorze pour cent... en une seule séance.",
     {"screen": True, "under": clip("0")},
     [{"type": "date", "text": "Vendredi 20 novembre 2026 · Wall Street", "until_beat": 0},
      {"type": "screen_logos", "kicker": "VENDREDI NOIR POUR L'I.A.", "value_from": 0, "value_to": 14, "decimals": 0,
       "prefix": "−", "suffix": " %", "color": "red", "pill": "NVIDIA EN UNE SÉANCE",
       "keys": ["NVDA", "AMD", "MU", "AVGO", "TSM", "ANT"], "desc": ST + " · " + CN}])

t = "Le Nasdaq plonge de plus de 5 % et efface tous ses gains de 2026."
beat(t, "Le Nasdaq plonge de plus de cinq pour cent... et efface tous ses gains de deux mille vingt-six.",
     {"screen": True, "under": clip("1")},
     [{"type": "screen_counter", "kicker": "NASDAQ COMPOSITE · 20 NOV.", "value_from": 0, "value_to": -5.28, "decimals": 2,
       "prefix": "", "suffix": " %", "color": "red", "pill": "NÉGATIF SUR 2026", "desc": "Clôture à 22 617,73 points · " + CN, "logo": "NDAQ"}])

t = "Et ce n'est pas le pire : le S&P 500 entre en correction, 10 % sous son record."
beat(t, "Et ce n'est pas le pire : le S. and P. cinq cents entre en correction... dix pour cent sous son record.",
     {"shots": [clip("2"), dict(clip("2b"), at_word=w(t, "correction"))]},
     [{"type": "news", "at_word": w(t, "S&P"), "left": "WALL STREET", "right": "20 NOV.", "tag": "MARCHÉS",
       "headline": "Le S&P 500 et le Dow Jones clôturent en correction, environ 10 % sous leurs records",
       "highlight": "en correction", "sub": CN + " · " + AP}])

t = "Sur la semaine : près de 9 % de baisse, du jamais vu depuis avril 2025."
beat(t, "Sur la semaine : près de neuf pour cent de baisse... du jamais vu depuis avril deux mille vingt-cinq.",
     {"screen": True, "under": clip("3")},
     [{"type": "screen_counter", "kicker": "S&P 500 · SUR LA SEMAINE", "value_from": 0, "value_to": -8.6, "decimals": 1,
       "prefix": "", "suffix": " %", "color": "red", "pill": "PIRE SEMAINE DEPUIS AVRIL 2025", "desc": "7e séance de baisse d'affilée · " + CN}])

t = "Les puces s'effondrent : Micron, AMD et Broadcom lâchent toutes plus de 12 %."
beat(t, "Les puces s'effondrent : Micron, A.M.D. et Broadcom lâchent toutes plus de douze pour cent.",
     {"shots": [clip("4"), dict(clip("4b"), at_word=w(t, "Broadcom"))]},
     [{"type": "tickers", "title": "SEMI-CONDUCTEURS · 20 NOV.", "rows": [
        {"name": "Micron", "key": "MU", "pct": "−13,89 %", "at_word": w(t, "Micron")},
        {"name": "AMD", "key": "AMD", "pct": "−13,25 %", "at_word": w(t, "AMD")},
        {"name": "Broadcom", "key": "AVGO", "pct": "−12,19 %", "at_word": w(t, "Broadcom")},
        {"name": "TSMC", "key": "TSM", "pct": "−9,48 %", "at_word": w(t, "12")}]},
      {"type": "source", "text": ST + " · " + CN}])

t = "Même Anthropic, entrée en Bourse jeudi, recule de plus de 8 %."
beat(t, "Même Anthropic, entrée en Bourse jeudi, recule de plus de huit pour cent.",
     {"shots": [clip("5"), dict(clip("5b"), at_word=w(t, "recule"))]},
     [{"type": "stock", "key": "ANT", "name": "Anthropic", "sub": "ANT · Nasdaq · 2e séance · 88,91 $ · " + ST,
       "pct": "−8,50 %", "up": False, "y": 560, "at_word": w(t, "Anthropic")}])

t = "Alors, qui a allumé la mèche ?"
beat(t, "Alors... qui a allumé la mèche ?", clip("6"),
     [{"type": "bigtitle", "lines": ["QUI A ALLUMÉ", "LA MÈCHE ?"], "at_word": w(t, "qui")}])

t = "Cette tempête, je la suis heure par heure sur mon Telegram. Lien en bio."
beat(t, "Cette tempête, je la suis heure par heure sur mon Telegram. Lien en bio.", clip("7"),
     [{"type": "phone", "mode": "mini", "img": "tg_38e4f34b.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "Selon Reuters, le gendarme de la Bourse américaine examine de possibles problèmes comptables chez Nvidia."
beat(t, "Selon Reuters, le gendarme de la Bourse américaine examine de possibles problèmes comptables chez Nvidia.",
     {"shots": [clip("8"), dict(clip("8b"), at_word=w(t, "examine"))]},
     [{"type": "news", "at_word": 1, "left": "REUTERS", "right": "20 NOV.", "tag": "NVIDIA",
       "headline": "Des équipes de la SEC examineraient de possibles problèmes comptables chez Nvidia",
       "highlight": "possibles problèmes comptables", "sub": "Rapporté par " + ST + " · " + CN},
      {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "NVDA · Nasdaq · clôture 125,53 $", "pct": "−14,01 %", "up": False,
       "y": 1180, "at_word": w(t, "Nvidia")}])

t = "Rien n'est prouvé. Mais la Californie enquête aussi : ses puces sont-elles arrivées en Chine ?"
beat(t, "Rien n'est prouvé. Mais la Californie enquête aussi : ses puces sont-elles arrivées en Chine ?",
     {"shots": [clip("9"), dict(clip("9b"), at_word=w(t, "puces"))]},
     [{"type": "news", "at_word": w(t, "Californie"), "left": "CALIFORNIE", "right": "19 NOV.", "tag": "ENQUÊTE",
       "headline": "Le procureur général Rob Bonta adresse une assignation à Nvidia : ses puces ont-elles atteint la Chine ?",
       "highlight": "assignation", "sub": CN + " · aucune accusation prouvée"}])

t = "Résultat : la tech perd plus de 7 %. Seul secteur dans le vert : la consommation de base."
beat(t, "Résultat : la tech perd plus de sept pour cent. Seul secteur dans le vert : la consommation de base.",
     {"screen": True, "under": clip("10")},
     [{"type": "screen_duo",
       "a": {"kicker": "TECHNOLOGIE · S&P 500", "value_to": -7.27, "decimals": 2, "prefix": "", "suffix": " %", "color": "red", "desc": "Pire secteur de la séance", "logo": "NVDA"},
       "b_at_word": w(t, "Seul"),
       "b": {"kicker": "CONSOMMATION DE BASE", "value_to": 0.67, "decimals": 2, "prefix": "+", "suffix": " %", "color": "green", "desc": "Seul secteur en hausse · " + CN}}])

t = "L'indice de la peur, le VIX, bondit à près de 36. Au plus haut depuis mars."
beat(t, "L'indice de la peur, le VIX, bondit à près de trente-six... Au plus haut depuis mars.",
     {"screen": True, "under": clip("11")},
     [{"type": "screen_gauge", "kicker": "VIX · 35,89 (+26 %)", "pill": "INDICE DE LA PEUR", "desc": "Plus haute clôture depuis fin mars · " + CN}])

t = "Le paradoxe ? L'argent fuit vers les obligations : le taux américain à 10 ans retombe sous 5 %."
beat(t, "Le paradoxe ? L'argent fuit vers les obligations : le taux américain à dix ans retombe sous cinq pour cent.",
     {"screen": True, "under": clip("12")},
     [{"type": "screen_duo",
       "a": {"kicker": "TAUX US À 10 ANS · JEUDI", "value_to": 5.04, "decimals": 2, "prefix": "", "suffix": " %", "color": "white", "desc": AP},
       "b_at_word": w(t, "retombe"),
       "b": {"kicker": "TAUX US À 10 ANS · VENDREDI", "value_to": 4.92, "decimals": 2, "prefix": "", "suffix": " %", "color": "green", "desc": "Plus forte baisse depuis le 22 oct. · " + CN}}])

t = "La contagion est mondiale : Taïwan perd 17 % sur la semaine, un record. Paris recule de près de 2 %."
beat(t, "La contagion est mondiale : Taïwan perd dix-sept pour cent sur la semaine, un record. Paris recule de près de deux pour cent.",
     {"shots": [clip("13"), dict(clip("13b"), at_word=w(t, "Paris"))]},
     [{"type": "tickers", "title": "LE MONDE ENTIER TOUCHÉ", "rows": [
        {"name": "Taiex · semaine", "pct": "−17,5 %", "at_word": w(t, "Taïwan")},
        {"name": "Nikkei · vendredi", "pct": "−5,06 %", "at_word": w(t, "semaine")},
        {"name": "CAC 40 · vendredi", "pct": "−1,89 %", "at_word": w(t, "Paris")},
        {"name": "SoftBank", "key": "SFTBY", "pct": "−14,48 %", "at_word": w(t, "recule")}]},
      {"type": "source", "text": "Taiex : pire semaine de son histoire · " + CN}])

t = "À surveiller lundi : les indices PMI à 15 h 45, puis la Fed de New York à 22 h."
beat(t, "À surveiller lundi : les indices P.M.I. à quinze heures quarante-cinq... puis la Fed de New York à vingt-deux heures.",
     {"shots": [clip("15"), dict(clip("15b"), at_word=w(t, "puis"))]},
     [{"type": "tickers", "title": "À SURVEILLER LUNDI 23 NOV.", "rows": [
        {"name": "PMI flash US", "pct": "15H45", "at_word": w(t, "PMI"), "up": True},
        {"name": "John Williams (Fed NY)", "pct": "22H00", "at_word": w(t, "York"), "up": True},
        {"name": "Hausse Fed le 9 déc.", "pct": "90 %", "at_word": w(t, "22"), "up": True}]},
      {"type": "source", "text": "Agenda, heure de Paris · probabilité Kalshi · " + CN}])

t = "Alors, simple purge ou bulle de l'I.A. qui éclate ? Dis-le en commentaire."
beat(t, "Alors... simple purge, ou bulle de l'I.A. qui éclate ? Dis-le en commentaire.", clip("16"),
     [{"type": "bigtitle", "lines": ["SIMPLE PURGE", "OU BULLE QUI ÉCLATE ?"], "at_word": w(t, "simple")}])

t = ("Ce week-end, pendant que tout le monde digère le choc, on prépare lundi sur mon Telegram gratuit : "
     "actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. "
     "Plus de 22 000 personnes déjà. Lien en bio.")
say = ("Ce week-end, pendant que tout le monde digère le choc... on prépare lundi sur mon Telegram gratuit : "
       "actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. "
       "Plus de vingt-deux mille personnes déjà. Lien en bio.")
beat(t, say, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Krach de l'I.A. : le plan pour lundi", "imgs": ["tg_4b2fa9a8.jpg", "tg_3435c02c_top.jpg", "tg_38e4f34b.jpg"],
       "subs": 22760, "subs_at_word": w(t, "22"), "bio_at_word": len(tokens(t)) - 1, "button": "ACCÈS GRATUIT"}],
     cta="long", endcard={"duration": 1.8, "button": "ACCÈS GRATUIT", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "21 novembre 2026", "brand": "Invest Family Fr",
        "hook_type": "logowall", "hook_formula": "le jour où",
        "cta_angle": "Ce week-end, pendant que tout le monde digère le choc, on prépare lundi ensemble",
        "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad",
                  "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.stocktitan.net/articles/stock-market-today-live-november-20-2026",
                    "https://cappnotes.substack.com/p/closing-look-friday-november-20-2026",
                    "https://www.bnnbloomberg.ca/markets/2026/11/20/us-stocks-tumble-and-the-sp-500-drops-as-the-sell-off-for-ai-stocks-accelerates/",
                    "https://finance.yahoo.com/markets/stocks/articles/stock-market-today-nov-20-223513707.html"],
        "beats": B}
json.dump(spec, open(f'/home/claude/kit/episodes/{EP}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'/home/claude/kit/episodes/{EP}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), "beats", sum(len(tokens(b["text"])) for b in B), "mots")
