import json, sys
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep34_assureurs_medicare'
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
CN = "CappNotes · clôture du 18 nov. 2026"
BI = "Beinsure · 18 nov. 2026"
YF = "Yahoo Finance · 18 nov. 2026"

t = "90 milliards de dollars. C'est ce que Washington veut reprendre aux assureurs santé."
beat(t, "Quatre-vingt-dix milliards de dollars... C'est ce que Washington veut reprendre aux assureurs santé.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "Washington"))]},
     [{"type": "date", "text": "Jeudi 19 novembre 2026 · Wall Street hier soir", "until_beat": 1},
      {"type": "hook_bignum", "value_to": 90, "prefix": "", "suffix": " Md$", "unit": "À RÉCUPÉRER EN 10 ANS",
       "label": "Estimation de l'agence Medicare (CMS) · 2027-2036", "logos": ["UNH", "HUM", "CVS"],
       "reveal_at_word": w(t, "Washington"), "count_dur": 1.0}])

t = "Résultat : UnitedHealth s'effondre de 10 % en une seule séance."
beat(t, "Résultat : UnitedHealth s'effondre de dix pour cent... en une seule séance.",
     {"screen": True, "under": clip("1")},
     [{"type": "screen_counter", "kicker": "UNITEDHEALTH · MER. 18 NOV.", "value_from": 0, "value_to": -10.2, "decimals": 1,
       "prefix": "", "suffix": " %", "color": "red", "pill": "CLÔTURE ≈ 349,81 $", "desc": CN + " · " + BI},
      {"type": "stock", "key": "UNH", "name": "UnitedHealth", "sub": "UNH · NYSE · 18 nov. 2026", "pct": "−10,21 %", "up": False,
       "y": 1380, "at_word": w(t, "UnitedHealth")}])

t = "Et ce n'est pas le pire : Humana plonge de 13 %. Elevance, Centene et CVS suivent."
beat(t, "Et ce n'est pas le pire : Humana plonge de treize pour cent. Elevance, Centene et C.V.S. suivent.",
     {"shots": [clip("2"), dict(clip("2b"), at_word=w(t, "Elevance"))]},
     [{"type": "tickers", "title": "ASSUREURS SANTÉ · 18 NOV.", "rows": [
         {"name": "Humana", "pct": "−12,98 %", "at_word": w(t, "Humana"), "key": "HUM", "up": False},
         {"name": "Elevance", "pct": "−7,63 %", "at_word": w(t, "Elevance"), "key": "ELV", "up": False},
         {"name": "Centene", "pct": "−7,03 %", "at_word": w(t, "Centene"), "key": "CNC", "up": False},
         {"name": "CVS Health", "pct": "−5,20 %", "at_word": w(t, "CVS"), "key": "CVS", "up": False}]},
      {"type": "source", "text": CN}])

t = "UnitedHealth en tête, le Dow Jones recule de 561 points."
beat(t, "UnitedHealth en tête, le Dow Jones recule de cinq cent soixante et un points.",
     {"screen": True, "under": clip("4")},
     [{"type": "screen_counter", "kicker": "DOW JONES · MER. 18 NOV.", "value_from": 0, "value_to": -561, "decimals": 0,
       "prefix": "", "suffix": "", "color": "red", "pill": "POINTS PERDUS · −1,11 % · 50 198",
       "desc": "UnitedHealth ≈ 4,3 % de l'indice (Yahoo Finance) · " + CN}])

t = "Alors, qui a déclenché cette panique ?"
beat(t, "Alors... qui a déclenché cette panique ?", clip("5"),
     [{"type": "bigtitle", "lines": ["QUI A DÉCLENCHÉ", "CETTE PANIQUE ?"], "at_word": w(t, "qui")}])

