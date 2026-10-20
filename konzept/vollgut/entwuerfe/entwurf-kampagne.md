# Entwurf „Kampagne / Story-first“: Controller/in einer Getränkegruppe

Stand 19.10.2026. Sicherheitsstufen: **[sicher]** belegt (Quellen 01–08) · **[wahrscheinlich]** starke Ableitung · **[Vermutung]** Annahme oder Designvorschlag. Referenzbetrieb ist die „Getränkegruppe“ aus 08 **ohne Kelterei**. Neue Zahlen (Hausmarke, Abfüllanlage, Szenen) sind Annahmen, aber per Skript gerechnet (`(Rechenskripte des Entwurfs, nicht abgelegt)`: calc.py, mob2.py, hollmann.py, extra.py, bab.py). Alle Marken und Personen sind fiktiv.

---

## 1. Kurzfassung und Arbeitstitel

Der Spieler tritt am 4.1.2027 die Controller-Stelle einer Familien-Getränkegruppe an: Großhandel (GmbH & Co. KG, 17,5 Mio. € Außenumsatz) mit drei eigenen Abholmärkten (Märkte GmbH, 4,5 Mio. €). Die Kampagne läuft über drei Geschäftsjahre in vier Kapiteln: Pilotmarkt → Großhandel → Gruppe → Abfüllung der Hausmarke. Jedes Kapitel hat eine Leitfrage, die eine Figur stellt und die nur mit Controlling-Methoden beantwortbar ist. Der Spieler empfiehlt, die Geschäftsführung entscheidet; Folgen zeigen sich Monate später in Abschluss, Bankgespräch oder Prüfung. Wiederholung entsteht doppelt: Monatsabschluss, Forecast, Budget und Jahresabschluss kehren jedes Jahr unter neuen Bedingungen wieder, und ein Echtzeit-Scheduler (FSRS) erzwingt das Auffrischen einzelner Fertigkeiten. Alle Inhalte hängen an Lernziel-IDs je IHK-Handlungsbereich, sodass die Lehrgangsskripte später ohne Designänderung zugeordnet werden. Ehrlich gesagt: Das Spiel trainiert HB1–HB4 tief und HB5/HB6 nur als Methode, nicht als Prüfungsersatz.

**Arbeitstitel:** **„VOLLGUT – Drei Jahre Controlling in der Getränkegruppe“**. Alternative mit Wiederholungs-Metapher: „Leergut kommt zurück“. Vor Veröffentlichung im DPMA-Register prüfen **[sicher als Empfehlung aus 05]**.

---

## 2. Ehrliche Grenzen und wie das Konzept damit umgeht

| Grenze | Befund | Umgang im Konzept |
|---|---|---|
| **75 % der IHK-Note** | Projektarbeit 45 %, mündlich 30 %, schriftlich/praktisch (HB1–HB4) 25 % (§ 7 Abs. 4 ContrPrV) **[sicher]**. Ein Spiel kann weder die 30-Tage-Arbeit im eigenen Betrieb noch ein Fachgespräch bewerten. | HB5/HB6 als **Methodentraining** mit Vorlagen, Rubriken und Gesprächssimulation (Abschn. 10). Klar kommuniziert: kein Prüfungsersatz, Präsenz- oder Peer-Übung bleibt nötig. |
| **Pflicht-Wiederholung × alle Facetten** | ≈ 300 Skills × ≈ 7 Abrufe = ≈ 2.100 Abrufe, bei 8 pro Tag ≈ 260 Tage **[Vermutung, 06]**. | Zwei Stufen: „Kern“ (≈ 60 % der Lernziele, IHK-Relevanz hoch) ist Pflicht für Kapitel-Gates; „Ausblick“ ist optional **[Vermutung]**. Realistische Ansage: 6–9 Monate mit 5–10 min täglich plus ≈ 20 h Kampagne. |
| **HB4 am Tabellenkalkulationsprogramm** | 240 Min. Praxisprüfung **[sicher]**. Ein Browser-Rechenblatt ist kein Excel. | Eingebautes Arbeitsblatt für Routinen, dazu **HB4-Werkstatt** mit Datenexport und Aufgaben in echter Tabellenkalkulation (Abschn. 10). |
| **Industrie-KLR nur über Lohnabfüllung + Make-or-Buy** | Lohnabfüllung liefert keinen eigenen BAB mit Fertigungsstellen. Die IHK-Prüfung ist industriegeprägt **[wahrscheinlich, 06]**. | Plan-BAB, Maschinenstundensatz, Äquivalenzziffern und Plankosten werden für die Entscheidung *immer* gerechnet. Laufende Industrie-KLR gibt es nur bei Kauf; sonst Ersatz über Open-Book-Nachkalkulation mit dem Lohnabfüller. Bestandsbewertung in der Produktion und Kuppelprodukte bleiben dünn. |
| **Größere Simulation = mehr Bauaufwand** | GFGH + Märkte kostet +80–130 PT gegenüber dem Einzelmarkt **[Vermutung, 08]**. | Simulationstiefe begrenzen: Markt 1 auf Tagesebene, Märkte 2/3 als Monatsaggregate, Großhandel nach Kundenklassen plus 12 benannte Kunden, Abfüllung als Monats-Kostenmodell. Veröffentlichung kapitelweise. |
| **Abstrakter B2B-Einstieg** | Kein Kassentag, Leergutkonten und Gastroverträge sind Domänenwissen **[wahrscheinlich, 08]**. | Kapitel 1 spielt komplett im anschaulichen Markt 1. Der Großhandel kommt erst, wenn KLR-Grundlagen sitzen, und zwar über Personen (Wirt, Fahrer, Logistikleiter), nicht über Tabellen. |
| **Weitere** | Der Controller führt kaum ein Team (HB6). Zahlenwelt unbelegt. Rechtsstand ab 2028 unbekannt. Die Simulation kennt immer die „wahre Ursache“. | Teamführung über Inventur und Assistenz. Spannen statt Punktwerte, Annahme-Hinweise, Fachreview. Recht eingefroren auf Okt. 2026, ab 2028 als „Spielwelt-Fortschreibung“ markiert. Ab Kapitel 3 mehrdeutige Fälle mit mehreren vertretbaren Lösungen. |

---

## 3. Zielgruppen und Lernversprechen

**Primär:** Teilnehmende am Lehrgang „Geprüfte/r Controller/in (IHK)“ als Ergänzung zum Lehrgang. Das sind nur 80–115 Prüflinge pro Jahr **[wahrscheinlich, 05]**, deshalb **sekundär:** Junior-Controller und Quereinsteiger in Handel und Großhandel, Handelsfachwirt-Prüflinge, für Kapitel 1–2 auch Azubis Groß- und Außenhandel. Das Spiel richtet sich an Lernende mit externer Motivation (Prüfung, Job), nicht an Freizeitspieler **[Vermutung, 06]**.

**Messbare Lernversprechen** (Messung im Spiel, neue Parameter je Versuch):

| ID | Versprechen | Kriterium |
|---|---|---|
| LV1 | Monatsabschluss eines Abholmarkts (KER, Warengruppen-RE, Pfand- und Leergutabstimmung in Mengen) | unassistiert ≤ 30 min, ≤ 1 Fehler, an 3 Kalendertagen |
| LV2 | Kunden-DB I–III aus Prozesskostensätzen, relevante vs. versunkene Kosten | ≥ 80 % korrekt in gemischten Sets, Beträge ± 1 % |
| LV3 | Budget im Gegenstrom, 13-Wochen-Liquidität, Covenant-Headroom, Schulden- und Zwischengewinnkonsolidierung | jede Teilaufgabe 2× in Folge korrekt |
| LV4 | Plan-BAB (Stufenleiter), Maschinenstundensatz, Äquivalenzziffern, flexible Plankosten | ≤ 45 min, Ergebnisse ± 0,5 % |
| LV5 | Kern-Lernziele „beherrscht“ | ≥ 85 % mit FSRS-Stabilität ≥ 21 Tage plus 2 Spielanwendungen |
| LV6 | IHK-Format HB1–HB3 | ≥ 65/100 Punkte in 2 aufeinanderfolgenden Simulationen (Bestehensgrenze 50 Punkte **[wahrscheinlich]**) |
| LV7 | HB4-Werkstatt | ≥ 70 % Ergebnisgenauigkeit in 240 min, echte Tabellenkalkulation |

