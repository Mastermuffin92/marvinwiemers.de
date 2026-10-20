# Entwurf „Prüfungs-first / Fallmaschine“: Controller/in in der Getränkegruppe

Stand 19.10.2026. Sicherheitsstufen: **[sicher]** belegt oder nachgerechnet · **[wahrscheinlich]** starke Ableitung oder Einzelquelle · **[Vermutung]** Designannahme oder gefüllte Lücke. Alle Betriebszahlen sind Annahmen. Basis ist der Startbetrieb „Getränkegruppe“ aus 08 in der Variante **ohne Kelterei**, ergänzt um die Hausmarke (4.3). Alle neuen Zahlen stammen aus `scratchpad/scripts_pruef/` (hausmarke.py, szenen.py, rest.py) und sind dort nachrechenbar.

---

## 1. Kurzfassung und Arbeitstitel

**Arbeitstitel: „Prüfstand – Controllerfälle aus der Getränkegruppe“** (Alternative: „Fallakte Getränkegruppe“). „IHK“ steht bewusst nicht im Namen (05, 6.1).

1. Jede Spielsituation ist eine Situationsaufgabe im Stil der schriftlichen Controller-Prüfung: Fallbeschreibung, Anlagen, Teilaufgaben mit Operatoren und Punkten, Lösungshinweise, Bewertungsbogen.
2. Eine **Fallmaschine** erzeugt sie aus dem aktuellen Zustand der eigenen Getränkegruppe (GFGH-KG mit 600 Gastrokunden, drei Abholmärkte, Hausmarke Limonade in Lohnabfüllung); jede Zahl hat eine Vorgeschichte im Spiel.
3. Ein Geschäftsjahr ist ein Run mit neuem Seed und endet mit einer Jahresprüfung; Meta-Fortschritt ist nur das Kompetenzprofil je Handlungsbereich (HB) und Lernziel-ID.
4. Die Kampagne läuft vom Pilotmarkt über den Großhandel und den Make-or-Buy-Bogen „eigene Abfüllanlage“ bis zur Gruppe.
5. Wiederholung ist Pflicht und wird rückwärts vom eingegebenen Prüfungstermin geplant (FSRS plus Countdown).
6. Eigene Modi decken ab, was schriftliche Fälle nicht leisten: Tabellen-Labor (HB4, echte .xlsx-Dateien), Projektarbeit-Simulator (HB5), Präsentation und Fachgespräch (HB6).
7. Alle Inhalte hängen nur an Lernziel-IDs; die Lehrgangsskripte werden später per Zuordnungstabelle angehängt, ohne das Spieldesign zu ändern.
8. Ehrlich: Auf die 75 % der Note aus Projektarbeit und mündlicher Prüfung bereitet das Spiel vor, bewerten kann es sie nicht verlässlich.

---

## 2. Ehrliche Grenzen der Grundidee und Umgang damit

| Grenze | Was sie bedeutet | Umgang im Konzept |
|---|---|---|
| **75 % der Note sind Projektarbeit (45 %) und mündliche Prüfung (30 %)**, nur 25 % schriftlich, § 7 Abs. 4 ContrPrV **[sicher]**; HB4 zählt zum schriftlichen Teil **[wahrscheinlich, 05]** | Eine 30-Tage-Arbeit über den eigenen Betrieb und ein Fachgespräch kann keine Software verlässlich bewerten. | HB5- und HB6-Modi trainieren Teilfertigkeiten (Themenwahl, Gliederung, Rechenkern, Empfehlung, Fragen vorwegnehmen). Automatisch bewertet wird nur die Struktur, der Inhalt per Rubrik (selbst oder Mentor). Versprochen wird „vorbereitet“, nicht „bewertet“ (3). |
| **Pflichtwiederholung über alle Facetten** | ≈ 300 Skills × 7 Abrufe ≈ 2.100 Abrufe; bei 8 pro Tag sind das 260 Tage (06, 6.8) **[Vermutung]** | Pflichtkanon nach Prüfungsrelevanz: ≈ 200 Skills, ≈ 1.400 Abrufe. Mit in Fälle eingebetteten Abrufen ≈ 14 je Lerntag, also ≈ 100 Lerntage. Ausblick-Lernziele werden geplant, sperren nichts. Gesamtaufwand ≈ 105–130 h über 6–9 Monate (5). |
| **HB4 wird 240 Min. am Tabellenkalkulationsprogramm geprüft** **[sicher]** | Ein Rechenblatt im Browser ist kein Excel. | Tabellen-Labor mit echten .xlsx-Dateien (Download, Excel oder LibreOffice, Upload, automatische Prüfung); das Browser-Raster nur für Mikroübungen. Formatierung und Diagrammqualität nur per Rubrik. |
| **Industrie-KLR nur über Lohnabfüllung und Make-or-Buy** | Die Lohnabfüllung liefert Zuschlagskalkulation mit Fremdleistung, Herstellkosten nach § 255 HGB, Target Costing und Preisprüfung. Einen BAB mit Fertigungsstellen gibt es nur als Planrechnung, laufend erst nach einem Kauf. Kuppelprodukte, unfertige Erzeugnisse und mehrstufige Serienfertigung fehlen ganz, sie sind mit der Kelterei entfallen. Die Prüfung ist industriegeprägt **[wahrscheinlich, 06]**. | Die Fallmaschine garantiert die Abdeckung unabhängig vom Kaufausgang: ohne Kauf jährliche Schattenrechnung (Plan-BAB-Review) und 10–15 % Transferfälle aus fremden Branchen (E4). |
| **Größere Simulation = mehr Bauaufwand** | GFGH plus Märkte kosten +80–130 PT gegenüber dem Einzelmarkt (08) **[Vermutung]** | Die Fallmaschine braucht keine Tagessimulation der Gruppe. Es reichen Monatsaggregate je Gesellschaft, Segment, Kundenklasse und Kostenstelle plus ≈ 20 benannte Einheiten. Nur Markt 1 läuft optional tagesgenau. Das spart grob 30–50 PT, die HB4–6-Modi kosten 25–40 PT dazu **[Vermutung]**. |
| **Abstrakterer B2B-Einstieg** | Keine Kasse, kein Kunde vor Augen | Kapitel 1 spielt in Markt 1 (Bon, Pfandbon, Regal). Der Großhandel kommt über benannte Kunden als Fallfiguren hinzu (Brauhaus, Eckkneipe) und über eine Tourenkarte. |
| **Weitere** | DIHK-Rahmenplan nicht frei; Original-Prüfungsaufgaben geschützt **[sicher, 05]**, Skripte vermutlich auch **[wahrscheinlich]**; Zahlenwelt unbelegt (08: Belegbarkeit 1 von 5); ohne Kelterei weniger Covenant-Druck (EK-Quote 28,6 % statt 26,4 %) | Lernziel-Katalog aus Verordnungswortlaut und Modulen; nur eigene Aufgaben im Prüfungsstil; Skripte nur für Zuordnung und Stilabgleich; Spannen und Fachreview; Covenant-Druck über Investition (Szene C) und Gastro-Darlehen |

---

## 3. Zielgruppen und Lernversprechen

**Primär:** Teilnehmende eines Lehrgangs „Geprüfte/r Controller/in“, 6–12 Monate vor dem schriftlichen Teil. Bundesweit sind es 80–115 Prüfungsteilnehmende pro Jahr; 2025 waren es 82, davon 54 bestanden (≈ 66 %) **[wahrscheinlich, DIHK-Statistik in 05/06]**. **Sekundär:** Bilanzbuchhalter (Teilmengen aus HB1/HB3), Fachwirte, Junior-Controller im Groß- und Einzelhandel. Lehrgangsträger dienen als Multiplikator.

| Nr. | Versprechen | Messung im Spiel | Schwelle |
|---|---|---|---|
| L1 | Schriftliche HB1–HB3 sicher | zwei Probeklausuren in Folge mit neuen Seeds, Prüfungszeit, eigene Aufgaben | ≥ 67 Punkte je HB („befriedigend“) |
| L2 | Behalten bis zum Termin | prognostizierte Abrufwahrscheinlichkeit am Prüfungstag | ≥ 0,90 für ≥ 85 % der Pflichtkanon-Skills |
| L3 | HB4 am echten Werkzeug | 240-Min.-Probeübung als .xlsx, automatisch geprüft | ≥ 67 Punkte |
| L4 | HB5 strukturiert | zwei Themenvorschläge, Exposé, Gliederung, Rechenkern und Entscheidungsvorlage zum **eigenen** Betrieb | alle Pflichtkriterien der Rubrik |
| L5 | HB6 präsentationsfähig | 15-Min.-Präsentation, 20 Fachgesprächsfragen zur eigenen Arbeit | Zeit ± 1 min, Selbstbewertung ≥ 70 % |
| L6 | Typische Fehler abgestellt | Fehlerlogbuch der letzten 30 Tage | keine Top-10-Misconception öfter als 1× |