t = "Cette secousse, je la suis en direct sur mon Telegram. Lien en bio."
beat(t, t, clip("6"),
     [{"type": "phone", "mode": "mini", "img": "tg_3435c02c.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "Le coupable, c'est l'État américain lui-même. Son agence Medicare vient de dévoiler un plan baptisé CRUSH."
beat(t, "Le coupable... c'est l'État américain lui-même. Son agence Medicare vient de dévoiler un plan baptisé Creuche.",
     {"shots": [clip("7"), dict(clip("7b"), at_word=w(t, "agence"))]},
     [{"type": "news", "at_word": w(t, "agence"), "left": "CMS · AGENCE MEDICARE", "right": "16 NOV.", "tag": "ALERTE",
       "headline": "« CRUSH » : le nouveau plan anti-fraude de Medicare vise les assureurs privés",
       "highlight": "vise les assureurs privés", "sub": BI + " · " + YF}])

t = "Le principe : contrôler un échantillon de dossiers… puis étendre les erreurs à tout le contrat."
beat(t, "Le principe : contrôler un échantillon de dossiers... puis étendre les erreurs à tout le contrat.",
     {"shots": [clip("8"), dict(clip("8b"), at_word=w(t, "étendre"))]},
     [{"type": "bigtitle", "lines": ["UN ÉCHANTILLON…", "TOUT LE CONTRAT"], "at_word": w(t, "échantillon")},
      {"type": "source", "text": "Audits RADV · Medicare Advantage · " + BI}])

t = "Et ces contrôles remonteraient jusqu'aux paiements de 2018."
beat(t, "Et ces contrôles remonteraient jusqu'aux paiements de deux mille dix-huit.",
     {"screen": True, "under": clip("9")},
     [{"type": "screen_counter", "kicker": "AUDITS MEDICARE ADVANTAGE", "value_from": 2026, "value_to": 2018, "decimals": 0,
       "prefix": "", "suffix": "", "color": "gold", "pill": "ANNÉE DE PAIEMENT DE DÉPART", "desc": "Règle proposée le 16 nov. 2026 · " + BI}])

t = "Selon l'agence, près de 9 milliards de dollars de trop-perçus par année de paiement."
beat(t, "Selon l'agence, près de neuf milliards de dollars de trop-perçus... par année de paiement.",
     {"screen": True, "under": clip("10")},
     [{"type": "screen_counter", "kicker": "TROP-PERÇUS RÉCUPÉRABLES", "value_from": 0, "value_to": 9, "decimals": 0,
       "prefix": "≈ ", "suffix": " Md$", "color": "gold", "pill": "PAR ANNÉE DE PAIEMENT", "desc": "Estimation CMS · " + BI}])

t = "Washington cite des abus : des fauteuils roulants fantômes facturés, des seniors en bonne santé placés en soins palliatifs."
beat(t, "Washington cite des abus : des fauteuils roulants fantômes facturés... des seniors en bonne santé placés en soins palliatifs.",
     {"shots": [clip("11"), dict(clip("11b"), at_word=w(t, "seniors"))]},
     [{"type": "news", "at_word": w(t, "fauteuils"), "left": "HHS · CMS", "right": "16 NOV.", "tag": "EXEMPLES CITÉS",
       "headline": "Fauteuils roulants inexistants facturés, seniors en bonne santé inscrits en soins palliatifs",
       "highlight": "inexistants", "sub": YF}])

t = "Le plus frappant ? La santé chute de plus de 2 %… pendant que la tech monte."
beat(t, "Le plus frappant ? La santé chute de plus de deux pour cent... pendant que la tech monte.",
     {"screen": True, "under": clip("12")},
     [{"type": "screen_duo",
       "a": {"kicker": "SECTEUR SANTÉ · S&P 500", "value_to": -2.2, "decimals": 1, "prefix": "", "suffix": " %", "color": "red", "desc": CN},
       "b_at_word": w(t, "tech"),
       "b": {"kicker": "SECTEUR TECH · S&P 500", "value_to": 0.34, "decimals": 2, "prefix": "+", "suffix": " %", "color": "green", "desc": "Nasdaq +0,42 % · " + CN}}])

t = "Mais rien n'est joué : un tribunal a annulé une règle similaire en 2025. Et Oppenheimer prévoit de nouveaux recours."
beat(t, "Mais rien n'est joué : un tribunal a annulé une règle similaire en deux mille vingt-cinq. Et Oppenheimer prévoit de nouveaux recours.",
     {"shots": [clip("13"), dict(clip("13b"), at_word=w(t, "Oppenheimer"))]},
     [{"type": "news", "at_word": w(t, "Oppenheimer"), "left": "OPPENHEIMER · ANALYSTES", "right": "18 NOV.", "tag": "CITATION",
       "headline": "« La CMS fera face aux mêmes recours juridiques qu'en 2025 »",
       "highlight": "mêmes recours juridiques", "sub": YF}])

t = "À surveiller : l'avis du public sur ce plan est ouvert jusqu'au 19 janvier."
beat(t, "À surveiller : l'avis du public sur ce plan est ouvert jusqu'au dix-neuf janvier.", clip("14"),
     [{"type": "tickers", "title": "À SURVEILLER", "rows": [
         {"name": "UnitedHealth", "pct": "349,81 $", "at_word": 0, "key": "UNH", "up": False},
         {"name": "Humana", "pct": "−12,98 %", "at_word": w(t, "plan"), "key": "HUM", "up": False},
         {"name": "Fin des commentaires", "pct": "19 JANV.", "at_word": w(t, "19"), "up": True}]},
      {"type": "source", "text": BI + " · " + YF}])

t = "Alors, simple coup de semonce… ou début d'une longue descente pour les assureurs ? Dis-le en commentaire."
beat(t, "Alors... simple coup de semonce... ou début d'une longue descente pour les assureurs ? Dis-le en commentaire.", clip("15"),
     [{"type": "bigtitle", "lines": ["COUP DE SEMONCE", "OU LONGUE DESCENTE ?"], "at_word": w(t, "simple")}])

t = ("La prochaine secousse, tu veux la subir ou la voir venir ? Mon canal Telegram gratuit, c'est plus de 22 000 personnes, "
     "l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées, les opportunités en temps réel. Lien en bio.")
say = t.replace("plus de 22 000", "plus de vingt-deux mille")
beat(t, say, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Assureurs santé : ce que prépare Washington", "imgs": ["tg_4b2fa9a8.jpg", "tg_38e4f34b.jpg", "tg_1eaa56f0.jpg"],
       "subs": 22760, "subs_at_word": w(t, "22"), "bio_at_word": w(t, "bio"), "button": "REJOINDRE LE CANAL"}],
     cta="long", endcard={"duration": 1.8, "button": "REJOINDRE LE CANAL", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "19 novembre 2026", "brand": "Invest Family Fr",
        "hook_type": "bignum", "hook_formula": "chiffre choc",
        "cta_angle": "La prochaine secousse, tu veux la subir ou la voir venir ?", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad",
                  "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://cappnotes.substack.com/p/closing-look-wednesday-november-18",
                    "https://www.stocktitan.net/articles/stock-market-today-live-november-18-2026",
                    "https://beinsure.com/news/healthcare-stocks-fall-as-medicare-rules-trigger-a-selloff/",
                    "https://finance.yahoo.com/healthcare/article/unitedhealth-and-other-insurance-stocks-drag-down-the-dow-after-cms-proposes-new-anti-fraud-rule-173851810.html",
                    "https://www.alainguillot.com/stock-market-recap-november-18-2026/"],
        "beats": B}
json.dump(spec, open(f'/home/claude/kit/episodes/{EP}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'/home/claude/kit/episodes/{EP}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), sum(len(b["say"].split()) for b in B), "mots")
