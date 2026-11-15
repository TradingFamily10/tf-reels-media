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
RT = "Reuters via Kitco · 13 nov. 2026"
KN = "Kitco News · 13 nov. 2026"
BV = "BullionVault · 13 nov. 2026"
FX = "FXStreet via TMGM · 13 nov. 2026"

t = "L'inflation repart. Et pourtant, l'or, la valeur refuge, s'effondre."
beat(t, "L'inflation repart. Et pourtant, l'or... la valeur refuge... s'effondre.",
     {"shots": [C("B0"), {**C("B0b"), "at_word": W(t, "pourtant")}]}, [
    {"type": "date", "text": "Semaine du 9 au 13 novembre 2026 · Or", "until_beat": 0},
    {"type": "bigtitle", "lines": ["L'OR, ENCORE", "UNE VALEUR REFUGE ?"], "at_word": W(t, "pourtant")}])
t = "Cette semaine, l'once d'or a perdu presque 5 %. Sa pire semaine depuis juin."
beat(t, "Cette semaine, l'once d'or a perdu presque cinq pour cent. Sa pire semaine... depuis juin.", {"screen": True, "under": C("B1")}, [
    {"type": "screen_counter", "kicker": "OR · SEMAINE DU 9 AU 13 NOV.", "value_from": 0, "value_to": 4.5, "decimals": 1, "prefix": "− ", "suffix": " %",
     "color": "red", "pill": "PIRE SEMAINE DEPUIS JUIN", "desc": RT + " · " + FX}])
t = "Lundi, elle valait encore plus de 4 100 dollars. Jeudi, elle tombait sous les 3 900."
beat(t, "Lundi, elle valait encore plus de quatre mille cent dollars. Jeudi, elle tombait sous les trois mille neuf cents.", {"screen": True, "under": C("B2")}, [
    {"type": "screen_duo",
     "a": {"kicker": "LUNDI · PLUS HAUT", "value_to": 4149, "decimals": 0, "prefix": "", "suffix": " $", "color": "gold", "desc": "Once d'or, au comptant"},
     "b_at_word": W(t, "Jeudi"),
     "b": {"kicker": "JEUDI · PLUS BAS", "value_to": 3852, "decimals": 0, "prefix": "", "suffix": " $", "color": "red", "desc": "Plus bas depuis octobre 2025 · " + KN}}])
t = "Et ce n'est pas le pire : l'or a baissé 10 semaines sur les 12 dernières."
beat(t, "Et ce n'est pas le pire : l'or a baissé dix semaines... sur les douze dernières.", {"screen": True, "under": C("B3")}, [
    {"type": "screen_counter", "kicker": "SEMAINES DE BAISSE SUR 12", "value_from": 0, "value_to": 10, "decimals": 0, "prefix": "", "suffix": " / 12",
     "color": "red", "pill": "PIRE SÉRIE DEPUIS 1989", "desc": BV}])
t = "Une série pareille, on ne l'avait plus vue depuis 1989."
beat(t, "Une série pareille... on ne l'avait plus vue depuis mille neuf cent quatre-vingt-neuf.", C("B4"), [
    {"type": "bigtitle", "lines": ["DU JAMAIS-VU", "DEPUIS 1989"], "at_word": W(t, "1989")},
    {"type": "source", "text": BV}])
t = "L'argent, lui, repasse sous les 50 dollars. Moins de la moitié de son record de janvier."
beat(t, "L'argent, lui, repasse sous les cinquante dollars. Moins de la moitié... de son record de janvier.", {"screen": True, "under": C("B5")}, [
    {"type": "screen_counter", "kicker": "ARGENT · L'ONCE", "value_from": 60, "value_to": 49.9, "decimals": 1, "prefix": "", "suffix": " $",
     "color": "red", "pill": "PLUS DE −50 % DEPUIS LE RECORD DE JANVIER", "desc": RT + " · " + BV}])
