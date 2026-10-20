# VOLLGUT – Finales Konzept: Controller/in in der Getränkegruppe

Stand 20.10.2026. Sicherheitsstufen: **[sicher]** belegt oder nachgerechnet · **[wahrscheinlich]** starke Ableitung oder Einzelquelle · **[Vermutung]** Annahme oder Designvorschlag. ⟨Entscheidung: …⟩ markiert Annahmen des Standardpfads, die der Kunde per Entscheidungskarte ändern kann; die vollständige Liste steht in `offene-entscheidungen.md`. Alle Betriebszahlen sind Annahmen. Basis ist das skriptgeprüfte Modell aus 08 in der Variante **ohne Kelterei**, ergänzt um die Hausmarke und den Make-or-Buy-Fall. Jede neue Zahl stammt aus `rechenmodell/final.py`, das auf dem 08-Modell rechnet und Plausibilitätsprüfungen enthält. Beträge in T€, in Belegen und Szenen in €.

---

## 1. Kurzfassung und Arbeitstitel

1. „VOLLGUT“ ist ein Browser-Lernspiel (offline-fähige PWA). Darin ist man drei Geschäftsjahre lang (2027–2029) Controller/in einer Familien-Getränkegruppe: ein Getränkefachgroßhandel (KG, 17,6 Mio. € Außenumsatz, 600 Gastrokunden), drei eigene Abholmärkte und eine Hausmarke Limonade, die ein fremder Lohnabfüller abfüllt.
2. Gespielt wird ein Controlling-Schreibtisch: Posteingang, Monatsabschluss AT1–AT5, Leergutkonten in Stück, Bonus-Tracking, Liquiditätsvorschau, Budgetrunde und Covenant-Bericht. Der Spieler empfiehlt, die Geschäftsführung entscheidet nach einer sichtbaren Regel.
3. Die Kampagne führt vom Pilotmarkt (KLR-Grundlagen, Handelskalkulation, Pfand) über den Großhandel (Prozesskosten, Kunden-DB, Touren, Konditionen, Darlehen) zur Gruppe (Verrechnungspreise, Budget, Bank, Konsolidierung light). Ab 2028 kommt der Projektbogen „eigene Abfüllanlage?“ hinzu: Plan-BAB, Maschinenstundensatz, Äquivalenzziffern, Plankosten.
4. Eine Fallmaschine erzeugt jeden Vorgang aus dem Spielstand als Situationsaufgabe mit IHK-Operatoren, Punkten und Folgefehlerbewertung. Damit ist jede Arbeit im Spiel zugleich Prüfungstraining.
5. Wiederholung ist Pflicht: Die Routinen kehren jeden Monat mit neuen Zahlen wieder, und fällige Fertigkeiten (Echtzeit-Scheduler FSRS) werden in den Monatsabschluss eingebettet, der ohne sie nicht schließt. Eine 5-Minuten-Frühschicht räumt sie vorher ab.
6. Gelerntes schaltet Werkzeuge frei, die mehr sichtbar machen. Vergessenes lässt sie „beschlagen“.
7. Alle Inhalte hängen über stabile Skill-IDs an opaken Lernziel-IDs je Handlungsbereich HB1–HB6. Die Lehrgangsskripte werden später als reine Datenzuordnung (`skript_map.yaml`) eingehängt.
8. Ehrlich: Tief trainiert werden der schriftliche Teil (25 % der Note) und die Methodik von Projektarbeit und Fachgespräch. Die 75 % aus diesen beiden Teilen kann das Spiel nicht bewerten, und Version 1.0 kostet ≈ 300–420 Personentage.

**Arbeitstitel:** „VOLLGUT – Controlling in der Getränkegruppe“. Alternative ist „Leergut kommt zurück“ (Wiederholungsmetapher). „IHK“ steht nicht im Namen (05, 6.1); vor der Veröffentlichung DPMA-Register prüfen ⟨Entscheidung: Arbeitstitel⟩.

**Designbasis:** Die Gutachten waren uneins (Summe der Punkte: Routine 99, Prüfung 98, Kampagne 96). Basis ist der Routine-Entwurf, weil er die Kundenforderung „alle Aufgaben machen und wiederholen“ am direktesten als Spielmechanik umsetzt und für einen Einzelentwickler am besten baubar ist. Einem Prüfungstrainer nachträglich Spielspaß einzubauen ist schwerer als einem Spiel das Prüfungsformat. Aus dem Prüfungsentwurf kommen deshalb Fallmaschine, IHK-Format, Countdown und `skript_map`, aus dem Kampagnenentwurf Leitfragen, Figuren sowie die Aktions-, Eckkneipen- und Abfüllszene ⟨Entscheidung: Grundrichtung⟩.

---

## 2. Ehrliche Grenzen der Grundidee und Umgang damit

