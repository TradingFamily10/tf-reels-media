import json, sys
sys.path.insert(0, '/home/claude/kit/engine')
from build_timeline import tokens
EP = 'ep41_or_bitcoin_fed'
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
CR = "Cryptoast · 20 nov. 2026"
NO = "Reuters / Schwab via Nocta · 21 nov. 2026"
JK = "JKN · 20 nov. 2026"
CN = "The Cryptonomist · 20 nov. 2026"
KC = "CoinDesk via KuCoin · 20 nov. 2026"

t = "L'or et le bitcoin devaient te protéger. Pourquoi s'effondrent-ils ensemble ?"
beat(t, "L'or et le bitcoin devaient te protéger... Pourquoi s'effondrent-ils ensemble ?",
     {"shots": [clip("0"), dict(clip("0b"), at_word=w(t, "Pourquoi"))]},
     [{"type": "date", "text": "Vendredi 20 novembre 2026 · Or & bitcoin", "until_beat": 1},
      {"type": "bigtitle", "lines": ["OR ET BITCOIN :", "POURQUOI ?"], "at_word": 0},
      {"type": "stock", "key": "BTC", "name": "Bitcoin", "sub": "BTC · vs record oct. 2025 · calcul", "pct": "−56 %", "up": False,
       "y": 1420, "at_word": w(t, "Pourquoi")}])

t = "Vendredi soir, le bitcoin est tombé à 55 830 dollars, au plus bas depuis septembre 2024."
beat(t, "Vendredi soir, le bitcoin est tombé sous les cinquante-six mille dollars... au plus bas depuis septembre deux mille vingt-quatre.",
     {"screen": True, "under": clip("1")},
     [{"type": "screen_counter", "kicker": "BITCOIN · VENDREDI SOIR", "value_from": 70000, "value_to": 55830, "decimals": 0,
       "prefix": "", "suffix": " $", "color": "red", "pill": "PLUS BAS DEPUIS SEPT. 2024", "desc": "20 nov., 23h13 heure de New York · " + NO, "logo": "BTC"}])

t = "Et ce n'est pas le pire : l'or a perdu près de 9 % en une semaine."
beat(t, "Et ce n'est pas le pire : l'or a perdu près de neuf pour cent... en une semaine.",
     {"screen": True, "under": clip("2")},
     [{"type": "screen_counter", "kicker": "OR · SUR LA SEMAINE", "value_from": 0, "value_to": -9, "decimals": 0,
       "prefix": "≈ ", "suffix": " %", "color": "red", "pill": "PIRE SEMAINE DEPUIS MARS", "desc": "3 515 $ l'once le 20 nov., plus bas depuis sept. 2025 · " + CR}])

t = "Depuis son record de janvier, l'once a fondu de 37 %."
beat(t, "Depuis son record de janvier, l'once a fondu de trente-sept pour cent.",
     {"screen": True, "under": clip("3")},
     [{"type": "screen_duo",
       "a": {"kicker": "OR · RECORD DE JANVIER 2026", "value_to": 5600, "decimals": 0, "prefix": "≈ ", "suffix": " $", "color": "white", "desc": "L'once d'or · " + CR},
       "b_at_word": w(t, "fondu"),
       "b": {"kicker": "OR · 20 NOVEMBRE 2026", "value_to": 3515, "decimals": 0, "prefix": "", "suffix": " $", "color": "red", "desc": "−37 % depuis le record · " + CR}}])

t = "Le bitcoin, lui, a perdu plus de la moitié de sa valeur depuis son record d'octobre 2025."
beat(t, "Le bitcoin, lui, a perdu plus de la moitié de sa valeur... depuis son record d'octobre deux mille vingt-cinq.",
     {"screen": True, "under": clip("4")},
     [{"type": "screen_duo",
       "a": {"kicker": "BITCOIN · RECORD OCT. 2025", "value_to": 126210, "decimals": 0, "prefix": "", "suffix": " $", "color": "white", "desc": JK, "logo": "BTC"},
       "b_at_word": w(t, "moitié"),
       "b": {"kicker": "BITCOIN · 20 NOV. 2026 (SOIR)", "value_to": 55830, "decimals": 0, "prefix": "", "suffix": " $", "color": "red", "desc": "≈ −56 % (calcul) · " + NO}}])

t = "Sept semaines de baisse d'affilée : du jamais vu depuis le krach de 2022."
beat(t, "Sept semaines de baisse d'affilée... du jamais vu depuis le krach de deux mille vingt-deux.",
     {"shots": [clip("5"), dict(clip("5b"), at_word=w(t, "jamais"))]},
     [{"type": "news", "at_word": 1, "left": "CRYPTO", "right": "20 NOV.", "tag": "BITCOIN",
       "headline": "Le bitcoin enchaîne sept semaines de baisse, sa plus longue série depuis 2022 et Terra-Luna",
       "highlight": "sept semaines de baisse", "sub": JK + " · " + CN}])