**Nicht versprochen:** Bestehen der Prüfung, Noten für Projektarbeit oder Fachgespräch.

---

## 4. Spielerrolle, Setting, Figuren

**Rolle:** Controller/in der Gruppe, Stabsstelle der Geschäftsführung, 75 T€ Personalkosten = **23,6 % des Konzern-EBIT** (318,4 T€ ohne Kelterei, 08) **[Rechnung]**. Die Stelle muss ihren Nutzen zeigen: Ein Zähler „Wertbeitrag Controlling“ summiert belegbare Effekte der Empfehlungen (vermiedene Verluste, Verhandlungserfolge). Der Spieler empfiehlt, die Figuren entscheiden (06 W9).

**Setting (08, ohne Kelterei):** Kreisstadt in NRW. KG mit Großhandel in fünf Segmenten (600 Gastro-, 150 Wiederverkäufer-, 25 Strecken-, 300 Objekt- und 900 Heimdienstkunden, Veranstaltungen), 5.000 m² Lager gemietet von der Besitzgesellschaft der Familie, 11 Lkw und 4 Transporter. Märkte GmbH mit EAV und Organschaft: Markt 1 (= korrigierter Referenzmarkt aus 02/06, nur Laden, 2.150 T€, EBIT 15,9 T€), Markt 2 (EBIT 3,1), Markt 3 (EBIT −14,8). Konzern 2027: Außenumsatz 22.000 T€, EBITDA 763,7, EBIT 318,4, Ergebnis nach GewSt 165,6 T€; EK-Quote 01.01. 28,6 %, Nettoverschuldung/EBITDA 2,85 **[Rechnung aus 08]**.

**Hausmarke: Limonade in Mehrweg-Glas (3 Sorten, 0,33 / 0,5 / 1,0 l), abgefüllt im Lohn.** Begründung: Natürliches Mineralwasser muss am Quellort abgefüllt werden **[wahrscheinlich, Mineral- und Tafelwasser-VO]**; eine eigene Anlage wäre ohne eigene Quelle unmöglich, Make-or-Buy also kein echter Fall. Apfelschorle hängt an volatilen Saftkonzentratpreisen und liegt thematisch nah an der verworfenen Kelterei **[Vermutung]**. Limonade bietet eine echte Rezepturkalkulation (Zucker, Grundstoff, CO₂), passt mit 0,33 l in die Gastronomie und bringt mit der geplanten Zuckersteuer einen Target-Costing-Anlass (Kabinett 14.10.2026: 26 ct/l bei 5–8 g, 32 ct/l ab 8 g Zucker je 100 ml ab 1.7.2027 **[wahrscheinlich]**).

**Zahlen Hausmarke 2027** (Lohnabfüllung mit Beistellung von Grundstoff, Zucker, Verschluss und Etikett; Rezeptur 7,5 g Zucker/100 ml; alle Werte **[Vermutung, Skript]**):

| je Kasten | 24 × 0,33 (Gastro) | 20 × 0,5 (Märkte, Heimdienst) | 12 × 1,0 (Märkte, Wiederverk.) |
|---|---|---|---|
| Absatz 2027 (Kästen) | 14.000 | 9.000 | 16.000 |
| Erlös netto ohne Pfand | 12,90 € | 10,40 € | 7,40 € |
| Rohstoff (0,19 €/l) | 1,51 | 1,90 | 2,28 |
| Verschluss + Etikett (0,03 €/Fl) | 0,72 | 0,60 | 0,36 |
| **Lohnabfüllpreis** (0,19 / 0,21 / 0,25 €/Fl) | 4,56 | 4,20 | 3,00 |
| Leergut-Ersatz (3 % Flaschen, 1 % Kästen) | 0,24 | 0,23 | 0,19 |
| Fracht (Sattelzug-Rückfracht) | 0,15 | 0,15 | 0,15 |
| **Einstand** | 7,18 | 7,08 | 5,98 |
| **DB I** (Quote) | 5,72 (44,4 %) | 3,32 (31,9 %) | 1,42 (19,1 %) |
| zum Vergleich: DB verdrängte Fremdmarke | 4,75 | 3,17 | 1,85 |

Summe 2027: 708.000 Flaschen, 392.880 l, Umsatz 392,6 T€, DB I 132,6 T€ (33,8 %), Lohnabfüllung 149,6 T€. Mit 70 % Kannibalisierung von Fremdware und 37 T€ Markenfixkosten (Labor, Listung, Marketing) bleiben **+8,4 T€ EBIT**. Der Leergut-Pool (186.250 Flaschen, 10.729 Individualkästen, 107,9 T€, Festwert nach § 240 Abs. 3 HGB **[wahrscheinlich]**) kostet 8 % Kontokorrentzins ≈ 8,6 T€. **Die Hausmarke ist 2027 EBT-neutral**; ihr Wert ist strategisch (Rezepturhoheit, Gastrobindung). Kommt die Zuckersteuer, kostet sie bei 7,5 g/100 ml ≈ 102 T€ im Jahr, das sind 77 % des DB I, solange sie nicht überwälzt wird. Wer Steuerschuldner ist (Abfüller oder Auftraggeber), ist laut Entwurf zu prüfen **[Vermutung]**. Der Golden Master aus 08 muss um die Hausmarke erweitert werden.

**Figuren** (Vertrauen je Figur ist eine Spielressource):

| Figur | Rolle | Haltung, Konflikt | Lernfunktion |
|---|---|---|---|
| Tobias Wernsing (44) | Geschäftsführer, Kommanditist, 2. Generation | will Wachstum, die Hausmarke ist sein Projekt | Adressat aller Vorlagen (HB5), entscheidet |
| Hildegard Wernsing (69) | Seniorchefin, Beiratsvorsitz | führte Markt 1 bis 2019 selbst: „Der Markt hat 50 T€ verdient“ | Abgrenzung, Bilanzanalyse, Beiratspräsentation (HB3/HB6) |
| Ralf Kübler (56) | Spartenleiter Großhandel/Vertrieb | denkt in Hektolitern, schützt Wirte | Kunden-DB, Budget-Slack (M33, M51) |
| Derya Aksoy (41) | Spartenleiterin Märkte, GF Märkte GmbH | kämpft gegen den Verrechnungspreis „Einstand + 3 %“ | Profit Center, VP (M41) |
| Sabine Kowalski (47) | Marktleiterin Markt 1 (06 F18) | Prämie auf Markt-Rohertrag | Aktionen, Business Partnering (Kap. 1) |
| Holger Timmermann (52) | Logistikleiter: Fuhrpark, Lager, Leergut | will Touren straffen, Fahrermangel | Prozesskosten, sprungfixe Kosten (M12, M14) |
| Kemal Yıldız (34) | Gastro-Außendienst | Prämie auf Umsatz, vergibt gern Darlehen | Kreditrisiko, Anreize (M37, M51) |
| Marc Lindemann | Key Account GFGH der Brauerei Nordhang | Konditionen, WKZ, Bonusstaffel | Konditionencontrolling, Verhandlung (M48, M43) |
| Petra Hollmann | GF des Lohnabfüllers (60 km) | eigene Marke hat im Sommer Vorrang | Kalkulationsprüfung, Verhandlung |
| Ulrich Kessler | GF einer Regionalbrauerei | will seine alte AfG-Linie schließen | Zusatzauftrag, Preisuntergrenze, Klumpenrisiko |
| Katrin Vogt | Firmenkundenbetreuerin Hausbank | Covenants: EK-Quote ≥ 25 %, ND/EBITDA ≤ 3,5, KDF ≥ 1,2 **[Annahme, 08]** | HB3, M50 |
| Dr. Frank Esser | Abschlussprüfer (KG ist prüfungspflichtig, 08) | Stichproben aus *deinen* Abschlüssen | verzögertes Feedback, Worked Examples |
| Lena Brockmann | Assistenz Controlling ab 2028 | lernt von dir, macht typische Fehler | Teamführung, Lernen durch Lehren (M55) |

