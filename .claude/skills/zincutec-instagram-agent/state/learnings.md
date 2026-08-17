# Erkenntnisse

Das Langzeitgedächtnis des Agents. **Nach jedem Lauf fortschreiben, vor jedem Lauf lesen.**

Der Unterschied zum `content-log.md`: dort steht, *was* produziert wurde. Hier steht, *was der Agent daraus gelernt hat*. Ein Lauf, der nichts hinzufügt, ist möglich — aber drei Läufe hintereinander ohne neue Erkenntnis bedeuten, dass zu oberflächlich geprüft wird.

## Wie ein Eintrag entsteht

Am Ende jedes Laufs drei Fragen beantworten:

1. **Was hat überrascht?** Ein Bild, das besser oder schlechter war als der Dateiname vermuten ließ. Ein Kriterium, bei dem die Bewertung schwankte. Eine Caption-Formulierung, die beim Streichtest zusammenfiel.
2. **Was hat Louis korrigiert?** Jede Rückmeldung ist ein Datenpunkt. Wenn er ein Bild tauscht, eine Zeile umschreibt oder einen Post nicht veröffentlicht — der Grund gehört hierher.
3. **Was würde ich beim nächsten Mal anders machen?** Konkret und überprüfbar, nicht „mehr auf Qualität achten".

Nur echte Erkenntnisse eintragen. Wiederholungen von Bekanntem verwässern die Datei.

## Wenn ein Muster dreimal auftritt

Dann ist es keine Notiz mehr, sondern eine Regel. **In die zuständige Referenzdatei überführen** und hier auf „übernommen" setzen:

| Art der Erkenntnis | Ziel |
|---|---|
| Bild-, Licht-, Kompositionsurteil | `quality-rubric.md` |
| Sprache, Tonfall, verbotene Formulierung | `brand-dna.md` oder Hard Rejects |
| Layout, Typografie, Maße | `design-system.md` |
| Säulen, Rhythmus, Hashtags, Zeitfenster | `content-system.md` |
| Werkzeug- oder API-Verhalten | `pipeline.md` |
| Wettbewerbsbeobachtung | `competitors.md` |

**Die Rubrik ist ausdrücklich änderbar.** Sie ist die beste bisherige Fassung des Qualitätsbegriffs, kein Gesetz. Wenn die Praxis zeigt, dass ein Kriterium falsch gewichtet ist oder ein Hard Reject fehlt: ändern, im Commit begründen, hier vermerken.

## Was Louis' Reaktionen bedeuten

| Beobachtung | Auslegung |
|---|---|
| Post unverändert veröffentlicht | Score war belastbar. Motiv- und Tonwahl bestätigt. |
| Bild getauscht | Die Bildkriterien greifen noch nicht. Beide Bilder vergleichen, Unterschied hier festhalten. |
| Caption umgeschrieben | Stimme noch nicht getroffen. Vorher/Nachher notieren, Muster in `brand-dna.md` schärfen. |
| Post liegen gelassen | Stärkstes Negativsignal. Ursache suchen, bevor Ähnliches erneut produziert wird. |
| Reihenfolge geändert | Feed-Rhythmus stimmt nicht. `content-system.md` prüfen. |

---

## Einträge

### 2026-08-17 — Erstlauf

**Renderings verlieren gegen Fotografie, und zwar deutlich.**
Derselbe Post mit dem Shopify-Rendering: 82. Mit `KINKO 35.jpg` aus dem Shooting-Ordner: 85. Der Unterschied lag komplett bei Materialwahrheit (6 → 9) und Licht (8 → 9). Canvas eigene Bilderkennung vergab für das Rendering die Tags „render" und „3d" — eine brauchbare unabhängige Gegenprobe.
→ *Übernommen in `pipeline.md`: `2. S`-Ordner vor Shopify-CDN.*

**Generative Layout-Werkzeuge erfinden Fakten.**
Canvas `generate-design` hat bei präzisem Prompt ein ZINCUTEC-Logo erfunden, zwei fremde Produkte eingesetzt und eine Telefonnummer frei erfunden. Nicht „ungenau" — erfunden. Für ein Marken-Asset disqualifizierend.
→ *Übernommen in `design-system.md`: Weg gesperrt, Master-Duplikat ist der einzige Pfad.*

**Ein Dateiname sagt nichts über Bildqualität.**
`kinko-steel-3` klang nach Standardaufnahme, war aber die beste Fotografie im Bestand — nur mit unpassender Wandfarbe. Ohne Ansehen wäre die Wahl falsch gefallen.
→ *Übernommen als Pflichtschritt: zwei bis vier Kandidaten ansehen.*

**Offen für den nächsten Lauf:** Bislang existiert keine Rückmeldung von Louis zu einem veröffentlichten Post. Solange kein Post live war, ist jeder Score eine Selbsteinschätzung ohne Außenprüfung. Der erste veröffentlichte Post ist der wichtigste Datenpunkt — Reaktion abwarten und hier auswerten.
