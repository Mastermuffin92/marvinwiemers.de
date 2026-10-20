# 08 – Großhandel als Kulisse: Prüfung von 07, Startbetrieb „Getränkegruppe“, Modul-Mapping und Bewertung (Stand Oktober 2026)

Antwort auf die Frage: „Wäre ein Getränke-Großhandel auch eine Option? Mit Leergut, Vollgut, Wareneinkauf usw.?“

Sicherheitsstufen: **[sicher]** amtlich, mehrfach belegt oder per Skript nachgerechnet · **[wahrscheinlich]** einzelne Fachquelle, Suchauszug oder starke Ableitung · **[Vermutung]** Lücke mit Branchenlogik gefüllt. **Alle Betriebszahlen des Startbetriebs (Abschnitt 2) sind Annahmen [Vermutung].** Ihre Summen, Salden und Abstimmungen sind per Skript geprüft (Abschnitt 2.16). Beträge in T€, sofern nicht anders angegeben; Rundungsdifferenzen in der letzten Stelle sind möglich, die Prüfungen laufen auf ungerundeten Werten.

**Quellenlage:** Die Websuche lief. Belegt wird nur über Suchauszüge, ganze Seiten habe ich nicht abgerufen. Öffentliche Betriebsvergleiche für GFGH, Abholmärkte und Keltereien fehlen weiter. Destatis führt den Getränkegroßhandel als WZ 46.34, die Werte liegen bei Statista hinter einer Bezahlschranke **[wahrscheinlich]**. Neu belegt gegenüber 07: DSLV-Mauttabelle für 12–18 t, ADAC-Dieselpreis und Tankrabatt, Kabinettsbeschluss zur Zuckersteuer, Mostobstpreise 2024/2025, Keltermenge 2025 und die Einschätzung des Bundeskartellamts zur Direktbelieferung durch Hersteller.

---

## 0. Kurzantwort

1. **Ja, und zwar als GFGH mit eigenen Abholmärkten.** Für das Ziel „Geprüfter Controller (IHK)“ ist das die stärkste der geprüften Kulissen **[Vermutung, Begründung in 3 und 4]**. Von 56 Modulen werden 6 neu natürlich spielbar (Verrechnungspreise, Konzern, IT- und Projektcontrolling; Plankosten nur mit Kelterei, Target Costing teilweise) und 28 deutlich besser (u. a. Prozesskosten je Stopp und Kolli, Kunden-DB, Covenants, Kreditrisiko, Fuhrpark-Investitionen, Steuercontrolling). Die Controller-Stelle kostet hier 21 % des Konzern-EBIT statt 51 % wie am Einzelmarkt (06).
2. **Startbetrieb (Abschnitt 2):** GmbH & Co. KG mit 17.500 T€ Großhandelsumsatz in fünf Segmenten (≈ 1.250 Geschäftskunden, davon 600 Gastronomie, dazu 900 Heimdienst-Haushalte), eine Märkte-GmbH mit drei Abholmärkten (4.500 T€, Markt 1 = Referenzmarkt aus 02 mit den Korrekturen aus 06) und optional eine Kelterei-GmbH (720,1 T€, davon 453,4 T€ an die KG). Konzern 2027: Außenumsatz 22.266,7 T€, EBIT 363,3 T€ (1,6 %), Ergebnis nach GewSt 166,1 T€, EK-Quote 26,4 % bei einem Covenant von 25 %, Nettoverschuldung/EBITDA 3,01 bei einem Covenant von 3,5 (beide Covenants sind Annahmen). Der Kapitaldienst ist nicht aus dem Cashflow gedeckt, der Kontokorrent steigt im Plan um 142,9 T€. Das ist gewollt: eine knappe, aber tragfähige Startlage.
3. **07 ist brauchbar, aber nicht fehlerfrei (Abschnitt 1).** Die Arithmetik stimmt. Es fehlen Fahrerdeckung, eine Finanzrechnung und eine saubere Abgrenzung des Referenzmarkts; zwei Befunde verschieben die Märkte-Ökonomie deutlich (G19, G20).
4. **Preis:** Mehr Bauaufwand (Schätzung +80–130 PT gegenüber dem Einzelmarkt, mit Kelterei +25–40 PT) **[Vermutung]**, ein schwererer Einstieg (B2B, Leergut-Mechanik) und eine noch dünnere Datenlage. Gegenmittel: Einstieg über Markt 1, Großhandel aggregiert nach Kundenklassen simulieren, Kelterei als Herbst-Fallstudie statt als Dauersimulation.
5. **Empfehlung (Abschnitt 4):** GFGH mit Märkten als Kulisse, Spieljahr 1 im Markt 1 und in der Zentrale, Kelterei erst als Erweiterung. Das Datenmodell sollte von Anfang an mehrere Gesellschaften, Kostenstellen und Innenleistungen kennen, auch wenn der erste Prototyp nur Markt 1 zeigt.

---

## 1. Prüfung von 07: Widersprüche und unplausible Zahlen

Nachgerechnet per Python-Skript (alle Tabellen in 07, Abschnitte 1–11). Die Rechenwege in 07 stimmen bis auf Rundung. Die Befunde betreffen Mengengerüste, Bezugsbasen und fehlende Rechnungen.

| Nr. | Stelle in 07 | Befund (nachgerechnet) | Korrektur im Startbetrieb | Stufe |
|---|---|---|---|---|
| G1 | 1.4, 11.1 | „13 Lkw und 3 Transporter“; Tabelle 5.2 hat 8 + 1 + 1 = 10 Lkw | 10 Lkw + 3 Transporter = 13 Fahrzeuge; Startbetrieb: 11 Lkw + 4 Transporter | sicher |
| G2 | 5.2 | Spalte T€/Jahr enthält nicht ausgewiesene Unterhaltskosten (Versicherung, Kfz-Steuer, Wartung, Reifen): 11,1 / 6,5 / 16,0 / 3,3 T€ je Fahrzeug. Tabellensumme 667,6 T€ gegen 678 T€ Sachkosten Fuhrpark | Unterhalt als eigene Spalte (2.3) | sicher |
| G3 | 5.2, 5.3, 11.2 | 11 CE-Fahrer × 210 Einsatztage = 2.310 Fahrertage für 2.500 Lkw-Tage. Gastro (1.687,5 Tourtage), Märkte (234) und Sattelzug (250) brauchen schon 2.171,5, dazu kommen die Wiederverkäufer | 12,5 VZÄ CE für 2.370 Tourtage plus Sattelzug (Skript-Prüfung) | wahrscheinlich |
| G4 | 1.5 vs. 5.3 | „1–3 Stopps pro Woche“, aber 27.000 Stopps ÷ 600 Kunden ÷ 52 = 0,87 Stopps je Woche | Kundenklassen: A 2×/Woche, B 1×/Woche, C 30×/Jahr | sicher |
| G5 | 4.5 | 210 T€ ÷ 45 € = 4.667 Besuche. Der genannte Rhythmus (A 2×/Monat, B monatlich, C quartalsweise) ergibt bei 100/250/250 Kunden schon 6.400 Besuche = 288 T€ | Mix festgelegt: 4.520 Besuche, 41,81 €/Besuch | sicher |
| G6 | 4.6 | Kolli-Basis uneinheitlich: Kommissionierung impliziert 2.746 bzw. 672 Kolli, Leergut 2.687 bzw. 658 (−2 %). DB III Eckkneipe −453 statt −452 € | Kolli einmal festlegen (2.9) | sicher |
| G7 | 3.3 | Pfand 30 T€ für 1.200 Fässer = 25 €/Fass, 2.3 nennt 30 € als üblich → 36 T€ (Zinswirkung nur +0,03 T€) | Fasspfand einheitlich 30 € brutto = 25,21 € netto | sicher |
| G8 | 3.2 vs. 02 | Gastro zahlt 172,05 € je 50 l = 3,44 €/l netto. Im 02-Markt zahlt der Endkunde für das 30-l-Partyfass 3,33 €/l netto, der Markt kauft es für 2,60 €/l. Ein Gastro-Fasspreis über dem Endkundenpreis ist nur mit Finanzierungsanteil (Rückvergütung, Darlehen, Schanktechnik) erklärbar. Einen belastbaren Gastro-Fasspreis habe ich nicht gefunden | Als Lernfall nutzen („Warum ist das Partyfass im Markt billiger?“), Preis vor Verwendung fachlich prüfen | Vermutung |
| G9 | 5.2, 10 | Diesel-Plan 1,95 €/l netto liegt unter dem Niveau ohne Steuersenkung: 2,233 ÷ 1,19 + 0,1404 = 2,02 €/l. Das Ereignis „Ende Tankrabatt +14 T€“ fehlt damit im Plan oder zählt doppelt | Plan 2,00 €/l netto inklusive Rabattende, das Ereignis nur als Abweichung | sicher (Rechnung); ADAC-Wert sicher |
| G10 | 5.2 | Maut 12–18 t „≈ 25 ct [Vermutung]“. Die DSLV-Tabelle ab 12/2023 nennt für 12–18 t 24,0–35,2 ct/km je nach Klasse (Suchauszug) | 25 ct beibehalten, Stufe auf wahrscheinlich anheben | wahrscheinlich |
| G11 | 6 | Logistikquote 12,0 % bezieht sich auf 22,0 Mio. € inklusive Märkte, „56 % der Kosten nach Wareneinsatz“ auf Kosten ohne Märkte. Aus den GuV-Posten ist beides nicht exakt herleitbar; auf den GFGH-Umsatz ohne Märkte bezogen sind es ≈ 15 % | Eine Bezugsbasis; der Startbetrieb rechnet Prozesskosten je Segment | sicher |
| G12 | 2.1 | „0,46 €/Kasten = 45 % der Lagerkosten + Sortieranlage“: 0,45 × (473 + 330 + 100 + 65) + 60 = 495,6 T€ ÷ 1,2 Mio. = 0,41 €/Kasten | Leergutsatz aus der Kostenstelle herleiten (2.3) | sicher |
| G13 | 2.4 | „Silvester-Rückstau … ≈ 162 T€“ ist der Gesamtbestand. Der Stichtagseffekt (Überhang 35.000 Kästen × 2,70 €) beträgt 94,5 T€ | Überhang getrennt ausweisen (2.13) | sicher |
| G14 | 11.3 | DPO 32 Tage = (1.700 − 300) ÷ 16.242,5 × 365 setzt Bruttoverbindlichkeiten gegen den Netto-Wareneinsatz (Fehler E5 aus 06). Brutto gegen brutto ≈ 26 Tage | DPO brutto/brutto | sicher |
| G15 | 11.3 | KDF 1,42 = (Ergebnis + AfA − Entnahmen) ÷ (Zins + Tilgung). M50 (06) rechnet (JÜ + AfA + Zinsaufwand) ÷ (Zins + Tilgung) = 1,72 | Eine Bankformel (M50) | sicher |
| G16 | 11 | Plan-Cashflow fehlt. 270 + 440 − 100 Entnahmen − 300 Tilgung = 310 T€. Mit Reinvestition auf AfA-Niveau (440) und netto 100 T€ neuen Wirt-Darlehen bleiben ≈ −230 T€, der Kontokorrent steigt von 500 auf ≈ 730 T€ | Cashflow und Planbilanz (2.12) | wahrscheinlich |
| G17 | 11.2 | Zinsen 100 T€ auf 2.000 T€ ohne Tilgungseffekt (Ø-Saldo ergibt 92,5 T€). Zinssätze uneinheitlich: Kontokorrent 6 %, Vorkauf 8 %, kalkulatorisch 6 % | Ø-Salden; Kontokorrent 8 %, kalkulatorisch 6 % | sicher |
| G18 | 11.2, 9 | Ist der Geschäftsführer der Familien-KG zugleich Kommanditist, ist sein Gehalt Sondervergütung (§ 15 Abs. 1 Nr. 2 EStG) und erhöht den Gewerbeertrag. Bei 120 T€ sind das +16,8 T€ GewSt (Hebesatz 400 %) | GF = Kommanditist, 140 T€, +19,6 T€ GewSt (2.10) | wahrscheinlich |
| G19 | 7, 11.2 vs. 02 | Markt 1 soll der 02-Markt sein. 02 enthält aber Heimdienst (250 T€) und Festservice (100 T€), die im GFGH zu Segment D/E gehören, sowie Inhaber-GF und Büro im Personal. Zieht man Markt 1 (02: 355 T€) von 547,5 T€ ab, bleiben für Markt 2 und 3 (2,35 Mio. €) nur 192,5 T€ Personal = 8,2 % Personalquote | Markt 1 nur als Laden (2,15 Mio. €), Personal aus Stundenbedarf (2.4) | sicher |
| G20 | 7 | Interne Belieferung 296 T€ = 6,6 % des Märkteumsatzes, aber ohne Wareneingang, Lagerung und Beschaffungslogistik. Die Direktbelieferung eigener Märkte durch Brauereien fehlt, obwohl das Bundeskartellamt Direktbelieferung durch Hersteller als regional verbreitet beschreibt (Suchauszug) | Vollständige Prozesskosten (2.6), Strecke an Märkte als Entscheidungskarte | wahrscheinlich |
| G21 | 8 | 576 t Saft ≠ 576.000 l. Bei 1,048 kg/l sind es ≈ 549.600 l; die HK je Liter steigen um ≈ 5 % | Dichte ansetzen (2.5) | sicher (Rechnung); Dichte wahrscheinlich |
| G22 | 8 | Äquivalenzziffern auf 127,5 T€ Abfüllkosten für alle Linien, aber die Glaslinie allein kostet laut Maschinenstundensatz 1.200 h × 150,72 € = 180,9 T€ (96,9 T€ ohne Bediener). Das Mengengerüst fehlt; 0,160/0,401/0,064 €/l passen nur zu 400.000 l Glas 1,0 l, 100.000 l 0,2 l und 364.000 l BiB inklusive Lohnmost | BAB mit Mengengerüst (2.5) | sicher |
| G23 | 1.2, 6 | Umsatz je Kopf 259 T€ (22.000 ÷ 85) gegen 558 T€ Branchenmittel je Kopf | Abstand erklären: gastronomielastig, eigene Märkte, wenig Strecke; der Mittelwert ist durch Großlogistiker verzerrt | wahrscheinlich |