Worked Examples kommen diegetisch aus dem **Übergabeordner des Vorgängers** („Pohls Ordner“) und vom Prüfer. Wer den Ordner nutzt, löst „mit Hilfe“ (zählt nicht für Mastery).

---

## 5. Spielschleifen auf allen Zeitskalen

**Minute (Aufgabenschleife, 1–4 min):** Figur stellt Frage in ihrer Sprache („Lohnt sich die 9,99-€-Woche?“) → Spieler öffnet Daten (Glass Box: jede Zahl bis zum Beleg klickbar) → rechnet im Arbeitsblatt → Sicherheitsregler 50/70/90 % → Abgabe → diagnostisches Feedback (Folgefehler, Misconception) → „Warum?“-Frage (Auswahl) → Ergebnis wird Spielwirklichkeit (Bericht, Vorlage, Buchung).

**Session (25–35 min):**
1. **Frühschicht** (5–8 min): 5–8 fällige Items, gemischt über ≥ 3 HB, neue Zahlen aus dem eigenen Spielstand.
2. **Posteingang:** 2–4 Ereignisse (Brief des Lohnabfüllers, Rücklastschrift, Wetterwarnung).
3. **Monatsabschluss** als Arbeitstage AT1–AT6 (07): Belege und Leergutauszüge → Kreditoren, Abgrenzung Boni/WKZ → Bestands- und Leergutplausibilität → Kostenstellen, Fuhrpark je Fahrzeug → Segment-/Kunden-DB → Bericht. Pflichtschritte sperren das Monatsende (Abschluss-Gate).
4. **Fall des Monats:** eine Abweichung als Deduktionsfall mit Datenraum und Fallakte (Ursache, Betrag, Art, Maßnahme).
5. **Entscheidungskarten** (3–5): Ja / Nein / Prüfauftrag; mit gemeisterten Methoden zeigen die Karten Effektvorschauen.
6. **Monatsgespräch** mit einer Figur (Dialogbaum, Optionen hängen an gemeisterten Skills).
7. **Nachbesprechung** (3–5 min, Pflicht).

**Spielmonat:** Kalender je Kapitel; Tage laufen im Zeitraffer und halten nur bei Karten. Quartalsende bringt Forecast, Covenant-Reporting und eine Prüfer-Stichprobe.

**Spieljahr (Routinen kehren wieder, Bedingungen wechseln):**

| Monat | Routine | 2027 | 2028 | 2029 |
|---|---|---|---|---|
| Jan | Inventur an 4 Standorten, Leergut-Saldenbestätigung, Bonusabrechnung | Mindestlohn 14,60 €, Diesel-Rabattende | 290 T€ Altboni eintreiben | Festwert Leergut-Pool Hausmarke prüfen |
| Feb–Apr | Jahresabschluss, Prüfer, Bankgespräch | JA 2026 des Vorgängers analysieren | erster eigener JA, Covenant-Test | JA 2028 entscheidet über die Kreditzusage |
| Mär–Apr | Jahresgespräche Brauereien | Aktionsplan Pils | Bonusstaffel neu | Lohnabfüller-Vertrag |
| Mai | Saison-Liquidität, Vorkauf | Zuckersteuer-Entscheidung | Lohnabfüller-Brief | Inbetriebnahme oder Open-Book |
| Jun–Aug | Hitzewelle (1× je Saison gezogen, 06 E10), Feste | Kistenknappheit möglich | Fahrermangel | Linie im Engpass |
| Jul | Halbjahres-Forecast | | | |
| Sep | Strategieklausur | Segmentportfolio | Make-or-Buy-Szenarien | E-Sattelzug |
| Okt–Nov | Budget im Gegenstrom, Preisrunde | Budget 2028 (erste Runde) | Budget 2029 mit Investition | Budget 2030 |
| Dez | Bonusklippe, Vorkauf, Silvester-Leergut | | | |

**Kampagne:**

| Kapitel | Zeit | Leitfrage (Figur) | Schwerpunkt | Gate |
|---|---|---|---|---|
| 1 Pilotmarkt | Jan–Apr 2027, Markt 1 | „Früher hat Markt 1 50 T€ verdient, jetzt 15,9. Was habt ihr kaputt gemacht?“ (Hildegard) | HB1-Grundlagen, Pfand, HB4-Bericht | Kern-LZ Kap. 1 „gelernt“ |
| 2 Großhandel | Mai–Dez 2027, KG | „Welche Kunden und Touren tragen uns?“ (Tobias) | Prozesskosten, Kunden-DB, Konditionen, Liquidität | Kern-LZ Kap. 2 „gelernt“, Budget-Freigabe |
| 3 Gruppe | 2028 | „Steuern wir richtig, und bleibt die Bank bei uns?“ (Vogt, Aksoy) | VP, Profit Center, Budget mit 4 Verantwortlichen, JA-Analyse, Konsolidierung light | Covenant-Bericht ohne Prüferbeanstandung |
| 4 Abfüllung | Mai 2028–2029 (parallel zu 3) | „Füllen wir selbst ab?“ (Tobias) | Industrie-KLR, Make-or-Buy, HB5-Vorlage, HB6-Beirat | Entscheidungsvorlage ≥ 7/10 Rubrikpunkte |
| Epilog (optional) | 2030 | Übernahmeangebot eines Konzern-GFGH | Bewertung (M56), Fachgespräch | – |

Drei große **Weichen** (Aktionspolitik Markt 1, Liefer- und Darlehenspolitik Gastro, Make or Buy) mit vielen kleinen Folgen über Zustandsvariablen; die Handlung läuft danach wieder zusammen. Ein Konkurs ist ausgeschlossen: Ein Covenant-Bruch startet einen **Krisenmodus** (13-Wochen-Plan, Bank-Workout, StaRUG-Frühwarnung, M37/M50).

---

## 6. Lernsystem

**Theorie:** Lernkarte ≤ 90 Wörter, Formel direkt an den Zahlen, durchgerechnetes Beispiel mit Gruppenzahlen. Sie erscheint just in time, wenn die Geschichte das Thema zum ersten Mal braucht. Jede Karte hat ein leeres Feld `skript_ref` für das Kapitel des Lehrgangsskripts. „Wissen ist Sicht“: Gemeisterte Methoden schalten Effektvorschauen, Drilldowns und Dialogoptionen frei (03).

**Praxis:** Parametrisierte Vorlagen (04): Jede Wiederholung zieht neue Zahlen, bevorzugt aus dem eigenen Spielstand („Juni-Wareneinsatz *deines* Markts“). Vier Fading-Stufen je Skill (vorgemacht → letzter Schritt fehlt → zwei Schritte fehlen → leer), adaptiv, mit Einstufungstest für Kundige. Nach dem Ersterwerb nur noch gemischte Aufgaben; die Aufgabe nennt die Methode nicht.

**Wiederholung (Pflichtmechanik und Algorithmus):**
1. Jeder Skill ist eine ts-fsrs-Karte (FSRS v6, Zielbehalt 90 %), Zeit in **Kalendertagen** (06 W8/W10).
2. Rating aus dem Ergebnis: falsch oder Lösung angezeigt = Again; richtig mit Hinweis oder im 2. Versuch = Hard (wird geplant, zählt nicht für Mastery); richtig = Good; richtig und schneller als der eigene Median = Easy.
3. Täglich: Kandidaten mit Abrufwahrscheinlichkeit R < 0,90. Priorität = (0,90 − R) × IHK-Gewicht (hoch 1,0 / mittel 0,6 / niedrig 0,3) × 1,2 bei Bezug zum aktuellen Kapitel + Bonus bei wiederholter Misconception (≥ 2× in 7 Tagen → Contrast-Pair-Block). Höchstens 8 Items, mindestens 3 HB, keine zwei aus derselben Vorlage.
4. **Ein Gate pro Ebene** (06 W11): Hat ein Pflichtschritt des Monatsabschlusses einen Kern-Skill mit R < 0,70, ist der Schritt gesperrt, bis ein 2-Minuten-Auffrischer gelöst ist. Der Auffrischer zählt zugleich als Pflichtaufgabe. Ausweichen: an Lena delegieren (kostet ihre Kapazität) oder an den Prüfer (150 € Honorar, Vertrauen −); beides ohne Mastery.
5. Beliebig viele Spielmonate pro Tag sind spielbar, FSRS wertet aber nur den **ersten Abschluss je Kalendertag** (06 Karte 42).
6. Pflichtanteil ≤ 30 % der Sessionzeit; darüber führt der Scheduler weniger neue Skills ein.
7. Gegen zu seltene Jahresroutinen (06, 6.7): quartalsweise Mini-Zyklen (Forecast, Covenant-Bericht, Bonus-Hochrechnung) und „Übungsmandate“ abseits der Hauptlinie, z. B. ein Probeabschluss für Markt 2.

