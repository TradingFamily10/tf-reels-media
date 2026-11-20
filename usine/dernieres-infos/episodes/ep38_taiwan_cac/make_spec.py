import json, sys
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep38_taiwan_cac'
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
GG = "GGMA Macro · 20 nov. 2026, 07h27"
AB = "Agefi-Dow Jones via ABC Bourse · 20 nov. 2026, 9h47"
MV = "AFP via MoneyVox · 20 nov. 2026"

t = "Ce n'est pas Paris qui fait plonger le CAC 40. C'est Taïwan."
beat(t, "Ce n'est pas Paris qui fait plonger le CAC quarante... C'est Taïwan.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "Taïwan"))]},
     [{"type": "date", "text": "Vendredi 20 novembre 2026 · Bourses mondiales", "until_beat": 0},
      {"type": "hook_bignum", "value_to": 17, "prefix": "−", "suffix": ",5 %", "unit": "TAÏWAN EN UNE SEMAINE",
       "label": "Pire semaine depuis 1991 · " + GG, "logos": ["TSM", "SSU", "SFTBY"],
       "reveal_at_word": w(t, "Taïwan"), "count_dur": 1.0}])

t = "La Bourse de Taïwan perd 17,5 % sur la semaine. Du jamais vu depuis plus de 30 ans."
beat(t, "La Bourse de Taïwan perd dix-sept pour cent et demi sur la semaine... Du jamais vu depuis plus de trente ans.",
     {"screen": True, "under": clip("1")},
     [{"type": "screen_counter", "kicker": "TAIEX · SUR LA SEMAINE", "value_from": 0, "value_to": -17.5, "decimals": 1,
       "prefix": "", "suffix": " %", "color": "red", "pill": "PIRE SEMAINE DEPUIS 1991", "desc": GG}])

t = "Et ce n'est pas le pire : ce vendredi, Taipei lâche encore plus de 6 %."
beat(t, "Et ce n'est pas le pire : ce vendredi, Taipei lâche encore plus de six pour cent.",
     {"shots": [clip("2"), dict(clip("2b"), at_word=w(t, "Taipei"))]},
     [{"type": "tickers", "title": "ASIE · CE VENDREDI", "rows": [
         {"name": "Taipei", "pct": "−6,23 %", "at_word": w(t, "Taipei"), "up": False},
         {"name": "Séoul · Kospi", "pct": "−5,21 %", "at_word": w(t, "encore"), "up": False},
         {"name": "Tokyo · Nikkei", "pct": "−5,06 %", "at_word": w(t, "6"), "up": False}]},
      {"type": "source", "text": MV}])

t = "TSMC recule de près de 5 %, Samsung de 7 %, et SoftBank de 14 %."
beat(t, "T.S.M.C. recule de près de cinq pour cent, Samsung de sept... et SoftBank de quatorze.",
     {"screen": True, "under": clip("3")},
     [{"type": "tickers", "title": "LES GÉANTS DES PUCES ET DE L'IA", "rows": [
         {"name": "TSMC", "pct": "−4,8 %", "at_word": 0, "key": "TSM", "up": False},
         {"name": "Samsung Electronics", "pct": "−7,2 %", "at_word": w(t, "Samsung"), "key": "SSU", "up": False},
         {"name": "SoftBank Group", "pct": "−14,2 %", "at_word": w(t, "SoftBank"), "key": "SFTBY", "up": False}]},
      {"type": "source", "text": GG}])

t = "Et la vague arrive en Europe : ce matin, le CAC 40 recule encore de près de 1 %."
beat(t, "Et la vague arrive en Europe : ce matin, le CAC quarante recule encore de près de un pour cent.",
     {"shots": [clip("4"), dict(clip("4b"), at_word=w(t, "CAC"))]},
     [{"type": "tickers", "title": "EUROPE · VERS 9H40", "rows": [
         {"name": "CAC 40", "pct": "−0,9 %", "at_word": w(t, "CAC"), "up": False},
         {"name": "DAX · Francfort", "pct": "−1,1 %", "at_word": w(t, "recule"), "up": False},
         {"name": "Stoxx Europe 600", "pct": "−0,9 %", "at_word": w(t, "près"), "up": False}]},
      {"type": "source", "text": AB}])

