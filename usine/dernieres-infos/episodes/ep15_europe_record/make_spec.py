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

t = "Pourquoi la Bourse européenne frôle-t-elle son record… pendant que Nvidia s'effondre ?"
beat(t, "Pourquoi la Bourse européenne frôle-t-elle son record... pendant que Nvidia s'effondre ?", C("B0"), [
    {"type": "date", "text": "Jeudi 12 novembre 2026 · fin de matinée", "until_beat": 1},
    {"type": "bigtitle", "lines": ["L'EUROPE AU RECORD,", "NVIDIA À TERRE ?"], "at_word": 0},
    {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "NVDA · avant-Bourse · Reuters", "pct": "−6,9 %", "up": False, "y": 1420, "at_word": W(t, "Nvidia")}])
t = "Mercredi soir, le Stoxx 600 a fini à moins d'un point de son record d'août."
beat(t, "Mercredi soir, le Stoxx six cents a fini à moins d'un point de son record d'août.", {"screen": True, "under": C("B1")}, [
    {"type": "screen_counter", "kicker": "STOXX 600 · ÉCART AU RECORD", "value_from": 10, "value_to": 0.6, "decimals": 1, "prefix": "", "suffix": " pt", "color": "gold",
     "pill": "3e HAUSSE D'AFFILÉE", "desc": "Clôture du mercredi 11 novembre · Zonebourse / Boursorama"}])
t = "Et ce matin, Paris suit : le CAC 40 grimpe de près de 1 %, autour de 8 400 points."
beat(t, "Et ce matin, Paris suit : le CAC quarante grimpe de près d'un pour cent, autour de huit mille quatre cents points.", C("B2"), [
    {"type": "tickers", "title": "EUROPE · ≈ 8 400 PTS À PARIS", "rows": [
        {"name": "CAC 40", "pct": "+0,8 %", "at_word": W(t, "CAC"), "up": True},
        {"name": "DAX", "pct": "+1,2 %", "at_word": W(t, "grimpe"), "up": True}]},
    {"type": "source", "text": "Boursorama · 12 nov. 2026"}])
t = "Pendant ce temps, Nvidia perd près de 7 % avant l'ouverture de Wall Street."
beat(t, "Pendant ce temps, Nvidia perd près de sept pour cent avant l'ouverture de Wall Street.", {"screen": True, "under": C("B3")}, [
    {"type": "screen_counter", "kicker": "NVIDIA · AVANT-BOURSE", "value_from": 0, "value_to": 6.9, "decimals": 1, "prefix": "− ", "suffix": " %", "color": "red",
     "pill": "CRISE AU CONSEIL", "desc": "Reuters, via Boursorama · 12 nov. 2026", "logo": "NVDA"}])
t = "Son conseil envisage d'écarter son patron. Et toute l'Asie des puces décroche."
beat(t, "Son conseil envisage d'écarter son patron... Et toute l'Asie des puces décroche.", C("B4"), [
    {"type": "tickers", "title": "ASIE · JEUDI", "rows": [
        {"name": "Bourse de Taïwan", "pct": "−2,6 %", "at_word": W(t, "Asie"), "up": False},
        {"name": "Advantest", "pct": "−5,1 %", "at_word": W(t, "puces"), "up": False},
        {"name": "Ibiden", "pct": "−9,3 %", "at_word": W(t, "décroche"), "up": False}]},
    {"type": "source", "text": "Reuters, via Boursorama · 12 nov. 2026"}])
t = "Alors, qu'est-ce qui protège l'Europe ?"
beat(t, "Alors... qu'est-ce qui protège l'Europe ?", C("B5"), [
    {"type": "bigtitle", "lines": ["QU'EST-CE QUI", "PROTÈGE L'EUROPE ?"], "at_word": 1}])
t = "Premier bouclier : le pétrole. Le Brent est tombé à son plus bas depuis deux mois, autour de 92 dollars."
beat(t, "Premier bouclier : le pétrole. Le Brent est tombé à son plus bas depuis deux mois... autour de quatre-vingt-douze dollars.", {"screen": True, "under": C("B7")}, [
    {"type": "screen_counter", "kicker": "BRENT · BARIL", "value_from": 100, "value_to": 92, "decimals": 0, "prefix": "≈ ", "suffix": " $", "color": "green",
     "pill": "PLUS BAS DEPUIS 2 MOIS", "desc": "Espoirs de désescalade au Moyen-Orient · Boursorama"}])