**Mastery (dreistufig):** *gelernt* = 3 unassistierte richtige Lösungen mit verschiedenen Parametern an ≥ 2 Kalendertagen plus 1 im zweiten Format. *beherrscht* = FSRS-Stabilität ≥ 21 Tage plus ≥ 2 korrekte Anwendungen im Spielkontext. *prüfungsreif* (je HB) = IHK-Format ≥ 65 Punkte zweimal in Folge. Kapitel-Gates verlangen „gelernt“, Verantwortung (Budget, Bankgespräch) verlangt „beherrscht“ der Voraussetzungen.

**Feedback und Debriefing:** Sofort und diagnostisch bei Routinen; verzögert über Monatsbericht und Bankgespräch bei Entscheidungen; spät über die Prüfer-Stichprobe, die alte Fehler zur Aufgabe macht. Nachbesprechung je Monat: drei auffällige Zahlen mit Vorhersage, Treiberbaum, **Kontrafaktum** per Replay mit gleichem Seed und genau einer geänderten Entscheidung (erfordert Common Random Numbers, 06 W12), Expertenpfad, Lehrsatz ins Notizbuch. Jahresdebriefing trennt Entscheidungsqualität vom Ergebnis.

**Fehler:** Jeder Fehler wird ein Fall in der Fallakte und kommt als Wiederholung zurück. Wer mit 90 % Sicherheit falsch liegt, bekommt eine betonte Erklärung (Hypercorrection). Konsequenzen sind spürbar, aber reparabel (Korrekturbuchung, Vertrauensdelle). „Erst probieren“ nur bei Konzeptthemen (Make-or-Buy, Verrechnungspreis, Darlehen als Investition), nie bei Routinen.

---

## 7. Inhaltsabdeckung

**ID-Schema für die spätere Skript-Zuordnung:** HB → **Lernziel** `LZ-HB1-06-03` (HB, Modulnummer aus 01/06, laufende Nr.) → **Skill** `sk.bab.stufenleiter` → **Vorlagen** → Routinen und Szenen. Spiel und Geschichte referenzieren nur Skills. Die Datei `lernziele.yaml` führt je LZ: HB, Modul, Text, Bloom-Stufe, Skills, Prüfungsform, Kern/Ausblick und `skript_ref` (anfangs leer). Kommen die Skripte, werden nur `skript_ref` gefüllt und fehlende LZ ergänzt; der Build meldet Lücken (jedes Kern-LZ: ≥ 3 Vorlagen, ≥ 2 Kontexte, ≥ 1 Routine, ≥ 1 IHK-Format-Item). Die Zuordnung LZ ↔ HB ist abgeleitet, weil der DIHK-Rahmenplan nicht frei verfügbar ist **[wahrscheinlich, 01]**.

| HB | Kapitel | Module | Übung mit Gruppenzahlen | Aufgabentyp |
|---|---|---|---|---|
| HB1 | 1 Pilotmarkt | M04, M05 | Überleitung Markt 1: EBIT 50,5 T€ (Einzelmarkt 02) → 15,9 T€ (Filiale): Heimdienst/Fest in die KG, Einkaufsvorteil 6 %, VP +3 %, Umlage 32,2, Inhaber → angestellte Leitung | Überleitungstabelle mit Folgefehler |
| HB1 | 1 | M07 | Rückwärtskalkulation Hausmarke 1,0 l: VK 8,99 brutto = 7,555 netto, Zielspanne 25 % → max. Einstand 5,67 € < Ist 5,98 € | Lückentabelle Kalkulationsschema |
| HB1 | 1 | M09, M45, M51 | Aktion Pils: Markt −352 €, Gruppe +32 € je Woche (Szene 1) | Mehrschritt, Fallakte |
| HB1 | 1–2 | M12, M44 | Leergut 0,45 €/Kasten brutto, 0,35 € nach Sortiervergütung; Markt-Automat vs. KG-Sortierung | Prozesskostensatz bilden |
| HB1 | 2 Großhandel | M12, M33, M14 | Eckkneipe DB III −498 €, relevant +1.002 €; Rhythmusprogramm 106,6 T€ „Ersparnis“, davon kurzfristig 15,1 T€ (Szene 2) | Tabelle DB I–III, Entscheidung begründen |
| HB1 | 2 | M31, M48, M15 | Nachvergütungen 417,4 T€, 290 T€ offen; Vorkauf vor Preisrunde (+3,75 €/Fass, 1.200 Fässer, netto ≈ +2,7 T€, 07) | Hochrechnung, Stufensprung |
| HB1 | 3 Gruppe | M41, M40, M14 | VP-Varianten Märkte (Summe stets −165,8 T€); Schließung Markt 3: −17,9 T€ bei 50 %, +9,7 T€ bei 100 % Logistikabbau | Variantentabelle, Invarianzprobe |
| HB1 | 4 Abfüllung | M06, M07 | Plan-BAB, MSS 270,15 €/h, ÄZ 1,00/1,15/1,60 → 0,176/0,203/0,282 €/Fl (Szene 3) | Stufenleiter-Tabelle, Mehrschritt |
| HB1 | 4 | M11 | Juli 2029: Verbrauchsabw. +2,47, Beschäftigungsabw. +3,33 T€ | Abweichungszerlegung mit Summenprobe |
| HB1 | 2–4 | M13 | Zuckersteuer 26 ct/l = 2,06 €/Kasten 0,33 l; Zielkosten für Rezeptur < 5 g | Target Costing |
| HB2 | 2–3 | M18, M51 | Budget 2028 im Gegenstrom: Kübler plant +4 % Gastro trotz Gedat-Trend −4 % Stopps **[wahrscheinlich, 07]** | Budgettabelle, Slack-Diagnose |
| HB2 | 2 | M23, M24, M49 | Kontokorrent +89,6 T€ im Plan, Pfand-Float 341,7 T€ zu 8 %, Silvester-Überhang 79,0 T€, Steuertermine | 13-Wochen-Plan |
| HB2 | 2–4 | M25, M54 | E-Sattelzug (07: −19,5 T€ Energie, −20,7 T€ Maut, +30 T€ Leasing); Abfüllanlage KW (Szene 3) | KW, Sensitivität |
| HB2 | 3 | M16, M17, M37 | Segment-DB III: Gastro 11,8 %, Wiederverkäufer 0,8 %, Strecke 5,0 % (25 Kunden); Darlehensportfolio 1.200 T€ | Portfolio, Risikomatrix |
| HB3 | 3 | M22, M50 | JA 2027: EK-Quote 30,4 % brutto / 32,8 % Pfand saldiert, ND/EBITDA 2,64, KDF 2,03 (M50-Formel) | Strukturbilanz, Covenant-Bericht |
| HB3 | 1–3 | M02, M44 | Pfand-Bruttomodell (BFH I R 36/07 **[wahrscheinlich]**), Leergut-Pool der Hausmarke als Festwert | Buchung, Zuordnung |
| HB3 | 3 | M40 | Zwischengewinn Märkte-Vorräte 263,0 × 3/103 = 7,66 T€; Schuldenkonsolidierung Cash-Pool 150 T€ | Konsolidierungsbuchung |
| HB4 | alle | M26–M29, M53 | Monatsbericht Markt 1 (IBCS), Segmentbericht, Bankbericht; Datenqualität: Fahrerzählung Leergut vs. Lagerzählung | Satzbaustein-Kommentar, Diagramm-Aufgabe, HB4-Werkstatt |
| HB5 | 3–4 | M42, M14, M25 | Entscheidungsvorlage Abfüllanlage für Beirat; Alternativthemen Markt 3, VP-System, Fuhrpark | Vorlage nach Rubrik |
| HB6 | 2–4 | M43, M55 | Budgetrunde moderieren (Kübler, Aksoy, Timmermann), Inventur leiten, Lena anleiten, Verhandlung Hollmann | Dialogbaum, Moderationszyklus |