| Grenze | Befund | Umgang im Konzept |
|---|---|---|
| **75 % der Note sind Projektarbeit (45 %) und Mündlich (30 %)** | § 7 Abs. 4 ContrPrV **[wahrscheinlich: über Suchauszug, Volltext ungelesen]**. Eine 30-Tage-Arbeit im eigenen Betrieb und ein Fachgespräch kann keine Software verlässlich bewerten **[sicher]**. | HB5-Werkstatt mit **Pflicht-Transferpfad auf den eigenen Betrieb** und Export für Mentor oder Dozent; HB6-Werkstatt mit Fachgesprächs-Personas, lokaler Selbstaufnahme und Peer-Rollenkarten (Abschn. 10). Versprochen wird „vorbereitet“, nicht „bewertet“. Vor jedem Prüfungsmodus wird der Verordnungstext geprüft (Bestehensregeln, Hilfsmittel). |
| **Pflicht-Wiederholung über alle Facetten kostet Übezeit** | Pflichtkanon ≈ 190 Skills × ≈ 9 Abrufe bis zum Prüfungstag ≈ 1.700 Abrufe **[Vermutung, Rechnung]**. „Beherrscht“ (Stabilität ≥ 21 Tage) ist je Skill frühestens nach ≈ 4–6 Wochen Echtzeit erreichbar **[wahrscheinlich, ts-fsrs-Standardparameter]**. | Etwa die Hälfte der Abrufe stecken in Routinen und Fällen. Die Frühschicht trägt den Rest (≈ 850 Items ≈ 11 h). Gesamtaufwand ≈ 100–120 h über 6–9 Monate (≈ 3–4 h pro Woche). Pflicht sind nur Lernziele mit IHK-Relevanz hoch oder mittel ⟨Entscheidung: Pflichtkanon-Umfang⟩; Lastdeckel 30 % je Session, Routine-Kompression und Rückkehrmodus (Abschn. 5/6). |
| **HB4 wird 240 Min. am Tabellenkalkulationsprogramm geprüft** | **[sicher, 01]**; ein Browser-Rechenblatt ist kein Excel. | Excel-Werkstatt: Datenpaket als .xlsx, Abgabe mit benannten Zellen, Prüfung auf hartkodierte Zahlen und Prüfsummen (Abschn. 10). |
| **Industrie-KLR nur über Lohnabfüllung und Make-or-Buy** | Lohnabfüllung liefert keinen BAB mit eigenen Fertigungsstellen. Ohne Kauf gibt es keine Bestandsveränderungen aus eigener Fertigung, keine Kuppelprodukte und keine mehrstufige Fertigung **[sicher]**. HB1 ist industriegeprägt **[wahrscheinlich, 06]**. | Plan-BAB, Maschinenstundensatz, Bezugsgrößen- und Äquivalenzziffernkalkulation, Plankosten und die Prüfung der Lohnabfüller-Kalkulation sind in **beiden** Zweigen Pflicht. Im Kauf-Zweig läuft ab 2029 monatlich Industrie-KLR, im Buy-Zweig eine Open-Book-Nachkalkulation. Dazu kommen **10–15 % Pflicht-Transferfälle** aus fremden Branchen (Kuppel-, Divisions-, Normalkosten-BAB, GKV/UKV mit Bestandsveränderung) ⟨Entscheidung: Transferanteil⟩. |
| **Größere Simulation = mehr Bauaufwand** | GFGH plus Märkte kosten +80–130 PT gegenüber dem Einzelmarkt **[Vermutung, 08]**. | Keine Tagessimulation der Gruppe: Markt 1 läuft tagesgenau, Märkte 2/3 als Monatsaggregate, die KG nach Kundenklassen plus 12 benannten Kunden, die Abfüllung als Monatsmodell ⟨Entscheidung: Simulationstiefe⟩. Der MVP läuft auf Golden-Master-Daten statt auf einer Live-Engine; veröffentlicht wird kapitelweise. |
| **Abstrakterer B2B-Einstieg** | Kein Kassentag; Leergutkonten und Gastroverträge sind Domänenwissen **[wahrscheinlich, 08]**. | Kapitel 1 spielt komplett im Markt 1 (Kasse, Kasten, Pfandbon). Der Großhandel kommt über Figuren und benannte Kunden (Brauhaus, Eckkneipe). Der MVP enthält trotzdem zwei Großhandels-Vorgänge, um die riskanteste Annahme früh zu testen. |
| **Prüfungsbedingungen weichen ab** | Die Klausur läuft auf Papier mit Taschenrechner und ohne vorgegebene Tabellen; Lückentabellen verraten das Lösungsschema **[wahrscheinlich]**. | Fading-Stufe 5 „leeres Blatt“ mit Rechenweg-Pflicht, Probeklausuren als PDF zum Ausdrucken, Zeitdruck nur im Prüfungsmodus. |
| **Buchhalter- statt Controllertraining** | Belegarbeit kann die Spielzeit dominieren (06 #13). | Die Buchhaltung (2,5 VZÄ) bucht, der Controller prüft, stimmt ab, plausibilisiert und berät. Belegarbeit ≤ 20 % der Monatszeit, ab Kapitel 2 delegierbar an Lena. |
| **Der Controller führt kaum ein Team (HB6)** | **[wahrscheinlich, 08]** | Führung über die Assistenz Lena, drei Inventurteams und das Projektteam Abfüllung. |
| **Zahlenwelt unbelegt, Simulation kennt die „wahre Ursache“** | Keine öffentlichen GFGH-Betriebsvergleiche **[sicher, 07/08]**. | Spannen statt Punktwerte, „Annahme“-Kennzeichnung, Fachreview durch eine GFGH-Controllerin, ab Kapitel 2 mehrdeutige Fälle mit Begründungsbewertung. |
| **Wirksamkeit in kurzer Zeit nicht prüfbar** | Eine Mechanik über 6–9 Monate lässt sich in 3 Wochen Playtest nicht validieren. | Entwicklerwerkzeuge (simulierte Uhr, synthetische Lernende), eine Längsschnitt-Kohorte über ≥ 8 Wochen vor 1.0, ein Prä-/Posttest mit Dozenten-Items und freiwillige Meldung echter Prüfungsergebnisse. |

---

## 3. Zielgruppen und Lernversprechen

**Primär:** Teilnehmende eines Lehrgangs „Geprüfte/r Controller/in“, 6–12 Monate vor dem schriftlichen Teil, als Ergänzung zum Lehrgang. Bundesweit sind das nur ≈ 80–115 Prüflinge pro Jahr (2025: 82, davon 54 bestanden) **[wahrscheinlich, DIHK-Statistik in 05/06]** ⟨Entscheidung: Primäre Zielgruppe⟩. **Sekundär:** Junior-Controller und Quereinsteiger im Handel und Großhandel, Bilanzbuchhalter (Teilmengen HB1/HB3), Handelsfachwirte, für Kapitel 1–2 auch Azubis Groß- und Außenhandel. **Nicht Zielgruppe:** Freizeitspieler ohne Lernziel (06 #17).

| Nr. | Versprechen | Messung | Schwelle ⟨Entscheidung: Lernversprechen-Schwellen⟩ |
|---|---|---|---|
| L1 | Routine: Monatsabschluss eines Markts (6 Routinen), später der Gruppe (≈ 20 Routinen, davon 3–5 voll gespielt) | Zeit- und Fehlerprotokoll je AT | Markt ≤ 25 min, ≤ 1 Diagnosefehler; Gruppe ≤ 45 min |
| L2 | Behalten bis zum Prüfungstag | prognostizierte Abrufwahrscheinlichkeit R(T); unangekündigter Re-Test 30 Tage nach Kampagnenende | R(T) ≥ 0,90 für ≥ 85 % der Pflicht-Skills; Re-Test ≥ 80 % |
| L3 | Schriftlich HB1–HB3 | zwei Probeklausuren in Folge, neue Seeds, Zeitlimit, wahlweise auf Papier | ≥ 67 Punkte je HB |
| L4 | HB4 am echten Werkzeug | 240-Min.-Probe in Excel oder Calc | ≥ 67 Punkte, keine hartkodierten Zahlen in Formelzellen |
| L5 | Verbale Leistung („nennen, erläutern, beurteilen“) | Kurzfreitext-Items mit Rubrik, Abgleich mit Dozentenkorrektur | ≥ 70 % der Rubrikpunkte |
| L6 | HB5 strukturiert | Exposé, Gliederung, Rechenkern, Entscheidungsvorlage **zum eigenen Betrieb** | alle Pflichtkriterien; Mentor-Feedback eingeholt |
| L7 | HB6 präsentationsfähig | 15-Min.-Präsentation, 20 Fachgesprächsfragen | Zeit ± 1 min; ≥ 75 % tragfähige Antworten |
| L8 | Typische Fehler abgestellt | Fehlerlogbuch | keine Top-10-Misconception öfter als 1× in 30 Tagen |

Die Schwellen sind interne Maße. Sie werden über drei Wege kalibriert: einen Prä-/Posttest mit Dozenten-Items (Einstufung = Prätest), den Abgleich der Automatik mit einer blinden Dozentenkorrektur (Ziel ≥ 90 % Übereinstimmung der Teilpunkte) und freiwillig gemeldete Prüfungsergebnisse. **Nicht versprochen:** Bestehen, Gesprächskompetenz ohne menschliches Gegenüber, Ersatz der Projektarbeit.

---

## 4. Spielerrolle, Setting, Figuren

### 4.1 Rolle

Der Spieler ist Controller/in der Gruppe, eine Stabsstelle der Geschäftsführung (1,0 VZÄ, 75 T€). Das sind **23,7 % des Konzern-EBIT von 317,1 T€** **[sicher, Rechnung]**. Ein Zähler „Wertbeitrag Controlling“ summiert belegbare Effekte der Empfehlungen in € (aufgedeckte Fehler, vermiedene Verluste, Verhandlungserfolge) gegen die Stellenkosten ⟨Entscheidung: Wertbeitrag-Zähler⟩.

Der Spieler **empfiehlt**, Geschäftsführer Tobias **entscheidet** nach einer sichtbaren Regel: Erreicht die Vorlage ≥ 7 von 10 Rubrikpunkten und ist sein Vertrauen mindestens neutral, folgt er ihr. Sonst folgt er seiner bekannten Vorliebe (Wachstum, Hausmarke, „selbst machen“). Zufall wirkt nur in der Umwelt, etwa ob ein Drittkunde vertragstreu ist ⟨Entscheidung: Entscheidungsregel GF⟩.

### 4.2 Referenzbetrieb „Getränkegruppe“ (Standardpfad, Plan 2027)

| Einheit | Inhalt | Plan 2027 |
|---|---|---|
| {NAME} Getränke GmbH & Co. KG | GFGH und Zentrale: 600 Gastrokunden (60 A, 200 B, 340 C), 150 Wiederverkäufer, 25 Streckenkunden, 300 Objekte und 900 Haushalte, ≈ 180 Veranstaltungskunden; 11 Lkw, 4 Transporter; 5.000 m² Halle der Besitzgesellschaft; 49,0 VZÄ | Außenumsatz 17.583,6 T€ (08: 17.500,0 plus Hausmarken-Mehrumsatz 83,6). Segment-DB III laut 08, vor Hausmarken-Delta: Gastro 1.120,5 T€ (11,8 %), Wiederverkäufer 22,6 (0,8 %), Strecke 125,6 (5,0 %), Objekt/Heimdienst 37,2 (2,5 %), Feste 72,3 (7,2 %), Märkte intern −169,9 |
| {NAME} Getränkemärkte GmbH (EAV, Organschaft) | Markt 1 = korrigierter Referenzmarkt aus 02/06, **nur Laden** (G19); Markt 2, Markt 3 | Umsatz 4.500 T€; EBIT 15,9 / 3,1 / −14,8 T€ |
| Sparte Hausmarke (in der KG, seit 2026) | Limonade in Mehrweg-Glas, Lohnabfüller „Hollmann“ (60 km) | 708.000 Flaschen, Umsatz 392,6 T€, DB I 132,6 T€ (4.3) |
| **Konzern mit Hausmarke** | Konsolidierung light (EAV, Cash-Pool, Zwischengewinn) | Außenumsatz 22.083,6; EBITDA 762,3; **EBIT 317,1 (1,4 %)**; EBT 210,0; Ergebnis nach GewSt 158,1 T€ |
| Bank (Covenants [Annahme 08]) | EK-Quote ≥ 25 %, Nettoverschuldung/EBITDA ≤ 3,5, Kapitaldienstfähigkeit ≥ 1,2 | 01.01.: EK-Quote 28,2 % (Pfand saldiert 30,5 %), ND/EBITDA 2,97 · Plan 31.12.: 29,9 %, 2,77, KDF 1,99 |
| Leergut | Konten je Partner und Gebindeart in Stück | Pfand-Float Fremdgebinde 341,7 T€ (≈ 27,3 T€ Zins bei 8 %), Silvester-Überhang 30.000 Kästen = 79,0 T€; Hausmarken-Pool netto 89,4 T€ |

Übernommene Korrekturen aus 06/08: 304 Öffnungs- und 254 Liefertage (F1), Start Sa 02.01.2027 (F19), Diesel 2,00 €/l netto mit eingerechnetem Ende des Tankrabatts (G9), Fahrerdeckung 12,5 VZÄ CE (G3), DPO brutto/brutto (G14), eine Formel für die Kapitaldienstfähigkeit (G15), Zinsen auf Durchschnittssalden (G17), Markt 1 ohne Heimdienst und Festservice (G19), vollständige Prozesskosten der internen Logistik (G20). Pfandsätze sind brutto, die Bilanz netto, und es gilt das Bruttomodell (BFH I R 36/07 **[wahrscheinlich]**) ⟨Entscheidung: Pfand-Bilanzmodell⟩. Die Hausmarke ist als Delta auf das 08-Modell gerechnet: Die 94 Prüfungen aus 08 bleiben gültig, das Delta hat eigene Prüfungen. Rechtsstand eingefroren am 20.10.2026, alles danach ist als fiktive Fortschreibung markiert ⟨Entscheidung: Rechtsstand-Freeze⟩.

### 4.3 Hausmarke: Produktwahl und Datenblatt

**Produkt: Limonade** (Zitrone, Orange, Rhabarber; Mehrweg-Glas) ⟨Entscheidung: Hausmarke-Produkt⟩. Begründung:
1. Natürliches Mineralwasser muss am Quellort abgefüllt werden **[wahrscheinlich, Mineral- und Tafelwasser-VO]**. Ohne eigene Quelle wäre die eigene Anlage kein echter Make-or-Buy-Fall.
2. Mehrere Rohstoffe (Zucker, Grundstoff, Aroma, CO₂) erzeugen Preis-, Verbrauchs- und Mischungsabweichungen in prüfungstypischer Form.
3. Die Zuckersteuer liefert einen echten Target-Costing-Fall, weil eine Rezeptur unter 5 g/100 ml steuerfrei bliebe (Kabinettsbeschluss 14.10.2026: 26 ct/l bei 5–8 g, 32 ct/l ab 8 g Zucker je 100 ml **[wahrscheinlich, 07/08]**).
4. Die 0,33-l-Flasche passt in die Gastronomie; alkoholfrei ist auch eine Schulversion möglich.

Apfelschorle bleibt als Seed-Variante: Konzentrat 70 °Brix und Beistellung liefern Preis- und Verbrauchsabweichungen.

**Zuckersteuer-Konvention im Standardpfad:** Die Steuer steht nicht im Plan 2027. Im Spiel beschließt der Bundestag im März 2027, in Kraft ab 1.1.2028. Seeds variieren Termin und Höhe ⟨Entscheidung: Zuckersteuer-Konvention⟩. Startrezeptur 7,5 g/100 ml ⟨Entscheidung: Rezeptur Hausmarke⟩.

| je Kasten (Plan 2027) | H33 24 × 0,33 l | H50 20 × 0,5 l | H100 12 × 1,0 l |
|---|---|---|---|
| Kanal 2027 (nur KG-Kanäle) | Gastro | Heimdienst/Objekt | Wiederverkäufer 10.000 · Heimdienst/Objekt 6.000 |
| Kästen | 14.000 | 9.000 | 16.000 |
| Erlös netto | 12,90 | 10,40 | 7,40 (7,14 / 7,83) |
| Rohstoff 0,19 €/l (Zucker 75 g/l × 0,80 €/kg + Grundstoff 0,13 €/l) | 1,50 | 1,90 | 2,28 |
| Verschluss und Etikett (Beistellung, 0,03 €/Fl) | 0,72 | 0,60 | 0,36 |
| **Lohnabfüllung** (0,19 / 0,21 / 0,25 €/Fl inkl. Wasser, CO₂, Waschen, Füllen, Etikettieren) | 4,56 | 4,20 | 3,00 |
| Leergut-Ersatz (3 % Flaschen, 1 % Kästen) | 0,24 | 0,23 | 0,19 |
| Fracht (Rückfracht Sattelzug) | 0,15 | 0,15 | 0,15 |
| **Einstand** | **7,18** | **7,08** | **5,98** |
| **DB I** (Quote) | 5,72 (44,4 %) | 3,32 (31,9 %) | 1,42 (19,1 %) |
| verdrängte Fremdware, RE II inkl. 3 % Nachvergütung, gleicher Kanal | 5,05 | 3,43 | 2,03 |
| Pfand brutto (0,15 €/Fl + 1,50 €/Kasten) | 5,10 | 4,50 | 3,30 |
| Zuckersteuer bei 26 ct/l (ab 2028) | 2,06 | 2,60 | 3,12 |

Kastenwerte sind auf Cent gerundet, Einstand und DB aus ungerundeten Werten (H33: 7,178 €); im Spiel zeigen Belege die Rechenbasis mit drei Nachkommastellen (Anzeigeregel, Abschn. 9).

**Summen 2027:** 708.000 Flaschen, 392.880 l, Umsatz 392,6 T€, DB I 132,6 T€ (33,8 %), Lohnabfüllung 149,6 T€. Leergut-Pool aus 186.250 Flaschen und 10.729 Individualkästen = 107,9 T€, als Festwert (§ 240 Abs. 3 HGB **[wahrscheinlich]**). Davon decken Kundenpfänder für die Hälfte im Umlauf netto 18,5 T€; die Nettobindung beträgt 89,4 T€, das sind 7,2 T€ Zins. Die Bilanzierung eigener Gebinde als Inverkehrbringer (BFH I R 33/11) muss eine WP prüfen **[Vermutung]** ⟨Entscheidung: Pfand eigener Gebinde⟩.

**Entscheidungswert statt Produkt-DB.** Annahmen ⟨Entscheidung: Hausmarken-Parameter⟩: 70 % der Hausmarken-Kästen verdrängen Fremdware, 37 T€ Markenfixkosten (Labor 12, Listung und Marketing 25), für Individualleergut keine Sortiervergütung (−2,5 T€).
- **Kurzfristig** (Kapazitäten fix): ΔEBIT −1,3 T€, nach Pool-Zins **ΔEBT −8,5 T€**.
- **Langfristig**, mit Prozesskosten der 11.700 Mehrkästen (Lager 0,30 + Kommissionierung 0,32 + Leergut brutto 0,45 €): **ΔEBT −20,4 T€** **[sicher, Rechnung]**.
- Die Hausmarke trägt sich erst, wenn die Füllkosten um ≈ 14 % sinken oder der Gastro-Anteil wächst. Sie verdient nur dort: H33 schlägt die Fremdware um 0,67 €/Kasten, H100 liegt 0,61 € darunter.
- Die Zuckersteuer bei der Startrezeptur kostet ≈ 102 T€ im Jahr (Menge 2027) gegen 132,6 T€ DB I. Genau das ist der Target-Costing-Anlass in Kapitel 2.
- Die **Listung in den eigenen Märkten** ist eine Weiche in Kapitel 1 ⟨Entscheidung: Hausmarken-Listung Märkte⟩. Bei VK 8,99 € brutto verdient Markt 1 an H100 1,39 €/Kasten (18,4 %), an der Fremdmarke bei 9,49 € aber 1,83 € (22,9 %). Auch die Gruppe verdient an H100 weniger (1,57 gegen 2,19 € inkl. Nachvergütung). Bei H50 (VK 11,99 € gegen 13,99 €) ist es umgekehrt: Der Markt verdient an der Hausmarke mehr (2,78 gegen 2,69 €), die Gruppe weniger (2,99 gegen 3,22 €). Markt- und Gruppensicht widersprechen sich also in beide Richtungen.

### 4.4 Figuren

**Gesprächsfiguren** haben Dialogbaum, Vertrauen und Gedächtnis. **Korrespondenzfiguren** treten nur über Dokumente, E-Mails und ein Verhandlungs-Minispiel auf. Das begrenzt den Erzählaufwand ⟨Entscheidung: Figurenbudget⟩. Namen sind Arbeitsnamen; Firma und Familie bleiben `{NAME}` ⟨Entscheidung: Firmen- und Figurennamen⟩.

| Figur | Rolle | Konflikt | Lernfunktion |
|---|---|---|---|
| Tobias {NAME} (44) | GF, Kommanditist, 2. Generation | Hausmarke ist sein Projekt, will „selbst machen“ | Adressat aller Vorlagen (HB5), entscheidet |
| Hildegard {NAME} (69) | Seniorchefin, Beirat; führte Markt 1 bis 2019 | „Der Markt hat 50 T€ verdient“ | Leitfrage K1, Beiratspräsentation, Einwände (HB3/HB6) |
| Sabine Kowalski | Marktleiterin Markt 1 (06 F18) | Prämie auf Markt-Rohertrag | Aktionen, Business Partnering |
| Holger Timmermann | Logistikleiter | will Touren straffen, Fahrermangel | Prozesskosten, sprungfixe Kosten, Budget-Slack |
| Kemal Yıldız | Gastro-Außendienst | Umsatzprämie, vergibt gern Darlehen | Kunden-DB, Kreditrisiko, Anreize |
| Derya Aksoy | GF Märkte GmbH | kämpft gegen „Einstand + 3 %“ | Profit-Center, Verrechnungspreis |
| Lena Brockmann | Assistenz Controlling ab K2 | lernt, macht typische Fehler | Delegation, Stichprobe, Feedback (HB6) |
| Katrin Vogt | Hausbank | Covenants | HB3, Bankgespräch als Fachgesprächsübung |
| *Korrespondenz:* Monika Hoff (Leitung Rechnungswesen), Dr. Frank Esser (Abschlussprüfer, „Citations“), Marc Lindemann (Brauerei Nordhang), Petra Hollmann (Lohnabfüller), Ulrich Kessler (Regionalbrauerei), Herr Pohl (Vorgänger, nur über den Übergabeordner) | | | Daten, Stichproben, Konditionen, Kalkulation, Drittauftrag, Worked Examples |

Die Worked Examples kommen diegetisch aus **Pohls Übergabeordner**. Wer ihn nutzt, löst die Aufgabe „mit Hilfe“; das zählt nicht für Mastery.

---

## 5. Spielschleifen auf allen Zeitskalen

**5.1 Minute: ein Vorgang (1–4 min).**
1. Vorgang öffnen: Absender, Frist, Anlagen, Stundenkosten. Das Regelbuch zeigt nur bereits eingeführte Prüfregeln.
2. Werkzeug wählen: Arbeitsblatt, Rechenweg-Editor, Datenraum-Suche oder Rückfrage (kostet Stunden).
3. Ergebnis eintragen und stempeln: Freigabe, Rückfrage, Korrektur veranlassen oder Eskalation. Davor den Sicherheitsregler setzen (50/70/90 %).
4. Feedback: bei Routinen sofort und diagnostisch, bei Entscheidungen später über die Zahlen. Danach Eintrag in Fallakte, Wertbeitrag und FSRS-Historie.

**5.2 Session (25–35 min).**
1. **Frühschicht** (≤ 8 Items, ≈ 5 min, auch am Smartphone).
2. 1–2 Schreibtischtage mit 3–5 **Fokusvorgängen** und kompakten Routinen.
3. Ein Gespräch oder 1–3 Entscheidungskarten (Ja / Nein / Prüfauftrag).
4. **Feierabend:** Bewertungsbogen, 2-Min.-Debrief, Ausblick auf Fristen, automatische Sicherung.

**5.3 Spielmonat (K1: 1 Session, ab K2: 2 Sessions).**

| Termin | Routinen (Beispiel Kapitel 2) |
|---|---|
| AT1 | Belegvollständigkeit, Leergut-Lieferscheine der Fahrer gegen Lagerzählung, Kassen der Märkte |
| AT2 | Leergutkonten Lieferanten und Kunden in Stück je Gebindeart, Kreditoren |
| AT3 | Abgrenzung Boni/WKZ/Kundenboni/Urlaub, Nachbelastungen, Bestandsplausibilität |
| AT4 | Kostenstellen Soll-Ist (Fuhrpark je Fahrzeug), Segment- und Kunden-DB, Abweichungen |
| AT5 | Monatsbericht und Monatsgespräch mit der GF |
| montags · 10./15. | 13-Wochen-Liquidität · Steuer- und Lohntermine, Bonus-Tracking, hl-Meldung |

- **Stundenbudget:** 160 Controllerstunden je Spielmonat ⟨Entscheidung: Stundenbudget⟩. Unbeherrschte Routinen kosten mehr Stunden als beherrschte. Delegation an Lena spart Stunden, bringt aber ein Stichprobenrisiko. Prüfaufträge (4–16 h), Analysen und Projektarbeit konkurrieren um den Rest. Reichen die Stunden nicht, fallen Karten auf die Standardoption und die GF entscheidet ohne Analyse. Das ersetzt den Timer und übt Selbstorganisation (HB6).
- **Routine-Kompression:** Voll gespielt werden je Monat 3–5 Vorgänge, die der Scheduler nach fälligen Skills und neuen Regeln wählt. Beherrschte Routinen laufen als 1-Klick-Plausibilitätscheck oder delegiert ⟨Entscheidung: Routine-Kompression⟩.
- **Monatsgate (einziges Gate auf Monatsebene):** Der Monat schließt erst, wenn die Pflichtvorgänge mit ≥ 50 % der Punkte bearbeitet sind. Nicht bestandene Vorgänge kommen mit neuen Zahlen zurück ⟨Entscheidung: Monatsgate⟩.

**5.4 Spieljahr.**
- Januar: Inventur an vier Standorten, Saldenbestätigungen, Bonusabrechnung, Weitergabe der Preisrunde.
- Februar bis April: Jahresabschluss der prüfungspflichtigen KG, Konzernrechnung für die Bank, Bankgespräch, Risikoinventur, Jahresgespräche mit Brauereien.
- Mai bis August: Saison mit Wetter-Disposition, Festen, Fahrer- und Leergutengpässen.
- September: Strategieklausur.
- Oktober/November: Budget im Gegenstrom mit den Kostenstellenleitern, Preisrunde.
- Dezember: Bonus-Endspurt, Vorkauf, Silvester-Leergut.
- Quartalsweise: Forecast, Covenant-Zertifikat, Stichprobe von Dr. Esser aus *eigenen* Vormonaten, 45-Min.-Zwischenprüfung über alle HB.
- Seltene Jahresroutinen bekommen Mini-Zyklen: Übungsabschlüsse aus der „Archivakte“ (Markt 2/3, Vorjahre).

**5.5 Kampagne (36 Spielmonate)** ⟨Entscheidung: Kampagnenlänge⟩

| Kapitel | Zeit | Leitfrage | Schwerpunkt | Neue Werkzeuge | Kapitelabschluss |
|---|---|---|---|---|---|
| 1 Pilotmarkt | Jan.–Apr. 2027 | Hildegard: „Früher hat Markt 1 50 T€ verdient, jetzt 15,9. Was habt ihr kaputt gemacht?“ | Abgrenzung, Kostenarten, Handelskalkulation, Pfand, Markt-KER, Aktion | Mengenlupe, Netto-Brille, Kalkulationsschieber | Überleitungsvorlage (7.2) und Kapitelprüfung |
| 2 Großhandel | Mai 2027–Apr. 2028 | Tobias: „Welche Kunden und Touren tragen uns, und trägt meine Limo?“ | Leergutkonten, Konditionen, Prozesskosten, Kunden-DB, Touren, Darlehen, Forderungen, Zuckersteuer, erster eigener Jahresabschluss | DB-Spalten, Prozesskosten-Etikett, Staffel-Radar, Zahlungskalender; Delegation | Kundenportfolio-Vorlage, Jahresabschlussanalyse, Kapitelprüfung |
| 3 Gruppe mit Projekt „Abfüllung“ | Mai 2028–Dez. 2029 | Vogt und Aksoy: „Steuert ihr richtig, und bleibt die Bank dabei?“ · Tobias: „Füllen wir selbst ab?“ | Spartenrechnung, Verrechnungspreise, Budget mit 4 Verantwortlichen, Covenants, Konsolidierung light; Make-or-Buy Mai–Nov. 2028, Folgen 2029 | VP-Regler, Covenant-Tacho, Treiberbaum, Maschinenstunden-Uhr | Beiratsvorlage Abfüllung, Jahresprüfung |
| Epilog (optional) | 2030 | Übernahmeangebot eines Konzern-GFGH | Bewertung (M56), Fachgespräch | – | „Zeugnis“ |

- **Drei große Weichen:** Aktionspolitik und Hausmarken-Listung in K1, Gastro-Liefer- und Darlehenspolitik in K2, Make or Buy in K3. Alles Weitere läuft über Zustandsvariablen; die Handlung läuft wieder zusammen.
- **Kein Game Over:** Ein Covenant-Bruch startet den **Krisenmodus** mit 13-Wochen-Plan, Bank-Workout und StaRUG-Frühwarnung ⟨Entscheidung: Krisenmodus⟩.
- **Kapitelgate (einziges Gate auf Kapitelebene):** Die Kapitelprüfung (45 Min., ≥ 50 Punkte) wird erst frei, wenn die Kern-Skills des Kapitels „gelernt“ sind; das braucht ≥ 2 Kalendertage. Wer durchfällt, spielt nicht neu, sondern bekommt im nächsten Kapitel gezielte **Nachprüfungsfälle** ⟨Entscheidung: Kapitelgate und Nichtbestehen⟩.
- **Lehrgangsmodus:** Kapitel ordnen nur Setting und Routinen. Lehrt der Lehrgang HB3 früh, zieht die Fallmaschine Sonderaufträge vor, etwa „Bank will eine Analyse des Jahresabschlusses 2026“ schon in Kapitel 1 ⟨Entscheidung: Lehrgangsmodus⟩.

**5.6 Die ersten 20 Minuten (FTUE).**

| Minute | Inhalt |
|---|---|
| 0–1 | Mo 04.01.2027, 7:45 Uhr. Tobias begrüßt den Spieler in zwei Sätzen; auf dem Tisch liegt Pohls Ordner. |
| 1–3 | Hildegard ruft an und stellt die Leitfrage; das Kapitelziel ist sichtbar. |
| 3–4 | Einstufung: drei Aufgaben oder „Ich kenne mich aus“ (springt auf Fading-Stufe 3). |
| 4–10 | Vorgang 1 als Worked Example aus dem Ordner: Leergut-Rückgabe Markt → KG. Lieferschein 612 Bierkästen, Nebenbuch 640, die Differenz von 28 × 2,61 € beträgt 73,08 €. Regel R1 „Erst Stück, dann Euro“, Stempel „Rückfrage KG-Lager“, eine Selbsterklärungsfrage. |
| 10–16 | Vorgang 2 (Fading 2): Tobias will die Hausmarke 1,0 l in Markt 1 listen. Was bliebe dem Markt bei 8,99 €? Ergebnis 1,39 € (18,4 %) gegen 1,83 € bei der Fremdmarke. Der Teaser zur Hausmarkenweiche. |
| 16–18 | Die **Mengenlupe** wird bis morgen leihweise freigeschaltet (dauerhaft, sobald der Skill „gelernt“ ist). |
| 18–20 | Feierabend-Debrief in 90 Sekunden. Ausblick: „Morgen 3 Items Frühschicht. Dr. Esser kündigt für April eine Stichprobe aus deinen Vorgängen des ersten Quartals an.“ |

**5.7 Binge-Spiel, Pausen.**
- Beliebig viele Spielmonate pro Tag sind möglich, aber je Skill zählt nur ein Abruf pro Kalendertag (06 W10). Ist das Kapitelgate noch nicht offen, bietet das Spiel Wartebeschäftigung an: Archivakte, Excel-Werkstatt, Probeklausur, Theorie-Dossier. Die UI sagt ehrlich: „Dein Gedächtnis braucht eine Nacht.“
- Nach Pausen verteilt der **Rückkehrmodus** den Rückstau auf höchstens 10 Items pro Tag.
- Der **Urlaubsschein** schützt die Serie 2 Tage pro Woche. Die Serie zählt nur erfolgreiche Wiederholungen, Ligen gibt es keine ⟨Entscheidung: Serie und Urlaubsschein⟩.

---

## 6. Lernsystem

### 6.1 Theorie (wie erklärt)

- **Theoriekarte**: ≤ 90 Wörter, Formel direkt an den Zahlen des eigenen Spielstands („Dein Markt 1, Januar: …“). Sie erscheint just in time, wenn eine Regel zum ersten Mal im Posteingang auftaucht, und endet immer mit einer Abrufaufgabe.
- **Worked Example** aus Pohls Ordner, kommentiert in 1–2 Sätzen je Schritt, mit einer Selbsterklärungsfrage.
- **Theorie-Dossier bzw. Skript-Lesepfad** (≤ 600 Wörter oder Verweis auf ein Skriptkapitel über `skript_map`): für Verfahrensvergleiche, die eine Karte nicht trägt, etwa starre, flexible und Grenzplankostenrechnung, Vor- und Nachteile der Prozesskostenrechnung oder Konsolidierungsmethoden. Danach folgen Abrufaufgaben: Vergleichstabelle ausfüllen und Kurzfreitext ⟨Entscheidung: Skript-Lesepfad⟩.
- **Productive Failure** („erst probieren“) nur bei Konzeptthemen: Gemeinkostenverteilung, Preisuntergrenze, Make-or-Buy, Verrechnungspreis.

### 6.2 Praxis (wie geübt)

- Jeder Vorgang ist eine **parametrisierte Vorlage** im Spielkontext; im Juni rechnet man mit dem Juni-Wareneinsatz des eigenen Markts. Die Aufgabe nennt die Methode nicht („Was bleibt uns bei 9,99?“).
- **Fading** je Skill in fünf Stufen: vorgemacht → letzter Schritt fehlt → zwei Schritte fehlen → leeres Formular → **leeres Blatt mit Rechenweg-Pflicht** (Prüfungsbedingung). Der Wechsel ist adaptiv; Kundige überspringen per Einstufung.
- **Interleaving** nach dem Ersterwerb, dazu gezielte **Kontrastpaare**: Liter- gegen Maschinenzeit-Bezugsbasis, Pfand brutto gegen netto, Prozesskostensatz gegen kurzfristig abbaubare Kosten.
- Jedes Lernziel erscheint in **≥ 3 Oberflächen**: Einzelrechnung, Tabellenzeile, Fehlersuche („Finde den Fehler in Lenas Rechnung“), Begründung bzw. Kurzfreitext.
- **Transferfälle** (10–15 %) laufen als „Mandat eines Verbundkollegen“ in fremden Betrieben.

### 6.3 Wiederholung: Pflichtmechanik und Algorithmus

1. **Einheit ist der Skill** (z. B. `sk.kalk.mss`). Jeder Skill ist eine ts-fsrs-Karte (FSRS v6, Zeit in Kalendertagen). Zielretention 0,90 für den Pflichtkanon, 0,85 für Ausblick-Skills.
2. **Rating aus dem Ergebnis:**
   - falsch oder Lösung angezeigt → Again
   - richtig mit Konzepthinweis oder im 2. Versuch → Hard (zählt nicht für Mastery)
   - richtig im 1. Versuch → Good
   - richtig und schneller als der eigene Median → Easy

   Worked Example oder Pohls Ordner zählen als Again ⟨Entscheidung: Hilfe-Rating⟩.
3. **Credit Assignment bei Mehrschrittaufgaben:**
   - Jede Teilaufgabe ist 1–2 Skills zugeordnet.
   - Der Skill des fehlerhaften Schritts bekommt Again.
   - Ein Folgeschritt, der mit dem eigenen falschen Vorwert richtig gerechnet ist, bekommt Good für seinen Skill.
   - Nicht bearbeitete Schritte erzeugen kein Rating.
4. **Zählregel:** Je Skill zählt ein Abruf pro Kalendertag, egal ob in Frühschicht, Routine oder Fall ⟨Entscheidung: Zählregel⟩.
5. **Tagesqueue:**
   - Kandidaten sind die laut FSRS fälligen Skills (R ≤ Zielretention) sowie Taper-Skills.
   - **Priorität** p = g_HB × g_LZ × (1 − R) × (1 + 0,5 × Misconception-Flag) × (1 + 0,3 × Lehrgangsbezug) **[Vermutung, per Playtest kalibrieren]**.
   - g_HB richtet sich nach der Prüfungsdauer; g_LZ nach der Relevanz (hoch 1,0 / mittel 0,6 / niedrig 0,3).
   - Der Lehrgangsbezug ist 1, wenn das Skriptkapitel laut Lehrgangsfahrplan in den letzten 14 Tagen behandelt wurde.
6. **Pflicht ohne zweites Gate:**
   - Die Frühschicht nimmt höchstens 8 Items und mischt mindestens 3 HB. Nie stehen zwei Items derselben Vorlage hintereinander, bei Misconception-Flag kommt ein Kontrastpaar.
   - Was die Frühschicht nicht schafft, bettet der Scheduler als Teilaufgaben in die Pflichtvorgänge des Monats ein. So erzwingt das Monatsgate die Wiederholung ⟨Entscheidung: Frühschicht-Pflicht⟩.
   - Den Lastdeckel bilden Pflicht ≤ 30 % der Sessionzeit; darüber führt der Scheduler weniger neue Skills ein.
7. **Countdown und Tapering:** Mit eingegebenem Prüfungstermin T bekommen alle Pflicht-Skills mit prognostiziertem R(T) < 0,90 im Fenster [T−21; T−3] einen Zusatzabruf. Probeklausuren nehmen dann zu ⟨Entscheidung: Prüfungstermin-Countdown⟩.
8. **Rost als UI:**
   - Die Rost-Anzeige ist eine Sicht auf die FSRS-Abrufwahrscheinlichkeit R.
   - Bei R < 0,70 **beschlägt** das zugehörige Werkzeug und zeigt nur noch die Richtung („DB II: negativ“), keine Zahl.
   - Der Arbeitsschritt bleibt von Hand machbar und ist selbst ein Abruf. Es gibt keine Sperre ⟨Entscheidung: Rost-Konsequenz⟩.
9. **Kalibrierung:** Die ts-fsrs-Standardparameter sind für Faktenkarten kalibriert, nicht für Prozeduren **[wahrscheinlich]**. Ab ≥ 1.000 Reviews optimiert der FSRS-Optimierer die Parameter, bis dahin gilt die Zielretention als Stellschraube.

### 6.4 Mastery

| Stufe | Kriterium | Wirkung |
|---|---|---|
| gelernt | 3 unassistierte richtige Lösungen mit verschiedenen Parametern an ≥ 2 Kalendertagen, davon 1 in zweiter Oberfläche (03) | schaltet das Werkzeug frei; Voraussetzung fürs Kapitelgate |
| beherrscht | FSRS-Stabilität ≥ 21 Tage und ≥ 2 richtige Anwendungen im Spielkontext (04) | Effektvorschau, Delegierbarkeit, Routine-Kompression |
| prüfungsfest | ≥ 67 % der Punkte auf diesem Lernziel in einer Probe unter Zeitlimit, nicht älter als 30 Tage | zählt fürs „Zeugnis“ |

Der Status eines Lernziels ist der schwächste Status seiner Skills ⟨Entscheidung: Mastery-Stufen⟩.

### 6.5 Feedback und Debriefing

Vier Schichten:
1. **Sofort:** Diagnose aus Fehlerfunktionen.
2. **Nach dem Vorgang:** Bewertungsbogen wie bei einer korrigierten Klausur (Punkte je Teilaufgabe, Prüferkommentar, Lösungsskizze).
3. **Monatlich:** 3–5-Min.-Debrief mit drei auffälligen Zahlen (vorher Vorhersage), Treiberbaum, **Kontrafaktum** und Lehrsatz fürs Notizbuch.
4. **Verzögert:** Citations von Dr. Esser aus eigenen Vormonaten.

Das Kontrafaktum ist ein Replay mit genau einer geänderten Entscheidung. Common Random Numbers verhindern dabei Drift (06 W12). Im MVP ohne Live-Engine gibt es nur eine vorgerechnete Alternative. Das Jahresdebrief trennt Entscheidungsqualität vom Ergebnis.

### 6.6 Umgang mit Fehlern

- Jeder Fehler wird ein Fall in der **Fallakte** (z. B. „Jan. 2028: Rügefrist Leergut versäumt, 261 €“) und kehrt nach 2–7 Tagen mit neuen Zahlen zurück.
- Nach dem zweiten Fehler kommt ein **Corrective in anderer Darstellung**, etwa Leergut als Palettenbild statt Tabelle.
- Wer bei 90 % Sicherheit falsch lag, bekommt eine betonte Erklärung (Hypercorrection).
- Folgen sind spürbar, aber reparierbar: Korrekturbuchung, Vertrauensdelle, Citation, Krisenmodus.

---

## 7. Inhaltsabdeckung

### 7.1 Lernziel-Architektur (Andockpunkt für die Lehrgangsskripte)

```
HB (ContrPrV § 3, fest) ─n:m─ Lernziel lz:k7q2 (opak, unveränderlich) ─n:m─ Skill sk.kalk.mss ─n:m─ Vorlage tp.abf.planbab ─1:n─ Oberflächen
lernziele.yaml  { id: lz:k7q2, hb: [1], themenfeld: "Kalkulation", text, bloom: anwenden, relevanz: hoch,
                  pruefungsform: schriftlich, herkunft: [M06, M07], skills: [sk.kalk.mss, sk.kalk.bab-stufen], status: vorlaeufig }
skript_map.yaml { lz: lz:k7q2, quelle: "Skript HB1 Teil 2", kapitel: "4.3", seiten: "112-118", gewicht: 1.0, termin: 2027-03-14 }
```

- Die **Spielmechanik kennt nur Skills**; Vorlagen und Routinen referenzieren Skills, nie Lernziele. Ein Skript anzuhängen heißt, `skript_map.yaml` zu füllen. Das ist eine reine Datenänderung.
- **Teilen die Skripte ein Lernziel anders**, entstehen neue Lernziel-IDs, die alten bleiben als `ersetzt_durch` ladbar. Die Skills und damit die FSRS-Historie bleiben unverändert.
- Modulnummern aus 01/06 stehen nur als Herkunft im Datensatz, nie in der ID ⟨Entscheidung: Lernziel-ID-Schema⟩.
- Ein **CI-Abdeckungsbericht** prüft drei Richtungen: Lernziel ohne Skriptkapitel, Skriptkapitel ohne Lernziel, Lernziel ohne Inhalt.
- **Pflicht je Lernziel:** ≥ 1 Theoriekarte oder Lesepfad, ≥ 3 Oberflächen aus ≥ 2 Vorlagen, ≥ 1 Routine- oder Fallkontext, ≥ 1 Item im Prüfungsformat, bei den Operatoren „erläutern“ und „beurteilen“ ≥ 1 Kurzfreitext. Fehlt etwas, ist das Content-Arbeit, keine Designänderung.
- Der vorläufige Katalog (≈ 150 Lernziele) wird jetzt aus dem Wortlaut von § 4 ContrPrV und M01–M56 abgeleitet ⟨Entscheidung: Lernziel-Katalog jetzt oder später⟩.

### 7.2 Abdeckungstabelle

Bereich: **PM** Pilotmarkt (K1) · **GH** Großhandel (K2) · **GR** Gruppe (K3) · **AB** Abfüllprojekt (K3) · **TR** Transfer.

| HB | Bereich | Module | Übung mit Zahlen der Getränkegruppe | Aufgabentyp |
|---|---|---|---|---|
| 1 | PM | M04, M05 | Überleitung Markt 1 von EBIT 50,5 auf 15,9 T€: Heimdienst/Fest in die KG −139,1; Nachvergütungen bleiben in der KG −46,7; Inventurdifferenz +1,8; Einkaufsvorteil 6 % +94,4; VP-Aufschlag 3 % −44,4; Personal +51,1 (Inhaber und Büro raus, angestellte Leitung, +0,5 VZÄ); Sachkosten +74,8; Umlage −32,2; AfA +5,7 | Überleitungstabelle mit Folgefehler, Erläutern |
| 1 | PM | M07, M15 | L01: Liste 14,20 → Rechnung 12,40 → netto-netto 11,78 €; Gruppen-Einstand 11,656 €, VP 12,006 €; VK 17,49 € brutto = 14,697 € netto → Markt-db 2,69 € (18,3 %), Konzern-db 3,04 € | Kalkulationsschema vorwärts/rückwärts |
| 1 | PM | M08, M02, M44 | Markt 1 Januar: AB 125,0 + Zugänge 102,1 − EB 128,0 = Wareneinsatz 99,1 T€; RE I 40,7 T€ (29,1 %); EBIT −8,3 T€ ist Saison, kein Schließungsgrund | KER-Lückentabelle, Kurzfreitext an die GF |
| 1 | PM | M09, M45, M41 | Aktion L01 zu 9,99 €: Markt −352,3 €, Gruppe +31,6 € je Woche; Nachbelastung 1.184 € (Szene A) | Mehrschritt, Abgrenzung |
| 1 | PM/GH | M06, M12, M44 | KG-Kostenstellen → Sätze: Lagerung 0,30 €/Kolli, Kommissionierung 0,32, Leergut 0,45 brutto / 0,35 netto, Beschaffung 0,09; Tourtag 454,30 €; Gastro-Stopp 34,16 €; Mindestbestellwert 125 € | BAB-Lückentabelle (Stufenleiter) |
| 1 | GH | M09, M12, M14, M33 | Eckkneipe DB III −493 €, 14-tägig +395 €; Kündigung kostet kurzfristig 3,7 T€; Rhythmusprogramm 120 Kunden: 106,6 T€ „Ersparnis“, kurzfristig abbaubar 15,1 T€ (Abschn. 9) | Situationsaufgabe mit Fristigkeit |
| 1 | GH | M48, M31, M08 | Bonusstaffel Brauerei Nord: 1 % = 23.610 € statt 2 % = 47.600 €, weil die Klausel den Abverkauf zählt; Nachvergütungen 417,4 T€, 290 T€ aus 2026 offen (Szene B) | Hochrechnung, Klauselprüfung |
| 1 | GH | M13, M49 | Zuckersteuer H33: Allowable Costs 7,74 € (Zielpreis 12,90, Ziel-DB 40 %), Drifting Costs mit Steuer 9,24 € (Lücke 1,50 €), Rezeptur unter 5 g → 7,23 €. Zielkostenspaltung (5 Funktionen, 5 Komponenten): Zielkostenindex Lohnabfüllung 0,52 (zu teuer), Rezeptur 1,77 | Zielkostenspaltung, Zielkostenindex, Kontrolldiagramm |
| 1 | GH | M14, M09 | Hausmarke: DB I 132,6 T€ gegen ΔEBT −8,5 T€ (kurzfristig) bzw. −20,4 T€ (langfristig) | Entscheidungsrechnung mit Fristigkeit |
| 1 | GR | M41, M40, M51 | VP-Varianten Märkte: 96,7 / 4,1 / −232,2 / −447,9 T€, Gruppensumme stets −165,8 T€; Prämie von Sabine hängt am VP | Variantentabelle mit Invarianzprobe |
| 1 | GR | M14 | Markt 3 schließen: −17,9 T€ bei 50 % abbaubarer Logistik, +9,7 T€ bei 100 % | Entscheidung unter Unsicherheit |
| 1 | AB | M06, M07 | Plan-BAB mit 7 Stellen, Maschinenstundensatz 270,15 €/h (364,11 mit Bedienung); Bezugsgrößenkalkulation: Herstellkosten 0,171 / 0,202 / 0,300 €/Fl (Szene C) | Stufenleiter, Kalkulation |
| 1 | AB | M07, M15, M31 | Hollmann-Kalkulation 224,21 → 207,78 → 199,51 € je 1.000 Fl; Vorlage 2 (Lohnabfüller B, Zuschlagskalkulation): Forderung +16,0 %, berechtigt +6,5 % | Fehlersuche im Kalkulationsschema |
| 1 | AB | M14, M25 | Make 258,2 (mit Drittauftrag) bzw. 361,2 T€ gegen Buy +9 % 260,6 T€; kritische Menge allein für die Hausmarke 1,79 Mio. Fl | Entscheidungsvorlage |
| 1 | AB (Kauf) | M11, M06 | Juli 2029: Verbrauchsabweichung +2,50, Beschäftigungsabweichung +3,37 T€; Ist-BAB mit Normal-Maschinenstundensatz: Unterdeckung 2,07 T€ | Abweichungszerlegung, Normalkosten |
| 1 | GR/AB | M04 | kalkulatorische AfA 105 gegen bilanziell 95 T€ (Anderskosten), kalkulatorischer Zins 28,5 T€ (Zusatzkosten), Zinsdifferenz Wirt-Darlehen 6 % − 3 % | Abgrenzungstabelle |
| 1 | TR | M07, M08, M06, M12, M13 | Kuppelkalkulation, mehrstufige Divisionskalkulation, Kostenträgerzeitrechnung GKV/UKV mit Bestandsveränderung, Ist-/Normalkosten-BAB mit Über-/Unterdeckung, Gleichungsverfahren gegen Stufenleiter, lmi/lmn-Umlage, Lebenszykluskosten | Transferfall „Mandat eines Verbundkollegen“ |
| 2 | GH | M19, M46, M03 | Newsvendor L09 in Markt 1: μ 600, σ 120, C_u 2,15 €, C_o 0,11 € → CR 0,951 → Q ≈ 799 Kästen; Gedat-Trend −4 % Stopps; Diesel ±30 ct = ±33,4 T€ | Berechnen, MAPE/Bias |
| 2 | GH | M23, M49 | 13-Wochen-Plan Dez./Jan.: Silvester-Überhang 79,0 T€, Steuertermine; Kontokorrent Plan 566,1 gegen Ist 682,9 T€ (Szene B) | Tabelle mit Folgefehler, Überleitung |
| 2 | GH/GR | M25, M54 | Gastro-Darlehen 30 T€ (6 J., 3 % statt 6 %): Barwert des Zinsnachteils 2,71 T€; E-Sattelzug +10,2 T€/J. (07); Abfüllanlage (Szene C) | Kapitalwert, Annuität, Sensitivität |
| 2 | GR | M18, M51 | Budget Fuhrpark 747,2 T€: Timmermann plant +9 %, die Treiber ergeben +4 % → Slack ≈ 37 T€ | Gegenstrom, Moderation |
| 2 | GR | M16, M17, M37 | Segmentportfolio (Gastro 11,8 % DB III, Wiederverkäufer 0,8 %, Strecke 5,0 % an 25 Kunden), BSC für die Märkte, Risikomatrix Darlehensportfolio 1.200 T€ | Strukturieren, Kurzfreitext „beurteilen“ |
| 2 | GR | M50, M37, M23 | Covenants Plan 2027: 29,9 % / 2,77 / 1,99; pro forma Abfüllanlage 3,41 bzw. 3,85 (Bruch); Krisenmodus mit 13-Wochen-Plan | Szenariorechnung |
| 3 | PM–GR | M02, M44 | Pfand-Bruttomodell: EK-Quote 28,2 % brutto gegen 30,5 % saldiert; Leergutkonto in Stück; Palette als eigene Leistung mit 19 % | Buchen, Zuordnen |
| 3 | GH/GR | M22, M20 | DuPont-ROI 1,44 % × 2,98 = 4,27 %; EK-Rendite 7,6 %; Ø-FK-Zins 2,7 % gegen Grenzzins Kontokorrent 8 % (Leverage im Schnitt positiv, an der Grenze negativ); Anlagendeckung II 113,2 % (goldene Bilanzregel knapp erfüllt); Liquidität 2. Grades 85,8 % mit, 66,6 % ohne Pfand; DSO 25 / DPO 26 Tage brutto/brutto | Kennzahlenkette, beurteilen |
| 3 | GR | M23, M22 | Kapitalflussrechnung DRS 21 indirekt, Plan 2027: CF laufende Tätigkeit 603,4, Investitionen −405,0, Finanzierung −292,6 → Finanzmittelfonds −94,2 T€ | Tabelle |
| 3 | GR | M40 | Konsolidierung light: Innenumsatz 3.178,4; Schulden 145,1 / 150,0 / 66,0 / 4,1; Zwischengewinn 263,0 × 3/103 = 7,66 T€ | Konsolidierungsbuchung |
| 3 | GR | M49 | Gewerbesteuer im Organkreis: Sondervergütung GF +19,6 T€; Hinzurechnung | Mehrschritt |
| 3 | GH | M24, M37 | Insolvenz Bistro Mühlentor: 28,6 T€, Forderung mit USt-Berichtigung nach § 17 UStG (Szene B) | Mehrschritt, Buchung |
| 3 | TR | M22 | IFRS-Grundzüge (Leasing IFRS 16 gegen HGB), Kapitalflussrechnung direkt | Transferfall |
| 4 | alle | M26, M27 | Monatsbericht Markt 1, Segmentbericht mit Wasserfall, Kommentar nach „Was – Warum – Was tun – Wer bis wann“ | Kurzfreitext, Diagrammaufgabe |
| 4 | alle | M28 | Excel-Werkstatt: Pivot der 600 Gastrokunden, XVERWEIS auf Prozesssätze, Mindestbestellwert per Zielwertsuche (125 €), VP-Modell mit Prüfsumme −165,8 | xlsx-Abgabe |
| 4 | PM/GH | M29, M38, M53 | Stammdatenfehler „Flasche statt Kasten“, Fahrer- gegen Lagerzählung Leergut, Warenkorb Markt 1 (Lift 1,5) | Datenraum-Fall |
| 4 | GH/GR | M35, M36 | E-Rechnungspflicht für alle KG-Rechnungen ab 1.1.2027, nicht für die Bons der Märkte; ERP-Ablösung als TCO und Projekt | TCO-Tabelle, Earned Value |
| 5 | GR | M42, M36, M56 | Projektwerkstatt (30 Tage): Themen aus dem eigenen Run, Pflicht-Transferpfad auf den eigenen Betrieb | Struktur- und Rubrikprüfung |
| 6 | GH/GR | M43, M55, M51, M01 | Budgetrunde moderieren, Konfliktgespräch Timmermann ↔ Yıldız (Glasl), Lena führen, Inventur an 4 Standorten, Beiratspräsentation, Fachgespräch | Dialog, Kurzfreitext, Selbstaufnahme |

### 7.3 Was auch die Gruppe nur schwach abdeckt

- **M21 wertorientierte Steuerung:** Es gibt keinen Kapitalmarkt; WACC bleibt Annahme, nur Capital Employed je Segment ist echt.
- **M40 international:** IFRS, Minderheiten, Equity-Methode und Währung fehlen; konsolidiert wird nur nach HGB light, freiwillig für die Bank.
- **M39 CSRD:** nur VSME-Anfragen.
- **M55 Teamführung:** Der Controller führt allenfalls eine Assistenz.
- **Industrie-KLR jenseits einer einstufigen Linie:** Kuppelprodukte und mehrstufige Fertigung fehlen; Bestandsveränderungen gibt es nur im Kauf-Zweig.
- **M45, M53, M46:** Aktionen, Warenkorb und Endkunden-Wetter gibt es nur in den Märkten.
- **Systeme:** ERP und BI sind keine echten Systeme.
- **Prüfungsteile:** die echte Projektarbeit und das reale Gegenüber im Fachgespräch.
- **Gegenmittel:** Pflicht-Transferfälle (10–15 % der Fälle in HB1, 5–10 % in HB3), der Lesepfad und die Peer-Formate in HB6.

---

## 8. Branchenspezifische Mechaniken

| Mechanik | Spielregel und Zahlen | trainiert |
|---|---|---|
| **Vollgut-/Leergutkonten, Pfand** | Konten je Partner und Gebindeart **in Stück**; monatlich Lieferantenauszug gegen Nebenbuch, Fahrer- gegen Lagerzählung, Rügefrist 5 Werktage. ≈ 3,12 Mio. € Pfand pro Jahr (08); Leergut- und Palettendifferenzen 48,5 T€; Fasspfand 30 € brutto = 25,21 € netto. In Belegen werden Pfand-Nettowerte je Gebinde auf Cent gerundet (2,61 / 2,77 €) | M02, M44, M38, M22 (Bilanzausweis), M24 |
| **Pfand-Float, Silvester** | Float Fremdgebinde 341,7 T€ über den Kontokorrent; Silvester-Überhang 30.000 Kästen = 79,0 T€ als Stichtagseffekt (G13) | M23, M24, M22 (Bilanzpolitik) |
| **Wetter-Forecast** | 7-Tage-Prognose mit Fehlerband, das Ist kommt später; Hitzewelle ≈ einmal je Saison gezogen (06 E10); Bestellung nach Newsvendor (Q ≈ 799) | M46, M19, M30 |
| **Aktionen (Märkte)** | Aktions-EK nur gegen Abverkaufsnachweis; Restmengen werden nachbelastet; das WKZ fließt der KG zu, nicht dem Markt | M45, M15, M41, M51 |
| **Konditionen, Boni, Vorkauf** | Staffeln mit Klippe und Klausel zur Bezugsbasis; Preisrunde mit Vorkaufsoption; hl-Meldungen; 290 T€ offene Nachvergütungen aus 2026 | M48, M31, M08, M22 |
| **Gastro-Darlehen, Leihinventar** | 1.200 T€ bei ≈ 80 Wirten zu 3 %, Neuvergabe 300 T€ pro Jahr; Leihinventar 900 T€. Insolvenzkaskade aus Forderung (§ 17 UStG), Darlehen, Inventar (20–40 % verwertbar) und Leergut. Frühwarnung über Rücklastschrift und wachsenden Leergutsaldo; Bezugsbindung 10 J. (BGH) gegen 5 J. Gruppenfreistellung | M25 (Darlehen als Investition), M33, M37, M24 |
| **Touren, Fuhrpark** | 15 Fahrzeuge, 747,2 T€; Tourtag 454,30 €, davon variabel (Diesel, Maut) nur 82,19 €; Auslastung 94,8 %, Leerkosten 29,3 T€; E-Sattelzug mautfrei bis 30.6.2031 **[sicher, 07]** | M05 (sprungfix), M12, M14, M25, M39 |
| **Lager** | Sätze je Kolli und Kasten; Märkte-Lieferungen gewichtet; interne Logistik 328,8 T€ = 7,3 % des Märkteumsatzes; Stellplätze als Engpass im Silvester-Peak | M06, M32, M41 |
| **Saison** | Märkte Januar bis April negativ, Bestandsaufbau im Mai, Feste Mai bis September, Kontokorrent-Spitze im Dezember | M03, M18, M23 |
| **Ereignisse** | Gastro-Insolvenz, Preisrunde, Fahrermangel, LEH zieht Strecke ab, Kistenknappheit, Brauerei-Insolvenz, Zuckersteuer. Ein **Ereignisbudget** je Quartal und ein Schwierigkeitsband verhindern Seed-Häufungen, z. B. höchstens eine Gastro-Insolvenz im ersten Großhandelsjahr ⟨Entscheidung: Ereignisbudget⟩ | M37, M19, M16 |
| **Hausmarke** | Rezeptur, Lohnabfüllpreis, eigener Leergut-Pool, Zuckersteuer, Listung in den Märkten, Make or Buy | M07, M13, M14, M06, M11, M25 |

---

## 9. Aufgabentypen und automatische Bewertung

**Typen:**
- Stempel-Vorgang (Aktion, Betrag, Begründung)
- Abstimmung in Stück
- Rechenkette und Rechenweg-Editor (Zeilen „Bezeichnung = Betrag“)
- Lückentabelle (BAB, KER, DB-Stufen, Liquidität, Budget)
- Buchungssatz
- Fallakte im Deduktionsstil (Ursache – Betrag – echt oder Messfehler – Maßnahme; bestätigt erst ab zwei korrekten Slots)
- **Kurzfreitext** für „nennen, erläutern, beurteilen“
- Argumentkarten (nur Fading-Stufe 1–2, weil Abruf stärker wirkt als Wiedererkennen)
- Dialog, xlsx-Abgabe, Struktur-Upload (HB5)

**IHK-Format:**
- **Operatoren mit Punkteregel:** nennen 1 P je Nennung; erläutern 2 P (Nennung + Begründung); berechnen 1/1/1 für Ansatz/Weg/Ergebnis; beurteilen 2–4 P (Kriterium, Wertung, Empfehlung).
- **Zeit:** 1,8 min je Punkt in HB1/HB2 **[Vermutung]**.
- **Notenschlüssel:** 100–92 / 91–81 / 80–67 / 66–50 / 49–30 / 29–0 **[wahrscheinlich, IHK-üblich]**.
- **Probeklausuren:** 180/180/90 Min., zusätzlich als PDF zum Ausdrucken mit Bewertungsbogen ⟨Entscheidung: Prüfungsmodus auf Papier⟩. Es sind ausschließlich eigene Aufgaben; Original-Prüfungsaufgaben sind urheberrechtlich geschützt **[sicher, 05]**.

**Folgefehler und Lösungsgraph:** Jede Fallinstanz trägt einen Graphen der Teilergebnisse. Der Prüfer rechnet jeden Schritt mit den **eigenen Vorwerten** des Spielers nach und akzeptiert äquivalente Wege, die Diagnose meldet etwa „Fehler nur in Schritt 2“. Toleranzen: Geld ±1 € bzw. ±0,5 %, Quoten ±0,1 Prozentpunkte ⟨Entscheidung: Toleranzen⟩.

**Anzeigeregel:** Der Golden Master löst jede Aufgabe mit genau den angezeigten (gerundeten) Werten. Ein CI-Test vergleicht beides. Dieser Fehler steckte in allen drei Entwürfen bei der Eckkneipe.

**Kurzfreitext:**
- Standard ist Musterlösung plus Rubrik zur Selbstbewertung (Kernaussage, Begründung, Zahl, Grenze), dazu ein Regelprüfer für Betrag, Richtung und Schlüsselbegriffe. Die Selbstbewertung ergibt Hard oder Good.
- Ein LLM-Feedback ist optional, nie Gate und nie Punkte ⟨Entscheidung: Freitext-Bewertung⟩.

**Fehlerdiagnose:** Jede Vorlage führt Fehlerfunktionen mit; jeder Distraktor ist deren Ergebnis.
- Aus 03 (M1–M12): Aufschlag statt Spanne, brutto statt netto, Pfand im Umsatz, Vorzeichen der Bestandsveränderung u. a.
- Neu für die Gruppe:
  - **D1** Prozesskostensatz als kurzfristig abbaubar gelesen
  - **D2** versunkene Inventar-AfA als relevant gezählt
  - **D3** „VP verändert das Gruppenergebnis“
  - **D4** Zwischengewinn nicht eliminiert
  - **D5** Pfand netto/brutto vermischt
  - **D6** falsche Bonusbezugsbasis
  - **D7** inkonsistente Bezugsbasis in der Kalkulation (z. B. Füllvolumen statt Kostenverursachung; korrigiert gegenüber den widersprüchlichen Katalogen der Entwürfe)
  - **D8** kalkulatorischer Zins auf volle statt halbe AHK
  - **D9** Beschäftigungsabweichung als Verschwendung gedeutet
  - **D10** Aktion am Umsatz gemessen
  - **D11** Stichtagseffekt als Trend gedeutet
  - **D12** Forderungsausfall brutto statt netto (§ 17 UStG)
  - **D13** Kapitaldienstfähigkeit mit gemischter Formel (G15)
- **Ratedetektion:** Antworten unter 3 s zählen nicht für Mastery.

**Beispiel Situationsaufgabe „Die Eckkneipe“** (GH, Oktober 2027, 20 P, 36 Min. im Prüfungstakt).

*Situation:* Timmermann will 120 B-Kunden am unteren Rand auf 14-tägig setzen oder kündigen; Yıldız widerspricht: „Die Eckkneipe bringt 12.000 € Umsatz!“

*Anlagen (angezeigte Sätze):* RE I 4.200 €; 52 Stopps; 670 Kolli; 0,85 Leergutkästen je Kolli; 12 Besuche; AfA Leihinventar 1.500 €; Ausfallrisiko 2 %. Lagerung und Beschaffung 0,39 €/Kolli, Kommissionierung 0,32 €/Kolli, Leergut 0,35 €/Kasten, Stopp 34,16 €, Besuch 41,81 €, Diesel und Maut 4,83 € je Stopp.

| Teilaufgabe | P | Lösung |
|---|---|---|
| 1. Berechnen Sie den Kunden-DB I–III. | 6 | −261,3 − 214,4 − 199,3 − 1.776,3 → **DB II 1.748,7 €**; −501,7 − 1.500 − 240 → **DB III −493,1 €** |
| 2. Berechnen Sie den Mindestbestellwert für DB = 0 (Segment-RE 33 %, Kollikosten 5,67 % vom Umsatz). | 3 | 34,16 ÷ (33 % − 5,67 %) = **125 €**; Ø-Bestellwert der Kneipe 230,77 € |
| 3. Berechnen Sie DB II und III bei 14-tägiger Belieferung. | 3 | 26 Stopps → **DB II 2.636,8 €, DB III +395,1 €** |
| 4. Erläutern Sie, welche Kosten bei Kündigung kurz- bzw. langfristig wegfallen. | 4 | Kurzfristig nur Diesel und Maut (52 × 4,83 €) und das Ausfallrisiko: die Kündigung **kostet ≈ 3,7 T€**. Langfristig (Kapazität anpassbar, Prozesskostensätze ≈ variabel) trägt der Kunde **+1.007 €** bei. Die Inventar-AfA ist versunken. |
| 5. Beurteilen Sie Kündigung, Rhythmuswechsel und die Außendienstprämie. | 4 | Nicht kündigen, auf 14-tägig umstellen (Beitrag +1.895 €); Prämie auf DB II statt Umsatz (M51) |

*Kontrastpaar (Fehlerfunktion D1):* 120 Kunden auf 14-tägig sparen 3.120 Stopps = 183,5 Tourtage. Die Prozesskostenrechnung „spart“ 106,6 T€, kurzfristig abbaubar sind nur 15,1 T€ (14,2 %). Die Fahrerkosten (41,9 T€) fallen erst bei einer unbesetzten Stelle weg, die Lkw-Fixkosten (38,6 T€) erst bei Leasingende. Danach fahren 9 statt 10 Lkw mit 97,2 % Auslastung, fast ohne Reserve. Lehrsatz: „Prozesskostensätze sind Vollkosten; kurzfristig abbaubar ist, was jemand abbaut.“

---

## 10. Training für HB4, HB5 und HB6

**HB4 – Excel-Werkstatt** ⟨Entscheidung: HB4-Werkzeug⟩
1. **Mikroübungen** im Browser-Arbeitsblatt (eigener Formelparser plus formula.js, 04): Bezüge, SUMMEWENNS, XVERWEIS, WENN, RUNDEN.
2. **„Baue nach“-Aufträge** (30–60 Min.) ab Kapitel 2. Die Engine erzeugt ein Datenpaket als .xlsx (Kundenklassen, Leergutbewegungen, VP-Varianten). Der Spieler baut den Bericht in Excel oder LibreOffice Calc und lädt ihn mit **benannten Abgabezellen** hoch. exceljs prüft die Werte gegen die Engine, Formelzellen auf hartkodierte Zahlen und die Prüfsummen. Dazu kommt der Stammdatenfall „Flasche statt Kasten“.
3. **240-Min.-Probe** zweimal im Prüfungsjahr: Datenaufbereitung, Kennzahlen, Abweichungsbericht, Szenario/Zielwertsuche, IBCS-Grafik. Diagramm und Layout prüft nur eine Selbstcheck-Rubrik mit Musterdatei, weil exceljs Diagramme nicht liest **[wahrscheinlich]**.

**HB5 – Projektwerkstatt** ⟨Entscheidung: HB5-Transferpfad⟩
- **30-Kalendertage-Modus:** Tag 0 zwei Themenvorschläge (§ 4 Abs. 1–5 **[sicher, 01]**), Meilensteine an den Tagen 1/7/14/21/28/30 mit 20–40 Min. je Termin, dazu zwei **Formaliatage** (Umfang, Gliederung, Quellen, Eigenständigkeitserklärung).
- **Themenpool aus dem Run:** eigene Abfüllung, Lieferrhythmus der C-Kunden, VP-System, Zukunft von Markt 3, E-Sattelzug, Hausmarke und Zuckersteuer, Bonus-Tracking, IKS im Leergutprozess.
- **Transferpfad (Pflicht für das Zeugnis):** Dieselben Schablonen (Auftragsklärung, Issue Tree, Rechenkern, Nutzwert, Empfehlung) werden auf den **eigenen Betrieb** angewandt. Die echte Projektarbeit verlangt diesen Praxisbezug **[wahrscheinlich]**.
- **Bewertung:**
  - Automatisch: Pflichtkapitel, Zahlengleichheit von Text und Rechenkern, quantifizierte Empfehlung, genannte Risiken.
  - Inhalt: Rubrik nach § 4 Abs. 5 (Analyseinstrumente angewandt, Alternativen verglichen, Empfehlung gegeben, als Beratungsleistung aufbereitet) als Selbstbewertung.
  - Export als .docx/.pdf für Mentor oder Dozent; LLM-Feedback optional.

**HB6 – Präsentation, Fachgespräch, Führung** ⟨Entscheidung: HB6-Übungsform⟩
- **Präsentation:** Folienbaukasten mit ≤ 10 Folien, Kernaussage im Titel, SCQA, IBCS-Presets, Zahlen an den Rechenkern gebunden; 15 Min. mit Timer.
- **Fachgesprächs-Simulator:**
  - Fragen aus der eigenen Arbeit (Annahmen, Sensitivität, verworfene Alternativen) und aus HB1–HB6.
  - Drei Prüfer-Personas: Praktikerin, Methodiker, Skeptiker.
  - Antwortschema „Kernaussage – Begründung – Zahl – Grenze“.
  - Die Beiratsfrage „Kessler springt ab“ dient als Aufwärmrunde.
- **Selbstaufnahme:** per Browser-Mikrofon, nur lokal (MediaRecorder), mit Checkliste.
- **Führung und Moderation** (§ 4 Abs. 6 **[sicher]**):
  - Budgetrunde mit drei Kostenstellenleitern nach Moderationszyklus.
  - Konfliktgespräch Timmermann ↔ Yıldız nach Glasl-Stufen.
  - Inventur mit drei Zählteams (Zweitzählung ab 2 % Abweichung).
  - Lena anleiten: Delegation, Stichprobe, Feedback nach Situation–Verhalten–Wirkung.
- **Grenze:** Ein Dialogbaum trainiert Erkennen, nicht Auftreten. Deshalb gibt es einen **Peer-Modus mit druckbaren Rollenkarten** für Lerntandems und Lehrgangsgruppen.

---

## 11. Drei Beispielszenen

### Szene A – „Die 9,99-€-Woche“ (K1, Februar 2027, Markt 1, ≈ 25 Min.)

*Module M07, M09, M41, M45, M08; HB1/HB4.*

**Ausgangslage:** Lindemann (Brauerei Nordhang) bietet für KW 7 Fernsehpils L01 zu 9,99 € brutto an: Aktions-EK 8,20 €, WKZ 400 €. Sabine will zusagen, ihre Prämie hängt am Markt-Rohertrag. Tobias fragt: „Lohnt sich das?“ Kosten: 6 Controllerstunden.

1. **Frühschicht:** 6 Items, darunter „Spanne vs. Aufschlag“ (Flugrost).
2. **Glass Box:** Normal-VK 14,697 € netto, Gruppen-Einstand 11,656 €, VP an den Markt 12,006 €. Aktion: 8,395 € netto, Einstand 7,708 €, VP 7,939 €.
3. **Vorgang im Prüfungsformat (20 P, Fading-Stufe 2):**

| Teilaufgabe | P | Lösung |
|---|---|---|
| a) Berechnen Sie den Stück-DB normal und in der Aktion für Markt (VP) und Gruppe (Einstand). | 4 | Markt 2,692 / 0,456 €; Gruppe 3,041 / 0,687 € |
| b) Berechnen Sie den inkrementellen Rohertrag je Aktionswoche (Basis 120 Kästen, Lift × 4, 60 % Kannibalisierung, 48 Kästen Nachholeffekt, 150 Verbundbons, Leergut für 96 echte Mehrkästen). | 8 | siehe Tabelle |
| c) Erläutern Sie zwei Ursachen für den Unterschied zwischen Markt und Gruppe. | 4 | Das WKZ fließt der KG zu; der VP-Aufschlag verschiebt Marge in die KG; die Leergutkosten fallen auf beiden Ebenen an |
| d) Beurteilen Sie das Angebot und empfehlen Sie Tobias eine Entscheidung. | 4 | Gegenangebot 10,99 € mit Aktions-EK 8,60 €: Markt −134,8 €, Gruppe +254,5 € (bei gleichem Lift, also optimistisch); dazu Prämienbasis von Sabine ändern |

