import json, sys, os
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep58_kioxia_nvidia'
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
INV = "Investing.com · 26 nov. 2026"
WV = "Wisevoter · 26 nov. 2026"
SAXO = "Saxo · 27 nov. 2026"
HEY = "Heygotrade / CNBC · 27 nov. 2026"
EDGE = "The Edge · 27 nov. 2026 · 3h08 GMT"

t = "Ce n'est pas un résultat qui a fait bondir Kioxia de 14 %. C'est un test avec Nvidia."
beat(t, "Ce n'est pas un résultat qui a fait bondir Kioxia de quatorze pour cent... C'est un test avec Nvidia.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "test"))]},
     [{"type": "date", "text": "Vendredi 27 novembre 2026 · avant l'Europe", "until_beat": 0},
      {"type": "breaking", "label": "DERNIÈRES INFOS", "lines": ["KIOXIA +14,5 %", "UN TEST AVEC NVIDIA", "TOKYO · JEUDI 26/11"]},
      {"type": "stock", "key": "KXIA", "name": "Kioxia", "sub": "Tokyo · plus haut de séance jeudi", "pct": "+14,5 %", "up": True, "size": "big", "y": 1600, "at_word": w(t, "Kioxia")}])

t = "Et ce n'est pas le plus fou : la veille, le même titre avait plongé de 14 %."
beat(t, "Et ce n'est pas le plus fou... la veille, le même titre avait plongé de quatorze pour cent.", scr("1"),
     [{"type": "screen_duo", "a": {"kicker": "KIOXIA · MERCREDI 25 NOV.", "value_to": -14.18, "decimals": 2, "prefix": "", "suffix": " %", "color": "red", "desc": "Séance de panique sur les puces"},
       "b_at_word": w(t, "plongé"), "b": {"kicker": "KIOXIA · JEUDI 26 NOV.", "value_to": 12.57, "decimals": 2, "prefix": "+", "suffix": " %", "color": "green", "desc": "Clôture à 7 762 yens · " + WV}},
      {"type": "source", "text": INV}])

t = "Kioxia, c'est la mémoire flash : les disques SSD qui stockent les données de l'IA."
beat(t, "Kioxia, c'est la mémoire flash... les disques S.S.D. qui stockent les données de l'I.A.",
     {"shots": [clip("2"), dict(clip("3"), at_word=w(t, "disques"))]},
     [{"type": "stock", "key": "KXIA", "name": "Kioxia", "sub": "Mémoire flash · SSD", "y": 1480, "at_word": 0},
      {"type": "source", "text": INV}])

t = "Le test : 144 disques Kioxia dans un système Nvidia."
beat(t, "Le test... cent quarante-quatre disques Kioxia, dans un système Nvidia.", scr("3"),
     [{"type": "screen_counter", "kicker": "PREUVE DE CONCEPT · NVIDIA GB200 NVL72", "value_from": 0, "value_to": 144, "decimals": 0, "prefix": "", "suffix": "", "color": "white", "pill": "SSD KIOXIA", "desc": "18 serveurs, 8 disques chacun · " + INV}])

t = "Environ 1,1 pétaoctet de stockage, mis à portée des puces de Nvidia."
beat(t, "Environ un pétaoctet de stockage... mis à portée des puces de Nvidia.",
     {"shots": [clip("4"), dict(clip("0b", ss=6), at_word=w(t, "mis"))]},
     [{"type": "bigtitle", "lines": ["≈ 1,1 PÉTAOCTET", "POUR LES GPU"], "at_word": 0},
      {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "Logiciel SCADA + architecture Storage-Next", "y": 1480, "at_word": w(t, "Nvidia")},
      {"type": "source", "text": INV}])

