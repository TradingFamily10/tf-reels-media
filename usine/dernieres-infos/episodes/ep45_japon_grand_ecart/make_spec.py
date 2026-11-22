import json, sys
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep45_japon_grand_ecart'
def w(text, word, n=0):
    t = tokens(text); k = 0
    for i, x in enumerate(t):
        if word.lower() in x.lower():
            if k == n: return i
            k += 1
    raise SystemExit(f"mot introuvable: {word} dans {text}")
CX = {"0": 0.27, "10": 0.72, "4": 0.45, "6": 0.62, "8": 0.47}
def clip(n, ss=1, cx=None):
    return {"clip": f"b{n}.mp4", "ss": ss, "cx": CX.get(n, 0.5) if cx is None else cx}
def scr(n): return {"screen": True, "under": clip(n)}
B = []
def beat(text, say, bg, overlays, **kw):
    b = {"text": text, "say": say, "bg": bg, "overlays": overlays}; b.update(kw); B.append(b); return b
DGT = "DG Trésor · veille Japon-Corée · 20 nov. 2026"
IL = "investingLive · 16 nov. 2026"

t = "22 % effacés depuis juin. Et ce n'est pas Wall Street : c'est la Bourse de Tokyo."
beat(t, "Vingt-deux pour cent effacés depuis juin... Et ce n'est pas Wall Street : c'est la Bourse de Tokyo.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "Wall"))]},
     [{"type": "date", "text": "Dimanche 22 novembre 2026 · Japon", "until_beat": 0},
      {"type": "breaking", "label": "DERNIÈRES INFOS", "lines": ["−22 % DEPUIS JUIN", "LA BOURSE DE TOKYO", "DÉCROCHE"]},
      {"type": "ticket", "at_word": w(t, "Wall"), "title": "TOKYO · NIKKEI 225", "subtitle": "Clôture du vendredi 20 nov. 2026",
       "rows": [["Record du 22 juin", "72 353"], ["Clôture du 20 nov.", "56 437"], ["Sur la semaine", "−7,7 %"]],
       "total": ["DEPUIS LE RECORD", "−22 %"], "stamp": "TOKYO"}])

t = "Et ce n'est pas le pire : sur la seule semaine, le Nikkei a perdu près de 8 %."
beat(t, "Et ce n'est pas le pire : sur la seule semaine, le Nikkei a perdu près de huit pour cent.",
     scr("1"),
     [{"type": "screen_counter", "kicker": "NIKKEI · SEMAINE", "value_from": 0, "value_to": -7.7, "decimals": 1,
       "prefix": "", "suffix": " %", "color": "red", "pill": "CLÔTURE 56 437 PTS",
       "desc": "Semaine du 16 au 20 nov. · " + DGT}])

t = "Pendant ce temps, l'économie japonaise recule : −0,1 % au troisième trimestre, en rythme annuel."
beat(t, "Pendant ce temps, l'économie japonaise recule... au troisième trimestre, en rythme annuel.",
     scr("2"),
     [{"type": "screen_duo",
       "a": {"kicker": "PIB · ATTENDU", "value_to": 0.3, "decimals": 1, "prefix": "+", "suffix": " %", "color": "gold", "desc": "3e trimestre 2026, en rythme annuel · " + IL},
       "b_at_word": w(t, "recule"),
       "b": {"kicker": "PIB · PUBLIÉ", "value_to": -0.1, "decimals": 1, "prefix": "", "suffix": " %", "color": "red", "desc": "1re baisse en un an, après +1,7 % au 2e trimestre · " + DGT}}])

t = "Les marchés attendaient une hausse. C'est le premier recul depuis un an."
beat(t, "Les marchés attendaient une hausse... C'est le premier recul depuis un an.",
     {"shots": [clip("3"), dict(clip("3b"), at_word=w(t, "premier"))]},
     [{"type": "news", "at_word": w(t, "attendaient"), "left": "JAPON · PIB T3", "right": "16 NOV.", "tag": "SURPRISE",
       "headline": "Le PIB japonais recule de 0,1 % en rythme annuel, contre +0,3 % attendu",
       "highlight": "recule de 0,1 %", "sub": IL + " · " + DGT}])