t = "Les gros fonds fuient : jeudi, 541 millions de dollars sont sortis de l'ETF bitcoin de BlackRock. Un record."
beat(t, "Les gros fonds fuient : jeudi, cinq cent quarante et un millions de dollars sont sortis de l'E.T.F. bitcoin de BlackRock. Un record.",
     {"shots": [clip("6"), dict(clip("6b"), at_word=w(t, "BlackRock"))]},
     [{"type": "stock", "key": "BLK", "name": "BlackRock · IBIT", "sub": "Sortie du 19 nov. · record · Crypto Economy",
       "pct": "−541 M$", "up": False, "y": 560, "at_word": w(t, "541")}])

t = "Alors, qui a tiré le tapis sous les deux valeurs refuges ?"
beat(t, "Alors... qui a tiré le tapis sous les deux valeurs refuges ?", clip("7"),
     [{"type": "bigtitle", "lines": ["QUI A TIRÉ", "LE TAPIS ?"], "at_word": w(t, "qui")}])

t = "Ce double plongeon, je le décrypte en direct sur mon Telegram. Lien en bio."
beat(t, "Ce double plongeon, je le décrypte en direct sur mon Telegram. Lien en bio.", clip("8"),
     [{"type": "phone", "mode": "mini", "img": "tg_1eaa56f0.jpg", "bio_at_word": w(t, "bio")}], cta="short")

t = "La réponse : la Fed. Une hausse de ses taux le 9 décembre est jouée à 92 %."
beat(t, "La réponse : la Fed. Une hausse de ses taux le neuf décembre... est jouée à quatre-vingt-douze pour cent.",
     {"screen": True, "under": clip("9")},
     [{"type": "screen_counter", "kicker": "HAUSSE DE TAUX DE LA FED · 9 DÉC.", "value_from": 0, "value_to": 92, "decimals": 0,
       "prefix": "", "suffix": " %", "color": "white", "pill": "PROBABILITÉ (CME FEDWATCH)", "desc": "Vendredi soir · " + NO, "at_word": w(t, "hausse")}])

t = "Inflation déduite, les taux américains à 10 et 30 ans sont au plus haut depuis plus de 20 ans."
beat(t, "Inflation déduite, les taux américains à dix et trente ans... sont au plus haut depuis plus de vingt ans.",
     {"shots": [clip("10"), dict(clip("10b"), at_word=w(t, "plus"))]},
     [{"type": "news", "at_word": 1, "left": "TAUX RÉELS US", "right": "20 NOV.", "tag": "OBLIGATIONS",
       "headline": "Les taux réels à 10 et 30 ans au plus haut depuis plus de 20 ans, selon Robin Brooks (Brookings)",
       "highlight": "plus haut depuis plus de 20 ans", "sub": KC}])

t = "Or l'or et le bitcoin ne rapportent aucun intérêt. Face à ces taux, ils perdent leur attrait."
beat(t, "Or... l'or et le bitcoin ne rapportent aucun intérêt. Face à ces taux, ils perdent leur attrait.",
     {"screen": True, "under": clip("11")},
     [{"type": "screen_duo",
       "a": {"kicker": "TAUX RÉEL US À 2 ANS", "value_to": 2.4, "decimals": 2, "prefix": "> ", "suffix": " %", "color": "green", "desc": "Plus haut depuis 2023 · ING via " + KC},
       "b_at_word": w(t, "aucun"),
       "b": {"kicker": "OR ET BITCOIN", "value_to": 0, "decimals": 0, "prefix": "", "suffix": " %", "color": "red", "desc": "Aucun intérêt versé"}}])

t = "Et le dollar en profite : il grimpe au plus haut depuis 19 mois."
beat(t, "Et le dollar en profite : il grimpe au plus haut depuis dix-neuf mois.",
     {"screen": True, "under": clip("12")},
     [{"type": "screen_counter", "kicker": "INDICE DOLLAR (DXY)", "value_from": 98, "value_to": 104, "decimals": 0,
       "prefix": "≈ ", "suffix": "", "color": "green", "pill": "PLUS HAUT DEPUIS 19 MOIS", "desc": CR}])

t = "Le twist ? Strategy, plus gros détenteur coté, a payé ses bitcoins plus de 75 000 dollars en moyenne : son trésor est sous l'eau."
beat(t, "Le twist ? Strategy, plus gros détenteur coté, a payé ses bitcoins plus de soixante-quinze mille dollars en moyenne... son trésor est sous l'eau.",
     {"shots": [clip("12"), dict(clip("13b"), at_word=w(t, "trésor"))]},
     [{"type": "stock", "key": "MSTR", "name": "Strategy", "sub": "850 849 BTC · prix moyen ≈ 75 452 $",
       "pct": "−26 %", "up": False, "y": 560, "at_word": w(t, "Strategy")},
      {"type": "source", "text": "The Cryptonomist · écart prix moyen / plus bas de vendredi (55 830 $) : calcul"}])