**Bestätigt [sicher, nachgerechnet]:**
- Konditionskaskade: 126,72 → 120,39 €/Fass, RE 26,3 % bzw. 30,0 %; Biersteuer 4,53 €/Fass.
- Kunden und Touren: Mindestbestellwert 114 €; Kunden-DB III 3.776 € bzw. −453 €, bei 14-tägiger Belieferung +380 €; Tourtag 464 €; 2,35 € Logistik je Gastro-Kolli = 13 %.
- Fuhrpark: 100.360 l Diesel, 52,7 T€ Maut.
- GuV und Bilanz: EBIT 416,3, EBT 322,3 und GewSt 52,3 T€ (mit Freibetrag 24,5 T€ und Hebesatz 400 %); Bilanz 7.306 T€ auf beiden Seiten, EK-Quote 26,0 % bzw. 28,5 %.
- Verrechnungspreise: Summe in allen drei Varianten −79,7 T€, Schließungswirkung −164 T€.
- Kelterei: Maschinenstundensatz 80,72 €/h, Beschäftigungsabweichung 36 T€.
- Prüfungspflicht: Umsatz und Beschäftigte liegen über den Schwellen, das trägt die Aussage.

**Folgerung:** 07 taugt als Domänenbeschreibung. Keiner der Befunde kippt die Grundaussage. G19 und G20 machen die eigenen Märkte aber deutlich schwächer, als 07 sie zeigt. Der Startbetrieb unten rechnet deshalb alles neu, statt 07 zu flicken.

---

## 2. Startbetrieb „Getränkegruppe“ (Planjahr 2027)

### 2.1 Struktur und Rollen

| Gesellschaft | Verhältnis | Inhalt | Außenumsatz 2027 | VZÄ |
|---|---|---|---|---|
| {NAME} Getränke GmbH & Co. KG (Mutter) | Organträger, Familie hält alle Kommanditanteile | GFGH: Gastronomie, Wiederverkäufer, Strecke, Objekt/Heimdienst, Veranstaltungen; Zentrale mit Einkauf, Lager, Fuhrpark und Verwaltung | 17.500,0 | 49,0 |
| {NAME} Getränkemärkte GmbH | 100 %, Ergebnisabführungsvertrag (EAV) und Organschaft seit 2020 | 3 Abholmärkte, Markt 1 = Referenzmarkt aus 02 | 4.500,0 | 16,2 |
| Kelterei {NAME} GmbH (optional) | 100 %, gekauft zum 1.1.2025 für 330 T€ (EK 300, Geschäftswert 30), EAV und Organschaft | Kelterei mit Lohnmosterei, Hausmarke Apfelsaft | 266,7 (+ 453,4 an die KG) | 4,5 |
| Besitzgesellschaft der Familie | Schwester, nicht konsolidiert (Betriebsaufspaltung) | vermietet Lager (330 T€) und Kelterei-Halle (36 T€) | – | – |

- **Konzernabschluss:** Die KG ist Mutterunternehmen (§ 290 HGB), wegen ihrer Größe aber nach § 293 HGB befreit **[wahrscheinlich]**. Die Hausbank verlangt eine Konzernrechnung, weil die Covenants auf Konzernebene gelten **[Annahme]**. Die Konsolidierung ist also Management- und Bankrechnung, kein Pflichtabschluss.
- **Prüfungspflicht:** Die KG überschreitet alle drei Schwellen kleiner Gesellschaften: Bilanzsumme 7,63 Mio. € > 7,5 Mio. €, Umsatz 20,7 Mio. € > 15 Mio. €, ≈ 58 Köpfe > 50. Sie ist mittelgroß und über § 264a HGB prüfungspflichtig **[wahrscheinlich]**. Die beiden GmbHs sind klein. Gruppe gesamt ≈ 100 Köpfe.
- **Steuern:** Wegen der Organschaft zahlen die GmbHs weder KSt noch GewSt. Ihr Gewerbeertrag wird der KG zugerechnet, ihr Einkommen über die KG den Kommanditisten (ESt) **[wahrscheinlich]**. Annahme: Der Hinzurechnungsfreibetrag von 200 T€ gilt je Gesellschaft **[Vermutung, mit Steuerberatung prüfen]**.
- **Rollen:** Der Spieler ist Controller der Gruppe (Stabsstelle der Geschäftsführung, 75 T€ = 20,6 % des Konzern-EBIT). Figuren: Geschäftsführer (Kommanditist, 2. Generation), Logistikleiter, Marktleiterin Markt 1 (Sabine, bisher stellvertretende Marktleitung, vgl. 06 F18), Kellermeister, Außendienst, Hausbank, Abschlussprüfer.

### 2.2 Wichtigste Annahmen und übernommene Korrekturen

| Thema | Annahme im Startbetrieb | Herkunft |
|---|---|---|
| Kalender 2027 | 254 Liefertage (Mo–Fr), 304 Öffnungstage (Mo–Sa), NRW-Feiertage per Skript; Lkw 250, Fahrer 210 Einsatztage | 06 F1, 07 |
| Diesel | 2,00 €/l netto, Tankrabatt-Ende eingerechnet | G9; ADAC 7.10.2026 [sicher] |
| Maut | 12–18 t: 25 ct/km auf 50 % der km; Sattelzug 34,8 ct auf 85 %; 7,5 t 17,7 ct | G10 [wahrscheinlich] |
| Pfand | Sätze brutto (3,10 / 3,30 / 2,40 / 30 €), Bilanz netto (÷ 1,19), Palette 10 € netto | 06 W4, Karte 32 |
| Pfand-Bilanzmodell | brutto: Erstattungsanspruch gegen Abfüller und Verbindlichkeit gegenüber bekannten Kunden | 06 W3/Karte 31, BFH I R 36/07 [wahrscheinlich] |
| Markt 1 | 02 ohne Heimdienst und Festservice (gehen in KG-Segmente D/E); Inhaber durch angestellte Marktleitung ersetzt, Büro zentral | G19, 06 F18 |
| Personal Märkte | Stundenbedarf je Woche ≤ bezahlte Stunden × 0,815 (6 Wochen Urlaub, 7 % Krankenstand) | 06 F6 |
| Saisonkräfte | Arbeitgeberfaktor 1,10 | 06 F16 |
| Kühlmöbel Markt 1 | Kauf Dezember 2027, AfA pro rata 278 € | 06 F7 |
| Einkaufsvorteil der Gruppe | Einstand = 94 % des Rechnungs-EK des Einzelmarkts (der 20-%-Bezug über einen fremden GFGH entfällt, Bündelung) | Vermutung |
| Verrechnungspreis Märkte | Einstand + 3 %, historisch gesetzt, nie nachkalkuliert | Vermutung |
| Nachvergütungen | 3 % auf Lager-Wareneinsatz, 1 % auf Strecke, keine auf Kelterei-Bezug | 07 3.4 |
| Löhne 2027 | Mindestlohn 14,60 €, Minijob 633 €; SV-Faktor 1,245 (Sätze 2026) | 02/06 [sicher]; Faktor Annahme |
| Zinsen | Kontokorrent 8 %, Betriebsmitteldarlehen 5 %, Akquisitions- und Kelterei-Darlehen 4,5 %, kalkulatorisch 6 %, Wirt-Darlehen 3 % | G17 |
| Gewerbesteuer | Hebesatz 400 % (NRW-Kreisstädte liegen oft höher), Freibetrag 24,5 T€ für die KG | Vermutung |
| Zuckersteuer | nicht im Plan; Kabinett 14.10.2026: 26 ct/l (5–8 g) bzw. 32 ct/l (ab 8 g Zucker je 100 ml) ab 1.7.2027, Bundestag offen → Ereigniskarte | [wahrscheinlich, Suchauszüge PwC, Tageskarte] |


### 2.3 Großhandel (KG)

**Segmente und Kunden**

| Segment | Kunden | Umsatz | RE I | RE-Quote | Aufträge/Stopps | Kolli | DSO (Tage) |
|---|---|---|---|---|---|---|---|
| A Gastronomie | 600 (60 A, 200 B, 340 C) | 9.500,0 | 3.135,0 | 33,0 % | 27.000 | 526.500 | 25 |
| B Wiederverkäufer | 150 Fremdmärkte, Kioske, Tankstellen | 3.000,0 | 450,0 | 15,0 % | 3.000 | 250.000 | 20 |
| C Strecke (LEH, Großkunden) | 25 | 2.500,0 | 112,5 | 4,5 % | 1.500 | 0 | 30 |
| D Objekt/Heimdienst | 300 Objekte + 900 Haushalte | 1.500,0 | 506,4 | 33,8 % | 21.000 | 160.000 | 21 |
| E Veranstaltungen | ≈ 180 Auftraggeber, 350 Feste | 1.000,0 | 424,0 | 42,4 % | 350 | 57.000 | 14 |
| F Märkte (intern) | 3 Märkte | 3.178,4 | 92,6 | 2,9 % | 364 | 386.208 | 14 |
| **Summe** |  | **20.678,4** | **4.720,5** | 22,8 % | 53.214 | 1.379.708 |  |

Segment D enthält 60 T€ Liefergebühren, E 200 T€ Miete und Service (Rohertrag 100 %). Die RE-Quoten liegen in den Spannen aus 07 1.5 **[Vermutung]**.

| Gastro-Klasse | Kunden | Ø Umsatz T€ | Stopps/Jahr | Außendienstbesuche/Jahr |
|---|---|---|---|---|
| A-Kunden (Brauhaus, Hotel) | 60 | 50,0 | 104 | 24 |
| B-Kunden (Restaurant, Kneipe) | 200 | 20,0 | 52 | 12 |
| C-Kunden (Eckkneipe, Verein) | 340 | 7,4 | 30 | 2 |
| Summe | 600 | 15,8 | 26.840 | 4.520 |

Die Klassen ergeben 26.840 Regelstopps; die Differenz zu 27.000 sind Nach- und Sonderlieferungen. Darlehen an Wirte 1.200 T€ (≈ 80 Kunden, Ø 15 T€, 3 % Zins), Leihinventar Restbuchwert 900 T€ (wie 07).

**Fuhrpark (Kosten je Jahr ohne Fahrer)**

| Fahrzeug | Anz. | Leasing €/Monat | km/Jahr | l/100 km | Maut | Leasing | Diesel | Maut T€ | Unterhalt | T€ je Fz. | T€ gesamt |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 18-t-Lkw (Verteilung) | 9 | 2.300 | 30.000 | 28 | 50 % × 25,0 ct | 27,6 | 16,8 | 3,8 | 11,0 | 59,2 | 532,4 |
| 7,5-t-Lkw (Innenstadt) | 1 | 1.300 | 22.000 | 18 | 50 % × 17,7 ct | 15,6 | 7,9 | 1,9 | 6,5 | 32,0 | 32,0 |
| Sattelzug (Abholung, Leergut) | 1 | 3.200 | 70.000 | 31 | 85 % × 34,8 ct | 38,4 | 43,4 | 20,7 | 16,0 | 118,5 | 118,5 |
| Transporter < 3,5 t (Objekt, Heimdienst, Feste) | 4 | 650 | 25.000 | 10 | mautfrei | 7,8 | 5,0 | 0,0 | 3,3 | 16,1 | 64,4 |
| **Summe** | 15 |  |  |  |  | 333,6 | 222,5 | 56,4 | 134,7 |  | **747,2** |

Diesel 111.260 l/Jahr; ±30 ct/l = ±33,4 T€. Scope 1 ≈ 295 t CO₂ (2,65 kg/l **[wahrscheinlich]**). Tourtage der Verteiler-Lkw: Gastro 1.588,2 (17 Stopps je Tour), Wiederverkäufer 500,0 (6 Stopps), Märkte 182,0 (½ Tourtag je Anlieferung), Feste 100,0 → 2.370,2 von 2.500 Kapazitätstagen = 94,8 % Auslastung. Die freie Kapazität (29,3 T€ Leerkosten) ist Reserve für Ausfälle und Spitzen.

**Personal KG**