**Auch in der Gruppe nur schwach abgedeckt:** M21 wertorientierte Steuerung (kein Kapitalmarkt, WACC bleibt Annahme). M40 nur HGB-Konsolidierung light, freiwillig für die Bank, ohne IFRS, Minderheiten, Equity-Methode. M39 CSRD (nur VSME-Anfragen). M55/M43 Teamführung (der Controller führt allenfalls eine Assistenz). Industrie-KLR ohne Kuppelproduktion; Bestandsveränderungen nur im Make-Zweig. M45/M53 (Aktionen, Warenkorb) nur in den Märkten. Projektarbeit und Fachgespräch bleiben Methodentraining.

---

## 8. Branchenspezifische Mechaniken

| Mechanik | So wird sie gespielt | Trainiertes Controlling-Wissen |
|---|---|---|
| Vollgut-/Leergutkonten | Konten je Partner und Gebindeart **in Mengen**; Monatsbilanz AB + Rücknahme − Rückgabe − Ausbuchung = EB; Abgleich mit Brauerei-Auszug; Leergutdifferenzen 48,5 T€/Jahr | M44, M38 (Fahrer- vs. Lagerzählung), M02, M08 |
| Pfand-Float | 341,7 T€ über Kontokorrent finanziert (Konzernbilanz 08 ohne Kelterei: 1.057,5 − 535,8 − 180,0 **[Rechnung]**); Silvester-Überhang 79,0 T€ verzerrt den Stichtag | M23, M24, M22 (Bilanzpolitik) |
| Wetter-Forecast | 7-Tage-Prognose mit Fehlerband, Ist kommt später; Bestellung nach Newsvendor; Hitzewelle einmal je Saison gezogen | M46, M19, M30 |
| Aktionen | Aktions-EK nur gegen Abverkaufsnachweis, Restmenge wird nachbelastet; WKZ fließt der KG zu, nicht dem Markt | M45, M15, M41, M51 |
| Konditionen, Boni, Vorkauf | Bonusstaffeln mit Klippe, Vorkauf vor Preisrunden, hl-Meldungen | M48, M31, M08, M22 |
| Gastro-Darlehen und Leihinventar | 1.200 T€ Darlehen zu 3 %, 300 T€ Neuvergabe pro Jahr; Insolvenzkaskade (Forderung, Darlehen, Inventar, Leergut) | M25 (Darlehen als Investition), M33, M37 |
| Forderungen | DSO Gastro 25 Tage; Frühwarnsignale Rücklastschrift, wachsender Leergutsaldo | M24, M37, M30 |
| Touren und Fuhrpark | Tourtag 454,30 €, Stopp 34,16 €, Auslastung 94,8 %; Diesel ±30 ct = ±33,4 T€ | M12, M05 (sprungfix), M14, M25, M39 |
| Lager | 0,30 €/Kolli Lagerung, 0,32 €/Kolli Kommissionierung; Hilfsstellen mit Leistungsverrechnung | M06, M12, M32 |
| Saison | Monatsindex 6,5–10,5 %, Kontokorrent-Spitze im Dezember | M18, M23, M03 |
| Ereignisse | Zuckersteuer, Preisrunde, Fahrermangel, Gastro-Insolvenz, Kistenknappheit, Großkundenverlust Strecke, Brauerei-Insolvenz | M37, M19, M16 |
| Hausmarke | Rezeptur, Lohnabfüllpreis, Leergut-Pool, Zuckersteuer, Make-or-Buy | M07, M13, M14, M06, M11, M25 |
| Verrechnungspreise | „Einstand + 3 %“ deckt die interne Logistik (7,3 % des Märkteumsatzes) nicht | M41, M40, M51 |
| E-Rechnung | Pflicht für alle B2B-Rechnungen der KG ab 2027 **[sicher, 02/07]** | M35, M29 |

---

## 9. Aufgabentypen und automatische Bewertung

| Typ | Beispiel | Bewertung |
|---|---|---|
| Zahl mit Toleranz | Kosten je Stopp | ± 1 € bzw. ± 0,5 % relativ, Quoten ± 0,1 PP |
| Mehrschritt | Stück-DB → Inkrement → Wochenergebnis | jeder Schritt gegen das eigene Vorergebnis (Folgefehler = Teilpunkte) |
| Lückentabelle | BAB, Kalkulationsschema, Budget | zellweise mit Folgefehler |
| Buchung | Pfand-Einkauf, Konsolidierung | Soll/Haben-Menge, Reihenfolge egal |
| Fallakte (Deduktion) | Rohertrag-Rückgang | Slots Ursache/Betrag/Art/Maßnahme, Bestätigung ab 2 korrekten Slots |
| Fehlersuche | Kalkulation des Lohnabfüllers | Fehlerstelle + korrigierter Betrag |
| Entscheidung begründen | Kündigen oder Rhythmus ändern | Auswahl + 2 von 6 Gründen |
| Satzbaustein-Kommentar | Abweichungskommentar „Was – Warum – Was tun – Wer bis wann“ | regelbasiert; Freitext mit LLM nur als Feedback, nie als Gate |
| Dialog | Monatsgespräch, Verhandlung | Zielerreichung (BATNA gehalten, Einwand entkräftet) |
| **IHK-Format** | Situationsaufgabe mit 4–6 Teilaufgaben, 100 Punkte, Zeitlimit (HB1/HB2 180 min, HB3 90 min) | Punkteschema je Schritt; eigene Aufgaben, keine Original-Prüfungsaufgaben **[sicher: urheberrechtlich geschützt, 05]** |

**Fehlerdiagnose:** Katalog aus 03 (M1–M12) plus gruppenspezifisch: D1 Prozesskostensatz als abbaubare Kosten gelesen · D2 versunkene Inventar-AfA als entscheidungsrelevant · D3 „VP verändert das Gruppenergebnis“ · D4 Zwischengewinn nicht eliminiert · D5 Pfand netto/brutto vermischt · D6 Bonusbasis Vorjahr statt Plan · D7 ÄZ auf Liter statt Flasche bezogen · D8 kalkulatorischer Zins auf volle AHK · D9 Beschäftigungsabweichung als Verschwendung gedeutet · D10 Aktion am Umsatz gemessen. Jeder Distraktor ist das Ergebnis einer dieser Fehlerfunktionen.

---

## 10. Training für HB4, HB5, HB6

**HB4 (Tabellenkalkulation):** Im Spiel ein Arbeitsblatt mit Lückentabellen und freiem Formelmodus (eigener Parser plus formula.js, 04). Dazu die **HB4-Werkstatt**: Export echter Spieldaten als XLSX (27.000 Gastro-Stopps, Kassendaten Markt 1, Budgetrohdaten) mit Aufträgen im IHK-Stil: Pivot Kunden-DB nach Klassen, Szenario-Budget mit Zielwertsuche, IBCS-Diagramm. Geprüft werden 10–15 benannte Ergebniszellen nach Re-Import (exceljs) plus Plausibilität; Formelqualität nur per Checkliste. Einmal je Kapitel eine 240-min-Probeübung **[Vermutung: Ergebnisprüfung reicht für Feedback, nicht für Note]**.

