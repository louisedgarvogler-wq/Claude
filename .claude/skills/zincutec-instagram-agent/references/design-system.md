# Design-System für Instagram-Formate

**Quelle der Wahrheit ist die Skill `canva-design-style`** — Louis' dokumentiertes Designsystem. Vor jedem Canva-Bau lesen. Diese Datei überträgt es nur auf Instagram-Formate und ersetzt es nicht.

Zusätzliche Referenz: Pinterest-Board `pinterest.com/filmedbylouis/zincutec-katalog` (22 Pins, Themen: Book Design, Furniture Magazine, Graphic Design Layouts). Richtung: **Editorial-Print, nicht Social-Grafik.** Ein ZinCuTec-Post soll wie eine Magazinseite aussehen, die zufällig quadratisch beschnitten ist.

---

## Die nicht verhandelbaren Konstanten

Direkt aus `canva-design-style` übernommen — hier gelten sie unverändert:

| Element | Vorgabe |
|---|---|
| **Schrift** | **Nur Helvetica.** Helvetica Neue oder Helvetica Now Display. Nichts anderes, nie. |
| **Hintergrund** | Nahezu weiß: `#f6f6f6` oder `#fafaf7`. Kein reines Weiß, kein Farbton. |
| **Produktnamen** | ALL CAPS — `KINKO`, `TUKKON TABLE`, `ZEN COFFEE TABLE` |
| **Marken-Microline** | `TURNING METAL INTO ART.` — winzig, oben rechts |
| **Wortmarke** | `ZinCuTec`, gesperrt, klein, oben links |
| **Kursiv** | Ausschließlich für die eine poetische Zeile pro Layout. Sonst nie. |
| **Zahlenformat** | Deutsch: Dezimalkomma, gespertes ×. `100 × 63 × 27,5 cm`, `30 kg` |
| **Ausrichtung** | Textspalte rechtsbündig (align end), wie im Katalog |
| **Dekoration** | Keine. Keine Rahmen, Schatten, Verläufe, Icons, Sticker. |

**Die Leere ist das Design.** Wenn ein Layout überladen wirkt, wird ein Element **gelöscht**, nicht verkleinert. Das ist Louis' dokumentierte Arbeitsweise und gilt hier genauso.

---

## Format 4:5 — Feed (1080 × 1350 px)

Der Katalog ist Querformat mit Bild links und Spaltentext rechts. Im Hochformat kippt diese Anatomie:

```
┌─────────────────────────────┐
│ ZinCuTec      TURNING METAL │  ← Kopfzeile, winzig, Wortmarke links /
│                    INTO ART.│     Microline rechts
│                             │
│   ┌─────────────────────┐   │
│   │                     │   │
│   │      BILD           │   │  ← ein starkes Bild, großzügige Ränder
│   │   (~62 % Höhe)      │   │     rundum. Nie randabfallend.
│   │                     │   │
│   └─────────────────────┘   │
│                             │
│                    KINKO    │  ← Produktname ALL CAPS, rechtsbündig
│      Messing brüniert       │  ← Spezifikationszeile, rechtsbündig
│                             │
│   Die Patina folgt der      │  ← optionale kursive Zeile,
│   Hand, die sie auftrug.    │     max. zwei Zeilen
└─────────────────────────────┘
```

**Typohierarchie** (aus dem Katalog übertragen — Verhältnis zählt, nicht die Absolutzahl):
- Produktname: größte Stufe, entspricht dem Katalog-Seitentitel
- Kursive Zeile: ca. 70 % davon
- Spezifikationen: ca. 55 %
- Kopfzeile: ca. 20 %, sehr klein

**Ränder:** links/rechts mindestens 80 px, oben/unten mindestens 100 px. Im Zweifel mehr.

**Wichtigste Variante — das reine Bild:** Für Detail- und Objekt-Posts ist ein Layout ohne jeden Text oft stärker. Bild randabfallend, Caption trägt den Text. Wenn ein Bild allein trägt, **soll es allein stehen**. Kriterium 3 der Rubrik belohnt das.

---

## Format 9:16 — Story und Reel-Cover (1080 × 1920 px)

- Gleiche Anatomie, mehr vertikale Luft.
- **Sichere Zonen:** oben 250 px und unten 320 px freihalten — dort liegen Instagrams eigene UI-Elemente.
- Text nur im mittleren Drittel.
- Bei Reel-Covern: der Produktname darf allein stehen, kein Spezifikationsblock.

---

## Carousel

Wie eine Magazinstrecke aufbauen, nicht als Bilderstapel:

