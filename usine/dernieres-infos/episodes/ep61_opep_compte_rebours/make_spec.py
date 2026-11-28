import json, sys, os
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep61_opep_compte_rebours'
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
FB = "Forbes · 27 nov. 2026, 11 h 29 (Paris)"
AD = "Admirals (Reuters, Bloomberg) · 27 nov. 2026"
HS = "House of Saud (OPEP, Bloomberg) · 26 nov. 2026"
IC = "ICIS · 25 nov. 2026"
RT = "Rio Times · 26 nov. 2026"
YF = "Yahoo Finance · 27 nov. 2026"

t = "24 heures. C'est le temps qu'il reste avant que 21 pays décident de leur pétrole pour 2027."
beat(t, "Vingt-quatre heures... C'est le temps qu'il reste avant que vingt-et-un pays décident de leur pétrole pour deux mille vingt-sept.",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "avant"))]},
     [{"type": "hook_bignum", "value_to": 24, "prefix": "", "suffix": " H", "unit": "OPEP+ · DIMANCHE 29/11", "label": "21 pays · quotas 2027 · Vienne",
       "logos": ["ARAMCO", "XOM", "TTE", "SHEL", "CVX", "BP"], "reveal_at_word": w(t, "avant"), "count_dur": 1.1}])

t = "Et ce n'est pas le pire : après le 31 décembre, plus aucun quota n'est en vigueur."
beat(t, "Et ce n'est pas le pire... après le trente-et-un décembre, plus aucun quota n'est en vigueur.", clip("1"),
     [{"type": "bigtitle", "lines": ["APRÈS LE 31 DÉCEMBRE", "AUCUN QUOTA"], "at_word": w(t, "après")},
      {"type": "source", "text": HS}])

t = "Fin octobre, le Brent frôlait 118 dollars."
beat(t, "Fin octobre, le Brent frôlait cent dix-huit dollars.", scr("2"),
     [{"type": "screen_counter", "kicker": "BRENT · CLÔTURE DU 30 OCTOBRE", "value_from": 90, "value_to": 118, "decimals": 0, "prefix": "≈ ", "suffix": " $",
       "color": "gold", "pill": "PLUS HAUT DEPUIS AVRIL", "desc": "Reuters, cité par " + AD}])

t = "En novembre, il a perdu près de 20 %. Vendredi, il tournait autour de 90 dollars."
beat(t, "En novembre, il a perdu près de vingt pour cent... Vendredi, il tournait autour de quatre-vingt-dix dollars.", scr("3"),
     [{"type": "screen_duo", "a": {"kicker": "BRENT · NOVEMBRE (AU 20/11)", "value_to": -20, "decimals": 0, "prefix": "≈ ", "suffix": " %", "color": "red", "desc": "Trading Economics, cité par Admirals"},
       "b_at_word": w(t, "Vendredi"), "b": {"kicker": "BRENT · VEN. 27 NOV.", "value_to": 90, "decimals": 0, "prefix": "≈ ", "suffix": " $", "color": "red", "desc": "En séance · " + YF}}])

t = "La raison : trop de pétrole. Selon l'AIE, l'offre dépasse la demande de 1,7 million de barils par jour ce trimestre."
beat(t, "La raison... trop de pétrole. Selon l'Agence internationale de l'énergie, l'offre dépasse la demande d'un million sept cent mille barils par jour ce trimestre.",
     {"shots": [clip("4"), dict(clip("4b"), at_word=w(t, "Selon"))]},
     [{"type": "news", "at_word": w(t, "Selon"), "left": "AIE · RAPPORT DE NOVEMBRE", "right": "T4 2026", "tag": "EXCÉDENT",
       "headline": "L'offre mondiale dépasserait la demande de 1,7 million de barils par jour au 4e trimestre 2026",
       "highlight": "1,7 million de barils", "sub": IC}])

t = "Le premier excédent depuis le début de la guerre entre les États-Unis et l'Iran, fin février."
beat(t, "Le premier excédent depuis le début de la guerre entre les États-Unis et l'Iran, fin février.", clip("5"),
     [{"type": "bigtitle", "lines": ["1ER EXCÉDENT", "DEPUIS FÉVRIER"], "at_word": w(t, "premier")},
      {"type": "source", "text": IC}])

t = "Alors, qui va fermer le robinet ?"
beat(t, "Alors... qui va fermer le robinet ?", clip("6"),
     [{"type": "bigtitle", "lines": ["QUI VA FERMER", "LE ROBINET ?"], "at_word": 1}])