| Komponente je Aktionswoche | Markt 1 (VP) | Gruppe (Einstand) |
|---|---|---|
| 480 Aktionskästen × Stück-DB | +218,7 | +329,7 |
| entgangene Basis 120 Kästen | −323,0 | −365,0 |
| Kannibalisierung 216 Kästen (2,80 / 3,10 €) | −604,8 | −669,6 |
| Nachholeffekt 48 Kästen | −129,2 | −146,0 |
| Verbund 150 Bons (3,40 / 3,60 €) | +510,0 | +540,0 |
| WKZ | 0 | +400,0 |
| Leergut 96 Mehrkästen (Markt 0,25 €; KG zusätzlich 0,35 €) | −24,0 | −57,6 |
| **Ergebnis** | **−352,3 €** | **+31,6 €** |

4. **Fehlerdiagnose:**
   - „+2.265,90 € Umsatz“ → D10 (Aktion am Umsatz gemessen).
   - 0,456 € als Gruppen-db → D3 (VP verschiebt nur).
   - Ohne Kannibalisierung ergäbe sich +252,5 € für den Markt.
   - Mit Brutto-VK ergäbe sich ein Stück-DB von 2,051 € → M2.
5. **Gespräch mit Sabine:**
   - Option *Vorwurf* („Ihre Aktion kostet 352 €“) senkt ihr Vertrauen.
   - Option *Zahlenblick* (nur mit dem Skill Stück-DB „gelernt“): „Für den Markt ist es ein Verlust, für die Gruppe knapp positiv, und nur wegen des WKZ. Das Problem ist Ihre Prämienbasis.“ Das öffnet den Folgevorgang Prämienformel (M51) und den K3-Faden Verrechnungspreis.
