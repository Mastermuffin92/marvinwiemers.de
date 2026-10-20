# 06 – Lücken, Korrekturen, Widersprüche, offene Entscheidungen

Stand 19.10.2026. Grundlage: vollständige Lektüre von 01–05, Nachrechnung per Skript (Python) und Websuche (Abrufe ganzer Seiten scheiterten erneut an DNS, belegt ist daher über Suchauszüge). Sicherheitsstufen: **[sicher]** belegt oder nachgerechnet · **[wahrscheinlich]** starke Schlussfolgerung · **[Vermutung]** Lücke gefüllt. Alle neuen Getränkemarkt-Zahlen sind **Annahmen** und beziehen sich auf den Betrieb aus **02, Abschnitt 12** (2,5 Mio. € Umsatz), weil 04 diesen bereits als Golden Master nutzt.

---

## 0. Die wichtigsten Befunde in Kürze

1. **Es gibt zwei Referenzbetriebe.** 01 und 03 rechnen mit der „Durstlöscher GmbH“ (2,4 Mio. €, RE 25 %, Bilanz 900 T€), 02 und 04 mit der „{MARKTNAME} Getränke GmbH“ (2,5 Mio. €, RE II 30 %, Bilanz 451 T€). Auch Artikelpreise, Pfandmodell und Kostenstruktur weichen ab. Das ist der größte Konstruktionsfehler und muss vor jedem Content-Schreiben behoben werden. **[sicher]**
2. Das Beispielunternehmen aus 02 ist **rechnerisch weitgehend geschlossen** (Bilanz, GuV, Monatsverteilung, Leitartikel stimmen bis auf Rundung). Es enthält aber **19 konkrete Fehler oder Unplausibilitäten**, darunter eine Kostentabelle, die nur 99,6 % ergibt, eine falsche Anlagendeckung II, 304 statt 306 Öffnungstage und eine Personalplanung, die ihren eigenen Stundenbedarf um ≈ 1,5 VZÄ unterschreitet. **[sicher/wahrscheinlich]**
3. Das Curriculum (43 Module) ist breit. Es fehlen aber **13 Facetten**: vor allem Pfand-/Leergutcontrolling als eigenes Modul, Konditionen-/Bonus-Tracking, Steuercontrolling, Finanzierung/Rating/Covenants, verhaltensorientiertes Controlling, **Teamführung (IHK HB6 nennt sie ausdrücklich)**, Unternehmensbewertung/Nachfolge, Daten-Handwerk (Warenkorbanalyse) und ESG-Kosten (CO₂-Preis, F-Gase). Ergänzt als M44–M56. **[wahrscheinlich]**
4. **Die IHK-Gewichtung aus 05 stimmt:** 25 % schriftlich, 45 % Projektarbeit, 30 % mündlich (§ 7 Abs. 4 ContrPrV). **[sicher]** Damit liegen 75 % der Note gerade in den Teilen, die ein Spiel am schlechtesten abbilden kann.
5. Echtzeit-Rost (03) plus FSRS-Mastery ab 21 Tagen Stabilität (04) plus Abschluss-Gate führen bei „alle Facetten“ rechnerisch zu **≥ 9 Monaten täglichen Übens**. Das ist eine Designentscheidung, keine Nebensache. **[Vermutung, Rechenbeispiel in 6]**

---

## 1. Fehlende Controlling-Facetten und Ergänzungsmodule

### 1.1 Abgleich gegen die Bezugsrahmen

| Bezugsrahmen | Abdeckung in 01 | Lücke |
|---|---|---|
| ContrPrV HB1–HB4 | gut (M04–M30) | Steuern als Planungsgröße, Inventur und Bewertung, Finanzierung/Rating nur verstreut |
| ContrPrV HB5 Beratung | M42 | Bewertung/Nachfolge (beim Inhaber mit 61 Jahren naheliegend) fehlt als N-Modul |
| ContrPrV HB6: „Führen und Organisieren von Teams; Moderation, Kommunikation und Konfliktmanagement“ **[sicher, Wortlaut § 4 Abs. 6]** | M43 (Kommunikation, Moderation, Verhandlung) | **Teamführung und Organisation** fehlen praktisch, weil der Spieler-Controller niemanden führt |
| IGC-Prozessmodell 2.0 | alle Hauptprozesse vorhanden | „Datenmanagement“ nur konzeptionell, kein Analyse-Handwerk; „Weiterentwicklung Controlling“ nur in M42 |
| Funktionsbereichs-Controlling | Beschaffung, Logistik, Vertrieb, Personal, IT, Projekt | **Dienstleistungen** (Heimdienst/Festservice gibt es in 02 schon im Startzustand!), Energie/Anlagen, Standort/Immobilie, Steuern |
| Soft Skills (Kompetenzklassen Fach/Methode/Sozial/Personal plus digital, nach Schöning/Mendel 2021) **[wahrscheinlich]** | Kommunikation, Präsentation, Verhandlung | Selbstorganisation unter Abschlussdruck, schriftliche Entscheidungsvorlagen, Feedback/Lehren, Integrität unter Druck, Unsicherheit kommunizieren |
| Daten/BI | M28–M30 | Warenkorbanalyse, Datenmodell, DSGVO bei Kundendaten, KI-Kompetenzpflicht |
| ESG | M39 (Scope 1/2, VSME) | CO₂-Preis als Kostenart, F-Gase als Investitionsrisiko, Scope 3, Mehrweg/PPWR als Sortimentsthema |
| Branchenkern Getränkehandel | Pfand verteilt auf M02/M24/M38 | **Pfand/Leergut als eigenes Steuerungsobjekt**, Aktionen, Bonusstaffeln, Wetter-Disposition |

Ein ICV-eigenes, veröffentlichtes Controller-Kompetenzmodell habe ich nicht gefunden. Die IGC-Grundsatzposition nennt Transparenz- und Methodenkompetenz und die Rollen „Guardian“ und „Change Agent“. **[wahrscheinlich]**

### 1.2 Ergänzungsmodule (Struktur wie 01)

Rhythmus: T täglich · W wöchentlich · M monatlich · Q quartalsweise · J jährlich · AH ad hoc. Eignung: N natürlich am Einzelmarkt · S Szenario-Erweiterung.

#### M44 Pfand- und Leergutcontrolling (Block F, HB1/3/4, IHK mittel, N)
- **Lernziele:** Pfandkreislauf als Mengen- und Wertstrom abbilden (Verstehen). Leergutkonten je Lieferant abstimmen (Anwenden). Pfand-Float und Stellplatzbedarf steuern (Analysieren). Bilanzausweis begründen (Bewerten).
- **Formeln:**
  - Ø Leergutbestand = Tageszugang × Abholintervall (Öffnungstage) / 2.
  - Pfand-Float = Pfandwert Leergut im Lager + offene Pfandgutschriften − Pfandverbindlichkeiten an bekannte Kunden.
  - Rücklaufquote = ausgezahltes Pfand / vereinnahmtes Pfand.
  - Fremdleergutverlust = Rücknahme × Fremdleergutquote × nicht rückführbarer Anteil × Pfandsatz.
- **Alltag:** Automaten- und Pfandbon-Abgleich (T), Leergutabholung disponieren (W), Leergutkonto mit Lieferant abstimmen (M), Leergutinventur (J, Stichtag nach Silvester).
- **Voraussetzungen:** M02, M24.
- **Typische Fehler:** Abstimmung nur in Euro statt in Mengen je Gebindeart. Leergut als Warenvorrat ausweisen; laut Verwaltungsauffassung bleibt es Eigentum des Abfüllers, der Händler hat einen Erstattungsanspruch **[wahrscheinlich, BFH I R 36/07]**. Abholrhythmus ohne Stellplatzrechnung ändern.
- **Übung:**
  - (a) Zugang 570 Kästen/Tag (02). Wöchentliche Abholung ergibt Ø 1.710 Kästen ≈ 5.470 € Pfandwert und 34 Paletten. Zweiwöchentliche Abholung ergibt 3.420 Kästen, 68 Paletten. Das sprengt die 60 Leergut-Stellplätze aus 02. Lernpunkt: Eine Kostenersparnis bei Abholungen kann an der Fläche scheitern.
  - (b) Laut Kontoauszug der Brauerei Nord sind 1.840 Kästen offen, laut eigenem Nebenbuch 1.912. Die Differenz von 72 × 3,10 € = 223,20 € muss geklärt werden: Gutschrift fehlt, Zählfehler oder Fremdkästen?
  - (c) Fremdleergut 2 % von 175.000 Kästen = 3.500 Kästen; davon 25 % nicht rückführbar → 875 × 3,10 € = 2.713 €. Das passt zu den 3.000 € „Pfanddifferenzen“ in 02.

