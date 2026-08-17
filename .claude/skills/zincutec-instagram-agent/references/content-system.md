# Content-System

## Die sechs Säulen

Jeder Post gehört zu genau einer Säule. Der Wochenrhythmus mischt sie, damit der Feed nicht kippt.

| Säule | Anteil | Was es ist | Beispiel |
|---|---|---|---|
| **Objekt** | 30 % | Das Stück als Skulptur, isoliert, Studiolicht | MONOLITH GOLDEN PEAK freigestellt, Streiflicht von rechts |
| **Raum** | 25 % | Produkt im bewohnten Kontext, Proportion lesbar | ZEN DINING TABLE 300 cm im Altbau, Nachmittagslicht |
| **Detail** | 20 % | Makro auf Material, Kante, Naht, Patina | TUKKON-Zylinder, Übergang Patina zu Hochglanz |
| **Prozess** | 15 % | Manufaktur, Hand, Werkzeug — komponiert, nicht dokumentarisch | Brünierbad, Hand mit Tuch auf Messing |
| **Kontext** | 7 % | Materialkultur, Referenz, Namensherkunft | Was YUGEN bedeutet und warum das Regal so heißt |
| **Kollektion** | 3 % | Neuheit, Auflage, Set-Logik | INFINITY BOOKSHELF als Set of 10 |

**Nie zwei gleiche Säulen hintereinander.** Nie dasselbe Produkt zweimal in 21 Tagen.

## Produktpriorität — Neues zuerst

**Bei der Produktwahl haben Neuheiten Vorrang.** Der Feed soll zeigen, was gerade entsteht, nicht die immer gleichen Bestseller durchrotieren.

Reihenfolge bei sonst gleicher Eignung:

1. **Shop-Tag `Neu`** — live aus `https://zincutec.eu/en/collections/alle-pieces/products.json?limit=250` prüfen, nie aus der Referenz. Stand 17.08.2026: OYAKATA, YUGEN, YORU, ORIGAMI, KANJI, PYRAMID TABLE, INFINITY BOOKSHELF, TUKKON CHAIR, TUKKON CONSOLE, THE ROYAL GAME.
2. **Frisches Bildmaterial** — Produktordner in `00_LOUISVI_FOLDERSTRUCTURE`, deren Dateien zuletzt geändert wurden. Neue Aufnahmen sind ein Signal, dass Louis dort gerade arbeitet.
3. **Nie oder lange nicht gezeigt** — Rotationstabelle im `content-log.md`, Spalte „Zuletzt" leer oder weit zurück.
4. **Bestseller** — KINKO, ZEN DINING, ZEN COFFEE, TUKKON TABLE, TAISHO, REFLECTION. Erst wenn nichts aus 1–3 trägt, oder wenn ein Bestseller ein außergewöhnlich starkes neues Motiv hat.

**Die Ausnahme:** Bildqualität schlägt Neuheit. Ein Neuprodukt mit schwachem Material wird nicht erzwungen — dann lieber ein älteres Stück mit einem Bild, das die Rubrik trägt. Die Priorität ordnet gleich starke Kandidaten, sie rechtfertigt keinen schwachen Post.

Wenn ein Neuprodukt nur schwaches Material hat: im Report benennen, welches Motiv fehlt. Das ist eine Shooting-Ansage an Louis.

## Wochenrhythmus (Richtwert)

| Tag | Säule | Format |
|---|---|---|
| Mo | Objekt | 4:5 Single |
| Di | Detail | 4:5 Carousel (3–5 Slides) |
| Mi | Raum | 4:5 Single |
| Do | Prozess | Reel-Konzept 9:16 |
| Fr | Objekt | 4:5 Carousel |
| Sa | Kontext | 4:5 Single |
| So | — | frei / Story-Material |

Der Rhythmus ist Vorgabe, kein Zwang. Wenn das beste verfügbare Bild am Mittwoch ein Detail ist, wird es ein Detail — und der Log vermerkt die Abweichung.

