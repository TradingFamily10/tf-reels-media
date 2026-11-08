# Usine « Dernières Infos » — Invest Family Fr (3 reels / jour)

> **📲 DEPUIS LE 8 NOV. 2026 — TIKTOK À LA MAIN, LE RESTE RESTE DANS METRICOOL** (Clément : « ne les mets plus dans Metricool […] ça plafonne à 0 les vues. Et envoie des alertes par mail aux heures où je dois poster », puis : « je veux que tu gardes Metricool pour les comptes Facebook et YouTube en lien, je voulais juste arrêter pour TikTok »).
> - Metricool (§8) : programmer comme avant sur TOUS les réseaux reliés à la marque 7946352 d'après getBrandSettings **SAUF TikTok** (jamais `{"network":"tiktok"}` ni `tiktokData`). Facebook Reel aujourd'hui ; YouTube Short s'il est relié un jour.
> - TikTok : **envoyer le MP4 à Clément dans la conversation (SendUserFile, display "attach", status "proactive")** et écrire dans `history.json` `title`, `caption` (légende prête à copier) et `media_url`, poussés sur main AVANT l'heure du créneau. À 06:55 · 13:05 · 14:55, les tâches planifiées « Alerte mail — Dernières Infos » envoient à clement.istasse@gmail.com le lien du MP4 + la légende : Clément poste lui-même sur TikTok.

Chaque exécution fabrique **1 reel vertical 1080×1920 de 70–85 s** sur l'actu éco / géopolitique / financière / macro, le dépose sur la branche `videos-dernieres-infos` du dépôt de médias (URL publique, comme les autres usines) et le programme dans Metricool sur la marque **Invest Family Fr** (blogId `7946352`, Facebook Reel ; TikTok posté à la main par Clément). Tout est automatique : ne demande rien à Clément, décide et note tes choix dans le rapport final.