#### M45 Aktions- und Promotionscontrolling (Block B/F, HB1, IHK mittel, N)
- **Lernziele:** Inkrementellen Aktionserfolg berechnen (Anwenden). Kannibalisierung, Vorzieheffekt und Verbund trennen (Analysieren). Aktionskalender mit Brauerei-Konditionen bewerten (Bewerten).
- **Formel:** Inkrementeller RE = x_Akt × db_Akt − x_Basis × db_normal − Kannibalisierung × db_Substitut − Nachholmenge × db_normal + Verbund-RE + WKZ.
- **Alltag:** Aktionsplanung mit Lieferanten (Q), Nachbetrachtung (W), Abverkaufsnachweis für Aktions-EK (W/M).
- **Voraussetzungen:** M09, M15.
- **Typische Fehler:** Aktion am Umsatz messen. Kannibalisierung ignorieren. Restmengen zum Aktions-EK nicht abgrenzen (Nachbelastung).
- **Übung (L01 aus 02):** Normalwoche 120 Kästen × 2,30 € db = 276 €. Aktion 10,99 € mit Aktions-EK 8,60 € ergibt db 0,64 €; Lift × 4 = 480 Kästen = 307 €. Davon sind 60 % der 360 Mehrkästen Kannibalisierung anderer Biere: 216 × 2,80 € = −605 €. Nachholeffekt in 2 Wochen: −48 Kästen × 2,30 € = −110 €. Verbund: 150 Zusatzbons × 3,40 € = +510 €. **Ergebnis −174 € je Aktionswoche, mit 400 € WKZ +226 €.** Lernpunkt: Das WKZ trägt die Aktion, die Spanne nicht.

#### M46 Kurzfristprognose und Disposition unter Unsicherheit (Block E/F, HB2/4, IHK niedrig, N)
- **Lernziele:** Wetterprognose mit Fehlerband in die Bestellung übersetzen (Anwenden). Fehlmengen- und Überbestandskosten abwägen (Bewerten). Prognosegüte messen (Analysieren).
- **Formeln:**
  - Kritisches Verhältnis CR = C_u / (C_u + C_o), Bestellmenge Q = μ + z(CR) × σ (Newsvendor).
  - MAPE, Bias (wie M19).
  - Prognoseintervall μ ± 1,64 σ (90 %).
- **Alltag:** Bestellung und Personal bei 7-Tage-Wetter (T/W von Mai bis August), Prognosegüte-Review (M).
- **Voraussetzungen:** M03, M19, M32.
- **Typische Fehler:** Die Punktprognose bestellen. Für lange haltbares Wasser und unfiltriertes Bier (MHD 3–6 Monate) dieselbe Logik verwenden. Prognosefehler nicht erfassen.
- **Übung:** Wasser L09, Hitzewoche, μ = 600 Kästen, σ = 120. C_u = db 1,53 € + 0,50 € Goodwill = 2,03 €. C_o = 0,11 € (Kapitalbindung und Stellplatz pro Woche) → CR 0,95 → z ≈ 1,64 → **Q ≈ 797 Kästen**. Kontrast: Fassbier für ein Fest mit hohem C_o (angestochen nicht rücknehmbar), dort Q unter μ.

#### M47 Dienstleistungscontrolling Heimdienst und Festservice (Block F, HB1/5, IHK mittel, **N** – in 02 schon im Startzustand)
- **Lernziele:** DB je Stopp und je Auftrag rechnen (Anwenden). Liefergebühr und Mindestbestellwert gestalten (Bewerten). Kommissionsgeschäft bewerten (Analysieren).
- **Formeln:**
  - Kosten je Stopp = (Fahrerstunden × Satz + km × Kilometersatz + Fahrzeugfix) / Stopps.
  - Mindestbestellwert für DB = 0: (Kosten je Stopp − Gebühr) / RE-Quote.
  - Kommissions-DB = (ausgegeben − Rücklauf) × db − Rücklauf × Handling − Fahrten.
- **Alltag:** Tourenplanung (T), Stopps je Stunde (W), Service-DB (M), Festsaison-Review (J).
- **Voraussetzungen:** M09, M12, M14.
- **Typische Fehler:** Leergutabholung beim Kunden nicht als Leistung kalkulieren. „Gratis ab X €“ ohne Wirkung auf Bestandskunden rechnen.
- **Übung (Werte aus 02):** Kosten 11,80 €/Stopp, Gebühr 6,12 €, RE 28 %. Grenzbestellwert = 5,68 / 0,28 = **20,29 €**, ohne Gebühr **42,14 €**. Angebot „gratis ab 50 €“: Wenn 35 % der 4.900 Aufträge darüber liegen, fallen 10.496 € Gebühren weg. Zum Ausgleich braucht es ≈ 1.517 neue Aufträge (+31 %). Festservice: 60 Kästen Kommission, 15 kommen ungeöffnet zurück (25 %). Ergebnis 45 × 3,04 € − 15 × 0,80 € − 70 € Fahrten = 55 € plus Garniturmiete.

#### M48 Konditionen- und Bonuscontrolling (Block F, HB1/2, IHK mittel, N)
- **Lernziele:** Bonusstaffeln hochrechnen (Anwenden). Stufensprünge und Vorkäufe bewerten (Bewerten). Rückvergütungen und Zentralregulierung abstimmen (Analysieren).
- **Formeln:**
  - Zielerreichung_FC = (Ist_YTD + Rest-FC) / Bezugsbasis.
  - Wert des Stufensprungs = Δ Bonussatz × Gesamtvolumen − Kapitalbindungskosten − Abschriftenrisiko.
  - Lohnt ein Vorkauf vor einer Preiserhöhung? Ersparnis Δp × Menge gegen Bestand × i × Tage/365 + Handling.
- **Alltag:** Bonus-Tracking (M), Hochrechnung zur Jahresendrallye (Q4), Bonusabrechnung (J, Januar), Prüfung der Preiserhöhungen (J, Herbst).
- **Voraussetzungen:** M08, M15, M31.
- **Typische Fehler:** Bezugsbasis falsch lesen (Einkauf oder Abverkauf, Vorjahr oder Plan). Rückwirkende Staffel als Grenzstaffel rechnen. Bonusforderung nicht abgrenzen.
- **Übung:** Brauerei Nord, Vorjahr 20.000 Kästen à Ø 12,00 €. Staffel 1 % ab 90 %, 2 % ab 100 %, 3 % ab 110 %. Forecast per 30.11.: 19.700 Kästen (98,5 %), also 1 % = 2.364 €. Mit 300 Kästen Vorkauf im Dezember: 2 % auf 20.000 = 4.800 €, **Δ +2.436 €**. Dagegen stehen 3.600 € gebundenes Kapital für 6 Wochen (≈ 42 € Zinsen bei 10 %) und 6 Paletten Stellfläche im Silvester-Peak. Klausel prüfen: Zählt nur der Abverkauf laut Kasse, ist der Vorkauf wertlos. Das ist zugleich Bilanzpolitik (Bestand per 31.12.).

#### M49 Steuercontrolling und Steuerplanung im KMU (Block D, HB2/3, IHK mittel, N)
- **Lernziele:** Steuerzahlungen in den Liquiditätsplan einbauen (Anwenden). Ertragsteuern planen (Anwenden). Gestaltungshebel wie Dauerfristverlängerung, GGF-Gehalt und Ausschüttung bewerten (Bewerten).
- **Formeln und Recht:**
  - GmbH 29,825 % bei Hebesatz 400 % (02) **[sicher]**.
  - Sondervorauszahlung = 1/11 der Vorjahres-USt-Zahllast (bei Dauerfristverlängerung) **[sicher]**.
  - Vorauszahlungstermine KSt 10.3./10.6./10.9./10.12., GewSt 15.2./15.5./15.8./15.11. **[sicher]**.
  - Ausschüttung: KapESt 25 % + Soli = 26,375 % **[sicher]**.
- **Alltag:** USt-Voranmeldung zuliefern (M), Steuerforecast (Q), Ausschüttungsentscheidung (J).
- **Voraussetzungen:** M02, M23.
- **Typische Fehler:** Steuern nur in der GuV planen statt nach Zahlungstermin. Vorauszahlungen auf Basis des Vorjahres vergessen. GGF-Gehalt ohne Angemessenheitsprüfung (vGA) erhöhen.
- **Übung:** Jahres-Zahllast ≈ 80 T€ **[Annahme]**. Die Sondervorauszahlung beträgt 7.273 €. Die Dauerfristverlängerung verschiebt jede Monatszahlung um einen Monat, im Juli sind das ≈ 9 T€ Liquiditätsgewinn genau im Kontokorrent-Engpass. Netto bleibt ein Vorteil von ≈ 1,7 T€ über die Saison **[Annahme]**.

#### M50 Finanzierung, Bankbeziehung, Covenants und Krisenfrüherkennung (Block D, HB2/3, IHK hoch, N)
- **Lernziele:** Kapitaldienstfähigkeit berechnen (Anwenden). Covenant-Headroom simulieren (Analysieren). Kredit gegen Leasing und Kontokorrent abwägen (Bewerten). 13-Wochen-Plan im Krisenmodus führen (StaRUG-Bezug aus M37).
- **Formeln:**
  - KDF = (JÜ + AfA + Zinsaufwand) / (Zinsen + Tilgung).
  - Covenant-Headroom = Ist-Kennzahl − Schwelle.
  - Dynamischer Verschuldungsgrad in zwei Varianten: Gesamt-FK oder nur verzinsliches FK.
