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

## 0. Bildquelle — `00_LOUISVI_FOLDERSTRUCTURE` (primär)

**Das ist die wichtigste Bildquelle. Immer zuerst hier suchen, nicht auf der Shopify-CDN.**

Wurzel: `1DjKwaiyERdvjy-rpCRgw0gl8fb3FVX3p` (liegt in „VIDEOS LOUIS XI", Eigentümer kontakt@zincutec.eu)

25 nummerierte Produktordner. Pro Produkt drei Unterordner-Typen:

| Präfix | Bedeutung | Wert für Instagram |
|---|---|---|
| `1. RD <PRODUKT>` | **Renderings** — CGI, teils auch Rendering-Videos (.mp4) | Stark im Bildaufbau, aber CGI. Kostet Punkte bei Materialwahrheit. |
| `2. S <PRODUKT>` | **Shooting** — echte Fotografie (`DSC*.jpg`, `<PRODUKT> 1–45.jpg`), bis 26 MB | **Erste Wahl.** Echtes Licht, echte Patina, echte Schatten. |
| `3. SH <PRODUKT> <FINISH>` | Weiteres Shooting, nach Finish getrennt | Zweite Wahl, gut für Finish-spezifische Posts. |

Dazu je Produkt ein `.docx` mit dem Produkttext (z. B. „Kinkō Bücherregal Text.docx").

**Bekannte Ordner-IDs**

| Produkt | ID | Produkt | ID |
|---|---|---|---|
| 1. ZEN DINING | `1S6xTOYgWwM2Qfob9brfitPX1As4czqyj` | 13. BOOKSHELF INFINITY | `1eh-XMm1TIPmE7TZaWyJTknAn67h0qKIs` |
| 2. PYRAMID TABLE | `1t9la7k2pU1ozypUX1BqtCcOUkndfttoI` | 14. JIKU | `1kuiiTuYUU7xIxg_3oS9OFfniNGW9VUJ8` |
| 3. SAMURAI TABLE | `12uD0jVPxv2RmwOb43zY73QRkPDPJXHF9` | 15. ORIGAMI | `1VyEmtX7aTYnjEKRzJb35dI7Yg8doZZLT` |
| 4. SATORI TABLE | `14IjETXgJKVgmCu2MwFk1gHCEeGK6-ipr` | 16. ZEN BENCH | `1VTR0WHZwXQUhHTmWdqjTsCdazcbYzdlp` |
| 5. ZEN COFFEE TABLE | `1IJOA--xWwa0PK522J7VrDi5J6OtX1IFR` | 17. T-STOOL | `1OkCOJhivapUuWG-zbrQlNFi0ryiW-_tl` |
| 6. ELYSIAN | `1B1Ecv7dcrwFirZCG7COv3W7at-ivPBht` | 18. TUKKON CHAIR | `1fPT-HUEhIBb7-VPc4UbP5PI00CUiLtlf` |
| 6. TUKKON | `1FNCKXm7R7GW9hMkCprcjuJy_C_4iXaPL` | 19. REFLEXION | `1lLDFIcXJEGBFeOuVLMU4O1OzD9zVIwM2` |
| 7. KANJI | `18nHeXfpSMSUqMAnxhA15HDotqNiKVR5o` | 20. THE ROYAL GAME | `1gztmQ1akXW7IXP1_S7Inm-ybQNfwWiWk` |
| 8. OYAKATA | `1zL6-W8-IsmRBZFiZHbchwKCWJj8Nbmun` | 21. YORU | `1hx7K1qRkjrZQF6_O56rvW_28J41OBOOk` |
| 9. KINKO | `1ZdqEPM0VOUns_z1VgYjpscncdCTIEmH7` | 22. TUKKON CONSOLE | `1vSO05H3gs_Fsjyf1v3yvihPazm4jzl2e` |
| 10. TAISHO | `19GeMUSDOB3cZzrmvw9CUukCjX2Ol9KtR` | 23. ZEN CONSOLE | `1HpJsEptY5tImdMImY62ph_fGWtSYBCqT` |
| 11. CHOWA | `1oSY6W8k8R40n4ewKwMO-l56GtmadT3kb` | ARCHIVE PRODUCTS | `1H3HOe_h0CikXjTaF6_QvXjxW5Z8LSaY7` |
| 12. YUGEN | `1MRRkeZPernsE_Lk2EikgAcE6IiYgtTMm` | | |

Fehlt ein Produkt in der Tabelle: mit `search_files` und `parentId = '1DjKwaiyERdvjy-rpCRgw0gl8fb3FVX3p'` auflisten.

### Bilder wirklich ansehen — der Pflichtschritt

**Nie ein Bild allein nach dem Dateinamen wählen.** Der Agent muss es sehen, sonst kann er die Rubrik-Kriterien Bild, Licht und Komposition nicht bewerten.

`download_file_content` sprengt bei diesen Dateigrößen den Kontext und wird in eine Zwischendatei umgeleitet. **Das ist kein Fehler — das ist der vorgesehene Weg.** Von dort dekodieren, ohne den Base64-String je in den Kontext zu holen:

```python
import json, base64
from PIL import Image
d = json.load(open('<pfad-zur-zwischendatei>.txt'))
open('bild.jpg','wb').write(base64.b64decode(d['content']))
im = Image.open('bild.jpg')          # Originalmaß prüfen
im.thumbnail((900,900))               # verkleinern, sonst teuer
im.save('bild_v.jpg', quality=88)
```

Dann `bild_v.jpg` mit `Read` ansehen und bewerten. Pillow ist ggf. per `pip install Pillow` nachzuinstallieren; `ffmpeg` ist **nicht** verfügbar.

Zwei bis vier Kandidaten pro Post ansehen, dann entscheiden. Die Wahl mit Begründung in die Caption-Datei.

### Canva-Einschränkung bei Drive-Bildern

`upload-asset-from-url` braucht eine **öffentlich** erreichbare URL. Drive-Links sind das nicht, auch nicht als `uc?export=download`. Dateien aus diesem Ordner lassen sich daher **nicht** automatisch nach Canva bringen.

Konsequenz: Der Agent wählt und begründet das Bild, legt es in den Drive-Tagesordner, und nennt Louis **Ordner und Dateiname exakt**, damit er es in Canva ins bestehende Bildfeld zieht — dieselbe Handbewegung wie in seinem Katalog-Workflow. Kein Ersatzbild von der CDN einsetzen, nur weil das automatisierbar wäre.

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

**Reihenfolge nach Kosten — der erste erreichbare Kanal gewinnt.**

### 1. Telegram (Standard, kostenlos)

`mcp__Zapier__execute_zapier_write_action`

```json
{
  "selected_api": "TelegramCLIAPI",
  "action": "send_message",
  "params": { "chat_id": "<chat_id>", "text": "<Report>", "format": "Markdown" }
}
```

Einmalige Verbindung nötig; danach `chat_id` in `state/content-log.md` eintragen.

### 2. Push/E-Mail des Routine-Laufs (kostenlos, ohne Einrichtung)

Greift automatisch, wenn der Lauf über die Tages-Routine kommt. Report einfach als Abschlusstext ausgeben — er landet in Push und E-Mail. **Das funktioniert heute schon, ohne dass Louis etwas tut.**

### 3. Slack — nur wenn Louis es ausdrücklich will

Channel `#zincutec-graphic-design-chat`, ID `C0BQN0X6SQK`, via `mcp__Slack__slack_send_message`.

**Kostenhinweis:** Slack ist für Louis kostenpflichtig. **Nicht von sich aus dorthin melden.** Nur nutzen, wenn er es für den jeweiligen Zeitraum verlangt. Der Channel existiert und bleibt bestehen — er wird nur nicht automatisch bespielt.

Wenn kein Kanal erreichbar ist: Report in den Tagesordner in Drive schreiben und den Blocker im Log vermerken.

## 7. Log fortschreiben

`state/content-log.md` in diesem Skill um eine Zeile pro Post ergänzen — auch für verworfene Konzepte, mit Grund. Der Log ist das Gedächtnis des Agents; ohne ihn wiederholt er sich.
