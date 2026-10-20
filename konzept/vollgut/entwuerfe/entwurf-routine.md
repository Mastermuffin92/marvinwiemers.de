# Entwurf „Routine-first“: Der Controlling-Schreibtisch einer Getränkegruppe

Stand 19.10.2026. Sicherheitsstufen: **[sicher]** belegt oder nachgerechnet · **[wahrscheinlich]** starke Ableitung · **[Vermutung]** Designannahme oder gefüllte Lücke. Alle Betriebszahlen sind Annahmen; die Gruppe-Zahlen stammen aus dem skriptgeprüften Startbetrieb in 08 (Variante **ohne Kelterei**). Neue Zahlen (Hausmarke, Make-or-Buy, Szenen) habe ich per Skript nachgerechnet (`(Rechenskript des Entwurfs, nicht abgelegt)`, `make.py`). Beträge in T€, in Belegen in €.

---

## 1. Kurzfassung und Arbeitstitel

**Arbeitstitel:** „SALDO – Der Controlling-Schreibtisch“ (Alternativen: „AT5“, „Kastenbilanz“; vor Veröffentlichung im DPMA-Register prüfen, 05).

1. Der Spieler ist Controller/in der fiktiven {NAME}-Getränkegruppe: GFGH-KG, Märkte-GmbH mit drei Abholmärkten und eine Hausmarke Apfelschorle in Lohnabfüllung; Konzern-Außenumsatz 22.000 T€, EBIT 318,4 T€.
2. Gespielt wird ein Schreibtisch im Stil von „Papers, Please“ mit Posteingang, wachsendem Regelbuch, Stempeln, Rückfragen und Gesprächen. Die Simulation erzeugt im Hintergrund Belege, Auszüge und Berichte, entscheiden tut die Geschäftsführung.
3. Den Kern bilden Pflichtroutinen: Monatsabschluss AT1–AT5, Leergutkonten in Stück, Bonus-Tracking, Liquiditätsvorschau, Covenant-Zertifikat und Budgetrunde.
4. Ihr Regelwerk wächst über drei Kapitel (Pilotmarkt → Großhandel → Gruppe). Ab Spieljahr 2 kommt der Abfüll-Bogen dazu: Lohnabfüller-Kalkulation prüfen, Plan-BAB und Make-or-Buy einer eigenen Linie.
5. Gemeisterte Methoden schalten Werkzeuge frei, die mehr sichtbar machen („Wissen ist Sicht“). Verblasst das Wissen, beschlagen sie.
6. Wiederholung ist zweifach Pflicht: in den Routinen und in einer täglichen 5-Minuten-Frühschicht, die ts-fsrs in Echtzeit plant.
7. Jeder Inhalt hängt über Skill-IDs an vorläufigen Lernziel-IDs je IHK-Handlungsbereich. Die Lehrgangsskripte werden später per Datenzuordnung angedockt.
8. Ehrlich: Gut trainiert wird der schriftliche Teil (25 % der Note), Projektarbeit und Fachgespräch (75 %) nur in Teilfertigkeiten. Der kleinste Beweis ist ein Schreibtisch-MVP mit zwei Spielmonaten Markt 1 in ≈ 31–44 PT.

---

## 2. Ehrliche Grenzen und Umgang

