# Pipeline — konkrete Tool-Aufrufe

## Feste IDs

| Ressource | ID |
|---|---|
| Drive: Zincutec Instagram Queue | `1_bI4QKyxkM0710ZWsYA0PtO2nb4Oset1` |
| Drive: Zincutec (Elternordner) | `10cixaBHjf8G6ypeC4gnMCbRrsSFq7Gyt` |
| Drive: Zincutec Stills | `1QSXPmz48_mTFeFkAlSWPlcfEBdJcshPd` |
| Drive: Zincutec RAW | `1eC7hjhIja5etWWXM8ePMVoUk-YBwnJp4` |
| Drive: Zincutec Reels Export | `1lvT_erWX6EYiBq-n39SFoLqkL7T1sTuY` |
| Drive: UGC Content | `1SNRWsZ2ewyeWGo4XiUZSmQwU1ATJhJfN` |
| Canva: Zincutec Instagram | `FAHSlXE3Mxs` |
| Canva: Katalog-Design (Referenz für Stil) | `DAHRCVv3px8` |

## 1. Produktdaten live holen

```bash
curl -s "https://zincutec.eu/products/<handle>.json"
```

Liefert Beschreibung, alle Varianten mit Preisen und alle Bild-URLs. Die Collection-Übersicht:

```bash
curl -s "https://zincutec.eu/en/collections/alle-pieces/products.json?limit=250"
```

**Bild-Namensheuristik auf dem Shopify-CDN:** `*-2` ist meist die weite Raumaufnahme, `-3/-4/-5` sind Detailaufnahmen, `*-1-square` der freigestellte Packshot.

## 2. Tagesordner in Drive anlegen

`mcp__Google_Drive__create_file`

```json
{
  "title": "2026-08-18",
  "contentMimeType": "application/vnd.google-apps.folder",
  "parentId": "1_bI4QKyxkM0710ZWsYA0PtO2nb4Oset1"
}
```

## 3. Caption-Datei ablegen

`mcp__Google_Drive__create_file` mit `textContent`, `contentMimeType: "text/plain"`, `disableConversionToGoogleType: true`, `parentId` = Tagesordner.

Dateiname: `<PRODUKT>_caption.txt`. Inhalt:

```
POST — 2026-08-18 · KINKO · Säule: Objekt
Format: 4:5 (1080×1350) · Zeitfenster: Di 18:30 CEST
Score: 87/100

--- CAPTION ---
<Text>

--- HASHTAGS ---
<Tags>

--- BILD ---
Quelle: <URL oder Drive-Pfad>
Winkel: <Beschreibung>

--- OFFENE PUNKTE ---
<was Louis prüfen sollte, oder "keine">

--- CANVA ---
<Design-URL>
```

## 4. Bild in Drive legen

Bild herunterladen, dann `mcp__Google_Drive__create_file` mit `base64Content`, passendem `contentMimeType` (`image/jpeg`/`image/png`) und `disableConversionToGoogleType: true`.

## 5. Canva-Design bauen

1. `mcp__Canva__upload-asset-from-url` — Shopify-CDN-URLs funktionieren direkt. **Drive-`uc?export=download`-URLs funktionieren nicht** — solche Bilder erst lokal laden und als Asset hochladen.
2. `mcp__Canva__generate-design-structured` oder `create-design-from-candidate` für ein neues 4:5- bzw. 9:16-Design.
3. `mcp__Canva__move-item-to-folder` → Zielordner `FAHSlXE3Mxs`.
4. `mcp__Canva__read-design` mit `open_transaction: true`, dann `edit-design` für Feinarbeit.

**Gotchas aus der Katalogarbeit (gelten hier genauso):**
- In der CDF bedeutet `pos: a,b` → **top, left** (y zuerst).
- `crop_media` erwartet `left`/`top` vertauscht gegenüber dem gedruckten `imageBox=(top,left w×h)`.
- `add_text` kann die Schriftfamilie nicht setzen — Text landet in Canvas Standardfont. Größen/Ausrichtung per `format_text` im zweiten Aufruf. Im Report erwähnen, damit Louis die Schrift in einem Durchgang korrigiert.
- `commit`/`cancel` ohne Operationen aufrufen; Commit schließt die Transaktion.
- Alle 1–3 Seiten committen, damit fertige Arbeit nicht verloren geht.

## 6. Melden

**Telegram** (bevorzugt) — `mcp__Zapier__execute_zapier_write_action`

```json
{
  "selected_api": "TelegramCLIAPI",
  "action": "send_message",
  "params": { "chat_id": "<Chat>", "text": "<Report>", "format": "Plain Text" }
}
```

Telegram muss einmalig verbunden werden (siehe `state/content-log.md`, Abschnitt Setup). Solange keine Verbindung besteht: Report über den Push/E-Mail-Kanal des Routine-Laufs ausgeben und den Blocker im Log vermerken.

**Kein Instagram-Publishing.** Der Agent hat bewusst keinen Zugriff auf `InstagramBusinessCLIAPI`. Das ist Absicht, kein fehlendes Setup — nicht „nachrüsten", ohne dass Louis es ausdrücklich verlangt.

## 7. Log fortschreiben

`state/content-log.md` in diesem Skill um eine Zeile pro Post ergänzen — auch für verworfene Konzepte, mit Grund. Der Log ist das Gedächtnis des Agents; ohne ihn wiederholt er sich.