**HB5 (Projektarbeit):** Das Kapitel 4 ist als **„Meisterstück“** gebaut: Auftragsklärung → Ist-Analyse → Alternativen → Bewertung (KW, Nutzwert, Sensitivität) → Empfehlung → Umsetzungs- und Risikoplan, also der Beratungsprozess aus M42. Der Spieler füllt einen Gliederungs-Baukasten mit Zahlen aus dem Spiel; automatisch geprüft werden Zahlen, Vollständigkeit und Logik (Empfehlung passt zur eigenen Rechnung), dazu eine 10-Punkte-Rubrik zur Selbstbewertung. Export als Dokument. Ehrlich: Die IHK-Projektarbeit behandelt den eigenen Betrieb; das Spiel übt die Methode und liefert eine Themenliste als Vorlage.

**HB6 (Präsentation, Fachgespräch, Führung):** Folienbaukasten für die Beiratssitzung (max. 3 Kernaussagen, Pyramidenprinzip). **Fachgesprächs-Simulation**: 15 Minuten, Fragen von Beirat, Bank und Prüfer zu den eigenen Entscheidungen, Antworten per Struktur-Auswahl; optional Sprachaufnahme zur Selbstkontrolle und LLM-Rollenspiel mit Feedback, nie als Gate. Moderation der Budgetrunde als Mini-Spiel (Moderationszyklus, Konflikt Kübler ↔ Timmermann). Führung über Lena (delegieren, Fehler korrigieren, Feedback nach Situation–Verhalten–Wirkung) und die Inventurleitung. Empfehlung für Prüflinge: zusätzlich Peer- oder Präsenzübung.

---

## 11. Drei Beispielszenen

### Szene 1 – „Die 9,99-€-Woche“ (Kapitel 1, März 2027, Markt 1, ≈ 25 min)

**Ausgangslage:** Lindemann (Brauerei Nordhang) bietet für KW 11 Fernsehpils L01 (20 × 0,5) zu 9,99 € brutto an: Aktions-EK 8,20 €, WKZ 400 €. Sabine will sofort zusagen: „Die Kunden lieben das.“ Tobias fragt: „Lohnt sich das?“ Sabines Prämie hängt am Markt-Rohertrag.

1. **Frühschicht:** 6 Items, darunter „Spanne vs. Aufschlag“ (Rost) und „Pfand gehört nicht in den Rohertrag“.
2. **Glass Box:** Normal-VK 17,49 € = 14,697 € netto. Rechnungs-EK 12,40 €, Gruppen-Einstand 94 % = 11,656 €, VP an den Markt +3 % = 12,006 €. Aktion: 8,395 € netto; Einstand 7,708 €, VP 7,939 €.
3. **Fading-Stufe 2:** Stück-DB normal Markt 2,692 € / Gruppe 3,041 €; Aktion Markt 0,456 € / Gruppe 0,687 € (Spieler ergänzt die Aktionswerte).
4. **Inkrementeller Rohertrag je Woche** (Modell aus 02/06: Basis 120 Kästen, Lift × 4, 60 % Kannibalisierung, 48 Kästen Nachholeffekt, 150 Verbundbons, Leergut für 96 echte Mehrkästen):

| Komponente | Markt 1 (VP) | Gruppe (Einstand) |
|---|---|---|
| 480 Aktionskästen × Stück-DB | +218,7 | +329,7 |
| entgangene Basis 120 Kästen | −323,0 | −365,0 |
| Kannibalisierung 216 Kästen (2,80 / 3,10 €) | −604,8 | −669,6 |
| Nachholeffekt 48 Kästen | −129,2 | −146,0 |
| Verbund 150 Bons (3,40 / 3,60 €) | +510,0 | +540,0 |
| WKZ (fließt der KG zu) | 0 | +400,0 |
| Leergut 96 Mehrkästen (Markt 0,25 €, KG +0,35 €) | −24,0 | −57,6 |
| **Ergebnis je Aktionswoche** | **−352,3 €** | **+31,6 €** |

5. **Fehlerdiagnose:** Wer „+2.265,90 € Umsatz netto“ abgibt, bekommt D10 („Aktion am Umsatz gemessen“). Wer 0,456 € für die Gruppe nimmt, bekommt D3 („VP verschiebt nur“).
6. **Monatsgespräch Sabine:** Option *Vorwurf* („Ihre Aktion kostet 352 €“) → Vertrauen Sabine −. Option *Zahlenblick* (nur mit Skill Stück-DB gemeistert): „Für den Markt ist es ein Verlust, für die Gruppe knapp positiv, nur wegen des WKZ. Das Problem ist Ihre Prämienbasis.“ → öffnet Folgeaufgabe Prämienformel (M51) und den Kapitel-3-Faden „Verrechnungspreis“.
7. **Entscheidungskarte an Tobias:** Zusage / Absage / Gegenangebot „10,99 € mit Aktions-EK 8,60 €“ (gerechnet bei gleichem Lift, also optimistisch: Markt −134,8 €, Gruppe +254,5 €). Annahme hängt an Vorlagenqualität und Vertrauen.
8. **Verzögerte Konsequenz (April-Abschluss):** 300 Kästen wurden zum Aktions-EK bezogen, aber erst nach KW 11 normal verkauft. Die Brauerei belastet 300 × (11,656 − 7,708) = **1.184 €** nach. Wer im März keine Abgrenzung gebildet hat, findet die Differenz als Fall des Monats.
9. **Nachbesprechung:** Kontrafaktum „Gegenangebot statt Zusage“, Lehrsatz „Wessen Marge? Erst die Ebene klären.“ Skills „Inkrementeller Aktionserfolg“ und „VP-Ebene“ gehen in den Scheduler; die Transferaufgabe kommt in Kapitel 3 als Verrechnungspreisfrage zurück.

### Szene 2 – „Die Eckkneipe“ (Kapitel 2, Oktober 2027, KG, ≈ 30 min)

**Ausgangslage:** Timmermann will 120 B-Kunden am unteren Rand „rauswerfen oder auf 14-tägig setzen“. Beispiel ist die Eckkneipe „Zum Anker“: 12 T€ Umsatz, 52 Stopps, 670 Kolli. Kemal wehrt sich: „Das sind meine Stammkunden.“

1. **Kunden-DB aus Prozesskostensätzen (Fading 3, 08 2.9):** RE I 4.200 € → DB I 4.200 → Lagerung/Beschaffung −262, Kommissionierung −217, Leergut −201, Stopps 52 × 34,16 € = −1.776 → **DB II 1.744 €** → Außendienst −502, AfA Leihinventar −1.500, Ausfallrisiko −240 → **DB III −498 €**.
2. **Relevanz:** Die Inventar-AfA ist für eine Kündigung versunken (D2). Ohne sie trägt der Kunde **+1.002 €** pro Jahr bei; Kündigung schadet, solange das Inventar nicht anderswo einsetzbar ist.
3. **Alternative 14-tägig:** 26 Stopps → DB III **+390 €**.
4. **Hochrechnung auf 120 Kunden:** −3.120 Stopps = 183,5 Tourtage. Die Prozesskostenrechnung „spart“ 3.120 × 34,16 € = **106,6 T€**. Kurzfristig abbaubar sind nur Diesel und Maut: 183,5 × 82,36 € = **15,1 T€ (14,2 %)**. Fahrerkosten 41,9 T€ fallen nur weg, wenn eine offene Fahrerstelle unbesetzt bleibt; 38,6 T€ Lkw-Fixkosten erst, wenn ein Leasingvertrag endet. Dann fahren 9 statt 10 Lkw mit 97,2 % Auslastung, also fast ohne Reserve (D1, M05 sprungfix).
5. **Hausmarke als Hebel?** Listung der 0,33-l-Limonade beim Anker: +0,97 €/Kasten gegenüber der Fremdmarke, bei 40 Kästen +39 € im Jahr. Lehrsatz: Sortiment rettet keinen Stoppkosten-Kunden.
6. **Moderiertes Gespräch Timmermann ↔ Kemal:** Ziel ist eine gemeinsame Regel (Rhythmus nach DB II, Mindestbestellwert 125 €, Ausnahme mit Begründung). Je nach Verlauf sinkt das Vertrauen einer der beiden Figuren.
7. **Nebenfaden mit verzögerter Folge:** Im Datenraum stehen beim „Bistro Mühlentor“ zwei Rücklastschriften und ein wachsender Leergutsaldo. Wer jetzt einen Prüfauftrag zieht (Kreditlimit, Barzahlung, Inventar sichern), halbiert den Schaden. Ohne Reaktion meldet das Bistro im Februar 2028 Insolvenz: Forderung 6,0 T€ × 95 % + Darlehensrest 18,0 + Inventar 8,0 × 70 % + Leergut 1,4 = **30,7 T€**, einzuordnen im ersten eigenen Jahresabschluss.
8. **Nachbesprechung:** Kontrafaktum „alle 120 Kunden kündigen“ (Umsatz- und DB-II-Verlust gegen 15,1 T€ Ersparnis). Lehrsatz: „Prozesskostensätze sind Vollkosten; abbaubar ist, was jemand abbaut.“