| Grenze | Befund | Umgang im Konzept |
|---|---|---|
| **75 % der Note sind Projektarbeit (45 %) und Mündlich (30 %)** | § 7 Abs. 4 ContrPrV **[sicher, 06]**. Eine 30-Tage-Arbeit im eigenen Betrieb und ein Fachgespräch kann kein Spiel automatisch bewerten **[sicher]** | Eigene Werkstätten für HB5 und HB6 (Kap. 10). Trainiert werden Struktur, Rechnung, Argumentation und Einwandbehandlung. Ein Bildschirm „Was dieses Spiel nicht kann“ empfiehlt menschliches Feedback (Dozent, Peer) und einen Transferbogen fürs eigene Unternehmen |
| **Pflicht-Wiederholung aller Facetten kostet Zeit** | ≈ 280 Skills × 6–7 Abrufe bis Stabilität 21 Tage ≈ 1.900 Abrufe **[Vermutung, Rechnung wie 06 #8]** | Etwa die Hälfte der Abrufe stecken die Routinen selbst. Rest über die Frühschicht (≤ 10 Items). Kern (≈ 180 Skills) ≈ 5–6 Monate, alles ≈ 9–10 Monate Echtzeit bei 4 Spieltagen pro Woche. Stufe „Kern Pflicht, Rest Kür“ als Entscheidungskarte (Kap. 14) |
| **HB4 wird 240 min am Tabellenkalkulationsprogramm geprüft** | **[sicher, 01]**; ein eingebautes Rechenblatt ist kein Excel | Excel-Werkstatt mit Datenpaket, xlsx-Abgabe und automatischer Prüfung benannter Zellen (Kap. 10) |
| **Industrie-KLR nur über Lohnabfüllung + Make-or-Buy** | Ohne Kelterei gibt es kein Kuppelprodukt, keine Saisonpressung und Bestandsveränderungen nur bei Kauf **[sicher]** | Plan-BAB, Maschinenstundensatz, Äquivalenzziffern und Plankosten sind Pflichtstoff des Bogens. Bei Nichtkauf läuft eine Open-Book-Klausel: Der Lohnabfüller liefert monatlich einen Kostennachweis, den der Spieler prüft. Industrie-KLR wird dann an fremden Zahlen geübt. Mehrstufige Fertigung und Kuppelkalkulation bleiben Frühschicht-Transferfälle |
| **Größere Simulation = mehr Bauaufwand** | +80–130 PT gegenüber dem Einzelmarkt **[Vermutung, 08]** | „Routine-first“ braucht keine feine Simulation, nur glaubwürdige Dokumente: Großhandel nach Kundenklassen plus 12 benannte Kunden, Märkte 2/3 als Monatsaggregate, das MVP läuft auf Skriptdaten |
| **B2B-Einstieg ist abstrakter** | Kein Kassentag, keine Laufkundschaft **[sicher]** | Kapitel 1 spielt komplett im Markt 1 (Kasse, Kiste, Pfandbon). Erst danach wird die Zentrale geöffnet; Brauhaus und Eckkneipe sind wiederkehrende Figuren |
| **Routine kann ermüden** | Papers-Please-Muster lebt von Variation **[wahrscheinlich]** | Jeder Monat bringt neue Regel, Störung oder Figurendrama; Zeitdruck nur als Kür nach Mastery |
| **Buchhalter- statt Controller-Training** | Belegarbeit kann dominieren (06 #13) | Buchhaltung (2,5 VZÄ) bucht. Der Spieler prüft, stimmt ab, plausibilisiert und berät. Belegarbeit ≤ 20 % der Monatszeit, Delegation an die Azubi ab Kapitel 2 |
| **Zahlenwelt unbelegt, Simulation kennt die „wahre Ursache“** | Keine öffentlichen GFGH-Betriebsvergleiche **[sicher, 07/08]**; eindeutige Lösungen trainieren falsche Sicherheit (06 #12) | Spannen statt Punktwerte, Annahme-Kennzeichnung, Fachreview vor Release; ab Kapitel 2 mehrdeutige Fälle mit Begründungsbewertung |

---

## 3. Zielgruppen und Lernversprechen

**Primär:** Teilnehmende am Lehrgang „Geprüfte/r Controller/in (IHK)“ als Ergänzung zum Lehrgang, nicht als Ersatz. Bundesweit sind das nur ≈ 80–115 Prüflinge pro Jahr **[wahrscheinlich, 05]**. **Sekundär:** Junior-Controller und Quereinsteiger im Handel und Großhandel, Bilanzbuchhalter (KLR- und Abschluss-Teilmengen), Handelsfachwirte. **Nicht Zielgruppe:** Freizeitspieler ohne Lernziel (06 #17); Schulen nur mit Sortimentsschalter.

**Lernversprechen (messbar):**

| Nr. | Versprechen | Messung im Spiel |
|---|---|---|
| L1 | Markt-Monatsabschluss (6 Routinen) nach Kapitel 1 in ≤ 25 min mit ≤ 1 Diagnosefehler; Gruppenabschluss (≈ 20 Routinen) nach Kapitel 3 in ≤ 45 min | Zeit- und Fehlerprotokoll je AT |
| L2 | ≥ 90 % der Pflicht-Skills „beherrscht“; 30 Tage nach Kampagnenende ≥ 80 % korrekt im unangekündigten Re-Test | FSRS-Stabilität, Re-Test mit neuen Parametern |
| L3 | Probeklausuren HB1/HB2/HB3 im IHK-Stil (eigene Aufgaben, 180/180/90 min) mit ≥ 65 % der Punkte | Automatische Korrektur mit Folgefehlern |
| L4 | HB4: Berichtsmodell in ≤ 240 min in Excel oder Calc bauen; ≥ 90 % korrekte Abgabezellen, keine hartkodierten Zahlen in Formelzellen | xlsx-Upload-Prüfung |
| L5 | HB5: Projektbericht mit ≥ 6 von 8 Rubrik-Kriterien erfüllt; alle Zahlen engine-geprüft | Rubrik (Selbst-/Peer-Bewertung) + Zahlenprüfer |
| L6 | HB6: 15-min-Präsentation und Fachgespräch-Simulation mit ≥ 75 % korrekt beantworteten Fachfragen | Dialogbaum mit Zeitfenster |

Der Einstufungstest ist zugleich Prä-Test. **Nicht versprochen:** Bestehen, Gesprächskompetenz ohne menschliches Gegenüber, Ersatz der Projektarbeit im eigenen Betrieb.

---

## 4. Spielerrolle, Setting, Figuren

**Rolle:** Controller/in als Stabsstelle der Geschäftsführung (75 T€ Arbeitgeberkosten). Ohne Kelterei sind das **23,6 % des Konzern-EBIT von 318,4 T€**; die 20,6 % aus 08 gelten nur mit Kelterei **[sicher, nachgerechnet]**. Ein Meta-Ziel läuft mit: Die Stelle muss ihren Nutzen belegen. Ein „Nutzenlog“ summiert aufgedeckte Fehler, Einsparungen und vermiedene Fehlentscheidungen in €.

**Setting (08, Variante ohne Kelterei; Start Sa 02.01.2027, 304 Öffnungs- und 254 Liefertage, 06 F1/F19):**

| Größe | Wert |
|---|---|
| KG (GFGH + Zentrale) | Umsatz 20.678,4 T€ (davon 3.178,4 intern an Märkte), 600 Gastro- und 150 Wiederverkäuferkunden, 25 Streckenkunden, Objekt/Heimdienst, Veranstaltungen; 49,0 VZÄ, 15 Fahrzeuge |
| Märkte GmbH (EAV, Organschaft) | Markt 1 = korrigierter Referenzmarkt (nur Laden, 2.150 T€, 329 Kunden/Tag, EBIT 15,9), Markt 2 3,1, Markt 3 −14,8 T€ |
| Konzern | Außenumsatz 22.000,0; EBITDA 763,7; EBIT 318,4; Ergebnis nach GewSt 165,6 T€ |
| Bank (Covenants [Annahme]) | EK-Quote 28,6 % brutto / 30,9 % Pfand saldiert (≥ 25 %); NV/EBITDA 2,85 (≤ 3,5) zum 01.01.; KDF Plan 2,03 (≥ 1,2) |
| Pfand | Pfand-Float ohne Kelterei 341,7 T€ (1.057,5 − 535,8 − 180,0), Silvester-Überhang 30.000 Kästen = 79,0 T€ |
| Saft | wie 08 „ohne Kelterei“ bei fremder Kelterei bezogen; Saftkästen sind Pfandansprüche gegen diese |
| Hausmarke | Apfelschorle, Lohnabfüllung bei einem Mineralbrunnen (Datenblatt in 8.2) |

Übernommene Korrekturen u. a.: G9, G14, G15, G17, G19 (über 08), Pfand-Bruttomodell und Pfand brutto auf Rechnungen (W3/W4), Mindestlohn 14,60 € (E9), Samstag-Index 1,44 (E11), Hitzewelle ≈ 1 × pro Saison (E10).

**Warum Apfelschorle als Hausmarke** **[wahrscheinlich]:** Mineralwasser muss am Quellort abgefüllt werden, eine eigene Linie ohne Quelle wäre kein Make-or-Buy-Fall. Limonade fiele sicher unter die Zuckersteuer (26/32 ct/l ab 1.7.2027, Kabinettsentwurf, 08), die den Fall dominieren würde. Apfelschorle hat einen echten Rohstoff mit Preisrisiko (Konzentrat), ein Gastro-Gebinde 0,33 l und mit L14 eine Markenkonkurrenz im Markt. Ob fruchteigener Zucker unter die Steuer fällt, ist offen **[Vermutung]** und wird eine Ereigniskarte.

**Figuren:**

| Figur | Rolle | Lernfunktion |
|---|---|---|
| Jana Hagedorn (46) | Geschäftsführerin, Kommanditistin, 2. Generation | Adressatin, entscheidet nach Empfehlung (Vertrauen × Vorlagenqualität, 06 W9) |
| Karl Hagedorn (72) | Seniorchef im Beirat | Bauchgefühl, Einwände, Langbogen Nachfolge/Bewertung (M56) |
| Sabine Kowalski | Marktleiterin Markt 1 (bisher Stellvertreterin, 06 F18) | Pilotmarkt, Abweichungsgespräch, Prämie auf VP-Ergebnis (M51) |
| Ralf Brinkmann | Logistikleiter (Lager, Fuhrpark) | größter Kostenstellenleiter, Budget-Slack, Konfliktgespräch |
| Derya Demir | Leiterin Buchhaltung | liefert Saldenlisten, Fristenkonflikt, Abgrenzung Buchhaltung/Controlling |
| Mehmet Aydın | Außendienstleiter Gastro | Darlehensanträge, Umsatz- gegen DB-Denken |
| Lena Wolf | Azubi Groß- und Außenhandel, 2. Lj., ab Kapitel 2 | Delegation, Stichprobe, Feedback (HB6), macht typische Fehler |
| Dr. Matthias Brand | Steuerberater der Familie | Mentor, Worked Examples |
| Frau Lindqvist | Abschlussprüferin (KG prüfungspflichtig, 08) | „Citations“: Stichproben aus Vormonaten |
| Aylin Yilmaz | Hausbank | Covenants, Bankgespräch |
| Jens Otte | Außendienst Brauerei Nord | Staffeln, Aktions-EK, WKZ, Preisrunden |
| Uwe Hellwig | Betriebsleiter des Lohnabfüllers | Preiskalkulation, Verhandlung |

---

## 5. Spielschleifen

**5.1 Minute: ein Vorgang (1–3 min)**
1. Vorgang mit Absender, Frist und Anlage öffnen; das Regelbuch zeigt nur eingeführte Prüfregeln.
2. Werkzeug wählen: Arbeitsblatt, Datenraum-Suche oder Rückfrage (kostet Spielzeit).
3. Ergebnis und Betrag eintragen, stempeln (Freigabe / Rückfrage / Korrektur veranlassen / Eskalation), Sicherheitsregler setzen (50/70/90 %).
4. Feedback: bei Routinen sofort und diagnostisch, bei Entscheidungen später über die Zahlen. Eintrag in Fallakte, Nutzenlog und FSRS-Historie.

**5.2 Session (20–35 min):** Frühschicht (≤ 10 Items, ≈ 5 min) → 2–4 Schreibtischtage mit je 4–8 Vorgängen, dazwischen spult die Simulation zum nächsten Termin vor → Gespräch oder Entscheidungskarten (Ja / Nein / Prüfauftrag) → Feierabend mit Kurz-Debrief (2 min), Ausblick auf fällige Fristen und automatischer Sicherung.

**5.3 Spielmonat (≈ 25 min Spielzeit, Gate am Monatsende)**

| Termin | Routinen (Beispiele, Kapitel 2) |
|---|---|
| AT1 | Belegvollständigkeit, Leergut-Lieferscheine Fahrer gegen Lagerzählung, Kassen der Märkte |
| AT2 | Leergutkonten Lieferanten und Kunden in Stück je Gebindeart, Kreditoren-OP |
| AT3 | Abgrenzung Boni/WKZ/Kundenboni/Urlaub, Bestandsplausibilität |
| AT4 | Kostenstellen Soll-Ist (Fuhrpark je Fahrzeug), Segment- und Kunden-DB, Abweichungen |
| AT5 | Monatsbericht (Satzbaustein-Builder) und Monatsgespräch mit der GF |
| montags | 13-Wochen-Liquiditätsvorschau (1 Vorgang) |
| 10./15. | Steuer- und Lohnzahlungen in der Liquidität; Bonus-Tracking, hl-Meldung |
| laufend | 2–3 Ereignisse, 3–5 Anfragen und Karten (Darlehen, Aushilfe, Vorkauf) |

Der Monat schließt erst, wenn die Pflichtvorgänge bestanden sind (Gate aus 04). Das ist das **einzige** Gate (06 W11). Ein Frühschicht-Auffrischer zählt zugleich als Pflichtaufgabe.

**5.4 Spieljahr (GFGH-Kalender)**
- **Jan:** Inventur an 4 Standorten mit Leergut je Gebindeart, Saldenbestätigungen, Bonusabrechnung, Weitergabe der Preisrunden.
- **Feb–Apr:** Jahresabschluss und Prüfung der KG, Konzernrechnung für die Bank, Bankgespräch, Risikoinventur, Jahresgespräche mit den Brauereien.
- **Mai–Aug:** Saison mit Wetter-Disposition und Festen, Fahrer- und Leergutengpässe, Halbjahres-Forecast.
- **Sep:** Strategieklausur (Gedat-Trend, Segmentportfolio).
- **Okt–Nov:** Budget im Gegenstrom mit den Kostenstellenleitern, Investitionsplan, Herbst-Preisrunde.
- **Dez:** Bonus-Endspurt und Vorkauf, Silvester-Leergut, Abgrenzungen.
- **Quartalsweise:** Forecast, Covenant-Zertifikat, Konsolidierung light, Stichprobe der Prüferin.

**5.5 Kampagne (36 Spielmonate)**

| Kapitel | Spielmonate | Fokus | Neue Routinen | Freischaltung |
|---|---|---|---|---|
| 1 Pilotmarkt | 1–6 (Jan–Jun 2027) | Markt 1: KLR-Grundlagen, Handelskalkulation, Pfand, KER | R1–R6 (Pfandbon-Abgleich, Leergut intern, Neuartikel kalkulieren, Wareneinsatz/RE, Markt-KER, Monatsbericht) | Netto-Brille, Mengenlupe, Kalkulationsschieber; Zugang Zentrale |
| 2 Großhandel | 7–18 | Leergutkonten, Konditionen/Boni, Prozesskosten, Kunden-DB, Touren/Fuhrpark, Darlehen, Forderungen, erster Jahresabschluss | R7–R14 | DB-Spalten, Prozesskosten-Etikett, Staffel-Radar, Zahlungskalender; Delegation an Lena |
| Abfüll-Bogen | ab 13 (Jan 2028) | Lohnabfüller-Kalkulation, Make-or-Buy, Entscheidung zum Budget 2029 | bei Kauf R21–R23 (BAB, Plan-Ist, HK-Bewertung); sonst Open-Book-Prüfung | Maschinenstunden-Uhr |
| 3 Gruppe | 19–36 | Spartenrechnung, VP, Budget mit Kostenstellenleitern, Covenants, Konsolidierung light | R15–R20 | VP-Regler, Covenant-Tacho, Treiberbaum |
| Endspiel | ab 31 | Prüfungsjahr (HB4-Werkstatt, HB5-Projekt, HB6-Fachgespräch); Übernahmeangebot eines Konzern-GFGH (M56) | – | „Zeugnis“ |

Danach gibt es ein freies Spiel mit neuen Seeds (Krise, Wachstum, Brauereibindung). Kapitelinhalte schalten frei, sobald die Voraussetzungs-Skills „gelernt“ sind.

---

## 6. Lernsystem

**6.1 Theorie.** Jede neue Prüfregel kommt mit einer Theoriekarte (≤ 90 Wörter, Formel direkt an den Zahlen) und einem Worked Example von Brand mit Gruppenzahlen. Sie erscheint just in time, wenn die Regel erstmals im Posteingang gebraucht wird. Jede Karte trägt ihre Lernziel-IDs und, sobald vorhanden, den Skript-Verweis. Nach dem zweiten Fehler folgt ein Corrective in anderer Darstellung, z. B. Leergut als Palettenbild statt Tabelle.

**6.2 Praxis.** Jeder Vorgang ist eine parametrisierte Vorlage im Spielkontext: im Juni der eigene Juni-Wareneinsatz. Die Aufgabe nennt die Methode nie („Was bleibt uns bei 10,99?“). Je Skill gibt es 4 Fading-Stufen (vorgemacht → letzter Schritt fehlt → zwei Schritte fehlen → leer), adaptiv; Kundige überspringen per Einstufung. Nach dem Ersterwerb läuft alles gemischt, mit gezielten Kontrastpaaren (Liter- gegen Zeit-Äquivalenzziffer, Pfand brutto gegen netto).

**6.3 Wiederholung (Pflichtmechanik und Algorithmus).** Zwei Schleifen: Routinen im Spielkalender und die Echtzeit-Frühschicht. Der Scheduler ist ts-fsrs (FSRS v6). Die Rost-Anzeige ist nur eine UI über der FSRS-Abrufwahrscheinlichkeit R (06 E12/W8).
1. **Kandidaten:** eingeführte Skills mit R < 0,85 oder fälligem Termin.
2. **Priorität** = (0,85 − R) × IHK-Gewicht (hoch 1,5 / mittel 1,0 / niedrig 0,6) + 0,3 bei wiederholter Misconception (≥ 2 in 7 Tagen) + 0,2 bei mehr als 30 Tagen ohne Spielkontext-Anwendung **[Vermutung, Kalibrierung per Playtest]**.
3. **Auswahl:** N = min(10, max(5, fällige Items)). Nie zwei Items desselben Moduls hintereinander. Mindestens 1 Transfer-Item aus einem anderen Kapitel, bei Misconception-Flag ein Kontrastpaar.
4. **Instanz:** neue Zahlen per Seed (Spielstand, Skill, Wiederholungsnummer), abwechselnd synthetisch und aus dem Spielstand.
5. **Rating:** falsch oder Lösung angezeigt = Again, mit Hinweis = Hard (zählt nicht für Mastery), richtig = Good, richtig und schneller als der eigene Median = Easy (04).
6. **Zählregel:** je Skill und Kalendertag zählt nur ein Abruf, egal ob Frühschicht oder Routine (06 W10). Man darf beliebig viele Spielmonate am Tag spielen, es zählt aber nur einmal Wiederholung.
7. **Last:** Pflichtanteil ≤ 30 % der Session. Nach einer Pause verteilt der „Rückkehrmodus“ den Rückstau auf mehrere Tage (max. 10 pro Tag, Priorität aus Schritt 2).
8. **Konsequenz von Rost:** Bei R < 0,70 beschlägt das zugehörige Werkzeug. Es zeigt dann nur noch die Richtung („DB II: negativ“), keine Zahl, bis ein Auffrischer gelöst ist. Der Arbeitsschritt bleibt machbar, aber nur von Hand.
9. **Seltene Jahresroutinen** (Budget, Inventur, Jahresabschluss) bekommen Mini-Zyklen: Quartals-Forecast, unterjährige Bankanfragen, Übungsabschlüsse aus der „Archivakte“ (Markt 2/3, Vorjahre) in der Frühschicht.

**6.4 Mastery.**
- **„Gelernt“:** 3 korrekte, unassistierte Lösungen mit verschiedenen Parametern an ≥ 2 Kalendertagen plus 1 Lösung im zweiten Format (03). Das schaltet das Werkzeug frei.
- **„Beherrscht“:** FSRS-Stabilität ≥ 21 Tage plus ≥ 2 korrekte Anwendungen im Spielkontext (04). Bei IHK-hoch-Skills zusätzlich 1 Lösung im Prüfungsformat mit Zeitlimit. Das schaltet Effektvorschau und Delegierbarkeit frei (06 W7).
- **Lernziel beherrscht:** alle seine Skills beherrscht.
- **„Zeugnis“:** alle Pflicht-Lernziele beherrscht und zum Prüfungsjahr nicht eingerostet, dazu Probeklausuren HB1–HB4.

**6.5 Feedback und Debriefing.**
- **Drei Schichten** (03): sofort-diagnostisch bei Routinen, verzögert über Zahlen bei Entscheidungen, spät-sozial über Citations der Prüferin. Die Prüferin zieht quartalsweise 10 Vorgänge aus den bearbeiteten Vormonaten; jeder übersehene Fehler wird zur Aufgabe.
- **Monats-Debrief (3–5 min, Jahres-Debrief 15 min):** drei stärkste Veränderungen mit Vorhersage, Treiberbaum, Kontrafaktum und Lehrsatz fürs Notizbuch. Das Kontrafaktum ist ein Replay mit genau einer geänderten Entscheidung; Zufallszahlen per Hash (Seed, Tag, Objekt, Zweck) verhindern Drift (06 W12).

**6.6 Umgang mit Fehlern.** Fehler sind Fälle: Die Fallakte speichert z. B. „Jan 2028: Rügefrist Leergut versäumt, 261 €“ und spielt den Fall als Wiederholung zurück. Wer bei 90 % Sicherheit falsch lag, bekommt die betonte Erklärung (Hypercorrection). Folgen sind spürbar, aber reparierbar (Korrekturbuchung, Vertrauensdelle, Citation). Kein Game Over: Ein Covenant-Bruch löst einen Krisenmodus mit 13-Wochen-Plan aus (M50/M37).

**6.7 Lernziel-Architektur (Andockpunkt für die Skripte).** Vier Ebenen mit n:m-Verweisen:

| Ebene | Beispiel | Quelle, Änderbarkeit |
|---|---|---|
| Handlungsbereich | HB1 Kostenrechnung und Kostenmanagement | ContrPrV § 3, fest **[sicher]** |
| Lernziel-ID | `HB1.LZ07` „Maschinenstundensatz bilden und beurteilen“ | vorläufig aus 01/06 abgeleitet **[Vermutung]**; Feld `skript: []` bleibt bis zur Lieferung leer |
| Skill-ID | `kalk.mss.bilden`, `kalk.aez.zeitbasis` | Wissenskomponente, FSRS-Karte |
| Vorlage/Routine | `abf.planbab.f2`, `R22.planist` | referenziert nur Skills |

Spielmechanik und Routinen kennen nur Skills. Kommen die Skripte, wird nur die Tabelle Lernziel → Skriptkapitel befüllt. Lernziele, die das Skript neu bringt, landen als Lücke im Abdeckungsbericht. Ein CI-Schritt prüft je Lernziel: ≥ 1 Theoriekarte, ≥ 3 Vorlagen, ≥ 1 Routine- oder Fallkontext, ≥ 1 Prüfungsformat-Item. Fehlt etwas, entsteht Content-Arbeit, keine Designänderung.

---

## 7. Inhaltsabdeckung

| HB / LZ | Bereich | Module | Konkrete Übung (Gruppenzahlen) | Aufgabentyp |
|---|---|---|---|---|
| HB1.LZ01 | Pilotmarkt | M02, M07 | Pils L01: Rechnungs-EK 12,40 € → Gruppen-Einstand 11,66 € → VP an Markt 12,01 €; VK 17,49 € brutto = 14,70 € netto; Markt-RE 2,69 € (18,3 %), Konzern-RE 3,04 € | Rechenkette mit Folgefehlern |
| HB1.LZ02 | Pilotmarkt | M08 | Markt 1 Januar: Umsatz 139,8, RE I 40,7 (29,1 %), EBIT −8,3 T€; das ist ein Saisoneffekt, kein Schließungsgrund | KER-Lückentabelle + „Erklär’s der GF“ |
| HB1.LZ03 | Pilotmarkt/Großhandel | M44, M38 | Leergut Markt → KG: 612 statt 640 Bierkästen; 28 × 2,61 € = 73,08 € | Abstimmung in Stück, Stempel |
| HB1.LZ05 | Großhandel | M06, M12 | Leergut-Kostenstelle 455,1 T€ ÷ 1.012.500 gewichtete Kästen = 0,45 €/Kasten (netto 0,35 €); Gastro-Stopp 34,16 €; Mindestbestellwert 125 € | BAB-Lückentabelle, Satzbildung |
| HB1.LZ06 | Großhandel | M09, M33, M14 | Kunden-DB III: Brauhaus +4.252 €, Eckkneipe −498 €, 14-tägig +390 €; AfA Leihinventar 1.500 € ist versunken | Mehrstufen-DB, Fehlersuche in Aydıns Rechnung |
| HB1.LZ07 | Abfüllung | M06, M07 | Plan-BAB: MSS 249,4 €/MH; Äquivalenzziffern 0,667/0,8/1,0; HK 0,161/0,193/0,249 €/Fl | BAB, Äquivalenzziffernkalkulation |
| HB1.LZ08 | Abfüllung | M07, M15, M31 | Lohnabfüller fordert +12,0 % (1,0 l: 0,251 €), berechtigt +5,2 % (0,236 €) | Fehlersuche Zuschlagskalkulation |
| HB1.LZ09 | Abfüllung (bei Kauf) | M11 | 400 statt 587 MH → Beschäftigungsabweichung 83,2 × (1 − 400/587) = 26,5 T€; Konzentrat 0,097 statt 0,092 kg/l → Verbrauchsabweichung 2,5 T€ | Abweichungsfall (Fallakte) |
| HB1.LZ10 | Gruppe | M41 | VP Märkte: Startregel 4,1 / −169,9; Marktpreis −447,9 / +282,1 T€; Summe immer −165,8 T€ | 4-Varianten-Tabelle mit Invarianzprobe |
| HB1.LZ11 | Gruppe | M14 | Markt 3 schließen: −17,9 T€ bei 50 % abbaubarer Logistik, +9,7 T€ bei 100 % | Entscheidungsvorlage |
| HB2.LZ02 | Großhandel | M48, M08 | Bonusstaffel Brauerei Nord: 99,2 % → 1 % = 23.610 €; Vorkauf 1.600 Kästen → 2 % = 47.600 €; Klausel „Bezugsbasis Abverkauf“ | Hochrechnung + Klauselprüfung |
| HB2.LZ04 | Großhandel | M23, M49 | 13-Wochen-Plan Dez/Jan mit Steuerterminen; Kontokorrent Plan 472,1, Ist 588,8 T€ | Tabelle, Überleitung |
| HB2.LZ05 | Gruppe | M18, M51 | Budget Fuhrpark 747,2 T€: Brinkmann plant +9 %, die Treiber ergeben +4 % → Slack ≈ 37 T€ **[Vermutung]** | Gegenstrom-Dialog + Treiberrechnung |
| HB2.LZ06 | Großhandel | M25, M54 | E-Sattelzug: −19,5 Energie, −20,7 Maut, +30,0 Mehrleasing → +10,2 T€ pro Jahr (07) | Kapitalwert + Sensitivität |
| HB2.LZ07 | Abfüllung | M25, M37 | Linie: KW +46,5 T€ mit Fremdauftrag, −623,5 T€ ohne; Erwartungswert −221,5 T€; kritische Fremdmenge 1,12 Mio. Fl | Szenario-Tabelle, Vorlage |
| HB2.LZ08 | Gruppe | M19 | Gastro-Stopps −4 % (Gedat 95,7), Diesel ±30 ct = ±33,4 T€ | Forecast-Tabelle |
| HB3.LZ01 | Gruppe | M22, M50 | EK-Quote 28,6 % / 30,9 %; NV/EBITDA 2,85; KDF = (JÜ + AfA + Zins) ÷ (Zins + Tilgung) | Kennzahlenkette, Bankgespräch |
| HB3.LZ03 | Großhandel | M22, M44 | Silvester-Überhang 79,0 T€ als Stichtagseffekt; Pfand-Float 341,7 T€ (≈ 27,3 T€ Zins bei 8 %) | Fehlersuche „Trend oder Stichtag?“ |
| HB3.LZ05 | Gruppe | M40, M49 | Schuldenkonsolidierung 145,1 + 150,0 + 66,0 + 4,1 T€; Zwischengewinn 263,0 × 3/103 = 7,7 T€; GewSt auf die Sondervergütung der GF: +19,6 T€ | Buchungssatz-Prüfer |
| HB4.LZ01–03 | alle | M26, M27, M29 | Monats- und Spartenbericht, EBIT-Wasserfall; Stammdatenfehler „Flasche statt Kasten“ | Satzbaustein-Builder, Datenraum-Fall |
| HB4.LZ04 | Gruppe | M28 | VP-Modell in Excel mit Prüfsumme −165,8 | xlsx-Abgabe |
| HB5 | Gruppe | M42, M36 | Projekte: Markt 3, Lieferrhythmus C-Kunden, Make-or-Buy | Projektwerkstatt |
| HB6 | Gruppe | M43, M55 | Budgetrunde moderieren; Inventur mit 3 Zählteams; Delegation an Lena | Dialog, Planungsaufgabe, Feedback-Bausteine |

**Auch die Gruppe deckt nur schwach ab:** wertorientierte Steuerung (M21, kein Kapitalmarkt); IFRS, Minderheiten, Equity-Methode, Währung (M40); CSRD-Pflicht (M39, nur VSME-Anfragen); echte Teamführung (M55); Industrie-KLR jenseits einer einstufigen Linie (mehrstufige Fertigung, Kuppelprodukt, Bestandsveränderungen ohne Kauf); Aktion, Warenkorb und Endkunden-Wetter nur in den Märkten (M45, M53, M46). Diese Themen laufen als **Transfer-Akten** (Fälle aus fremden Branchen) in der Frühschicht, ausdrücklich als Ausblick.

---

## 8. Branchenspezifische Mechaniken

**8.1 Übersicht**

| Mechanik | Im Spiel | Trainiert |
|---|---|---|
| Vollgut-/Leergutkonten und Pfand | Saldenbestätigung je Lieferant in Stück; Fahrer- gegen Lagerzählung; Rügefristen; Kundenkonten Gastro; Fasspfand 30 € brutto (25,21 € netto); Bruttomodell in der Bilanz | Abstimmung, IKS, Bilanzausweis, Working Capital (M02, M22, M38, M44) |
| Wetter-Forecast | 7-Tage-Vorschau mit Fehlerband für Märkte und Feste; Ist kommt später; Hitzewelle ≈ 1 × pro Saison | Newsvendor, Prognosegüte (MAPE, Bias), Disposition (M19, M46) |
| Aktionen (Märkte) | Aktions-EK nur gegen Abverkaufsnachweis, Restmengen werden nachbelastet; L01 mit db 0,91 € im Markt, 1,15 € im Konzern | inkrementeller Aktionserfolg, Abgrenzung (M15, M45) |
| Konditionen, Boni, Vorkauf | 417,4 T€ Nachvergütungen pro Jahr, 290 T€ aus 2026 noch offen; Staffeln; Preisrunde mit Vorkaufsoption | Hochrechnung, Abgrenzung, Klausellesen, Bilanzpolitik (M08, M31, M48) |
| Gastro-Darlehen | 1.200 T€ bei ≈ 80 Wirten, 3 % Zins; Leihinventar 900 T€; Insolvenzkaskade (p ≈ 60 % für ≥ 1 Fall pro Jahr, 07); Bezugsbindung 10 J. (BGH) gegen 5 J. Gruppenfreistellung | Kunden-DB III, Kreditrisiko, Investitionssicht (M24, M33, M37) |
| Touren und Fuhrpark | 15 Fahrzeuge, 747,2 T€; Tourtag 454,30 €; Auslastung 94,8 %, Leerkosten 29,3 T€; Diesel 111.260 l | Prozesskosten, sprungfixe Kosten, Make-or-Buy Abholung (M05, M12, M14, M25) |
| Lager | Stellplätze als Engpass im Silvester-Peak; Prozesskostensätze je Kolli und Kasten | Engpass, Opportunitätskosten (M06, M32) |
| Saison | Märkte Jan–Apr negativ, Feste Mai–Sep, Dezember-Spitze | Saisonindex, Liquidität (M03, M23) |
| Ereignisse | Mindestlohn, Zuckersteuer, Brauerei-Insolvenz (Individualgebinde wertlos), Fahrermangel, Großkundenverlust, Kistenknappheit | Risiko, Forecast-Update, Szenarien (M37, M19) |
| Hausmarke | eigener Kastenpool, Konzentrat-Beistellung, Lohnabfüller; ab Jahr 2 Make-or-Buy | Industrie-KLR, Zuschlagskalkulation, Entscheidungsrechnung (M06, M07, M11, M14, M25) |

**8.2 Hausmarken-Datenblatt (Plan 2027, Lohnabfüllung) [Vermutung, nachgerechnet]**

Parameter:
- Apfelschorle, 55 % Saft aus Konzentrat (70 °Brix): 0,092 kg/l × 2,00 €/kg = 0,184 €/l. Das Konzentrat beschafft die Gruppe selbst und stellt es dem Lohnabfüller bei.
- Abfülllohn je Flasche (inkl. Wasser, CO₂, Verschluss, Etikett, Poolflasche, Reinigung): 0,150 € (0,33 l) / 0,175 € (0,5 l) / 0,225 € (1,0 l).
- Eigener Kastenpool: 5.000 Kästen × 4,00 € = 20 T€ Anlagevermögen; AfA 8 J. plus 3 % Schwund ergeben 0,14 € je Füllung.
- Pfand: 0,15 € je Flasche + 1,50 € je Kasten = 5,10 / 4,50 / 3,30 € je Kasten.
- Bilanziell ist die Gruppe Eigentümerin der Kästen. Die Behandlung nach BFH I R 33/11 muss vor der Content-Freigabe mit einer WP geprüft werden **[wahrscheinlich]**.
- Die Werte sind eine Aufgliederung innerhalb der Segmentwerte aus 08; die geprüften Summen bleiben unverändert.

| Gebinde | Kästen | Flaschen | Einstand €/Kasten (Konzentrat + Lohn + Kasten) | Ø Preis netto €/Kasten | Umsatz T€ | RE I T€ |
|---|---|---|---|---|---|---|
| 24 × 0,33 Glas (Gastro) | 6.500 | 156.000 | 1,46 + 3,60 + 0,14 = 5,20 | 11,76 | 76,4 | 42,7 (55,8 %) |
| 20 × 0,5 Glas (Objekt, Feste) | 4.000 | 80.000 | 1,84 + 3,50 + 0,14 = 5,48 | 10,40 | 41,6 | 19,7 (47,3 %) |
| 12 × 1,0 Glas (Märkte, Wiederverkäufer, Heimdienst) | 12.000 | 144.000 | 2,21 + 2,70 + 0,14 = 5,05 | 6,88 | 82,5 | 22,0 (26,6 %) |
| **Summe** | 22.500 | 380.000 (235.480 l) | | | **200,6** | **84,3 (42,0 %)** |

Vom RE I zum DB III vor Touren:
- RE I 84,3 T€
- − Prozesskosten der KG je Kasten (Lager 0,30 + Kommissionierung 0,32 + Leergut 0,45 brutto + Beschaffung 0,09 = 1,16 €/Kasten): 26,1 T€. Für eigene Kästen zahlt keine Brauerei Sortiervergütung, deshalb gilt der Bruttosatz.
- = DB II 58,2 T€
- − Hausmarken-Fixkosten (Marketing 18, QS/Labor 5, Konzentratlager 2): 25,0 T€
- = **DB III 33,2 T€ (16,6 %)**

**Lernpunkte:**
- Die 1,0-l-Flasche erzielt im Konzern 26,6 % RE, die Marke L14 (PET) 36,0 % nach Nachvergütungen. Im Markt liegt sie bei 27,1 % gegen 32,1 % für die Marke; deshalb will Sabine die Marke behalten. Die Hausmarke verdient in der Gastro, nicht im Markt.
- Fällt die Schorle unter die Zuckersteuer (26 ct/l), kostet das 61,2 T€ und frisst den DB III mehr als auf.

**8.3 Make-or-Buy „eigene Linie“ (Plan 2029, Bogen ab Spieljahr 2) [Vermutung, nachgerechnet]**

Ausgangslage:
- Gebrauchte Glas-Mehrweg-Linie aus der Insolvenzmasse der Privatbrauerei Wiesental: Kaufpreis 190 + Montage/Umbau 70 = AHK 260 T€; Wiederbeschaffungswert 300 T€; Nutzungsdauer 10 Jahre.
- Effektive Leistung 3.000 / 2.500 / 2.000 Fl/h. Daraus folgen Äquivalenzziffern nach Maschinenzeit 0,667 / 0,8 / 1,0, nicht nach Füllvolumen.
- Kapazität 1.500 h im Einschichtbetrieb.
- Plan: Hausmarke 408.000 Fl (167 MH) plus ein Fremdauftrag über 1,2 Mio. Fl Limonaden (0,33/0,5 l, 420 MH) zum Lohn von 0,12/0,14 €/Fl. Den Fremdauftrag vergibt der Investor, der die Limonadenmarke der Insolvenzbrauerei übernommen hat.
- 58 Chargen à 2,5 h; Belegung 732 h (48,8 %).

| Plan-BAB 2029 | Bezugsgröße | T€ | Satz |
|---|---|---|---|
| H1 Technik/Instandhaltung (→ F1 10 %, F2 90 %) | – | 18,4 | – |
| F1 Ausmischung & Labor | 697.440 l | 37,3 | 0,0535 €/l |
| F2 Abfülllinie (kalk. AfA 30,0 statt bilanziell 26,0; kalk. Zins 7,8; Ersatzfläche 11,2; Energie/Lauge 31,7; Linienhelfer 31,6; Abfüllmeister 15,6; Versicherung 2,0; Umlage H1 16,6) | 587 MH | 146,4 | **249,4 €/MH** |
| F3 Rüsten/CIP | 58 Chargen | 23,1 | 398 €/Charge |
| Material Hausmarke (Einzelkosten) | 408.000 Fl | 18,0 | 0,044 €/Fl |
| **Summe** | | **224,7** | |

| €/Flasche | 0,33 l | 0,5 l | 1,0 l |
|---|---|---|---|
| Make (Vollkosten HK) | 0,161 | 0,193 | 0,249 |
| Buy, verhandelt (+5,2 %) | 0,158 | 0,184 | 0,237 |
| Buy, Forderung (+12 %) | 0,168 | 0,196 | 0,252 |

| Vergleich (gegen Buy +5,2 %) | mit Fremdauftrag | ohne |
|---|---|---|
| Vollkostenvorteil Make pro Jahr | +3,9 T€ (Hausmarke allein −3,2, Überdeckung Fremdauftrag +7,0) | −87,2 T€ |
| Cash-Ersparnis pro Jahr | +41,7 T€ | −49,4 T€ |
| Kapitalwert (6 %, 10 J., ohne Restwert) | **+46,5 T€** | **−623,5 T€** |
| NV/EBITDA bei Kreditfinanzierung (Basis Plan 31.12.2027) | 2,83 | 3,19 |

Bei p = 0,6 für den Fremdauftrag liegt der Erwartungswert bei **−221,5 T€**. Die kritische Fremdmenge beträgt **1,12 Mio. Fl**; der Sicherheitsabstand zur Planmenge ist nur 6,9 %. Die EK-Quote fällt mit Kredit auf 29,4 %. Der Fall ist ehrlich offen: Make lohnt nur mit einer Take-or-pay-Zusage über die kritische Menge. Ob die Gruppe kauft, entscheidet die GF im Spiel (Szene C).

---

## 9. Aufgabentypen und automatische Bewertung

**Typen:** Stempel-Vorgang (Aktion + Betrag + Begründung), Abstimmung in Stück je Gebindeart, Rechenkette, Lückentabelle (BAB, KER, DB-Stufen, Liquidität), Buchungssatz, Fallakte im Deduktionsstil (Ursache – Betrag – echt/Messfehler – Maßnahme; Bestätigung erst ab zwei korrekten Slots), Satzbaustein-Builder für Vorlage und Kommentar, Dialogbaum, xlsx-Abgabe, Prüfungsformat.

**IHK-Format:** Probeklausuren bestehen aus einer Situationsbeschreibung der Gruppe, Anlagen (Auszüge, BAB, Verträge) und Teilaufgaben mit Punkten, unter Zeitlimit (HB1/HB2 180, HB3 90 min). Es sind eigene, parametrisierte Aufgaben; Original-IHK-Aufgaben sind urheberrechtlich geschützt **[sicher, 05]**.

**Bewertung:**
- **Toleranzen:** Geld ±1 € bzw. ±0,5 % relativ, Quoten ±0,1 Prozentpunkte.
- **Folgefehler:** Jede Zelle wird gegen das eigene Vorergebnis geprüft und bekommt Teilpunkte; die Diagnose meldet z. B. „Fehler nur in Schritt 2“. Äquivalente Lösungswege werden akzeptiert.
- **Ratedetektion:** Antworten unter 3 s und Hint-Spam zählen nicht für Mastery.
- **Kalibrierungsscore:** aus dem Sicherheitsregler.

**Fehlerdiagnose:** Der Misconception-Katalog aus 03 (M1–M12) wird um GFGH-Fehler ergänzt. Jede Regel prüft die Antwort gegen eine Fehlerfunktion:

| ID | Fehler | Erkennung |
|---|---|---|
| G-M13 | Leergut in € statt Stück abgestimmt | Euro-Eintrag ohne Mengenzeile, Ursachen fehlen |
| G-M14 | VP verändert das Gesamtergebnis | Summe der Varianten ≠ −165,8 |
| G-M15 | versunkene AfA als entscheidungsrelevant | DB enthält 1.500 € AfA bei Kündigungsfrage |
| G-M16 | DPO brutto gegen netto (06 E5/G14) | Ergebnis entspricht der Brutto/Netto-Mischung |
| G-M17 | KDF-Formel gemischt (G15) | Entnahmen statt Zinsaufwand im Zähler |
| G-M18 | Äquivalenzziffer nach Liter statt Maschinenzeit | HK 1,0 l zu hoch, 0,33 l zu niedrig |
| G-M19 | Zuschlag auf erhöhte Lohnbasis akzeptiert | Forderung +12 % ungeprüft übernommen |
| G-M20 | Stichtagseffekt als Trend gedeutet | Silvester-Überhang hochgerechnet |
| G-M21 | Logistikkosten bei Schließung voll abbaubar | 100 % ohne Rückfrage beim Logistikleiter |

---

## 10. Training für HB4, HB5 und HB6

**HB4: Excel-Werkstatt.**
- Die Engine erzeugt ein Datenpaket als xlsx/CSV, z. B. Tourtage, Kundenklassen, Leergutbewegungen, VP-Varianten.
- Dazu kommt ein Auftrag, etwa: „Segmentbericht DB I–III mit Planabweichung, Wasserfall, Kommentar“.
- Gebaut wird in Excel oder LibreOffice Calc; abgegeben wird eine xlsx-Datei mit **benannten Abgabezellen**.
- Das Spiel liest sie mit exceljs ein und vergleicht die Werte mit der Engine-Lösung. Formelzellen werden auf hartkodierte Zahlen geprüft, Prüfsummen müssen aufgehen.
- Diagramme und Layout sind nicht automatisch prüfbar **[wahrscheinlich: exceljs liest Werte und Formeln, keine Diagramme]**; dafür gibt es eine Selbstcheck-Rubrik.
- Stufen: Übungsaufträge (30–60 min) in Kapitel 2/3, im Prüfungsjahr zwei 240-min-Proben.

**HB5: Projektwerkstatt.**
- Ablauf im 30-Kalendertage-Modus: Der Spieler wählt aus zwei Themenvorschlägen (wie in der IHK-Praxis, 01). Meilensteine an Tag 1/7/14/21/28/30 mit 20–40 min Arbeit je Termin.
- Gliederung: Management Summary, Auftrag, Ist-Analyse mit Gruppendaten, ≥ 2 quantifizierte Alternativen, Bewertung (Rechnung und Nutzwertanalyse), Empfehlung, Umsetzung, Risiken.
- Bewertung: Zahlen prüft die Engine, Struktur und Argumentation eine 8-Kriterien-Rubrik (Selbst- und Peer-Bewertung). Ab 1.1 optional LLM-Feedback, nie als Gate.
- Export als Dokument für den Dozenten; ein Transferbogen überträgt die Gliederung aufs eigene Unternehmen. Die echte Projektarbeit verlangt Praxisbezug im eigenen Umfeld **[wahrscheinlich, 08]**.

**HB6: Präsentation und Fachgespräch.**
- **Präsentation:** Folienbaukasten nach dem Pyramidenprinzip mit IBCS-Presets, 15 min, Zeitanzeige.
- **Fachgespräch-Simulation:** Ein Prüfer-Dialog zieht Fragen aus dem eigenen Projekt und aus HB1–HB5 („Warum Maschinenstundensatz statt Lohnzuschlag?“). Geantwortet wird durch Auswahl und Ordnen von Argumenten und kurze Rechnungen im Zeitfenster.
- **Selbstaufnahme** per Browser-Mikrofon (nur lokal) mit Checkliste.
- **Moderation, Konflikt, Führung:** Budgetrunde mit drei Kostenstellenleitern nach Moderationszyklus; Konfliktgespräch mit Brinkmann (Glasl-Stufen); Inventur mit 3 Zählteams; Delegation an Lena mit Stichprobe und Feedback nach Situation–Verhalten–Wirkung.
- **Grenze:** Ein Dialogbaum trainiert Erkennen, nicht Können (06 #5). Echtes Üben braucht einen Peer-Modus (Rollenkarten zum Ausdrucken) oder Lehrgangssitzungen.

---

## 11. Drei Beispielszenen

### Szene A: „Erster Abschluss im Pilotmarkt“ (Februar 2027, AT1–AT3 Januar, ≈ 25 min)

Module M02, M07, M08, M44; HB1/HB3.

1. **Briefing:** Jana: „Fang in Markt 1 an. Sabine braucht den Januar bis zum 5.“ Das Regelbuch hat 3 Regeln: Menge, Preis, Pfand netto.
2. **Vorgang 1 (Worked Example, Brand): Leergut-Rückgabe Markt → KG vom 21.01.**
   - Der Fahrer-Lieferschein nennt 612 Bierkästen und 388 Wasserkästen, das Markt-Nebenbuch 640 und 388.
   - Neue Regel R1: „Erst in Stück je Gebindeart abstimmen, dann bewerten.“
   - Bewertung: 28 × 2,61 € (3,10 € ÷ 1,19) = **73,08 €**.
   - Das Automatenprotokoll im Datenraum zeigt 28 Kästen „fremd/unbekannt“. Das KG-Lager hat sie aussortiert.
   - Stempel „Rückfrage KG-Lager“. Selbsterklärungsfrage: „Warum ist das kein Umsatzverlust?“ Antwort: Pfand ist ein Erstattungsanspruch, kein Erlös.
3. **Vorgang 2 (Fading 2):** Sabine: „Otte will Pils für 10,99 €. Was bleibt uns?“
   - Aktions-EK 8,60 € × 0,94 = 8,08 €; VP +3 % = **8,33 €**.
   - VK 10,99 € brutto = 9,24 € netto → **db 0,91 €/Kasten (9,8 %)**. Ohne Aktions-EK: −2,77 €.
   - Distraktoren: 2,66 € (Brutto-VK minus VP → „Die USt gehört dem Finanzamt“); 0,64 € (Aktions-EK der Brauerei 8,60 € direkt → „Markt 1 kauft bei der KG zum VP: Einstand 94 % plus 3 %“).
   - Warum-Frage zur Konzernsicht: Die KG verdient 0,24 € VP-Aufschlag mit, der Konzern-db liegt bei 1,15 €. Das ist der Teaser für Kapitel 3.
4. **Vorgang 3 (KER, Fading 3):**
   - Bestand AB 125,0 T€, Zugänge zum VP 102,1 T€, EB 128,0 T€ **[Annahme]** → Wareneinsatz 99,1 T€.
   - Umsatz 139,8 T€ (Saisonanteil 6,5 %) → RE I 40,7 T€ (**29,1 %**).
   - Abzüge: Inventurdifferenz −0,7, Personal −24,3, Sachkosten −20,2, Umlage −2,1, AfA −1,7 → EBIT **−8,3 T€**.
   - Diagnose: 41,1 % ist der Aufschlag statt der Spanne (M1), 24,8 % eine vorzeichenfalsche Bestandsveränderung (M4).
5. **E-Mail der GF:** „−8,3 T€. Müssen wir über Markt 1 reden?“
   - Satzbaustein-Antwort: Saisonmuster Jan–Apr, Jahresplan +15,9 T€, Prüfmarke im März. Das bringt Vertrauen +.
   - Die Option „Schließung prüfen“ kostet Vertrauen; Brand erklärt den Fehler im Debrief.
6. **Freischaltung und Planung:**
   - Nach der dritten korrekten Leergut-Abstimmung an ≥ 2 Tagen ist die **Mengenlupe** frei: Auszüge zeigen Stückspalten je Gebindeart.
   - Frühschicht morgen: „Pfand netto/brutto“. In 3 Tagen kommt „Aktions-db mit VP“ als Fehlersuche in Lenas Rechnung.
   - Lehrsatz: „Leergut erst in Stück, dann in Euro.“

### Szene B: „Drei Salden und eine E-Mail“ (Januar 2028, AT2–AT5, ≈ 30 min)

Module M44, M48, M08, M23, M22, M55; HB1–HB3/HB6.

1. **Frühschicht** mit 7 Items, darunter mit Flugrost „rückwirkende Staffel gegen Grenzstaffel“.
2. **AT2: Saldenbestätigung Brauerei Nord, Bierkästen.**
   - Auszug 62.480 Stück, eigenes Konto 61.200; die Differenz von **1.280** ist zu klären.
   - Datenraum, Ursache (a): 880 Kästen am 30.12. zurückgegeben, bei der Brauerei erst am 04.01. gebucht. Das ist eine Umgliederung „Gutschrift offen“ (2.296,80 €) ohne Wertkorrektur.
   - Ursache (b): 300 Fremdkästen der Brauerei Süd zurückgewiesen. Sie werden aufs Süd-Konto umgebucht (783,00 €).
   - Ursache (c): Zähldifferenz bei der Rücknahme (Lieferschein 1.360, Brauerei 1.260). Regel: Rüge binnen 5 Werktagen.
   - Verzögerte Konsequenz: Hat der Spieler im Dezember das Rücknahmeprotokoll gerügt, kommt eine Gutschrift. Sonst fallen **261,00 €** Aufwand an, und die Prüferin vermerkt eine Citation.
3. **AT3: Bonusabgrenzung (Folge einer Dezember-Karte).**
   - Staffel 1 % ab 95 %, 2 % ab 100 %, 2,5 % ab 105 % auf 200.000 Kästen Vorjahr, Ø-EK 11,90 €. Ist 198.400 (99,2 %).
   - Der Spieler hatte im Dezember 1.600 Kästen Vorkauf empfohlen: 2 % = 47.600 € statt 1 % = 23.610 € (+23.990 €).
   - Vertrag § 4: Bezugsbasis ist der Abverkauf laut hl-Meldung. Der Vorkauf zählt nicht, die Abgrenzung beträgt **23.610 €**.
   - Restnutzen: Preisrunde +0,60 € → 960 € gespart. Dagegen stehen 23,2 T€ Kapitalbindung (≈ 214 € Zins) und 40 Paletten im Silvester-Peak.
   - Kontrafaktum im Debrief: Mit „Prüfauftrag: Vertrag lesen“ hätte die Empfehlung nur auf die Preisrunde gezielt.
4. **AT4/AT5: E-Mail der GF:** „Kontokorrent 588,8 T€, Plan 472,1. Problem?“
   - Überleitung: Leergut-Überhang 42.000 statt 30.000 Kästen (Abholung wegen Fahrermangel ausgefallen) 12.000 × 2,63 € = **+31,6**; Vorkauf **+23,2**; DSO Gastro 27 statt 25 Tage: 9.500 × 1,19 × 2/365 = **+61,9**. Summe +116,7 T€ ✓.
   - Zwei Stichtagseffekte kehren sich im Februar um, einer ist strukturell. Maßnahme: Mahnlauf und Lastschriftpflicht für C-Kunden.
   - Covenant-Tacho: EK-Quote 29,9 % (Plan 30,4 %), NV/EBITDA 2,79, also unkritisch. Antwort nach dem Muster „Botschaft zuerst, drei Treiber, eine Maßnahme“.
5. **Delegation:** Lena hat die 40 Wiederverkäufer-Leergutkonten abgestimmt. Die Stichprobe (5 Konten) findet einen Fehler: Paletten als Warenumschließung statt eigene Leistung mit 19 % (F14). Der Spieler gibt Feedback nach Situation–Verhalten–Wirkung; Lenas Fehlerquote sinkt mit guter Rückmeldung.
6. **Debrief:** Treiberbaum Kontokorrent, Kalibrierung. Lehrsatz: „Erst Bezugsbasis lesen, dann Staffel rechnen.“

### Szene C: „Die Linie aus der Insolvenzmasse“ (Sep/Okt 2028, 3 Sessions à 25 min)

Module M06, M07, M11, M14, M15, M25, M37, M42, M43, M50; HB1/HB2/HB5/HB6.

1. **Posteingang: Lohnabfüller Hellwig fordert +12 % für 2029** (1,0 l: 0,225 → 0,251 €).
   - Kalkulationsblatt 2027 je Flasche: Material 0,044, Wasser/CO₂ 0,015, Fertigungslohn 0,040, FGK 175 % auf Lohn 0,070, Energiezuschlag 0,018, Verwaltung/Gewinn 20 %.
   - Forderung: Material +3 %, Wasser/CO₂ +10 %, Lohn +6 %, FGK-Satz 195 % „wegen Energie“, Energiezuschlag +25 %.
   - Fehlersuche: (i) Die FGK (AfA, Raum) steigen über den Zuschlag mit dem Tariflohn mit (+0,005 €). (ii) Energie wird doppelt erhöht, über die Satzanhebung (+0,010 €) und den Zuschlag.
   - Berechtigt sind **0,236 € (+5,2 %)**. Gegenangebot: Preisgleitklausel mit indexierten Anteilen für Lohn, Energie und Material, FGK fix, dazu eine Open-Book-Option.
2. **Neue Lage:** Der Insolvenzverwalter bietet die Glaslinie für 190 T€ an. Ein Investor sucht einen Abfüller für 1,2 Mio. Fl. Jana: „Prüfen Sie, ob wir selbst abfüllen.“
3. **Projektauftrag (HB5-Format)** mit Ziel, Kriterien und Termin (Budgetrunde 15.10.).
   - Projektteam: Brinkmann (450 m² Leergut-Puffer, Ersatzfläche 14 T€), Lager (2 Helfer je Belegungsstunde), QS, Einkauf Konzentrat.
   - Der Spieler verteilt Aufgaben und Fristen (Teamführung).
4. **Plan-BAB (Fading 2):**
   - H1 (18,4 T€) wird 10/90 umgelegt. Sätze: F1 0,0535 €/l, **F2 249,4 €/MH**, F3 398 €/Charge.
   - Distraktor 229,3 €/MH (bilanzielle AfA, kein kalkulatorischer Zins) → „Anderskosten und Zusatzkosten fehlen“.
5. **Äquivalenzziffern:**
   - Nach Maschinenzeit 0,667 / 0,8 / 1,0 ergeben sich HK 0,161 / 0,193 / 0,249 €/Fl.
   - Kontrastpaar Liter-Äquivalenzziffern 0,33 / 0,5 / 1,0: Damit würde die 1,0-l-Flasche zu teuer und die 0,33-l-Flasche zu billig gerechnet (G-M18). Weil die 1,0-l-Flasche 60 % der Hausmarken-Liter stellt, verzerrt das jede Sortimentsentscheidung.
6. **Vergleich (Tabelle aus 8.3):**
   - Mit Fremdauftrag: Kapitalwert +46,5 T€. Ohne: −623,5 T€. Erwartungswert −221,5 T€.
   - Kritische Menge 1,12 Mio. Fl. Covenants mit Kredit: EK-Quote 29,4 %, NV/EBITDA 2,83 bzw. 3,19.
   - Qualitativ: Haftung als Inverkehrbringer; ohne eigene Quelle nur Trink- oder Tafelwasser statt Mineralwasser **[wahrscheinlich]**; Flächenkonflikt im Silvester-Peak.
7. **Vorlage und Präsentation vor Jana und Karl:**
   - Empfehlung: „Buy mit Preisgleitklausel (+5,2 %) und Open-Book. Make nur bei Take-or-pay ≥ 1,12 Mio. Fl über ≥ 7 Jahre.“
   - Karl wendet ein: „Mein Vater hat selbst abgefüllt.“ Es folgt ein Einwand-Dialog.
   - Die GF entscheidet mit Wahrscheinlichkeit aus Vertrauen und Vorlagenqualität.
8. **Zweige:**
   - **(a) Kauf:** Ab 2029 laufen die Routinen R21–R23 (monatlicher BAB, Plan-Ist, Bewertung der Bestände zu HK nach § 255 HGB). Im Mai erfüllt der Investor nur 70 % → Fall „400 statt 587 MH“ mit Beschäftigungsabweichung 26,5 T€ und Konzentrat-Verbrauchsabweichung 2,5 T€.
   - **(b) Kein Kauf:** Verhandlungs-Minispiel mit Hellwig; die BATNA ist die eigene Linie. Danach prüft der Spieler monatlich den Open-Book-Kostennachweis.
9. **Debrief:** Entscheidungsqualität ist vom Ergebnis zu trennen. Lehrsatz: „Fixkosten brauchen Menge, Menge braucht Vertrag.“

---

## 12. Technik und MVP-Schnitt

**Architektur (auf 04 aufbauend):**
- Angular-22-PWA, local-first (IndexedDB über Dexie).
- Frameworkfreie, deterministische TS-Engine `step(state, action)`, Integer-Cent, Hauptbuch mit Soll = Haben, Nebenbücher (Leergut je Partner in Stück).
- Inhalte als YAML/Markdown mit Zod-Validierung; ts-fsrs; ECharts mit IBCS-Presets; eigene Lückentabelle und Mini-Formelparser; exceljs für den HB4-Ex- und -Import.
- Hosting über Cloudflare Pages; kein LLM in 1.0.

**Zusätze für „Routine-first“:**
1. **Dokumentgenerator:** typisierte Dokumente (Beleg, Saldenbestätigung, Kontoauszug, E-Mail) mit seedbasierter Fehlerinjektion aus dem Katalog.
2. **Regelwerk als Daten** (Regel-ID, Kapitel, Prüffunktion, Skills) und **Tool-Registry** (Skill → Werkzeug).
3. **Posteingang-Scheduler** mit Lastdeckel 20–30 min.
4. **Common Random Numbers** für Replays; **Testorakel** aus dem 08-Skript (94 Prüfungen) und den neuen Skripten; **Abdeckungsbericht** je Lernziel im CI.

**Simulationstiefe:** Markt 1 als Tagesaggregate je Leitartikel und Warengruppe; Märkte 2/3 als Monatsaggregate. Die KG nach Kundenklassen (60/200/340) plus 12 benannte Kunden, mit Tourtagen statt Tourenplanung. Die Abfüllung als Monatsmodell.

**MVP-Schnitt „Schreibtisch-MVP“:** Zwei Spielmonate Markt 1 (Jan/Feb 2027) und ein Vorschau-Vorgang Großhandel (Saldenbestätigung). Die Daten kommen aus dem 08-Skript, eine Live-Engine gibt es noch nicht. Umfang: 5 Routinen, 8 Regeln, 3 Werkzeuge, ≈ 25 Skills, 15 Vorlagen, Frühschicht über 14 echte Tage, Debrief, Fallakte.

| Posten | PT |
|---|---|
| Setup (Repo, Angular 22, CI, PWA, Deploy) | 2–3 |
| Schreibtisch-UI (Posteingang, Dokumentansicht, Arbeitsblatt, Stempel, Regelbuch, Datenraum light) | 8–11 |
| Aufgaben-Framework (Instanziierung, Prüfer numeric/table/choice, Folgefehler, Distraktoren) | 4–6 |
| Dokumentgenerator aus Skriptdaten mit Fehlerinjektion | 3–4 |
| ts-fsrs, Frühschicht-Algorithmus, Dexie, Export | 3–4 |
| „Wissen ist Sicht“ (3 Werkzeuge, Beschlagen) | 2–3 |
| Inhalte (Theoriekarten, Vorlagen, Fälle, fachliche Prüfung) | 6–9 |
| Playtest mit 5 Personen über 14 Tage, Fixes | 3–4 |
| **Summe** | **31–44 PT** (mit KI-Unterstützung ≈ 25–35 PT) |

**Was der MVP beweisen muss:** ≥ 4 von 5 Testpersonen spielen an ≥ 8 von 14 Tagen, die Frühschicht dauert im Median ≤ 6 min, die Fehlerquote je Skill sinkt, der Re-Test nach 14 Tagen liegt bei ≥ 70 % korrekt, „würde weiterspielen“ bei ≥ 3,5 von 5.

**Danach:** Engine für Markt 1 und KG-Aggregat +40–60 PT. Version 1.0 der Gruppe: 160–280 (04) + 80–130 (08) + Abfüll-Bogen 20–35 + Werkstätten HB4/5/6 15–25 ≈ **275–470 PT**, im Hobbytempo von 1,5 PT pro Woche 3,5–6 Jahre **[Vermutung]**. Deshalb kapitelweise veröffentlichen.

---

## 13. Risiken und Gegenmaßnahmen

| Risiko | Gegenmaßnahme |
|---|---|
| Routine-Ermüdung | Jeder Monat bringt eine neue Regel, Störung oder Figurenkonflikt; Zeitdruck als Kür; Delegation des Beherrschten |
| Abbruch wegen Übezeit | Lastdeckel 30 %, Rückkehrmodus, Streak nur über erfolgreiche Wiederholung, Urlaubsschein 2 Tage pro Woche |
| Content-Volumen (Ein-Personen-Projekt) | Contentaufwand nach Kapitel 1 messen (06 Karte 87); KI-Entwurf plus Fachreview; kapitelweise veröffentlichen |
| Skripte passen nicht zu den Lernziel-IDs | n:m-Zuordnung, Abdeckungsbericht; neue Lernziele sind Content, kein Design |
| Industrie-KLR bleibt dünn | Pflicht-Bogen plus Open-Book-Zweig plus Transfer-Akten |
| Exploits (Hint-Spam, Raten) | Hints zählen nicht für Mastery, Ratedetektion, neue Zahlen bei jedem Versuch |
| Rechtsstand altert (Mindestlohn, Zuckersteuer, PPWR) | Rechtsstand 2027 einfrieren und versionieren (06 #15) |
| Alkohol als Kulisse | Sortimentsschalter; fiktive Marken (05) |

---

## 14. Offene Designentscheidungen

1. **Frühschicht: Wie verbindlich?** Pflicht vor dem Schreibtisch / Pflicht mit 1 Tag Gleitzeit / freiwillig. *Empfehlung: Pflicht mit 1 Tag Gleitzeit, max. 10 Items.*
2. **Was bewirkt Rost?** Werkzeug beschlägt / Arbeitsschritt gesperrt / nur Warnung. *Empfehlung: Werkzeug beschlägt (kein zweites Gate, 06 W11).*
3. **Mastery-Definition:** zweistufig / nur FSRS ≥ 21 Tage / nur 3 Lösungen über 2 Tage. *Empfehlung: zweistufig.*
4. **Umfang „alle Facetten“:** alle 56 Module Pflicht / IHK-Kern Pflicht, Rest Kür / Kapitel frei wählbar. *Empfehlung: Kern Pflicht (IHK hoch/mittel), Rest Kür; das Zeugnis nennt beides.*
5. **Wiederholungszählung:** ein Abruf je Skill und Tag / unbegrenzt. *Empfehlung: einer je Tag, Spielmonate unbegrenzt.*
6. **Belegarbeit und Delegation:** ≤ 20 % mit Delegation ab Kapitel 2 / Spieler macht alles / Buchhaltung macht alles. *Empfehlung: ≤ 20 % mit Delegation.*
7. **Wer entscheidet?** GF nach Empfehlung mit Wahrscheinlichkeit / Spieler / fest geskriptet. *Empfehlung: GF mit Wahrscheinlichkeit, Kernpfade mit beiden Ästen.*
8. **Ausgang Make-or-Buy:** frei mit beiden Ästen / immer Kauf / nie Kauf. *Empfehlung: frei; bei Nichtkauf Open-Book-Prüfung als Industrie-KLR-Routine.*
9. **Hausmarke:** Apfelschorle / Limonade / Mineralwasser. *Empfehlung: Apfelschorle (Begründung in 4).*
10. **HB4-Werkzeug:** eingebautes Blatt plus xlsx-Prüfung / nur Export / nur eingebaut. *Empfehlung: beides.*
11. **Bewertung HB5/HB6:** Rubrik mit Selbst-/Peer-Bewertung / plus LLM-Feedback / Dozentenexport. *Empfehlung: Rubrik + Export in 1.0, LLM ab 1.1.*
12. **Zeitdruck:** Kür nach Mastery / Pflicht im Prüfungsjahr / nie. *Empfehlung: Kür; Pflicht nur in Probeklausuren.*
13. **Lernziel-Schema:** jetzt vorläufig aus ContrPrV und 01/06 / auf die Skripte warten. *Empfehlung: jetzt vorläufig, beim Import ergänzen.*
14. **Erster Bauschritt:** Schreibtisch-MVP mit Skriptdaten (31–44 PT) / MVP mit Engine (60–85 PT) / Lernprototyp ohne Schreibtisch (20–25 PT). *Empfehlung: Schreibtisch-MVP, weil er die Kernthese „Routine + Frühschicht trägt“ am billigsten testet.*
15. **Kampagnenlänge:** 36 / 24 / 48 Spielmonate. *Empfehlung: 36 (drei Budgetzyklen, zwei Jahresabschlüsse mit Prüfung).*
