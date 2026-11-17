import json, sys, os
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
def W(text, word, n=0):
    t = tokens(text); hits = [i for i, w in enumerate(t) if word in w]
    return hits[n]
B = []
def beat(text, say=None, bg=None, ov=None, **kw):
    b = {"text": text}
    if say: b["say"] = say
    b["bg"] = bg or {}; b["overlays"] = ov or []; b.update(kw); B.append(b); return text
C = lambda clip, ss=1, cx=0.5, **k: dict(clip=clip, ss=ss, cx=cx, **k)

INV = "Investing.com · 17 nov. 2026"
AFP = "AFP (Yahoo Finance, Blick) · 17 nov. 2026"
RT = "Reuters via Investing.com · 17 nov. 2026"
NQ = "Newsquawk · 17 nov. 2026"

t = "15 millions de documents internes. Et Deutsche Bank plonge en Bourse."
beat(t, "Quinze millions de documents internes... Et Deutsche Bank plonge en Bourse.", {"shots": [C("B0"), {**C("B0b"), "at_word": W(t, "Deutsche")}]}, [
    {"type": "date", "text": "Mardi 17 novembre 2026 · Francfort", "until_beat": 0},
    {"type": "breaking", "label": "DERNIÈRES INFOS", "lines": ["15 MILLIONS", "DE DOCUMENTS", "ONT FUITÉ"]},
    {"type": "stock", "key": "DB", "name": "Deutsche Bank", "sub": "DBK · Francfort · −5,2 %", "y": 560, "at_word": W(t, "Deutsche")}])
t = "Ce mardi matin, l'action recule de plus de 5 %."
beat(t, "Ce mardi matin, l'action recule de plus de cinq pour cent.", {"screen": True, "under": C("B1")}, [
    {"type": "screen_counter", "kicker": "DEUTSCHE BANK · 17 NOV.", "value_from": 0, "value_to": -5.2, "decimals": 1, "prefix": "", "suffix": " %", "color": "red",
     "pill": "31,22 € · FRANCFORT", "desc": INV + " · près de −6 % après l'ouverture (AFP)"}])
t = "Et ce n'est pas le pire : plus de 200 journalistes de 50 médias ont épluché ces fichiers."
beat(t, "Et ce n'est pas le pire : plus de deux cents journalistes de cinquante médias... ont épluché ces fichiers.", {"screen": True, "under": C("B2")}, [
    {"type": "screen_duo",
     "a": {"kicker": "JOURNALISTES", "value_to": 200, "decimals": 0, "prefix": "+", "suffix": "", "color": "gold", "desc": AFP},
     "b_at_word": W(t, "50"),
     "b": {"kicker": "MÉDIAS", "value_to": 50, "decimals": 0, "prefix": "+", "suffix": "", "color": "gold", "desc": "Der Spiegel · FT · Le Monde · NYT · " + AFP}}])
t = "Alors, qu'y a-t-il dans ces fichiers pour faire trembler le géant bancaire allemand ?"
beat(t, "Alors... qu'y a-t-il dans ces fichiers pour faire trembler le géant bancaire allemand ?", C("B4"), [
    {"type": "bigtitle", "lines": ["QUE CONTIENNENT", "CES FICHIERS ?"], "at_word": W(t, "fichiers")}])
t = "D'abord la Russie : fin 2020, la banque voulait gonfler ses revenus tirés de riches clients russes."
beat(t, "D'abord la Russie : fin deux mille vingt, la banque voulait gonfler ses revenus tirés de riches clients russes.", {"shots": [C("B5"), {**C("B5b"), "at_word": W(t, "riches")}]}, [
    {"type": "news", "at_word": W(t, "2020"), "left": "DEUTSCHE BANK · RUSSIE", "right": "FIN 2020", "tag": "RÉVÉLATION",
     "headline": "Objectif : accroître fortement les revenus tirés de riches clients russes, malgré les alertes", "highlight": "riches clients russes", "sub": "Financial Times via " + AFP}])
