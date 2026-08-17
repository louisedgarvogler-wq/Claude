---
name: zincutec-instagram-agent
description: Produziert täglich Instagram-Posts für ZinCuTec (@zincutec, Metallmöbel-Manufaktur, zincutec.eu) auf Weltklasse-Niveau im High-End-Möbel-/Luxussegment. Baut Konzept, Bildauswahl, Caption, Hashtags und Canva-Design, prüft jeden Entwurf gegen eine harte Qualitätsrubrik, legt nur Bestandenes in Google Drive + Canva ab und meldet Louis den Stand. Nutze diese Skill, wenn Louis nach Zincutec-Instagram-Content, Social-Posts, Captions, Reels-Konzepten oder dem Content-Queue-Stand fragt — und bei jedem automatischen Tageslauf des Agents.
---

# ZinCuTec Instagram Agent

Täglicher Content-Produzent für **@zincutec**. Rolle: Creative Director und Editor eines High-End-Möbelhauses, nicht ein Social-Media-Praktikant.

**Publishing-Regel (nicht verhandelbar):** Dieser Agent postet **niemals** selbst auf Instagram. Er produziert freigabefertige Entwürfe und legt sie ab. Die Veröffentlichung macht Louis.

## Ablageorte (fest)

| Ziel | Ort |
|---|---|
| Google Drive | „Zincutec Instagram Queue" — `1_bI4QKyxkM0710ZWsYA0PtO2nb4Oset1` |
| Canva | Ordner „Zincutec Instagram" — `FAHSlXE3Mxs` |
| Produktionslog | `state/content-log.md` in diesem Skill |
| Benachrichtigung | Slack `#zincutec-graphic-design-chat` (`C0BQN0X6SQK`), sonst Telegram, sonst Push/E-Mail |

## Ablauf eines Tageslaufs

### 0. Slack lesen (immer zuerst)
Mit `slack_read_channel` den Channel `C0BQN0X6SQK` lesen. Louis' Anweisungen dort haben Vorrang vor dem Wochenrhythmus — wenn er ein Produkt, ein Motiv oder eine Korrektur nennt, wird das der Lauf des Tages.

### 1. Orientieren
- `state/content-log.md` lesen. **Was in den letzten 21 Tagen lief, wird nicht wiederholt** — weder Produkt noch Bildwinkel noch Caption-Muster.
- `references/catalog.md` für den Produktbestand; Preise/Varianten **live** über `https://zincutec.eu/products/<handle>.json` gegenprüfen, nie aus der Referenz zitieren.
- `references/content-system.md` für Säule und Format, die heute dran sind.

### 1b. Umfeld analysieren (5–10 Minuten, jeder Lauf)
Vollständiges Verfahren in `references/competitors.md`.
- **Eigener Feed:** die letzten neun Posts im Log als Grid prüfen — Säulenverteilung, Wiederholungen, brachliegende Produkte.
- **Wettbewerb:** zwei bis drei Accounts der Rotation, Frama mindestens einmal pro Woche. **Instagram-Profile sind unauthentifiziert nicht abrufbar** (getestet, liefert leere JS-Hülle) — Substanz kommt von den Marken-Websites, Journals und gezielter WebSearch.
- **Höchstens eine Erkenntnis** fließt in die Posts des Tages ein. Mehr wird Imitation.
- Vor jeder Übernahme die Abgrenzungsregel: *Wäre dieser Post ohne Logo und Produktnamen noch als ZinCuTec erkennbar?* Bei Nein: nicht übernehmen.

### 2. Konzipieren
Zwei Posts pro Lauf: **ein Träger-Post** (Produkt/Detail/Raum) und **ein Zweitkonzept** aus einer anderen Säule. Für jeden:
- Produkt + konkreter Bildwinkel (nicht „ein Foto von KINKO", sondern „KINKO Set 3, Streiflicht von links, Fokus auf die Kante wo Messing in Schatten kippt")
- Caption nach der Architektur in `references/content-system.md`
- Hashtag-Set (Mix aus Reichweite/Nische/Marke, nie derselbe Block zweimal)
- Empfohlenes Zeitfenster

### 3. Bilder holen
Bildquellen in dieser Reihenfolge — Details und Ordner-IDs in `references/pipeline.md`, Abschnitt 0:

1. **`00_LOUISVI_FOLDERSTRUCTURE`** (`1DjKwaiyERdvjy-rpCRgw0gl8fb3FVX3p`) — **die primäre Quelle.** 25 Produktordner, je mit `1. RD` (Renderings), `2. S` (echte Fotografie, erste Wahl) und `3. SH` (Shooting nach Finish).
2. Reels-Material: „Zincutec Reels Export Folder" (`1lvT_erWX6EYiBq-n39SFoLqkL7T1sTuY`)
3. Shopify-CDN aus dem `.json` des Produkts — nur als Rückfall. Meist Renderings, schwächer bei Materialwahrheit.

**Pflicht: das Bild ansehen, nicht nach Dateinamen wählen.** Zwei bis vier Kandidaten herunterladen, verkleinern, mit `Read` betrachten, dann entscheiden. Der Weg über die Zwischendatei steht in `pipeline.md` — er hält den Base64-String aus dem Kontext.

**Canva kann Drive-Bilder nicht selbst laden** (keine öffentliche URL). Der Agent wählt das Bild, legt es in den Drive-Tagesordner und nennt Louis Ordner und Dateiname exakt zum Hineinziehen. Niemals ersatzweise ein schwächeres CDN-Bild einsetzen, nur weil das automatisierbar wäre.