t = "Le verdict de dimanche, je le décortique en direct sur mon Telegram. Lien en bio."
beat(t, "Le verdict de dimanche, je le décortique en direct sur mon Telegram. Lien en bio.", clip("7"),
     [{"type": "phone", "mode": "mini", "img": "tg_3435c02c_top.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "Scénario le plus probable selon Reuters : personne. Les quotas resteraient inchangés au moins jusqu'à fin mars."
beat(t, "Scénario le plus probable selon Reuters... personne. Les quotas resteraient inchangés, au moins jusqu'à fin mars.",
     {"shots": [clip("8"), dict(clip("8b"), at_word=w(t, "quotas"))]},
     [{"type": "news", "at_word": w(t, "Reuters"), "left": "OPEP+ · AVANT LA RÉUNION", "right": "27 NOV.", "tag": "SCÉNARIO",
       "headline": "L'OPEP+ devrait garder ses objectifs de production inchangés au moins jusqu'à la fin du 1er trimestre 2027",
       "highlight": "inchangés", "sub": "Deux sources proches des discussions · " + AD}])

t = "Car en coulisses, les membres se déchirent."
beat(t, "Car en coulisses... les membres se déchirent.", clip("9"),
     [{"type": "bigtitle", "lines": ["EN COULISSES", "ILS SE DÉCHIRENT"], "at_word": w(t, "membres")}])

t = "L'Irak réclame une base de 6 millions de barils par jour. Son quota actuel : 4,4 millions."
beat(t, "L'Irak réclame une base de six millions de barils par jour... Son quota actuel ? À peine plus de quatre millions.", scr("10"),
     [{"type": "screen_duo", "a": {"kicker": "IRAK · BASE RÉCLAMÉE 2027", "value_to": 6, "decimals": 0, "prefix": "", "suffix": " M b/j", "color": "gold", "desc": "Bloomberg, cité par House of Saud"},
       "b_at_word": w(t, "quota"), "b": {"kicker": "IRAK · QUOTA ACTUEL", "value_to": 4.4, "decimals": 1, "prefix": "", "suffix": " M b/j", "color": "red", "desc": "4,431 M b/j · capacité estimée par l'AIE : ≈ 4,9"}}])

t = "Riyad déclare 10,6 millions de barils en octobre. Les observateurs de l'OPEP n'en comptent que 9,2."
beat(t, "Riyad déclare plus de dix millions et demi de barils en octobre... Les observateurs de l'OPEP n'en comptent qu'un peu plus de neuf.",
     scr("11"),
     [{"type": "screen_duo", "a": {"kicker": "ARABIE SAOUDITE · DÉCLARÉ (OCT.)", "value_to": 10.6, "decimals": 1, "prefix": "", "suffix": " M b/j", "color": "gold", "desc": "Chiffre officiel de Riyad : 10,563", "logo": "ARAMCO"},
       "b_at_word": w(t, "observateurs"), "b": {"kicker": "SOURCES SECONDAIRES OPEP", "value_to": 9.2, "decimals": 1, "prefix": "", "suffix": " M b/j", "color": "red", "desc": "9,194 M b/j · écart de 1,369 M b/j"}},
      {"type": "source", "text": HS}])

t = "Et les Émirats ne sont plus à la table : ils ont quitté l'OPEP le 1er mai."
beat(t, "Et les Émirats ne sont plus à la table : ils ont quitté l'OPEP le premier mai.", clip("12"),
     [{"type": "news", "at_word": w(t, "Émirats"), "left": "OPEP+ · 21 PAYS", "right": "1ER MAI 2026", "tag": "DÉPART",
       "headline": "Les Émirats arabes unis ont quitté l'OPEP et l'OPEP+ le 1er mai 2026, annoncé le 28 avril",
       "highlight": "quitté l'OPEP", "sub": RT + " · " + AD}])

t = "Pour 2027, l'AIE voit déjà un surplus de 3,8 millions de barils par jour."
beat(t, "Pour deux mille vingt-sept, l'Agence internationale de l'énergie voit déjà un surplus de près de quatre millions de barils par jour.", scr("13"),
     [{"type": "screen_counter", "kicker": "SURPLUS MONDIAL ATTENDU EN 2027", "value_from": 0, "value_to": 3.8, "decimals": 1, "prefix": "", "suffix": " M b/j",
       "color": "red", "pill": "PRÉVISION AIE", "desc": "S&P Global, cité par Admirals · House of Saud"}])

t = "Aramco, TotalEnergies, Exxon, Shell : tous suspendus à cette décision."
beat(t, "Aramco, TotalEnergies, Exxon, Shell : tous suspendus à cette décision.", clip("14"),
     [{"type": "tickers", "title": "LES MAJORS DU PÉTROLE", "rows": [
        {"key": "ARAMCO", "name": "Saudi Aramco", "pct": "", "up": True, "at_word": 0},
        {"key": "TTE", "name": "TotalEnergies", "pct": "", "up": True, "at_word": w(t, "TotalEnergies")},
        {"key": "XOM", "name": "ExxonMobil", "pct": "", "up": True, "at_word": w(t, "Exxon")},
        {"key": "SHEL", "name": "Shell", "pct": "", "up": True, "at_word": w(t, "Shell")}]}])

t = "Goldman Sachs voit le Brent à 78 dollars fin 2027. Verdict dimanche, à Vienne."
beat(t, "Goldman Sachs voit le Brent à soixante-dix-huit dollars fin deux mille vingt-sept... Verdict dimanche, à Vienne.",
     {"shots": [scr("15"), dict(clip("15b"), at_word=w(t, "Verdict"))]},
     [{"type": "screen_counter", "kicker": "BRENT · PRÉVISION GOLDMAN SACHS", "value_from": 90, "value_to": 78, "decimals": 0, "prefix": "", "suffix": " $",
       "color": "red", "pill": "DÉCEMBRE 2027", "desc": "Note du 15 nov. 2026 · Admirals · House of Saud", "until_word": w(t, "Verdict")},
      {"type": "date", "text": "Dimanche 29 novembre · Vienne · OPEP+", "at_word": w(t, "Verdict")}])

t = "Et toi, tu vois le baril sous les 80 dollars l'an prochain ? Dis-le en commentaire."
beat(t, "Et toi, tu vois le baril sous les quatre-vingts dollars l'an prochain ? Dis-le en commentaire.", clip("16"),
     [{"type": "bigtitle", "lines": ["SOUS 80 $", "EN 2027 ?"], "at_word": w(t, "baril")}])

t = ("Dimanche soir, pendant que tout le monde attendra les gros titres de lundi, mes abonnés auront déjà l'analyse. Sur mon Telegram gratuit : "
     "l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées et mes opportunités en temps réel. Plus de 22 000 personnes nous ont rejoints. Le lien est en bio.")
s = ("Dimanche soir, pendant que tout le monde attendra les gros titres de lundi... mes abonnés auront déjà l'analyse. Sur mon Telegram gratuit : "
     "l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées et mes opportunités en temps réel. Plus de vingt-deux mille personnes nous ont rejoints... Le lien est en bio.")
beat(t, s, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "OPEP+ : ce qui a été décidé à Vienne", "imgs": ["tg_38e4f34b.jpg", "tg_4b2fa9a8.jpg", "tg_1eaa56f0.jpg"], "subs": 22760,
       "subs_at_word": w(t, "personnes"), "bio_at_word": w(t, "bio"), "button": "ACCÈS GRATUIT"}],
     cta="long", endcard={"duration": 1.8, "button": "ACCÈS GRATUIT", "small": "Telegram gratuit · lien en bio"})

spec = {"id": EP, "date_label": "28 novembre 2026", "brand": "Invest Family Fr", "hook_type": "bignum", "hook_formula": "compte à rebours",
        "cta_angle": "Dimanche soir, pendant que tout le monde attendra les gros titres de lundi, mes abonnés auront déjà l'analyse", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://admiralmarkets.com/analytics/traders-blog/opec-meeting-november-29-2026-preview",
                    "https://houseofsaud.com/opec-nov29-2027-quotas/",
                    "https://www.icis.com/explore/resources/news/2026/11/25/11243387/oil-falls-on-supply-glut-concerns-eyes-on-29-nov-opec-meeting/",
                    "https://www.riotimesonline.com/opec-plus-weighs-january-oil-quota-rollover-2026",
                    "https://finance.yahoo.com/markets/live/stock-market-today-firday-november-27-dow-sp-500-nasdaq-black-friday-holiday-091152065.html"],
        "beats": B}
DROP = {5, 9, 12, 13}
spec["beats"] = [b for i, b in enumerate(B) if i not in DROP]; B = spec["beats"]
json.dump(spec, open(f'{D}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'{D}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), "beats", sum(len(b["say"].split()) for b in B), "mots")