6. **Entscheidungskarte an Tobias** nach der Regel aus 4.1.
7. **Verzögerte Konsequenz:**
   - 300 Kästen wurden zum Aktions-EK bezogen, aber nach KW 7 normal verkauft. Die Brauerei belastet 300 × (11,656 − 7,708) = **1.184,40 €** nach.
   - Wer im Februar-Abschluss (AT3) keine Abgrenzung bildet, findet den Betrag im März als periodenfremden Aufwand („Fall des Monats“) und im April als Citation aus der Quartalsstichprobe von Dr. Esser. Der Golden Master liegt damit innerhalb des MVP-Ausschnitts Januar bis März.
8. **Debrief:**
   - Kontrafaktum: Gegenangebot statt Zusage.
   - Lehrsatz: „Wessen Marge? Erst die Ebene klären.“
   - Die Skills `sk.aktion.inkrementell`, `sk.vp.ebene` und `sk.abgr.nachbelastung` gehen in den Scheduler.
   - Bewertungsbogen: x/20 P, Note nach Schlüssel.

### Szene B – „Drei Salden und eine E-Mail“ (K2, Januar 2028, AT2–AT5, ≈ 30 Min.)

*Module M44, M48, M08, M23, M22, M24, M55; HB1–HB3/HB6.*