- **Alltag:** Covenant-Reporting (Q), Bankgespräch (J), Kreditlinie verlängern (J), Krisenstatus (AH).
- **Voraussetzungen:** M22, M23, M25.
- **Typische Fehler:** Varianten des Verschuldungsgrads mischen. Leasing für „schuldenfrei“ halten (Banken rechnen Leasingverpflichtungen im Rating ein **[wahrscheinlich]**).
- **Übung (02):** KDF = (30,1 + 26,0 + 7,7) / (7,7 + 30) = **1,69**. Dynamischer Verschuldungsgrad: Gesamt-FK (325 − 67) / 56 = 4,6 Jahre, nur verzinslich (140 − 67) / 56 = 1,3 Jahre. Covenant EK-Quote ≥ 25 %: Wird die Kühlzelle (36 T€, aus 03) per Kredit finanziert, sinkt die Quote auf 126/487 = 25,9 %. Schon ein Verlust von **5,7 T€** bricht dann den Covenant. Lernpunkt zur Finanzierungsform.

#### M51 Verhaltensorientiertes Controlling und Anreizsysteme (Block A/H, HB5/6, IHK mittel, N)
- **Lernziele:** Budget-Slack, Goodhart-Effekte und Denkfehler (Anker, Sunk Cost, Bestätigungsfehler) erkennen (Analysieren). Prämienformel mit Malus und Deckel entwerfen (Erschaffen).
- **Formel:** Prämie = min(Deckel; Satz × max(0; Ist − Ziel)) − Malus.
- **Alltag:** Budgetgespräche (J), Zielvereinbarung (J), Kommentarprüfung auf Ausreden (M).
- **Voraussetzungen:** M01, M18.
- **Typische Fehler:** Eine Kennzahl allein incentivieren. Slack aufdecken und damit bloßstellen, statt treiberbasiert zu begründen.
- **Übung:** Sabine plant Personal 2028 mit +8 %. Treiber (Mindestlohn, Bons) ergeben +4,5 %, der Slack liegt also bei 3,5 % × 355 T€ ≈ 12,4 T€. Ziel „Out-of-Stock < 2 %“ führt zu Überbestellung: +20 T€ Bestand × 9 % = 1,8 T€ Zins plus MHD-Risiko. Gegenvorschlag: 5 % auf RE II über Plan, Malus bei Schwund > 0,5 %, Deckel 5 T€.

#### M52 Energie-, Anlagen- und Standortcontrolling (Block F, HB1/2, IHK niedrig, N)
- **Lernziele:** Energie-KPIs und TCO von Kühlmöbeln (Anwenden). Wartung gegen Ausfallrisiko (Bewerten). Mietvertrag und Indexmiete (Analysieren).
- **Formeln:**
  - kWh/m², kWh je Kühlmöbel.
  - Erwartungsschaden = p × S.
  - Indexmiete_neu = Miete × VPI_neu / VPI_alt.
- **Alltag:** Energie-Monitoring (M), Wartungsplan (J), Mietvertragsoptionen (AH, Jahre vorher).
- **Voraussetzungen:** M25, M37.
- **Typische Fehler:** Wartung als reine Kosten sehen. Optionsfristen im Mietvertrag verpassen.
- **Übung:** 10 Kühlmöbel × 3.000 kWh × 0,26 € = 7.800 €/Jahr. Nachtabdeckung (−15 %, 1.500 € Invest) spart 1.170 €/Jahr, KW (7 %, 8 Jahre) = 1.170 × 5,971 − 1.500 = **+5.486 €**. Wartungsvertrag Kühlzelle 900 €/Jahr senkt die Ausfallwahrscheinlichkeit von 10 % auf 4 % bei 15 T€ Schaden. Der Erwartungswert spart genau 900 €, also indifferent. Entscheiden müssen Risikoaversion und Lieferfähigkeit. Indexmiete +2,2 % = +2.495 €/Jahr.

#### M53 Daten-Handwerk: Kassendaten, Warenkorb, Datenmodell, Datenschutz (Block E, HB4, IHK mittel, N)
- **Lernziele:** Bon-Positionsdaten modellieren, als Fakt mit Dimensionen Artikel, Zeit und Wetter (Verstehen). Warenkorbanalyse durchführen (Anwenden). Korrelation von Wirkung trennen (Bewerten). DSGVO-Grenzen bei Kundenkarte und Personaldaten kennen (Erinnern).
- **Formeln:** Support = P(A∩B). Konfidenz = P(B|A). Lift = P(B|A) / P(B).
- **Alltag:** Ad-hoc-Abfragen (W), Datenqualitätsregeln (W), Kennzahlen-Glossar (J).
- **Voraussetzungen:** M28, M29.
- **Typische Fehler:** Lift als Kausalität lesen, obwohl Grillwetter Bier und Chips gleichzeitig treibt. Kundendaten ohne Rechtsgrundlage auswerten.
- **Übung:** 100.000 Bons. 30.000 enthalten L01, 8.000 Chips, 3.600 beides. P(Chips|L01) = 12 % gegen 8 %, also **Lift 1,5**. Rechnerisch „zusätzlich“ sind 3.600 − 2.400 = 1.200 Chips-Bons. Das liefert die Verbundzahl für M45, mit Warnhinweis. Für Unternehmen, die KI einsetzen, gilt seit 2.2.2025 die KI-Kompetenzpflicht nach Art. 4 KI-VO **[wahrscheinlich]**.

#### M54 ESG-Ergänzung: CO₂-Kosten, Kältemittel, Scope 3, Mehrweg (Block G, IHK niedrig, N)
- **Lernziele:** CO₂-Preis als Kostenart planen (Anwenden). F-Gas-Risiko in der Investitionsplanung berücksichtigen (Bewerten). Scope 3 abschätzen (Analysieren). Mehrwegquote als Sortiments-KPI nutzen (Anwenden).
- **Recht und Zahlen:**
  - Nationaler CO₂-Preis 2026 im Korridor 55–65 €/t. Für 2027 soll der Korridor bleiben, ETS 2 ist auf 2028 verschoben. **[wahrscheinlich]**: Gesetzentwurf im Bundestag, Verabschiedung offen.
  - Diesel ≈ 2,65 kg CO₂/l **[wahrscheinlich]**, das entspricht ≈ 14,6–17,2 ct/l netto CO₂-Preis.
  - R404A hat ein GWP von 3.922. Anlagen ab 40 t CO₂e dürfen nicht mehr mit Neuware ab GWP 2.500 befüllt werden **[wahrscheinlich, EU-F-Gas-VO]**.
- **Alltag:** CO₂-Bilanz (J), Kältemittel-Dichtheitsprüfung (J), Bank-/VSME-Fragebogen (AH).
- **Voraussetzungen:** M39, M25.
- **Typische Fehler:** Nur Scope 1/2 bilanzieren, obwohl beim Händler die eingekaufte Ware dominiert **[wahrscheinlich]**. Kältemittel nicht als Investitionsrisiko sehen.
- **Übung:** Kraftstoff 9.000 € ≈ 6.500 l ≈ 17 t → CO₂-Kosten ≈ 0,9–1,1 T€ p. a. Gas für Wärme ≈ 9 t. Strom 85 MWh × 0,363 ≈ 31 t (Faktor **[Vermutung]**, UBA-Wert prüfen). Eine Kühlzelle mit 20 kg R404A entspricht 78 t CO₂e und liegt damit über der 40-t-Schwelle. Im Investitionsantrag steht dann vorgezogener Ersatz gegen Weiterbetrieb.

#### M55 Teamführung, Selbstorganisation und schriftliche Kommunikation (Block H, **HB6**, IHK hoch, N mit Kniff)
- **Lernziele:** Ein Team für Inventur, Budgetworkshop oder Projekt planen und führen (Anwenden). Abschlusskalender unter Kapazitätsgrenze priorisieren (Bewerten). Entscheidungsvorlage und Bank-E-Mail schreiben (Erschaffen). Feedback geben (Anwenden).
- **Konzepte:** Delegation (Reifegrad), Feedback nach Situation–Verhalten–Wirkung, Eisenhower/Kapazitätsplan, Management Summary in fünf Sätzen, Glasl-Stufen (aus M43).
- **Alltag:** Wochenplanung (W), Abschlusskalender (M), Inventurleitung (J), Azubi-Anleitung (W).
- **Voraussetzungen:** M43, M08.
- **Typische Fehler:** Alles selbst machen. Feedback als Urteil über die Person. Vorlage ohne Empfehlung.
- **Übung:** Spielerstelle 20 h/Woche. Die Pflichtroutinen des Monatsabschlusses brauchen 14 h, also bleiben 6 h für Analysen. Der Spieler muss AT1-Aufgaben an Azubi Lena delegieren und ihre Fehlerquote kontrollieren. Inventur 31.12.: 2.800 SKU plus Leergut nach Gebindeart, 3 Zählteams. Zählplan, Zweitzählung bei Abweichung über 2 %, Nachbesprechung mit dem Team.