t = "Mais attention : les deux groupes évaluent encore la faisabilité technique."
beat(t, "Mais attention... les deux groupes évaluent encore la faisabilité technique.", clip("5"),
     [{"type": "news", "at_word": w(t, "groupes"), "left": "KIOXIA × NVIDIA", "right": "26 NOV.", "tag": "PRUDENCE", "headline": "Les deux sociétés évaluent encore la faisabilité technique et les performances de la solution", "highlight": "évaluent encore", "sub": "Aucun chiffre de vitesse publié · " + INV}])

t = "Alors, pourquoi un simple test fait-il bondir une action à ce point ?"
beat(t, "Alors... pourquoi un simple test fait-il bondir une action à ce point ?", clip("6"),
     [{"type": "bigtitle", "lines": ["POURQUOI", "UN TEL BOND ?"], "at_word": 1}])

t = "Ces montagnes russes de la tech, je les suis en direct sur mon Telegram. Lien en bio."
beat(t, t, clip("7"),
     [{"type": "phone", "mode": "mini", "img": "tg_38e4f34b.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "Parce que Kioxia a fondu de plus de 40 % ce mois-ci."
beat(t, "Parce que Kioxia a fondu... de plus de quarante pour cent ce mois-ci.", scr("8"),
     [{"type": "screen_counter", "kicker": "KIOXIA · NOVEMBRE 2026", "value_from": 0, "value_to": -40, "decimals": 0, "prefix": "> ", "suffix": " %", "color": "red", "pill": "SUR LE MOIS", "desc": "Malgré le rebond de jeudi · " + SAXO}])

t = "Elle vaut environ 1,7 fois ses bénéfices attendus : la moins chère du Nikkei 225."
beat(t, "Elle vaut moins de deux fois ses bénéfices attendus... la moins chère du Nikkei deux cent vingt-cinq.", scr("9"),
     [{"type": "screen_counter", "kicker": "KIOXIA · PER ATTENDU", "value_from": 0, "value_to": 1.7, "decimals": 1, "prefix": "≈ ", "suffix": " x", "color": "white", "pill": "LA MOINS CHÈRE DU NIKKEI 225", "desc": SAXO}])

t = "Le doute vient de New York : mercredi, Nvidia et Micron ont reculé de plus de 3 %."
beat(t, "Le doute vient de New York... mercredi, Nvidia et Micron ont reculé de plus de trois pour cent.", scr("10"),
     [{"type": "tickers", "title": "WALL STREET · MERCREDI 25 NOV. · CLÔTURE", "rows": [
         {"key": "NVDA", "name": "Nvidia", "pct": "−3,91 %", "up": False, "at_word": w(t, "Nvidia")},
         {"key": "MU", "name": "Micron", "pct": "−4,53 %", "up": False, "at_word": w(t, "Micron")}]},
      {"type": "source", "text": HEY}])

t = "Selon TrendForce, des géants chinois du cloud ont réduit leurs commandes de mémoire pour 2027."
beat(t, "Selon TrendForce, des géants chinois du cloud ont réduit leurs commandes de mémoire pour deux mille vingt-sept.", clip("11"),
     [{"type": "news", "at_word": w(t, "géants"), "left": "TRENDFORCE", "right": "25 NOV.", "tag": "MÉMOIRE", "headline": "Des fournisseurs de cloud chinois réduisent les commandes de mémoire prévues pour 2027", "highlight": "réduisent les commandes", "sub": HEY}])

t = "Ce matin, l'Asie rebondit : Séoul prend 2,72 %, Tokyo 1,17 %."
beat(t, "Ce matin, l'Asie rebondit... Séoul prend près de trois pour cent, Tokyo plus d'un pour cent.", scr("12"),
     [{"type": "screen_duo", "a": {"kicker": "SÉOUL · KOSPI", "value_to": 2.72, "decimals": 2, "prefix": "+", "suffix": " %", "color": "green", "desc": "4 839,20 points"},
       "b_at_word": w(t, "Tokyo"), "b": {"kicker": "TOKYO · NIKKEI 225", "value_to": 1.17, "decimals": 2, "prefix": "+", "suffix": " %", "color": "green", "desc": "58 172 points"}},
      {"type": "source", "text": EDGE}])

t = "Mais à Tokyo, l'inflation hors produits frais accélère à 2,9 %."
beat(t, "Mais à Tokyo, l'inflation hors produits frais accélère... à près de trois pour cent.", scr("13"),
     [{"type": "screen_duo", "a": {"kicker": "TOKYO · INFLATION · OCTOBRE", "value_to": 2.6, "decimals": 1, "prefix": "", "suffix": " %", "color": "white", "desc": "Hors produits frais"},
       "b_at_word": w(t, "accélère"), "b": {"kicker": "TOKYO · NOVEMBRE", "value_to": 2.9, "decimals": 1, "prefix": "", "suffix": " %", "color": "red", "desc": "Cible de la Banque du Japon : 2 %"}},
      {"type": "source", "text": "The Edge / Trading Economics · 27 nov. 2026"}])

t = "Ce soir, Wall Street rouvre pour une demi-séance. Et lundi, la Banque du Japon prend la parole."
beat(t, "Ce soir, Wall Street rouvre pour une demi-séance... Et lundi, la Banque du Japon prend la parole.", clip("14"),
     [{"type": "bigtitle", "lines": ["WALL STREET : 20 H", "LUNDI : LA BOJ PARLE"], "at_word": w(t, "Wall")},
      {"type": "source", "text": "Saxo / The Edge · 27 nov. 2026"}])

t = "Alors, Kioxia : vrai rebond ou simple sursaut ? Dis-le en commentaire."
beat(t, "Alors... Kioxia : vrai rebond ou simple sursaut ? Dis-le en commentaire.", clip("16"),
     [{"type": "bigtitle", "lines": ["VRAI REBOND", "OU SURSAUT ?"], "at_word": 1},
      {"type": "stock", "key": "KXIA", "name": "Kioxia", "sub": "−40 % en novembre", "y": 1480, "at_word": 1}])

t = ("Si tu veux comprendre avant les autres au lieu de subir, rejoins plus de 22 000 personnes sur mon Telegram gratuit : "
     "actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. Lien en bio.")
s = ("Si tu veux comprendre avant les autres... au lieu de subir, rejoins plus de vingt-deux mille personnes sur mon Telegram gratuit : "
     "actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. Lien en bio.")
beat(t, s, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Kioxia, Nvidia et la mémoire de l'IA : mon décryptage du jour",
       "imgs": ["tg_1eaa56f0.jpg", "tg_4b2fa9a8.jpg", "tg_3435c02c.jpg"], "subs": 22760,
       "subs_at_word": w(t, "22"), "bio_at_word": w(t, "bio"), "button": "ACCÈS GRATUIT"}],
     cta="long", endcard={"duration": 1.8, "button": "ACCÈS GRATUIT", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "27 novembre 2026", "brand": "Invest Family Fr", "hook_type": "breaking",
        "hook_formula": "coupable inattendu", "cta_angle": "Si tu veux comprendre avant les autres au lieu de subir",
        "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": [
            "https://www.investing.com/news/stock-market-news/kioxia-jumps-14-after-nvidia-collaboration-as-chip-stocks-rebound-5052074",
            "https://wisevoter.com/world/2026/11/26/kioxia-shares-jump-nvidia-ai-storage-test",
            "https://www.heygotrade.com/en/news/ai-stocks-rebound-kioxia-nvidia-memory-demo/",
            "https://www.home.saxo/en-sg/content/articles/macro/asia-market-quick-take--27-november-2026-27112026",
            "https://edgeconsultancykw.com/asia-market-wrap-27-november-2026/",
            "https://tradingeconomics.com/japan/tokyo-core-cpi",
            "https://www.breitbart.com/news/asian-shares-mostly-rise-ahead-of-wall-streets-reopening-after-the-thanksgiving-holiday/"],
        "beats": B}
json.dump(spec, open(f'{D}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'{D}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), "beats", sum(len(b["say"].split()) for b in B), "mots")