| Funktion | VZÄ | T€ je VZÄ (AG-Kosten) | T€ |
|---|---|---|---|
| Fahrer CE (Lkw, Sattelzug) | 12,5 | 48,0 | 600,0 |
| Fahrer B (Transporter) | 5,0 | 40,0 | 200,0 |
| Beifahrer Gastro | 1,5 | 34,0 | 51,0 |
| Lager, Kommissionierung, Leergut | 11,0 | 43,0 | 473,0 |
| Innendienst/Disposition | 5,0 | 45,0 | 225,0 |
| Außendienst Gastro | 3,0 | 70,0 | 210,0 |
| Schanktechnik | 1,5 | 55,0 | 82,5 |
| Veranstaltungsservice (Leitung) | 1,0 | 42,0 | 42,0 |
| Saisonkräfte (Feste, Silvester) | 1,0 | 40,0 | 40,0 |
| Verwaltung (Buchhaltung 2,5, Lohn 1, IT 1) | 4,5 | 50,0 | 225,0 |
| Controller | 1,0 | 75,0 | 75,0 |
| Logistikleiter | 1,0 | 95,0 | 95,0 |
| Geschäftsführer (Kommanditist) | 1,0 | 140,0 | 140,0 |
| **Summe** | **49,0** |  | **2.458,5** |

Fahrerbedarf CE: (2.370,2 + 250) ÷ 210 = 12,48 VZÄ, B-Fahrer: 4 × 250 ÷ 210 = 4,76 VZÄ (beides skriptgeprüft). Personalquote KG 14,0 % des Außenumsatzes.

**Lager, Leergut und Prozesskostensätze**

5.000 m² Halle und 5.000 m² Hof (wie 07), gemietet von der Besitzgesellschaft. Kostenstellen-Pools aus Lagerpersonal, Miete/Nebenkosten, Lagertechnik, Sortieranlage, Lager-AfA, Entsorgung und Leergutdifferenzen; Schlüssel in der Skriptdatei. Märkte-Lieferungen werden bei Lagerung und Beschaffung mit 0,7 gewichtet (Schnelldreher, teils Durchschleusen), Märkte-Leergut mit 0,8 (vom Automaten vorsortiert), Märkte-Kolli in der Kommissionierung mit 0,35 (Lagen und Ganzpaletten), Wiederverkäufer mit 0,6 **[Vermutung]**.

| Prozess / Kostenstelle | Kosten T€ | Bezugsgröße | Satz |
|---|---|---|---|
| Wareneingang/Lagerung | 377,8 | 1.263.845 gewichtete Kolli | 0,30 €/Kolli |
| Kommissionierung | 333,6 | 1.028.673 gewichtete Kolli | 0,32 €/Kolli |
| Leergut inkl. Differenzen (brutto) | 455,1 | 1.012.500 gewichtete Kästen | 0,45 €/Kasten |
| Leergut nach Sortiervergütung (netto) | 358,0 | Sortiervergütung 97,2 T€ (0,09 €/Kasten) | 0,35 €/Kasten |
| Beschaffung Sattelzug (nach Abholvergütung 60 T€) | 115,6 | 1.263.845 gewichtete Kolli | 0,09 €/Kolli |
| Verteiler-Lkw je Kapazitätstag | 564,3 | 2.500 Lkw-Tage | 225,73 €/Tag |
| Fahrer CE je Einsatztag | 48 T€ ÷ 210 |  | 228,57 €/Tag |
| Tourtag (Lkw + Fahrer) |  |  | 454,30 € |
| Gastro-Stopp (Tourtag ÷ 17 + Beifahrer) |  |  | 28,61 € |
| Auftragsabwicklung (Innendienst + 50 % IT) | 295,0 | 53.214 Aufträge | 5,54 €/Auftrag |
| Außendienstbesuch (90 % Gastro) | 189,0 | 4.520 Besuche | 41,81 €/Besuch |

**Abgeleitet:** Gastro-Stopp inklusive Auftrag 34,16 € (07: 32 €), Logistik je Gastro-Kolli 2,73 € = 15,2 % des Kolliwerts von 18,04 € (07: 2,34 € = 13 %), Mindestbestellwert für DB = 0: 34,16 ÷ (33 % − 5,6 %) = **125 €** (07: 114 €). Leergut 1.079.500 Kästen und 11.000 Fässer im Jahr, ≈ 4.250 Kästen je Liefertag.

### 2.4 Abholmärkte (Märkte GmbH)

| Kennzahl | Markt 1 | Markt 2 | Markt 3 | Summe |
|---|---|---|---|---|
| Verkaufsfläche / Gesamtfläche m² | 900 / 1.350 | 600 / 900 | 450 / 700 | 1.950 / 2.950 |
| Öffnungszeiten | Mo–Sa 8–20 (72 h) | Mo–Fr 9–19, Sa 8–18 (60 h) | Mo–Fr 9–19, Sa 9–16 (57 h) |  |
| Umsatz netto | 2.150,0 | 1.350,0 | 1.000,0 | 4.500,0 |
| Bons / Kunden je Tag (304 Tage) | 100.000 / 329 | 67.500 / 222 | 52.600 / 173 | 220.100 |
| Ø Bon netto € | 21,50 | 20,00 | 19,01 |  |
| Umsatz je m² VK € | 2.389 | 2.250 | 2.222 | 2.308 |
| RE-Quote bei Fremdbezug (02-Basis) | 26,8 % | 27,5 % | 27,0 % |  |
| Einstand der Gruppe (94 %) | 1.479,6 | 920,0 | 686,2 | 3.085,8 |
| Wareneinsatz zum VP (Einstand + 3 %) | 1.524,0 | 947,6 | 706,8 | 3.178,4 |
| RE I auf VP | 626,0 (29,1 %) | 402,4 (29,8 %) | 293,2 (29,3 %) | 1.321,6 |
| − Inventurdifferenz 0,5 % | −10,8 | −6,8 | −5,0 | −22,5 |
| − Personal | −304,3 | −208,5 | −166,7 | −679,6 |
| − Sachkosten | −242,6 | −149,8 | −111,3 | −503,7 |
| − Umlage Zentrale 1,5 % | −32,2 | −20,2 | −15,0 | −67,5 |
| − AfA | −20,3 | −14,0 | −10,0 | −44,3 |
| **EBIT (= Ergebnisabführung)** | **15,9** | **3,1** | **−14,8** | **4,1** |
| VZÄ / Personalquote | 7,18 / 14,2 % | 5,01 / 15,4 % | 4,01 / 16,7 % | 16,19 |
| Stunden je Woche: bezahlt / produktiv / Bedarf | 287 / 234 / 226 | 200 / 163 / 162 | 160 / 131 / 130 |  |
| Raumkostenquote (Miete + NK) | 6,6 % | 5,8 % | 5,5 % |  |

Personal je Markt aus Dienstplan (Auszug Markt 1): Marktleitung (angestellt, statt Inhaber) 55,3 T€; Stellv. Marktleitung 47,6 T€; Verkauf/Lager Vollzeit (2) 81,5 T€; Kasse Teilzeit 25 h 24,3 T€; Verkauf Teilzeit 20 h (neu, 06 F6) 19,4 T€; Azubi 2. Lj. (50 % im Markt) 16,1 T€; 5 Minijobber à 600 € 47,5 T€; Saison Mai–Aug (2), Faktor 1,10 (06 F16) 12,7 T€.

Stundenbedarf Markt 1 (produktiv je Woche): Kasse 72 h + Zweitkasse Fr 4 / Sa 8 84 h, Fläche/Leergut 72 h + Fr 6 / Sa 10 88 h, Warenannahme/Verräumen 24 h, Marktleitung Büro/Dispo 20 h, Reinigung, MHD, Inventur 10 h = 226 h. Damit ist die Personallücke F6 aus 06 für den Laden geschlossen. Die 330 h in 02 enthielten Heimdienst und Büro.

**Markt 1: 02-Einzelmarkt gegen Filiale in der Gruppe**

| Position | 02 (Einzelmarkt, GmbH) | Gruppe 2027 (Filiale) | Grund |
|---|---|---|---|
| Umsatz | 2.500,0 (Laden 2.150, Heimdienst 250, Fest 100) | 2.150,0 | Heimdienst und Festservice gehen in KG-Segmente D/E |
| Rohertrag | 749,3 = RE II 30,0 % | 626,0 = RE I 29,1 % auf VP | Einkaufsvorteil 6 %, VP-Aufschlag 3 %; Boni fallen in der KG an |
| Personal (VZÄ) | 355,4 (8,12) inkl. Inhaber 60,6 und Büro 25,9 | 304,3 (7,18) | angestellte Marktleitung, Büro zentral, +0,5 VZÄ (F6), Saison ×1,10 |
| Sachkosten | 317,4 inkl. Fuhrpark 37 und Steuerberatung 15 | 242,6 | Fuhrpark in der KG, Gruppenverträge (IT, Versicherung, Marketing) |
| Umlage Zentrale | – | 32,2 | ersetzt Büro, Steuerberatung, Verbundbeitrag |
| AfA | 26,0 (Festservice-Inventar 6) | 20,3 | Festservice-Inventar in der KG; Kühlmöbel pro rata (F7) |
| EBIT | 50,5 | 15,9 | Laden allein ist knapp; 02 lebte vom Service-DB |
| Kunden je Tag | 327 (306 Tage) | 329 (304 Tage) | F1 |


### 2.5 Kelterei (optional)

| Mengengerüst | Wert |
|---|---|
| Obst eigener Zukauf / Lohnmost | 800 t zu 150 €/t / 400 t |
| Saftausbeute, Dichte | 72 %, 1,048 kg/l |
| Saft eigen / Lohnmost | 549.618 l / 274.809 l |
| Trester | 336 t (Erlös 15 €/t, Abholung 8 €/t) |
| Abfüllung eigen | Glas 1,0 l 350.000 l, Glas 0,2 l 100.000 l, BiB 5 l 99.618 l |
| Flaschen / BiB | 850.000 Flaschen, 74.885 BiB |
| Laufzeit Glaslinie | 1.200 h ≈ 708 Flaschen/h |

Mostobstpreis: VdF-Durchschnitt 2024 28 €/100 kg, Bio 40 € **[wahrscheinlich]**. Für 2025 meldet der Streuobst-Infobrief Oberfranken deutlich niedrigere Preise ohne Zahl **[wahrscheinlich]**. Für 2026 habe ich keine Zahl gefunden. Der Plan setzt 15 €/100 kg (Niedrigpreisjahr) **[Vermutung]**, das Ereignis „Missernte“ 28 €/100 kg. Keltermenge Deutschland 2025 ≈ 216,5 Mio. l Apfelsaft **[wahrscheinlich, Meininger-Suchauszug]**.

| Produkt | Liter an KG | Liter extern | VP KG €/l | Preis extern €/l | Umsatz T€ |
|---|---|---|---|---|---|
| Glas 1,0 l | 280.000 | 70.000 | 0,88 | 0,90 | 309,4 |
| Glas 0,2 l (Gastro) | 100.000 | 0 | 1,50 | 1,50 | 150,0 |
| BiB 5 l (eigen) | 60.000 | 39.618 | 0,95 | 1,20 | 104,5 |
| Lohnmost (Lohn inkl. BiB) | – | 274.809 | – | 0,55 | 151,1 |
| Trester | – | 336 t | – | 15,00 €/t | 5,0 |
| **Summe** |  |  |  |  | **720,1** (intern 453,4) |

Der Verrechnungspreis an die KG entspricht dem Preis an fremde Händler (marktorientiert) **[Annahme]**. Die KG verkauft die 0,2-l-Flaschen an die Gastronomie, das 1,0-l-Glas an Gastronomie, Objekte und die Märkte (162.000 l), BiB an Märkte und Heimdienst.

**Betriebsabrechnungsbogen (Primärkosten T€) und Herstellkosten**

| Kostenart | H1 Annahme | H2 Pasteurisieren | H3 Abfüllung Glas | H4 Abfüllung BiB | VV Verwaltung | Summe |
|---|---|---|---|---|---|---|
| Personal | 46,0 | 32,0 | 70,0 | 34,0 | 18,0 | 200,0 |
| Energie | 6,0 | 16,8 | 14,0 | 4,0 | – | 40,8 |
| Instandhaltung | 5,0 | 5,0 | 10,0 | 2,0 | – | 22,0 |
| Entsorgung | 8,7 | – | – | – | – | 8,7 |
| AfA | 25,0 | 28,0 | 45,0 | 6,0 | – | 104,0 |
| Miete | 10,0 | 12,0 | 10,0 | 4,0 | – | 36,0 |
| Hilfsstoffe | – | 12,0 | – | – | – | 12,0 |
| Labor | – | 8,0 | – | – | – | 8,0 |
| Versicherung | – | 6,0 | – | – | 2,0 | 8,0 |
| Sonstiges | – | – | – | – | 10,0 | 10,0 |
| Umlage_KG | – | – | – | – | 15,0 | 15,0 |
| **Summe** | **100,7** | **119,8** | **149,0** | **50,0** | **45,0** | **464,5** |
| Bezugsgröße | 824.427 l | (mit H1) | 600.000 ÄZ-l | 374.427 l | – |  |

Einzelkosten: Obst (800 t × 150 €/t) 120,0; Verschlüsse, Etiketten (0,04 €/Fl.) 34,0; Glasersatz 2 % (0,30 €/Fl.) 5,1; BiB-Beutel/Karton eigen (0,85 €/5 l) 16,9; BiB-Beutel/Karton Lohnmost 46,7 T€. Sätze: Pressen und Tank 0,2613 €/l (nach Trester-Gutschrift 5,0 T€, Restwertmethode), Glasabfüllung 0,2483 € je Äquivalenzliter (1,0 l = 1,0; 0,2 l = 2,5), BiB 0,1335 €/l, Obst 0,2183 €/l eigener Saft.

