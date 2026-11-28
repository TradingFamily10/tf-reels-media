import json, sys, os
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep62_sp_france_negative'
D = f'/home/claude/kit/episodes/{EP}'
def w(text, word, n=0):
    t = tokens(text); k = 0
    for i, x in enumerate(t):
        if word.lower() in x.lower():
            if k == n: return i
            k += 1
    raise SystemExit(f"mot introuvable: {word} dans {text}")
CX = {"13": 0.35, "12": 0.42}
SS = {"1": 3, "4": 5, "9": 3, "13": 3, "6": 2}
def clip(n, ss=None, cx=None):
    return {"clip": f"b{n}.mp4", "ss": SS.get(n, 1) if ss is None else ss, "cx": CX.get(n, 0.5) if cx is None else cx}
def scr(n): return {"screen": True, "under": clip(n)}
B = []
def beat(text, say, bg, overlays, **kw):
    b = {"text": text, "say": say, "bg": bg, "overlays": overlays}; b.update(kw); B.append(b); return b
BR = "Reuters via Boursorama · 27 nov. 2026"
FT = "FranceTransactions (AFT, S&P) · 28 nov. 2026"
XT = "XTB (Insee, AFT) · 27 nov. 2026"

# 0 — accroche (breaking, formule « chiffre choc »)
t = "Près de 3 600 milliards d'euros de dette. Et vendredi soir, S&P a sorti le carton orange."
beat(t, "Près de trois mille six cents milliards d'euros de dette... Et vendredi soir, S&P a sorti le carton orange.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "vendredi"))]},
     [{"type": "date", "text": "Samedi 28 novembre 2026 · dette française", "until_beat": 0},
      {"type": "breaking", "label": "DERNIÈRES INFOS", "lines": ["S&P : ALERTE", "NOTE A+ SOUS MENACE", "FRANCE · VEN. 27/11"]}])

t = "Et ce n'est pas le pire : les 3 grandes agences sont maintenant négatives sur la France."
beat(t, "Et ce n'est pas le pire... les trois grandes agences sont maintenant négatives sur la France.",
     scr("1"),
     [{"type": "screen_counter", "kicker": "AGENCES NÉGATIVES", "value_from": 0, "value_to": 3, "decimals": 0,
       "prefix": "", "suffix": " / 3", "color": "red", "pill": "MOODY'S · FITCH · S&P",
       "desc": "Moody's Aa3 (23/10) · Fitch A+ (30/10) · S&P A+ (27/11) · " + FT}])

t = "S&P garde la note A+. Mais la perspective passe de stable à négative : une dégradation devient possible."
beat(t, "S&P garde la note A plus. Mais la perspective passe de stable à négative... une dégradation devient possible.",
     clip("3"),
     [{"type": "news", "at_word": w(t, "perspective"), "left": "S&P GLOBAL RATINGS", "right": "27 NOV. · APRÈS LA CLÔTURE", "tag": "NOTATION",
       "headline": "S&P confirme la note A+ de la France mais l'assortit d'une perspective négative",
       "highlight": "perspective négative", "sub": BR}])

t = "Pourquoi ? Une dette qui grossit, et une croissance en panne."
beat(t, "Pourquoi ? Une dette qui grossit... et une croissance en panne.",
     clip("4"),
     [{"type": "bigtitle", "lines": ["DETTE QUI GROSSIT", "CROISSANCE EN PANNE"], "at_word": 1}])

t = "En cause : une dette publique à 119 % du PIB fin juin."
beat(t, "En cause... une dette publique à cent dix-neuf pour cent du P.I.B. fin juin.",
     scr("5"),
     [{"type": "screen_counter", "kicker": "DETTE PUBLIQUE · FIN JUIN 2026", "value_from": 100, "value_to": 119, "decimals": 0,
       "prefix": "", "suffix": " %", "color": "red", "pill": "3 595,5 MDS €", "desc": "En % du PIB · " + XT}])