Nicht versprochen wird das Bestehen. Die Schwellen sind interne Maße und werden mit freiwillig gemeldeten echten Prüfungsergebnissen kalibriert (13).

---

## 4. Spielerrolle, Setting, Figuren

### 4.1 Rolle

Der Spieler ist Controller/in der Gruppe, eine Stabsstelle der Geschäftsführung. Die Stelle kostet 75 T€, das sind **23,4 % des Konzern-EBIT von 320,3 T€** (mit Hausmarke). Sie muss ihren Nutzen nachweisen (06, Karte 9). Der Spieler **empfiehlt**, der Geschäftsführer **entscheidet** (06 W9). Die Zustimmungswahrscheinlichkeit hängt von Vertrauen und Punktzahl der Vorlage ab. Damit wird die Prüfungsleistung zur Spielwirkung.

### 4.2 Setting (08 ohne Kelterei)

| Einheit | Inhalt | Plan 2027 |
|---|---|---|
| {NAME} Getränke GmbH & Co. KG | GFGH und Zentrale: 600 Gastrokunden (60 A, 200 B, 340 C), 150 Wiederverkäufer, 25 Streckenkunden, 300 Objekte und 900 Haushalte, 350 Feste; 11 Lkw und 4 Transporter, 5.000 m² Halle, 49,0 VZÄ | Außenumsatz 17.500 T€; Tourtag 454,30 €, Gastro-Stopp inkl. Auftrag 34,16 €, Leergut 0,35 €/Kasten netto |
| Märkte GmbH (EAV, Organschaft) | 3 Abholmärkte. **Markt 1 = Referenzmarkt aus 02 mit den Korrekturen aus 06** als reiner Laden (G19) | 4.500 T€; Markt 1: 2.150 T€, 100.000 Bons, 329 Kunden/Tag an 304 Tagen, RE I 29,1 % auf Verrechnungspreis (VP), EBIT 15,9 T€; Markt 3: EBIT −14,8 T€ |
| Hausmarke (Sparte der KG seit 2026) | Limonade, Lohnabfüllung beim fiktiven Mineralbrunnen „Brunnenhof“ | 518,2 T€ Umsatz (4.3) |
| Besitzgesellschaft | vermietet die Halle | 330 T€ Miete |

**Konzern 2027:** Außenumsatz 22.000 T€, EBITDA 780,7 T€, EBIT 320,3 T€. Zum 01.01.: EK-Quote 28,2 % brutto bzw. 30,5 % bei saldiertem Pfand, Nettoverschuldung/EBITDA 2,91. Die Covenants liegen bei ≥ 25 % bzw. ≤ 3,5 (Annahme 08). Pfand-Float 341,7 T€, das kostet ≈ 27,3 T€ Zins bei 8 %. Saft kauft die KG bei einer fremden Kelterei (08, 2.7).

### 4.3 Hausmarke: Produktwahl und Datenblatt

**Limonade** (Zitrone und Orange, Mehrweg-Glas). Begründung aus Prüfungssicht:

1. Natürliches Mineralwasser muss am Quellort abgefüllt werden **[wahrscheinlich, Mineral- und Tafelwasser-VO]**; ohne eigene Quelle wäre Make-or-Buy kein echter Fall.
2. Mehrere Rohstoffe (Zucker, Saftkonzentrat, Aroma, CO₂) ergeben Preis-, Verbrauchs- und Mischungsabweichungen in prüfungstypischer Form.
3. Die geplante Zuckersteuer (Kabinett: 26 ct/l bei 5–8 g, 32 ct/l ab 8 g je 100 ml, ab 1.7.2027, Bundestag offen **[wahrscheinlich, 08]**) liefert Target Costing und Steuern als Planungsgröße.
4. 0,33 l passt in die Gastronomie; alkoholfrei erlaubt eine Schulversion.

Gegenargument: Apfelschorle hat echtes Konzentrat-Preisrisiko (E3).

| Größe | H33 (24 × 0,33 l) | H50 (20 × 0,5 l) | H100 (12 × 1,0 l) | Summe |
|---|---|---|---|---|
| Kästen 2027 (Kanal) | 18.000 (Gastro) | 14.000 Märkte + 8.000 Wiederverkäufer | 9.000 Märkte + 6.000 Heimdienst | 55.000 Kästen = 1.052.000 Fl = 542.560 l |
| Grundstoff 0,15 €/l (95 g Zucker/l, 6 % Saft) | 1,19 € | 1,50 € | 1,80 € | 81,4 T€ |
| Abfülllohn je Flasche (inkl. Waschen, CO₂, Wasser, Verschluss, Etikett) | 0,19 € → 4,56 € | 0,21 € → 4,20 € | 0,26 € → 3,12 € | 221,3 T€ |
| Fracht Sattelzug / Leergut-Pool je Kasten | 0,09 / 0,31 € | 0,09 / 0,31 € | 0,09 / 0,31 € |  |
| **Herstellkosten je Kasten** | **6,15 €** | **6,10 €** | **5,32 €** | 324,7 T€ |
| Preis (netto; Markt: VK brutto) | Gastro 11,10 € | WV 7,90 €; Markt 10,99 € brutto | Markt 9,99 € brutto; HD 8,40 € | 518,2 T€ |
| RE I der Gruppe | 44,6 % | 22,8 % / 33,9 % | 36,6 % / 36,7 % | 37,4 % |
| Pfand brutto je Kasten | 5,10 € | 4,50 € | 3,30 € |  |

- **Leergut-Pool:** 11.000 Individualkästen (8 Wochen Umlauf × Saisonfaktor 1,3) und 210.400 Flaschen. Anschaffungskosten 94,8 T€, AfA 15,1 T€ (Kästen 10 Jahre, Flaschen 5 Jahre), Schwund 2,2 T€ **[Vermutung]**.
- **Ergebnis:** RE I 193,6 T€. Nach Pool und 29 T€ Fixkosten der Hausmarke (Marketing 15, Labor 5, Produktmanagement 9) bleibt ein Produkt-DB II von 164,3 T€. **Gegenüber der verdrängten Fremdware** (Segment-RE plus 3 % Nachvergütung) bringt die Hausmarke aber nur **+1,9 T€ EBIT**. Der Break-even gegenüber Fremdware liegt bei 51.600 Kästen. Diese Lücke ist ein eingebauter Lernanlass: Produkt-DB ist nicht gleich Entscheidungswert.
- **Konsistenz mit 08:** Die Hausmarke ersetzt AfG-Fremdware innerhalb unveränderter Segmentumsätze; Konzern-EBIT 318,4 + 1,9 = 320,3 T€; Pool als Sachanlage gegen Kontokorrent.
- **Offen:** Die Pfandbilanzierung eigener Gebinde (Inverkehrbringer statt Händler) ist ungeklärt; 07 nennt BFH I R 33/11 nur für Brunnen **[Vermutung, Fachprüfung]**. Im Spiel ein Lernfall.

### 4.4 Figuren (Name – Rolle – Prüfungsfunktion)

- **Jan {NAME}**, Geschäftsführer (Kommanditist, 2. Generation): entscheidet; Adressat der Entscheidungsvorlagen (HB5).
- **Petra Hoff**, Leitung Rechnungswesen: Monatsabschluss; HB3, Datenqualität, Abstimmungsfälle.
- **Marco Lenz**, Logistikleiter: Kostenstellen Lager und Fuhrpark; Budgetverantwortlicher, Plankosten, Raum und Personal der Abfüllung.
- **Sabine Kowalski**, Marktleiterin Markt 1 (06 F18): Kapitel 1, Business Partnering, Prämie am VP.
- **Ralf Becker**, Außendienstleiter Gastro mit Umsatzprämie: Kunden-DB, Konfliktgespräch (HB6).
- **Aylin Yilmaz**, Hausbank: Covenants; das Bankgespräch dient als Übung fürs Fachgespräch.
- **Dr. Brand**, Abschlussprüfer: Quartalsaudit mit alten Fehlern.
- **Frau Albers**, Geschäftsführerin Brunnenhof: Kalkulationsprüfung, Verhandlung (BATNA, ZOPA).
- **Lena**, Assistentin Controlling (ab Jahr 2): HB6 Teamführung, Lernen durch Lehren.
- **Prüfungsausschuss** (Personas Praktikerin, Methodiker, Skeptiker): Probeprüfungen, Fachgespräch-Simulator.

---

## 5. Spielschleifen auf allen Zeitskalen