## Règles non négociables
- **Français impeccable**, ton humain et tendu, phrases courtes. Jamais « Dans un monde où… », jamais de formules IA.
- **Faits vérifiés** : chaque chiffre vient d'une page ouverte (WebFetch), datée de moins de 72 h pour le sujet principal. Sources dans `spec.json`.
- **Visuels** : uniquement des vidéos Pixabay HD/4K filmées (jamais d'animation 3D, jamais d'image IA). **Aucune photo de personnalité publique** (ni téléchargée, ni insérée) : utilise lieux, drapeaux, bâtiments, logos, data.
- **Logo de chaque action citée**, au mot près (carte `stock`, lignes de `tickers`, `logo` des écrans). Logos dans `assets/logos/logos.json` ; s'il en manque un, ajoute-le depuis le dépôt GitHub public `nvstly/icons` (`ticker_icons/<TICKER>.png`) et déclare sa tuile.
- **Logo TF rond** en haut à droite tout le long (automatique via `assets/logo_tf.png`).
- **Accent gold** (#F6C343). Le rouge n'est utilisé que pour les chiffres en baisse, le vert pour les hausses.
- **Voix : « Clément 2 » sur Hedra** (voir §5). Ne jamais accélérer la voix après coup.
- **Metricool** : ne jamais cocher « contenu généré par IA » (`isAigc:false`, `isAiGeneratedContent:false`).
- **Varier à chaque vidéo** : accroche visuelle, formule d'accroche écrite et CTA final doivent être différents des 3 dernières entrées de `history.json`.

## 0. Créneau de ce run (à faire EN PREMIER)
Créneaux fixes (Europe/Paris) : **06:55 · 13:05 · 14:55**. Ils laissent ≥ 3 h avec les carrousels déjà prévus sur cette page (10:00 · 18:00 · 21:30, autre usine) : ne jamais les déplacer.
1. `TZ=Europe/Paris date` → créneau du run = le premier créneau situé **au moins 40 min** après maintenant (après 14:15 : 06:55 du lendemain).
2. Metricool `getScheduledPosts` (brandId `7946352`, Europe/Paris, journée du créneau). Si un post est déjà programmé à ±20 min de ce créneau → terminer tout de suite par « rien à faire (créneau HH:MM déjà pris) ».
3. Noter dans le rapport tout autre post de la page à moins de 3 h du créneau (sans rien déplacer).

## 1. Préparer l'espace
```bash
# dépôt public (déjà rattaché en push par add_repo TradingFamily10/tf-reels-media)
git clone --depth 1 https://github.com/TradingFamily10/tf-reels-media /home/claude/tf-reels-media
cp -r /home/claude/tf-reels-media/usine/dernieres-infos /home/claude/kit
cd /home/claude/kit
printf '%s' "$PIXABAY_KEY" > assets/pixabay_key.txt        # clé fournie dans le message de la tâche
NO_PROXY=localhost,127.0.0.1 no_proxy=localhost,127.0.0.1 pip install --break-system-packages -q faster-whisper
```
Prérequis déjà présents : Python 3 (numpy, scipy), Playwright + Chromium, ffmpeg, ImageMagick, `gh` (API REST seulement).

## 2. Choisir le sujet
1. Recherche (WebSearch extended puis WebFetch des articles) : ce qui a fait bouger les marchés ou la géopolitique dans les dernières 24–48 h (krach / envolée d'une valeur, banque centrale, inflation, emploi, pétrole, or, guerre, sanctions, élections, dette, tarifs douaniers, crypto majeure).
2. Écarter tout sujet déjà traité dans `history.json` (même événement), sauf rebondissement nouveau.
3. Préférer un sujet avec : un chiffre choc, un « coupable » ou un retournement, 2 à 4 sociétés cotées à montrer en logo, une suite à venir (date).
4. Créneau 06:55 → la nuit : Asie, Wall Street de la veille, ce qui attend l'Europe ; 13:05 → macro / géopolitique / Europe ; 14:55 → avant l'ouverture de Wall Street (15:30) : valeurs US, stats US, Fed. Le week-end : géopolitique, macro, dossiers de fond liés à l'actu de la semaine.

## 3. Écrire le script (16–19 phrases, 70–85 s de voix)
Structure : **accroche (chiffre ou fait choc, lu à l'écran)** → relance (« et ce n'est pas le pire ») → contexte chiffré → le pourquoi → boucle ouverte (« alors, qui… ? ») → **CTA court Telegram vers 35–50 %** (1 phrase) → révélation → preuves (2–3 chiffres) → twist macro / géopolitique → prochaine date à surveiller → question ouverte → **CTA long original**.

Chaque phrase = un objet `{"text": ..., "say": ...}` :
- `text` = ce qui s'affiche (chiffres en chiffres, « 2 500 », « 17 % »).
- `say` = ce que dit la voix : chiffres en lettres, **pas de décimales** (« plus de cinq pour cent »), sigles avec points (« A.M.D. », « l'I.A. »), « … » pour une pause dramatique.

Formules d'accroche écrites (tourner, pas 2 fois de suite la même) :
1. Chiffre choc : « 2 500 milliards de dollars, effacés en une seule séance. »
2. Coupable inattendu : « Ce n'est pas la Fed qui a fait plonger X. C'est… »
3. Contre-intuitif : « Les chiffres sont excellents. Et pourtant X s'effondre. »
4. Question directe : « Ton épargne vient-elle de perdre 10 % sans que tu le saches ? »
5. Compte à rebours : « Dans 48 heures, un chiffre peut tout faire basculer. »
6. Le jour où : « Le jour où un pays a fait trembler tout le marché du pétrole. »
7. Personne n'en parle : « Tout le monde regarde X. Le vrai danger est ailleurs. »

CTA court (35–50 %), exemples : « Ce krach, je le suis en direct sur mon Telegram. Lien en bio. » / « La suite, je la publie en temps réel sur mon Telegram. »

CTA long (fin) — toujours original, contient : canal Telegram gratuit, actu géopolitique et financière décortiquée, analyses d'actions détaillées, opportunités en temps réel, « plus de 22 000 personnes », lien en bio. Idées d'angle (une différente à chaque fois) :
- « Pendant que les marchés paniquent, sur mon Telegram on garde la tête froide… Rejoins la famille. »
- « Ce que je viens de te montrer, mes abonnés l'ont lu avant tout le monde… »
- « Si tu veux comprendre avant les autres au lieu de subir… »
- « Chaque matin, je fais le tri dans le bruit pour toi… »
- « La prochaine secousse, tu veux l'apprendre ici ou la voir venir ? »
- « 22 000 personnes ont déjà la longueur d'avance. Il manque toi. »

## 4. Écrire `episodes/<id>/spec.json`
Modèle complet : `episodes/ep02_krach_ia/spec.json` (à copier). Chaque beat : `text`, `say`, `bg`, `overlays`. Les index `at_word` se calculent avec `tokens()` de `engine/build_timeline.py` (les « 59 000 » et « 5 % » comptent pour un mot).

**Accroche visuelle — tourner entre ces 6 types** (`spec.hook_type`) :
| type | beat 0 |
| --- | --- |
| `bignum` | `hook_bignum` : chiffre géant qui compte + pastille gold + logos floutés qui se révèlent |
| `breaking` | `date` + `breaking` (3 lignes gold) + `stock` en grand ou `ticket` de séance |
| `logowall` | `screen_logos` : compteur + grille de logos sur vidéo floutée |
| `question` | vidéo forte + `bigtitle` (question en 2 lignes gold) + `stock` |
| `headline` | `date` + carte `news` en gros avec surlignage gold |
| `chip` | `stock` taille `big` + `bigtitle` court |

**Habillage disponible** : `date`, `source`, `breaking`, `bigtitle`, `stock` (logo + nom + variation, option `strike_at_word`), `ticket`, `tickers`, `news` (aussi pour les citations), `photo`, `screen_counter`, `screen_duo`, `screen_gauge`, `screen_vote`, `screen_logos`, `hook_bignum`, `phone` (CTA court : `"img": "tg_xxx.jpg"`), `cta_telegram` (CTA long : notification + vraies captures qui défilent + compteur d'abonnés + bouton gold + cercle sur « lien en bio »), `endcard`.

**Data par-dessus les vidéos** : au moins 4 éléments data par vidéo (écran chiffre, duo, logos, tickers, carte action). Un nouvel élément ou un nouveau plan toutes les 2–4 s.

**Fonds** : `bg` = `{"clip": "fichier.mp4", "cx": 0.5, "ss": 1, "inset": 0}` ; plusieurs plans dans une phrase longue : `{"shots": [ {...}, {..., "at_word": n} ]}` ; sous un écran data : `{"screen": true, "under": {"clip": ...}}` (flouté) ; CTA : `{"blur_prev": true}`.

**CTA long** : `cta_telegram` avec `notif` (texte de notification, à varier), `imgs` (2–3 captures parmi `assets/telegram/`, ordre varié), `subs: 22760`, `subs_at_word`, `bio_at_word`, `button` (varier : « REJOINS LA FAMILLE », « ACCÈS GRATUIT », « ENTRE DANS LE CANAL »), puis `endcard`.

## 5. Voix « Clément 2 » (Hedra, un seul appel)
1. `generate_speech` : `voice = voice_ed52485f-b64d-4dc4-8080-0847ae629dad`, `model = elevenlabs-v3`, `language = fr`, `speed = 1.08`, `model_specific_parameters = {"stability": 0.5}`, `text` = tous les `say` à la suite, séparés par un saut de ligne. (≈ 25 crédits ; vérifier `get_balance` avant : sous 60 crédits, prévenir dans le rapport.)
2. `get_generations` (wait 20 s) jusqu'à COMPLETED, puis télécharger l'URL dans `episodes/<id>/voice_raw/full.mp3` (curl ; si l'URL est très longue, `engine/fetch_hedra.sh` reconstruit l'URL à partir de l'id, de la signature et du token).
3. `python3 engine/voice_hedra.py episodes/<id>` → découpe par phrase, coupe les blancs, aligne chaque mot (Whisper). Lire la transcription affichée : si un mot clé est mal prononcé, corriger son `say` et régénérer **seulement cette phrase** (mettre `voice_raw/beat_XX.mp3`… ou refaire `full.mp3`).

Secours si Hedra est indisponible : `engine/tts_supertonic.py` (voix gratuite, `--sid 6 --speed 1.16`), modèle à télécharger depuis la release GitHub `k2-fsa/sherpa-onnx` `tts-models/sherpa-onnx-supertonic-3-tts-int8-2026-05-11.tar.bz2` ; le signaler dans le rapport.

## 6. Vidéos Pixabay
```bash
# requêtes en anglais, 2–3 par plan
python3 engine/broll_candidates.py episodes/<id> episodes/<id>/cand_queries.json
```
**Regarder chaque planche** `cand/sheet_b*.jpg` et choisir le clip qui colle vraiment à la phrase (4K si possible). Télécharger par id (API `https://pixabay.com/api/videos/?key=…&id=…`, User-Agent navigateur, rendu `large` sinon `medium`) dans `episodes/<id>/broll/`. Vérifier le recadrage 9:16 (extraire une image, ajuster `cx`), les bandes noires (`inset`) et le début du clip (`ss` pour éviter un fondu ou un flou).

## 7. Fabriquer
```bash
python3 engine/build_timeline.py episodes/<id>
python3 engine/check_broll.py episodes/<id>        # FAIL = clip quasi noir -> changer de clip / de ss, refaire build_timeline
python3 engine/audio.py episodes/<id>
python3 engine/render.py episodes/<id> --still 1,8,20,40,60,75     # contrôle rapide de l'habillage
python3 engine/render.py episodes/<id> --best --out episodes/<id>/<id>.mp4   # ≈ 15 min
python3 engine/contact_sheet.py episodes/<id>/<id>.mp4 episodes/<id>/check.png 2.5
```
**Regarder `check.png`** : rien ne cache les sous-titres, chaque plan colle au texte, logos présents à chaque action, CTA lisibles, pas d'écran noir. Corriger et refaire si besoin.

## 8. Publier
```bash
python3 engine/publish_media.py episodes/<id>/<id>.mp4    # -> "[media] 200 <URL>" + episodes/<id>/media_url.txt
URL=$(cat episodes/<id>/media_url.txt)
```
Puis Metricool `getBrandSettings` (réseaux reliés à la marque 7946352 = clés de `networksData`, lues en direct) et `createScheduledPost` : `blogId 7946352`, date = **le créneau choisi au §0** (s'il est à moins de 25 min, prendre maintenant + 25 min et le signaler), `info` ci-dessous. **TikTok exclu depuis le 8 nov. 2026 (voir encadré en tête) : retirer `tiktok` des providers et `tiktokData` de l'info ; Clément le poste à la main.** Aujourd'hui la marque a Facebook (+ TikTok, à la main) ; si Instagram est relié un jour, ajouter `{"network":"instagram"}` + `"instagramData": {"type":"REEL","showReelOnFeed":true,"isAiGenerated":false}` ; si YouTube l'est, `{"network":"youtube"}` + `"youtubeData": {"title":"<titre court>","type":"short","privacy":"public","madeForKids":false,"isAiGeneratedContent":false,"category":"NEWS_POLITICS"}`.
```json
{"autoPublish": true, "draft": false, "media": ["<URL>"], "providers": [{"network": "facebook"}],
 "publicationDate": {"dateTime": "YYYY-MM-DDTHH:MM:00", "timezone": "Europe/Paris"},
 "text": "<légende>", "facebookData": {"type": "REEL", "title": "<titre court>"},
 "firstCommentText": "", "hasNotReadNotes": false, "shortener": false, "smartLinkData": {"ids": []}, "descendants": [], "mediaAltText": []}
```
Légende : 1 phrase d'accroche (≠ du titre vidéo) + 1 phrase de contexte + « Toute l'actu décortiquée, mes analyses d'actions et mes opportunités en temps réel sur mon canal Telegram gratuit (lien en bio). » + « Ceci n'est pas un conseil en investissement. » + 6–9 hashtags pertinents. Vérifier ensuite avec `getScheduledPosts` qu'aucun autre post n'est déjà sur ce créneau.
Puis, pour TikTok : **SendUserFile** du MP4 (`display: "attach"`, `status: "proactive"`, légende « Reel TikTok du JJ/MM à poster à HH:MM — <titre> »).

## 9. Mémoriser et pousser
Ajouter une entrée à `history.json` (`date`, `slot`, `id`, `topic`, `hook_type`, `hook_formula`, `cta_angle`, `title`, `caption`, `media_url`, `planner_url`, `tiktok: "a_poster_main"`) — **à pousser AVANT l'heure du créneau** (l'alerte mail TikTok la lit sur main), puis copier `spec.json`, `script.json` et `history.json` dans `tf-reels-media/usine/dernieres-infos/` (jamais de MP4, jamais de clé) et pousser (`git pull --rebase` avant `git push`).

## 10. Rapport final
Un message court (5 lignes max) : sujet ; accroche visuelle + formule ; créneau + réseaux Metricool + lien (`plannerUrl`) + « MP4 TikTok envoyé, alerte mail à HH:MM » ; crédits Hedra restants ; problèmes rencontrés ou « tout est programmé ». Si Hedra n'a plus assez de crédits (< 30), utiliser la voix de secours et le dire en ligne 1.