t = "Avant même ce vendredi, Paris avait déjà perdu 3,44 % depuis lundi."
beat(t, "Avant même ce vendredi, Paris avait déjà perdu plus de trois pour cent depuis lundi.",
     {"screen": True, "under": clip("5")},
     [{"type": "screen_counter", "kicker": "CAC 40 · DE LUNDI À JEUDI", "value_from": 0, "value_to": -3.44, "decimals": 2,
       "prefix": "", "suffix": " %", "color": "red", "pill": "CLÔTURE JEUDI : 8 080,74 PTS", "desc": MV}])

t = "Alors, comment une île d'Asie peut-elle faire trembler ton épargne ?"
beat(t, "Alors... comment une île d'Asie peut-elle faire trembler ton épargne ?", clip("6"),
     [{"type": "bigtitle", "lines": ["UNE ÎLE D'ASIE", "ET TON ÉPARGNE ?"], "at_word": w(t, "île")}])

t = "Cette tempête, je la suis en temps réel sur mon Telegram. Lien en bio."
beat(t, t, clip("7"),
     [{"type": "phone", "mode": "mini", "img": "tg_1eaa56f0.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "La réponse tient en deux lettres : IA."
beat(t, "La réponse tient en deux lettres : I.A.", clip("8b"),
     [{"type": "bigtitle", "lines": ["DEUX LETTRES :", "I.A."], "at_word": w(t, "lettres")}])

t = "Hier, Anthropic a levé 81 milliards de dollars en Bourse."
beat(t, "Hier, Anthropic a levé quatre-vingt-un milliards de dollars en Bourse.",
     {"screen": True, "under": clip("8")},
     [{"type": "screen_counter", "kicker": "ANTHROPIC · INTRODUCTION RECORD", "value_from": 0, "value_to": 81.3, "decimals": 1,
       "prefix": "", "suffix": " Md$", "color": "gold", "pill": "+17,07 % À LA 1RE CLÔTURE · 97,17 $", "desc": MV},
      {"type": "stock", "key": "ANT", "name": "Anthropic", "sub": "ANT · Nasdaq · 19 nov. 2026", "pct": "+17,07 %", "up": True,
       "y": 1380, "at_word": w(t, "Anthropic")}])

t = "Et pourtant, le même jour, Wall Street a chuté de plus de 2 %."
beat(t, "Et pourtant, le même jour... Wall Street a chuté de plus de deux pour cent.",
     {"shots": [clip("9"), dict(clip("9b"), at_word=w(t, "Wall"))]},
     [{"type": "tickers", "title": "WALL STREET · CLÔTURE DU 19 NOV.", "rows": [
         {"name": "Dow Jones", "pct": "−2,19 %", "at_word": w(t, "Wall"), "up": False},
         {"name": "S&P 500", "pct": "−2,02 %", "at_word": w(t, "chuté"), "up": False},
         {"name": "Nasdaq", "pct": "−2,25 %", "at_word": w(t, "plus"), "up": False}]},
      {"type": "source", "text": MV}])

t = "Le doute : l'IA a besoin de montagnes d'argent, alors qu'emprunter coûte toujours plus cher."
beat(t, "Le doute : l'I.A. a besoin de montagnes d'argent... alors qu'emprunter coûte toujours plus cher.",
     {"shots": [clip("10"), dict(clip("10b"), at_word=w(t, "qu'emprunter"))]},
     [{"type": "news", "at_word": 2, "left": "SWISSQUOTE", "right": "20 NOV.", "tag": "ANALYSE",
       "headline": "L'infrastructure de l'IA « a toujours besoin de financements considérables » alors que le coût du crédit grimpe",
       "highlight": "financements considérables", "sub": "Ipek Ozkardeskaya, Swissquote · " + MV}])

t = "Et en Europe, les marchés de taux voient à 97 % une hausse de la BCE en décembre."
beat(t, "Et en Europe, les marchés de taux voient à quatre-vingt-dix-sept pour cent une hausse de la B.C.E. en décembre.",
     {"screen": True, "under": clip("12")},
     [{"type": "screen_counter", "kicker": "BCE · RÉUNION DE DÉCEMBRE", "value_from": 0, "value_to": 97, "decimals": 0,
       "prefix": "", "suffix": " %", "color": "gold", "pill": "PROBABILITÉ D'UNE HAUSSE DE TAUX", "desc": "Prix des marchés de taux · " + GG}])

t = "Prochain test : Christopher Waller, de la Fed, prend la parole à 14 h 25."
beat(t, "Prochain test : Christopher Waller, de la Fed... prend la parole à quatorze heures vingt-cinq.",
     clip("13"),
     [{"type": "tickers", "title": "À SURVEILLER CE VENDREDI", "rows": [
         {"name": "Waller · Fed", "pct": "14H25", "at_word": w(t, "Waller"), "up": True},
         {"name": "Confiance Michigan", "pct": "16H00", "at_word": w(t, "parole"), "up": True}]},
      {"type": "source", "text": "Agenda (heure de Paris) · " + GG}])

t = "Et ce soir, une 7e baisse du S&P 500 serait sa plus longue série depuis 2020."
beat(t, "Et ce soir, une septième baisse du S&P cinq cents serait sa plus longue série... depuis deux mille vingt.",
     {"shots": [clip("14"), dict(clip("14b"), at_word=w(t, "longue"))]},
     [{"type": "news", "at_word": 2, "left": "DEUTSCHE BANK", "right": "20 NOV.", "tag": "STATISTIQUE",
       "headline": "Une 7e baisse du S&P 500 : plus longue série depuis le krach de la pandémie, en février 2020",
       "highlight": "depuis février 2020", "sub": "Jim Reid, Deutsche Bank · " + MV},
      {"type": "stock", "key": "DB", "name": "Deutsche Bank", "sub": "Analyse de Jim Reid", "y": 1380, "at_word": 3}])

t = "Alors, simple purge, ou début d'une vraie correction ? Dis-le en commentaire."
beat(t, "Alors... simple purge, ou début d'une vraie correction ? Dis-le en commentaire.", clip("15"),
     [{"type": "bigtitle", "lines": ["SIMPLE PURGE", "OU CORRECTION ?"], "at_word": w(t, "simple")}])

t = ("Quand l'Asie éternue, ton portefeuille s'enrhume. Rejoins mon Telegram gratuit : "
     "actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. "
     "Plus de 22 000 personnes déjà. Accès gratuit, lien en bio.")
say = t.replace("Plus de 22 000", "Plus de vingt-deux mille").replace("éternue,", "éternue...")
beat(t, say, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Taïwan −17,5 % en une semaine : mon analyse", "imgs": ["tg_4b2fa9a8.jpg", "tg_3435c02c.jpg", "tg_38e4f34b.jpg"],
       "subs": 22760, "subs_at_word": w(t, "22"), "bio_at_word": w(t, "bio"), "button": "ACCÈS GRATUIT"}],
     cta="long", endcard={"duration": 1.8, "button": "ACCÈS GRATUIT", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "20 novembre 2026", "brand": "Invest Family Fr",
        "hook_type": "bignum", "hook_formula": "coupable inattendu",
        "cta_angle": "Quand l'Asie éternue, ton portefeuille s'enrhume", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad",
                  "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://gfxfts.substack.com/p/ai-rout-sinks-asian-stocks-as-japan",
                    "https://www.abcbourse.com/marches/l-europe-decroche-vif-regain-d-aversion-au-risque_706431",
                    "https://www.moneyvox.fr/bourse/actualites/111329/le-cac-40-en-net-repli-a-ouverture-ce-vendredi-20-novembre"],
        "beats": B}
json.dump(spec, open(f'/home/claude/kit/episodes/{EP}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'/home/claude/kit/episodes/{EP}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), sum(len(b["say"].split()) for b in B), "mots")