| Zeitskala | Dauer | Ablauf | Lernfunktion |
|---|---|---|---|
| **Minute** (Teilaufgabe, 1–6 P) | 2–10 min | Situation lesen → Operator erkennen → Anlage auswerten → Eingabe mit Rechenweg → Sicherheitsregler (50/70/90 %) → Abgabe → im Übungsmodus sofort Diagnose | Retrieval, Kalibrierung |
| **Session** | 30–45 min | **Frühschicht** (5–8 fällige Items, gemischt, ≤ 10 min) → **Fall des Tages** (10–25 P aus dem laufenden Monat) → Bewertungsbogen und 3-Min.-Nachbesprechung → optional Tabellen-Labor oder Fachgesprächsfrage | Spacing, Interleaving |
| **Spielmonat** | 2–3 Sessions | Abschlusskalender AT1–AT6 (07, 9) als Serie aus **3–5 Pflichtfällen** (Abschluss-, Abweichungs-, Ereignis- und Fehlerfall), 2–4 Entscheidungskarten, Monatsbericht. **Gate:** Der Monat schließt erst, wenn die Pflichtfälle bearbeitet sind. | Routine mit neuen Zahlen |
| **Quartal** | +1 Session | Forecast, Covenant-Reporting, Audit durch Dr. Brand (10 Teilaufgaben aus alten Fällen), 45-Min.-Zwischenprüfung über alle HB | verzögertes Feedback |
| **Spieljahr = Run** | ≈ 25–30 Sessions ≈ 17–20 h | Erster Tick Sa 02.01. (06 F19). Jahreskalender aus 01 (3c): Inventur, Bonusabrechnung, Jahresabschluss, Bank, Strategie (Sept.), Budget im Gegenstrom (Okt./Nov.), Silvester-Leergut; dazu je eine HB5-Etappe und eine Präsentation. **Ende: Jahresprüfung** (HB1–HB3-Probeklausuren, 60-Min.-HB4-Übung, HB5/HB6-Etappe) | Gesamtzyklus, Transfer |
| **Echtzeit** | bis zum Prüfungstermin | Countdown steuert Scheduler, Tapering (6.3) und Anteil der Probeklausuren | Prüfungsform |

**Run-Regeln (Roguelite):** Jeder Run startet aus dem Zustand seiner Kampagnenstufe.

- **Seed:** variiert Wetter, 0–3 Gastro-Insolvenzen, Preisrunde (Höhe, Termin), Diesel (±30–50 ct/l), Zuckersteuer, Drittauftrag und Lohnabfüller-Preis (Szene C), Fahrerkündigung, Großkundenverlust, Kistenknappheit. Replays laufen mit Common Random Numbers (06 W12).
- **Bestehen:** jede Teilprüfung ≥ 50 Punkte **[wahrscheinlich, IHK-üblich; Volltext prüfen]** → nächste Stufe, Zustand wird fortgeschrieben.
- **Nicht bestanden:** Wiederholungsjahr mit gleichem Start, neuem Seed.
- **Meta-Fortschritt:** Kompetenzprofil, Werkzeuge (Rechenweg-Schablonen, Berichtsvorlagen, Notizbuch-Lehrsätze), Notenkurve je HB; keine Spielboni wie „+5 % Umsatz“ (03, 3.8).

| Stufe | Spieljahr | Kapitel | Schwerpunkte |
|---|---|---|---|
| 1 | 2027 | K1 Pilotmarkt (Jan.–Apr., Markt 1), K2 Großhandel (Mai–Dez.) | Handelskalkulation, Pfand, KER, Prozesskosten, Kunden-DB, Touren, Konditionen |
| 2 | 2028 | K3 Großhandel vertieft und Abfüllbogen (Mai–Nov.) | Fuhrpark-Investition, Gastro-Darlehen, Forderungen, Plan-BAB, Maschinenstundensatz, Äquivalenzziffern, Make-or-Buy |
| 3 | 2029 | K4 Gruppe, bei Kauf mit laufender Abfüllung | Verrechnungspreise, Spartenrechnung, Budget mit mehreren Kostenstellenverantwortlichen, Covenants, Konsolidierung light, Steuern |
| 4 | ab 2030 | Prüfungsjahre | Seeds aus allen Stufen, strenger Prüfungsmodus |

**Gesamtzeit** **[Vermutung]**: Stufen 1–3 ≈ 55–60 h, Tabellen-Labor 15–20 h, HB5 15–25 h, HB6 8–12 h, Probeprüfungen ≈ 10 h, zusammen ≈ 105–130 h über 6–9 Monate (≈ 4 h/Woche) – rund ein Viertel eines Lehrgangs mit 438 UStd. (05). Ergänzung, kein Ersatz.

---

## 6. Lernsystem

### 6.1 Lernziel-Architektur (Umhängbarkeit auf die Skripte)

```
HB (1–6) → Themenfeld → Lernziel LZ-1.04.03 → Skills (2–4) → Fall-Templates (≥ 3 Oberflächen)
lz_katalog.yaml   { id: LZ-1.04.03, hb: 1, text, operator_niveau, relevanz: hoch, module: [M07] }
skript_map.yaml   { lz: LZ-1.04.03, quelle: "Skript HB1", kapitel: "4.3", seiten: "112-118", gewicht: 1.0 }
```

- Spielinhalte referenzieren **nur LZ-IDs**; ein Skript anzuhängen heißt, `skript_map.yaml` zu füllen (reine Datenänderung).
- Der Build erzeugt einen **Abdeckungsbericht** (Lernziele ohne Skriptkapitel, Kapitel ohne Lernziel, Lernziele ohne Template). Lernkarten zeigen den „Skript-Anker“ aus der Map. IDs sind unveränderlich (04, 4.4).
- **Katalog-Entwurf** **[Vermutung]**: ≈ 150 Lernziele, abgeleitet aus § 4 Abs. 1–6 ContrPrV und den Modulen M01–M56. Themenfelder in HB1 zum Beispiel: .01 Abgrenzung (M04), .02 Kostenarten (M05), .03 Kostenstellen/BAB (M06), .04 Kalkulation Handel/Industrie (M07), .05 KER (M08), .06 Teilkosten/BEP (M09/M10), .07 Plankosten (M11), .08 Prozesskosten (M12), .09 Kostenmanagement (M13), .10 Entscheidungsrechnung (M14), .11 Konditionen (M15/M48), .12 Verrechnungspreise (M41).

### 6.2 Theorie und Praxis

**Theorie:** Lernkarte mit ≤ 90 Wörtern, die Formel steht an Zahlen aus dem aktuellen Gruppenzustand („Dein Markt 1, März: …“). Danach folgen ein Worked Example in 4 Fading-Stufen (03, 1.4), eine Selbsterklärungsfrage und ein **Prüferhinweis** zu typischen Punktverlusten („Rechenweg fehlt = Ansatzpunkt weg“). Productive Failure nur bei Konzeptthemen (Gemeinkostenverteilung, Preisuntergrenze, Investition).

**Praxis:** Fälle im Prüfungsformat (9), entweder im **Übungsmodus** (sofortige Diagnose, Hinweisleiter Konzept → erster Schritt → Worked Example) oder im **Prüfungsmodus** (Zeitlimit, nur Taschenrechner und Formelblatt (E10), Bewertung erst am Ende).

### 6.3 Wiederholung: Pflichtmechanik und Algorithmus

1. **Einheit ist der Skill.** Jeder Skill ist eine FSRS-Karte (ts-fsrs, FSRS v6 mit Potenzkurve; die Exponentialformel aus 03 ist korrigiert, 06 E12). Die Zielretention liegt bei 0,90.
2. **Rating aus dem Ergebnis** (04, 5.2): falsch oder Lösung angezeigt = Again; mit Konzepthinweis oder im 2. Versuch = Hard; im 1. Versuch richtig = Good; schneller als der eigene Median = Easy.
3. **Tagesqueue:** fällige Skills plus **Taper-Skills**. Taper-Skills sind alle Pflichtkanon-Skills, deren prognostizierte Retrievability am Prüfungstag T unter 0,90 liegt; sie bekommen einen Zusatzabruf im Fenster [T−21; T−3].
4. **Priorität:** p = g_HB × g_LZ × (1 − R_heute) × (1 + 0,5 × Fehlerflag). g_HB richtet sich nach der Prüfungsdauer (HB1/HB2 180, HB3 90, HB4 240 Min.), g_LZ nach der Relevanz (hoch 1,0 / mittel 0,6 / niedrig 0,3).
5. **Deckel:** Frühschicht höchstens 8 Items; der Überhang wird **in den nächsten Fall eingebettet** (jede Teilaufgabe zählt als Abruf ihrer Skills), ein Rest wird zum 15-Min.-Auffrischfall des Monats. Es gibt **genau ein Gate**, keine zusätzliche Rost-Sperre (06 W11).
6. **Echtzeit-Spacing:** Ein Skill zählt höchstens einmal je Kalendertag (06 W10); sechs Spielmonate an einem Abend sind ein Übungstag.
7. **Interleaving:** Die Frühschicht mischt mindestens 3 HB. Aufgabentexte nennen die Methode nicht. Tritt eine Misconception 2× in 7 Tagen auf, folgt ein Kontrastpaar-Block.
8. **Pflicht und Ausblick:** Lernziele mit Relevanz hoch oder mittel bilden den Pflichtkanon. Ausblick-Lernziele (ESG, KI, IT) werden geplant, sperren aber nichts.