t = "Et vendredi, 1,5 milliard de dollars de paris à crédit ont été liquidés sur les cryptos."
beat(t, "Et vendredi, un milliard et demi de dollars de paris à crédit... ont été liquidés sur les cryptos.",
     {"screen": True, "under": clip("14")},
     [{"type": "screen_counter", "kicker": "LIQUIDATIONS CRYPTO · 20 NOV.", "value_from": 0, "value_to": 1.5, "decimals": 1,
       "prefix": "≈ ", "suffix": " Md$", "color": "red", "pill": "POSITIONS À EFFET DE LEVIER", "desc": JK}])

t = "À surveiller : la Fed, les 8 et 9 décembre. Goldman Sachs ne voit pas l'or revenir à son record avant fin 2028."
beat(t, "À surveiller : la Fed, les huit et neuf décembre. Goldman Sachs ne voit pas l'or revenir à son record... avant fin deux mille vingt-huit.",
     {"shots": [clip("15"), dict(clip("15b"), at_word=w(t, "Goldman"))]},
     [{"type": "tickers", "title": "À SURVEILLER", "rows": [
        {"name": "Réunion de la Fed", "pct": "8-9 DÉC.", "at_word": w(t, "Fed"), "up": True},
        {"name": "Hausse suivante (Goldman)", "pct": "MARS 2027", "at_word": w(t, "Goldman"), "up": True},
        {"name": "Or à 5 600 $ (Goldman)", "pct": "FIN 2028", "at_word": w(t, "record"), "up": True}]},
      {"type": "source", "text": "Goldman Sachs via Kitco, cité par " + CR}])

t = "Alors, l'or et le bitcoin sont-ils encore des refuges ? Dis-le en commentaire."
beat(t, "Alors... l'or et le bitcoin sont-ils encore des refuges ? Dis-le en commentaire.", clip("16"),
     [{"type": "bigtitle", "lines": ["ENCORE DES", "VALEURS REFUGES ?"], "at_word": w(t, "refuges")}])

t = ("L'or et le bitcoin ne préviennent pas avant de chuter. Mon Telegram gratuit, si : "
     "actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. "
     "Plus de 22 000 personnes y sont déjà. Lien en bio.")
say = ("L'or et le bitcoin ne préviennent pas avant de chuter... Mon Telegram gratuit, si : "
       "actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel. "
       "Plus de vingt-deux mille personnes y sont déjà. Lien en bio.")
beat(t, say, {"blur_prev": True},
     [{"type": "cta_telegram", "notif": "Or & bitcoin : ce que la Fed prépare", "imgs": ["tg_3435c02c_top.jpg", "tg_1eaa56f0.jpg", "tg_4b2fa9a8.jpg"],
       "subs": 22760, "subs_at_word": w(t, "22"), "bio_at_word": len(tokens(t)) - 1, "button": "ENTRE DANS LE CANAL"}],
     cta="long", endcard={"duration": 1.8, "button": "ENTRE DANS LE CANAL", "small": "Telegram gratuit · lien en bio"})

DROP = {3, 5, 12, 14}
B = [b for i, b in enumerate(B) if i not in DROP]
spec = {"id": EP, "date_label": "21 novembre 2026", "brand": "Invest Family Fr",
        "hook_type": "question", "hook_formula": "question directe",
        "cta_angle": "L'or et le bitcoin ne préviennent pas avant de chuter. Mon Telegram, si.",
        "cta_type": "notif_scroll",
        "voice": {"engine": "hedra", "voice": "Clément 2", "voice_id": "voice_ed52485f-b64d-4dc4-8080-0847ae629dad",
                  "model": "elevenlabs-v3", "speed": 1.08, "stability": 0.5},
        "sources": ["https://cryptoast.fr/or-bitcoin-chute-dollar-fed-taux-anthropic-gold-xau/",
                    "https://noctaaa.substack.com/p/daily-brief-saturday-21-november-2026",
                    "https://news.jkn.co.kr/editions/french/post/1111422",
                    "https://fr.cryptonomist.ch/2026/11/20/chute-du-prix-du-bitcoin-sous-60-000-dollars-septieme-perte-en-vue/",
                    "https://www.kucoin.com/fr/news/flash/gold-and-bitcoin-fall-amid-rising-u-s-real-yields",
                    "https://www.kucoin.com/fr/news/flash/bitcoin-hits-4-5-month-low-amid-record-etf-outflows-in-november-2026"],
        "beats": B}
json.dump(spec, open(f'/home/claude/kit/episodes/{EP}/spec.json', 'w'), ensure_ascii=False, indent=1)
open(f'/home/claude/kit/episodes/{EP}/voice_text.txt', 'w').write("\n".join(b["say"] for b in B))
print(len(B), "beats", sum(len(tokens(b["text"])) for b in B), "mots")