#### M56 Unternehmensbewertung und Nachfolge im KMU (Block C/H, HB5, IHK mittel, **N**)
- **Lernziele:** Bewertungsanlässe und -zwecke unterscheiden (Verstehen). Vereinfachtes Ertragswertverfahren und Multiplikator anwenden (Anwenden). Wertlücke zwischen Verkäufer und Käufer erklären (Bewerten).
- **Formeln:** Vereinfachtes Ertragswertverfahren: Jahresertrag × 13,75 (§ 203 BewG) **[sicher]**. EBIT-Multiple. DCF aus M21.
- **Alltag:** AH (Nachfolge, Bankanfrage, Gesellschafterwechsel).
- **Voraussetzungen:** M21, M22.
- **Typische Fehler:** Steuerwert mit Marktwert verwechseln. Ersatz des Inhaber-GF nicht einpreisen.
- **Übung:** Ø Betriebsergebnis 45 T€ × 0,7 = 31,5 T€ × 13,75 = **433 T€ Steuerwert**. Käufersicht: Fremd-GF kostet 70 statt 60 T€, das EBIT sinkt auf ≈ 40 T€; × 4–5 **[Vermutung]** ergibt 160–200 T€. Lernpunkt: Der Wert hängt vom Zweck ab. Für Karls Nachfolge (03) ist das der natürliche Endspiel-Bogen.

**Bewusst nicht ergänzt:** Produktions-, F&E- und IFRS-Konzerncontrolling. Am Getränkemarkt sind sie nur künstlich darstellbar; siehe 6.

---

## 2. Nachrechnung des Domänenmodells (02) und der Rechenbeispiele

### 2.1 Was stimmt (nachgerechnet) **[sicher]**
- Eröffnungsbilanz 451.000 € auf beiden Seiten, alle Teilsummen, Pfand im Vollgut 8.000 × 2,61 € = 20.880 €.
- Rohertrag I nach Warengruppen 575.985 € (26,79 %), Heimdienst 91.600 €, Festservice 47.500 €, zusammen 715.085 €.
- Sachkosten 317.360 €, Monatsverteilung (alle zwölf EBIT-Werte und die Kumulation), EBT 42.828 €, Steuer 12.773 €.
- Leitartikel: alle 24 Umsatz- und RE-Werte, Summe 877.682 € (35,1 %, RE 22,5 %), Pfand 273.230 € (ohne Kaution L23).
- Konditionskaskade 14,20 → 12,40 → 11,78 €, Biersteuer 0,94 €/Kasten, Buchungsbeispiel Pfand, Gewerbesteuer-Hinzurechnung unter dem Freibetrag.
- Break-even 2.350.756 € (Text: 2.350.735 €, Rundung), Sicherheitsabstand 6,0 %, Heimdienst-DB 6,92 €/Stopp.

### 2.2 Fehler und Korrekturen in 02

| Nr. | Stelle | Befund | Korrektur | Stufe |
|---|---|---|---|---|
| F1 | 2, 12.1 | Öffnungstage 2027: Mo–Sa sind 313 Tage, NRW-Feiertage auf Mo–Sa sind 9 (1.1., 26.3., 29.3., 1.5., 6.5., 17.5., 27.5., 1.11., 25.12.) | **304** statt 306; Kunden/Tag 329, Pfand/Tag ≈ 1.908 € | sicher |
| F2 | 7 | Prozentspalte summiert sich auf **99,6 %**. „Versicherung, Beratung, Sonstiges“ ist laut 12.7 55.400 € = 2,2 %, nicht 1,8 % | 2,2 % eintragen | sicher |
| F3 | 12.2 | Anlagendeckung II 171 % rechnet das ganze Darlehen langfristig. In der Liquidität stehen 30 T€ Tilgung aber als kurzfristig im Nenner (204 T€) | Einheitlich: (126 + 110) / 156 = **151 %** | sicher |
| F4 | 12.3 | „2,6 % des Wareneinsatzes“ ergibt 46.408 €, gebucht sind 46.733 € (2,62 %) | Quote 2,62 % nennen oder RE II auf 749,0 T€ anpassen | sicher |
| F5 | 12.4/12.6 | Sonderzahlungen laut Stamm (1.000 € + 3 × 500 €) × 1,245 = 3.112,50 €, im November sind 4.500 € geplant. Dazu Rundungsabweichungen: Fahrer 42.056 statt 42.048, Kasse 24.278 statt 24.270, Büro 25.896 statt 25.906; Summe 355.431 € | Sonderzahlung = 3.113 € oder Stamm ergänzen; Werte aus Formel generieren | sicher |
| F6 | 8 vs. 12.6 | Bedarf 330 h/Woche. Der Stamm bezahlt ≈ 334 h/Woche, produktiv nach 6 Wochen Urlaub und 7 % Krankenstand nur ≈ 272 h. **Lücke ≈ 58 h ≈ 1,5 VZÄ ≈ 45–50 T€** | Bedarf herleiten (≈ 270 h realistisch) oder Personal aufstocken; dann EBIT ≈ 3–5 T€ | wahrscheinlich |
| F7 | 12.2 | Kühlmöbel im Dezember „erst ab 2028 abgeschrieben“ | Pro rata temporis: 20.000 / 72 = **278 €** AfA 2027 (§ 7 Abs. 1 S. 4 EStG, handelsrechtlich analog) | sicher |
| F8 | 12.7 | „Kippt bei kostenloser Lieferung“ | Falsch: Der DB bleibt +0,80 €/Stopp. Er kippt ohne Gebühr erst unter **42,14 €** Bestellwert | sicher |
| F9 | 10, 12.8 | E-Rechnung für „jede Gastro- und Festservice-Rechnung“ | Nur B2B (Gastro, unternehmerisch tätige Vereine). Festservice an Privatleute bleibt B2C | sicher |
| F10 | 4.1 vs. 12.2 | Palettenpfand 8–15 €, Bilanz 250 Paletten = 5.000 € (20 €/Stück) | Bilanz 2,0–3,75 T€ oder Spanne anheben | sicher |
| F11 | 4.3, 12.2 | Posten „Leergut, Pfandgut“ als Umlaufvermögen neben der Ware | Ausweis als Erstattungsanspruch gegen Abfüller (sonstige VG), denn Leergut ist Eigentum des Abfüllers | wahrscheinlich (BFH I R 36/07, Verwaltungsauffassung) |
| F12 | 12.7 | Break-even linear. Der Jahresbonus L01 hängt an **12.000 Kästen, das ist exakt die Planmenge**. Bei −6 % Umsatz fallen 2 % × 12,40 € × 12.000 = **2.976 €** zusätzlich weg | Stufen im BEP berücksichtigen. Cash-BEP (+30 T€ Tilgung, −26 T€ AfA) = **2.364.700 €**, Sicherheitsabstand nur **5,4 %** | sicher |
| F13 | 12.3 | Der Plan-Cashflow ignoriert Steuer-Timing (Rückstellung 9 T€ ab), Bonuseingang (24 T€ zu) und Δ Working Capital | Indirekte Cashflow-Rechnung vollständig führen. Didaktisch ist sie gerade der Lerninhalt | wahrscheinlich |
| F14 | 4.3 | „BMF-Entwurf trennte Warenumschließungen (Flasche, Kasten) von Transporthilfsmitteln (Palette)“, Status offen | Laut BMF vom 05.11.2013 (geändert 2014) sind Flaschen **und Kästen** Warenumschließungen und teilen das Schicksal der Ware; Paletten sind Transporthilfsmittel (eigene Leistung). Ein neueres Schreiben ließ sich nicht finden | wahrscheinlich |
| F15 | 8, 12.6 | SV-Sätze 2026 für das Planjahr 2027 verwendet | Als Annahme kennzeichnen, Zusatzbeitrag 2027 ist offen | wahrscheinlich |
| F16 | 12.6 | Saisonkräfte mit Faktor 1,0 | U2, Insolvenzgeldumlage, BG und ggf. Pauschsteuer 25 % → Faktor ≈ 1,01–1,26 | wahrscheinlich |
| F17 | 2 | „trinkgut-Ableitung ≈ 360 Kunden/Tag bei 25 € Bon“ | 3,3 Mio. € / 306 / 25 € = 431 (brutto) bzw. 513 (netto). 360 ergibt sich erst bei ≈ 30 € Bon | sicher |
| F18 | 12.1 vs. 03 | Der Inhaber ist laut 02 „zugleich Marktleiter“, in 03 gibt es eine Marktleiterin Sabine | Rollen angleichen. Vorschlag: Sabine = „Stellv. Marktleitung“ aus dem Stamm | sicher (Inkonsistenz) |
| F19 | 12.2 | Startdatum 01.01.2027 (04: DayIndex 0) ist Neujahr, der Markt ist geschlossen | Erster Tick Sa 02.01.2027 | sicher |

### 2.3 Fehler in 01, 03, 04

