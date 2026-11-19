import json, sys
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep36_intel_client'
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
ST = "Stocktwits · 19 nov. 2026"
YH = "Stocktwits (Yahoo Finance) · 19 nov. 2026, 5h30 heure de New York"
LB = "Zhitong (Longbridge) · 19 nov. 2026"
GF = "GuruFocus · Seeking Alpha · 19 nov. 2026"

t = "Intel a perdu plus de la moitié de sa valeur en deux mois. Et pourtant, ce matin, elle rebondit."
beat(t, "Intel a perdu plus de la moitié de sa valeur en deux mois... Et pourtant, ce matin, elle rebondit.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "pourtant"))]},
     [{"type": "date", "text": "Jeudi 19 novembre 2026 · avant Wall Street", "until_beat": 0},
      {"type": "bigtitle", "lines": ["PLUS DE −50 %", "ET POURTANT…"], "at_word": 0},
      {"type": "stock", "key": "INTC", "name": "Intel", "sub": "INTC · Nasdaq · depuis fin septembre", "size": "big", "y": 600, "at_word": w(t, "pourtant")}])

t = "Près de 5 % de hausse avant l'ouverture."
beat(t, "Près de cinq pour cent de hausse... avant l'ouverture.",
     {"screen": True, "under": clip("1")},
     [{"type": "screen_counter", "kicker": "INTEL · PRÉOUVERTURE", "value_from": 0, "value_to": 4.65, "decimals": 2,
       "prefix": "+", "suffix": " %", "color": "green", "pill": "APRÈS 5 SÉANCES DE BAISSE", "desc": YH}])

t = "La raison ? Son tout premier client extérieur pour sa gravure la plus avancée, le 18A."
beat(t, "La raison ? Son tout premier client extérieur... pour sa gravure la plus avancée, le dix-huit A.",
     {"shots": [clip("2"), dict(clip("2b"), at_word=w(t, "gravure"))]},
     [{"type": "news", "at_word": 2, "left": "INTEL FOUNDRY", "right": "18 NOV.", "tag": "CONTRAT",
       "headline": "Intel signe son premier client externe pour sa technologie 18A-P",
       "highlight": "premier client externe", "sub": GF}])

t = "Son patron, Lip-Bu Tan, l'a annoncé hier à Austin, au Texas."
beat(t, "Son patron, Lip-Bu Tan, l'a annoncé hier à Austin, au Texas.",
     clip("3"),
     [{"type": "news", "at_word": 1, "left": "SOMMET TOMORROWX · AUSTIN", "right": "18 NOV.", "tag": "CITATION",
       "headline": "« Et puis le 18A… nous venons de signer le premier client » — Lip-Bu Tan, PDG d'Intel",
       "highlight": "premier client", "sub": ST + " · " + LB}])

t = "Fin octobre, Intel a prévenu : ses ventes du trimestre manqueront d'au moins 1 milliard de dollars."
beat(t, "Fin octobre, Intel a prévenu : ses ventes du trimestre manqueront d'au moins un milliard de dollars.",
     {"screen": True, "under": clip("4")},
     [{"type": "screen_counter", "kicker": "VENTES VS ATTENTES", "value_from": 0, "value_to": 1, "decimals": 0,
       "prefix": "− ", "suffix": " Md$", "color": "red", "pill": "AU MOINS · PC EN BERNE", "desc": LB}])

t = "Et le marché des PC restera déprimé jusqu'à mi-2027 au moins."
beat(t, "Et le marché des P.C. restera déprimé jusqu'à mi-deux-mille-vingt-sept au moins.",
     {"shots": [clip("5"), dict(clip("5b"), at_word=w(t, "déprimé"))]},
     [{"type": "news", "at_word": 3, "left": "INTEL · PRÉVISIONS", "right": "29 OCT.", "tag": "ALERTE",
       "headline": "Le marché des PC restera en crise au moins jusqu'au premier semestre 2027",
       "highlight": "premier semestre 2027", "sub": ST}])