| Produkt (€/l) | Obst | Pressen/Tank | Abfüllung | Verpackung | HK | VP bzw. Preis | Spanne vor VV |
|---|---|---|---|---|---|---|---|
| Glas 1,0 l | 0,218 | 0,261 | 0,248 | 0,046 | **0,774** | 0,88 | 12,0 % |
| Glas 0,2 l (Gastro) | 0,218 | 0,261 | 0,621 | 0,230 | **1,330** | 1,50 | 11,3 % |
| BiB 5 l (eigen) | 0,218 | 0,261 | 0,134 | 0,170 | **0,783** | 0,95 | 17,6 % |
| Lohnmost (BiB) | 0,000 | 0,261 | 0,134 | 0,170 | **0,565** | 0,55 | −2,7 % |

Herstellkosten nach § 255 Abs. 2 HGB mit angemessenen Gemeinkosten und Werteverzehr, ohne Verwaltung und Vertrieb (Wahlrecht nicht genutzt) **[sicher als Rechtsrahmen]**. Abstimmung: Σ HK × Menge = 637,2 T€ = Einzelkosten + Fertigungsstellen − Trester (Skript). **Lohnmost:** Preis 0,55 €/l liegt unter den Vollkosten von 0,56 €/l, aber über den variablen Kosten von ≈ 0,17 €/l (DB 0,38 €/l, 104,4 T€) **[Vermutung]**. Teilkosten- gegen Vollkostensicht als Lernfall.

**Maschinenstundensatz Glaslinie (kalkulatorisch):** kalk. AfA (WBW 540 / 12 J.) 45,0 + kalk. Zins (6 % × AHK/2 = 240) 14,4 + Raum (Miete-Anteil) 10,0 + Instandhaltung 10,0 + Energie 14,0 = 93,4 T€ ÷ 1.200 h = **77,83 €/h**, mit Bedienern (70 T€) **136,17 €/h**. Bilanzielle AfA 40 T€ gegen kalkulatorische 45 T€ (Anderskosten, M04). **Beschäftigungsabweichung** bei 700 statt 1.200 h: 135,0 T€ Fixkosten × (1 − 700/1.200) = **56,2 T€**. **Missernte** (28 statt 15 €/100 kg): +104,0 T€ Obstkosten, Kelterei-EBIT −71,1 T€.

### 2.6 Verrechnungspreise und interne Leistungen

| Leistung | Regel (Start) | Plan 2027 |
|---|---|---|
| Ware KG → Märkte | Einstand + 3 %, Pfand zum Pfandsatz, Leergut bei jeder Anlieferung zurück | 3.178,4 |
| Saft Kelterei → KG | Preis an fremde Händler | 453,4 |
| Umlage Zentrale → Märkte / Kelterei | 1,5 % vom Umsatz / pauschal 15 T€ | 67,5 / 15,0 |
| Cash-Pool KG → Märkte | zinslos (in der Organschaft steuerlich unkritisch [wahrscheinlich]) | 150,0 |
| Interne Logistik (Anlieferung, Lager, Leergut) | nicht gesondert berechnet, „im Aufschlag enthalten“ | 328,8 Kosten |

| Interne Logistik je Markt | Lagerung | Kommiss. | Leergut | Beschaffung | Anlieferung | Auftrag | Summe | % Marktumsatz |
|---|---|---|---|---|---|---|---|---|
| M1 | 38,7 | 21,0 | 45,3 | 11,9 | 35,4 | 0,9 | 153,2 | 7,1 % |
| M2 | 24,1 | 13,1 | 28,3 | 7,4 | 23,6 | 0,6 | 97,0 | 7,2 % |
| M3 | 18,0 | 9,7 | 21,2 | 5,5 | 23,6 | 0,6 | 78,6 | 7,9 % |
| Summe | 80,8 | 43,8 | 94,8 | 24,7 | 82,7 | 2,0 | 328,8 | 7,3 % |

**Varianten des Verrechnungspreises (T€).** Märkte = EBIT der Märkte; KG-Anteil = VP-Aufschlag + Nachvergütung auf Märkte-Einstand − Inventurdifferenz − interne Logistik − Marketing-Anteil; Summe = Gruppenbeitrag des Marktes vor Overhead, aber nach Umlage.

| Variante (Märkte / KG-Anteil) | Markt 1 | Markt 2 | Markt 3 | Märkte gesamt | Summe Gruppe |
|---|---|---|---|---|---|
| a) Einstand | 60,3 / −121,3 | 30,7 / −77,3 | 5,7 / −63,9 | 96,7 / −262,5 | −165,8 |
| b) Einstand + 3 % (Startregel) | 15,9 / −77,0 | 3,1 / −49,7 | −14,8 / −43,3 | 4,1 / −169,9 | −165,8 |
| c) Einstand + interne Logistik (Vollkosten) | −92,9 / 31,8 | −66,4 / 19,8 | −72,9 / 14,8 | −232,2 / 66,4 | −165,8 |
| d) Marktpreis wie Wiederverkäufer (RE 15 %) | −200,8 / 139,8 | −131,7 / 85,1 | −115,4 / 57,2 | −447,9 / 282,1 | −165,8 |

Die Summe bleibt in jeder Variante gleich (Skriptprüfung). Gruppensicht vor Overhead: −165,8 T€ einschließlich Umlage, −98,3 T€ ohne Umlage (diese deckt Overhead der KG). Unter der Startregel weist die Märkte GmbH 4,1 T€ aus, Markt 3 −14,8 T€. Unter Marktpreis-VP sehen alle Märkte wie Wertvernichter aus.

| Schließung (Gruppenwirkung T€) | Markt 1 | Markt 2 | Markt 3 |
|---|---|---|---|
| entgangener Rohertrag + NV − Inventurdifferenz | −696,3 | −446,0 | −325,8 |
| ersparte Personal- und Sachkosten | 546,9 | 358,3 | 278,1 |
| ersparte Logistik: Kommissionierung, Leergut, Anlieferung, Auftrag zu 50 % | 51,3 | 32,8 | 27,6 |
| ersparter Marketing-Anteil | 4,8 | 3,0 | 2,2 |
| **Wirkung bei 50 % Logistikabbau** | **−93,3** | **−51,9** | **−17,9** |
| Wirkung bei 100 % Logistikabbau | −42,0 | −19,1 | 9,7 |

Umlage, Lagerung und Beschaffung gelten als fix, die Markt-AfA ist versunken. **Lernpunkt:** Markt 3 ist schon unter der Startregel negativ, unter kostendeckendem VP deutlich. Ob eine Schließung hilft, hängt allein davon ab, wie viel Logistik wirklich abbaubar ist (bei 50 % schadet sie mit −17,9 T€, bei 100 % bringt sie 9,7 T€). Das ist eine Frage an den Logistikleiter, keine Rechenfrage.

### 2.7 Plan-GuV 2027 je Gesellschaft und Konzern (T€)

| Position | KG | Märkte GmbH | Kelterei GmbH | Konsolidierung | Konzern mit Kelterei | Konzern ohne Kelterei |
|---|---|---|---|---|---|---|
| Umsatzerlöse | 20.678,4 | 4.500,0 | 720,1 | −3.631,8 | 22.266,7 | 22.000,0 |
| davon Innenumsatz | 3.178,4 | 0,0 | 453,4 | −3.631,8 | 0,0 | 0,0 |
| − Wareneinsatz/Material | −15.957,9 | −3.178,4 | −234,8 | 3.631,8 | −15.739,3 | −15.957,9 |
| **= Rohertrag I** | **4.720,5** | **1.321,6** | **485,4** | **0,0** | **6.527,5** | **6.042,1** |
| − Kundenboni | −142,5 | 0,0 | 0,0 | 0,0 | −142,5 | −142,5 |
| + Nachvergütungen | 417,4 | 0,0 | 0,0 | 0,0 | 417,4 | 417,4 |
| − Inventurdifferenzen | −47,5 | −22,5 | 0,0 | 0,0 | −70,0 | −70,0 |
| + Sortier-, Abhol-, Depotvergütung, Umlage | 279,7 | 0,0 | 0,0 | −82,5 | 197,2 | 197,2 |
| − Personal | −2.458,5 | −679,6 | −200,0 | 0,0 | −3.338,1 | −3.138,1 |
| − Sachkosten | −2.038,7 | −503,7 | −133,5 | 0,0 | −2.675,9 | −2.542,4 |
| − Umlage Zentrale | 0,0 | −67,5 | −15,0 | 82,5 | 0,0 | 0,0 |
| **= EBITDA** | **730,3** | **48,4** | **136,9** | **0,0** | **915,6** | **763,7** |
| − AfA (Konsolidierung: Geschäftswert) | −401,0 | −44,3 | −104,0 | −3,0 | −552,3 | −445,3 |
| **= EBIT** | **329,3** | **4,1** | **32,9** | **−3,0** | **363,3** | **318,4** |
| − Zinsen (netto) | −117,4 | 0,0 | −25,6 | 0,0 | −143,1 | −99,9 |
| **= EBT vor Ergebnisabführung** | **211,9** | **4,1** | **7,3** | **−3,0** | **220,2** | **218,5** |
| − Gewerbesteuer (Organkreis, bei der KG) |  |  |  |  | −54,1 | −52,8 |
| **= Ergebnis vor ESt der Gesellschafter** |  |  |  |  | **166,1** | **165,6** |
| EBIT-Marge (auf Außenumsatz) | 1,9 % | 0,1 % | 4,6 % |  | 1,6 % | 1,4 % |

Die KG bucht zusätzlich die Ergebnisabführungen (4,1 + 7,3 T€) als Ertrag; sie werden konsolidiert. Die Variante „ohne Kelterei“ unterstellt, dass die KG denselben Saft zum selben Preis bei einer fremden Kelterei kauft; es entfallen Umlage (15 T€) und Akquisitionsdarlehen. **Die Kelterei bringt dem Konzern 1,8 T€ EBT**, aber Industrie-KLR (2.5) und Konsolidierungsstoff.

### 2.8 Segment-Deckungsbeitragsrechnung der KG (T€)

| Position | A Gastro | B Wiederverk. | C Strecke | D Objekt/HD | E Feste | F Märkte (intern) | Summe |
|---|---|---|---|---|---|---|---|
| Umsatz | 9.500,0 | 3.000,0 | 2.500,0 | 1.500,0 | 1.000,0 | 3.178,4 | 20.678,4 |
| RE I | 3.135,0 | 450,0 | 112,5 | 506,4 | 424,0 | 92,6 | 4.720,5 |
| − Kundenboni | −142,5 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | −142,5 |
| + Nachvergütungen | 185,0 | 75,9 | 23,9 | 28,4 | 17,1 | 87,2 | 417,4 |
| − Inventurdifferenz | −22,3 | −8,9 | 0,0 | −3,5 | −2,0 | −10,8 | −47,5 |
| **= RE II** | **3.155,2** | **516,9** | **136,4** | **531,3** | **439,1** | **168,9** | **4.947,9** |
| − Wareneingang/Lagerung | −157,4 | −74,7 | 0,0 | −47,8 | −17,0 | −80,8 | −377,8 |
| − Kommissionierung | −170,7 | −48,6 | 0,0 | −51,9 | −18,5 | −43,8 | −333,6 |
| − Leergut (netto) | −141,4 | −70,4 | 0,0 | −39,1 | −12,4 | −94,8 | −358,0 |
| − Beschaffung Sattelzug | −48,2 | −22,9 | 0,0 | −14,6 | −5,2 | −24,7 | −115,6 |
| − Auftragsabwicklung | −149,7 | −16,6 | −8,3 | −116,4 | −1,9 | −2,0 | −295,0 |
| − Touren/Transporter/Beifahrer | −772,5 | −227,1 | 0,0 | −198,3 | −111,5 | −82,7 | −1.392,2 |
| **= DB II nach Logistik** | **1.715,3** | **56,6** | **128,1** | **63,2** | **272,5** | **−159,9** | **2.075,7** |
| − Außendienst | −189,0 | −21,0 | 0,0 | 0,0 | 0,0 | 0,0 | −210,0 |
| − Schanktechnik | −110,2 | 0,0 | 0,0 | 0,0 | −12,2 | 0,0 | −122,5 |
| − Veranstaltungsservice | 0,0 | 0,0 | 0,0 | 0,0 | −173,0 | 0,0 | −173,0 |
| − AfA Leihinventar | −220,0 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | −220,0 |
| − Forderungs-/Darlehensausfälle | −71,5 | −3,0 | −2,5 | −1,0 | 0,0 | 0,0 | −78,0 |
| − Marketing | −40,0 | −10,0 | 0,0 | −25,0 | −15,0 | −10,0 | −100,0 |
| + Zinsertrag Wirt-Darlehen | 36,0 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 36,0 |
| **= DB III** | **1.120,5** | **22,6** | **125,6** | **37,2** | **72,3** | **−169,9** | **1.208,2** |
| DB III in % vom Umsatz | 11,8 % | 0,8 % | 5,0 % | 2,5 % | 7,2 % | −5,3 % | 5,8 % |