t = "Et pourtant, les prix accélèrent : 2,3 % d'inflation en octobre, au plus haut depuis un an."
beat(t, "Et pourtant, les prix accélèrent : plus de deux pour cent d'inflation en octobre... au plus haut depuis un an.",
     scr("4"),
     [{"type": "screen_counter", "kicker": "INFLATION · OCTOBRE", "value_from": 0, "value_to": 2.3, "decimals": 1,
       "prefix": "+", "suffix": " %", "color": "gold", "pill": "PLUS HAUT DEPUIS NOV. 2025",
       "desc": "Sur un an · inflation sous-jacente 2,2 % · " + DGT}])

t = "Alors, une économie qui recule et des prix qui montent : que va faire la Banque du Japon ?"
beat(t, "Alors... une économie qui recule et des prix qui montent : que va faire la Banque du Japon ?",
     clip("5"),
     [{"type": "bigtitle", "lines": ["QUE VA FAIRE", "LA BANQUE DU JAPON ?"], "at_word": w(t, "que")}])

t = "Le Japon, je le suis de près sur mon Telegram. Lien en bio."
beat(t, t, clip("6"),
     [{"type": "phone", "mode": "mini", "img": "tg_4b2fa9a8.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "La réponse des marchés est claire : une hausse de taux le 18 décembre, jugée probable à 85 %."
beat(t, "La réponse des marchés est claire : une hausse de taux le dix-huit décembre... jugée probable à quatre-vingt-cinq pour cent.",
     scr("7"),
     [{"type": "screen_counter", "kicker": "BOJ · 18 DÉCEMBRE", "value_from": 0, "value_to": 85, "decimals": 0,
       "prefix": "", "suffix": " %", "color": "gold", "pill": "PROBABILITÉ D'UNE HAUSSE DE 0,25 POINT",
       "desc": "Anticipations de marché au 20 nov. 2026 · " + DGT}])

t = "Monter les taux dans une économie qui recule : c'est le grand écart."
beat(t, "Monter les taux dans une économie qui recule... c'est le grand écart.",
     clip("8"),
     [{"type": "bigtitle", "lines": ["LE GRAND", "ÉCART"], "at_word": w(t, "grand")}])

t = "Sur les marchés, le taux japonais à 30 ans frôle déjà les 4 %. Le 10 ans est à 2,79 %."
beat(t, "Sur les marchés, le taux japonais à trente ans frôle déjà les quatre pour cent... Le dix ans est à près de trois pour cent.",
     {"shots": [clip("9"), dict(clip("9b"), at_word=w(t, "Le", 1))]},
     [{"type": "tickers", "title": "TAUX JAPONAIS · 20 NOV.",
       "rows": [{"name": "Japon 30 ans", "pct": "3,97 %", "at_word": w(t, "30"), "up": True},
                {"name": "Japon 20 ans", "pct": "3,69 %", "at_word": w(t, "frôle"), "up": True},
                {"name": "Japon 10 ans", "pct": "2,79 %", "at_word": w(t, "10"), "up": True}]},
      {"type": "source", "text": DGT}])

t = "Côté entreprises, Nissan sabre ses ventes en Chine : 370 000 à 400 000 voitures attendues, contre 580 000."
beat(t, "Côté entreprises, Nissan sabre ses ventes en Chine... au mieux quatre cent mille voitures attendues, contre cinq cent quatre-vingt mille.",
     {"shots": [clip("10"), dict(clip("10b"), at_word=w(t, "370"))]},
     [{"type": "stock", "key": "NSANY", "name": "Nissan", "sub": "Prévision de ventes en Chine 2026 abaissée", "y": 520, "at_word": w(t, "Nissan")},
      {"type": "news", "at_word": w(t, "370"), "left": "NISSAN · CHINE 2026", "right": "NOV.", "tag": "PRÉVISION",
       "headline": "Ventes attendues en Chine : 370 000 à 400 000 véhicules, contre 580 000 prévus",
       "highlight": "370 000 à 400 000", "sub": DGT}])

t = "En octobre, les ventes de voitures neuves en Chine ont plongé de 27 %."
beat(t, "En octobre, les ventes de voitures neuves en Chine ont plongé de vingt-sept pour cent.",
     scr("11"),
     [{"type": "screen_counter", "kicker": "CHINE · AUTOS · OCT.", "value_from": 0, "value_to": -27, "decimals": 0,
       "prefix": "", "suffix": " %", "color": "red", "pill": "SUR UN AN",
       "desc": "Part des marques japonaises en Chine : −20 % depuis 2022 · " + DGT}])

t = "Le twist : malgré la chute, les investisseurs japonais ont raflé 3 milliards de dollars de l'introduction en Bourse d'Anthropic."
beat(t, "Le twist : malgré la chute, les investisseurs japonais ont raflé trois milliards de dollars... de l'introduction en Bourse d'Anthropic.",
     {"shots": [clip("12"), dict(clip("12b"), at_word=w(t, "raflé"))]},
     [{"type": "stock", "key": "ANT", "name": "Anthropic", "sub": "3 Md$ pris par des investisseurs japonais · 3,7 % de l'opération", "y": 520, "at_word": w(t, "investisseurs")},
      {"type": "source", "text": "Introduction valorisée 81 Md$ · " + DGT}])

t = "Prochaine date à surveiller : le 18 décembre. Ce jour-là, la Banque du Japon tranche."
beat(t, "Prochaine date à surveiller : le dix-huit décembre... Ce jour-là, la Banque du Japon tranche.",
     {"shots": [clip("13"), dict(clip("13b"), at_word=w(t, "Ce"))]},
     [{"type": "news", "at_word": w(t, "18"), "left": "AGENDA · JAPON", "right": "18 DÉC.", "tag": "À SURVEILLER",
       "headline": "Vendredi 18 décembre : décision de la Banque du Japon sur ses taux",
       "highlight": "18 décembre", "sub": DGT}])

t = "Alors, le Japon peut-il secouer les marchés du monde entier ? Dis-le en commentaire."
beat(t, "Alors... le Japon peut-il secouer les marchés du monde entier ? Dis-le en commentaire.",
     clip("14"),
     [{"type": "bigtitle", "lines": ["LE JAPON, PROCHAINE", "SECOUSSE ?"], "at_word": w(t, "Japon")}])

t = "Si tu veux comprendre avant les autres au lieu de subir, rejoins mon Telegram gratuit : actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. Plus de 22 000 personnes y sont déjà. Lien en bio."
say = "Si tu veux comprendre avant les autres au lieu de subir, rejoins mon Telegram gratuit : actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. Plus de vingt-deux mille personnes y sont déjà... Lien en bio."
beat(t, say, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Japon : le grand écart de la Banque centrale, décrypté", "imgs": ["tg_38e4f34b.jpg", "tg_1eaa56f0.jpg", "tg_3435c02c_top.jpg"],
       "subs": 22760, "subs_at_word": w(t, "22"), "bio_at_word": w(t, "bio"), "button": "ACCÈS GRATUIT"}],
     cta="long", endcard={"duration": 1.8, "button": "ACCÈS GRATUIT", "small": "Telegram gratuit · lien en bio"})

B = [b for i, b in enumerate(B) if i not in (3,)]  # coupé (durée)
spec = {"id": EP, "date_label": "22 novembre 2026", "brand": "Invest Family Fr", "hook_type": "breaking",
        "hook_formula": "chiffre choc",
        "cta_angle": "Si tu veux comprendre avant les autres au lieu de subir, rejoins mon Telegram gratuit",
        "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.tresor.economie.gouv.fr/Articles/2026/11/20/japon-coree-du-sud-veille-economique-et-financiere-du-16-au-20-novembre-2026",
                    "https://investinglive.com/news/japan-q3-gdp-shrinks-0-1-annualised-vs-0-3-expected-as-exports-and-consumers-weigh/"],
        "beats": B}
json.dump(spec, open(f'/home/claude/kit/episodes/{EP}/spec.json', 'w'), ensure_ascii=False, indent=1)
txt = "\n".join(b["say"] for b in B)
open(f'/home/claude/kit/episodes/{EP}/voice_text.txt', 'w').write(txt)
print(len(B), "beats", len(txt.split()), "mots")