## Caption-Architektur

Vier Teile, in dieser Reihenfolge:

**1. Haken (1 Zeile, max. ~60 Zeichen)**
Muss ohne den „mehr"-Klick tragen. Kein Produktname als Eröffnung — der Name ist keine Aussage.

> Die Patina lässt sich nicht zweimal gleich auftragen.

**2. Substanz (1–3 Sätze)**
Aus den Substanzquellen in `brand-dna.md`. Ein konkreter Fakt schlägt drei Adjektive.

**3. Produktzeile (1 Zeile)**
Name, Finish, ggf. Maß. Nüchtern.

> KINKO — Set 3, Messing brüniert.

**4. Stiller Abschluss (optional, 1 Zeile)**
Kein Imperativ. Ein Hinweis reicht.

> Manufaktur seit 2000, Deutschland.

**Gesamtlänge:** 40–90 Wörter im Regelfall. Kontext-Posts dürfen bis 150. Alles darüber wird gestrichen, nicht gerechtfertigt.

**Sprache:** Deutsch als Standard, Englisch bei internationalen Motiven oder Reels. Nie gemischt im selben Block. Zweisprachig nur als sauber getrennte Absätze.

## Hashtags

**Aufbau:** 12–18 Tags, in drei Gruppen gemischt, als Kommentar oder ans Caption-Ende nach Leerzeilen.

| Gruppe | Anzahl | Zweck | Beispiele |
|---|---|---|---|
| Reichweite (100k–1M Posts) | 4–5 | Sichtbarkeit | `#interiordesign` `#furnituredesign` `#minimalinterior` |
| Nische (10k–100k) | 6–8 | Qualifiziertes Publikum | `#brassfurniture` `#sculpturalfurniture` `#steelfurniture` `#collectibledesign` `#materialstudy` `#handmadefurniture` |
| Marke / Produkt | 2–4 | Wiedererkennung | `#zincutec` `#metalbecomesart` `#<produktname>` |

**Regeln**
- Nie derselbe Block zweimal in Folge — mindestens ein Drittel rotieren.
- Keine Tags über 5 Mio. Posts (`#design`, `#home`) — reine Verdünnung.
- Keine irreführenden Tags (`#vintage`, `#antique`) für Neuware.
- Keine Engagement-Tags (`#l4l`, `#followme`) — im Luxussegment sofort disqualifizierend.

## Zeitfenster (CEST, Richtwert)

- **Beste Fenster:** Di–Do 18:00–20:30, Sa 10:00–12:00
- **Vermeiden:** Mo vormittags, Fr abends
- Reels früher am Abend als Feed-Posts.

Wenn Instagram-Insights vorliegen, schlagen sie diese Richtwerte. Bis dahin gilt die Tabelle.

## Carousel-Logik

Wenn Carousel, dann mit Dramaturgie — nicht als Bilderhaufen:

1. **Slide 1** — der stärkste Frame. Entscheidet allein über den Stopp.
2. **Slide 2–3** — Annäherung: weiter → näher, oder Kontext → Detail.
3. **Slide 4** — Material-Makro. Der Beweis für Handarbeit.
4. **Slide 5** (optional) — Maßstab oder Set-Variante.

Nie mehr als 5 Slides. Nie zwei Slides mit demselben Bildabstand hintereinander.

## Reel-Konzepte

Für Prozess-Posts. Kurze Struktur, kein Trending-Audio ohne Bezug:

- **0–1 s:** harter Materialframe, Bewegung schon im Bild
- **1–5 s:** ein einziger Fertigungsschritt, ungeschnitten
- **5–10 s:** Ergebnis im Raum
- **Ton:** Werkstattgeräusch oder ruhige Ambient-Spur. Louis produziert Melodic House — eigene Spuren sind zulässig und markenstärkend.
- **Text im Bild:** höchstens eine Zeile, nie über dem Produkt.