1. **Stundenkonflikt:** Im Januar fallen Inventur an vier Standorten, 40 Saldenbestätigungen, Bonusabrechnung und Jahresabschlussvorbereitung an. Der Spieler delegiert die Wiederverkäufer-Leergutkonten an Lena (spart 12 h) und behält die Brauereikonten.
2. **AT2 Saldenbestätigung Brauerei Nord, Bierkästen:**
   - Auszug 62.480, eigenes Konto 61.200, die Differenz **1.280** ist zu klären.
   - (a) 880 Kästen am 30.12. zurückgegeben, bei der Brauerei erst am 04.01. gebucht: Periodenverschiebung, Umgliederung „Gutschrift offen“ 2.296,80 € ohne Wertkorrektur.
   - (b) 300 Fremdkästen der Brauerei Süd zurückgewiesen: Umbuchung aufs Süd-Konto, 783,00 €.
   - (c) 100 Kästen Zähldifferenz bei der Rücknahme, Rügefrist 5 Werktage. Wer im Dezember das Protokoll gerügt hat, bekommt eine Gutschrift. Sonst entstehen **261,00 €** Aufwand und eine Citation.
3. **AT3 Bonusabgrenzung** (Folge einer Dezember-Karte):
   - Staffel 1 % ab 95 %, 2 % ab 100 %, 2,5 % ab 105 % auf 200.000 Kästen Vorjahr, Ø-EK 11,90 €; Ist 198.400 (99,2 %).
   - Der Spieler hatte 1.600 Kästen Vorkauf empfohlen, das ergäbe 2 % = 47.600 € statt 1 % = 23.610 €.
   - Vertrag § 4: Bezugsbasis ist der **Abverkauf laut hl-Meldung**, die Abgrenzung beträgt also **23.610 €**.
   - Restnutzen: 960 € aus der Preisrunde gegen ≈ 214 € Zins und 40 Paletten Stellplatz im Silvester-Peak.
   - Kontrafaktum: Mit „Prüfauftrag: Vertrag lesen“ (2 h) hätte die Empfehlung nur auf die Preisrunde gezielt.