t = "Et au 3e trimestre, le PIB a reculé de 0,2 %. Récession technique, selon l'Insee."
beat(t, "Et au troisième trimestre, le P.I.B. a encore reculé... Récession technique, selon l'Insee.",
     scr("6"),
     [{"type": "screen_counter", "kicker": "PIB FRANCE · 3E TRIMESTRE 2026", "value_from": 0, "value_to": -0.2, "decimals": 1,
       "prefix": "", "suffix": " %", "color": "red", "pill": "RÉCESSION TECHNIQUE", "desc": "Estimation révisée · Insee · " + XT}])

t = "Alors, qui va payer l'addition ?"
beat(t, "Alors... qui va payer l'addition ?",
     clip("7"),
     [{"type": "bigtitle", "lines": ["QUI VA PAYER", "L'ADDITION ?"], "at_word": 1}])

t = "Lundi, la réaction des marchés, je la suis en direct sur mon Telegram. Lien en bio."
beat(t, t, clip("8"),
     [{"type": "phone", "mode": "mini", "img": "tg_3435c02c_top.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "Selon S&P, sans nouvelles mesures, le déficit serait encore de 5,3 % en 2027. L'objectif du gouvernement : 5 %."
beat(t, "Selon S&P, sans nouvelles mesures, le déficit serait encore de plus de cinq pour cent en deux mille vingt-sept... L'objectif du gouvernement : cinq pour cent.",
     scr("9"),
     [{"type": "screen_duo",
       "a": {"kicker": "DÉFICIT 2027 (S&P)", "value_to": 5.3, "decimals": 1, "prefix": "", "suffix": " %", "color": "red",
             "desc": "Sans mesures supplémentaires · en % du PIB"},
       "b_at_word": w(t, "objectif"),
       "b": {"kicker": "OBJECTIF DU GOUVERNEMENT", "value_to": 5, "decimals": 0, "prefix": "", "suffix": " %", "color": "gold",
             "desc": "Projet de budget 2027 · " + FT}}])

t = "L'écart : environ 10 milliards d'euros à trouver."
beat(t, "L'écart... environ dix milliards d'euros à trouver.",
     scr("10"),
     [{"type": "screen_counter", "kicker": "ÉCART À COMBLER EN 2027", "value_from": 0, "value_to": 10, "decimals": 0,
       "prefix": "≈ ", "suffix": " MDS €", "color": "gold", "pill": "0,3 POINT DE PIB", "desc": FT}])

t = "Et S&P voit les intérêts de la dette grimper jusqu'en 2029."
beat(t, "Et S&P voit les intérêts de la dette grimper jusqu'en deux mille vingt-neuf.",
     clip("11"),
     [{"type": "bigtitle", "lines": ["INTÉRÊTS EN HAUSSE", "JUSQU'EN 2029"], "at_word": w(t, "intérêts")},
      {"type": "source", "text": BR}])

t = "Le vrai risque, selon l'agence : un blocage politique qui durerait après la présidentielle de 2027."
beat(t, "Le vrai risque, selon l'agence... un blocage politique qui durerait après la présidentielle de deux mille vingt-sept.",
     clip("12"),
     [{"type": "news", "at_word": w(t, "blocage"), "left": "S&P · MOTIFS", "right": "27 NOV.", "tag": "POLITIQUE",
       "headline": "Risque élevé que la fragmentation politique persiste après l'élection présidentielle de 2027",
       "highlight": "fragmentation politique", "sub": BR}])

t = "Jeudi, la France empruntait à 10 ans à 4,74 %. L'Allemagne, à 3,25 %."
beat(t, "Jeudi, la France empruntait à dix ans à près de cinq pour cent... L'Allemagne, à un peu plus de trois.",
     scr("13"),
     [{"type": "screen_duo",
       "a": {"kicker": "OAT FRANCE · 10 ANS", "value_to": 4.74, "decimals": 2, "prefix": "", "suffix": " %", "color": "red",
             "desc": "Taux de jeudi 26 nov."},
       "b_at_word": w(t, "Allemagne"),
       "b": {"kicker": "BUND ALLEMAND · 10 ANS", "value_to": 3.25, "decimals": 2, "prefix": "", "suffix": " %", "color": "gold",
             "desc": "Écart ≈ 1,5 point · " + XT}}])

t = "Lundi, les banques du CAC 40 seront surveillées : Crédit Agricole, Société Générale."
beat(t, "Lundi, les banques du CAC quarante seront surveillées... Crédit Agricole, Société Générale.",
     clip("14"),
     [{"type": "tickers", "title": "BANQUES DU CAC 40", "rows": [
        {"key": "ACA", "name": "Crédit Agricole", "pct": "", "up": True, "at_word": w(t, "Crédit")},
        {"key": "GLE", "name": "Société Générale", "pct": "", "up": True, "at_word": w(t, "Société")}]},
      {"type": "source", "text": "XTB · 27 nov. 2026"}])

t = "Le budget 2027 est au Sénat. Roland Lescure réclame un déficit ramené à 5 % au plus."
beat(t, "Le budget deux mille vingt-sept est au Sénat... Roland Lescure réclame un déficit ramené à cinq pour cent au plus.",
     clip("15"),
     [{"type": "news", "at_word": w(t, "Roland"), "left": "BERCY · COMMUNIQUÉ", "right": "27 NOV.", "tag": "CITATION",
       "headline": "« L'absolue nécessité de doter le pays dans les meilleurs délais d'un budget responsable »",
       "highlight": "budget responsable", "sub": "Roland Lescure, ministre de l'Économie · " + BR}])

t = "Et toi, tu crois que la France tiendra ses 5 % ? Dis-le en commentaire."
beat(t, "Et toi, tu crois que la France tiendra ses cinq pour cent ? Dis-le en commentaire.",
     clip("16"),
     [{"type": "bigtitle", "lines": ["5 % EN 2027 :", "TENABLE ?"], "at_word": 3}])

t = ("La prochaine secousse sur la dette française, tu veux la subir ou la voir venir ? Sur mon Telegram gratuit : "
     "l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées et mes opportunités en temps réel. "
     "Plus de 22 000 personnes sont déjà dedans. Le lien est en bio.")
say = ("La prochaine secousse sur la dette française... tu veux la subir, ou la voir venir ? Sur mon Telegram gratuit : "
       "l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées et mes opportunités en temps réel. "
       "Plus de vingt-deux mille personnes sont déjà dedans... Le lien est en bio.")
beat(t, say, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Dette française : ce que S&P change pour toi", "imgs": ["tg_4b2fa9a8.jpg", "tg_1eaa56f0.jpg", "tg_38e4f34b.jpg"],
       "subs": 22760, "subs_at_word": w(t, "22"), "bio_at_word": w(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
     cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "28 novembre 2026", "brand": "Invest Family Fr", "hook_type": "breaking",
        "hook_formula": "chiffre choc",
        "cta_angle": "La prochaine secousse, tu veux la subir ou la voir venir ?",
        "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad",
                  "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.boursorama.com/bourse/actualites/s-p-assortit-la-note-souveraine-de-la-france-d-une-perspective-negative-480ecf2212c42e72497c6bc0bc15ec88",
                    "https://www.francetransactions.com/actus/news-finances/dette-francaise-agence-notation.html",
                    "https://www.xtb.com/fr/analyses-marches/note-france-sp-verdict-27-11-2026"],
        "broll_credits": "broll/credits.json"}
DROP = set(int(x) for x in os.environ.get("DROP", "").split(",") if x)
spec["beats"] = [b for i, b in enumerate(B) if i not in DROP]
json.dump(spec, open(f'{D}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'{D}/voice_text.txt', 'w').write("\n".join(b["say"] for b in spec["beats"]))
print(len(spec["beats"]), "beats,", sum(len(b["say"].split()) for b in spec["beats"]), "mots")
