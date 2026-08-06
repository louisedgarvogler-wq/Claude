---
name: ernaehrungs-log
description: Trägt Mahlzeiten, Gewicht und Training in Louis' Google Sheet "Ernährung & Performance 2026" ein und gibt danach immer die aktuelle Kalorienbilanz zurück. Nutze diese Skill, sobald Louis per Sprachnachricht oder Text sagt was er gegessen hat ("ich hatte gerade...", "zum Mittag gab es...", "hab 200 g Reis mit Lachs gegessen"), sein Gewicht meldet ("heute 95,4 kg"), ein Training ankündigt oder nachmeldet ("ich geh gleich boxen", "war eben laufen"), oder fragt wie viele Kalorien und Makros er heute noch übrig hat, wie die Bilanz steht, wie die Woche läuft oder ob er Richtung 88 kg im Plan liegt. Trigger auch bei "trag das ein", "wie steht's heute", "was hab ich noch übrig", "Ernährungssheet", "Kalorien heute", "meine Bilanz", "meine Woche".
---

# Ernährungs- und Performance-Log

Louis schickt meistens eine Sprachnachricht mit dem, was er gegessen hat. Der Ablauf ist bewusst auf zwei Tool-Calls begrenzt: **anhängen, dann Status lesen**. Die Nährwerte schätzt du selbst aus der Referenztabelle weiter unten, damit kein zusätzlicher Lesezugriff nötig ist.

## Stammdaten

- Spreadsheet-ID: `1tJ_-u7hcdAKkJbLwkGvbvqWs5sfqbWVMH64VQjaiLpc`
- Zugriff über die Zapier-Tools `google_sheets_make_api_get_request` und `google_sheets_make_api_mutating_request` (Google-Sheets-API v4, Konto louis.vi1997@gmail.com). Beide brauchen zusätzlich `method` und `fail_on_errors: "true"`.
- Sheet-Locale `de_DE`: Formeln mit Semikolon als Argumenttrenner, Datum `TT.MM.JJJJ`, Dezimalkomma
- Datum immer per `TZ=Europe/Berlin date +%d.%m.%Y` holen, nie schätzen
- Mehrere Bereiche pro GET funktionieren nicht: `values:batchGet` mit wiederholtem `ranges=` wird von Zapier auf den letzten Bereich reduziert. Immer einen zusammenhängenden Bereich lesen.

Körper: 1,92 m, 28 Jahre, männlich. Start 96 kg am 05.08.2026, Ziel 88 kg bis spätestens 05.02.2027.
Wettkämpfe: Tegernsee Halbmarathon 27.09.2026, Hyrox 01.11.2026.

## Standardablauf für eine Mahlzeit

### Schritt 1: Zeile anhängen

Spalten von `Mahlzeiten` (A bis K, elf Werte, Reihenfolge exakt einhalten):

| A | B | C | D | E | F | G | H | I | J | K |
|---|---|---|---|---|---|---|---|---|---|---|
| Datum | Uhrzeit | Mahlzeit | Was gegessen | Menge | Gramm | Kalorien | Protein (g) | Kohlenhydrate (g) | Fett (g) | Quelle |

```
Tool: google_sheets_make_api_mutating_request
method: POST
url: https://sheets.googleapis.com/v4/spreadsheets/1tJ_-u7hcdAKkJbLwkGvbvqWs5sfqbWVMH64VQjaiLpc/values/Mahlzeiten!A5:K1010:append?valueInputOption=USER_ENTERED&insertDataOption=OVERWRITE
body: {"values":[["TT.MM.JJJJ","HH:MM","<Mahlzeit>","<Was gegessen>","<Menge>",<Gramm>,<kcal>,<Protein>,<KH>,<Fett>,"Sprachnachricht"]]}
```

- Spalte C nur aus: `Frühstück`, `Mittagessen`, `Abendessen`, `Snack`, `Getränk`, `Supplement`.
- Spalte E ist Freitext ("3 Dosen à 80 g, abgetropft ca. 156 g"), Spalte F die reine Zahl in Gramm.
- Mehrere Gerichte einer Mahlzeit als getrennte Zeilen, alle in einem einzigen `values`-Array.

### Schritt 2: Status lesen

```
Tool: google_sheets_make_api_get_request
method: GET
url: https://sheets.googleapis.com/v4/spreadsheets/1tJ_-u7hcdAKkJbLwkGvbvqWs5sfqbWVMH64VQjaiLpc/values/API!A1:A4?valueRenderOption=FORMATTED_VALUE&majorDimension=COLUMNS
```

Das versteckte Blatt `API` rendert den kompletten Stand in vier Zellen:

| Zelle | Inhalt |
|---|---|
| A1 | `kcal <ist>/<ziel> uebrig <rest> \| P <ist>/<ziel> \| KH <ist>/<ziel> \| F <ist>/<ziel> \| Stufe <n>` |
| A2 | `Bilanz <±n> kcal aus <n> abgeschlossenen Tagen` (kumuliert, heute bewusst ausgenommen) |
| A3 | `Gewicht <kg> kg \| noch <kg> kg bis 88` |
| A4 | `Eintraege heute <n>` |