### 6.4 Mastery (drei Stufen)

| Stufe | Kriterium |
|---|---|
| gelernt | 3 unassistierte richtige Lösungen an ≥ 2 Kalendertagen, davon 1 in einem zweiten Format (03) |
| beherrscht | FSRS-Stabilität ≥ 21 Tage und ≥ 2 richtige Anwendungen im Fallkontext (04) |
| **prüfungsfest** | in einer Probeklausur unter Zeitlimit ≥ 67 % der Punkte auf diesem Lernziel, innerhalb der letzten 30 Tage |

Der Status eines Lernziels ist der schwächste Status seiner Skills. Das Profil zeigt je HB ein Netz aus Stufe und Retrievability sowie die prognostizierte Klausurpunktzahl.

### 6.5 Feedback, Debriefing, Fehler

Feedback kommt in vier Schichten: **sofort** im Übungsmodus als Diagnose aus Fehlerfunktionen (9); **nach dem Fall** als Bewertungsbogen wie bei einer korrigierten Klausur (Punkte je Teilaufgabe, Prüferkommentar, Lösungsskizze); **monatlich** als Nachbesprechung von 3–5 min (drei Zahlen mit Vorhersage, Treiberbaum, Kontrafaktum per Replay, Lehrsatz fürs Notizbuch, 03, 2.3); **verzögert** im Quartalsaudit von Dr. Brand. Jeder Fehler landet im **Fehlerlogbuch** und kehrt in 2–7 Tagen mit neuen Zahlen als Fehlerfall zurück. Wer mit 90 % Sicherheit falsch lag, bekommt eine betonte Erklärung (Hypercorrection). Fehler kosten Vertrauen, sind aber reparierbar; ein Game Over gibt es nicht.

---

## 7. Inhaltsabdeckung

Kapitel: **K1** Pilotmarkt · **K2** Großhandel · **K3** Abfüllung · **K4** Gruppe. Lernziel-Felder nach 6.1.

| HB | Kap. | Module → LZ-Feld | Übung mit Zahlen der Getränkegruppe | Aufgabentyp |
|---|---|---|---|---|
| 1 | K1 | M07 → LZ-1.04 | Hausmarke H50 in Markt 1: VP 6,28 € → VK 10,99 € brutto: Aufschlag 47,0 %, Spanne 32,0 %; Kaskade L01 14,20 → 12,40 → 11,78 €, Gruppen-Einstand 11,66 € | Berechnen, Kalkulationsschema |
| 1 | K1 | M08, M02/M44 → LZ-1.05, LZ-3.01 | März-KER Markt 1: Wareneinsatz 112.100 €, RE I 29,23 %, Pfand aus dem Umsatz trennen (Szene A) | Mehrschritt mit Folgefehler |
| 1 | K1 | M45/M09 → LZ-1.06 | Aktion L01: −141 € im Markt, +259 € in der Gruppe (Szene A) | Rechnen und beurteilen |
| 1 | K2 | M05 → LZ-1.02 | Fuhrpark: sprungfixe Lkw, 2.370 von 2.500 Tourtagen, Diesel ±30 ct = ±33,4 T€ | Kostenauflösung, Zuordnung |
| 1 | K2 | M06/M12 → LZ-1.03/1.08 | KG-BAB: Kostenpools → 0,30 / 0,32 / 0,35 €, Stopp 34,16 €, Mindestbestellwert 125 € | BAB-Lückentabelle (Stufenleiter) |
| 1 | K2 | M09/M33 → LZ-1.06 | Segment-DB III: Gastro 1.120,5 T€ (11,8 %), Wiederverkäufer 22,6 T€ (0,8 %), Märkte intern −169,9 T€; Eckkneipe −498 € (Szene B) | Tabelle, beurteilen |
| 1 | K2 | M14, M15/M48 → LZ-1.10/1.11 | Sattelzug-Selbstabholung (115,6 T€ nach Abholvergütung) gegen Spedition (25–40 €/Palette); Bonus-Vorkauf Brauerei Nord +21,3 T€ (8) | Make-or-Buy, Abgrenzung |
| 1 | K3 | M06/M07 → LZ-1.03/1.04 | Plan-BAB Abfüllung, Maschinenstundensatz 312,55 €/h, Äquivalenzziffern 2,27 / 1,64 / 1,00 (Szene C) | Lückentabelle, Rechenweg |
| 1 | K3 | M14/M25 → LZ-1.10 | Make-or-Buy: Kapitalwert +151 bzw. −1.072 T€, kritische Drittmenge 1,40 Mio. Fl | Entscheidungsvorlage |
| 1 | K3 | M11, M13 → LZ-1.07/1.09 | Bei Kauf Beschäftigungsabweichung 63,1 T€ (649 statt 900 h), bei Lohnabfüllung Preisabweichung Zucker und Verbrauchsabweichung Füllmenge; Target Costing Zuckersteuer (Lücke 3,20 €/Kasten H50) | Abweichungsanalyse, Zielkosten |
| 1 | K4 | M41 → LZ-1.12 | VP in 4 Varianten: Märkte 96,7 / 4,1 / −232,2 / −447,9 T€, Gruppensumme stets −165,8 T€ | Tabelle, Fehlanreiz benennen |
| 1 | K4 | M14/M40 → LZ-1.10 | Markt 3 schließen: −17,9 T€ bei 50 % Logistikabbau, +9,7 T€ bei 100 % | Entscheidung unter Unsicherheit |
| 1 | K3/K4 | M04 → LZ-1.01 | Kalkulatorische AfA der Linie 110 gegen bilanzielle 95 T€; kalkulatorischer Zins auf Wirt-Darlehen (6 % gegen 3 %) | Überleitungstabelle |
| 2 | K2 | M19/M46 → LZ-2.03 | Stoppzahlen-Forecast (Gedat 95,7 → −4 %); Newsvendor für L09 in Markt 1: Q ≈ 799 Kästen | Berechnen, MAPE/Bias |
| 2 | K2/K3 | M25 → LZ-2.05 | Gastro-Darlehen über 30 T€: Barwert des Zinsnachteils 2,7 T€; E-Sattelzug | Kapitalwert, Annuität |
| 2 | K3/K4 | M23/M49 → LZ-2.04 | 13-Wochen-Plan Dezember: Silvester-Überhang 79,0 T€, Vorkauf 38,5 T€, Steuertermine; Plan-Kontokorrent +89,6 T€ | Tabelle mit Folgefehler |
| 2 | K4 | M18/M51 → LZ-2.02 | Budget im Gegenstrom mit Logistik, 3 Märkten und Außendienst; Budget-Slack treiberbasiert aufdecken | Planungstabelle und Moderation |
| 2 | K4 | M16/M17 → LZ-2.01 | Segmentportfolio (Gastro schrumpft, Strecke hängt an 25 Kunden), BSC für die Märkte | Strukturieren, beurteilen |
| 2 | K4 | M37/M50 → LZ-2.06 | Covenants: EK-Quote 28,2 %, NV/EBITDA 2,91, Kapitaldienstfähigkeit 2,03; Stresstest Investition → 3,27 bzw. 3,99 | Szenariorechnung |
| 3 | K1–K4 | M02/M44 → LZ-3.01 | Pfand brutto oder saldiert (28,2 % gegen 30,5 % EK-Quote), Leergutkonto in Mengen abstimmen | Buchen, Abstimmung |
| 3 | K4 | M22 → LZ-3.02 | Strukturbilanz der prüfungspflichtigen KG gegen Konzern; DSO 25 Tage und DPO 26 Tage, beide brutto/brutto (G14) | Kennzahlen, beurteilen |
| 3 | K4 | M40 → LZ-3.04 | Konsolidierung light: Innenumsatz 3.178,4 T€, Schulden 145,1 / 150,0 / 66,0 T€, Zwischengewinn 263 × 3/103 = 7,66 T€ | Konsolidierungstabelle |
| 3 | K4 | M49, M50/M23 → LZ-3.03/3.05 | Gewerbesteuer im Organkreis (Sondervergütung des GF +19,6 T€); Plan-Cashflow und Kapitaldienstfähigkeit nach einer Formel (G15) | Mehrschritt |
| 4 | alle | M26/M27 → LZ-4.01/4.02 | Monatsbericht Segment-DB mit Wasserfall, Kommentar nach Was–Warum–Was tun–Wer bis wann | Satzbaustein-Builder, Diagrammaufgabe |
| 4 | alle | M28 → LZ-4.03 | .xlsx mit 600 Gastrokunden: Pivot nach Klasse, XVERWEIS auf Prozesssätze, Kunden-DB je Kunde, Mindestbestellwert per Zielwertsuche | Tabellen-Labor (Upload) |
| 4 | K2/K4 | M29/M38/M53, M35 → LZ-4.04–4.06 | Stammdatenfehler Flasche/Kasten, Fahrer-Leergutzählung gegen das Lager, Warenkorb Markt 1 (Lift 1,5); ERP-Ablösung, E-Rechnung B2B ab 1.1.2027 (06 F9) | Fehlersuche im Datenraum, TCO |
| 5 | jeder Run | M42/M36/M56 → LZ-5.x | Projektarbeit-Simulator mit 12 Themen aus dem Run (10) | Struktur- und Rubrikprüfung |
| 6 | jeder Run | M43/M55/M51/M01 → LZ-6.x | Präsentation vor GF und Bank, Fachgespräch, Budgetworkshop moderieren, Inventur an 4 Standorten mit Lena | Folienbaukasten, Dialog, Aufnahme |