| Nr. | Stelle | Befund | Korrektur | Stufe |
|---|---|---|---|---|
| E1 | 01 0.4 | AV 600 T€ bei Mietobjekt und AfA 30 T€ (≈ 20 Jahre Nutzungsdauer für Ladeneinrichtung) | AV ≈ 150–200 T€ oder eigene Immobilie (dann keine Miete 110 T€) | wahrscheinlich |
| E2 | 01 M05 | 52.000 / 32.000 Kisten pro Monat bei ≈ 230.000 Kisten im Jahr (Ø 19.000) | z. B. 24.000 (Juli) / 14.000 (Feb.) → kv 0,60 €, K_f 12.000 € | sicher (Mengen-Hochrechnung) |
| E3 | 01 M12 | 340.000 Kisten Leergut, plausibel sind ≈ 230.000 (1.000 T€ / 13,44 + 1.000 T€ / 6,45) | Satz 0,46 €/Kiste, Kundenbeispiel 0,60 € statt 0,75 € | wahrscheinlich |
| E4 | 01 M19 | Der Biertrend −2 % ist auf den gesamten Restumsatz angewendet | Nur auf den Bieranteil (≈ 42 %): FC **2.390,8 T€** statt 2.375,6 | sicher |
| E5 | 01 M24 | DPO und DSO aus Bruttobeständen gegen Netto-Wareneinsatz, obwohl 01 „Brutto/Netto mischen“ selbst als typischen Fehler nennt | Netto: DSO 3,8, DPO 18,7, **CCC ≈ 15,5 Tage** | wahrscheinlich (Konvention) |
| E6 | 01 0.4 | Personal 255 T€ ohne erkennbares GF-Gehalt (GmbH) | GF-Gehalt ausweisen, EBIT sinkt entsprechend | wahrscheinlich |
| E7 | 01 M26 | Plan-RE Mai 70 T€ bei 25 % erfordert 280 T€ Umsatz, mehr als im Juli (260 T€) | Plan-RE ≈ 57 T€ | sicher |
| E8 | 01 M02 | „BMF-Schreiben von 2021, mehrfach verschoben“ | siehe F14 | wahrscheinlich |
| E9 | 04 3.4 | Aushilfe 14,50 €/h liegt im Spieljahr 2027 unter dem Mindestlohn von 14,60 € | ≥ 14,60 € | sicher |
| E10 | 04 3.4 | Hitzewelle mit p = 1.500 bp/Tag ergibt über 78 Sommertage ≈ 11,7 Auslösungen. 02 nennt 60 %/Jahr | ≈ 117 bp/Tag mit langem Cooldown, oder einmal pro Saison ziehen | sicher |
| E11 | 04 3.3 | Samstag-Index 1,9. Aus 02 (Sa = 24 % der Woche) folgt 0,24 × 6 = **1,44** | Parameter aus einer Quelle | sicher |
| E12 | 03 1.2 | „R = 0,9^(Δt/S), Definition folgt FSRS“ | FSRS v4.5/v6 nutzt eine Potenzkurve, nur R(S) = 90 % stimmt überein. ts-fsrs (04) rechnet anders | wahrscheinlich |
| E13 | 03 C | „Jahresüberschuss aus der Investition 5.600 €“ | Gemeint ist ein Einzahlungsüberschuss vor Steuern. Eigenanteil 6.000 € in t₀ fehlt im Liquiditätsvergleich | sicher |

**Folgerung:** Kein Rechenbeispiel darf von Hand gepflegt werden. Alle Zahlen in Lernkarten müssen aus der Engine bzw. dem Startzustand generiert und per Test gegen den Golden Master geprüft werden. 04 sieht das technisch schon vor, 01 und 03 halten sich nicht daran.

---

## 3. Fehlende Getränkemarkt-Mechaniken mit hohem Controlling-Lernwert

Status: **neu** = nirgends vorgesehen · **Daten da** = Parameter in 02 vorhanden, aber nicht als Spielmechanik · **teilweise** = in 01/03/04 angerissen.

| # | Mechanik | Controlling-Lernwert | Kernparameter | Status |
|---|---|---|---|---|
| 1 | **Pfand-Float und Leergut-Stellplatz** (Abholrhythmus je Lieferant wählbar) | Working Capital, Engpass Fläche, Liquidität | 570 Kästen/Tag, 60 Stellplätze, 3,10–3,30 € | Daten da |
| 2 | **Leergutkonto-Abstimmung in Mengen** | IKS, Abstimmung, Fehlersuche | Saldo je Lieferant und Gebinde | teilweise (04 Nebenbuch) |
| 3 | **Silvester-Stichtag** (Leergut-Peak im Bilanzbild) | Bilanzpolitik, Stichtagsverzerrung | Rückstau 3.000 Kästen ≈ 9,3 T€ | teilweise (01 Text) |
| 4 | **Wetterprognose mit Fehlerband** (7-Tage-Vorschau, Ist kommt später) | Disposition unter Unsicherheit, Newsvendor, Prognosegüte | σ der Vorhersage, C_u/C_o | neu (02/04 kennen nur Ist-Wetter) |
| 5 | **Aktionskalender mit Brauerei** (Aktions-EK nur gegen Abverkaufsnachweis, Restmenge wird nachbelastet) | Promotionscontrolling, Abgrenzung | Lift, Kannibalisierung 50–70 %, Dip 15–25 % | Daten da (02 3.1) |
| 6 | **Konkurrenz-Handzettel jeden Montag** (Preisabstand bei Eckartikeln) | Preis- und Wettbewerbscontrolling | −30 bis −50 % Absatz bei fehlender Reaktion | Daten da |
| 7 | **Bonusstaffel-Klippe und Jahresendvorkauf** | Hochrechnung, Fehlanreiz, Bilanzpolitik | L01-Bonus exakt bei Planmenge | neu |
| 8 | **Preisrunde der Brauereien mit Vorkaufoption** | Spekulationskauf vs. Kapitalbindung | +0,50–1,00 €/Kasten | teilweise |
| 9 | **Heimdienst-Touren** (Stopps, Gebührenmodell, Leergutabholung) | Service-DB, Preisgestaltung, CO₂ je Stopp | 11,80 €/Stopp | Daten da |
| 10 | **Festservice-Kommission** (Rückläufer, Kaution, Schäden, Zahlungsausfall Vereine) | Kommissionslogik, Forderungsmanagement | Rückläufer 10–25 % | Daten da |
| 11 | **Mehrweg/Einweg-Sortimentsentscheidung nach Prozesskosten** | DB nach Prozesskosten, ESG-Zielkonflikt | Leergut 0,25–0,46 €/Kasten, Mehrwegquote | neu |
| 12 | **Fremdleergut-Sortierung** (sortieren, ablehnen, abschreiben) | Kosten-Nutzen, Kundenservice | 2 % Fremdleergut | Daten da |
| 13 | **Einweg-Clearing mit Zahlungsverzug** | Forderung, Abstimmung Automat vs. Gutschrift | Clearing-Lag **[Vermutung 2–4 Wochen]** | neu |
| 14 | **Pfandbon-Fraud und Kassendifferenz** | IKS, Stichprobe, Toleranzschwelle | 01 M38: 5,6 % Differenz | teilweise |
| 15 | **Jugendschutz-Testkauf** | Compliance-Kosten vs. Bußgeld (bis 50.000 €) | Schulung 2 h/MA | Daten da |
| 16 | **Regionaler Kalender** (Karneval in NRW, Schützenfeste, Brückentage, Vatertag) | Saisonindex, Personalplanung | Event-Multiplikatoren | teilweise (Karneval fehlt **[wahrscheinlich relevant für NRW]**) |
| 17 | **Steuertermine und Dauerfristverlängerung im Liquiditätsplan** | Liquidität, Steuerplanung | 10./15. jedes Monats/Quartals | neu |
| 18 | **Kartenquote und Zahlungsgebühren** | variable Kosten, Kassenprozess | 8.400 €/Jahr | Daten da |
| 19 | **Leihkühlschrank des Cola-Lieferanten mit Mindestabsatz** | Konditionen, Opportunitätskosten Fläche | Mindestabsatz, Energie | neu |
| 20 | **Kältemittel-/Kühlausfall-Ereignis** | Risiko, Investitionszeitpunkt, F-Gase | p = 10 %, 15 T€ | teilweise |

Am wertvollsten für das MVP sind **1, 4, 5, 7 und 9**. Sie sind branchentypisch, mit wenigen Parametern simulierbar und decken Working Capital, Prognose, Aktion, Konditionen und Service-DB ab. **[Vermutung]**

---

## 4. Widersprüche zwischen den Dateien

