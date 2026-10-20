# VOLLGUT – Konzept für ein Controlling-Lernspiel

Arbeitstitel eines Browser-Lernspiels zur Vorbereitung auf den **Geprüften Controller / die Geprüfte Controllerin (IHK)**.
Der Spieler ist Controller/in einer Getränkegruppe: Getränkefachgroßhandel mit drei eigenen Abholmärkten und einer
Hausmarke Limonade in Lohnabfüllung. Die Kampagne führt vom Pilotmarkt über den Großhandel zur Gruppe; ab Spieljahr 2
folgt der Make-or-Buy-Fall „eigene Abfüllanlage“ für die industrielle Kostenrechnung.

Stand: 20.10.2026. Alle Betriebszahlen sind Annahmen, aber per Rechenmodell geprüft.

## Bereits entschieden

| Karte | Frage | Antwort |
|---|---|---|
| K001 | Welches Unternehmen soll das Spiel abbilden? | Großhandel plus eigene Märkte |
| K002 | Wie kommt die industrielle IHK-Kostenrechnung ins Spiel? | Lohnabfüllung der Hausmarke, ergänzt um Make-or-Buy „eigene Abfüllanlage“ ab Spieljahr 2 |

Die übrigen 88 Entscheidungen stehen in `entscheidungskarten.json` und werden über die Kartenseite beantwortet.

## Inhalt

| Datei | Inhalt |
|---|---|
| `konzept.md` | Finales Konzept (Standardpfad), Marker ⟨Entscheidung: …⟩ zeigen änderbare Annahmen |
| `entscheidungskarten.json` | 90 Entscheidungskarten (29 Kern, 36 wichtig, 25 Kür) |
| `entscheidungskarten.html` | Kartenseite zum lokalen Öffnen; ohne Claude-Speicher bleiben Antworten im Browser und lassen sich als Text kopieren |
| `entscheidungskarten-aenderungen.md` | Prüfbefunde zu den Karten und Standardannahmen für alles ohne Karte |
| `entscheidungs-kandidaten.md` | Alle 143 Kandidaten, aus denen die Karten ausgewählt wurden |
| `entwuerfe/` | Drei konkurrierende Konzeptentwürfe (Kampagne, Controller-Alltag, Prüfungsfälle) |
| `recherche/` | Controlling-Curriculum (IHK HB1–HB6), Getränkemarkt- und Großhandelsdomäne, Lern- und Spieldesign, Technik, Marktvergleich, Lückenkritik, Startbetrieb |
| `rechenmodell/` | Python-Modell des Startbetriebs (`model08.py`, Prüfungen eingebaut) und Konzeptzahlen (`final.py`) |

Rechenmodell ausführen:

```sh
cd rechenmodell && python3 final.py
```

## Offene Punkte

- Lehrgangsskripte des Auftraggebers einarbeiten (Zuordnung über Lernziel-IDs, siehe `konzept.md` Abschnitt 7.1).
- Rechtsquellen im Volltext prüfen (ContrPrV § 7, BFH I R 36/07, Vertikal-GVO), bisher nur über Suchauszüge belegt.
- Fachreview der Branchenzahlen durch eine Person aus dem Getränkegroßhandel.