**Auch in der Gruppe nur schwach abgedeckt:** **M21** (kein Kapitalmarkt, nur Capital Employed je Segment); **Industrie-Breite** (Kuppelprodukte, unfertige Erzeugnisse, mehrstufige Fertigung, Engpass-Maschinenbelegung → Transferfälle); **M40 international** (IFRS, Minderheiten, Equity, Währung; nur HGB light); **M55** (der Controller führt allenfalls eine Assistenz); **CSRD** (nur VSME-Anfragen); **ERP/BI** nicht als echte Systeme; die echte Projektarbeit im eigenen Betrieb und das reale Gegenüber im Fachgespräch.

---

## 8. Branchenspezifische Mechaniken

| Mechanik | Spielregel und Zahlen | Trainiert |
|---|---|---|
| **Vollgut-/Leergutkonten, Pfand** | Konten je Partner und Gebindeart in **Mengen**, ≈ 3,12 Mio. € Pfand pro Jahr; Float 341,7 T€, Silvester-Überhang 30.000 Kästen = 79,0 T€ (G13), Leergutdifferenzen 48,5 T€; monatlich Lieferantenauszug gegen Nebenbuch. | HB3 Ausweis (EK-Quote 28,2 % gegen 30,5 %), HB1 Prozesskosten 0,35 €/Kasten, HB2 Liquidität, HB4 IKS |
| **Wetter-Forecast** | 7-Tage-Prognose mit Fehlerband; L09 in Markt 1: μ = 600, σ = 120, C_u = 2,15 €, C_o = 0,11 € → CR 0,951 → Q ≈ 799 Kästen | HB2 Disposition unter Unsicherheit, MAPE/Bias |
| **Aktionen** | Aktions-EK nur gegen Abverkaufsnachweis, Restmengen werden nachbelastet; Lift, Kannibalisierung, Nachholeffekt aus 02. | HB1 inkrementeller DB, Abgrenzung |
| **Konditionen, Boni, Vorkauf** | Nachvergütungen 417,4 T€/Jahr, 290 T€ aus 2026 offen. Brauerei Nord: Vorjahr 180.000 Kästen, Staffel 1/2/3 % ab 90/100/110 %, Forecast 30.11. 98,5 %. Vorkauf von 2.700 Kästen: Bonus 20,7 → 42,0 T€ (+21,3 T€) gegen 38,5 T€ Bindung (0,36 T€ Zins) und 68 Paletten im Silvester-Peak; zählt laut Klausel der Abverkauf? | HB1 Konditionen, HB3 Abgrenzung und Bilanzpolitik |
| **Gastro-Darlehen** | 1.200 T€ bei ≈ 80 Wirten zu 3 %. Neues Darlehen 30 T€ (6 Jahre, linear): Barwert des Zinsnachteils ggü. 6 % = 2,7 T€ gegen den Kunden-DB. Insolvenzkaskade: Forderung, Darlehensrest, Inventar (20–40 % verwertbar), Leergut. | HB2 Investition und Risiko, HB3 Ausleihungen |
| **Touren, Fuhrpark** | Tourtag 454,30 €, Auslastung 94,8 %, Leerkosten 29,3 T€. Diesel 111.260 l zu 2,00 €/l netto (G9). Beim E-Sattelzug entfallen 20,7 T€ Maut, mautfrei bis 30.6.2031. | HB1 Plankosten, HB2 Investition, ESG |
| **Lager** | Sätze 0,30 €/Kolli (Lagerung), 0,32 € (Kommissionierung), 0,09 € (Beschaffung). Märkte-Lieferungen werden mit 0,35 / 0,7 / 0,8 gewichtet. Interne Logistik 328,8 T€ = 7,3 % des Märkteumsatzes (G20) | HB1 BAB, Leistungsverrechnung, VP |
| **Saison** | Jan.–Apr. Verlust der Märkte, Mai Bestandsaufbau, Dezember Kontokorrent-Spitze; Steuertermine, Dauerfristverlängerung | HB2 13-Wochen-Plan |
| **Ereignisse (gezogen per Seed)** | Gastro-Insolvenz (60 %/Jahr), Preisrunde (+0,50–1,00 €/Kasten mit Vorkaufoption), Fahrerkündigung (50 %), LEH zieht Strecke ab (15 %), Kistenknappheit (10 %), Zuckersteuer. Jedes Ereignis löst ein Fall-Template aus. | quer über HB1–HB3 |
| **Hausmarke** | Zuckersteuer 32 ct/l = 3,20 €/Kasten H50: Drifting 9,30 € gegen Allowable 6,10 € (32 % Marktspanne bei 10,99 €); Alternative Reformulierung unter 5 g/100 ml (Grundstoff 0,11 €/l, HK 5,70 €) mit Absatzrisiko; Make-or-Buy und Verhandlung (Szene C) | HB1 Target Costing und Industrie-KLR, HB2 Steuern als Planungsgröße |

---

## 9. Aufgabentypen und automatische Bewertung

| Typ | Beispiel | Bewertung |
|---|---|---|
| Berechnen | Wareneinsatz März | Toleranz je Größenart (±1 € bzw. ±0,5 %, Quoten ±0,1 Prozentpunkte); Punkte für Ansatz, Rechenweg und Ergebnis |
| Lückentabelle | BAB, Kalkulationsschema, Kunden-DB | zellweise, mit Folgefehlerlogik |
| Rechenweg-Raster | Formel wählen → einsetzen → Ergebnis | Teilpunkte wie in Lösungshinweisen üblich **[Vermutung, keine Originalaufgaben]** |
| Buchen / Zuordnen | Pfandbuchung, Kostenart fix/variabel | Menge von Soll-/Haben-Zeilen, Reihenfolge egal |
| Argumentkarten | „Beurteilen Sie …“: 3 aus 8 Karten | +1 je tragfähiges Argument, falsche kosten Punkte, Wertung und Empfehlung zählen gesondert |
| Kurzfreitext | Abweichungskommentar | Regelprüfer (Betrag, Richtung, Schlüsselbegriffe); LLM-Rubrik optional und **nur als Feedback** (04, 6) |
| Fehlersuche | „Finde den Fehler in Lenas BAB“ | Stelle plus Korrektur |
| Diagramm deuten | Wasserfall Segment-DB | Markieren, Auswahl |
| Entscheidungsvorlage | 3-Satz-Empfehlung | Satzbausteine plus Pflichtelemente (Zahl, Bedingung, Termin) |
| Datei (HB4) | .xlsx-Upload | Werte in benannten Zellen, Formeln vorhanden, keine hart codierten Zahlen |
| Struktur (HB5) | Gliederung, Exposé | Pflichtkapitel, Zahlengleichheit mit dem Rechenkern |

**IHK-Format im Spiel:**

- **Operatoren mit Punkteregel:** „nennen“ 1 P je Nennung; „erläutern“ 2 P (Nennung plus Begründung); „berechnen“ 1/1/1 für Ansatz, Weg und Ergebnis; „beurteilen“ 2–4 P für Kriterium, Wertung und Empfehlung.
- **Zeitbudget:** 1,8 min je Punkt bei HB1/HB2 (180 Min. für 100 P) **[Vermutung: Punktzahl je Klausur nicht belegt]**.
- **Notenschlüssel:** 100–92 / 91–81 / 80–67 / 66–50 / 49–30 / 29–0 **[wahrscheinlich, IHK-üblich]**.

**Folgefehler:** Jede Fallinstanz trägt einen Lösungsgraphen. Der Prüfer rechnet jede Teilaufgabe mit den **eigenen Vorwerten des Spielers** nach, ein Folgefehler kostet keine Punkte. Die Diagnose meldet: „Fehler nur in Schritt 2“.