Überleitung: Σ DB III 1.208,2 − Overhead 965,4 (Verwaltung, Controller, Geschäftsführung, Logistikleitung, IT-Rest, Versicherung, Prüfung, Büro, Verbund, Sonstiges, IT-AfA, Leerkosten Lkw 29,3 und Fahrer 1,1) + Umlage und Depotvergütung 122,5 − Zinsertrag (gehört ins Finanzergebnis) 36,0 = **KG-EBIT 329,3** (Skriptprüfung). **Lernpunkte:** Gastro trägt die KG trotz Leihinventar und Außendienst; Wiederverkäufer und Objekt/Heimdienst liegen bei 1–3 %; die Strecke verdient ohne eigene Logistik relativ gut, hängt aber an 25 Kunden (Ereignis „LEH zieht Logistik an sich“); das interne Segment F ist klar negativ.

### 2.9 Kunden-Deckungsbeitrag mit den Prozesskostensätzen (€ pro Jahr)

| Stufe | Brauhaus: 60 T€, 104 Stopps, 2.750 Kolli, Darlehen 30 T€ | Eckkneipe: 12 T€, 52 Stopps, 670 Kolli | Eckkneipe 14-tägig: 26 Stopps |
|---|---|---|---|
| Umsatz netto | 60.000 | 12.000 | 12.000 |
| Rohertrag I | 18.000 | 4.200 | 4.200 |
| − Kundenbonus | −1.200 | 0 | 0 |
| **= DB I** | **16.800** | **4.200** | **4.200** |
| − Lagerung und Beschaffung | −1.074 | −262 | −262 |
| − Kommissionierung | −892 | −217 | −217 |
| − Leergut (0,85 Kästen je Kolli) | −826 | −201 | −201 |
| − Stopps inkl. Auftrag | −3.552 | −1.776 | −888 |
| **= DB II** | **10.456** | **1.744** | **2.632** |
| − Außendienstbesuche | −1.004 | −502 | −502 |
| − kalk. Zinsdifferenz Darlehen (6 % − 3 %) | −900 | 0 | 0 |
| − AfA Leihinventar | −4.000 | −1.500 | −1.500 |
| − Ausfallrisiko | −300 | −240 | −240 |
| **= DB III** | **4.252** | **−498** | **390** |
| DB III in % vom Umsatz | 7,1 % | −4,2 % | 3,2 % |

Gleicher Lernfall wie 07 4.6, jetzt aus den Kostenstellen abgeleitet. Die Zinsdifferenz ersetzt den vollen kalkulatorischen Zins aus 07, weil der Wirt 3 % zahlt und dieser Ertrag schon im Segment steht. Die AfA für vorhandenes Inventar ist für eine Kündigung versunken.

### 2.10 Gewerbesteuer im Organkreis und Entnahmen

| Position | T€ |
|---|---|
| EBT KG (ohne Ergebnisabführung) | 211,9 |
| + Tätigkeitsvergütung GF (Sondervergütung, § 15 Abs. 1 Nr. 2 EStG) | 140,0 |
| + Hinzurechnung KG: 25 % × (Zinsen 153,4 + 50 % Miete 330 + 20 % Leasing 363,0 − 200) | 47,8 |
| + EBT Märkte GmbH (Organgesellschaft) | 4,1 |
| + Hinzurechnung Märkte (Basis 113,2 < 200) | 0,0 |
| + EBT Kelterei GmbH (Organgesellschaft) | 7,3 |
| + Hinzurechnung Kelterei (Basis 43,6 < 200) | 0,0 |
| − Freibetrag Personengesellschaft | −24,5 |
| **= Gewerbeertrag** | **386,5** |
| **GewSt = × 3,5 % × 400 %** | **54,1** |
| davon durch die Sondervergütung | 19,6 |
| Entnahmen für ESt: 45 % × Σ Einzel-EBT 223,2 − Anrechnung § 35 EStG | 46,3 |

ESt-Satz 45 % inklusive Soli und Anrechnung der GewSt bis zum 4-fachen Messbetrag sind grobe Annahmen **[Vermutung]**. Die Zwischengewinn- und Geschäftswert-Effekte der Konsolidierung sind steuerlich ohne Wirkung; latente Steuern (§ 306 HGB) bleiben vereinfachend außen vor **[Annahme]**. Lagert man die Märkte aus der GmbH in die KG zurück, fiele deren Miete unter die Hinzurechnung der KG; bei Freibetrag je Gesellschaft ist die GmbH-Lösung um bis zu ≈ 4 T€ GewSt günstiger **[Vermutung]**.

### 2.11 Eröffnungsbilanzen zum 01.01.2027 (T€, Bruttomodell Pfand)

**KG (Großhandel und Zentrale)**

| Aktiva | T€ | Passiva | T€ |
|---|---|---|---|
| Immaterielle VG (ERP-Software) | 40,0 | EK: Kommanditkapital | 600,0 |
| Sachanlagen (Sortieranlage 420, Lager-BGA 200, IT 40, Veranstaltungsinventar 196, Anhänger 60) | 916,0 | EK: Rücklagen | 1.500,0 |
| Leihinventar bei Wirten | 900,0 | Rückstellungen (Kundenboni 142,5, Urlaub 60, Prüfung 35, GewSt 25, Sonst. 20) | 282,5 |
| Beteiligung Märkte GmbH | 250,0 | Bankdarlehen Betriebsmittel (5 %, Tilgung 250/J.) | 2.000,0 |
| Beteiligung Kelterei GmbH | 330,0 | Akquisitionsdarlehen Kelterei (4,5 %, Tilgung 50/J.) | 300,0 |
| Ausleihungen (Gastro-Darlehen) | 1.200,0 | Verbindlichkeiten L+L extern (inkl. Pfandsaldo 180) | 1.663,7 |
| Vorräte (Lagerware) | 700,0 | Pfandverbindlichkeiten gg. Kunden | 535,8 |
| Pfand-Erstattungsansprüche gg. Abfüller | 1.012,1 | Pfandverbindlichkeit gg. Märkte (intern) | 66,0 |
| Forderungen L+L extern (inkl. Pfandsaldo 40, brutto) | 1.402,8 | Verb. gg. Kelterei: Lieferungen | 45,0 |
| Ford. gg. Märkte: Warenlieferungen | 145,1 | Sonstige Verbindlichkeiten (USt, LSt, SV) | 220,0 |
| Ford. gg. Märkte: Cash-Pool | 150,0 | Kontokorrent (Rahmen 1.300) | 419,8 |
| Ford. gg. Märkte: EAV 2026 | 4,1 |  |  |
| Ford. gg. Kelterei: Pfand Saftkästen | 45,4 |  |  |
| Ford. gg. Kelterei: EAV 2026 | 7,3 |  |  |
| Bonus-/WKZ-Forderungen (Nachvergütungen 2026) | 290,0 |  |  |
| Sonstige VG | 60,0 |  |  |
| Bank | 150,0 |  |  |
| RAP | 30,0 |  |  |
| **Summe Aktiva** | **7.632,7** | **Summe Passiva** | **7.632,7** |

EK-Quote KG 27,5 %. Forderungen extern = Umsatz brutto × DSO je Segment + 40 T€ Pfandsaldo; Verbindlichkeiten extern = Wareneinsatz brutto × 26 Tage + ein Monat Sachkosten + 180 T€ Pfandsaldo. Der Kontokorrent ist die Ausgleichsgröße.

**Märkte GmbH**

| Aktiva | T€ | Passiva | T€ |
|---|---|---|---|
| Sachanlagen (Markt 1: 120, Markt 2: 65, Markt 3: 45) | 230,0 | EK: Stammkapital | 100,0 |
| Vorräte zu VP (M1 125, M2 80, M3 58) | 263,0 | EK: Kapitalrücklage | 150,0 |
| Pfand-Erstattungsanspruch gg. KG (intern) | 66,0 | Rückstellungen | 20,0 |
| Einweg-Pfandforderungen (DPG-Clearing) | 6,0 | Verb. gg. KG: Warenlieferungen | 145,1 |
| Forderungen (Kartenzahlungen unterwegs) | 15,0 | Verb. gg. KG: Cash-Pool (zinslos) | 150,0 |
| Kasse | 18,0 | Verb. gg. KG: EAV 2026 | 4,1 |
| RAP | 3,0 | Sonstige Verbindlichkeiten (USt, LSt) | 45,0 |
| Bank | 38,2 | Verbindlichkeiten L+L extern | 25,0 |
| **Summe Aktiva** | **639,2** | **Summe Passiva** | **639,2** |

**Kelterei GmbH**

| Aktiva | T€ | Passiva | T€ |
|---|---|---|---|
| Sachanlagen (Glaslinie 160, Presse 50, Tanks 72, BiB 24, Leergut-Pool 30, BGA 20) | 356,0 | EK: Stammkapital | 100,0 |
| Vorräte (Tankware, Fertigware zu HK, Hilfsstoffe) | 229,6 | EK: Kapitalrücklage | 200,0 |
| Ford. gg. KG: Lieferungen | 45,0 | Bankdarlehen (4,5 %, Tilgung 50/J.) | 150,0 |
| Forderungen L+L extern | 12,0 | Pfandverbindlichkeit gg. KG (Saftkästen im Umlauf) | 45,4 |
| Bank | 5,0 | Verb. gg. KG: EAV 2026 | 7,3 |
|  |  | Verbindlichkeiten L+L | 28,0 |
|  |  | Rückstellungen | 12,0 |
|  |  | Sonstige Verbindlichkeiten | 10,0 |
|  |  | Saison-Kontokorrent (Rahmen 400) | 94,9 |
| **Summe Aktiva** | **647,6** | **Summe Passiva** | **647,6** |

Kelterei-Vorräte: 200.000 l Tankware zu 0,480 €/l, Fertigware Glas 1,0 l 80.000 l zu 0,774 €/l, Glas 0,2 l (Gastro) 25.000 l zu 1,330 €/l, BiB 5 l (eigen) 30.000 l zu 0,783 €/l, Hilfsstoffe 15 T€. Nach der Pressung (September bis November) liegt am 31.12. rund 61 % der Jahresmenge auf Lager.

**Konsolidierungsbuchungen zum 01.01.2027**

| Buchung (mit Kelterei) | Aktiva − | Passiva − |
|---|---|---|
| Kapitalkonsolidierung Märkte: Beteiligung 250 ↔ EK 250 | 250,0 | 250,0 |
| Kapitalkonsolidierung Kelterei: Beteiligung 330 ↔ EK 300, GoF 30 abzgl. AfA 2025/26 | 306,0 | 306,0 |
| Schulden: Warenlieferungen KG → Märkte | 145,1 | 145,1 |
| Schulden: Cash-Pool KG → Märkte | 150,0 | 150,0 |
| Schulden: Pfand Märkte ↔ KG | 66,0 | 66,0 |
| Schulden: EAV 2026 Märkte | 4,1 | 4,1 |
| Schulden: Lieferungen Kelterei → KG | 45,0 | 45,0 |
| Schulden: Pfand Saftkästen KG ↔ Kelterei | 45,4 | 45,4 |
| Schulden: EAV 2026 Kelterei | 7,3 | 7,3 |
| Zwischengewinn KG in Märkte-Vorräten (3/103) | 7,7 | 7,7 |
| Zwischengewinn Kelterei in KG- und Märkte-Vorräten | 3,6 | 3,6 |
| **Summe Eliminierung** | **1.030,0** | **1.030,0** |

Zwischengewinne: Märkte-Vorräte 263,0 T€ × 3/103 = 7,66 T€; Kelterei-Saft im Bestand der KG (Glas 1,0 l 12.000 l, Glas 0,2 l (Gastro) 5.000 l, BiB 5 l (eigen) 3.000 l) und der Märkte (Glas 1,0 l 6.000 l, BiB 5 l (eigen) 2.000 l) × (VP − HK) = 3,59 T€. Interne Logistik ist als Gemeinkosten nicht aktivierbar, daher wird der ganze Aufschlag eliminiert **[wahrscheinlich]**. Der Geschäftswert der Kelterei (30 T€) wird über 10 Jahre abgeschrieben, Restbuchwert 24,0 T€.

**Konzernbilanz zum 01.01.2027**

| Posten | mit Kelterei | ohne Kelterei |
|---|---|---|
| Geschäfts- oder Firmenwert (Kelterei) | 24,0 | 0,0 |
| Immaterielle VG | 40,0 | 40,0 |
| Sachanlagen | 1.502,0 | 1.146,0 |
| Leihinventar bei Wirten | 900,0 | 900,0 |
| Ausleihungen (Gastro-Darlehen) | 1.200,0 | 1.200,0 |
| Vorräte (nach Zwischengewinn) | 1.181,4 | 955,3 |
| Pfand-Erstattungsansprüche gg. Abfüller | 1.012,1 | 1.057,5 |
| Einweg-Pfandforderungen | 6,0 | 6,0 |
| Forderungen L+L extern | 1.429,8 | 1.417,8 |
| Bonus-/WKZ-Forderungen | 290,0 | 290,0 |
| Sonstige VG und RAP | 93,0 | 93,0 |
| Kasse und Bank | 211,2 | 206,2 |
| **Summe Aktiva** | **7.889,5** | **7.311,9** |
| Eigenkapital | 2.082,8 | 2.092,3 |
| Rückstellungen | 314,5 | 302,5 |
| Bankdarlehen | 2.450,0 | 2.000,0 |
| Kontokorrent | 514,7 | 382,5 |
| Verbindlichkeiten L+L extern | 1.716,7 | 1.733,7 |
| Pfandverbindlichkeiten gg. Kunden | 535,8 | 535,8 |
| Sonstige Verbindlichkeiten | 275,0 | 265,0 |
| **Summe Passiva** | **7.889,5** | **7.311,9** |