| Nr. | Thema | Widerspruch | Auflösungsvorschlag |
|---|---|---|---|
| W1 | Referenzbetrieb | 01/03: Durstlöscher (2,4 Mio., 800 m², RE 25 %, EBIT 60 T€, Bilanz 900 T€, 140.000 Bons). 02/04: 2,5 Mio., 900 m², RE II 30 %, EBIT 50,5 T€, Bilanz 451 T€, 100.000 Bons | **Ein** Betrieb, 02 als Basis (rechnerisch geschlossen, Golden Master in 04). 01-Beispiele daraus neu generieren |
| W2 | Leitartikel-Preise | Pils: EK 11,20 / VK 15,99 (01, 03) vs. 12,40 / 17,49 (02, 04). Aktions-EK 9,40 (01) vs. 8,60 (02). Wasser VK 7,69 (01) vs. 5,99 (02), EK 3,80 (03) | Artikelstamm aus 02 als einzige Quelle |
| W3 | Pfand-Bilanzmodell | 01: Pfandverbindlichkeit 50 T€, „steigt bei Mehrausgabe“. 02: keine Verbindlichkeit gegenüber anonymen Kunden. BFH I R 36/07: Erstattungsanspruch gegen Abfüller aktivieren, Kundenpfand gegenrechnen, erfolgsneutral | Entscheidungskarte. Empfehlung: Bruttomodell (Forderung gegen Abfüller und Verbindlichkeit gegenüber Kunden), weil es den Kreislauf sichtbar macht |
| W4 | Pfand auf Lieferantenrechnung | 02: 3,10 € brutto inkl. USt (2,61 netto). 03 Szene A: 3,10 € netto zuzüglich 19 % | Eine Konvention festlegen und als Lernkarte „Pfand netto/brutto“ erklären |
| W5 | Heimdienst/Festservice | 01: Szenario-Erweiterung S. 02: im Startzustand enthalten (350 T€ Umsatz, Forderungen, Pfandverbindlichkeiten) | 01-Eignung für M06, M14, M24, M33, M39 auf N setzen; nur Gastro-Großkunden bleiben S |
| W6 | Nachfrageparameter | Wetter: 02 +2,5 %/°C ab 20 °C (Wasser) vs. 04 +4 %/°C ab 22 °C. Elastizität Bier: 02 −2,5 bis −4 vs. 04 −1,8 vs. 01 −5,1. Hitzewelle: 02 Wasser +25–40 % vs. 04 ×1,6. Wochentag: E11 | Ein Parameterfile `markt.yaml`, 02 ist Quelle, 04 referenziert nur |
| W7 | Mastery | 03: 3 unassistierte Lösungen über ≥ 2 Tage plus zweites Format. 04: FSRS-Stabilität ≥ 21 Tage plus 2 Anwendungen im Spiel | Entscheidungskarte. Zwei Stufen trennen: „gelernt“ nach 03, „beherrscht“ nach 04 |
| W8 | Scheduler und Hinweise | 03: eigenes Rost-Modell, Aufgaben mit Hilfe zählen nicht. 04: ts-fsrs, „richtig mit Hinweis“ = Hard, erhöht die Stabilität | ts-fsrs nehmen; Hilfe → Again oder Hard per Entscheidungskarte; Rost-Anzeige als UI über FSRS-Retrievability |
| W9 | Wer entscheidet? | 05: „Du bist Controller, nicht Chef, der Inhaber entscheidet oft gegen deinen Rat.“ 03: Reigns-Karten, Spieler wählt und Balken reagieren | Spieler empfiehlt, Karl entscheidet mit einer Wahrscheinlichkeit, die von Vertrauen und Vorlagenqualität abhängt |
| W10 | Wiederholung durch Geschäftsrhythmus | 01: Spacing entsteht durch den Monatsrhythmus. 03: Spielzeit ≠ Echtzeit, wer sechs Monate an einem Abend spielt, hat nicht verteilt geübt | 03 hat recht **[sicher, Spacing-Befund]**; 01 korrigieren |
| W11 | Doppel-Gate | 03: Rost unter 0,70 sperrt Arbeitsschritte. 04: Monat endet erst nach Pflichtaufgaben. Zusammen blockiert das Spieler nach Pausen doppelt | Ein Gate pro Ebene, Auffrischer zählt zugleich als Pflichtaufgabe |
| W12 | Replay mit gleichem Seed | 03 braucht Kontrafaktum „genau eine Entscheidung geändert“. 04: ein Zufallsstrom pro Teilsystem; andere Entscheidungen verbrauchen andere Zufallszahlen, das Replay driftet | Zufallszahlen per Hash(seed, Tag, Artikel, Zweck) ziehen (Common Random Numbers) **[wahrscheinlich]** |
| W13 | „Vertical Slice“ | 03: 1 Jahr, 8 Module, 3 Figuren. 04: geskripteter Monat ohne Simulation (20–25 PT) | Begriffe trennen: „Lernprototyp“ (04) vs. „Vertical Slice“ (03) |
| W14 | Speicher | 05: Lernstand im localStorage. 04: IndexedDB/Dexie, localStorage nur für Einstellungen | 04 gilt |
| W15 | Kontenrahmen | 01/02: SKR03/04. 04: SKR04 | SKR04 (Bilanzgliederung näher an HGB) |
| W16 | Zielgruppe | 01: IHK-Controller als Rückgrat. 03: Azubis vs. Gründer offen. 05: Handelsfachwirte/Quereinsteiger primär | Entscheidungskarte A1 |
| W17 | Figuren | 02: Inhaber = Marktleiter. 03: Karl (Inhaber) und Sabine (Marktleiterin) | siehe F18 |

---

## 5. Offene Designentscheidungen (Kandidaten für Entscheidungskarten)

Format: Frage – Optionen – *Vorschlag* – Priorität (**P1** vor dem Prototyp, **P2** vor 1.0, **P3** später). Die Liste enthält 92 Kandidaten. Sie fasst 03 (12), 04 (14) und 05 (12) ohne Dubletten zusammen und ergänzt sie. Für das Limit von 100 Karten sollten zuerst die 45 P1-Fragen gestellt werden.

**A Zielgruppe und Anspruch**
1. Primäre Zielgruppe? Handelsfachwirt/Quereinsteiger / IHK-Controller / Azubis + Berufsschule / BWL-Studium / Inhaber – *Selbstlerner im Handel* – P1
2. Anspruch „alle Facetten“: vollständig (M01–M56) / IHK-Kern / Handelscontrolling-Kern + Ausblick – *Kern + Ausblick* – P1
3. Vorwissen: null / kaufmännische Ausbildung / Einstufungstest – *Einstufungstest* – P1
4. Tiefe: Verstehen / prüfungsreif / berufspraktisch – *berufspraktisch, Prüfungsmodus optional* – P1
5. Explizite Abdeckungskarte nach ContrPrV/Handelsfachwirt-VO? ja / nein – *ja* – P2
6. Zertifikat/„Arbeitszeugnis“-Export? ja / nein – *später* – P3

**B Rolle, Perspektive, Erzählung**
7. Spielerrolle: Controller / Controller mit Aufstieg / wählbar Inhaber – *Controller mit Aufstieg* – P1
8. Wer entscheidet: Spieler / Inhaber nach Empfehlung / gemischt – *Inhaber nach Empfehlung, Vertrauen als Hebel* – P1
9. Muss die Controller-Stelle sich selbst rechtfertigen (Meta-Ziel: Nutzen ≥ Kosten von 25,9 T€)? ja / nein – *ja* – P2
10. Tonalität: realistisch-trocken / humorvoll / gemischt – *realistisch mit Humor in Figuren* – P2
11. Figurenzahl im MVP: 3 / 5 / 6 – *3 (Karl, Sabine, Dr. Brand)* – P1
12. Darf der Markt pleitegehen (Game Over)? ja / nein, nur Krisenmodus – *Krisenmodus mit StaRUG-Kapitel* – P2
13. Narrativer Langbogen: Nachfolge / Expansion / Krise – *Nachfolge (M56)* – P2

**C Curriculum und Prüfungsbezug**
14. Modulreihenfolge: Lernpfad 01 / Kalenderpfad / frei – *Kalenderpfad mit Mindestvoraussetzungen* – P1
15. Szenario-Erweiterungen (Filiale, Holding, Lohnabfüllung): Teil der Kampagne / separate Fallstudien / weglassen – *separate Fallstudien* – P1
16. Produktions-/Konzerncontrolling: per Transfer-Mandat in fremder Branche / gar nicht – *Transfer-Mandat* – P2
17. Prüfungsmodus mit Zeitlimit (IHK-nah)? ja / nein – *ab 1.0* – P2
18. HB5-Projektarbeit simulieren (30-Tage-Beratungsprojekt im Spiel)? ja / nein – *ja, als Jahresprojekt* – P2
19. HB6 Präsentation: Folienbaukasten / Text / Video-Selbstaufnahme – *Folienbaukasten* – P3
20. ESG/KI-Module ab Version 1 oder später? – *M39/M54 ab 1.0, M30 später* – P2
21. Anteil Branchenspezifika (Pfand usw.) an der Lernzeit: ≤ 10 % / 10–20 % / frei – *10–20 %* – P2

**D Referenzbetrieb und Zahlenwelt**
22. Einziger Referenzbetrieb = 02 (2,5 Mio.)? ja / Durstlöscher / neu – *02* – P1
23. Spieljahr: 2027 fest / laufendes Kalenderjahr / fiktiv ohne Jahreszahl – *2027 fest, Rechtsstand versioniert* – P1
24. Startlage: gesund / knapp (Sicherheitsabstand 5–6 %) / Krise – *knapp* – P1
25. Personalproblem F6 lösen: Bedarf senken / Personal aufstocken (EBIT ≈ 4 T€) – *offen, Fachentscheidung* – P1
26. Standort: Stadtrand NRW / wählbar je Run – *NRW fest, später wählbar* – P2
27. Rechtsänderungen (Mindestlohn, Pfand, E-Rechnung) als jährliches Content-Update? ja / eingefroren – *eingefroren je Version* – P2
28. Realitätsgrad der Benchmarks: Spannen anzeigen / Punktwerte – *Spannen mit „Annahme“-Hinweis* – P2
29. Zahlenformat: T€ / € auf Cent – *€ auf Cent in Belegen, T€ in Berichten* – P2

**E Buchhaltung und Pfand**
30. Bucht der Spieler selbst? nie / in Lernmodulen / immer – *in Lernmodulen* – P1
31. Pfand-Bilanzmodell: brutto (Forderung + Verbindlichkeit) / netto (02) – *brutto* – P1
32. Pfand auf Lieferantenrechnungen netto + USt oder brutto? – *eine Konvention, Lernkarte* – P1
33. Skonto auf Pfand erlaubt? nein (03) / je Lieferant – *je Lieferant als Konditionsmerkmal* – P2
34. Kontenrahmen SKR04 vereinfacht (≈ 60–80 Konten)? ja / SKR03 – *SKR04* – P2
35. Kalkulatorische Kosten in der KLR-Schicht ab Start? ja / ab Modul M04 – *ab M04* – P2