Das ist die maßgebliche Quelle für die Antwort. Das Dashboard nicht zusätzlich lesen.

## Referenzwerte

Diese Tabelle spiegelt das Blatt `Lebensmittel` (Stand 06.08.2026). Steht ein Lebensmittel hier, nimm genau diese Werte, damit die Zahlen über Wochen konsistent bleiben. Nur was fehlt, wird geschätzt.

| Lebensmittel | Einheit | kcal | P | KH | F |
|---|---|---|---|---|---|
| Rio Mare Thunfisch in Olivenöl | 1 Dose 80 g, abgetropft | 120 | 13 | 0 | 7,5 |
| Rio Mare Thunfisch mit Öl, nicht abgetropft | 1 Dose 80 g | 295 | 13 | 0 | 20,5 |
| Thunfisch in Wasser | 100 g abgetropft | 110 | 25 | 0 | 1 |
| Prep-Mahlzeit Brokkoli, Chicken, Süßkartoffel | 100 g | 104 | 9,4 | 10,4 | 2,3 |
| Prep My Meal Gericht (unbekannt) | 1 Schale ca. 400 g | 480 | 40 | 45 | 14 |
| prepmymeal Alaska Seelachs mit Reis und Gemüsemix | 100 g | 79 | 6,4 | 7,2 | 2,5 |
| Hähnchenbrust | 100 g roh | 110 | 23 | 0 | 2 |
| Rindersteak mager | 100 g roh | 150 | 22 | 0 | 6,5 |
| Lachs | 100 g roh | 208 | 20 | 0 | 13 |
| Ei | 1 Stk M, 60 g | 78 | 6,5 | 0,6 | 5,5 |
| Ei roh gewogen ohne Schale | 100 g | 143 | 12,6 | 0,7 | 9,5 |
| Spiegelei in Olivenöl | 1 Ei M + 3 g Öl | 105 | 6,5 | 0,6 | 8,5 |
| Magerquark | 100 g | 67 | 12 | 4 | 0,3 |
| Skyr | 100 g | 63 | 11 | 4 | 0,2 |
| Whey Protein | 30 g | 117 | 24 | 2 | 1,5 |
| Kartoffeln gekocht | 100 g | 77 | 2 | 17 | 0,1 |
| Süßkartoffel gekocht | 100 g | 90 | 2 | 21 | 0,2 |
| Reis gekocht | 100 g | 130 | 2,7 | 28 | 0,3 |
| Haferflocken | 100 g | 372 | 13 | 59 | 7 |
| Rote Beete gekocht | 100 g | 44 | 1,7 | 10 | 0,2 |
| Rote Bete Würfel (Rewe Beste Wahl) | 100 g abgetropft | 46 | 1,1 | 8,4 | 0,1 |
| Brokkoli geköchelt | 100 g | 35 | 2,8 | 4 | 0,4 |
| Avocado | halbe, 70 g | 112 | 1,4 | 1,2 | 10 |
| Olivenöl | 1 EL, 10 g | 88 | 0 | 0 | 10 |
| Mandeln | 30 g | 174 | 6,4 | 1,8 | 15 |
| Raw Honey | 1 EL, 21 g | 64 | 0 | 17 | 0 |
| Deutscher Honig | 100 g | 304 | 0 | 82 | 0 |
| Dunkle Schokolade 85 Prozent | 28 g | 168 | 3 | 5 | 14 |
| Himbeeren | 100 g | 52 | 1,2 | 5 | 0,7 |
| Heidelbeeren | 100 g | 57 | 0,7 | 12 | 0,3 |
| Kiwi | 1 Stk, 75 g | 45 | 0,8 | 8 | 0,4 |
| Kiwi Gold | 100 g | 63 | 1 | 15,8 | 0,3 |
| Banane | 1 Stk, 120 g | 107 | 1,3 | 25 | 0,4 |
| Salzbrezeln getrocknet | 100 g | 381 | 10 | 74 | 4 |
| Grüner Tee GunPowder | 1 Tasse | 0 | 0 | 0 | 0 |
| Kreatin | 5 g | 0 | 0 | 0 | 0 |

Mengenangaben ernst nehmen. Fehlt eine Menge, realistische Portion annehmen und die Annahme in einem Halbsatz nennen. Es muss nicht exakt sein.

Kommt ein neues Standardlebensmittel vor, das Louis absehbar öfter isst, hänge es an `Lebensmittel!A5:G120` an und ergänze die Tabelle oben in dieser Datei beim nächsten Mal. Einmalige Gerichte nicht aufnehmen.

## Gewicht eintragen