4. **AT4/AT5 E-Mail der GF:** „Kontokorrent 682,9 T€, Plan 566,1. Problem?“
   - Überleitung in zwei Stichtagstreiber und einen Strukturtreiber:
     - Leergut-Überhang 42.000 statt 30.000 Kästen (Abholung wegen Fahrermangel ausgefallen): 12.000 × 2,633 € = **+31,6**
     - Vorkauf (Ware und Pfand netto) **+23,2**
     - DSO Gastro 27 statt 25 Tage: 9.500 × 1,19 × 2/365 = **+61,9**
     - Summe **+116,7 T€** ✓
   - Covenant-Tacho: EK-Quote 29,5 % (Plan 29,9 %), ND/EBITDA 2,92 (Plan 2,77), unkritisch.
   - Antwort nach dem Muster „Botschaft zuerst, drei Treiber, eine Maßnahme“: Mahnlauf und Lastschriftpflicht für C-Kunden. Bewertet wird sie als Kurzfreitext mit Rubrik.
5. **Delegation:** Die Stichprobe von 5 der 40 Konten findet bei Lena Paletten als Warenumschließung statt als eigene Leistung mit 19 % (BMF 05.11.2013 **[wahrscheinlich]**). Der Spieler gibt Feedback nach Situation–Verhalten–Wirkung; gutes Feedback senkt Lenas Fehlerquote.
6. **Verzögerte Konsequenz aus Oktober 2027:**
   - Im Datenraum standen beim Bistro Mühlentor zwei Rücklastschriften und ein wachsender Leergutsaldo. Im Februar 2028 meldet das Bistro Insolvenz.
   - Ohne Reaktion: Forderung 7,4 T€ brutto (Ware und Pfand) bei 5 % Quote → Ausfall netto 5,9 T€ (USt-Berichtigung 1,1 T€ nach § 17 UStG **[sicher]**), Darlehensrest 17,1 T€, Inventar (Restbuchwert 8,0, Verwertung 30 %) 5,6 T€ → **28,6 T€**.
   - Mit Prüfauftrag im Oktober (Barzahlung ab November, Bürgschaft deckt 40 % des Darlehens, Inventar früh zurückgeholt): **16,1 T€**.
   - Für die Gebinde beim Wirt heben sich verlorener Erstattungsanspruch und wegfallende Pfandverbindlichkeit im Bruttomodell auf; der Verlust steckt in der offenen Forderung.
7. **Debrief:** Treiberbaum Kontokorrent, Kalibrierung. Lehrsätze: „Erst Bezugsbasis lesen, dann Staffel rechnen.“ und „Stichtag ist nicht Trend.“