**F Kern-Loop, Zeit, Tempo**
36. Taktung: 1 Spielmonat ≈ 20 min / frei vorspulbar – *20 min, Vorspulen bis Ereignis* – P1
37. Tagessimulation sichtbar (Kassentage) oder nur Monatsergebnis? – *Tage im Zeitraffer, Eingriff nur bei Karten* – P1
38. Entscheidungskarten pro Monat: 3–6 / mehr – *3–6* – P1
39. Dritte Kartenoption „Prüfauftrag“ (kostet Zeit, öffnet Rechnung)? ja / nein – *ja* – P1
40. Zeitdruck-Modus (Papers, Please) Pflicht ab Mastery / Kür – *Kür* – P2
41. Kampagne mit festen Ereignissen oder Roguelite-Seeds ab Jahr 2? – *Jahr 1 fest, ab Jahr 2 Seeds* – P2
42. Wie viele Spielmonate pro Kalendertag zählen als Wiederholung? 1 / 2 / unbegrenzt – *1* – P1

**G Wiederholung, Mastery, Gates**
43. Echtzeit-Rost (03) ja / nur Spielzeit – *Echtzeit* – P1
44. Scheduler: ts-fsrs / eigenes Rost-Modell – *ts-fsrs* – P1
45. Tägliche Wiederholung: Pflicht / überspringbar / abschaltbar – *Pflicht bei Rost, max. 10 Items* – P1
46. Mastery-Definition: 03 / 04 / zweistufig – *zweistufig* – P1
47. Rost-Konsequenz: Sperre / Warnung / Delegation gegen Geld – *Sperre mit Delegationsoption* – P1
48. Lösung mit Hilfe: zählt nicht / zählt als Hard – *zählt nicht für Mastery, wird aber geplant* – P1
49. Obergrenze Pflichtanteil je Session: 25 % / 30 % / frei – *30 %* – P2
50. Streaks und Ligen? keine / Streak ohne Liga / beides – *Streak ohne Liga* – P2
51. Schnelleinstieg für Kundige (Fading überspringen per Test)? ja / nein – *ja* – P1
52. Akzeptierte Gesamtdauer bis „alle Kernmodule beherrscht“: 3 / 6 / 12 Monate Echtzeit – *6–9 Monate* – P1

**H Aufgaben, Feedback, Bewertung**
53. Eingabeform: Zahl tippen / Multiple Choice / gemischt – *Zahl tippen, MC selten* – P1
54. Toleranzen: streng (±1 €) / großzügig (±0,5 %) – *je Größenart wie 03* – P2
55. Folgefehler-Teilpunkte? ja / nein – *ja* – P2
56. Sicherheitsregler vor Abgabe (Kalibrierung)? ja / nein – *ja* – P2
57. Pflicht-Nachbesprechung nach jedem Monat? ja / überspringbar – *ja, 3–5 min* – P1
58. Kontrafaktisches Replay im Debriefing? ja / nein – *ja (erfordert W12-Lösung)* – P1
59. Quartals-Audit mit alten Fehlern? ja / nein – *ja* – P2
60. Freitext: Satzbausteine / LLM-Rubrik / beides – *Satzbausteine, LLM optional ab 1.1* – P2

**I Kommunikation und Soft Skills**
61. Gesprächssimulation mit Einwänden: Dialogbaum / LLM-Rollenspiel – *Dialogbaum* – P2
62. Berichte schreiben: Satzbaustein-Builder / Folienbaukasten / Freitext – *Builder* – P1
63. Teamführung (HB6): über Azubi und Inventurteam / weglassen – *Azubi und Inventurteam* – P2
64. Verhandlungen mit Brauerei als Minispiel (BATNA, ZOPA)? ja / nein – *ja* – P2
65. Ethik-Dilemmata (private Rechnung, Bilanzpolitik)? ja / nein – *ja, mit Vertrauenskosten* – P2

**J Werkzeuge und Daten**
66. Eingebautes Rechenblatt: Lückentabellen / freier Formelmodus / beides – *beides, frei ab Modul M28* – P1
67. Excel-Export und „Baue nach“-Aufgaben? ja / nein – *ja* – P2
68. Rohdaten-Datenraum (Bon-Export, SQL-ähnliche Filter)? ja / nein – *ja ab M53* – P2
69. Glass Box: Jede KPI bis zum Beleg klickbar? ja / nur Formel – *ja* – P1
70. Diagrammstil IBCS-nah als Lerninhalt? ja / nein – *ja* – P2

**K Simulation und Zufall**
71. Zufall sichtbar (Seed anzeigen, Ereignis-Wahrscheinlichkeiten offen)? ja / nein – *Seed ja, Wahrscheinlichkeiten nach Modul M37* – P2
72. Wetter mit Prognosefehler (Mechanik 3/4)? ja / nein – *ja* – P1
73. Konkurrenz reagiert dynamisch auf eigene Preise? ja / nur Ereignisse – *einfache Reaktionsregel* – P2
74. Mehrdeutige Fälle ohne eindeutige „wahre Ursache“? ja / nein – *ja, ab Stufe III* – P2
75. Schwierigkeit adaptiv (Elo) oder fest? – *adaptiv* – P2
76. Ereignisdichte: 2–3 / 4–6 pro Monat – *2–3* – P2

**L Technik und Plattform**
77. Plattform Stufe 1: PWA / Backend / Desktop – *PWA* – P1
78. Framework: Angular / React / Svelte – *Angular* – P1
79. Open Source? nein / MIT / GPLv3 (HyperFormula möglich) – *offen* – P1
80. Zielgeräte: Desktop + Tablet / auch Smartphone voll – *Desktop + Tablet, Smartphone für Wiederholung* – P1
81. Erst Lernprototyp ohne Simulation (20–25 PT) oder MVP mit Engine (40–60 PT)? – *Lernprototyp* – P1
82. Klassenmodus: nie / Datei-Abgabe / Server – *Datei-Abgabe* – P2
83. Ranglisten: keine / lokal / global – *keine* – P3
84. Domain: Subdomain / eigene – *Subdomain* – P3
85. Begehbare Marktansicht (2D) oder reine UI? – *reine UI mit SVG-Marktplan* – P2

**M Inhalte und Produktion**
86. Wer schreibt und prüft Inhalte: Auftraggeber / KI + Fachreview / extern – *KI-Entwurf + Fachreview* – P1
87. Inhalte erst für 1 Modul messen, dann planen? ja / nein – *ja* – P1

**N Recht, Ethik, Alkohol**
88. Marken: fiktive Archetypen / Gattungen – *fiktive Archetypen* – P1
89. Alkoholanteil: realistisch / Schulversion umschaltbar – *umschaltbar* – P2

**O Distribution und Geld**
90. Monetarisierung: kostenlos / Portfolio + Lehrkraftpaket / Freemium – *kostenlos + Portfolio* – P1
91. Sprache: Deutsch / Englisch vorbereiten – *Deutsch, i18n-fähig* – P3

**P Endspiel und Progression**
92. Endspiel: Nachfolge-Bewertung / Transfer-Mandat fremde Branche / beides – *beides* – P2

---

## 6. Falsche Prämissen und Blindstellen von „alle Facetten an EINEM Getränkemarkt“

