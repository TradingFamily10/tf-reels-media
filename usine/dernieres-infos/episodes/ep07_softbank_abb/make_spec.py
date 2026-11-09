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

t = "5,4 milliards de dollars. Et Pékin vient de dire non."
beat(t, "Cinq virgule quatre milliards de dollars... Et Pékin vient de dire non.", C("B0"), [
    {"type": "date", "text": "Jeudi 5 novembre 2026", "until_beat": 1},
    {"type": "hook_bignum", "value_to": 5400, "unit": "MILLIONS DE $", "label": "bloqués par Pékin", "logos": ["SFTBY", "ABB", "SFTBY", "ABB"], "reveal_at_word": W(t, "Pékin"), "count_dur": 1.0}])
t = "Tout le monde regarde Nvidia. Le vrai choc de la semaine est ailleurs."
beat(t, None, C("B1"), [{"type": "bigtitle", "lines": ["LE VRAI CHOC", "EST AILLEURS"], "at_word": W(t, "vrai")}])
t = "Jeudi, la Chine a interdit le rachat des robots industriels d'ABB par le japonais SoftBank."
beat(t, "Jeudi, la Chine a interdit le rachat des robots industriels d'A.B.B. par le japonais SoftBank.", C("B2"), [
    {"type": "news", "at_word": W(t, "interdit"), "left": "CHINE", "right": "5 NOV.", "tag": "SÉCURITÉ DES INVESTISSEMENTS",
     "headline": "Pékin bloque le rachat d'ABB Robotics par SoftBank", "highlight": "bloque", "sub": "Contrat signé · bouclage prévu avant la fin de l'année"},
    {"type": "stock", "key": "ABB", "name": "ABB", "sub": "ABBN · Bourse de Zurich", "size": "big", "y": 1480, "at_word": W(t, "ABB")},
    {"type": "source", "text": "Silicon Republic · Briefs (FT)"}])
t = "Problème : la Chine, c'est plus de 90 % de la demande de cette activité. Et environ 7 000 salariés."
beat(t, "Problème : la Chine, c'est plus de quatre-vingt-dix pour cent de la demande de cette activité... Et environ sept mille salariés.",
     {"screen": True, "under": C("B3")}, [
    {"type": "screen_duo", "a": {"kicker": "DEMANDE VENUE DE CHINE", "value_to": 90, "prefix": "+ de ", "suffix": " %", "color": "gold", "desc": "ABB Robotics", "logo": "ABB"},
     "b_at_word": W(t, "7"), "b": {"kicker": "SALARIÉS", "value_to": 7000, "prefix": "≈ ", "suffix": "", "color": "white", "desc": "Suède · États-Unis · Chine", "logo": "ABB"}},
    {"type": "source", "text": "Silicon Republic · Briefs"}])
t = "Avec un grand site à Shanghai, soutenu par les autorités chinoises."
beat(t, None, C("B4"), [{"type": "bigtitle", "lines": ["SHANGHAI", "SITE CLÉ"], "at_word": W(t, "Shanghai")}])
t = "Alors pourquoi bloquer un accord déjà validé par la concurrence chinoise en février ?"
beat(t, "Alors... pourquoi bloquer un accord déjà validé par la concurrence chinoise en février ?", C("B5"), [
    {"type": "bigtitle", "lines": ["POURQUOI", "BLOQUER ?"], "at_word": W(t, "pourquoi")}])