t = "Ce bras de fer, je le décrypte en direct sur mon Telegram. Lien en bio."
beat(t, None, {"blur_prev": True}, [
    {"type": "phone", "mode": "mini", "img": "tg_38e4f34b.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "Deuxième bouclier : Paris est bien moins exposé à l'IA que Wall Street ou l'Asie."
beat(t, "Deuxième bouclier : Paris est bien moins exposé à l'I.A. que Wall Street ou l'Asie.", C("B9"), [
    {"type": "news", "at_word": W(t, "Paris"), "left": "BOURSE DE PARIS", "right": "12 NOV.", "tag": "LE BOUCLIER",
     "headline": "Paris profite d'une exposition moindre aux valeurs liées à l'IA", "highlight": "exposition moindre", "sub": "Boursorama · 12 nov. 2026"}])
t = "Et les résultats tombent au bon moment : Siemens bondit de près de 5 %, porté par les data centers."
beat(t, "Et les résultats tombent au bon moment : Siemens bondit de près de cinq pour cent, porté par les data centers.", C("B10"), [
    {"type": "stock", "key": "SIE", "name": "Siemens", "sub": "Francfort · perspectives relevées · data centers IA", "pct": "+4,7 %", "up": True, "size": "big", "y": 1420, "at_word": W(t, "Siemens")},
    {"type": "source", "text": "Boursorama · 12 nov. 2026"}])
t = "Burberry s'envole de plus de 7 % : ses ventes surprennent, grâce aux États-Unis et à la Chine."
beat(t, "Burberry s'envole de plus de sept pour cent : ses ventes surprennent, grâce aux États-Unis et à la Chine.", C("B11"), [
    {"type": "stock", "key": "BRBY", "name": "Burberry", "sub": "Londres · ventes meilleures que prévu", "pct": "+7,5 %", "up": True, "size": "big", "y": 1420, "at_word": W(t, "Burberry")},
    {"type": "source", "text": "Boursorama · 12 nov. 2026"}])
t = "Allianz relève ses prévisions, Rolls-Royce confirme les siennes… et les deux montent."
beat(t, "Allianz relève ses prévisions, Rolls-Royce confirme les siennes... et les deux montent.", {"screen": True, "under": C("B12")}, [
    {"type": "tickers", "title": "RÉSULTATS DU JOUR", "rows": [
        {"name": "Allianz", "pct": "+1,7 %", "at_word": W(t, "Allianz"), "key": "ALV", "up": True},
        {"name": "Rolls-Royce", "pct": "+2,6 %", "at_word": W(t, "Rolls-Royce"), "key": "RR", "up": True},
        {"name": "Siemens", "pct": "+4,7 %", "at_word": W(t, "montent"), "key": "SIE", "up": True}]},
    {"type": "source", "text": "Boursorama · 12 nov. 2026"}])
t = "Mais attention : le taux américain à 10 ans touche 5 %, et le dollar est au plus haut depuis 19 mois."
beat(t, "Mais attention : le taux américain à dix ans touche cinq pour cent... et le dollar est au plus haut depuis dix-neuf mois.", {"screen": True, "under": C("B13")}, [
    {"type": "screen_duo", "a": {"kicker": "TAUX US À 10 ANS", "value_to": 5.01, "decimals": 2, "suffix": " %", "color": "red", "desc": "Reuters, via Boursorama"},
     "b_at_word": W(t, "dollar"), "b": {"kicker": "INDICE DOLLAR", "value_to": 19, "decimals": 0, "suffix": " mois", "color": "gold", "desc": "Plus haut depuis 19 mois"}},
    {"type": "source", "text": "Boursorama · 12 nov. 2026"}])
t = "Prochain test : vendredi, les prix à la production américains. Puis le 17 novembre, les résultats de Nvidia."
beat(t, "Prochain test : vendredi, les prix à la production américains. Puis le dix-sept novembre... les résultats de Nvidia.", C("B15"), [
    {"type": "date", "text": "Ven. 13/11 : prix à la production US · Mar. 17/11 : résultats Nvidia"},
    {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "Résultats trimestriels · 17 novembre", "y": 1420, "at_word": W(t, "Nvidia")}])
t = "Alors, l'Europe peut-elle vraiment tenir tête à Wall Street ? Dis-le-moi en commentaire."
beat(t, "Alors... l'Europe peut-elle vraiment tenir tête à Wall Street ? Dis-le-moi en commentaire.", C("B16"), [
    {"type": "bigtitle", "lines": ["L'EUROPE PEUT-ELLE", "TENIR TÊTE ?"], "at_word": W(t, "tenir")}])
t = "Pendant que les marchés paniquent, sur mon Telegram on garde la tête froide. Plus de 22 000 personnes y reçoivent gratuitement l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées et mes opportunités en temps réel. Rejoins la famille : lien en bio."
beat(t, "Pendant que les marchés paniquent, sur mon Telegram, on garde la tête froide. Plus de vingt-deux mille personnes y reçoivent gratuitement l'actu géopolitique et financière décortiquée, mes analyses d'actions détaillées, et mes opportunités en temps réel. Rejoins la famille : lien en bio.",
     {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "Europe au record, Nvidia à terre : ce qui se passe vraiment",
     "imgs": ["tg_4b2fa9a8.jpg", "tg_1eaa56f0.jpg", "tg_3435c02c_top.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "REJOINS LA FAMILLE"}],
    cta="long", endcard={"duration": 1.8, "button": "REJOINS LA FAMILLE", "small": "Telegram gratuit · lien en bio"})
d = os.path.dirname(os.path.abspath(__file__))
clips = json.load(open(os.path.join(d, "clips.json")))
def sub(bg):
    if isinstance(bg, dict):
        if "clip" in bg and bg["clip"] in clips: bg.update(clips[bg["clip"]])
        if "under" in bg: sub(bg["under"])
        for s in bg.get("shots", []): sub(s)
for b in B: sub(b["bg"])
spec = {"id": "ep15_europe_record", "date_label": "12 novembre 2026", "brand": "Invest Family Fr", "hook_type": "question", "hook_formula": "question directe", "cta_angle": "Pendant que les marchés paniquent, sur mon Telegram on garde la tête froide", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.boursorama.com/bourse/actualites/le-reflux-de-l-energie-rapproche-l-europe-de-ses-records-745590fa717b751f4eceb8963442ffea",
 "https://www.boursorama.com/bourse/actualites/hausse-prudente-en-vue-en-europe-nvidia-pourrait-peser-sur-la-tendance-actualise-daf524477ba98ca891f3615f4cdbeeb5",
 "https://www.boursorama.com/bourse/actualites/les-valeurs-a-suivre-a-paris-et-en-europe-actualise-da4dbf9cff0d67042f8717be475f0253"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
open(os.path.join(d, "voice_text.txt"), "w").write("\n".join(b.get("say") or b["text"] for b in B))