t = "Et son retrait de Russie n'est toujours pas terminé : 162 salariés sur place l'an dernier."
beat(t, "Et son retrait de Russie n'est toujours pas terminé : cent soixante-deux salariés sur place l'an dernier.", {"screen": True, "under": C("B6")}, [
    {"type": "screen_duo",
     "a": {"kicker": "SALARIÉS EN RUSSIE", "value_to": 162, "decimals": 0, "prefix": "", "suffix": "", "color": "gold", "desc": "L'an dernier · " + AFP},
     "b_at_word": W(t, "salariés"),
     "b": {"kicker": "BÉNÉFICE AVANT IMPÔTS", "value_to": 61, "decimals": 0, "prefix": "", "suffix": " M€", "color": "gold", "desc": "Filiale russe · " + AFP}}])
t = "Cette affaire, je la suis en direct sur mon Telegram. Lien en bio."
beat(t, None, C("B7"), [
    {"type": "phone", "mode": "mini", "img": "tg_3435c02c.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "Autre révélation : en 2017, un lien envoyé par erreur a exposé les données fiscales de 1 586 comptes."
beat(t, "Autre révélation : en deux mille dix-sept, un lien envoyé par erreur a exposé les données fiscales... de près de mille six cents comptes.", {"screen": True, "under": C("B8")}, [
    {"type": "screen_counter", "kicker": "FUITE INTERNE · 2017", "value_from": 0, "value_to": 1586, "decimals": 0, "prefix": "", "suffix": "", "color": "gold",
     "pill": "COMPTES · DONNÉES FISCALES EXPOSÉES", "desc": AFP}])
t = "Dont trois liés à Donald Trump, qui devait alors à la banque environ 331 millions de dollars."
beat(t, "Dont trois liés à Donald Trump... qui devait alors à la banque environ trois cent trente millions de dollars.", {"screen": True, "under": C("B9")}, [
    {"type": "screen_counter", "kicker": "DETTE DE TRUMP · 2016", "value_from": 0, "value_to": 331, "decimals": 0, "prefix": "≈ ", "suffix": " M$", "color": "gold",
     "pill": "3 COMPTES CONCERNÉS", "desc": "Selon l'enquête · " + AFP}])
t = "Et près de 600 millions de dollars d'opérations avec Jeffrey Epstein."
beat(t, "Et près de six cents millions de dollars d'opérations... avec Jeffrey Epstein.", {"screen": True, "under": C("B10")}, [
    {"type": "screen_counter", "kicker": "OPÉRATIONS EPSTEIN", "value_from": 0, "value_to": 600, "decimals": 0, "prefix": "≈ ", "suffix": " M$", "color": "red",
     "pill": "SELON L'ENQUÊTE", "desc": AFP}])
t = "La banque répond : des faits anciens, et 7 milliards d'euros investis dans ses contrôles depuis 2019."
beat(t, "La banque répond : des faits anciens... et sept milliards d'euros investis dans ses contrôles depuis deux mille dix-neuf.", C("B11"), [
    {"type": "stock", "key": "DB", "name": "Deutsche Bank", "sub": "« Une banque différente aujourd'hui »", "y": 520, "at_word": 0, "until_word": W(t, "anciens")},
    {"type": "news", "at_word": W(t, "7"), "left": "DEUTSCHE BANK · RÉPONSE", "right": "17 NOV.", "tag": "CITATION",
     "headline": "7 milliards d'euros investis dans les contrôles entre 2019 et 2025, pas d'impact financier significatif attendu", "highlight": "7 milliards d'euros", "sub": AFP + " · " + INV}])
t = "Subprimes, Libor : le marché, lui, se souvient des milliards d'amendes."
beat(t, "Subprimes, Libor... le marché, lui, se souvient des milliards d'amendes.", C("B12"), [
    {"type": "tickers", "title": "LES AMENDES DU PASSÉ", "rows": [
        {"name": "Subprimes · 2017", "pct": "7,2 Md$", "at_word": W(t, "Subprimes"), "key": "DB", "up": False},
        {"name": "Libor · 2015", "pct": "> 2 Md€", "at_word": W(t, "Libor"), "key": "DB", "up": False}]},
    {"type": "source", "text": AFP}])
t = "Et toute l'Europe recule aussi, plombée par la tech."
beat(t, "Et toute l'Europe recule aussi... plombée par la tech.", {"screen": True, "under": C("B13")}, [
    {"type": "screen_counter", "kicker": "STOXX 600 · 17 NOV.", "value_from": 0, "value_to": -0.64, "decimals": 2, "prefix": "", "suffix": " %", "color": "red",
     "pill": "658 POINTS", "desc": "Restrictions américaines sur les puces · " + INV}])
t = "Prochain test ce soir : Nvidia publie ses résultats après la clôture de Wall Street."
beat(t, "Prochain test ce soir : Nvidia publie ses résultats après la clôture de Wall Street.", C("B14"), [
    {"type": "tickers", "title": "À SURVEILLER CE SOIR", "rows": [
        {"name": "Nvidia · résultats", "pct": "MAR. SOIR", "at_word": W(t, "Nvidia"), "key": "NVDA", "up": True},
        {"name": "Deutsche Bank · réactions", "pct": "À SUIVRE", "at_word": W(t, "clôture"), "key": "DB", "up": False}]},
    {"type": "source", "text": NQ}])
t = "Alors, vieilles histoires… ou vraie menace pour Deutsche Bank ? Dis-le en commentaire."
beat(t, "Alors... vieilles histoires... ou vraie menace pour Deutsche Bank ? Dis-le en commentaire.", C("B15"), [
    {"type": "bigtitle", "lines": ["VIEILLES HISTOIRES", "OU VRAIE MENACE ?"], "at_word": W(t, "vieilles")}])
t = "Les banques ont leurs archives. Moi, je lis entre les lignes. Sur mon canal Telegram gratuit : l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées et les opportunités en temps réel. Plus de 22 000 personnes sont déjà avec nous. Lien en bio."
beat(t, "Les banques ont leurs archives. Moi, je lis entre les lignes. Sur mon canal Telegram gratuit : l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées et les opportunités en temps réel. Plus de vingt-deux mille personnes sont déjà avec nous. Lien en bio.", {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Deutsche Bank −5 % : ce que contient la fuite",
     "imgs": ["tg_4b2fa9a8.jpg", "tg_38e4f34b.jpg", "tg_1eaa56f0.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
    cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})
d = os.path.dirname(os.path.abspath(__file__))
clips = json.load(open(os.path.join(d, "clips.json"))) if os.path.exists(os.path.join(d, "clips.json")) else {}
def sub(bg):
    if isinstance(bg, dict):
        if "clip" in bg and bg["clip"] in clips: bg.update(clips[bg["clip"]])
        if "under" in bg: sub(bg["under"])
        for s in bg.get("shots", []): sub(s)
for b in B: sub(b["bg"])
spec = {"id": "ep29_deutsche_fuite", "date_label": "17 novembre 2026", "brand": "Invest Family Fr", "hook_type": "breaking", "hook_formula": "chiffre choc",
        "cta_angle": "Les banques ont leurs archives, moi je lis entre les lignes", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.investing.com/news/stock-market-news/deutsche-bank-shares-fall-5-as-it-defends-itself-from-media-reports-based-on-leaks-5031884",
 "https://wtaq.com/2026/11/17/deutsche-bank-shares-fall-5-as-it-defends-itself-from-media-reports-based-on-leaks/",
 "https://fr.finance.yahoo.com/actualites/russie-trump-epstein-fuite-massive-082457960.html",
 "https://www.blick.ch/fr/economie/trump-epstein-fuite-de-donnees-chez-deutsche-bank/wtcxhxc",
 "https://www.tradingsat.com/deutsche-bank-DE0005140008/actualites/deutsche-bank-elle-voulait-gagner-toujours-plus-d-argent-avec-les-riches-russes-la-tres-embarrassante-enquete-qui-fait-chuter-deutsche-bank-en-bourse-1173905.html",
 "https://fr.investing.com/news/stock-market-news/pourquoi-laction-deutsche-bank-chutetelle-aujourdhui--93CH-3699636",
 "https://www.newsquawk.com/headlines/newsquawk-daily-european-opening-news---17th-november-2026"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
open(os.path.join(d, "voice_text.txt"), "w").write("\n".join(b.get("say") or b["text"] for b in B))
