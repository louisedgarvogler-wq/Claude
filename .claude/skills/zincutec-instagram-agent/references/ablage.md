# Ablagestruktur — Drive und Canva

**Regel: ein Post = ein Ordner.** In Drive und in Canva, mit identischer Benennung. Wer einen Ordnernamen liest, weiß ohne Öffnen, worum es geht.

---

## Benennungsschema (verbindlich)

```
YYYY-MM-DD_PRODUKT_SAEULE_FORMAT
```

| Teil | Regel | Beispiel |
|---|---|---|
| `YYYY-MM-DD` | Produktionsdatum, nicht Posting-Datum | `2026-08-18` |
| `PRODUKT` | ALL CAPS, Katalogschreibweise, Leerzeichen zu `-` | `ZEN-COFFEE-TABLE` |
| `SAEULE` | `OBJEKT` · `RAUM` · `DETAIL` · `PROZESS` · `KONTEXT` · `KOLLEKTION` | `DETAIL` |
| `FORMAT` | `4x5` · `9x16` · `CAROUSEL` · `REEL` | `4x5` |

Vollständig: `2026-08-18_ZEN-COFFEE-TABLE_DETAIL_4x5`

Umlaute und Sonderzeichen niemals in Ordner- oder Dateinamen. Zwei Posts am selben Tag zum selben Produkt: Suffix `_A`, `_B`.

---

## Google Drive

Wurzel: **Zincutec Instagram Queue** — `1_bI4QKyxkM0710ZWsYA0PtO2nb4Oset1`

| Statusordner | Drive-ID |
|---|---|
| `01_FREIGABE_OFFEN` | `14Q1xUlZ8FlLuzCfqaTFA-8I4gLeuOa_P` |
| `02_FREIGEGEBEN` | `1DrA6_5NAtAeYDIM_dVBlii8M9lKG23tW` |
| `03_VEROEFFENTLICHT` | `1yKVsolnq4vnjtOCegZPT8d6TIu2VNPpy` |
| `09_AUSSORTIERT` | `1dMWFBjQaj9aYE17TsD6mVQk_ggcY1WsN` |

```
Zincutec Instagram Queue/
├─ 01_FREIGABE_OFFEN/          ← wartet auf Louis
│  └─ 2026-08-18_KINKO_RAUM_4x5/
│     ├─ 01_BILD_KINKO_RAUM_4x5.jpg
│     ├─ 02_CAPTION.txt
│     ├─ 03_BEWERTUNG.txt
│     └─ 04_LAYOUT_VORSCHAU.jpg
├─ 02_FREIGEGEBEN/             ← Louis verschiebt hierher
├─ 03_VEROEFFENTLICHT/         ← nach dem Posten
└─ 09_AUSSORTIERT/             ← durchgefallen oder zurückgestellt
   └─ 2026-08-17_KINKO_RAUM_4x5_DURCHGEFALLEN/
      └─ 00_GRUND.txt
```

**Die vier Statusordner sind fest.** Der Agent legt ausschließlich in `01_FREIGABE_OFFEN` und `09_AUSSORTIERT` ab. `02` und `03` gehören Louis — der Agent liest sie nur, um zu erkennen, was schon durch ist.

**Dateien im Post-Ordner, immer diese vier, immer nummeriert:**

| Datei | Inhalt |
|---|---|
| `01_BILD_<PRODUKT>_<FORMAT>.jpg` | Das gewählte Bild, auf Zielmaß skaliert |
| `02_CAPTION.txt` | Caption, Hashtags, Zeitfenster — nur das, was Louis kopiert |
| `03_BEWERTUNG.txt` | Score im Detail, Bildbegründung, offene Punkte, Quellpfad |
| `04_LAYOUT_VORSCHAU.jpg` | Vorschau aus `tools/layout_preview.py` |

Caption und Bewertung sind bewusst **getrennt**: Louis kopiert aus `02` und muss dabei nicht an Scores vorbeiscrollen.

---

## Canva

Wurzel: **Zincutec Instagram** — `FAHSlXE3Mxs`

| Statusordner | Canva-ID |
|---|---|
| `00_MASTER` | `FAHSldlu36c` |
| `01_FREIGABE_OFFEN` | `FAHSlZYzVng` |
| `02_FREIGEGEBEN` | `FAHSlZ80VHc` |
| `03_VEROEFFENTLICHT` | `FAHSlci-EZw` |
| `09_AUSSORTIERT` | `FAHSlRlcVGo` |

```
Zincutec Instagram/
├─ 00_MASTER/                  ← die Vorlagen, nie überschreiben
│  ├─ MASTER_4x5
│  ├─ MASTER_9x16
│  └─ MASTER_CAROUSEL
├─ 01_FREIGABE_OFFEN/
│  └─ 2026-08-18_KINKO_RAUM_4x5
├─ 02_FREIGEGEBEN/
├─ 03_VEROEFFENTLICHT/
└─ 09_AUSSORTIERT/
```

Gleiche Statusordner, gleiche Namen wie in Drive — ein Post ist in beiden Systemen unter demselben Namen auffindbar.

**`00_MASTER` ist unantastbar.** Nie direkt darin arbeiten. Ablauf: `copy-design` vom passenden Master → Kopie umbenennen nach Schema → `move-item-to-folder` nach `01_FREIGABE_OFFEN` → dann erst editieren.

Ordner anlegen mit `mcp__Canva__create-folder` und `parent_folder_id: "FAHSlXE3Mxs"`; Designs verschieben mit `mcp__Canva__move-item-to-folder`.

---

## Beim Aussortieren

Auch Verworfenes bekommt einen Ordner — sonst geht die Begründung verloren und der Fehler wiederholt sich.

Ordnername endet auf `_DURCHGEFALLEN` oder `_ZURUECKGESTELLT`. Darin mindestens `00_GRUND.txt`: welches Kriterium gerissen wurde, welcher Score, was stattdessen zu tun ist.

---

## Prüfung am Ende jedes Laufs

1. Trägt jeder neue Ordner das vollständige Schema?
2. Liegt jeder Post in genau einem Statusordner?
3. Heißt der Canva-Ordner exakt wie der Drive-Ordner?
4. Sind alle vier Dateien vorhanden — oder ist das Fehlen im Report benannt?
5. Keine losen Dateien direkt in der Queue-Wurzel?

Eine Abweichung wird sofort korrigiert, nicht gemeldet und liegengelassen.