t = "Alors, qui a fait tomber le métal refuge ?"
beat(t, "Alors... qui a fait tomber le métal refuge ?", C("B6"), [
    {"type": "bigtitle", "lines": ["QUI A FAIT TOMBER", "LE MÉTAL REFUGE ?"], "at_word": W(t, "Alors")}])
t = "L'or, je le suis chaque jour en direct sur mon Telegram. Lien en bio."
beat(t, "L'or, je le suis chaque jour en direct sur mon Telegram. Lien en bio.", C("B7"), [
    {"type": "phone", "mode": "mini", "img": "tg_38e4f34b.jpg", "bio_at_word": W(t, "bio")}], cta="short")
t = "Le coupable : le taux américain à 10 ans. Il grimpe au-dessus des 5 %."
beat(t, "Le coupable : le taux américain à dix ans. Il grimpe au-dessus des cinq pour cent.", {"screen": True, "under": C("B8")}, [
    {"type": "screen_counter", "kicker": "TAUX US À 10 ANS", "value_from": 4.86, "value_to": 5.13, "decimals": 2, "prefix": "", "suffix": " %",
     "color": "red", "pill": "+0,27 PT : RECORD DEPUIS AVRIL 2025", "desc": BV}])
t = "Mardi, l'inflation américaine d'octobre a surpris : elle est sortie plus forte que prévu."
beat(t, "Mardi, l'inflation américaine d'octobre a surpris... elle est sortie plus forte que prévu.", {"screen": True, "under": C("B10")}, [
    {"type": "screen_duo",
     "a": {"kicker": "ATTENDU", "value_to": 0.3, "decimals": 1, "prefix": "+ ", "suffix": " %", "color": "gold", "desc": "Prix à la consommation, octobre"},
     "b_at_word": W(t, "surpris"),
     "b": {"kicker": "PUBLIÉ", "value_to": 0.4, "decimals": 1, "prefix": "+ ", "suffix": " %", "color": "red", "desc": "Sur un mois · Reuters via ANC · 14 nov. 2026"}}])
t = "Résultat : les marchés parient à près de 90 % sur une hausse des taux de la Fed le 9 décembre."
beat(t, "Résultat : les marchés parient à près de quatre-vingt-dix pour cent... sur une hausse des taux de la Fed, le neuf décembre.", {"screen": True, "under": C("B11")}, [
    {"type": "screen_gauge", "kicker": "HAUSSE DE LA FED LE 9 DÉCEMBRE ?", "pill": "≈ 90 % SELON LE CME FEDWATCH", "desc": RT + " · " + FX}])
t = "Or l'or ne verse aucun intérêt. Quand les taux montent, il perd son attrait."
beat(t, "Or, l'or ne verse aucun intérêt. Quand les taux montent... il perd son attrait.", C("B12"), [
    {"type": "bigtitle", "lines": ["TAUX EN HAUSSE", "OR EN BAISSE"], "at_word": W(t, "Quand")}])
t = "Et le dollar grimpe à son plus haut depuis 19 mois. Double peine pour le métal jaune."
beat(t, "Et le dollar grimpe à son plus haut depuis dix-neuf mois. Double peine pour le métal jaune.", {"screen": True, "under": C("B13")}, [
    {"type": "screen_counter", "kicker": "INDICE DU DOLLAR", "value_from": 100, "value_to": 103.4, "decimals": 1, "prefix": "", "suffix": "",
     "color": "gold", "pill": "PLUS HAUT DEPUIS 19 MOIS", "desc": FX}])
t = "Même la tech trinque : vendredi, Nvidia a encore lâché près de 4 %."
beat(t, "Même la tech trinque : vendredi, Nvidia a encore lâché près de quatre pour cent.", C("B14"), [
    {"type": "stock", "key": "NVDA", "name": "Nvidia", "sub": "NVDA · Nasdaq · vendredi 13 nov.", "pct": "−3,9 %", "up": False,
     "size": "big", "y": 600, "at_word": W(t, "Nvidia")},
    {"type": "source", "text": BV}])