**Fehlerdiagnose:** Jedes Template führt Fehlerfunktionen mit, die den falschen Wert erzeugen: M1–M12 aus 03 (Aufschlag statt Spanne, brutto statt netto, Pfand im Umsatz, Vorzeichen der Bestandsveränderung …) und neu für die Gruppe: „VP verändert das Konzernergebnis“, versunkene Inventar-AfA als relevant gezählt, nicht abbaubare Fixkosten in Make-or-Buy, Äquivalenzziffer je Flasche statt je Liter, Zwischengewinn nicht eliminiert, DPO brutto gegen netto, rückwirkende Bonusstaffel als Grenzstaffel, vermischte Formeln der Kapitaldienstfähigkeit (G15). Ratedetektion bei Antworten unter 3 s; jede Wiederholung bringt neue Zahlen.

---

## 10. Training für HB4, HB5 und HB6

**HB4 – Tabellen-Labor.** Drei Stufen:

1. **Mikroübungen** im Browser-Raster mit eigenem Formelparser (04, 2.5): Bezüge, SUMMEWENNS, XVERWEIS, WENN, RUNDEN.
2. **„Baue nach“-Aufträge:** Rohdaten der Gruppe als .xlsx (600 Gastrokunden mit Umsatz, Stopps, Kolli; Leergut-Bewegungen; Segment-Monatswerte). Der Spieler baut den Bericht in Excel oder LibreOffice und lädt ihn hoch; geprüft werden benannte Ergebniszellen, Formeln statt Werte und vorhandene Diagramme.
3. **240-Min.-Probeübung** mit 4–5 Blöcken: Datenaufbereitung, Kennzahlen, Abweichungsbericht, Szenario/Zielwertsuche, Visualisierung nach IBCS.

Grenze: Gestaltungsqualität bewertet nur eine Rubrik mit Musterdatei. Welches Programm die IHK stellt, ist offen **[Vermutung: meist Excel]**; getestet wird gegen beide.

**HB5 – Projektarbeit-Simulator.** Die 30 Kalendertage werden als 30 Spieltage simuliert, verteilt auf 2–3 Echtwochen.

Tag 0: **zwei Themenvorschläge** (§ 4 Abs. 1–5 **[sicher, 01]**), der Ausschuss wählt einen **[wahrscheinlich]** · Tage 1–5 Auftragsklärung, Issue Tree · 6–15 Ist-Analyse im Datenraum · 16–22 Alternativen und Rechenkern (.xlsx) · 23–28 Empfehlung, Umsetzung, Risiken · 29–30 Formalia.

**Themenpool aus dem Run:** eigene Abfüllung, Portfolio der 340 C-Kunden, VP-System KG → Märkte, Zukunft von Markt 3, E-Sattelzug, Bonus-Tracking, Covenant-Monitoring, Kostenstellen-Budgetierung, ERP-Ablösung, IKS im Leergutprozess, Hausmarke und Zuckersteuer, Mindestbestellwert-Modell.

**Bewertung:** Automatisch geprüft werden Pflichtkapitel, Zahlengleichheit von Text und Rechenkern, quantifizierte Empfehlung, genannte Risiken und Umfang. Den Inhalt bewertet der Spieler selbst (optional mit LLM-Feedback) anhand einer Rubrik aus § 4 Abs. 5: Analyseinstrumente angewandt, Alternativen verglichen, Empfehlung gegeben, als Beratungsleistung aufbereitet. Export als .docx/.pdf für Dozent oder Mentor.

**Transfer-Werkstatt:** Dieselben Schablonen werden auf den **eigenen Betrieb** angewandt. Das ist für die echte Prüfung nötig **[wahrscheinlich: betrieblicher Bezug der Projektarbeit]**.

**HB6 – Präsentation und Fachgespräch.** Insgesamt höchstens 45 Min. (01, IHK Koblenz).

- **Folienbaukasten** mit ≤ 10 Folien, Kernaussage im Titel, SCQA-Struktur und IBCS-Presets. Die Zahlen sind an den Rechenkern gebunden.
- **Probedurchlauf mit Timer**, optional mit lokaler Audioaufnahme (MediaRecorder, kein Upload) und Selbstbewertung nach Rubrik.
- **Fachgespräch-Simulator:** Fragen aus der eigenen Arbeit (Annahmen, Sensitivität, verworfene Alternativen, Methodenkritik) und HB6-Stoff (Teamführung, Moderation, Konflikt, laut § 4 Abs. 6 **[sicher]**). Drei Prüfer-Personas, Antwortschema „Kernaussage – Begründung – Zahl – Grenze“.
- **Situationsfälle:** Budgetworkshop mit Lenz und Kowalski moderieren (Konflikt um den VP), Inventurteams an 4 Standorten mit Lena führen (Zählplan, Zweitzählung ab 2 % Abweichung), Feedback nach Situation–Verhalten–Wirkung.

Grenze: Der Dialogbaum trainiert Erkennen, nicht Auftreten; empfohlen ist ein Lerntandem (E8).

---

## 11. Drei Beispielszenen

### Szene A – „Monatsabschluss März, Markt 1“ (K1, 20 P, 36 min Prüfungstakt)

**Situation (aus dem Zustand erzeugt):** Sabine Kowalski schickt die Märzdaten; der GF fragt: „Warum liegt Markt 1 unter Plan, obwohl wir die Bieraktion hatten?“ **Anlagen:** Z-Bon-Summen (Warenumsatz 19 % brutto 182.903,00 €, 7 % brutto 5.029,00 €; Pfandausgabe 31.400,00 €, Leergutbons 30.150,00 €); Bestände zu VP (AB 01.03. 121.300 €, Lieferungen der KG ohne Pfand 114.900 €, EB 31.03. 124.100 €); Plan (Umsatz 161.250 € = 7,5 % von 2.150 T€, RE-Quote 29,12 %); Datenblätter H50 und L01.

| Teilaufgabe | P | Lösung | Fehlerfunktionen |
|---|---|---|---|
| 1. Netto-Warenumsatz ermitteln; Pfand begründet zuordnen | 5 | 153.700 + 4.700 = **158.400 €** (3 P). Pfand ist kein Erlös. Der Saldo von 1.050,42 € netto geht über das Pfandkonto bzw. den Erstattungsanspruch gegen die KG (2 P) | 159.450,42 → M3 (Pfand im Umsatz); 187.932 → M2 (brutto) |
| 2. Wareneinsatz, RE I, Abweichung zum Plan zerlegen | 5 | WE = 121.300 + 114.900 − 124.100 = **112.100 €**; RE I 46.300 € = **29,23 %**. Abweichung −650 € = Menge −829,81 € und Spanne +179,81 € | 25,69 % → M4 (WE 117.700); 41,3 % → M1 (Aufschlag) |
| 3. Hausmarke H50: HK 6,10 €, VP +3 % = 6,28 €, VK 10,99 € brutto. Aufschlag, Spanne, Faktor? Spanne bei Aktion zu 9,99 €? | 4 | Aufschlag **47,0 %**, Spanne **32,0 %**, Faktor **1,470**; bei Aktion **25,2 %** | Spanne auf brutto gerechnet → M2 |
| 4. Aktion L01, KW 12: Normalwoche 120 Kästen, Lift ×4, 60 % der Mehrkästen kannibalisieren (db 3,16 €), 48 Kästen Nachholeffekt, 150 Zusatzbons à 3,70 € Verbund-RE, WKZ 400 € an die KG. Inkrementeller Erfolg für Markt und Gruppe; beurteilen | 6 | db normal 2,69 €, in der Aktion 0,91 € (VP aus 12,40 × 0,94 × 1,03 bzw. 8,60 × 0,94 × 1,03). 436,21 − 323,02 − 680,40 − 129,21 + 555,00 = **−141,41 € für den Markt**, mit WKZ **+258,59 € für die Gruppe** (4 P). Wertung: Die Marktleitung streicht die Aktion rational, die Gruppe verliert dadurch. Ursache ist die VP-Regel, nicht die Aktion (2 P) | Aktion am Umsatz gemessen; Kannibalisierung vergessen (+539 €) |

**Spielfolge:** Ab 15 Punkten erhält die Vorlage an den GF die Option „WKZ über die VP-Regel durchreichen“; sie kehrt in K4 als VP-Fall wieder. Die sechs Skills (ust.netto, pfand.umsatz, we.bestand, abw.menge-spanne, kalk.spanne-aufschlag, aktion.inkrementell) gehen in FSRS. Ein Fehler in Teilaufgabe 2 erzeugt nach 2 Tagen einen Fehlerfall mit Aprilzahlen von Markt 2.

### Szene B – „Die Eckkneipe“ (K2, Oktober 2027, 20 P)