```
method: POST
url: .../values/Gewicht!A5:C154:append?valueInputOption=USER_ENTERED&insertDataOption=OVERWRITE
body: {"values":[["TT.MM.JJJJ",<kg>,"<Notiz oder leer>"]]}
```

Danach ebenfalls `API!A1:A4` lesen und A3 mitberichten.

## Training nachmelden

Der Abendsync holt Strava selbst. Wenn Louis vorher sagt, dass ein hartes Training kommt oder ausfällt, trage die Stufe direkt in `Tagesbilanz` Spalte F ein (1 bis 4).

Zeile = 5 + (Datum − 01.07.2026). Beispiel: 06.08.2026 ist Zeile 41.

Spalten von `Tagesbilanz`: A Datum, B Tag, C Gewicht, D Plan laut Rahmen, E Stufe, F Stufe manuell, G Tagesziel kcal, H Gegessen kcal, I Kalorien übrig, J Protein, K Protein-Ziel, L Kohlenhydrate, M Fett, N Lauf km, O Trainingszeit, P Relative Effort, Q Notiz. Erste Datenzeile 5, letzte 249.

## Kalorienstufen

| Stufe | kcal |
|---|---|
| 1 Ruhetag | 2.600 |
| 2 Normal | 2.800 |
| 3 Hart | 3.200 |
| 4 Sehr hart | 3.700 |

Woher die Stufe kommt:

- Zukünftige Tage: aus dem Trainingsrahmen (Blatt `Plan`, Spalte Stufe). Mo 2, Di 3, Mi 2, Do 2, Fr 1, Sa 3, So 3.
- Heute: die höhere von Plan-Stufe und Ist-Stufe, damit Louis für den Tag isst, der noch vor ihm liegt.
- Vergangene Tage: Ist-Stufe aus gemessener Trainingsdauer und Laufdistanz. Unter 30 min = 1, unter 75 min = 2, unter 150 min = 3, ab 150 min = 4. Lauf ab 15 km oder Rad ab 60 km hebt auf 4.
- Spalte F überschreibt alles.

Makros: Protein 2,0 g pro kg, Fett 0,9 g pro kg, Kohlenhydrate sind der Rest.

## Wichtiger Grundsatz

Kalorienschätzungen von Strava und Garmin werden NICHT zur Steuerung benutzt. Louis hält sie für zu hoch. Maßgeblich sind sein Kalorien-Input und gemessene Größen: Trainingsdauer, Laufdistanz, Relative Effort. Wenn du Kalorienverbrauch erwähnst, kennzeichne ihn als Schätzung oder lass ihn weg.

## Antwortformat

Nach jedem Eintrag genau diese vier Zeilen, aus `API!A1:A4` gefüllt:

```
Eingetragen: <Gericht>, <kcal> kcal, <P> g Protein.
Heute: <ist> von <ziel> kcal, noch <übrig>. Stufe <n>.
Makros: P <ist>/<ziel>, KH <ist>/<ziel>, F <ist>/<ziel>.
Bilanz: <±n> kcal aus <n> Tagen. Gewicht <kg> kg, noch <kg> kg bis 88.
```

Die Bilanzzeile immer mitgeben, auch wenn Louis nur eine Mahlzeit meldet. Negativ heißt Defizit.

Bei einer reinen Frage ohne Eintrag entfällt Zeile 1, dann nur Status lesen (ein Call).

Louis will neutrale, knappe Antworten. Keine Motivationssprache, keine Füllwörter, keine Gedankenstriche als Satzzeichen.

## Korrekturen

Zeile in `Mahlzeiten` leeren:

```
method: POST
url: .../values/Mahlzeiten!A<Zeile>:K<Zeile>:clear
body: {}
```

## Blatt API

Verstecktes Blatt, sheetId 1400854751, enthält nur Formeln in A1:A4. Wenn sich die Dashboard-Struktur ändert, müssen die Zellbezüge dort nachgezogen werden:

- A1 referenziert `Dashboard!B4:C9` (Kalorien, Protein, KH, Fett, Stufe)
- A2 rechnet über `Tagesbilanz!G5:H249` mit `SUMIFS` auf Datum kleiner heute und Gegessen größer 0
- A3 nimmt den letzten Wert aus `Gewicht!B5:B154` per `INDEX(...;COUNT(...))`
- A4 zählt `Mahlzeiten!A5:A1010` auf `TODAY()`

## Was Louis am Training bekannt ist

Aus der Analyse Juli 2026: sehr konsistent, aber Verteilung passt nicht zu den Zielen. 48 Prozent der Trainingszeit in Kraft, 18 Prozent Laufen, bei Halbmarathon und Hyrox als Zielen. Zu wenig Laufumfang, zu wenig Long Runs, fast keine Ruhetage. Der kritischste Wert bleibt die Zahl der Ruhetage, weil gleichzeitig ein Defizit läuft. Wenn die Wochenwerte das wieder zeigen, sachlich benennen, nicht wiederholt predigen.