t = "Et sur 13 analystes de Wall Street, 10 voient l'or baisser encore."
beat(t, "Et sur treize analystes de Wall Street... dix voient l'or baisser encore.", {"screen": True, "under": C("B15")}, [
    {"type": "screen_vote", "at_word": W(t, "13"), "kicker": "L'OR LA SEMAINE PROCHAINE",
     "groups": [{"n": 3, "label": "HAUSSE OU STABLE", "color": "gold"}, {"n": 10, "label": "BAISSE", "color": "red"}],
     "desc": "Sondage hebdomadaire Kitco · 13 analystes · 13 nov. 2026"}])
t = "Prochain rendez-vous : mercredi 18 novembre, les minutes de la Fed."
beat(t, "Prochain rendez-vous : mercredi dix-huit novembre... les minutes de la Fed.", C("B16"), [
    {"type": "date", "text": "Mercredi 18 novembre 2026 · Fed"},
    {"type": "bigtitle", "lines": ["MERCREDI 18 NOV.", "LES MINUTES DE LA FED"], "at_word": W(t, "mercredi")}])
t = "Alors, l'or est-il encore une valeur refuge ? Dis-le-moi en commentaire."
beat(t, "Alors... l'or est-il encore une valeur refuge ? Dis-le-moi en commentaire.", C("B17"), [
    {"type": "bigtitle", "lines": ["REFUGE", "OU PIÈGE ?"], "at_word": W(t, "refuge")}])
t = "Pendant que les marchés paniquent, sur mon Telegram gratuit, on garde la tête froide : actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. Plus de 22 000 personnes y sont déjà. Rejoins la famille, lien en bio."
beat(t, "Pendant que les marchés paniquent, sur mon Telegram gratuit, on garde la tête froide : actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. Plus de vingt-deux mille personnes y sont déjà. Rejoins la famille, lien en bio.",
     {"blur_prev": True}, [
    {"type": "cta_telegram", "notif": "L'or décroche : ce que ça change pour toi",
     "imgs": ["tg_4b2fa9a8.jpg", "tg_3435c02c_top.jpg", "tg_1eaa56f0.jpg"], "subs": 22760, "subs_at_word": W(t, "22"), "bio_at_word": W(t, "bio"), "button": "ENTRE DANS LE CANAL"}],
    cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})
d = os.path.dirname(os.path.abspath(__file__))
clips = json.load(open(os.path.join(d, "clips.json"))) if os.path.exists(os.path.join(d, "clips.json")) else {}
def sub(bg):
    if isinstance(bg, dict):
        if "clip" in bg and bg["clip"] in clips: bg.update(clips[bg["clip"]])
        if "under" in bg: sub(bg["under"])
        for s in bg.get("shots", []): sub(s)
B = [b for i, b in enumerate(B) if i not in (4, 13)]  # beats coupés après la voix (durée)
for b in B: sub(b["bg"])
spec = {"id": "ep23_or_refuge", "date_label": "15 novembre 2026", "brand": "Invest Family Fr", "hook_type": "question", "hook_formula": "contre-intuitif",
        "cta_angle": "Pendant que les marchés paniquent, sur mon Telegram on garde la tête froide", "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad", "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://www.bullionvault.com/gold-news/gold-price-news/gold-silver-price-week-111320261",
                    "https://www.kitco.com/news/off-the-wire/2026-11-13/rate-hike-bets-keep-gold-track-its-worst-week-four-months",
                    "https://www.kitco.com/news/article/2026-11-13/wall-street-bears-abound-after-inflation-sours-fed-outlook-main-street",
                    "https://www.tmgm.com/en/analysis/market-news/article/gold-faces-weekly-rout-as-high-us-yields-fuel-fed-rate-hike-bets-202611132023",
                    "https://ancstockinvestments.com/blog/2026/11/14/why-is-gold-falling-this-week/"],
        "beats": B}
json.dump(spec, open(os.path.join(d, "spec.json"), "w"), indent=1, ensure_ascii=False)
print(len(B), "beats", sum(len((b.get("say") or b["text"]).split()) for b in B), "mots")
open(os.path.join(d, "voice_text.txt"), "w").write("\n".join(b.get("say") or b["text"] for b in B))