EK-Quote brutto 26,4 % (ohne Kelterei 28,6 %), mit saldiertem Pfand 28,3 %. Konzern-EK 2.082,8 T€ liegt um 17,25 T€ unter dem EK der KG (Geschäftswert-AfA 6 T€, Zwischengewinne). Nettoverschuldung 2.753,5 T€.

### 2.12 Plan-Cashflow 2027 und Planbilanz 31.12.2027 (Konzern)

| Position | mit Kelterei | ohne Kelterei |
|---|---|---|
| Konzernergebnis nach GewSt | 166,1 | 165,6 |
| + Abschreibungen (inkl. GoF) | 552,3 | 445,3 |
| − Entnahmen für ESt der Kommanditisten | −46,3 | −45,5 |
| = Cashflow nach Entnahmen | 672,1 | 565,4 |
| − Investitionen | −415,0 | −355,0 |
| − neue Gastro-Darlehen | −300,0 | −300,0 |
| + Rückflüsse Gastro-Darlehen | 250,0 | 250,0 |
| − Tilgung Bankdarlehen | −350,0 | −250,0 |
| ± Working Capital (Stichtag wie Vorjahr) | 0,0 | 0,0 |
| = Anstieg Kontokorrent | 142,9 | 89,6 |

Investitionen: Leihinventar (Ersatz, neue Wirte) 200,0; KG übrige (Lager, IT, Veranstaltung) 110,0; Märkte (inkl. Kühlmöbel Markt 1 im Dezember) 45,0; Kelterei (Pumpen, Filter) 60,0 T€. Tilgung: Betriebsmitteldarlehen 250, Akquisitionsdarlehen 50, Kelterei 50 T€. Working Capital zum Stichtag unverändert (Silvester-Effekt wiederholt sich).

| Planbilanz 31.12.2027 | mit Kelterei | ohne Kelterei |
|---|---|---|
| Bilanzsumme | 7.802,2 | 7.271,6 |
| Eigenkapital | 2.202,5 | 2.212,5 |
| Bankdarlehen | 2.100,0 | 1.750,0 |
| Kontokorrent | 657,7 | 472,1 |
| EK-Quote brutto / Pfand saldiert | 28,2 % / 30,3 % | 30,4 % / 32,8 % |
| Nettoverschuldung / EBITDA | 2,78 | 2,64 |
| Kapitaldienstfähigkeit (M50) | 1,75 | 2,03 |

Der Kontokorrentzins ist iterativ bestimmt: Ø-Saldo KG = (Anfang + Ende) ÷ 2 + 100 T€ Saisonzuschlag = 591,3 T€ (ohne Kelterei 527,3 T€) × 8 %; der Kelterei-Kontokorrent bleibt konstant, ihr Cashflow läuft über den Cash-Pool der KG. Die Saisonspitze liegt im Dezember (Kelterei-Bestand, Silvester-Leergut, Vorkauf vor Preisrunden). **Lernpunkt:** Der Kapitaldienst (Tilgung 350 T€) ist nicht aus dem Cashflow nach Investitionen gedeckt; die Gruppe finanziert die Tilgung über den Kontokorrent. Die EK-Quote steigt trotzdem, weil Tilgung die Bilanz verkürzt.

### 2.13 Leergutkonten

**(a) Bestand je Gebindeart zum 01.01.2027 (Stück)**

| Ort | Bierkasten 20 × 0,5 (3,10 €) | Wasser-/AfG-Kasten (3,30 €) | Saftkasten Kelterei (2,40 €) | Fass 30/50 l (30 €) | Palette (10 € netto) | Pfandwert T€ |
|---|---|---|---|---|---|---|
| Kunden extern (Kundenkonten) | 90.000 | 60.000 | 12.000 | 3.600 | 2.000 | 535,8 |
| KG-Lager Vollgut | 35.000 | 25.000 | 4.000 | 1.500 | 2.500 | 231,4 |
| KG-Lager Leergut (Silvester-Rückstau) | 30.000 | 22.000 | 3.000 | 800 | 1.500 | 180,4 |
| Unterwegs / Gutschrift offen | 8.000 | 4.000 | 1.000 | 200 | 500 | 44,0 |
| Märkte Vollgut | 9.500 | 6.500 | 1.800 | 50 | 300 | 50,7 |
| Märkte Leergut | 3.200 | 2.000 | 700 | 0 | 0 | 15,3 |
| **Summe** | **175.700** | **119.500** | **22.500** | **6.150** | **6.800** | **1.057,5** |
| Pfand netto €/Stück | 2,61 | 2,77 | 2,02 | 25,21 | 10,00 |  |

Normaler Leergutbestand im KG-Lager: BK 14.000, WK 10.000, SK 1.000 Kästen. Der **Silvester-Überhang** über diesem Normalbestand beträgt 30.000 Kästen = **79,0 T€** (Stichtagseffekt, vgl. G13).

**(b) Zuordnung zu Bilanzposten (T€)**

| Bilanzposten | Gesellschaft | Herleitung | T€ |
|---|---|---|---|
| Pfand-Erstattungsansprüche gg. Abfüller | KG | alle Orte, Gebinde BK, WK, Fass, Palette | 1.012,1 |
| Forderung gg. Kelterei (Saftkästen) | KG | alle Orte, Gebinde SK | 45,4 |
| Pfandverbindlichkeiten gg. Kunden | KG | Gebinde bei Kunden (alle Arten) | 535,8 |
| Pfandverbindlichkeit gg. Märkte (intern) | KG | Gebinde in den Märkten | 66,0 |
| Pfand-Erstattungsanspruch gg. KG (intern) | Märkte GmbH | Gebinde in den Märkten | 66,0 |
| Pfandverbindlichkeit gg. KG (Saftkästen im Umlauf) | Kelterei GmbH | SK außerhalb der Kelterei | 45,4 |
| Leergut-Pool (eigene Kästen und Flaschen, AV zu AK) | Kelterei GmbH | Anlagenbuchhaltung | 30,0 |
| Pfandsaldo in Verbindlichkeiten L+L | KG | Vollgut-Pfand belastet, Leergut noch nicht gutgeschrieben | 180,0 |
| **Pfand-Float Konzern** | Konzern | Ansprüche − Verbindlichkeiten Kunden − Pfandsaldo L+L | **296,3** |

Interne Pfandkonten (Märkte, Kelterei) heben sich in der Konsolidierung auf. Der Float von 296,3 T€ ist zinspflichtig über den Kontokorrent finanziert (≈ 23,7 T€ Zins im Jahr).

**(c) Jahresbewegung 2027 (Stück; Plan: Endbestand = Anfangsbestand)**

| Gebindeart | Lieferantenkonto AB | + Belastung mit Vollgut | − Gutschrift Rückgabe | − Ausbuchung Schwund | = EB | Pfandvolumen T€ | Kundenkonten AB = EB | Auslieferung = Rücknahme extern |
|---|---|---|---|---|---|---|---|---|
| Bierkasten 20 × 0,5 (3,10 €) | 175.700 | 565.000 | −561.610 | −3.390 | 175.700 | 1.471,8 | 90.000 | 395.000 |
| Wasser-/AfG-Kasten (3,30 €) | 119.500 | 447.000 | −444.318 | −2.682 | 119.500 | 1.239,6 | 60.000 | 309.000 |
| Saftkasten Kelterei (2,40 €) | 22.500 | 67.500 | −67.095 | −405 | 22.500 | 136,1 | 12.000 | 40.500 |
| Fass 30/50 l (30 €) | 6.150 | 11.000 | −10.970 | −30 | 6.150 | 277,3 | 3.600 | 11.000 |
| Palette (10 € netto) | 6.800 | 30.000 | −28.800 | −1.200 | 6.800 | 300,0 | 2.000 | – |

Lieferant ist für BK, WK, Fass und Palette der jeweilige Abfüller bzw. Palettenpartner, für SK die eigene Kelterei. Durch die Pfandkonten laufen ≈ **3,12 Mio. € Pfand im Jahr** (netto, ohne Paletten), das sind 14 % des Außenumsatzes. Monatliche Leergutbilanz je Gebindeart: AB + Rücknahme Kunden − Rückgabe Lieferanten − Ausbuchung = EB; Abstimmung in Mengen gegen den Lieferanten-Kontoauszug (M44).

| Leergut- und Palettendifferenzen 2027 | T€ |
|---|---|
| Fremdleergut nicht rückführbar (4 % × 15 % × 2,70 €) | 17,5 |
| Fehlflaschen, Bruch (0,3 % × 1,00 €) | 3,2 |
| Palettenschwund (1.200 × 10 €) | 12,0 |
| Fässer verloren (30 × 25,21 €) | 0,8 |
| Zähl- und Erfassungsdifferenzen | 15,0 |
| **Summe (Sachkosten KG)** | **48,5** |

Fremdleergutquote 4 %, davon 15 % nicht rückführbar **[Vermutung, Spanne 07]**. Dazu kommen die Pfanddifferenzen der Märkte (6,5 T€).

### 2.14 Wichtigste Kennzahlen (Plan 2027)

| Ebene | Kennzahl | Plan 2027 | Vergleich | Stufe |
|---|---|---|---|---|
| Konzern | Außenumsatz / EBITDA / EBIT | 22.266,7 / 915,6 / 363,3 T€ | – | Skript |
| Konzern | EBIT-Marge / EBT-Marge | 1,6 % / 1,0 % | GFGH 0,5–3 % (07) | Vermutung |
| Konzern | Personalquote | 15,0 % | 10–15 % (07); obere Grenze wegen Märkten und Kelterei | Vermutung |
| Konzern | Umsatz je VZÄ | 319 T€ (69,7 VZÄ, ≈ 100 Köpfe) | Branche 558 T€ je Kopf (2022, verzerrt) | wahrscheinlich |
| Konzern | EK-Quote 01.01. brutto / Pfand saldiert | 26,4 % / 28,3 % | Covenant ≥ 25 % [Annahme] | Skript |
| Konzern | EK-Quote 31.12.2027 (Plan) | 28,2 % | Covenant ≥ 25 % | Skript |
| Konzern | Nettoverschuldung / EBITDA 01.01. / 31.12. | 3,01 / 2,78 | Covenant ≤ 3,5 [Annahme] | Skript |
| Konzern | Kapitaldienstfähigkeit (M50) | 1,75 | Bank ≥ 1,2 [Annahme] | Skript |
| Konzern | Pfand-Float / Silvester-Überhang | 296,3 / 79,0 T€ | – | Skript |
| Konzern | Controller-Kosten ÷ EBIT | 20,6 % | Einzelmarkt 51 % (06) | Skript |
| KG | RE II ÷ Umsatz inkl. F / nur Außenumsatz | 23,9 % / 27,3 % | Gastro-GFGH 25–32 %, strecken-/LEH-lastig 8–15 % (07) | Vermutung |
| KG | Kosten je Gastro-Stopp / Logistik je Gastro-Kolli | 34,16 € / 2,73 € | 25–45 € / 1,50–3,50 € (07) | Vermutung |
| KG | Mindestbestellwert Gastro (DB = 0) | 125 € | Mindermengenzuschlag 5–15 € (07) | Skript |
| KG | Leergut je Kasten brutto / netto | 0,45 / 0,35 € | 0,20–1,00 € (07; Zitate 2009/2016) | wahrscheinlich |
| KG | Fuhrpark-Auslastung Verteiler-Lkw | 94,8 % | – | Skript |
| KG | Lagerumschlag (Lager-WE ÷ Vorräte 01.01.) | 19,4 × | 12–25 × (07) | Vermutung |
| KG | DSO Gastro / DPO (brutto/brutto) | 25 / 26 Tage | 15–35 / 20–35 (07) | Vermutung |
| KG | Darlehen ÷ Gastro-Umsatz | 12,6 % | 8–20 % (07) | Vermutung |
| KG | Diesel / CO₂ Scope 1 / Maut | 111.260 l / 295 t / 56,4 T€ | – | Skript |
| Märkte | Kunden je Tag / Ø Bon (Markt 1) | 329 / 21,50 € | 200–500 / 18–28 € (02) | Vermutung |
| Märkte | Personalquote / Raumkosten Markt 1 | 14,2 % / 6,6 % | 11–16 % / 4–7 % (02) | Vermutung |
| Märkte | interne Logistik ÷ Märkteumsatz | 7,3 % | 07: 6,6 % (ohne Lager/Beschaffung) | Skript |
| Kelterei | HK 1,0-l-Glas / Lohnmost-DB je l | 0,774 € / 0,38 € | – | Skript |
| Kelterei | Maschinenstundensatz Glaslinie | 77,83 €/h (mit Bedienern 136,17) | – | Skript |
| Kelterei | Vorräte 31.12. ÷ Umsatz | 31,9 % | saisonale Kapitalbindung | Skript |
| Kelterei | EBIT-Marge / EBT | 4,6 % / 7,3 T€ | – | Vermutung |