1. **Einen Controller gibt es in diesem Betrieb real nicht.** Bei 2,5 Mio. € Umsatz und 14 Köpfen erledigen Inhaber und Steuerberater das Controlling **[wahrscheinlich]**. Die Spielerstelle (20 h, 25.906 €) kostet **51 % des EBIT** (50.528 €). Wird das nicht thematisiert, lernt man eine Rolle in einer Umgebung, in der es sie kaum gibt. Gegenmittel: Die Stelle muss ihren Nutzen nachweisen (Karte 9). Das ist selbst eine Controlling-Lektion (Kosten-Nutzen des Controllings).
2. **Viele Facetten existieren erst ab einer Größe**, die ein Einzelmarkt nicht hat: Konzern/Konsolidierung, Verrechnungspreise, Center-Steuerung, Kapitalmarkt/WACC, Budgetverhandlungen mit vielen Kostenstellenleitern, ERP-/Planungssysteme, Controlling-Organisation, **Führung eines Controller-Teams**. Die Holding-Erweiterung aus 01 wirkt bei 2,5 Mio. € künstlich. Realistisch ist nur die Betriebsaufspaltung Immobilien-GmbH plus Betriebs-GmbH **[wahrscheinlich]**.
3. **Die IHK-Prüfung ist industriegeprägt** **[wahrscheinlich]**. BAB mit Fertigungsstellen, Maschinenstundensätze, Äquivalenzziffern, Bestandsveränderungen und Plankosten in der Produktion kommen im Handel nicht vor. Die Lohnabfüllung als Szenario ist ein Kunstgriff. Ehrlicher ist das Transfer-Mandat in fremder Branche (03), dann aber nicht mehr „an einem Getränkemarkt“.
4. **75 % der IHK-Note sind kaum spielbar.** Projektarbeit 45 % und mündliche Prüfung 30 % (§ 7 Abs. 4 ContrPrV) **[sicher]**. Ein Spiel kann Teilfertigkeiten trainieren (Struktur, Rechnung, Satzbausteine), aber weder eine 30-tägige Beratungsarbeit noch ein Fachgespräch zuverlässig automatisch bewerten. „Alle Facetten erlernbar“ heißt deshalb nicht „prüfungsreif“.
5. **Soft Skills lassen sich per Dialogbaum erkennen, nicht beherrschen.** Moderation, Konfliktgespräch und Verhandlung brauchen echtes Gegenüber und Feedback. Ein LLM-Rollenspiel hilft, ist aber nicht verlässlich bewertbar (03, 04). Ohne Präsenz- oder Peer-Anteil bleibt HB6 Wissen über Kommunikation.
6. **Handelscontrolling ist ein Spezialfall**: Rohertrag statt Herstellkosten, triviale Kostenträgerrechnung, kaum Bestandsveränderungen, Pfand als Unikat. Die Gefahr ist Nahtransfer ohne Ferntransfer **[sicher, Transferbefund 03]**. Wer nur am Getränkemarkt lernt, rechnet später auch in der Industrie in Rohertrag.
7. **Jahresaufgaben bekommen zu wenig Wiederholung.** Budget, Inventur, Jahresabschluss, Strategieklausur und Bankrating kommen einmal pro Spieljahr, also etwa alle 5 Stunden Spielzeit. Bei Echtzeit-Spacing reicht das für Monatsroutinen, nicht für Jahresroutinen. Gegenmittel: Mini-Zyklen (Quartals-Forecast, Bank fragt unterjährig, Übungs-Abschlüsse außerhalb der Kampagne).
8. **Die Rechnung „Wiederholung ist Pflicht × alle Facetten“ geht nur über Monate auf.** Bei ≈ 300 Skills (43–56 Module × 3–8 Wissenskomponenten je Zelle laut 03) und ≈ 7 Wiederholungen je Skill bis zur Stabilität sind es ≈ 2.100 Abrufe. Bei 8 pro Tag dauert das ≈ **260 Tage tägliches Üben**, zusätzlich zur Spielzeit **[Vermutung]**. Entweder die tägliche Last steigt, oder das Ziel heißt „Kern + Ausblick“ (Karte 2, 52).
9. **Ein Ein-Personen-Projekt kann den Inhalt nicht abdecken.** Laut 04 kostet 1.0 160–280 PT, davon 65–130 PT Inhalt. Im Hobbytempo von 1,5 PT pro Woche sind das 2–3,5 Jahre. Mit M44–M56 kommen 20–40 PT dazu. Die Vollständigkeit ist das größte Projektrisiko, nicht die Technik.
10. **Die Zahlenwelt ist nicht belegt.** 02 sagt selbst: Öffentliche Betriebsvergleiche für Getränkefachmärkte fehlen, alle Quoten sind Vermutungen. Lernende verinnerlichen trotzdem Benchmarks („RE II 30 % ist normal“). Gegenmittel: Spannen statt Punktwerte, Annahme-Kennzeichnung im Spiel, fachliche Prüfung durch eine Person aus der Branche.
11. **Die Fragilität des Modells wird unterschätzt.** Ein einziger Plausibilitätsfehler (F6, ≈ 1,5 VZÄ) verschiebt das EBIT von 50 auf ≈ 5 T€. Wenn kleine Annahmen das Ergebnis kippen, kippen auch die Lehrsätze („Der Markt ist knapp profitabel“). Jede Grundannahme braucht Sensitivität und Golden-Master-Tests.
12. **Die Simulation kennt immer die „wahre Ursache“.** In der Realität sind Abweichungen höherer Ordnung, Mix-Definitionen und Ursachenketten nicht eindeutig zerlegbar, und Daten sind lückenhaft. Ein Spiel mit stets genau einer richtigen Antwort trainiert eine falsche Sicherheit. Gegenmittel: mehrdeutige Fälle mit mehreren vertretbaren Lösungen und Begründungsbewertung (Karte 74).
13. **Die Grenze zu Buchhaltung und Steuerberatung verschwimmt.** Belegprüfung, USt, Buchungssätze und Kassenführung sind überwiegend Buchhaltung. Im Papers-Please-Muster (03) können sie die Spielzeit dominieren. Dann lernt man Buchhalter, nicht Controller. Gegenmittel: Belegarbeit begrenzen (≤ 20 % der Monatszeit) und schrittweise an Azubi oder Steuerberater delegieren.
14. **Keine echten Werkzeuge.** HB4 wird 240 Minuten am Tabellenkalkulationsprogramm geprüft **[sicher, 01]**, in der Praxis kommen ERP und BI hinzu. Ein eingebautes Mini-Rechenblatt ist nicht Excel. Ohne Export- und „Baue nach“-Aufgaben fehlt der Werkzeugtransfer.
15. **Rechtsstand altert jährlich.** Mindestlohn, Minijob-Grenze, Pfand (PPWR, VerpackDG), E-Rechnung, CO₂-Preis und CSRD ändern sich laufend. Ein auf 2027 fixiertes Spiel ist 2029 in Details falsch. Entweder friert man den Rechtsstand ein und versioniert ihn, oder es braucht einen Pflegeprozess (Karte 27).
16. **Alkohol als Kulisse begrenzt die Zielgruppe.** Für Schulen mit Azubis ab 16 ist ein Biermarkt heikel (05). Für eine Schulversion braucht es einen Sortimentsschalter, und Werbeanschein muss vermieden werden.
17. **Die Kernfrage bleibt offen: Spaß oder Pflicht?** Echtzeit-Gates, Pflichtwiederholung und Abschluss-Sperren sind lernwirksam, aber genau das, was Freizeitspieler vertreibt. Das Spiel muss sich bewusst für Lernende mit externer Motivation (Prüfung, Job) entscheiden. „Für alle“ funktioniert nicht.

**Fazit:** „Alle Facetten an einem Getränkemarkt“ ist als **Lernlandkarte** sinnvoll und als **Kampagne** zu groß. Belastbar ist das Versprechen: „Den Kern des Controllings (KLR, Planung, Abschluss, Berichtswesen, Beratung) an einem Getränkemarkt beherrschen, dazu Ausblicke auf Industrie, Konzern und Prüfung.“ **[Vermutung, Empfehlung]**

---

## 7. Quellen

- Nachrechnung: eigenes Skript über alle Zahlen aus 01–04 (Bilanz, GuV, Monatsplan, Leitartikel, Break-even, Feiertage NRW 2027), 19.10.2026.
- ContrPrV § 7 (Gewichtung 25/45/30) und § 4 Abs. 1, 2, 4, 6 (Suchauszüge): https://www.gesetze-im-internet.de/contrprv/__7.html · https://www.gesetze-im-internet.de/contrprv/__4.html · https://www.buzer.de/gesetz/7281/v143552.htm
- DIHK-Fortbildungsstatistik 2025 (Controller: 82 Prüfungsteilnehmende, 54 bestanden): https://www.dihk.de/resource/blob/182428/f042794cd59a86fff2b781cccc93e14a/fachkraefte-weiterbildungsstatistik-2025-data.pdf
- USt bei Pfand / Transportbehältnissen (BMF 05.11.2013, Änderung 2014): https://www.haufe.de/steuern/finanzverwaltung/bmf-umsatzsteuer-bei-hin-und-rueckgabe-von-transportbehaeltnissen_164_206484.html · https://www.iww.de/mbp/steuern-und-bilanzierung-aktuell/umsatzsteuer-umsatzsteuer-bei-pfandgeldern-fuer-transporthilfsmittel-und-warenumschliessungen-f74100
- Bilanzierung Pfand/Leergut (BFH I R 36/07): https://www.rechtslupe.de/steuerrecht/einkommensteuer/einkommensteuer-betrieb/leergut-pfand-in-der-bilanz-330285 · https://www.anwalt24.de/urteile/bfh/2009-10-06/i-r-36_07
- CO₂-Preis 2027 und ETS-2-Verschiebung: https://www.advant-beiten.com/aktuelles/behg-novelle-co2-preis-bleibt-2027-im-korridor-von-55-bis-65-euro · https://www.ey.com/de_de/technical/steuernachrichten/referentenentwurf-zum-dritten-behg-aenderungsgesetz-stabilisierung-des-co2-preises-fuer-2027
- Controller-Kompetenzen: https://www.controllerakademie.de/wp-content/uploads/2024/01/ICV_IGC_Grundsatzpapier_DE.pdf · https://www.springer.com/us/book/9783658296582 · https://opus4.kobv.de/opus4-fhws/files/1817/Baltzer_FB_Kompetenzen_Controller.pdf
- Aus Fachwissen, nicht neu geprüft: § 203 BewG (Kapitalisierungsfaktor 13,75), § 7 Abs. 1 S. 4 EStG (pro rata temporis), Dauerfristverlängerung (§§ 46–48 UStDV), Vorauszahlungstermine KSt/GewSt, KapESt 25 % + Soli, EU-F-Gas-VO 2024/573, Art. 4 KI-VO, E-Rechnungspflicht nur B2B (§ 14 UStG n. F.).