### Szene 3 – „Selbst abfüllen?“ (Kapitel 4, Mai–Dezember 2028, ≈ 4 Sessions)

**Ausgangslage:** Hollmann kündigt ab 2029 +18 % an, dazu 380 € Rüstpauschale je Charge und Kapazitätsvorbehalt im Juni–August. Tobias: „Dann bauen wir selbst.“ Kessler sucht für 1,0 Mio. Flaschen 0,5 l pro Jahr einen Lohnabfüller, bietet 0,16 €/Fl und zunächst 3 Jahre Vertragslaufzeit. Planvolumen Hausmarke 2029: 1,06 Mio. Flaschen (26.000/11.000/18.000 Kästen), abhängig vom Gastro-Rollout aus Kapitel 2.

1. **Erst probieren:** „Lohnabfüllung kostet 280 T€ im Jahr, die Anlage 950 T€, nach 3,4 Jahren bezahlt.“ Die Auflösung zeigt, was fehlt: eigene Betriebskosten, Auslastung, Zeitwert.
2. **Plan-BAB** (gebrauchte, überholte Mehrweg-Glaslinie, 4.000 Fl/h nominal bei 0,33 l, OEE 65 % = 2.600 Äquivalenzflaschen/h; AHK 950 T€, Wiederbeschaffungswert 1.050 T€, 10 Jahre; Halle 800 m² von der Besitzgesellschaft zu 5 €/m²; Worked Example von Kesslers Betriebsleiter). Planbeschäftigung 2029 inklusive Kessler: 2.372.600 ÄZ-Fl = **912,5 h** (54,1 % einer Schicht, Hausmarke allein 27,9 %).

| T€ | H1 Energie/Medien | H2 Technik | H3 QS/Labor | F1 Ausmischung | F2 Leergut/Waschen | F3 Füllen/Etikett. | F4 Palett./Lager |
|---|---|---|---|---|---|---|---|
| Primärkosten | 58,9 | 42,9 | 32,2 | 24,3 | 87,4 | 141,5 | 31,1 |
| Umlage H1 (nach kWh) | −58,9 | +1,8 | +1,2 | +2,9 | +32,4 | +14,7 | +5,9 |
| Umlage H2 (nach Instandhaltungsstunden) | – | −44,7 | +0,9 | +3,6 | +15,6 | +20,1 | +4,5 |
| Umlage H3 (nach Prüfaufwand) | – | – | −34,3 | +13,7 | +3,4 | +17,1 | – |
| **Endkosten** | 0 | 0 | 0 | **44,5** | **138,8** | **193,5** | **41,5** |

   Summe 418,2 T€, davon fix 300,5 T€ (inkl. kalk. AfA 105 und kalk. Zins 28,5 als Anderskosten: bilanzielle AfA nur 95), variabel 117,7 T€ (Maschinenführer aus dem Lagerpool je Laufstunde, Energie, Wasser, Instandhaltung).
3. **Maschinenstundensatz Linie (F2 + F3):** maschinenabhängig **270,15 €/h**, mit Bedienpersonal 364,11 €/h.
4. **Äquivalenzziffern** nach Maschinenzeit je Flasche (0,33 l = 1,00; 0,5 l = 1,15; 1,0 l = 1,60): Fertigungskosten 0,1763 € je ÄZ-Flasche → **0,176 / 0,203 / 0,282 €** je Flasche. Lohnpreis neu 0,224 / 0,248 / 0,295 €.
5. **Kalkulationsprüfung Hollmann** (0,33 l, je 1.000 Fl): Linie 418,50 €/h + Personal 176 €/h bei 4.000 Fl/h = 148,62; Energie 22,40 (+40 %); Reinigung 9,50 → 180,53 × 1,15 Gemeinkosten × 1,08 Gewinn = **224,21 €** (+18,0 % auf 190). Gefunden werden: **A** kalkulatorischer Zins auf volle statt halbe AHK, 35 €/h zu viel → −10,87 €; **B** Energie +40 % statt Preisindex +12 % laut Gleitklausel → −5,56 €. Korrigiert **207,78 € (+9,4 %)**. **C** Streitpunkt: Laut Abfüllprotokollen lief die Hausmarke mit 4.200 Fl/h → 199,51 € (+5,0 %). Verhandlung mit BATNA „eigene Linie“; glaubwürdig ist sie nur mit Plan-BAB. Realistisches Ergebnis: +9 %.
6. **Make or Buy 2029 (kalkulatorisch, T€/Jahr):** Buy 260,6 (bei +9 %) bzw. 280,3 (bei +18 %); Make 258,2 mit Kessler bzw. 361,2 ohne. **Kritische Menge** nur Hausmarke: 1,79 Mio. Fl (bei +9 %) gegen 1,06 Mio. Plan. Kessler zahlt 0,16 €/Fl: unter Vollkosten (0,203), über den variablen Kosten (0,057) → Zusatzauftrag über Preisuntergrenze, aber Klumpenrisiko.
7. **Kapitalwert** (6 %, 10 Jahre, gegen Buy +9 %): Kessler 10 Jahre **+50,4 T€** (IZF 7,1 %) · 7 Jahre −132,6 · 5 Jahre −273,6 · 3 Jahre −432,1 · ohne Kessler −707,3 · Kessler 10 Jahre und Hausmarke +5 %/Jahr +349,6 T€. Gegen nicht verhandelte +18 % wäre schon Kessler 7 Jahre positiv (+12,3). Lehrsatz: Die gute Verhandlung entwertet die eigene Anlage, und ohne die Anlage gäbe es die gute Verhandlung nicht.
8. **Bank:** Mit 950 T€ Kredit und den Strukturwerten der Planbilanz 31.12.2027 als Näherung **[Annahme]**: EK-Quote 26,9 % (Covenant ≥ 25 %); ND/EBITDA 3,30 mit Kessler, aber **3,72 ohne Kessler → Covenant-Bruch**. Vogt verlangt Take-or-pay-Klausel oder Leasing.
9. **HB5/HB6:** Entscheidungsvorlage nach Rubrik und Beiratspräsentation; Hildegard fragt nach dem Szenario „Kessler springt ab“. Empfehlung im Expertenpfad: Buy zu +9 % mit Open-Book-Klausel und Kapazitätsgarantie; Make nur bei ≥ 10 Jahren Kessler-Vertrag mit Take-or-pay. Tobias entscheidet nach Vorlagenqualität und Vertrauen.
10. **Folgen 2029:** *Make*: monatliche Industrie-KLR. Juli 2029: Plan 95 h, Ist 78 h (Kessler nimmt 70 %), Istkosten 30,40 T€; Fixkosten 18,61 T€/Monat, 119,4 €/h variabel → Sollkosten 27,93, verrechnete Plankosten 24,59 → **Verbrauchsabweichung +2,47 T€** (Laugentemperatur), **Beschäftigungsabweichung +3,33 T€** (Leerkosten, D9). Dazu Bestandsbewertung Fertigware zu HK nach § 255 HGB. *Buy*: Quartalsweise Open-Book-Nachkalkulation mit dem Schatten-BAB des Spielers; Wiedervorlage, sobald die Hausmarke 1,5 Mio. Flaschen erreicht.

