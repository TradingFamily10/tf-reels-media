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


t = "Séoul a dû freiner d'urgence ce matin… mais pour une hausse."
beat(t, "La Bourse de Séoul a dû freiner d'urgence ce matin... mais pour une hausse.", C("B0"), [
    {"type": "date", "text": "Mardi 10 novembre 2026 · Asie", "until_beat": 1},
    {"type": "breaking", "label": "DERNIÈRES INFOS", "lines": ["SÉOUL FREINE", "SES ACHATS", "EN URGENCE"]},
    {"type": "tickers", "title": "ASIE · OUVERTURE MARDI", "rows": [
        {"name": "Kospi", "pct": "+5,55 %", "at_word": W(t, "freiner")},
        {"name": "Nikkei 225", "pct": "+3,05 %", "at_word": W(t, "matin")},
        {"name": "SoftBank", "pct": "+11,15 %", "at_word": W(t, "hausse"), "key": "SFTBY"}]}])
t = "Et ce n'est pas tout : SoftBank s'envole de plus de 11 % à Tokyo."
beat(t, "Et ce n'est pas tout : SoftBank s'envole de plus de onze pour cent à Tokyo.", C("B1"), [
    {"type": "stock", "key": "SFTBY", "name": "SoftBank Group", "sub": "9984 · Bourse de Tokyo · mardi", "pct": "+11 %", "up": True, "size": "big", "y": 560, "at_word": W(t, "SoftBank")},
    {"type": "source", "text": "TradingKey · investingLive · 10 nov."}])
t = "Vendredi encore, Tokyo et Séoul chutaient de près de 6 %."
beat(t, "Vendredi encore, Tokyo et Séoul chutaient de près de six pour cent.", {"screen": True, "under": C("B2")}, [
    {"type": "screen_counter", "kicker": "TOKYO & SÉOUL · LA SEMAINE DERNIÈRE", "value_from": 0, "value_to": -6, "decimals": 0, "prefix": "≈ ", "suffix": " %", "color": "red", "pill": "LA PANIQUE SUR L'IA", "desc": "Nikkei 225 · Kospi · AP / investingLive", "drop": True}])
t = "La peur : que la victoire démocrate aux midterms freine les data centers de l'IA."
beat(t, "La peur : que la victoire démocrate aux midterms freine les data centers de l'I.A.", C("B3"), [
    {"type": "bigtitle", "lines": ["LA PEUR :", "L'IA FREINÉE ?"], "at_word": W(t, "data")}])
t = "Puis lundi soir, Wall Street a tout renversé."
beat(t, None, C("B4"), [{"type": "bigtitle", "lines": ["WALL STREET", "REBONDIT"], "at_word": W(t, "Wall")}])
t = "Le S&P 500 et le Nasdaq ont bondi de plus de 2 % en une séance."
beat(t, "Le S. and P. cinq cents et le Nasdaq ont bondi de plus de deux pour cent en une séance.", {"screen": True, "under": C("B5")}, [
    {"type": "screen_duo", "a": {"kicker": "S&P 500 · LUNDI", "value_to": 2.35, "decimals": 2, "prefix": "+", "suffix": " %", "color": "green", "desc": "Clôture à 7 549,94 points"},
     "b_at_word": W(t, "Nasdaq"), "b": {"kicker": "NASDAQ · LUNDI", "value_to": 2.74, "decimals": 2, "prefix": "+", "suffix": " %", "color": "green", "desc": "Clôture à 25 253,14 points", "logo": "NDAQ"}},
    {"type": "source", "text": "JournalArta · TradingKey · 9 nov."}])
t = "Et les puces ont explosé : l'indice des semi-conducteurs, près de 7 % en un jour."
beat(t, "Et les puces ont explosé : l'indice des semi-conducteurs... près de sept pour cent en un jour.", {"screen": True, "under": C("B6")}, [
    {"type": "screen_logos", "kicker": "SEMI-CONDUCTEURS · LUNDI", "value_from": 0, "value_to": 6.85, "decimals": 2, "prefix": "+", "suffix": " %", "color": "green", "pill": "INDICE SOX · PHILADELPHIE", "keys": ["AMD", "TSM", "AVGO", "MU", "ASML"], "desc": "AMD · TSMC · Broadcom · Micron · ASML"}])
