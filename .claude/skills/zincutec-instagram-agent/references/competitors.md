# Wettbewerbsanalyse

Der Agent analysiert bei jedem Lauf den eigenen Feed **und** das Wettbewerbsumfeld. Zweck ist nicht Nachahmung, sondern Standardkontrolle: liegt ZinCuTec über oder unter dem Niveau, und wo gibt es eine Lücke, die nur ZinCuTec besetzen kann.

---

## Wichtig: Instagram ist nicht scrapebar

Getestet am 2026-08-17. Instagram liefert unauthentifizierten Abrufen eine leere JavaScript-Hülle — keine Posts, keine Captions, keine Followerzahlen. `framacph` antwortet mit 302. **Jeder Versuch, Instagram-Profile direkt zu laden, ist Zeitverschwendung — nicht wiederholen.**

Nutze stattdessen diese vier Wege, in dieser Reihenfolge:

1. **Marken-Websites und Journals** — voll abrufbar und inhaltlich näher an der Kampagnenlogik als der Feed selbst. Frama, New Works, Louise Roe und Metallbude führen Journal-/Lookbook-Bereiche, die zeigen, woran die Marke gerade arbeitet.
2. **WebSearch** — Kampagnen, Messeauftritte (Salone del Mobile, 3 Days of Design), Presse, Kooperationen. Gibt die strategische Richtung, die im Feed nur die Oberfläche ist.
3. **Screenshots von Louis** — die höchste Signalqualität. Wenn ein Lauf eine echte Feed-Analyse braucht, im Report gezielt danach fragen: welcher Account, welcher Zeitraum.
4. **Eigene Instagram-Insights** — zincutec.eu bindet `graph.instagram.com/v21.0` ein, es existiert also ein Business-Zugang. Wenn Louis diesen Token bereitstellt, sind für **@zincutec selbst** echte Reichweiten- und Engagement-Daten abrufbar. Fremde Accounts bleiben auch damit unzugänglich.

Wenn eine Runde ohne belastbare Wettbewerbsdaten endet: im Log vermerken, keine Vermutungen als Befund ausgeben.

---

## Der eigene Account

**@zincutec** — zincutec.eu · „Metal becomes Art" · Manufaktur seit 2000

Bei jedem Lauf gegen `state/content-log.md` prüfen:
- Welche Säulen sind in den letzten neun Posts über-, welche unterrepräsentiert?
- Häufen sich Winkel, Produkttypen oder Bildtöne?
- Welche Produkte lagen zuletzt brach? (Rotationstabelle im Log)
- Welcher Post lief zuletzt am besten — und war es das Motiv, die Caption oder das Zeitfenster?

---

## Wettbewerber

Von Louis benannt. Aufgeteilt nach dem, was ZinCuTec von ihnen lernen kann.

### Direkt: Metallmöbel

| Account | Marke | Was dort funktioniert | Wo ZinCuTec stärker ist |
|---|---|---|---|
| `@metallbude_official` | Metallbude (DE) — „hochwertige Metallmöbel im minimalistischen Design" | Klare Produktkommunikation, konsequenter Minimalismus, D2C-Reichweite | Metallbude ist Serie und Systemmöbel. ZinCuTec ist Handarbeit mit nicht reproduzierbarer Patina — das ist der Graben |
| `@form.eisen` | form & eisen (DE) | Stahl als ehrliches Material, handwerknahe Bildsprache | ZinCuTec spielt eine Preisklasse höher und arbeitet skulptural, nicht funktional |
| `@postandbeamsystem` | Post + Beam | Systemlogik, Modularität als Erzählung, Montage-Content | ZinCuTec verkauft Einzelstücke, kein System — Autorenschaft statt Baukasten |

### Referenz: skandinavisches High-End

| Account | Marke | Was dort funktioniert |
|---|---|---|
| `@framacph` | Frama (Kopenhagen) — „timeless design, honest materials" | **Die wichtigste Referenz.** Materialehrlichkeit, Stille im Grid, Räume die bewohnt statt gestylt wirken, Patina als erzählter Wert |
| `@newworksdk` | New Works (DK) | Editorial-Inszenierung, Licht als Hauptdarsteller, dunkle und schwere Materialpaletten |
| `@louiseroecph` | Louise Roe (Kopenhagen) | Objekt als Skulptur, Kunsthandwerk-Positionierung, Gründerin als Autorin der Marke |

### Kontext: Interior-Kuration

| Account | Marke | Was dort funktioniert | Vorsicht |
|---|---|---|---|
| `@casestudios.de` | Case Studios (DE) | Projektbezogene Räume, Architektur-Kontext | Kuratiert fremde Räume — für ZinCuTec kein Modell |
| `@livindahome` | Livindahome | Reichweitenstarke Interior-Kuration, Feed-Rhythmus | Deutlich kommerzieller Ton, näher am Shop als am Atelier |

---

## Analyse-Schritt im Tageslauf

**Zeitbudget: 5–10 Minuten. Kein Selbstzweck.** Nicht jeden Lauf alle Accounts — pro Tag zwei bis drei rotierend, Frama mindestens einmal pro Woche.

1. **Website/Journal des Rotations-Accounts abrufen.** Was zeigen sie gerade: neue Kollektion, Materialthema, Kampagne, Messe?
2. **Eine gezielte WebSearch**, wenn die Website nichts Aktuelles hergibt.
3. **Drei Fragen beantworten und in den Log schreiben:**
   - Welches Motiv oder Format trägt dort gerade — und warum funktioniert es?
   - Was davon ist **übersetzbar** in ZinCuTecs Bildsprache, ohne die Marke zu verbiegen?
   - Was machen alle gleich — und wo entsteht dadurch eine freie Position für ZinCuTec?
4. **Höchstens eine Erkenntnis** fließt in die Posts des Tages ein. Mehr wird Imitation.

---

## Die Abgrenzungsregel

Wettbewerbsanalyse dient dem Niveau, nicht der Vorlage. Vor der Übernahme jeder Beobachtung:

> **Würde dieser Post noch erkennbar von ZinCuTec sein, wenn man Logo und Produktnamen entfernt?**

Bei Nein: nicht übernehmen. Kriterium 10 der Rubrik („Eigenständigkeit") ist die Instanz, die das durchsetzt.

**Was ZinCuTec übernehmen darf:** Lichtqualität, Bildschärfe der Komposition, editorialer Anspruch, Mut zur Leerfläche, Ernsthaftigkeit im Materialgespräch.

**Was ZinCuTec nie übernimmt:**
- Framas helle, luftige Kopenhagen-Palette — ZinCuTec ist dunkler, kontrastreicher, moody. Das ist Louis' Handschrift und der Unterschied.
- Systemmöbel-/Modularitätserzählungen (Post + Beam) — ZinCuTec macht Einzelstücke.
- Kuratier-Logik fremder Räume (Case Studios, Livindahome) — ZinCuTec zeigt eigene Arbeit.
- Serien- und Verfügbarkeitssprache (Metallbude) — jedes Stück ist in der Oberfläche einmalig, genau das ist die Botschaft.

**Die Position, die nur ZinCuTec besetzen kann:** deutsche Metallmanufaktur seit 2000, japanisch benannte Entwürfe, brünierte Messingpatina die sich nicht zweimal gleich auftragen lässt, fotografiert von einem Filmemacher mit filmischem Kontrast. Kein Wettbewerber auf dieser Liste kann diese vier Dinge gleichzeitig behaupten. **Jeder Post sollte mindestens eines davon tragen.**