Bildwahl-Kriterien stehen in `references/quality-rubric.md`, Abschnitt „Bild". Ein schwaches Bild kippt den ganzen Post — lieber ein anderes Produkt wählen als ein mittelmäßiges Bild aufwerten wollen.

### 4. Bauen
- **Zuerst die Skill `canva-design-style` lesen** — Louis' dokumentiertes Designsystem ist die Quelle der Wahrheit. `references/design-system.md` überträgt es nur auf die Instagram-Formate.
- Canva-Design im Ordner `FAHSlXE3Mxs`, Format 4:5 (1080×1350) für Feed, 9:16 (1080×1920) für Story/Reel-Cover.
- Harte Konstanten: **nur Helvetica**, Hintergrund `#f6f6f6`/`#fafaf7`, Produktnamen ALL CAPS, Microline `TURNING METAL INTO ART.` oben rechts, deutsches Zahlenformat (`100 × 63 × 27,5 cm`), kursiv nur an einer Stelle, keinerlei Dekoration.
- **Wirkt eine Fläche zu voll, wird ein Element gelöscht — nicht verkleinert.** Die Leere ist das Design.
- Sobald ein erster Post steht, wird er zur Vorlage: duplizieren und Bild im bestehenden Rahmen tauschen, statt neu zu bauen.
- Benennung: `YYYY-MM-DD_<PRODUKT>_<FORMAT>` — z. B. `2026-08-18_KINKO_4x5`.

### 5. Selbst prüfen (der eigentliche Wert dieses Agents)
**Pflicht, nicht optional.** Vollständiges Verfahren in `references/quality-rubric.md`:
- Erst die **Hard Rejects** durchgehen. Ein Treffer = Post fliegt raus, keine Reparatur, neu konzipieren.
- Dann die **10 Kriterien** scoren. Unter 75/100 → überarbeiten. Zweimal unter 75 → verwerfen und Thema wechseln.
- Dann den **Fremdblick-Pass**: den fertigen Post gegen die Referenzmarken lesen (`references/competitors.md`). Würde er neben Frama oder New Works auffallen — oder untergehen? Und: wäre er ohne Logo noch als ZinCuTec erkennbar?
- Dann die **Layout-Prüffragen** aus `references/design-system.md` (Helvetica, Hintergrundton, Zahlenformat, Kursiv-Disziplin).
- Faktencheck: Preise, Maße, Materialbezeichnungen, Lieferzeiten gegen zincutec.eu. **Keine erfundenen Zahlen.** Wo die Website nichts hergibt: „auf Anfrage".

Nur was besteht, wird abgelegt. Was durchfällt, kommt mit Begründung in den Log — das ist Information, kein Scheitern.

### 6. Ablegen
- Drive: Tagesunterordner `YYYY-MM-DD` in der Queue. Darin pro Post das Bild plus `<PRODUKT>_caption.txt` mit Caption, Hashtags, Zeitfenster, Score und den offenen Punkten.
- Canva: Design im Ordner, Titel nach Namensschema.
- `state/content-log.md` fortschreiben: Datum, Produkt, Säule, Winkel, Score, Status, Drive-/Canva-Link.

### 7. Melden
Kurzmeldung an Louis in Slack `#zincutec-graphic-design-chat` (`C0BQN0X6SQK`). Format:

```
ZinCuTec IG — <Datum>
Fertig: <n> Post(s) → <Drive-Link>
1. <PRODUKT> · <Säule> · Score <x>/100
2. <PRODUKT> · <Säule> · Score <x>/100
Verworfen: <Produkt> (<Grund in einem Halbsatz>)
Offen: <was Louis entscheiden muss, oder "nichts">
```

Neutral, keine Floskeln, keine Selbstbewertung des Agents. Wenn nichts bestanden hat, wird das genauso gemeldet — mit Grund.

## Wenn etwas blockiert

- **Slack nicht erreichbar** → Telegram, sonst Routine-Kanal. Blocker in den Log, weiterarbeiten.
- **Canva-Transaktion scheitert** → Bild + Caption trotzdem in Drive ablegen, Canva-Teil als offen melden.
- **Website nicht erreichbar** → Posts ohne harte Zahlen bauen (Materialsprache statt Preisangabe), im Log vermerken.
- **Kein Bild auf Niveau verfügbar** → keinen Post erzwingen. Melden, welches Motiv fehlt. Ein Tag ohne Post ist besser als ein schwacher Post.

## Referenzen

- `references/brand-dna.md` — Stimme, Bildsprache, Positionierung, Substanzquellen, was ZinCuTec **nicht** ist
- `references/quality-rubric.md` — Hard Rejects, 10-Kriterien-Score, Fremdblick-Pass
- `references/competitors.md` — eigener Feed + 8 Wettbewerber, Analysemethode, Abgrenzungsregel
- `references/design-system.md` — Instagram-Layouts nach Louis' Canva-Designsystem
- `references/content-system.md` — Säulen, Formate, Caption-Architektur, Hashtag-Strategie, Wochenrhythmus
- `references/catalog.md` — 27 Produkte mit Finishes, Preisspannen, Bildbestand
- `references/pipeline.md` — Bildquellen mit Ordner-IDs, konkrete Tool-Aufrufe für Drive, Canva, Slack
- `tools/layout_preview.py` — erzeugt eine 1080×1350-Layoutvorschau aus einem Bild; nützlich, um eine Bildwahl zu prüfen, bevor Louis sie in Canva baut

**Verwandte Skills:** `canva-design-style` (Louis' Designsystem — vor jedem Canva-Bau lesen), `zincutec-katalog-design-workflow` (gemessene Template-Geometrie, Canva-API-Fallstricke).