### Szene C – „Selbst abfüllen?“ (K3, Projekt Mai–November 2028, Plan 2029, 4 Sessions)

*Module M06, M07, M11, M13, M14, M15, M25, M37, M42, M43, M50; HB1/HB2/HB5/HB6.*

**Ausgangslage:**
- Hollmann kündigt für 2029 **+18 %** an, dazu 380 € Rüstpauschale je Charge und einen Kapazitätsvorbehalt Juni bis August (ihre eigene Marke hat Vorrang).
- Tobias: „Dann bauen wir selbst.“
- Kessler (Regionalbrauerei) schließt seine AfG-Linie, sucht einen Lohnabfüller für 1,0 Mio. Fl 0,5 l pro Jahr, bietet 0,16 €/Fl und **3 Jahre** Laufzeit.
- Planvolumen Hausmarke 2029: 26.000 / 11.000 / 18.000 Kästen = 1,06 Mio. Fl, 531.920 l (Gastro-Rollout aus K2; im Standardpfad mit Rezeptur unter 5 g, also steuerfrei).
- Angeboten ist eine generalüberholte Mehrweg-Glaslinie: AHK 950 T€, Wiederbeschaffungswert 1.050 T€, 10 Jahre; nominal 4.000 Fl/h bei 0,33 l, Gesamtanlageneffektivität 65 % ⟨Entscheidung: Parameter Abfüllanlage⟩; 800 m² Halle der Besitzgesellschaft zu 5 €/m².
- Planbeschäftigung mit Kessler: 2.372.600 Äquivalenzflaschen = **912,5 h** (54,1 % einer Schicht, Hausmarke allein 27,9 %).

1. **Erst probieren:** „Die Lohnabfüllung kostet 280,3 T€ im Jahr, die Anlage 950 T€, nach 3,4 Jahren bezahlt.“ Die Auflösung zeigt, was fehlt: eigene Betriebskosten, Auslastung, Zeitwert.
2. **Projektauftrag (HB5-Format):** Ziel, Kriterien, Termin Budgetrunde 15.10. Teamaufgaben verteilen: Timmermann prüft die Fläche, QS die Lebensmittelauflagen, der Einkauf die CO₂-Versorgung.
3. **Plan-BAB (Stufenleiter; Fading 2; Worked Example von Kesslers Betriebsleiter):**

| T€ | H1 Energie/Medien | H2 Technik | H3 QS/Labor | F1 Ausmischung | F2 Leergut/Waschen | F3 Füllen/Etikettieren | F4 Palettieren/Lager |
|---|---|---|---|---|---|---|---|
| Primärkosten | 58,9 | 42,9 | 32,2 | 24,3 | 87,4 | 141,5 | 31,1 |
| Umlage H1 (nach kWh) | −58,9 | +1,8 | +1,2 | +2,9 | +32,4 | +14,7 | +5,9 |
| Umlage H2 (nach Instandhaltungsstunden) | – | −44,7 | +0,9 | +3,6 | +15,6 | +20,1 | +4,5 |
| Umlage H3 (nach Prüfaufwand) | – | – | −34,3 | +13,7 | +3,4 | +17,1 | – |
| **Endkosten** | 0 | 0 | 0 | **44,5** | **138,8** | **193,5** | **41,5** |
| Bezugsgröße und Satz | | | | 1.031.920 l → 0,0431 €/l | 2.372.600 Äquivalenzflaschen (912,5 h) → **0,1401 €** bzw. **270,15 €/h** ohne, 364,11 €/h mit Bedienung | | 105.000 Kästen → 0,395 €/Kasten |

   Summe 418,2 T€:
   - Fix 300,5 T€, darunter kalkulatorische AfA 105 (Wiederbeschaffungswert ÷ 10) gegen bilanziell 95 (Anderskosten) und kalkulatorischer Zins 6 % × 950/2 = 28,5 (Zusatzkosten).
   - Variabel 117,7 T€ (49,6 € je 1.000 Äquivalenzflaschen).
   - H3 enthält Laborfreigaben, HACCP-Dokumentation und Rückstellmuster; F3 die Produkthaftpflicht.
4. **Kalkulation je Gebinde mit Bezugsgrößen:** F1 je Liter, die Linie F2+F3 nach Maschinenzeit (Äquivalenzziffern 1,00 / 1,15 / 1,60), F4 je Kasten. Herstellkosten **0,171 / 0,202 / 0,300 €/Fl** (4,10 / 4,05 / 3,60 €/Kasten).
   - *Kontrastpaar:* Alles nach Maschinenzeit ergäbe 0,176 / 0,203 / 0,282 €; dann wäre die 1,0-l-Flasche zu billig gerechnet, weil die volumenabhängige Ausmischung fehlt (D7).
5. **Prüfung der Hollmann-Kalkulation** (je 1.000 Fl 0,33 l, prüfungskonformes Schema):

   | Position | € |
   |---|---|
   | Maschinenkosten 418,50 €/h ÷ 4.000 Fl/h | 104,63 |
   | Fertigungslohn 176 €/h | 44,00 |
   | Energie (+40 %) | 22,40 |
   | Reinigung/Rüsten anteilig | 9,50 |
   | **Herstellkosten** | **180,53** |
   | Verwaltungsgemeinkosten 10 % | 18,05 |
   | Vertriebsgemeinkosten 5 % | 9,03 |
   | **Selbstkosten** | **207,60** |
   | Gewinn 8 % | 16,61 |
   | **Angebotspreis** (+18,0 % auf 190) | **224,21** |

   - **Fehler A:** kalkulatorischer Zins auf volle statt halbe AHK, 35 €/h zu viel → −10,87 € (D8).
   - **Fehler B:** Energie +40 % statt Gleitklausel-Index +12 % → −5,56 €.
   - Korrigiert: **207,78 € (+9,4 %)**.
   - **Streitpunkt C:** Laut Abfüllprotokollen lief die Hausmarke mit 4.200 Fl/h → **199,51 € (+5,0 %)**.
   - Die Zone möglicher Einigung liegt zwischen +5,0 und +9,4 %. Glaubwürdig wird die BATNA „eigene Linie“ nur durch den Plan-BAB.
   - Zweiter Hebel: doppelte Losgröße (20 statt 40 Chargen) spart 7,6 T€ Rüstpauschale.
   - Verhandlungs-Minispiel mit Hollmann; Standardpfad-Ergebnis **+9 %** (0,207 / 0,229 / 0,273 €/Fl).
   - *Fallmaschine:* Vorlage 2 übt dieselbe Prüfung als Zuschlagskalkulation (MGK, FGK auf Lohn, SEKF, VwGK, VtGK, Gewinn): Der Lohnabfüller B erhöht den FGK-Satz von 175 auf 195 % auf den gestiegenen Lohn und schlägt die Energie zusätzlich separat auf. Gefordert sind +16,0 %, berechtigt +6,5 %.
6. **Make or Buy 2029 erst nach der Verhandlung** (die BATNA steht vor dem Vergleich):
   - Buy zu +9 %: 260,6 T€ (Lohn 238,4, Rüstpauschale 15,2, Fracht 7,0).
   - Make kalkulatorisch: 258,2 T€ mit Kessler, 361,2 ohne.
   - Kritische Menge allein für die Hausmarke: 1,79 Mio. Fl gegen 1,06 Mio. Plan.
   - Kesslers 0,16 €/Fl liegen unter den Vollkosten (0,202), aber über den variablen Kosten (0,057). Der Zusatzauftrag liegt also über der kurzfristigen Preisuntergrenze, bringt aber ein Klumpenrisiko.
   - Bei Vollauslastung ist Make für 0,33 und 0,5 l günstiger als Buy, für 1,0 l nicht.
7. **Kapitalwert** (Zahlungen, 6 %, 10 Jahre, Restwert 0, gegen Buy +9 %):

| Kessler-Laufzeit | 10 J. | 9 J. | 7 J. | 5 J. | 3 J. | ohne |
|---|---|---|---|---|---|---|
| Kapitalwert T€ | **+50,4** (IZF 7,1 %) | −7,1 | −132,6 | −273,6 | **−432,1** | −707,3 |

   - Die Break-even-Laufzeit liegt bei ≈ 9,1 Jahren. Kessler bietet aber nur 3.
   - Gegen die unverhandelten +18 % wäre schon Kessler über 7 Jahre positiv (+12,3); wächst die Hausmarke um 5 % pro Jahr, ergäbe Kessler über 10 Jahre +349,6.
   - Lehrsatz: „Die gute Verhandlung entwertet die eigene Anlage, und ohne die Anlage gäbe es die gute Verhandlung nicht.“
8. **Bank:** Mit 950 T€ Kredit auf Basis der Planbilanz 31.12.2027 **[Annahme]** liegt die EK-Quote bei 26,5 %. ND/EBITDA beträgt **3,41** mit Kessler (Headroom 0,09) und **3,85 ohne Kessler, also Covenant-Bruch**. Vogt verlangt Take-or-pay oder Leasing.
9. **K.-o.-Kriterien neben dem Kapitalwert** (Pflichtteil der Vorlage):
   - Registrierung als Lebensmittelunternehmer und HACCP **[wahrscheinlich, VO (EG) 852/2004]**.
   - Rückverfolgbarkeit (Art. 18 VO (EG) 178/2002) und Haftung als Inverkehrbringer; Rückruf-Erwartungsschaden 2 % × 120 T€ = 2,4 T€/J. **[Vermutung]**.
   - CO₂-Versorgung (Knappheit 2022).
   - Flächenkonflikt im Silvester-Peak.
10. **Vorlage und Beirat:**
    - Expertenpfad: „Buy zu +9 % mit Open-Book-Klausel und Kapazitätsgarantie. Make nur bei ≥ 10 Jahren Take-or-pay über ≥ 1,0 Mio. Fl oder mit Restwertsicherung. Wiedervorlage ab 1,5 Mio. Fl Hausmarke.“
    - Hildegard fragt nach dem Szenario „Kessler springt ab“.
    - Tobias entscheidet nach der Regel aus 4.1; bei schwacher Vorlage kauft er (seine Vorliebe) ⟨Entscheidung: Ausgang Make-or-Buy⟩.
11. **Folgen 2029:**
    - **Kauf:** Ab 2029 laufen monatlich Ist-BAB, flexible Plankosten und Bestandsbewertung der Fertigware zu Herstellkosten (§ 255 Abs. 2 HGB **[sicher]**), außerdem Kostenträgerzeitrechnung nach GKV mit Bestandsveränderung.
      - Juli: Plan 95 h (Hausmarke 52, Kessler 43), Kessler ruft nur 60 % ab → Ist 77,8 h; Istkosten der Linie 30,40 T€.
      - Sollkosten 27,90, verrechnete Plankosten 24,53 → **Verbrauchsabweichung +2,50 T€** (Laugentemperatur), **Beschäftigungsabweichung +3,37 T€** (Leerkosten, D9).
      - Mit Normal-Maschinenstundensatz 364,11 €/h: Unterdeckung 2,07 T€.
      - Fall „Wer ist schuld?“ mit dem Lehrsatz „Leerkosten sind keine Verschwendung.“
    - **Buy:** quartalsweise Open-Book-Nachkalkulation gegen den Schatten-BAB des Spielers, Kontrolle der Gleitklausel, Wiedervorlage bei 1,5 Mio. Fl.
    - In beiden Zweigen ist „Eigene Abfüllung“ ein Thema der HB5-Werkstatt.

---

## 12. Technik und MVP-Schnitt

**Architektur** (04, alle Kernabhängigkeiten MIT/Apache/ISC **[sicher, npm 19.10.2026]**):
- Angular-22-PWA, local-first; Dexie für IndexedDB, `navigator.storage.persist()`.
- Frameworkfreie, deterministische TS-Engine `step(state, action)` mit Integer-Cent, Hauptbuch (Soll = Haben) und Leergut-Nebenbuch in Stück.
- YAML/Markdown-Inhalte mit Zod-Prüfung.
- ts-fsrs 5.4; ECharts mit IBCS-Presets; eigener Formelparser plus formula.js; exceljs.
- Cloudflare Pages unter `spiel.marvinwiemers.de`; neues, sauberes Repo (04, 0.1) ⟨Entscheidung: Plattform und Framework⟩ ⟨Entscheidung: Lizenzmodell⟩.

**Neu für dieses Konzept:**
1. **Mehrgesellschafts-Datenmodell ab Tag 1:** Gesellschaft, Kostenstelle, Innenleistung, Leergutkonto je Partner und Gebindeart (08).
2. **Fallmaschine** (`packages/cases`):
   ```ts
   interface CaseTemplate { id; skills: string[]; trigger: Ausdruck; schwierigkeit: 1|2|3; anlagen: AnlagenGen[];
     teilaufgaben: { id; operator: 'nennen'|'erlaeutern'|'berechnen'|'beurteilen'; punkte; solverId; checker;
       dependsOn: string[]; fehlerfunktionen: string[]; skills: string[] }[];
     oberflaechen: ('einzel'|'tabelle'|'fehlersuche'|'freitext')[]; stunden: number; spielwirkung?: DecisionCardId }
   ```
   - **Auswahlregel:** Die Vorlage deckt fällige Skills ab, passt zu Monat und Ereignis, ihre Oberfläche war zuletzt nicht dran, die Schwierigkeit liegt im Zielband (70–85 % Erfolg, Elo).
   - **Abdeckungsgarantie:** Passt kein natürlicher Fall, kommt ein Sonderauftrag (Bank, Verbund) oder ein Transferfall.
3. **Dokumentgenerator** mit seedbasierter Fehlerinjektion (Beleg, Saldenbestätigung, Kontoauszug, E-Mail); Regelwerk als Daten; Tool-Registry (Skill → Werkzeug); Posteingang-Scheduler mit Stundenbudget und Lastdeckel.
4. **Golden Master:** Modell 08 plus `final.py` (Hausmarke, Abfüllung, Szenen). Die Anzeigeregel ist als CI-Test umgesetzt; je Vorlage laufen 50 Instanzen, der Distraktor darf nie gleich der Lösung sein (04). Common Random Numbers für Replays.
5. **`lernziele.yaml`, `skript_map.yaml`, Abdeckungsbericht** im Build (7.1).
6. **Entwicklerwerkzeuge:** simulierte Uhr, Zeitsprung, synthetische Lernende für Lasttests des Schedulers.
7. **Gerätewechsel:** ab MVP Export und Import als Datei bzw. QR-Code, Erinnerung bei Backups älter als 14 Tage. Vor 1.0 optionaler Sync über Firebase mit anonymer Anmeldung und Pseudonym ⟨Entscheidung: Sync⟩.
8. **Mobil (375 px):** Frühschicht-Typen Zahl (`inputmode="decimal"`, Komma-Parser), Auswahl, Zuordnung, kurze Rechenkette, Kurzfreitext. Lückentabellen, BAB und Excel-Werkstatt laufen erst ab 768 px; der Scheduler wählt passend zum Gerät ⟨Entscheidung: Mobile Aufgabentypen⟩.