### 2.15 Eingebaute Lernanlässe im Startzustand

1. **Covenant-Druck:** EK-Quote 26,4 % bei 25 % Covenant (Headroom 1,4 Prozentpunkte); mit saldiertem Pfand 28,3 %. Der Pfandausweis entscheidet mit (Karte 31, M22, M50).
2. **Kapitaldienstlücke:** Tilgung 350 T€, Kontokorrent +142,9 T€; Umschuldung, Leasing des Leihinventars oder weniger Wirt-Darlehen (M23, M25, M50).
3. **Märkte-Falle:** Unter der Startregel weist die Märkte GmbH 4,1 T€ aus, die Gruppe verliert mit den Märkten in Vollkosten 98,3 T€ vor Overhead, eine Schließung schadet trotzdem (M14, M40, M41).
4. **Verrechnungspreis „Einstand + 3 %“** deckt die interne Logistik (10,7 % des Einstands) nicht. Marktleiter-Prämien hängen am VP (M41, M51).
5. **Eckkneipe** mit DB III −498 €, positiv bei 14-tägiger Belieferung; Mindestbestellwert 125 € (M09, M12, M33).
6. **Dünne Segmente:** Wiederverkäufer 0,8 % und Objekt/Heimdienst 2,5 % DB III; Strecke hängt an 25 Kunden (M16, M33, M37).
7. **Nachvergütungen** 417,4 T€ im Jahr, 290 T€ aus 2026 noch offen; Stufensprünge und Vorkauf im Dezember (M08, M48).
8. **Diesel und Maut:** ±30 ct/l = ±33,4 T€, Maut 56,4 T€; E-Sattelzug als Investitionsfrage, mautfrei bis 30.6.2031 laut 07 (M25, M39, M54).
9. **Leerkosten Fuhrpark** 29,3 T€ bei 94,8 % Auslastung: Reserve oder ein Lkw zu viel (M11, M14)?
10. **Kelterei:** Lohnmost unter Vollkosten, aber mit positivem DB; Bestand 229,6 T€ zu Herstellkosten; Missernte kostet 104,0 T€ (M07, M11, M22, M24).
11. **Steuern:** Sondervergütung des GF erhöht die GewSt um 19,6 T€; Freibetragsfrage in der Organschaft; Zuckersteuer ab 1.7.2027 als Planprämisse (M49).
12. **Controller-Stelle** (20,6 % des EBIT) muss ihren Nutzen zeigen (06 Karte 9, M01).
13. **Mindestlohn 14,60 € und E-Rechnungspflicht:** Jede B2B-Rechnung der KG ist ab 1.1.2027 eine E-Rechnung, die Bons der Märkte nicht (M34, M35).

### 2.16 Prüfprotokoll

Alle **94 Prüfungen** im Skript bestanden (Toleranz 0,01 T€, Bilanzen und Konsolidierungsbuchungen exakt).

| Prüfgruppe | Anzahl |
|---|---|
| Kalender (Liefer- und Öffnungstage NRW 2027) | 2 |
| Mengengerüst Kunden, Kelterei-Absatz, Leergut-Durchlauf | 7 |
| Kapazität und Personal (Märkte-Stunden, Fahrer, Lkw) | 6 |
| Kelterei-Kostenrechnung (HK × Menge, Kostenarten = Kostenstellen) | 2 |
| KG-Kostenrechnung (Kostenverteilung vollständig, Segmente = EBIT, NV, interne Logistik) | 4 |
| Verrechnungspreise (Gesamtergebnis invariant, Startregel = GuV) | 14 |
| Einzelbilanzen und Kreditrahmen | 6 |
| Konsolidierung (jede Buchung beidseitig, Konzern-EK, Konzernbilanz, Gliederung) | 25 |
| Konzern-GuV (Tabelle = Rechnung, Σ Einzel-EBIT/EBT, Außenumsatz) | 15 |
| Cashflow, Planbilanz, Zinsiteration | 4 |
| Covenants | 4 |
| Leergutkonten (AB + Belastung − Gutschrift − Ausbuchung = EB) | 5 |
| **Summe** | **94** |

Das Skript bricht ab, sobald eine Prüfung scheitert; jede Zahl in den Tabellen stammt aus diesem Lauf.

---

## 3. Mapping: Welche Module werden durch den GFGH spielbar oder besser?

Grundlage: Eignung am Einzelmarkt aus 01 (M01–M43, N/S/K) und 06 (M44–M56). Bewertet wird der Startbetrieb aus Abschnitt 2 (GFGH mit drei Märkten; Kelterei, wo vermerkt). Kategorien: **neu natürlich** = am Einzelmarkt nur per Szenario (S) oder kaum (K), hier im Startzustand vorhanden · **deutlich besser** = vorher natürlich, hier mit echtem, größerem Fall · **etwas besser** · **gleich** · **schwach** = bleibt auch hier künstlich oder dünn. Alle Einstufungen **[Vermutung]**.

| Modul | Einzelmarkt | Gruppe | Anker im Startbetrieb |
|---|---|---|---|
| M01 Rolle, Business Partnering | N (Stelle = 51 % EBIT) | deutlich besser | echte Stabsstelle (≈ 21 % des EBIT), Adressaten GF, Logistikleiter, Marktleitung, Bank, Brauereien |
| M02 Rechnungswesen, Pfand, USt | N | deutlich besser | Bruttomodell mit Kunden- und Lieferanten-Pfandkonten, Palette als eigene Leistung (19 %), Fasspfand, EAV-Buchung |
| M03 Quantitative Methoden | N | gleich | – |
| M04 KLR-Grundlagen, Abgrenzung | N | etwas besser | Sondervergütung des GF, kalk. Zins auf Wirt-Darlehen, Kelterei-AfA auf Wiederbeschaffungswert (45 statt 40 T€) |
| M05 Kostenarten, Kostenauflösung | N | deutlich besser | echte Treiber: km, Tourtage, Stopps, Kolli, Kästen; sprungfixe Lkw und Fahrer |
| M06 Kostenstellen, BAB | N (5 Stellen) | deutlich besser | 12 Kostenstellen, Hilfsstellen Lager, Leergut und Fuhrpark mit Leistungsverrechnung, Leerkosten; Kelterei-BAB mit Fertigungsstellen |
| M07 Kostenträger, Kalkulation | N (Handel) | deutlich besser (Industrie mit Kelterei) | Gastro-Kalkulation mit Kundenkonditionen; Äquivalenzziffern, Kuppelprodukt Trester, HK nach § 255 HGB |
| M08 KER, Monatsabschluss | N | deutlich besser | 417 T€ Nachvergütungen abgrenzen, Leergutabstimmung in Mengen, Konzern-Monatsabschluss, Bestandsveränderung Kelterei |
| M09 Teilkosten, DB-Rechnung | N | deutlich besser | Segment- und Kunden-DB I–III, Tour-DB |
| M10 Break-even, CVP | N | gleich | Segment-BEP und sprungfixe Lkw; der Mehrprodukt-BEP über fünf Segmente ist unanschaulicher |
| M11 Plankosten, Abweichungen | N (S für Produktion) | neu natürlich (mit Kelterei) | Beschäftigungsabweichung Glaslinie 56 T€, Ausbeute, Obstpreis; ohne Kelterei flexible Plankosten je Tourtag |
| M12 Prozesskostenrechnung | N | deutlich besser | Sätze je Stopp, Kolli, Kasten, Besuch, Auftrag; Mindestbestellwert 125 € |
| M13 Kostenmanagement, Target Costing | S | neu natürlich (teilweise) | Verbund-Benchmarking, Target Costing für Fest- und Heimdienstpakete, Hausmarke Apfelsaft |
| M14 Entscheidungsrechnung | N | deutlich besser | Selbstabholung oder Spedition, Markt schließen, Lieferrhythmus, Strecke an eigene Märkte |
| M15 Preis- und Konditionencontrolling | N | deutlich besser | Konditionen auf beiden Seiten (Brauerei und Wirt), Weitergabe von Preisrunden, Rückvergütung je hl |
| M16 Strategisches Controlling | N | etwas besser | Gastro-Strukturbruch (Gedat), Konsolidierung der Branche, Verbundwahl, Segmentportfolio |
| M17 Balanced Scorecard | N | etwas besser | Kaskadierung auf Sparten und Center |
| M18 Budgetierung | N | deutlich besser | Gegenstrom mit mehreren Budgetverantwortlichen, integrierte Planung mit Konsolidierung |
| M19 Forecast | N | etwas besser | Stoppzahlen-Trend, Preisrunden, Ernteschätzung |
| M20 Kennzahlensysteme | N | deutlich besser | Logistik-, Kunden-, Konzern- und Bankkennzahlen (2.14) |
| M21 Wertorientierte Steuerung | S | schwach (etwas besser) | Capital Employed je Segment, Kaufpreis Kelterei; kein Kapitalmarkt |
| M22 Bilanzanalyse | N | deutlich besser | prüfungspflichtige KG, Konzern- gegen Einzelbilanz, Pfand brutto/netto, Covenants |
| M23 Liquidität | N | deutlich besser | Kapitaldienstlücke, Saisonspitze Kelterei und Silvester, Cash-Pool |
| M24 Working Capital | N (S für DSO) | deutlich besser | DSO Gastro, Kreditlimits, Pfand-Float ≈ 300 T€, Kelterei-Bestand |
| M25 Investitionsrechnung | N | deutlich besser | Lkw, E-Lkw, Sortieranlage, Wirt-Darlehen als Investition, Abfülllinie |
| M26 Reporting | N | etwas besser | Berichte an GF, Beirat, Bank, Brauereien (hl-Meldungen); Segmentbericht |
| M27 Visualisierung, IBCS | N | gleich | – |
| M28 Tabellenkalkulation | N | etwas besser | Konsolidierungs- und Tourenmodell als Übungsmodell |
| M29 Datenmanagement, BI | N | etwas besser | ERP mit Leergut je Debitor, Gedat-Stammdaten, Telematik |
| M30 Analytics, KI | N | etwas besser | Abwanderungs- und Insolvenz-Frühwarnung, Tourenoptimierung |
| M31 Beschaffungscontrolling | N | deutlich besser | Konditionsverträge, Vorkauf, Selbstabholung, Bonusstaffeln |
| M32 Logistik, Bestand | N | deutlich besser | Lager, Kommissionierung, Fuhrpark, Touren, Sortierung |
| M33 Vertriebscontrolling | N (S für B2B) | deutlich besser | Kunden-DB, Außendienststeuerung, Darlehen gegen Bezugsbindung |
| M34 Personalcontrolling | N | etwas besser | Fahrermangel, Lohnabstand Lager/Märkte/Fahrer, Lenkzeiten |
| M35 IT-Controlling | S | neu natürlich | ERP-Ablösung, E-Rechnungspflicht für alle KG-Rechnungen, Telematik |
| M36 Projektcontrolling | S | neu natürlich | ERP-, Sortieranlagen-, Marktumbau- und E-Lkw-Projekt |
| M37 Risikocontrolling | N | deutlich besser | Kreditportfolio Wirte, Brauerei-Insolvenz, Großkundenverlust, Missernte |
| M38 IKS, Compliance | N | etwas besser | Fahrer-Leergutzählung gegen Lager, Funktionstrennung, Kartellrecht der Bezugsbindung |
| M39 ESG | N (S Fuhrpark) | deutlich besser | Scope 1 ≈ 295 t CO₂ aus Diesel, E-Lkw, Mehrweglogistik |
| M40 Konzern, Filialen | S | neu natürlich | Kapital-, Schulden-, Aufwands-/Ertrags- und Zwischengewinnkonsolidierung, EAV; aber freiwillig, kein IFRS |
| M41 Verrechnungspreise, Center | S | neu natürlich | VP Märkte in vier Varianten, Kelterei-VP, Umlage, Leistungsverrechnung |
| M42 Beratung | N | deutlich besser | realistische Projektthemen: Fuhrpark, Kundenportfolio, VP-System, Markt 3 |
| M43 Kommunikation, Verhandlung | N | etwas besser | Verhandlungen mit Brauerei, Wirt, Bank; Moderation der Budgetrunde |
| M44 Pfand- und Leergutcontrolling | N | deutlich besser | Konten in Mengen je Gebindeart, Sortierung, ≈ 3 Mio. € Pfand im Jahr |
| M45 Aktionscontrolling | N | gleich (nur in den Märkten) | Lockvogel-Aktionen bleiben Markt-Thema |
| M46 Kurzfristprognose | N | gleich | Wetter, Feste, Fassbier-MHD, Ernte |
| M47 Dienstleistungscontrolling | N | deutlich besser | Veranstaltungen, Schanktechnik, Heimdienst, Depotdienst |
| M48 Konditionen und Boni | N | deutlich besser | 417 T€ Nachvergütungen, 290 T€ offen, hl-Meldungen, Staffeln |
| M49 Steuercontrolling | N | deutlich besser | Organschaft, Sondervergütung, Hinzurechnung, Betriebsaufspaltung, § 35 EStG |
| M50 Finanzierung, Covenants | N | deutlich besser | drei Covenants mit wenig Headroom, Kapitaldienstfähigkeit, Kreditversicherer |
| M51 Verhaltensorientiertes Controlling | N | etwas besser | Marktleiter-Prämie auf VP-Ergebnis, Außendienstprämie Umsatz oder DB |
| M52 Energie, Anlagen, Standort | N | etwas besser | Fuhrpark-TCO, Mietvertrag mit der Besitzgesellschaft, Kelterei-Energie |
| M53 Daten-Handwerk, Warenkorb | N | gleich (nur in den Märkten) | Warenkorb bleibt Markt-Thema |
| M54 ESG-Ergänzung | N | etwas besser | CO₂-Preis im Diesel, Mautbefreiung E-Lkw, Kältemittel im Fasskühlraum |
| M55 Teamführung | N mit Kniff | schwach (etwas besser) | Inventur an fünf Standorten, Budgetrunde; der Controller führt kaum ein Team |
| M56 Bewertung, Nachfolge | N | deutlich besser | Kauf der Kelterei über Ertragswert, Nachfolge in der Familien-KG, Übernahmeangebot eines Konzern-GFGH |