t = "Cette guerre des robots, je la suis en direct sur mon Telegram. Lien en bio."
beat(t, None, {"blur_prev": True}, [{"type": "phone", "mode": "mini", "img": "tg_1eaa56f0.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "La réponse : les données. Pékin craint de voir des actifs et des données partir au Japon."
beat(t, None, C("B7"), [
    {"type": "news", "at_word": W(t, "Pékin"), "left": "SELON LE FT", "right": "DONNÉES", "tag": "LA CRAINTE DE PÉKIN",
     "headline": "Des actifs et des données envoyés au Japon", "highlight": "données", "sub": "Pour entraîner des modèles d'IA · selon le Financial Times"}])
t = "Pour entraîner des modèles d'IA… y compris chez OpenAI, dans le portefeuille de SoftBank."
beat(t, "Pour entraîner des modèles d'I.A.... y compris chez OpenAI, dans le portefeuille de SoftBank.", C("B8"), [
    {"type": "stock", "key": "SFTBY", "name": "SoftBank Group", "sub": "9984 · Bourse de Tokyo · actionnaire d'OpenAI", "size": "big", "y": 560, "at_word": W(t, "SoftBank")}])
t = "Vendredi, en pleine tempête sur la tech, SoftBank a plongé de 11 % à Tokyo."
beat(t, "Vendredi, en pleine tempête sur la tech, SoftBank a plongé de onze pour cent à Tokyo.", C("B9"), [
    {"type": "stock", "key": "SFTBY", "name": "SoftBank Group", "sub": "9984 · Tokyo · vendredi 6 novembre", "pct": "−11 %", "up": False, "size": "big", "y": 560, "at_word": W(t, "SoftBank")},
    {"type": "source", "text": "Briefs · 7 novembre 2026"}])
t = "Et ce lundi, il perd encore 4 %… pendant que TSMC s'envole et que Tokyo rebondit."
beat(t, "Et ce lundi, il perd encore quatre pour cent... pendant que T.S.M.C. s'envole et que Tokyo rebondit.", {"screen": True, "under": C("B10")}, [
    {"type": "tickers", "title": "ASIE · LUNDI 9 NOVEMBRE", "rows": [
        {"name": "SoftBank", "pct": "−4,2 %", "at_word": 0, "key": "SFTBY"},
        {"name": "TSMC", "pct": "+4,7 %", "at_word": W(t, "TSMC"), "key": "TSM"},
        {"name": "Nikkei 225", "pct": "+2,3 %", "at_word": W(t, "Tokyo")}]},
    {"type": "source", "text": "AP · Boston Globe · 9 novembre"}])
t = "ABB perd plus de 5 % sur la semaine. Et selon Citi, sa force de frappe est coupée de moitié."
beat(t, "A.B.B. perd plus de cinq pour cent sur la semaine... Et selon Citi, sa force de frappe est coupée de moitié.",
     {"screen": True, "under": C("B11")}, [
    {"type": "screen_duo", "a": {"kicker": "ABB SUR LA SEMAINE", "value_to": 5, "prefix": "− ", "suffix": " %", "color": "red", "desc": "Plus de 5 % de baisse · Zurich", "logo": "ABB"},
     "b_at_word": W(t, "Citi"), "b": {"kicker": "TRÉSOR POUR RACHETER", "value_to": 5, "prefix": "≈ ", "suffix": " Md$", "color": "gold", "desc": "Coupé de moitié, selon Citi", "logo": "ABB"}},
    {"type": "source", "text": "Briefs · Citigroup"}])
t = "Plan B : isoler l'activité chinoise… ou revendre ailleurs, pour 2 à 3 milliards seulement."
beat(t, "Plan B : isoler l'activité chinoise... ou revendre ailleurs, pour deux à trois milliards seulement.",
     {"shots": [C("B12"), {**C("B12b"), "at_word": W(t, "revendre")}]}, [
    {"type": "news", "at_word": W(t, "isoler"), "left": "PLAN B", "right": "ABB · SOFTBANK", "tag": "CE QUI SE PRÉPARE",
     "headline": "Isoler la Chine… ou revendre 2 à 3 Md$", "highlight": "2 à 3 Md$", "sub": "Contre 5,4 Md$ prévus · rien n'est garanti"}])
t = "Le message de Pékin est limpide : ses robots, ses usines et ses données restent chez lui."
beat(t, None, C("B13"), [{"type": "bigtitle", "lines": ["ROBOTS, USINES, DONNÉES", "RESTENT EN CHINE"], "at_word": W(t, "robots")}])
t = "Et dès demain, l'inflation américaine peut encore secouer toute la tech."
beat(t, "Et dès demain, l'inflation américaine peut encore secouer toute la tech.", C("B14"), [
    {"type": "date", "text": "Mardi 10 novembre · inflation US d'octobre"},
    {"type": "bigtitle", "lines": ["DEMAIN :", "L'INFLATION US"], "at_word": W(t, "inflation")}])
t = "Simple bras de fer… ou début d'une guerre des robots ? Dis-le-moi en commentaire."
beat(t, "Simple bras de fer... ou début d'une guerre des robots ? Dis-le-moi en commentaire.", {"shots": [C("B15"), {**C("B15b"), "at_word": W(t, "Dis-le-moi")}]}, [
    {"type": "bigtitle", "lines": ["SIMPLE BRAS DE FER…", "OU GUERRE ?"], "at_word": 0}])
t = "Ce que je viens de te montrer, mes abonnés l'ont lu avant tout le monde. Sur mon Telegram gratuit, plus de 22 000 personnes reçoivent l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées et mes opportunités en temps réel. Lien en bio."
beat(t, "Ce que je viens de te montrer... mes abonnés l'ont lu avant tout le monde. Sur mon Telegram gratuit, plus de vingt-deux mille personnes reçoivent l'actu géopolitique et financière décortiquée, des analyses d'actions détaillées, et mes opportunités en temps réel. Lien en bio.",
     {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Chine, SoftBank, ABB : qui gagne la guerre des robots ?",
     "imgs": ["tg_3435c02c.jpg", "tg_38e4f34b.jpg", "tg_4b2fa9a8.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "ACCÈS GRATUIT"}],
    cta="long", endcard={"duration": 1.8, "button": "ACCÈS GRATUIT", "small": "Telegram gratuit · lien en bio"})

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
spec = {"id": "ep07_softbank_abb", "date_label": "9 novembre 2026", "brand": "Invest Family Fr", "hook_type": "bignum", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.siliconrepublic.com/business/china-softbank-abb-robotics-japan-data-ai-investment",
                    "https://www.briefs.co/news/softbank-and-abb-weigh-china-carve-out-after-beijing-blocks/",
                    "https://www.bostonglobe.com/2026/11/09/business/world-markets-bounce-back-recovery-ai-stocks-wall-street/",
                    "https://finance.yahoo.com/markets/stocks/articles/us-stock-futures-mixed-investors-095952467.html",
                    "https://www.bloomberg.com/news/articles/2026-11-05/china-blocks-softbank-s-acquisition-of-abb-industrial-robot-unit"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