**Situation:** Der GF will C-Kunden mit negativem DB III kündigen; Ralf Becker widerspricht: „Die Eckkneipe bringt 12.000 € Umsatz!“ **Anlagen:** Kundenblatt (Umsatz 12.000 €, RE I 4.200 €, 52 Stopps, 670 Kolli, 0,85 Leergutkästen je Kolli, 12 Außendienstbesuche, Leihinventar-AfA 1.500 €, Ausfallrisiko 2 %); Prozesskostensätze aus dem KG-BAB (Lagerung plus Beschaffung 0,39 €/Kolli, Kommissionierung 0,32 €/Kolli, Leergut 0,35 €/Kasten, Stopp 34,16 €, Besuch 41,81 €).

| Teilaufgabe | P | Lösung |
|---|---|---|
| 1. Kunden-DB I–III vervollständigen | 6 | Lagerung/Beschaffung −262, Kommissionierung −217, Leergut −201, Stopps −1.776 → **DB II 1.743 €**; Außendienst −502, AfA −1.500, Ausfall −240 → **DB III −498 €** |
| 2. Mindestbestellwert für DB = 0 bei Gastro-C (Segment-RE 33 %, Kollikosten 5,67 % vom Umsatz) | 4 | 34,16 ÷ (33 % − 5,67 %) = **125 €**. Der Ø-Bestellwert der Eckkneipe liegt bei 230,77 €, jeder Stopp deckt sich also. |
| 3. 14-tägige Belieferung bei gleichem Absatz | 4 | 26 Stopps = 888 € → **DB II 2.632 €, DB III +390 €**; Bestellwert 461,54 € |
| 4. Kündigung oder Halten beurteilen (Argumentkarten) | 6 | Die AfA auf das vorhandene Inventar ist **versunken**. Entscheidungsrelevant sind DB II − Außendienst − Ausfall = **+1.002 €** (52 Stopps) bzw. **+1.890 €** (26). Also nicht kündigen, sondern den Rhythmus umstellen. Die Umsatzprämie im Außendienst setzt einen Fehlanreiz; Vorschlag: Prämie auf DB II (M51) |

**Fehlerfunktionen:** volle Kündigungswirkung inklusive AfA (−498 € als „Ersparnis“), Stoppkosten ohne Auftragsabwicklung (28,61 €), Mindestbestellwert ohne Kollikosten (103,52 €).

**HB6-Anschluss:** Dialog mit Becker in 4 Zügen. „Ihr Kunde kostet uns Geld“ eskaliert (Glasl-Stufe 2), „Wie viel Lager hat der Wirt für zwei Wochen?“ öffnet den Kompromiss; das Ergebnis geht ins Vertrauen und ins mündliche Profil. **Folgefall:** Der Seed macht 30–50 % der C-Kunden ähnlich; daraus entsteht die Pivot-Analyse der 340 C-Kunden im Tabellen-Labor und der HB5-Themenvorschlag „Lieferrhythmus-Modell“.

### Szene C – „Selbst abfüllen?“ (K3, Oktober 2028, Planjahr 2029, 30 P, 2–3 Sessions)

**Situation:** Brunnenhof kündigt für 2029 **+15 %** an. Eine Regionalbrauerei bietet für den Fall einer eigenen Linie einen Dreijahresvertrag über 1,6 Mio. Fl 0,5 l zu **0,165 €/Fl**. Angeboten ist eine generalüberholte Gebrauchtlinie: Anschaffung 950 T€, Wiederbeschaffungswert 1.100 T€, Nutzungsdauer 10 Jahre, 550 m² Hallenfläche zu 5,50 €/m² und Monat, Nennleistung 6.000 / 5.500 / 4.500 Fl/h (0,33 / 0,5 / 1,0 l), Nutzungsgrad 65 % **[Vermutung]**. Planbeschäftigung **900 Belegungsstunden** (Hausmarke 295,4 h Lauf + 104 h Rüsten für 52 Chargen, Drittauftrag 447,6 h + 52 h).

**Anlage Plan-BAB (Primärkosten, T€):** H1 Medien (Energie, Druckluft, CO₂, Wasser) 61,58 · H2 Technik (Personal, Instandhaltung) 83,50 · F1 Ausmischung (Personal, AfA, Zins, Raum, Labor) 52,30 · F2 Linie 229,71 (Bedienung 75,60, AfA 90, Zins 23,10, Raum 26,40, Hilfsstoffe 10,61, Versicherung 4). Umlageschlüssel: H1 → H2 / F1 / F2 = 5 / 15 / 80 %; H2 → F1 / F2 = 10 / 90 %.

| Teilaufgabe | P | Lösung |
|---|---|---|
| 1. Stufenleiterverfahren, Endkosten, Maschinenstundensatz | 8 | H1 → 3,08 / 9,24 / 49,26; H2 (86,58) → 8,66 / 77,92. **F1 70,19 T€** (0,0523 €/l bei 1.342.560 l), **F2 356,89 T€**. MSS ohne Bedienung **312,55 €/h**, mit Bedienung **396,55 €/h** |
| 2. Äquivalenzziffern je Liter aus der Laufzeit, Linienkosten je Kasten, Make-HK gegen Buy-HK | 6 | ÄZ = 4.500 ÷ (6.000 × 0,33) = **2,27**; 4.500 ÷ (5.500 × 0,5) = **1,64**; **1,00**. 1,0 l kostet 396,55 ÷ 2.925 = 0,1356 €/l; je Kasten **2,44 / 2,22 / 1,63 €**. Rüsten 793 € je Charge = 0,75 €/Kasten. Make-HK 5,68 / 5,80 / 5,45 € gegen Buy 6,15 / 6,10 / 5,32 € → **eigene Linie bei 0,33 und 0,5 l günstiger, bei 1,0 l nicht** |
| 3. Make-or-Buy kalkulatorisch und dynamisch, kritische Menge | 6 | Fixkosten Make 289,3 T€ (kalk. AfA 110, Zins 28,5, Raum 36,3, Personal 80 u. a.), variabel 141,31 €/h + 0,026 €/Fl + 0,006 €/l. Hausmarke allein: Make 376,3 > Buy 221,3 T€; kritische Menge **2,27 Mio. Fl** (Ist 1,05 Mio.). Mit Drittauftrag (DB 166,2 T€ = 0,104 €/Fl): Make 210,1 < 221,3 T€. Kapitalwert (10 Jahre, 6 %, RBF 7,3601): Ersparnis 149,6 T€ pro Jahr → **+151,4 T€**, ohne Drittauftrag **−1.071,9 T€**. Kritische Drittmenge **1,40 Mio. Fl** (−12 %) |
| 4. Kalkulation von Brunnenhof prüfen (je 1.000 Fl 0,5 l): Material 32,00; MSS 336 €/h ÷ 5.000 Fl/h = 67,20; Lohn 12,80; QS 4,00; Rüsten 2,5 h × 400 € ÷ 20 = 50,00 → HK 166,00; +15 % VwVt = 190,90; +10 % Gewinn = 209,99. Angebot: alles +15 % = 241,49 | 5 | Begründet ist nur der Kostenanstieg (Energie 30 % des MSS +40 %, Lohn +5 %, Material +3 %): HK 181,10 → **229,10 € (+9,1 %)**. Bei Losgröße 40.000 Fl ergibt sich **194,03 € (−7,6 % gegenüber 2027)**. Variable Kosten von Brunnenhof ≈ 103 €. Verhandlungsziel: Lose verdoppeln, Energieklausel nur auf den Energieanteil |
| 5. Covenants pro forma (Plan 31.12.2027, Investition kreditfinanziert); Empfehlung in 3 Sätzen | 5 | NV/EBITDA 2,68 → **3,27** mit Drittauftrag, **3,99** ohne (**Bruch**, > 3,5); EK-Quote 30,1 % → 26,7 %. Empfehlung: „Kauf nur bei festem Drittvertrag ≥ 1,4 Mio. Fl pro Jahr über ≥ 3 Jahre mit Ausgleich bei Minderabnahme. Sonst Brunnenhof auf ≤ 0,21 € bei 40.000er-Losen verhandeln. Entscheidung bis 30.11.“ |

**Fehlerfunktionen:** Äquivalenzziffern je Flasche statt je Liter; kalkulatorische AfA als Auszahlung im Kapitalwert; Raum und Techniker bei „nur Hausmarke“ weggelassen; Pauschalerhöhung akzeptiert; Covenant mit EBITDA ohne Ersparnis.