t = "Alors, qui a rallumé la machine ?"
beat(t, "Alors... qui a rallumé la machine ?", C("B7"), [{"type": "bigtitle", "lines": ["QUI A RALLUMÉ", "LA MACHINE ?"], "at_word": 1}])
t = "Ce rebond, je le décortique en direct sur mon Telegram. Lien en bio."
beat(t, None, {"blur_prev": True}, [{"type": "phone", "mode": "mini", "img": "tg_38e4f34b.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "Réponse : le pétrole, et l'espoir d'une fin de guerre entre Washington et Téhéran."
beat(t, None, C("B9"), [
    {"type": "news", "at_word": W(t, "pétrole"), "left": "ÉTATS-UNIS · IRAN", "right": "10 NOV.", "tag": "CE QUI A TOUT CHANGÉ",
     "headline": "L'espoir d'une fin de guerre fait chuter le pétrole", "highlight": "fin de guerre", "sub": "Diplomatie États-Unis – Iran · médiation du Qatar"},
    {"type": "source", "text": "investingLive · JournalArta"}])
t = "Le Brent retombe vers 92 dollars, contre près de 118 au début du mois."
beat(t, "Le Brent retombe vers quatre-vingt-douze dollars... contre près de cent dix-huit au début du mois.", {"screen": True, "under": C("B10")}, [
    {"type": "screen_counter", "kicker": "BRENT · MARDI 10 NOV.", "value_from": 117.64, "value_to": 92, "decimals": 0, "prefix": "≈ ", "suffix": " $", "color": "red", "pill": "117,64 $ LE 2 NOVEMBRE", "desc": "Baril de Brent · investingLive · JournalArta", "drop": True}])
t = "À Séoul, les géants des puces mémoire s'envolent, et le Kospi prend plus de 4 %."
beat(t, "À Séoul, les géants des puces mémoire s'envolent... et le Kospi prend plus de quatre pour cent.", {"screen": True, "under": C("B11")}, [
    {"type": "tickers", "title": "ASIE · MARDI 10 NOVEMBRE", "rows": [
        {"name": "Kospi", "pct": "+4 à +5,5 %", "at_word": W(t, "Kospi")},
        {"name": "Nikkei 225", "pct": "+2,7 à +3 %", "at_word": 0},
        {"name": "SoftBank", "pct": "+11 %", "at_word": 0, "key": "SFTBY"}]},
    {"type": "source", "text": "TradingKey · investingLive · séance en cours"}])
t = "Mais un géant reste à terre : Nvidia a perdu plus de 4 % lundi."
beat(t, "Mais un géant reste à terre : Nvidia a perdu plus de quatre pour cent lundi.", C("B12"), [
    {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "NVDA · Nasdaq · lundi 9 novembre", "pct": "−4 %", "up": False, "size": "big", "y": 560, "at_word": W(t, "Nvidia"), "strike_at_word": W(t, "perdu")},
    {"type": "source", "text": "SBS · investingLive · JournalArta"}])
t = "Plombé par l'enquête qui vise son propre patron."
beat(t, None, C("B13"), [{"type": "bigtitle", "lines": ["L'ENQUÊTE SUR", "SON PATRON"], "at_word": W(t, "enquête")}])
t = "Et à 14 h 30, tout peut basculer : l'inflation américaine d'octobre tombe aujourd'hui."
beat(t, "Et à quatorze heures trente, tout peut basculer : l'inflation américaine d'octobre tombe aujourd'hui.", C("B14"), [
    {"type": "date", "text": "Aujourd'hui · 14 h 30 (Paris) · inflation US d'octobre"},
    {"type": "bigtitle", "lines": ["14 H 30 :", "INFLATION US"], "at_word": W(t, "inflation")}])
t = "Trop chaude, et la Fed pourrait remonter ses taux en décembre."
beat(t, None, C("B15"), [{"type": "bigtitle", "lines": ["HAUSSE DES TAUX", "EN DÉCEMBRE ?"], "at_word": W(t, "Fed")}])
t = "Alors, vrai rebond… ou simple respiration avant la prochaine chute ? Dis-le-moi en commentaire."
beat(t, "Alors... vrai rebond... ou simple respiration avant la prochaine chute ? Dis-le-moi en commentaire.", {"shots": [C("B16"), {**C("B16b"), "at_word": W(t, "Dis-le-moi")}]}, [
    {"type": "bigtitle", "lines": ["VRAI REBOND…", "OU RESPIRATION ?"], "at_word": 0}])
t = "Pendant que les marchés font les montagnes russes, sur mon Telegram on garde la tête froide. Plus de 22 000 personnes y reçoivent gratuitement l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées et mes opportunités en temps réel. Rejoins la famille, le lien est en bio."
beat(t, "Pendant que les marchés font les montagnes russes... sur mon Telegram, on garde la tête froide. Plus de vingt-deux mille personnes y reçoivent gratuitement l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées, et mes opportunités en temps réel. Rejoins la famille, le lien est en bio.",
     {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Rebond ou piège ? Mon analyse avant l'inflation US de 14 h 30",
     "imgs": ["tg_4b2fa9a8.jpg", "tg_1eaa56f0.jpg", "tg_3435c02c.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "REJOINS LA FAMILLE"}],
    cta="long", endcard={"duration": 1.8, "button": "REJOINS LA FAMILLE", "small": "Telegram gratuit · lien en bio"})

DROP = [int(x) for x in os.environ.get("DROP", "").split(",") if x]
B = [b for i, b in enumerate(B) if i not in DROP]
d = os.path.dirname(os.path.abspath(__file__))
clips = json.load(open(os.path.join(d, "clips.json"))) if os.path.exists(os.path.join(d, "clips.json")) else {}
def sub(bg):
    if isinstance(bg, dict):
        if "clip" in bg and bg["clip"] in clips:
            bg.update(clips[bg["clip"]])
        if "under" in bg: sub(bg["under"])
        for s in bg.get("shots", []): sub(s)
for b in B: sub(b["bg"])
spec = {"id": "ep08_asie_rebond", "date_label": "10 novembre 2026", "brand": "Invest Family Fr", "hook_type": "breaking", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.tradingkey.com/analysis/stocks/more/262297302-japan-korea-stocks-skhy-kospi-nikkei-samsung-skhynix-softbank-kioxia-nvda-sox-cpi-ppi-krx-tradingkey",
 "https://investinglive.com/stock-market-update/nikkei-kospi-extend-rebound-as-ai-and-chip-stocks-surge-recouping-friday-s-rout/",
 "https://journalarta.com/en/2026/11/10/asia-markets-today-nikkei-225-surges-and-asx-200-climbs-after-wall-streets-2-35-jump/",
 "https://news.sbs.co.kr/english/article.do?news_id=N1008838924",
 "https://www.wsls.com/business/2026/11/09/asian-markets-bounce-back-after-a-recovery-for-ai-stocks-on-wall-street/"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