---

## 12. Technik und MVP-Schnitt

**Technik (aufbauend auf 04, mit 08):** Local-first-PWA mit Angular 22, frameworkfreie deterministische TS-Engine (Integer-Cent, doppelte Buchführung, SKR04 vereinfacht), Inhalte als YAML/Markdown mit Zod-Prüfung, ts-fsrs, Dexie, Cloudflare Pages. Für die Kampagne zusätzlich:
- **Mehrgesellschafts-Datenmodell ab Tag 1:** Gesellschaft, Kostenstelle, Innenleistung, Leergutkonto je Partner und Gebindeart, auch wenn der Prototyp nur Markt 1 zeigt (08).
- **Kampagnen-Engine:** Kapitel als Zustandsmaschine; Story-Ereignisse und Dialoge als YAML mit Bedingungen auf Flags, KPIs und Vertrauen; keine Code-Ausführung im Inhalt.
- **Common Random Numbers** (Zufall per Hash aus Seed, Tag, Objekt und Zweck) für das Kontrafaktum.
- **Golden Master:** Modell 08 ohne Kelterei plus Hausmarke; alle Zahlen in Lernkarten werden generiert, nie von Hand gepflegt (06).
- **`lernziele.yaml`** mit Abdeckungsprüfung im Build (Abschn. 7).

**MVP – kleinster Kern, der die Idee beweist:** „Vertical Slice Kapitel 1“: Januar bis März 2027 in Markt 1, Zahlen geskriptet aus dem Golden Master (keine Marktsimulation).

| Inhalt | PT |
|---|---|
| Lernprototyp nach 04 (Engine-Kern, Aufgaben-Framework, Lückentabelle, FSRS-Frühschicht, Speicher) | 20–25 |
| Kampagnen-Engine light: Kapitelzustand, 3 Figuren (Hildegard, Sabine, Tobias), Dialogbaum, Vertrauen, eine verzögerte Konsequenz (Szene 1 → April-Nachbelastung) | 6–9 |
| Inhalt für 3 Monatsabschlüsse statt 1, Leitfrage „50,5 vs. 15,9 T€“, 10–12 Vorlagen, 6 Lernkarten | 5–7 |
| Lernziel-Mapping, Abdeckungsbericht, Mehrgesellschafts-Datenmodell | 2–3 |
| **Summe** | **33–44 PT** (≈ 5–7 Monate bei 1,5 PT/Woche; mit KI-Unterstützung im Code ≈ 28–37 PT **[Vermutung]**) |

**Erfolgskriterien MVP:** 5 Testpersonen aus der Zielgruppe spielen über ≥ 10 Kalendertage; ≥ 3 kommen ohne Aufforderung zurück; Frühschicht-Trefferquote nach 7 Tagen ≥ 70 %; die Leitfrage wird von ≥ 4 korrekt beantwortet.

**Gesamtaufwand ehrlich:** Einzelmarkt-Version 1.0 160–280 PT (04) + GFGH mit Märkten 80–130 PT (08) + Lohnabfüllung/Make-or-Buy mit laufender Industrie-KLR 20–35 PT + Kampagnenerzählung (13 Figuren, ≈ 150–250 Szenen, Weichen) 25–45 PT = **≈ 285–490 PT**, im Hobbytempo **≈ 3,5–6,5 Jahre** **[Vermutung]**. Deshalb kapitelweise Veröffentlichung: Kapitel 1 ist allein spielbar und nützlich.

---

## 13. Risiken und Gegenmaßnahmen

| Risiko | Wirkung | Gegenmaßnahme |
|---|---|---|
| Umfang übersteigt Ein-Personen-Projekt | Abbruch vor Kapitel 3 | Kapitelweise Releases; Inhalt nach Kapitel 1 messen, dann planen (06 Karte 87) |
| Zahlenwelt unbelegt, fachliche Fehler | Vertrauensverlust bei Fachleuten | Golden Master mit Prüfskript, Spannen statt Punktwerte, Review durch GFGH-Controller |
| Verzweigungsexplosion der Geschichte | Inhalt verdoppelt sich je Weiche | 3 große Weichen, sonst Zustandsvariablen; Handlung läuft wieder zusammen |
| Pflicht frustriert | Abbruch nach Pausen | ein Gate pro Ebene, Delegationsoption, Rost-Anzeige diegetisch statt Strafe |
| Make-Zweig wird selten gewählt | wenig laufende Industrie-KLR | Plan-BAB und Plankosten sind in beiden Zweigen Pflicht; Open-Book-Nachkalkulation; optionales Übungsmandat „Linie läuft“ |
| B2B wirkt trocken | Motivationsabfall in Kapitel 2 | Figuren statt Tabellen, benannte Kunden, Fall des Monats |
| Buchhaltung dominiert | man lernt Buchhalter statt Controller | Belegarbeit ≤ 20 % der Monatszeit, ab Kapitel 3 an Lena delegierbar |
| Rechtsstand altert | Details falsch ab 2028 | Recht eingefroren und versioniert, Fortschreibung als fiktiv markiert |
| Alkohol, Marken, IHK-Bezug | Schul- und Rechtsprobleme | fiktive Marken, Disclaimer „keine Verbindung zu IHK/DIHK“, AfG-Anteil sichtbar |
| LLM-Bewertung unzuverlässig | falsches Feedback | Regelprüfer zuerst, LLM nur optional und nie als Gate |

---

## 14. Offene Designentscheidungen

| Nr. | Frage | Optionen | Empfehlung |
|---|---|---|---|
| E1 | Kampagnenlänge | 2 / 3 Spieljahre + Epilog / 4 | 3 + optionaler Epilog |
| E2 | Hausmarke | Limonade / Apfelschorle / Mineralwasser | Limonade (Make-or-Buy real möglich, Zuckersteuer-Fall) |
| E3 | Wer entscheidet? | Spieler / GF nach Regel (Vorlage ≥ 7/10 und Vertrauen ≥ neutral) / GF per Zufall | GF nach transparenter Regel |
| E4 | Make-or-Buy-Ausgang | echte Weiche / Make immer / Buy immer | echte Weiche, Plan-BAB in beiden Zweigen Pflicht |
| E5 | Zuckersteuer | festes Ereignis 1.7.2027 / Zufall 70 % / weglassen | fest in Jahr 1, Höhe ab Jahr 2 per Seed |
| E6 | Ereignisse ab Jahr 2 | fest geskriptet / Seeds | Story-Ereignisse fest, Wetter und Marktwerte per Seed |
| E7 | Spielmonate pro Kalendertag | unbegrenzt, nur 1 zählt / max. 2 / unbegrenzt zählt | unbegrenzt spielbar, 1 zählt |
| E8 | Rost-Konsequenz | Sperre mit Delegation / Warnung / keine | Sperre mit Delegation |
| E9 | Kapitel-Gates | „gelernt“ / „beherrscht“ / keine | „gelernt“ für Kapitel, „beherrscht“ für Verantwortung |
| E10 | Krise | Game Over / Krisenmodus / keine Folgen | Krisenmodus mit Bank-Workout |
| E11 | HB4 | nur Browser / nur Export / beides | beides, Werkstatt je Kapitel |
| E12 | HB6-Gesprächssimulation | Dialogbaum / zusätzlich LLM-Rollenspiel / Präsenz-Material | Dialogbaum, LLM optional ab 1.1 |
| E13 | Prüfungsmodus IHK-Format | ab Kapitel-Ende / nur am Schluss / nie | ab jedem Kapitel-Ende |
| E14 | Tonalität | trocken / humorvoll / gemischt | realistisch, Humor in Figuren |
| E15 | Skript-Zuordnung | LZ-IDs aus Modulen jetzt, Skript später / warten auf Skripte | jetzt starten, `skript_ref` später füllen |
| E16 | MVP | Vertical Slice Kapitel 1 / Lernprototyp ohne Story / MVP mit Simulation | Vertical Slice Kapitel 1 (33–44 PT) |