- **Slide 1** trägt die volle Anatomie (Kopfzeile, Bild, Name, Spezifikation).
- **Slide 2–5** sind reine Bilder, nur mit der Kopfzeile. Kein wiederholter Produktname.
- Hintergrundton über alle Slides identisch — der Wisch soll ruhig laufen.
- Nie zwei Slides mit demselben Bildabstand hintereinander.

---

## Canvas KI-Generierung ist unbrauchbar — getestet

**`generate-design` NICHT für ZinCuTec-Posts verwenden.** Am 2026-08-17 mit einem sehr präzisen Prompt getestet (Helvetica, `#f6f6f6`, keine Dekoration, nur das gelieferte Bild). Ergebnis, vier Seiten:

| Verstoß | Befund |
|---|---|
| Falsche Schrift | Display-Serife (`fontRef=YAFMTwAmi5M`), nicht Helvetica — trotz expliziter Vorgabe |
| Dekoration | Abgerundete Bildecken (`cornerRounding=23`), brauner Rahmen `#62442e`, Pfeil-Grafik |
| **Erfundenes Logo** | Ein frei erfundenes ZINCUTEC-Bildzeichen (`mediaId=MAFbQ_ti1Go`) |
| **Falsche Produkte** | Seite 2 zeigt einen erfundenen Messingschrank, Seite 3 einen Holztisch — beides kein ZinCuTec |
| **Erfundene Telefonnummer** | Seite 4: „FOR INQUIRIES, CALL (12) 3456-7890" |
| Sprachmischung | „Messing brüniert craftsmanship with a unique design aesthetic" — plus Superlativ |

Einziger Treffer: der Hintergrund war korrekt `#f6f6f6`.

Erfundene Logos, fremde Produkte und frei erfundene Kontaktdaten auf einem Marken-Asset sind Hard Rejects. Das Ergebnis liegt als **`DURCHGEFALLEN 2026-08-17 KINKO`** im Canva-Ordner — als Beleg, nicht zur Verwendung.

**Konsequenz — der einzig gangbare Weg:** Louis baut **einmalig** ein 4:5-Master-Design von Hand (Helvetica, korrektes Logo, richtige Ränder). Danach arbeitet der Agent ausschließlich per `copy-design` + Bildtausch im bestehenden Rahmen. Das ist exakt Louis' dokumentierte Arbeitsweise — „duplizieren, nie neu bauen" — und umgeht zugleich die Schriftbeschränkung von `add_text`, weil die Schrift aus dem Master vererbt wird.

Solange kein Master existiert: Bild und Textspezifikation in Drive ablegen, Canva-Schritt als offen melden. **Keinen KI-Entwurf als Ersatz ablegen.**

## Bauweise in Canva

Louis' Regel „duplizieren statt neu bauen" gilt auch hier:

1. **Sobald ein erster Post steht, wird er zur Vorlage.** Design duplizieren, Bild in den bestehenden Rahmen tauschen (Crop bleibt erhalten), Text überschreiben.
2. Textelemente aus einem bestehenden Design kopieren, statt sie neu anzulegen — nur so werden Schrift, Größe und Ausrichtung exakt übernommen.
3. **`add_text` kann die Schriftfamilie nicht setzen.** Neu angelegter Text landet in Canvas Standardschrift, nicht in Helvetica. Zwei Konsequenzen:
   - Wo möglich bestehende Elemente duplizieren statt neuen Text anzulegen.
   - Wo neuer Text unvermeidbar ist: **im Report ausdrücklich vermerken**, damit Louis die Schrift in einem Durchgang korrigiert.
4. Größen und Ausrichtung per `format_text` im zweiten Aufruf setzen — `add_text` legt bei 16 px an.
5. Weitere API-Fallstricke in `pipeline.md` und in `zincutec-katalog-design-workflow/references/template-geometry.md`.

---

## Prüffragen vor dem Ablegen

Zusätzlich zur Rubrik, speziell fürs Layout:

1. Ist die Schrift Helvetica? (Wenn nein: als offenen Punkt melden.)
2. Ist der Hintergrund `#f6f6f6`/`#fafaf7` — nicht reines Weiß?
3. Wirkt eine Fläche zu voll? Dann ein Element löschen, nicht verkleinern.
4. Deutsches Zahlenformat mit Dezimalkomma und gespertem `×`?
5. Kursiv nur an genau einer Stelle?
6. Würde dieses Layout in einem Möbelmagazin funktionieren — oder sieht es nach Social-Grafik aus?