**MVP-Schnitt** ⟨Entscheidung: MVP-Schnitt⟩

| Stufe | Inhalt | PT **[Vermutung]** |
|---|---|---|
| **K0 Kernbeweis** (ohne Spielrahmen) | Golden-Master-Daten mit Seed-Perturbation von 20 Parametern; Fallmaschine mit 8 Vorlagen (u. a. Aktion, Eckkneipe, Saldenbestätigung, KER, Kalkulation); Prüfer mit Lösungsgraph, Folgefehlern, Fehlerfunktionen, Kurzfreitext-Rubrik; FSRS-Frühschicht mit Credit Assignment; Profil je Lernziel; Entwicklerwerkzeuge | **22–30** |
| **K1 Schreibtisch-MVP** (zusätzlich) | Schreibtisch-UI (Posteingang, Dokumentansicht, Arbeitsblatt, Stempel, Regelbuch, Datenraum light); Dokumentgenerator; Januar bis März 2027 in Markt 1 mit Szene A und Nachbelastung im März; zwei Großhandels-Vorgänge; Monatsgate, Stundenbudget light; 2 Werkzeuge mit Beschlagen; Leitfrage, 3 Figuren, Vertrauen; +6 Vorlagen, 10 Theoriekarten; `skript_map` und Abdeckungsbericht; Playtest 3 Wochen | **25–35** |
| **Summe MVP** | | **47–65** (mit KI-Unterstützung im Code ≈ 38–52; im Hobbytempo 1,5 PT/Woche ≈ 7–10 Monate) |

**Beweiskriterien:**
- ≥ 4 von 5 Testpersonen aus der Zielgruppe spielen an ≥ 10 von 21 Tagen; Frühschicht im Median ≤ 6 Min.
- Re-Test nach 14 Tagen ≥ 70 % korrekt; die Probeklausur steigt bei neuen Seeds um ≥ 15 Punkte.
- Die Automatik stimmt in ≥ 90 % der Teilpunkte mit einer blinden Dozentenkorrektur überein.
- **Eine neue Vorlage kostet ≤ 0,5 PT inklusive Fachreview.** Das ist der wichtigste Produktmesswert, weil der Inhalt der Engpass ist.

**Danach:**
- **Release Kapitel 1** (Engine für Markt 1 tagesgenau, alle K1-Routinen, Prüfungsmodus HB1-Teil): ≈ 120–160 PT kumuliert.
- **Version 1.0** ≈ 300–420 PT:
  - Engine 55–80; UI 35–50; Fallmaschine und Prüfungsmodus 10–15; Werkstätten HB4–6 20–30.
  - Inhalt ≈ 140–160 (≈ 150 Lernziele, ≈ 220 Vorlagen à 0,45 PT, Dossiers, ≈ 90 Szenen).
  - Balancing, Längsschnitt und Fachreview 35–55; Sync, Mobil und Barrierefreiheit 10–15.
- Im Hobbytempo sind das **4–5,5 Jahre**. Deshalb kapitelweise veröffentlichen. Die gelieferten Skripte senken vor allem den Theorieposten; das Fachreview ersetzen sie nicht.

---

## 13. Risiken und Gegenmaßnahmen

| Risiko | Wirkung | Gegenmaßnahme |
|---|---|---|
| Inhaltsvolumen übersteigt ein Ein-Personen-Projekt | Abbruch vor Kapitel 3 | Vorlagenkosten im MVP messen (≤ 0,5 PT), KI-Entwurf plus CI gegen den Golden Master plus Reviewer mit Stundenbudget ⟨Entscheidung: Inhaltsproduktion⟩; kapitelweise Releases |
| Fach- oder Rechenfehler in Musterlösungen | Vertrauensverlust, falsch gelehrte Regeln (in den Entwürfen geschehen) | keine handgepflegten Zahlen, Anzeigeregel-Test, Fachreview durch eine GFGH-Controllerin ⟨Entscheidung: Fachreview⟩, Plausibilitätsprüfungen in `final.py` |
| Routine-Ermüdung über 36 Monate | Monotonie | jeden Monat eine neue Regel, Störung oder Figurenkonflikt; Routine-Kompression; Zeitdruck nur als Kür |
| Abbruch nach Pausen | Rückstau, Schuldgefühl | Rückkehrmodus (≤ 10 pro Tag), Urlaubsschein, keine Sperre durch Rost, Inspektionsrundgang statt Popup |
| Binge-Spieler laufen gegen das Kapitelgate | Frust am ersten Abend | Wartebeschäftigung (Archivakte, Werkstatt, Probeklausur), ehrliche UI-Botschaft |
| Skripte schneiden Lernziele anders | Umverdrahtung | Skill-Indirektion, n:m-Zuordnung, `ersetzt_durch`, Abdeckungsbericht |
| Prüfungsstil verfehlt | Nahtransfer ohne Prüfungsnutzen | Abgleich mit Skripten und gekauften Altaufgaben nur intern; Dozenten-Review; Papier-Probeklausuren |
| Überanpassung an die Getränkebranche | Rechnen in Rohertrag statt Herstellkosten | 10–15 % Transferfälle, ≥ 3 Oberflächen je Lernziel |
| Datenverlust (Safari-Eviction) bei monatelanger Pflicht | Lernstand weg | `persist()`, Backup-Erinnerung, Datei/QR, Sync vor 1.0 |
| Rechtsstand altert (Zuckersteuer, Mindestlohn, PPWR) | Details falsch | Freeze 20.10.2026, Versionierung, Fortschreibung als fiktiv markiert |
| Rechtliches (IHK-Bezug, Marken, Alkohol) | Abmahnung, Schulausschluss | kein „IHK“ im Titel, Disclaimer „keine Verbindung zu IHK/DIHK“, fiktive Marken ⟨Entscheidung: Marken⟩, Sortimentsschalter ⟨Entscheidung: Alkoholschalter⟩ |
| Kleine Zielgruppe (80–115 pro Jahr) | geringe Reichweite | Nebenzielgruppen, Lehrgangsträger als Kanal, kostenlos als Portfolio ⟨Entscheidung: Monetarisierung⟩ |

---

## 14. Offene Designentscheidungen (Auszug; vollständig in `offene-entscheidungen.md`)

| Nr. | Frage | Optionen | Empfehlung |
|---|---|---|---|
| 1 | Grundrichtung | Routine-first + Fallmaschine / Prüfungstrainer / Story-Kampagne | Routine-first + Fallmaschine **[wahrscheinlich]** |
| 2 | Primäre Zielgruppe | Lehrgangsteilnehmende / Junior-Controller im Handel / Azubis + Schule | Lehrgangsteilnehmende, Rest sekundär |
| 3 | Hausmarke-Produkt | Limonade / Apfelschorle / Mineralwasser | Limonade; Apfelschorle als Seed-Variante |
| 4 | Zuckersteuer-Konvention | in Kraft 1.1.2028 / 1.7.2027 / Seed / weglassen | 1.1.2028, Seeds variieren |
| 5 | Ausgang Make-or-Buy | offene Weiche nach Regel / Kauf fest / Buy fest | offene Weiche, Plan-BAB in beiden Zweigen Pflicht |
| 6 | Entscheidungsregel GF | transparente Regel / Wahrscheinlichkeit / Spieler entscheidet | transparente Regel |
| 7 | Gates | Monatsgate + Kapitelgate / zusätzlich Rost-Sperre / keine | Monat + Kapitel, Rost nur Beschlagen |
| 8 | Frühschicht | Pflicht über Einbettung ins Monatsgate / harte Tagespflicht / freiwillig | Einbettung |
| 9 | Pflichtkanon | IHK hoch / hoch + mittel / alles | hoch + mittel |
| 10 | Prüfungstermin-Countdown | Countdown mit Tapering / nur FSRS | Countdown |
| 11 | Stundenbudget als Kernressource | ja / nein | ja |
| 12 | Kapitelzuschnitt | Setting-Kapitel + Lehrgangsmodus / strikt nach HB / frei | Setting + Lehrgangsmodus |
| 13 | Freitext-Bewertung | Rubrik + Regelprüfer / + LLM-Feedback / nur Auswahl | Rubrik + Regelprüfer, LLM ab 1.1 |
| 14 | HB5-Transferpfad | Pflicht fürs Zeugnis / optional | Pflicht |
| 15 | MVP-Schnitt | K0 + Schreibtisch-MVP / nur K0 / MVP mit Engine | K0 + Schreibtisch-MVP |
| 16 | Sync vor 1.0 | Datei/QR + optional Firebase / nur Datei / Pflicht-Konto | Datei/QR + optional Firebase |
| 17 | Simulationstiefe | Aggregate + benannte Einheiten / Tagestick ganze Gruppe | Aggregate; Tagestick nur Markt 1 |
| 18 | Lernziel-Katalog | jetzt vorläufig aus ContrPrV + Modulen / auf Skripte warten | jetzt vorläufig |

---

## 15. Glossar der Spielbegriffe

| Begriff | Bedeutung |
|---|---|
| AT1–AT5 | Arbeitstage des Monatsabschlusses mit festen Routinen |
| Archivakte | Übungsabschlüsse aus Markt 2/3 oder Vorjahren, zählen als Wiederholung |
| Beschlagen | Werkzeug bei R < 0,70: zeigt nur noch die Richtung, keine Zahl |
| Citation | verzögerte Beanstandung des Abschlussprüfers aus eigenen Vormonaten |
| Common Random Numbers | Zufall per Hash aus Seed, Tag, Objekt und Zweck; macht das Kontrafaktum möglich |
| Fallakte | Speicher aller Fehler als Fälle mit Wiederkehr nach 2–7 Tagen |
| Fallmaschine | erzeugt Vorgänge aus Vorlage, Spielstand, Seed und fälligen Skills |
| Fading | fünf Stufen vom Worked Example bis zum leeren Blatt |
| Frühschicht | tägliche 5-Min.-Wiederholung, ≤ 8 Items |
| FSRS | Scheduler (ts-fsrs) für den Abrufzeitpunkt je Skill in Echtzeit |
| Golden Master | skriptgeprüfter Referenzzustand, gegen den jede Musterlösung getestet wird |
| Kapitelgate | Kapitelprüfung, frei nach „gelernt“ der Kern-Skills |
| Kontrafaktum | Replay mit genau einer geänderten Entscheidung |
| Korrespondenzfigur | Figur nur über Dokumente und E-Mails, ohne Dialogbaum |
| Lernziel-ID | opake, unveränderliche ID je Lernziel, n:m zu HB, Skills und Skriptkapiteln |
| Monatsgate | Monatsabschluss schließt erst nach bestandenen Pflichtvorgängen |
| Oberfläche | Darstellungsform einer Vorlage: Einzelrechnung, Tabelle, Fehlersuche, Freitext |
| Pohls Ordner | Übergabeordner des Vorgängers mit Worked Examples; Nutzung gilt als „mit Hilfe“ |
| Prüfungsfest | Mastery-Stufe: ≥ 67 % unter Zeitlimit in den letzten 30 Tagen |
| Routine-Kompression | beherrschte Routinen laufen als 1-Klick-Check oder delegiert |
| Skill | kleinste geplante Wissenskomponente, Träger der FSRS-Historie |
| skript_map | Datei, die Lernziele den Kapiteln der Lehrgangsskripte zuordnet |
| Stundenbudget | 160 Controllerstunden je Spielmonat als knappe Ressource |
| Vorgang | eine Aufgabe im Posteingang, meist im Prüfungsformat |
| Wissen ist Sicht | gemeisterte Methoden schalten Werkzeuge, Vorschauen und Dialogoptionen frei |

---

## 16. Quellenhinweise

- **Prüfungsrecht:** ContrPrV über gesetze-im-internet.de (§§ 3, 4, 7 nur über Suchauszüge); IHK Koblenz, München, Köln (Prüfungsformen, Dauern, Rahmenplan über DIHK-Verlag); DIHK-Fortbildungsstatistik 2024/2025; DIHK zum Urheberrecht an Prüfungsaufgaben (01, 05, 06).
- **Lernwissenschaft:** Rowland 2014, Dunlosky et al. 2013, Cepeda et al. 2006/2008, Brunmair & Richter 2019, Renkl & Atkinson 2003, Kalyuga et al. 2003, Sinha & Kapur 2021, Wisniewski/Zierer/Hattie 2020, Tannenbaum & Cerasoli 2013, Wouters et al. 2013, Sailer & Homner 2020, Butterfield & Metcalfe 2001; FSRS/Anki-Doku, ts-fsrs (03, 04).
- **Domäne:** Destatis, UBA, Lebensmittel Praxis, LZ, Meininger, about-drinks, Gedat, BV GFGH-Mediadaten; BFH I R 36/07 und I R 33/11; BMF 05.11.2013; BGH VIII ZR 135/00; Toll Collect/DSLV-Maut; ADAC-Dieselpreis 7.10.2026; Kabinettsbeschluss Zuckersteuer 14.10.2026 (PwC, Tageskarte); MiLoV5 (02, 07, 08).
- **Technik:** npm-Registry 19.10.2026 (Angular 22.2.3, ts-fsrs 5.4.2, Dexie 4.4.6, ECharts 6.1.0, exceljs 4.4.0 u. a.), Lizenztexte Handsontable/PrimeNG/Jspreadsheet, Cloudflare/GitHub-Pages-Limits (04).
- **Markt:** TOPSIM, Celemi, Cesim, Capsim, HBP, MARGA, „Topsim Getränkemarkt“ (Landesbildungsserver BW), Fachwirt-Apps, Supermarket Simulator (05).
- **Rechnungen:** 08-Modell `scripts08/model08.py` mit Generatoren (94 Prüfungen laut 08) und `scripts-final/final.py` (Hausmarke, Konzern-Delta, Szenen, Make-or-Buy, Kennzahlen); Prüfungen der Gutachten in `review/check.py`.