**Zählung:** neu natürlich 6, deutlich besser 28, etwas besser 14, gleich 6, schwach 2 (Summe 56).

**Bleibt schwach, auch im GFGH:**
- **M21 (wertorientierte Steuerung):** Die Familien-KG hat keinen Kapitalmarkt, WACC bleibt eine Annahme. Capital Employed je Segment ist neu sinnvoll, EVA bleibt Übung.
- **M40 (Konzern):** Konsolidierung ist voll spielbar, aber nur freiwillig (§ 293 HGB) und nach HGB. IFRS, Minderheiten, Equity-Methode und Währung fehlen.
- **M39 (CSRD):** Keine Berichtspflicht; nur VSME-Anfragen von Bank und Brauereien.
- **M55/M43 (HB6 Führung):** Der Controller führt in einer Gruppe dieser Größe allenfalls eine Assistenz. Teamführung bleibt Inventur- und Projektleitung.
- **M11/M07/M13 mit Industriebezug** sind nur mit Kelterei natürlich, und auch dann klein und saisonal (eine Pressung im Herbst).
- **IHK-Gewicht:** Projektarbeit (45 %) und Fachgespräch (30 %) bleiben schwer spielbar (06, 6.4). Der GFGH liefert bessere Projektthemen, ersetzt aber weder die 30-Tage-Arbeit im eigenen Betrieb noch das Fachgespräch.

**Schwächer als am Einzelmarkt, wenn man die Märkte weglässt:** M45 (Aktionen), M53 (Warenkorb), M46 (Wetterdisposition im Endkundengeschäft) und die Anschaulichkeit von Kasse und Bon. Genau deshalb sollten die Märkte im Modell bleiben.

---

## 4. Ehrliche Bewertung der Kulissen

Skala 1–5, 5 = am besten; beim Bauaufwand bedeutet 5 = geringer Aufwand. Alle Einstufungen **[Vermutung]**, begründet unten.

| Kriterium | Getränkemarkt allein (02) | GFGH allein | GFGH + 3 Märkte | GFGH + Märkte + Kelterei |
|---|---|---|---|---|
| IHK HB1 Kosten- und Leistungsrechnung | 3 | 4 | 4 | 5 |
| IHK HB2 Planung und Budgetierung | 3 | 4 | 5 | 5 |
| IHK HB3 Jahresabschlussanalyse | 2 | 4 | 5 | 5 |
| IHK HB4 Berichtswesen und Information | 3 | 4 | 4 | 4 |
| IHK HB5 Beratung (Projektthemen) | 3 | 4 | 5 | 5 |
| IHK HB6 Führung und Moderation | 2 | 3 | 3 | 3 |
| Anschaulichkeit und Einstieg | 5 | 2 | 4 | 3 |
| Bauaufwand (5 = gering) | 4 (160–280 PT) | 3 (+40–70 PT) | 2 (+80–130 PT) | 1 (+105–170 PT) |
| Realismus der Controller-Rolle | 1 | 4 | 5 | 4 |
| Belegbarkeit der Zahlen | 2 | 1 | 1 | 1 |


**Begründung je Kulisse**

- **Getränkemarkt allein:** Sehr anschaulich (Kasse, Kunde, Kiste, Wetter), schnellster Einstieg, rechnerisch geschlossen (02/06). Schwach für HB3 (kleine GmbH ohne Prüfung und ohne echte Covenants), Center, Verrechnungspreise, Konzern und B2B. Die Controller-Stelle ist unrealistisch (51 % des EBIT, 06). Bauaufwand nach 04: Version 1.0 ≈ 160–280 PT.
- **GFGH allein:** Realistische Controller-Stelle, starke KLR (Prozesskosten, Hilfsstellen), Kunden-DB, Kreditrisiko, Finanzierung. Aber: B2B ist abstrakter, es gibt keinen Kassentag, Aktions- und Warenkorbthemen fallen weg, und die Leergut- und Gastrovertrags-Mechanik ist Domänenwissen, das vom Controlling ablenken kann. Bauaufwand ≈ +40–70 PT gegenüber dem Einzelmarkt: Auftrags- statt Bon-Modell, Tourtage, Leergutkonten je Kunde und Lieferant, Darlehen und Ausfälle **[Vermutung]**.
- **GFGH + 3 Märkte:** Verbindet beides. Markt 1 liefert den anschaulichen Einstieg, die Zentrale die Controller-Rolle, die Gruppe Verrechnungspreise und Konsolidierung. Einziger echter Nachteil ist der Aufwand: ≈ +80–130 PT gegenüber dem Einzelmarkt (beide Modelle, Innenleistungen, Konsolidierung, mehr UI-Sichten). Im Hobbytempo von 1,5 PT pro Woche (04) sind das 13–21 Monate mehr **[Vermutung]**.
- **+ Kelterei:** Bringt die Industrie-KLR (BAB mit Fertigungsstellen, Maschinenstundensatz, Äquivalenzziffern, Kuppelprodukt, Bestandsbewertung, Beschäftigungsabweichung) in die eigene Welt; HB1 ist industriegeprägt (06) **[wahrscheinlich]**. Dafür +25–40 PT, ein Saisonmodell und eine Konstellation, die selten ist (Kelterei bei weniger als 5 % der GFGH, 07 **[Vermutung]**). Wirtschaftlich trägt sie im Startbetrieb nur 1,8 T€ EBT bei. Ein „Transfer-Mandat“ in fremder Branche (03) leistet für HB1 vermutlich ähnlich viel und ist billiger **[Vermutung]**.

**Empfehlung**

1. **Kulisse: GFGH mit eigenen Märkten.** Sie ist die einzige Variante, in der die Controller-Rolle realistisch ist und zugleich der anschauliche Einstieg erhalten bleibt **[Vermutung]**.
2. **Gestufte Kampagne:** Spieljahr 1 als Controller der Gruppe mit Fokus Markt 1 und Zentrale-KLR (Monatsabschluss, Leergut, Prozesskosten). Spieljahr 2: Gastronomie und Logistik (Kunden-DB, Touren, Fuhrpark, Kreditrisiko, Covenants). Spieljahr 3: Konzern, Finanzierung und Kauf der Kelterei als Herbst-Kapitel (M40, M41, M56, Industrie-KLR).
3. **Simulationstiefe begrenzen:** Großhandel nach Kundenklassen und Tourtagen statt 1.250 Einzelkunden und echter Tourenplanung, dazu 10–20 benannte Kunden für Fälle. Markt 1 auf Bon-Ebene, Markt 2 und 3 als Monatsaggregate. Die Kelterei als geskriptete Fallstudie, nicht als Dauersimulation.
4. **Prototyp unverändert klein:** Den Lernprototyp aus 04 (20–25 PT) in Markt 1 bauen, aber mit Datenmodell für Gesellschaft, Kostenstelle, Innenleistung und Leergutkonto je Partner. Dann kostet der spätere Ausbau keine Neuentwicklung.
5. **Fachreview:** Eine Person aus dem GFGH-Controlling sollte Segment-Quoten, Prozesskostensätze und Konditionen prüfen. Die Datenlage ist hier noch dünner als beim Einzelmarkt.
6. **Neue Entscheidungskarten:** Kulisse (Einzelmarkt / GFGH / GFGH + Märkte / + Kelterei) – P1. Simulationstiefe Großhandel (Klassen / Einzelkunden) – P1. Märkte auf Bon-Ebene (nur Markt 1 / alle) – P2. Kelterei als Simulation oder Fallstudie – P2. Konsolidierung im Spiel (Bankrechnung / Pflichtabschluss-Übung) – P2.

**Gegenargumente, die man ernst nehmen sollte:** Mehr Domäne heißt mehr Stoff, der nicht Controlling ist: Leergutsortierung, Bezugsbindung und Mautklassen. Wer nur die IHK-Prüfung will, braucht davon wenig. Wenn der Bauaufwand der Engpass ist, bleibt der Einzelmarkt mit Szenario-Erweiterungen (01, 3b) die realistischere Wahl. Dann aber mit der offenen Ansage, dass Konzern, Verrechnungspreise und Controller-Rolle nur Ausblick sind.

---

## 5. Quellen

**Neu in 08 (Suchauszüge, Oktober 2026):**
- Maut: [DSLV-Mauttabelle ab 1.12.2023 (GVN)](https://www.gvn.de/227/pdf/NL_SuL/2023/2023.11.01_DSLV_Mauttabelle_2023_11_01.pdf) · [Maut-Rechner, inoffiziell](https://www.autobahn-baustellen.de/lkw-maut-rechner/)
- Diesel und Tankrabatt: [ADAC/leinetal24, 7.10.2026](https://www.leinetal24.de/na-pressemitteilungen/benzin-und-diesel-etwas-guenstiger-preisniveau-aus-sicht-des-adac-zu-hoch-senkung-der-energiesteuer-ab-oktober-zr-94518014.html) · [test.de Tankrabatt](https://www.test.de/Hohe-Benzinpreise-Der-Tankrabatt-kommt-zurueck-am-1-Oktober-gehts-los-6338058-0/)
- Zuckersteuer: [PwC Steuern und Recht](https://blogs.pwc.de/de/steuern-und-recht/article/257323/bundeskabinett-beschliesst-gesetzentwurf-zur-einfuehrung-der-zuckergetraenkesteuer/) · [Tageskarte](https://www.tageskarte.io/industrie/detail/kabinett-beschliesst-zuckersteuer.html) · [Lebensmittel Praxis](https://lebensmittelpraxis.de/industrie-aktuell/50078-zuckersteuer-kommt-koalition-einigt-sich-auf-steuer-fuer-zuckergesuesste-getraenke.html) · [ms-aktuell 16.10.2026](https://ms-aktuell.de/welt/zuckersteuer-softdrinks-16-10-2026/)
- Kelterei: [LP Rekordpreise Mostobst](https://lebensmittelpraxis.de/industrie-aktuell/42138-ernteschwankungen-treiben-kosten-fruchtsaftindustrie-zahlt-rekordpreise-fuer-mostobst.html) · [Infobrief Streuobst Oberfranken 09/2025](https://regierung.oberfranken.bayern.de/mam/service/umwelt/natur/infobrief_streuobst_nr_7_2025-09.pdf) · [Meininger Safthersteller 2025](https://www.meininger.de/alkoholfreie-getraenke/hersteller/stabiles-jahr-fuer-safthersteller)
- Großhandel: [Meininger, Kartellamt zu Rewe/Trinks (Direktbelieferung)](https://www.meininger.de/handel/getraenkefachgrosshandel-gfgh/kartellamt-winkt-rewe-deal-mit-trinks-durch) · [Tageskarte, Fassbier für Gastronomie teurer](https://www.tageskarte.io/industrie/detail/fassbier-wird-fuer-gastronomie-teurer.html) · [about-drinks, Zentrallager Team Beverage/Vinexus](https://www.about-drinks.com/team-beverage-und-vinexus-gruppe-bauen-weingeschaeft-im-gfgh-aus/) · [Statista, Umsatz Getränkegroßhandel WZ 46.34](https://de.statista.com/statistik/daten/studie/386069/umfrage/umsatz-im-grosshandel-mit-getraenken-in-deutschland)

**Übernommen:** Branchen-, Rechts- und Preisquellen aus 02 (Abschnitt 14), 06 (Abschnitt 7) und 07 (Abschnitt 13), u. a. Gedat, BV GFGH, BFH I R 36/07, BMF 5.11.2013, BGH VIII ZR 135/00, Toll Collect, VdF.

**Aus Fachwissen, nicht neu geprüft:** §§ 255 Abs. 2, 264a, 267, 290, 293, 301, 303–306 HGB; § 14 KStG (Organschaft); § 2 Abs. 2 GewStG; §§ 8 Nr. 1, 11 Abs. 1 GewStG (Hinzurechnung, Freibetrag 24.500 €); § 15 Abs. 1 Nr. 2, § 35, § 4 Abs. 5b EStG; Kapitalisierungs- und Steuersätze wie in 02/06.

**Rechnungen:** Python-Skripte `rechenmodell/model08.py` (Modell und Prüfungen) und die Generatoren `gen08_*.py` im selben Ordner, 19.10.2026. Alle Tabellen dieses Dokuments werden aus dem Modell erzeugt, nicht von Hand gepflegt (Folgerung aus 06, 2.3).