**Spielfolge:** Der GF entscheidet mit einer Wahrscheinlichkeit aus Vorlagenpunkten und Bedingungen. **Bei Kauf** läuft ab 2029 monatlich Industrie-KLR (BAB, Plankosten, Bestandsbewertung zu HK). Halbiert der Seed den Drittauftrag, fallen 649,2 Ist-Stunden an: Sollkosten 320,57 T€, verrechnete Plankosten 257,44 T€, **Beschäftigungsabweichung 63,13 T€**, Verbrauchsabweichung 6,40 T€. Daraus wird der Fall „Wer ist schuld?“ mit dem Lehrsatz „Leerkosten sind keine Verschwendung“. **Ohne Kauf** folgen eine jährliche Schattenrechnung, die monatliche Nachkalkulation von Brunnenhof und Transferfälle. In beiden Zweigen wird „Eigene Abfüllung“ zum HB5-Thema mit Präsentation vor GF und Bank.

---

## 12. Technik (auf 04 aufbauend) und MVP-Schnitt

Basis bleibt 04 (Angular-22-PWA, local-first, deterministische TS-Engine mit Integer-Cent, ts-fsrs, Dexie, ECharts, exceljs, Cloudflare Pages). Neu:

1. **Zustandsmodell:** Monatsaggregate je Gesellschaft, Segment, Kundenklasse und Kostenstelle plus benannte Einheiten (≈ 20 Kunden, 3 Märkte, 15 Fahrzeuge, 5 Lieferanten, Hausmarke); Hauptbuch nur, wo Fälle es brauchen (Markt 1, Abschlussfälle). **Golden Master:** Skript aus 08 (94 Prüfungen) plus Hausmarken-Delta.
2. **Fallmaschine** (`packages/cases`): Sie erzeugt eine Fallinstanz aus Template, Zustandsausschnitt, Seed und fälligen LZ.
   ```ts
   interface CaseTemplate { id; lz: string[]; hb: 1|2|3|4|5|6; trigger: Ausdruck;
     anlagen: AnlagenGen[]; teilaufgaben: { id; operator; punkte; solverId; checker;
     rechenweg: Schritt[]; dependsOn: string[]; fehlerfunktionen: string[] }[];
     zeitMin: number; spielwirkung?: DecisionCardId }
   ```
   **Auswahlregel:** Ein Template wird gewählt, wenn es (a) fällige LZ abdeckt, (b) zum Monat oder Ereignis passt und (c) seine Oberfläche zuletzt nicht gesehen wurde. **Abdeckungsgarantie:** Passt kein natürlicher Fall, kommt ein Sonderauftrag (Bank, Verbund) oder ein Transferfall.
3. **Weiteres:** Lernziel-Katalog und `skript_map.yaml` mit Zod-Schemas, Abdeckungsbericht in der CI; xlsx-Prüfer (exceljs liest Werte, `cell.formula`, definierte Namen); MediaRecorder für HB6 nur lokal; LLM optional, nur als Feedback (04, 6).

| Stufe | Inhalt | PT [Vermutung] |
|---|---|---|
| **K0 Kernbeweis** | Kein Spielrahmen. Zustand = Golden Master + Seed-Perturbation von 20 Parametern; 6 Templates (Szene A/B und 4 weitere, HB1–HB3); Bewertungsbogen mit Folgefehler und Fehlerfunktionen; Frühschicht mit FSRS; Profil je LZ | **20–28** |
| **K1 MVP** | dazu ein spielbarer Monat (März 2027, Markt 1 + KG), 2 Entscheidungskarten, Monats-Gate, 45-Min.-Probeklausur, 1 .xlsx-Auftrag, Lernziel-Mapping und Abdeckungsbericht, 8 Templates, 12 Lernkarten | **39–56** (mit KI-Unterstützung ≈ 30–45) |
| Version 0.5 | Stufe 1 komplett (K1/K2), Tabellen-Labor, Jahresprüfung | 110–160 |
| Version 1.0 | Stufen 1–3, Make-or-Buy-Zweige, HB5/HB6-Modi, ≈ 120 Templates | 240–450 |

**K1 im Detail:** Setup 2–3 · Zustandsmodell und Golden Master 4–6 · Fallmaschine 6–8 · Prüfer 4–6 · xlsx 2–3 · FSRS, Dexie, Profil 3–4 · UI 7–10 · LZ-Katalog 2–3 · Inhalt und Review 6–9 · Playtest 3–4.

**Beweiskriterien für K0/K1** (5 Lehrgangsteilnehmende, 3 Wochen): ≥ 70 % spielen an ≥ 10 von 21 Tagen; die Probeklausur steigt bei neuen Seeds um ≥ 15 P; die Automatik stimmt in ≥ 90 % der Teilpunkte mit einer blinden Dozentenkorrektur überein; ein neues Template kostet ≤ 0,5 PT.

Ehrlich: Version 1.0 heißt im Hobbytempo (1,5 PT/Woche) 3–6 Jahre. Engpass ist der Inhalt; die Skripte beschleunigen ihn, ersetzen aber kein Fachreview.

---

## 13. Risiken und Gegenmaßnahmen

| Risiko | Gegenmaßnahme |
|---|---|
| Eigene Aufgaben verfehlen den Prüfungsstil | Abgleich mit Skripten und gekauften Altaufgaben (DIHK-Shop) nur intern, ohne Übernahme; Dozenten-Review |
| Zahlen- oder Fachfehler | Golden-Master-Tests, keine handgepflegten Zahlen (06, 2.3), Fachreview aus GFGH-Controlling, Spannen mit Annahme-Kennzeichnung |
| Grind und Abbruch | Pflicht ≤ 30 % je Session, Fälle mit Spielwirkung, Belohnung durch Vertrauen und Verantwortung, kein Streak-Zwang |
| Überanpassung an die Getränkebranche | 10–15 % Transferfälle, ≥ 3 Oberflächen je LZ |
| HB5/HB6 nicht bewertbar | Struktur automatisch, Inhalt per Rubrik, Export für Mentoren, Lerntandem |
| Rechtliches (IHK-Name, Prüfungsaufgaben, Skripte, Marken) | kein „IHK“ im Titel, Disclaimer, nur eigene Aufgaben, fiktive Marken (05, 6) |
| Rechtsstand altert (Zuckersteuer, Mindestlohn, E-Rechnung) | Rechtsstand je Version einfrieren; Zuckersteuer bleibt Ereignis, nicht Plan |
| Kleine Zielgruppe (80–115 pro Jahr) | Nebenzielgruppen über HB1–HB3-Pakete; Lehrgangsträger als Kanal |
| Umfang eines Ein-Personen-Projekts | Stufenplan K0 → K1 → 0.5; ein Kapitel erst messen, dann planen (06, Karte 87) |

---

## 14. Offene Designentscheidungen

| Nr. | Frage | Optionen | Empfehlung |
|---|---|---|---|
| E1 | Prüfungstermin als Steuergröße? | a) Countdown mit Tapering · b) nur FSRS · c) frei | **a** |
| E2 | Run nicht bestanden | a) Wiederholungsjahr, neuer Seed · b) nur Warnung · c) frei weiter | **a**, b für Wiedereinsteiger |
| E3 | Hausmarke | a) Limonade · b) Apfelschorle · c) Mineralwasser | **a** (4.3); c scheidet aus |
| E4 | Transferfälle fremder Branchen in HB1 | a) 0 % · b) 10–15 % · c) 25 % | **b** |
| E5 | Ausgang Make-or-Buy | a) offen (Vorlage + GF-Wahrscheinlichkeit) · b) Kauf fest · c) kein Kauf fest | **a** mit Abdeckungsgarantie |
| E6 | HB4-Werkzeug | a) nur Browser · b) .xlsx-Upload Pflicht ab Stufe 2 · c) beides frei | **b** |
| E7 | HB5-Bewertung | a) Selbst + Rubrik · b) + LLM-Feedback · c) + Mentor-Export | **a + c**, b optional |
| E8 | HB6-Audioaufnahme und Lerntandem | a) nein · b) Aufnahme lokal · c) Aufnahme + Tandem-Code | **b**, c später |
| E9 | Lernziel-Katalog | a) jetzt aus Verordnungswortlaut, Skripte später mappen · b) auf Skripte warten | **a** |
| E10 | Hilfsmittel im Prüfungsmodus | a) wie IHK-Hilfsmittelliste · b) plus Formelblatt · c) frei | **a**, bis zur Liste b |
| E11 | Mastery-Stufen | a) zwei (06 W7) · b) drei mit „prüfungsfest“ | **b** |
| E12 | Simulationstiefe | a) Monatsaggregate + Entitäten · b) Tagestick der ganzen Gruppe | **a**; Tagestick nur für Markt 1 |
| E13 | Hinweise im FSRS | a) Konzepthinweis = Hard, Worked Example = Again · b) jede Hilfe = Again | **a**; Mastery nie mit Hilfe |
| E14 | Umfang des Pflichtkanons | a) nur Relevanz hoch · b) hoch und mittel · c) alle | **b** |