t = "Cette semaine, même Nvidia a réduit d'un quart sa participation."
beat(t, "Cette semaine, même Nvidia a réduit d'un quart sa participation.",
     {"screen": True, "under": clip("6")},
     [{"type": "screen_counter", "kicker": "NVIDIA ALLÈGE INTEL", "value_from": 0, "value_to": 25, "decimals": 0,
       "prefix": "− ", "suffix": " %", "color": "red", "pill": "CETTE SEMAINE", "desc": ST},
      {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "Allège sa ligne Intel", "y": 1380, "at_word": w(t, "Nvidia")}])

t = "Alors, qui est ce mystérieux client ?"
beat(t, "Alors... qui est ce mystérieux client ?", clip("7"),
     [{"type": "bigtitle", "lines": ["QUI EST CE", "MYSTÉRIEUX CLIENT ?"], "at_word": w(t, "qui")}])

t = "Ce suspense, je le suis en temps réel sur mon Telegram. Lien en bio."
beat(t, t, clip("8"),
     [{"type": "phone", "mode": "mini", "img": "tg_3435c02c_top.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "Intel garde le nom secret. L'analyste Ben Bajarin cite trois pistes : Nvidia, Apple… ou un géant du cloud."
beat(t, "Intel garde le nom secret. L'analyste Ben Bajarine cite trois pistes : Nvidia, Apple... ou un géant du cloud.",
     {"screen": True, "under": clip("9")},
     [{"type": "screen_logos", "kicker": "LES PISTES DE BEN BAJARIN", "value_from": 0, "value_to": 3, "decimals": 0,
       "suffix": " PISTES", "color": "gold", "pill": "CREATIVE STRATEGIES", "keys": ["NVDA", "AAPL", "AMZN", "MSFT", "GOOGL"],
       "desc": LB + " · hypothèses, rien de confirmé"}])

t = "Car les géants du cloud manquent de capacité chez TSMC, le leader taïwanais."
beat(t, "Car les géants du cloud manquent de capacité chez T.S.M.C., le leader taïwanais.",
     {"shots": [clip("10"), dict(clip("10b"), at_word=w(t, "TSMC"))]},
     [{"type": "tickers", "title": "LE GOULOT D'ÉTRANGLEMENT", "rows": [
         {"name": "Amazon", "pct": "CLOUD", "at_word": w(t, "géants"), "key": "AMZN", "up": True},
         {"name": "Microsoft", "pct": "CLOUD", "at_word": w(t, "cloud"), "key": "MSFT", "up": True},
         {"name": "Google", "pct": "CLOUD", "at_word": w(t, "manquent"), "key": "GOOGL", "up": True},
         {"name": "TSMC · capacités saturées", "pct": "N°1 MONDIAL", "at_word": w(t, "TSMC"), "key": "TSM", "up": False}]},
      {"type": "source", "text": LB}])

t = "Et Microsoft devient le premier client affiché de son assemblage de puces EMIB."
beat(t, "Et Microsoft devient le premier client affiché de son assemblage de puces E.M.I.B.",
     clip("11"),
     [{"type": "stock", "key": "MSFT", "name": "Microsoft", "sub": "1er client public d'Intel pour l'EMIB", "y": 560, "at_word": w(t, "Microsoft")},
      {"type": "source", "text": LB}])

t = "L'enjeu dépasse la Bourse : l'État américain détient 10 % d'Intel."
beat(t, "L'enjeu dépasse la Bourse : l'État américain détient dix pour cent d'Intel.",
     {"screen": True, "under": clip("13")},
     [{"type": "screen_counter", "kicker": "PART DE L'ÉTAT AMÉRICAIN", "value_from": 0, "value_to": 10, "decimals": 0,
       "prefix": "", "suffix": " %", "color": "gold", "pill": "DEPUIS AOÛT 2025", "desc": LB + " · Nvidia a aussi investi 5 Md$"}])

t = "Et Trump ouvre une porte : les puces Blackwell de Nvidia pourraient arriver en Chine d'ici deux ou trois ans."
beat(t, "Et Trump ouvre une porte : les puces Blackwell de Nvidia pourraient arriver en Chine... d'ici deux ou trois ans.",
     {"shots": [clip("14"), dict(clip("14b"), at_word=w(t, "Blackwell"))]},
     [{"type": "news", "at_word": 1, "left": "APRÈS LA RENCONTRE AVEC XI JINPING", "right": "FOX NEWS", "tag": "CITATION",
       "headline": "« Dans deux ou trois ans, je dirais : allez-y, vous pouvez vendre des Blackwell » — Donald Trump",
       "highlight": "deux ou trois ans", "sub": ST},
      {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "+2 % en préouverture", "y": 1380, "at_word": w(t, "Nvidia")}])

t = "Résultat : le Nasdaq est attendu en hausse d'environ 2 %."
beat(t, "Résultat : le Nasdaq est attendu en hausse d'environ deux pour cent.",
     clip("15"),
     [{"type": "tickers", "title": "FUTURES · 5H30 À NEW YORK", "rows": [
         {"name": "Nasdaq 100", "pct": "+2,06 %", "at_word": w(t, "Nasdaq"), "up": True},
         {"name": "Intel", "pct": "+4,65 %", "at_word": w(t, "hausse"), "key": "INTC", "up": True},
         {"name": "Nvidia", "pct": "+2 %", "at_word": w(t, "environ"), "key": "NVDA", "up": True}]},
      {"type": "source", "text": YH}])

t = "Prochain rendez-vous : 15h30, l'ouverture de Wall Street, et les débuts d'Anthropic en Bourse."
beat(t, "Prochain rendez-vous : quinze heures trente, l'ouverture de Wall Street... et les débuts d'Anthropic en Bourse.",
     clip("16"),
     [{"type": "tickers", "title": "À SURVEILLER CET APRÈS-MIDI", "rows": [
         {"name": "Intel · tient-elle sa hausse ?", "pct": "15H30", "at_word": w(t, "15h30"), "key": "INTC", "up": True},
         {"name": "Anthropic · 1re cotation", "pct": "NASDAQ", "at_word": w(t, "Anthropic"), "key": "ANT", "up": True}]},
      {"type": "source", "text": YH}])

t = "Alors, Intel peut-elle vraiment rattraper TSMC ? Dis-le en commentaire."
beat(t, "Alors... Intel peut-elle vraiment rattraper T.S.M.C. ? Dis-le en commentaire.", clip("17"),
     [{"type": "bigtitle", "lines": ["INTEL PEUT-ELLE", "RATTRAPER TSMC ?"], "at_word": w(t, "Intel")}])

t = ("Pendant que les marchés paniquent, sur mon Telegram gratuit on garde la tête froide : l'actu géopolitique et financière décortiquée, "
     "des analyses d'actions détaillées, les opportunités en temps réel. Plus de 22 000 personnes déjà. Rejoins la famille, lien en bio.")
say = t.replace("Plus de 22 000", "Plus de vingt-deux mille")
beat(t, say, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Intel : le client mystère, mon analyse", "imgs": ["tg_1eaa56f0.jpg", "tg_3435c02c_top.jpg"],
       "subs": 22760, "subs_at_word": w(t, "22"), "bio_at_word": w(t, "bio"), "button": "REJOINS LA FAMILLE"}],
     cta="long", endcard={"duration": 1.8, "button": "REJOINS LA FAMILLE", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "19 novembre 2026", "brand": "Invest Family Fr",
        "hook_type": "chip", "hook_formula": "contre-intuitif",
        "cta_angle": "Pendant que les marchés paniquent, sur mon Telegram on garde la tête froide", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad",
                  "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://finance.yahoo.com/markets/stocks/articles/stock-futures-climb-ahead-anthropics-110203603.html",
                    "https://stocktwits.com/news-articles/markets/equity/nvda-intc-stocks-ease-post-5-day-rout-after-meeting-xi-jinping-trump-says-nvidia-blackwell-chips-could-reach-china-within-2-3-years/cNbiTxFR9io",
                    "https://longbridge.com/en/news/306044243",
                    "https://www.gurufocus.com/news/9209413/intel-intc-signs-first-external-customer-for-18a-chip-tech-shares-rise-26",
                    "https://seekingalpha.com/news/4674509-intel-lands-first-external-customer-for-18a-p-chips"],
        "beats": B}
json.dump(spec, open(f'/home/claude/kit/episodes/{EP}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'/home/claude/kit/episodes/{EP}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), sum(len(b["say"].split()) for b in B), "mots")
