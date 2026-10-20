# 03 – Lernwissenschaft und Spieldesign für das Controlling-Lernspiel „Getränkemarkt“

Stand: 19.10.2026. Legende: **[sicher]** belastbar belegt, **[wahrscheinlich]** starke Schlussfolgerung oder Sekundärquelle, **[Vermutung]** gefüllte Lücke bzw. Designannahme. Effektstärken (d, g) nach Cohen-Konvention: 0,2 klein, 0,5 mittel, 0,8 groß. Alle Getränkemarkt-Zahlen beziehen sich auf den Referenzbetrieb „Durstlöscher GmbH“ aus Dokument 01 (2,4 Mio. € Nettoumsatz, Ø 200 T€/Monat, Rohertrag 25 %) und sind **Annahmen**.

---

## 0. Kernaussagen

1. Am besten belegt sind Abrufen statt Wiederlesen (Retrieval) und verteiltes Üben (Spacing). Beide gehören in den Kern-Loop. Ein Zusatzmodul reicht nicht. **[sicher]**
2. Spiele lernen nicht von selbst. Serious Games schlagen klassischen Unterricht nur knapp (d ≈ 0,29). Den Vorsprung erzeugen Mehrfach-Sessions, ergänzende Instruktion und Reflexion. Glasur erzeugt ihn nicht. **[sicher]**
3. Controlling-Wissen muss im Spiel **Macht** sein. Wer eine Methode beherrscht, sieht mehr: Effekt-Vorschauen, Dialogoptionen, Drilldowns. Das ist die Gegenstrategie zu „chocolate-covered broccoli“. **[wahrscheinlich]**
4. Verfall („Rost“) wird in **Echtzeit** berechnet und nicht in Spielzeit. Ein Spielmonat dauert 20 Minuten, das Vergessen dauert Tage. **[sicher]** (Gedächtnisbefund), Design daraus **[wahrscheinlich]**
5. Jede Simulation braucht eine eingebaute Nachbesprechung (Debriefing, d ≈ 0,67), ein Kontrafaktum per Replay mit gleichem Seed und eine Fehlerdiagnose mit konkreter Rückmeldung. **[sicher]** (Debriefing-Effekt)

---

## 1. Lernwissenschaft → Mechanik

### Übersicht

| Prinzip | Evidenzlage | Stufe | Kernmechanik im Spiel |
|---|---|---|---|
| Retrieval Practice | g ≈ 0,50 vs. Wiederlesen, mit Feedback ≈ 0,73 | sicher / wahrsch. | Jede Theorie endet mit Abrufaufgabe; Handbuch-Nutzung zählt nicht für Mastery |
| Spaced Repetition | Spacing-Effekt robust; FSRS in Anki seit 23.10 | sicher | Skill-Scheduler (FSRS-ähnlich) über echte Kalendertage, „Frühschicht“ |
| Interleaving | g = 0,42 (Mathe 0,34) | sicher | Gemischter Monatsabschluss; Aufgabenstellung verrät Methode nicht |
| Worked Examples + Fading | robust, Expertise-Reversal | sicher | 4-stufiges Ausblenden je Skill, adaptiv |
| Cognitive Load | robust (Split-Attention, Redundanz) | sicher | Regelwerk wächst schrittweise; Formeln inline |
| Desirable Difficulties | robust, aber nur wenn überwindbar | sicher | Rost-Checks, Variation, Hint-Leiter |
| Mastery Learning | ES ≈ 0,5; „2 Sigma“ nicht repliziert | wahrsch. | Freischaltung nur bei Mastery-Kriterium |
| Feedback | d = 0,48, stark heterogen | sicher | Sofort bei Routine, verzögert bei Strategie, immer diagnostisch |
| Productive Failure | Vorteil für Konzept/Transfer | wahrsch. | „Erst probieren“-Fälle bei Konzeptthemen |
| Elaboration/Selbsterklärung | moderater Nutzen | sicher | „Warum?“-Folgefrage, „Erklär’s dem Chef“ |
| Transfer | Nahtransfer gut, Ferntransfer selten | sicher | ≥ 3 Oberflächenkontexte je Konzept, Fallvergleiche |
| Kompetenzmodell | Taxonomien etabliert | sicher | Matrix Controlling-Prozess × Stufe |

### 1.1 Retrieval Practice / Testing-Effekt

- **Befund:** Rowland (2014) wertete 159 Effektstärken aus 61 Studien aus. Er fand g ≈ 0,50 für Testen gegenüber erneutem Lernen **[wahrscheinlich]** (Zahl aus Sekundärquelle). Mit Feedback lag der Effekt bei g ≈ 0,73, ohne Feedback bei 0,39 **[wahrscheinlich]**. Abruf in freier Form (Recall) wirkt stärker als Wiedererkennen (Recognition) **[sicher]** (Abstract). Dunlosky et al. (2013) stufen „Practice Testing“ als eine von zwei Techniken mit „high utility“ ein **[sicher]**.
- **Grenze:** Ohne Feedback und bei sehr niedriger Erfolgsquote schrumpft der Effekt **[wahrscheinlich]**.
- **Mechanik:**
  - Keine Theoriekarte endet mit „Weiter“, jede endet mit einer Abrufaufgabe.
  - Zahlen werden eingetippt. Ankreuzen ist die Ausnahme (Recall > Recognition).
  - Das Handbuch („Ordner des Steuerberaters“) ist jederzeit offen. Eine damit gelöste Aufgabe gilt aber als „mit Hilfe“ und zählt nicht für Mastery und nicht für den Rost-Reset.
  - Vor jedem Monatsabschluss liegt eine 3-Fragen-„Aufwärmrunde“ aus Vormonatsstoff.

### 1.2 Spaced Repetition (Leitner, SM-2, FSRS)

- **Befund:** Der Spacing-Effekt gehört zu den robustesten Befunden der Gedächtnisforschung (Cepeda et al. 2006, Dunlosky 2013: „high utility“) **[sicher]**. Den optimalen Abstand schätzt man auf ca. 10–20 % des gewünschten Behaltensintervalls. Bei längeren Intervallen sinkt der Anteil **[wahrscheinlich]** (Cepeda et al. 2008).
- **Algorithmen:**
  - *Leitner:* 5 Fächer mit festen Intervallen (z. B. 1–2–4–8–16 Tage). Falsch beantwortete Karten fallen zurück in Fach 1. Das ist trivial zu implementieren und für Spieler transparent **[sicher]**.
  - *SM-2* (SuperMemo/klassisches Anki): Intervalle 1 Tag, 6 Tage, dann jeweils Intervall × Ease-Faktor (Start 2,5) **[sicher]**.
  - *FSRS* basiert auf dem DSR-Modell (Difficulty, Stability, Retrievability). Stabilität ist die Zeit, bis die Abrufwahrscheinlichkeit von 100 % auf 90 % fällt. Die Parameter werden per Machine Learning an die Lernhistorie angepasst, und der Nutzer stellt eine Zielbehaltensquote ein. Seit Anki 23.10 ist FSRS optional verfügbar, Standard bleibt SM-2 **[sicher]**. Eine TypeScript-Implementierung (ts-fsrs) existiert, für ein Browsergame ist sie direkt nutzbar **[wahrscheinlich]**.
- **Problem für uns:** Karteikarten-Scheduler planen **Fakten**. Controlling besteht größtenteils aus **Prozeduren** (Rohertrag ermitteln, Abweichung zerlegen). Deshalb wird pro *Wissenskomponente* (Skill) geplant, etwa „Wareneinsatz über Bestandsveränderung“. Jede Wiederholung zieht eine neue, parametrisierte Aufgabe **[wahrscheinlich]**.
- **Mechanik (Vorschlag „Rost-Modell“):**
  - Jeder Skill *k* hat Stabilität *S_k* in Tagen und den Zeitpunkt *t_k* der letzten erfolgreichen, unassistierten Lösung.
  - Abrufwahrscheinlichkeit: *R_k = 0,9^(Δt/S_k)*. Die Definition folgt FSRS: Bei Δt = S ist R = 90 %. Die vereinfachte Exponentialform ist eine Designannahme.
  - *R ≥ 0,85*: blank. *0,70–0,85*: „Flugrost“, Skill erscheint in der Frühschicht. *< 0,70*: „eingerostet“. Der zugehörige Arbeitsschritt im Monatsabschluss ist dann gesperrt, bis ein Auffrischer gelöst ist.
  - Bei Erfolg gilt *S ← S · (1 + 2,5 · (1 − R))*. Abruf bei niedrigem R bringt also mehr, das entspricht der FSRS-Logik. Bei Fehler gilt *S ← max(1, 0,4 · S)*. Startwert *S = 1* Tag. Die Konstanten sind **[Vermutung]** und werden später per Playtest kalibriert.
  - **Echtzeit statt Spielzeit:** Δt wird in Kalendertagen gemessen. Wer 6 Spielmonate an einem Abend spielt, hat nicht „6 Monate wiederholt“. Ein Monatsabschluss am selben Tag zählt deshalb nur einmal pro Skill und Kalendertag als Wiederholung **[wahrscheinlich]**.
  - Wer mehrere Tage nicht spielt, sieht beim Wiedereinstieg einen Inspektionsrundgang: Der Markt zeigt rostige Stellen, Regale mit Staub, je eine pro eingerostetem Skill. Das ist diegetisch und ohne Schuldgefühl-Popup.

### 1.3 Interleaving

- **Befund:** Brunmair & Richter (2019) analysierten 59 Studien mit 238 Effektstärken. Der Mittelwert liegt bei g = 0,42, für Mathematik bei g = 0,34. Bei Wortmaterial war Blocken besser (g = −0,39). Der Effekt ist größer, wenn Kategorien einander ähnlich sind und die Unterscheidung schwerfällt **[sicher]** (Abstract).
- **Implikation:** Interleaving trainiert die Frage, *welche* Methode passt. Für Controlling ist das zentral: Marge oder Aufschlag? Rohertrag oder Deckungsbeitrag? Preis- oder Mengenabweichung? Prozent oder Prozentpunkte?
- **Mechanik:**
  - Ersterwerb geblockt, jeweils 3–4 Aufgaben eines Typs. Danach werden Aufgaben nur noch gemischt präsentiert.
  - Die Aufgabenstellung nennt die Methode nicht. Statt „Berechne die Handelsspanne“ heißt es: Marktleiterin: „Lohnt sich die 9,99-€-Aktion für Pils überhaupt?“
  - Ähnliche Paare werden gezielt nebeneinandergestellt (Contrast Pairs), etwa zwei Belege mit fast identischen Zahlen, aber verschiedener Logik (Skonto mit und ohne Pfand).

### 1.4 Worked-Example-Effekt und Fading

- **Befund:** Novizen lernen mit ausgearbeiteten Lösungsbeispielen mehr als mit Problemlösen (Sweller & Cooper 1985). Schrittweises Ausblenden der Lösungsschritte („backward fading“) ist dem abrupten Wechsel überlegen (Renkl & Atkinson 2003) **[sicher]**. Beim *Expertise-Reversal-Effekt* kehrt sich das für Fortgeschrittene um: Beispiele werden redundant und schaden dann sogar (Kalyuga et al. 2003) **[sicher]**.
- **Mechanik („Über die Schulter“-Stufen je Skill):**
  1. *Vorgemacht:* Steuerberater Brand löst vollständig und kommentiert jeden Schritt in ein bis zwei Sätzen. Der Spieler beantwortet eine Selbsterklärungsfrage („Warum zieht er den Endbestand ab?“).
  2. *Letzter Schritt fehlt:* Der Spieler ergänzt das Ergebnis.
  3. *Zwei Schritte fehlen:* Der Spieler ergänzt Zwischen- und Endergebnis.
  4. *Leeres Formular:* Der Spieler löst selbständig.
  - Der Wechsel ist adaptiv: Zwei korrekte Lösungen in Folge heben eine Stufe, ein Fehler senkt eine. Spieler mit Vorwissen können Stufe 1 per Einstufungsaufgabe überspringen (Expertise-Reversal).

### 1.5 Cognitive Load Theory

- **Befund:** Das Arbeitsgedächtnis ist eng begrenzt. Unterschieden wird zwischen *intrinsischer* Last (Elementinteraktivität des Stoffs) und *extrinsischer* Last (schlechte Darstellung). Belegte Gestaltungseffekte: Split-Attention, Redundanz, Modalität (Sweller; Mayer) **[sicher]**.
- **Implikation:** Ein Getränkemarkt-Beleg hat hohe Elementinteraktivität: Menge, Preis, Pfand, USt, Skonto und Bonus wirken zusammen.
- **Mechanik:**
  - **Regelwerk wächst** (siehe Papers, Please): Tag 1 nur Menge × Preis, ab Tag 3 Pfand, ab Tag 5 Skonto, ab Tag 8 Boni/WKZ, ab Monat 3 Abgrenzungen.
  - Formeln stehen direkt an den Zahlen und nicht in einem separaten Fenster (Split-Attention vermeiden).
  - Eine Tabelle zeigt nur die relevanten Zeilen, weitere klappen bei Bedarf auf.
  - **Zeitdruck erst nach Mastery.** Unter Zeitdruck wächst die Last, deshalb ist der „Stoßzeit-Modus“ eine Kür für gefestigte Skills **[wahrscheinlich]**.

### 1.6 Desirable Difficulties

- **Befund:** Spacing, Interleaving, Testen, Generieren und Variation senken die Leistung *während* des Übens und erhöhen das *langfristige* Behalten (Bjork 1994; Bjork & Bjork 2011) **[sicher]**. Lernende halten deshalb oft die schlechtere Strategie für die bessere (Kompetenzillusion) **[sicher]**.
- **Mechanik:**
  - Ein Meta-Onboarding in einer Szene: Karl Hagedorn sagt: „Wenn’s leichtfällt, lernst du nichts.“ Ein Diagramm zeigt die eigene Trefferquote neben der wachsenden Stabilität.
  - Schwierigkeiten müssen **überwindbar** bleiben. Die Hint-Leiter hat 3 Stufen: Hinweis auf das Konzept, dann der erste Schritt, dann das Worked Example. Jede Stufe kostet Spielzeit und senkt die Mastery-Wertung.

### 1.7 Mastery Learning (Bloom)

- **Befund:** Bloom (1968, 1984): Lernende rücken erst bei erreichtem Kriterium weiter, sonst folgen „Correctives“, also eine *andere* Erklärung. Kulik et al. (1990) finden im Mittel ES ≈ 0,5 **[wahrscheinlich]**. Blooms „2-Sigma“-Effekt (Tutoring plus Mastery) wurde nicht repliziert. In einer Übersicht über 96 Tutoring-Studien erreichte keine 2 Sigma **[wahrscheinlich]** (von Hippel, Sekundärquelle).
- **Mechanik:**
  - **Mastery-Kriterium je Skill:** 3 korrekte, unassistierte Lösungen mit verschiedenen Parametern, verteilt auf mindestens 2 Kalendertage, plus 1 Aufgabe in einem zweiten Format (z. B. Tabelle statt Einzelrechnung) **[Vermutung]**.
  - **Freischaltung neuer Verantwortung** nur bei Mastery der Voraussetzungen. Beispiel: Das Jahresbudget gibt Karl erst frei, wenn Rohertrag, Saisonindex und Personalkosten-Planung sitzen.
  - Correctives heißt: andere Darstellung statt Wiederholung desselben Textes. Nach dem zweiten Fehler kommt ein alternatives Worked Example, z. B. Rohertrag als Mengen-Bild mit Kästen statt Formel.

### 1.8 Feedback-Timing

- **Befund:** Wisniewski, Zierer & Hattie (2020) werteten 435 Studien mit N > 61.000 aus und fanden d = 0,48 bei hoher Heterogenität. Informationsreiches Feedback wirkt viel stärker als bloßes „richtig/falsch“ **[sicher]**. Hattie & Timperley (2007): Feedback auf Aufgaben-, Prozess- und Selbstregulationsebene wirkt, Lob der Person kaum **[sicher]**. Zum Timing: In Labor-MC-Studien schnitt verzögertes Feedback besser ab, in angewandten Settings meist sofortiges (Kulik & Kulik 1988) **[wahrscheinlich]**. Shute (2008) empfiehlt sofortiges Feedback für Novizen und Prozeduren, verzögertes für Fortgeschrittene und komplexe Aufgaben **[wahrscheinlich]**.
- **Mechanik (drei Feedback-Schichten):**
  1. **Sofort und diagnostisch** im Übungsmodus und bei Routineprozeduren. Die Rückmeldung nennt den erkannten Fehler (siehe 5.3), „falsch“ allein reicht nicht.
  2. **Verzögert und natürlich** bei Steuerungsentscheidungen. Die Folgen zeigen sich erst im Monatsreport, zum Beispiel ein Preisanstieg in der Mengenentwicklung. Danach folgt das Debriefing.
  3. **Spät und sozial** über Audits: Der Steuerberater findet im Quartal Fehler aus früheren Monatsabschlüssen. Das ist verzögertes Feedback mit Gewicht.

### 1.9 Fehlerkultur und Productive Failure

- **Befund:** Sinha & Kapur (2021) werteten 53 Studien mit 166 Vergleichen aus. Problemlösen *vor* der Instruktion verbessert konzeptuelles Wissen und Transfer, ohne prozedurales Wissen zu schwächen **[wahrscheinlich]**. Aus der Erinnerung stammen g ≈ 0,36 insgesamt und ≈ 0,58 bei hoher Umsetzungstreue **[Vermutung, nicht verifiziert]**. Voraussetzung ist eine anschließende Instruktion. Minimal geführtes Entdecken ohne Auflösung ist schwächer (Kirschner, Sweller & Clark 2006) **[sicher]**. Error-Management-Training ist fehlervermeidendem Training überlegen, vor allem beim Transfer (Keith & Frese 2008, d ≈ 0,44) **[wahrscheinlich]**. Beim *Hypercorrection-Effekt* werden Fehler, die mit hoher Sicherheit begangen wurden, besonders gut korrigiert (Butterfield & Metcalfe 2001) **[sicher]**.
- **Mechanik:**
  - **„Erst probieren“-Fälle** nur bei *Konzept*themen: Gemeinkostenverteilung, Preisuntergrenze, Investitionsbewertung. Der Spieler entwickelt einen eigenen Ansatz. Danach stellt die Auflösung seinen Weg neben die Standardmethode und benennt, was fehlt. Für Routineprozeduren wie Beleg- oder USt-Rechnung gibt es kein Productive Failure.
  - **Sicherheitsregler** vor jeder Abgabe (50/70/90 %). Die Kalibrierung geht ins Profil ein. Wer mit hoher Sicherheit falsch liegt, bekommt eine betonte Erklärung (Hypercorrection).
  - **Fallakte/Fehlerlogbuch:** Jeder Fehler wird als Fall gespeichert („Fall 2026-03-14: Skonto auf Pfand gezogen“) und taucht als Wiederholungsaufgabe wieder auf.
  - Konsequenzen sind im Übungsmodus folgenlos. Im Echtbetrieb sind sie spürbar, aber reparierbar: Rückfrage der Brauerei, Korrekturbuchung, Vertrauensdelle.

### 1.10 Elaboration und Selbsterklärung

- **Befund:** Dunlosky et al. (2013) stufen Elaborative Interrogation und Self-Explanation als „moderate utility“ ein **[sicher]**. Bisra et al. (2018) finden in einer Meta-Analyse zur Selbsterklärung g ≈ 0,55 **[wahrscheinlich]**.
- **Mechanik:**
  - **„Warum?“-Folgefrage** nach jeder richtigen Zahl, als Auswahl aus 3–4 Begründungen und damit automatisch bewertbar. Beispiel: „Warum gehört Pfand nicht in den Rohertrag?“ Richtig ist: Pfand ist Forderung bzw. Verbindlichkeit, kein Erlös.
  - **Vorhersage vor Aufdecken (Predict–Observe–Explain):** „Was passiert mit der RE-Quote, wenn der Aktionsanteil steigt?“ Erst danach rechnet der Spieler.
  - **„Erklär’s dem Chef“:** Der Spieler baut aus Satzbausteinen eine Laien-Erklärung für Karl Hagedorn. Fachjargon kostet Vertrauen, leere Phrasen ebenfalls.

### 1.11 Transfer (near/far)

- **Befund:** Die Taxonomie von Barnett & Ceci (2002) unterscheidet Distanz nach Wissensgebiet, Kontext, Zeit und Funktion **[sicher]**. Ferntransfer ist empirisch selten. Bei Hirnjogging und Schach zeigt er sich praktisch nicht (Sala & Gobet 2017) **[wahrscheinlich]**. Der Vergleich zweier Fälle mit gleicher Tiefenstruktur fördert Abstraktion und Übertragung (Analogical Encoding, Gentner et al. 2003) **[sicher]**.
- **Mechanik:**
  - Jedes Konzept erscheint in **mindestens drei Oberflächenkontexten**: Abholmarkt, Lieferservice, Festzelt-Ausschank, später Filiale 2.
  - **„Zwei Fälle, ein Prinzip“:** Der Spieler vergleicht die Kühlzellen-Investition mit dem Leasing eines Lieferwagens und benennt die Gemeinsamkeit (Kapitalwert, Kapitaldienst).
  - **Endspiel als Transferprüfung:** Der Spieler berät als „Freelance-Controller“ einen fremden Betrieb, z. B. Bäckerei oder Fahrradladen. Dort sind dieselben Methoden mit anderen Treibern gefragt (Verderb statt Pfand).

### 1.12 Kompetenzmodelle

- **Grundlagen:** Bloom-Taxonomie in der Revision von Anderson & Krathwohl (2001): Erinnern, Verstehen, Anwenden, Analysieren, Bewerten, Erschaffen × Fakten-, Konzept-, Prozedur- und metakognitives Wissen **[sicher]**. Stufenmodell nach Dreyfus (Novize bis Experte) **[sicher]**. IGC-Controlling-Prozessmodell 2.0 mit zehn Hauptprozessen, darunter Strategische Planung, Planung/Budgetierung/Forecast, Kosten-, Leistungs- und Ergebnisrechnung, Management Reporting, Projekt- und Investitionscontrolling, Risikocontrolling, Datenmanagement (neu in 2.0) und Business Partnering. Funktionscontrolling ist eine eigene Dimension **[wahrscheinlich]** (Sekundärquellen).
- **Vorschlag Spiel-Kompetenzmatrix:** Zeilen sind die Prozesse, gemappt auf die 43 Module aus Dokument 01. Spalten sind vier Spielstufen:

| Stufe | Name im Spiel | Bloom | Beispiel (Zeile „Ergebnisrechnung“) |
|---|---|---|---|
| I | **Lehrling** – kennen/verstehen | Erinnern/Verstehen | Rohertrag vs. DB unterscheiden |
| II | **Sachbearbeiter** – Routine | Anwenden | Monatsrohertrag fehlerfrei ermitteln |
| III | **Analyst** – diagnostizieren | Analysieren | RE-Rückgang in Mix-, Preis-, Schwundeffekt zerlegen |
| IV | **Business Partner** – beraten | Bewerten/Erschaffen | Sortimentsbereinigung begründen und durchsetzen |

  Jede Zelle enthält 3–8 Wissenskomponenten (Skills) mit Item-Templates. Das Profil zeigt die Stufe je Zeile und den Rost-Zustand.

---

## 2. Planspiel- und Simulationsdidaktik

### 2.1 Was die Klassiker tun

| Planspiel | Format | Lernmechanismus | Stärke | Schwäche |
|---|---|---|---|---|
| **TOPSIM** (Tata Interactive Systems) | Teams, meist 6 Perioden, Entscheidungsformular, Abgabe zu festen Terminen, Berichte als PDF, Auswertung im Plenum nach jeder Periode **[sicher]**; bis zu 90 min je Periode **[sicher]** (TH Köln) | Soll-Ist-Vergleich, Markt-/Konkurrenzanalyse, Entscheidung, Feedback durch Ergebnis | Interdependenzen, Konkurrenz, Diskussion im Team | Wenige Zyklen (≈ 6); Modell weitgehend Blackbox; Lernerfolg hängt am Spielleiter |
| **Celemi Apples & Oranges** | Brettspiel, 4–5 Personen je Team, 3 simulierte Jahre, 6–8 h; Teams erstellen am Jahresende GuV, Bilanz, KPIs **[wahrscheinlich]** | Haptischer Geldfluss: Münzen/Chips wandern sichtbar durch die Firma | Macht Cashflow und Bilanz „anfassbar“; für Nicht-Finanzleute | Einmal-Event, keine Wiederholung über Tage; moderationsabhängig |
| **Cesim** | Online, Runden, funktionsübergreifende Entscheidungen; Selbstbild „experiential learning“ **[wahrscheinlich]** | Silos überwinden, Wechselwirkungen | Skalierbar, Benchmarks zwischen Teams | Modellparameter intransparent |
| **Capsim** (Capstone) | Teams führen konkurrierende Firmen über Runden („Jahre“), Analystenbericht, automatisierte Debriefs **[wahrscheinlich]** | Deliberate Practice unter Konkurrenz | Viel Datenmaterial, Reporting-Kompetenz | Optimierung auf Spielmodell; Ranking ≠ Lernen |
| **Marketplace** | Quartalsentscheidungen, Teams, Gründung bis Wachstum **[Vermutung]** (Details nicht verifiziert) | Marktforschung → Strategie → Ergebnis | Starke Marketing-/Strategie-Verknüpfung | Wie oben |

### 2.2 Evidenz

- Sitzmann (2011) wertete 65 Studien mit N = 6.476 aus. Mit Simulationsspielen lagen Selbstwirksamkeit um 20 %, deklaratives Wissen um 11 %, prozedurales Wissen um 14 % und Behalten um 9 % höher. Simulationen *eingebettet in Instruktion* schlagen Simulation als alleinige Methode. Es gibt Hinweise auf Publikationsbias **[wahrscheinlich]** (Sekundärquellen).
- Wouters et al. (2013): Lernen d = 0,29, Behalten d = 0,36, Motivation nicht signifikant (d = 0,26). Größere Effekte zeigten sich mit ergänzender Instruktion, mehreren Sessions und Gruppenarbeit **[sicher]**.
- **Folgerung:** Ein Planspiel allein ist schwach. Stark wird es mit Wiederholung über Sessions, Instruktion an der richtigen Stelle und Reflexion.

### 2.3 Debriefing ist der Lernmotor

- Tannenbaum & Cerasoli (2013): 46 Stichproben, N = 2.136. Debriefings steigern die Leistung um ca. 25 % (d = 0,67), bei Teams wie bei Einzelpersonen und in simulierten wie realen Settings. Struktur und Moderation verstärken den Effekt **[sicher]**.
- Gängige Phasenmodelle (Lederman; Thiagarajan): Gefühl, Was ist passiert, Warum, Was lerne ich, Bezug zur Realität, Was wäre wenn, Was nehme ich mit **[wahrscheinlich]**.
- **Unser Problem:** Im Browsergame fehlt der Moderator. **Lösung „Nachbesprechung im Büro“** nach jedem Monat (3–5 min) und jedem Geschäftsjahr (10–15 min):
  1. *Fakten:* Drei Zahlen, die sich am stärksten verändert haben, mit Vorhersage: „Was glaubst du, warum?“
  2. *Treiberbaum:* Klickbarer Pfad Rohertrag → Menge × Preis × Mix → einzelne Warengruppe. Der Spieler markiert den Haupttreiber.
  3. *Kontrafaktum:* **Replay mit gleichem Seed**, genau eine Entscheidung geändert. Das kann nur eine Simulation, und es ist der stärkste didaktische Hebel gegenüber realer Praxis **[wahrscheinlich]**.
  4. *Expertenpfad („Geisterlauf“):* Ein Vergleich mit der Musterlösung zeigt, wo sie abweicht und warum. Eine bloße Highscore-Zahl reicht nicht.
  5. *Lehrsatz:* Der Spieler formuliert per Auswahl oder Satzbaustein eine Regel. Sie wandert in sein „Controller-Notizbuch“ und wird später abgefragt.
  - Optional für den Klassenraum-Einsatz: Ein Lehrer-Dashboard mit Debriefing-Leitfragen und anonymisierten Gruppenvergleichen **[Vermutung]**.

---

## 3. Game-Design-Muster und Übertragung

**Leitidee „Wissen ist Sicht“:** In Reigns, Disco Elysium und Obra Dinn bestimmt Information das Spiel. Bei uns schaltet jede gemeisterte Methode zusätzliche Information frei: Effektvorschau, Drilldown, Dialogoption. Lernen hat damit unmittelbaren Spielnutzen. Das ist *intrinsische Integration* nach Habgood & Ainsworth (2011): Inhalt in der Kernmechanik schlug in deren Studie die Variante mit abgetrennten Lernaufgaben bei Lernerfolg und freiwilliger Spielzeit **[wahrscheinlich]** (Ergebnis aus Erinnerung, nicht direkt verifiziert).

### 3.1 Reigns – Swipe-Entscheidungskarten mit Ressourcenbalken
- **Kern:** Binäre Entscheidungen per Wischen und vier Balken. Beide Extreme beenden das Spiel, Effekte sind nur als Punktgröße angedeutet, die Runs sind kurz **[sicher]**.
- **Übertragung:** Das Tagesgeschäft als Kartenstapel. „Brauerei-Außendienst bietet 400 € WKZ für 4 Wochen Zweitplatzierung Pils.“ „Marktleiterin will Aushilfe für Samstag.“ Balken: **Liquidität, Rohertrag, Kundenzufriedenheit, Teamstimmung, Vertrauen des Inhabers**. Zweiseitig wird es über **Lagerreichweite**: zu hoch bindet Kapital, zu niedrig führt zu Fehlbeständen.
- **Lernhaken:** Am Anfang sieht der Spieler wie in Reigns nur Punkte. Mit gemeisterter DB-Rechnung zeigt die Karte „≈ +310 € DB“, mit gemeisterter Liquiditätsplanung den Zahlungszeitpunkt. **Wissen = Sicht.**
- **Risiko:** Die Binärwahl ist zu grob. Deshalb gibt es eine dritte Option, „Prüfauftrag“: Sie kostet Zeit und öffnet eine Rechenaufgabe.

### 3.2 Papers, Please – Routineprüfung, wachsendes Regelwerk
- **Kern:** Dokumentenprüfung unter Zeitdruck, das Regelbuch wächst täglich. Jeder Fehler bringt eine „Citation“, dazu kommen moralische Zwickmühlen **[sicher]**.
- **Übertragung:** **Belegprüfung und Monatsabschluss.** Eingangsrechnungen, Lieferscheine, Leergut-Gutschriften, Kassenberichte. Der Spieler stempelt „Freigabe“, „Rückfrage“ oder „Korrektur“ und trägt den Differenzbetrag ein. Wachsende Regeln: Mengen-/Preisabgleich, Pflichtangaben nach § 14 UStG, Pfand, Skonto, Boni, E-Rechnung, Abgrenzung. Die „Citations“ kommen als Rückfragen vom Steuerberater.
- **Zwickmühle:** Karl bittet, eine private Rechnung „mitlaufen zu lassen“. Compliance wird so zur Entscheidung mit Vertrauenskosten.
- **Risiko:** Zeitdruck überlastet Novizen. Deshalb gibt es keinen Timer vor Mastery.

### 3.3 Tycoon- und Management-Sims
- **Game Dev Tycoon:** Schieberegler plus Review-Score als Feedback. Die verborgene Formel lernt man durch Experimentieren. Übertragung: **Sortiments- und Preisregler mit Monatsreport** als Feedback.
- **Two Point Hospital:** Viele parallele KPIs, Räume, Personal. Übertragung: **KPI-Cockpit** mit Personalproduktivität (Umsatz je Stunde), Flächenproduktivität und Leergut-Durchlaufzeit.
- **Supermarket Simulator/Together:** Ware einräumen, Preise setzen, Kunden reagieren auf den Preis. Übertragung: Eine erlebbare operative Schicht (Leergutannahme, Kasse) liefert die Daten, die man später controllt.
- **Cities: Skylines:** Budgetregler je Bereich mit laufendem Cashflow-Diagramm. Übertragung: **Kostenbudgets** für Personal, Energie, Werbung mit Echtzeit-Liquiditätskurve.
- **Gemeinsames Risiko:** Blackbox und Optimieren ohne Verstehen. **Gegenmittel: „Glass Box“.** Jede KPI ist klickbar und zeigt Formel, Eingangswerte und Herkunft der Daten.

### 3.4 Deduktionsspiele (Return of the Obra Dinn, Her Story)
- **Obra Dinn:** Die Schicksale von 60 Personen werden deduziert. Das Spiel bestätigt Lösungen erst in Dreiergruppen, das verhindert Brute Force **[sicher]**. **Her Story:** Videoclips in einer Datenbank, Zugriff nur per Stichwortsuche **[sicher]**.
- **Übertragung:** **Abweichungsanalyse als Fall.** Datenraum aus Kassenauswertung, WaWi, Kontenblättern, Inventurprotokoll und Lieferanten-Preislisten, mit Suche und Filter. Das schult die Datenabfrage im Her-Story-Stil. Die Fallakte hat Slots „Ursache – Betrag – Art (echte Abweichung/Messfehler) – Maßnahme“. Bestätigung kommt erst, wenn zwei Slots vollständig korrekt sind (Szene B).
- **Lernwert:** Es trainiert Stufe III (Analysieren), die in Planspielen meist untergeht.

### 3.5 Zachtronics (Opus Magnum, SpaceChem) – Optimierungspuzzles
- **Kern:** Ein offener Lösungsraum. Nach dem Lösen zeigen **Histogramme** (Kosten, Zyklen, Fläche), wo man im Feld aller Spieler steht. Rangplätze gibt es nicht **[sicher]**.
- **Übertragung:** Bestellmengenoptimierung (Bestellkosten vs. Lagerkosten, Mindestmengen der Brauerei), Personaleinsatzplanung gegen die Frequenzkurve, Tourenplanung für den Lieferservice, Regalflächen-Allokation nach DB/m². Die Histogramme zeigen „Kosten“, „Servicegrad“ und „Kapitalbindung“. Mehrere Optima (Pareto) sind erwünscht.
- **Risiko:** Leaderboards verleiten zum Exploit. Deshalb gehört eine Begründungspflicht für den gewählten Trade-off dazu.

### 3.6 Duolingo – Streaks, Ligen, Mini-Lektionen
- **Kern:** Lektionen von wenigen Minuten, Streak, Wochenligen, Herzen als Fehlerbudget **[sicher]** (Mechaniken). Die Lerneffekte der Streaks sind umstritten. Bekannte Risiken sind „Minimum für den Streak“ und Streak-Angst **[wahrscheinlich]**.
- **Übertragung:** **„Frühschicht“** mit 5 Minuten täglich und 5–8 Items aus rostigen Skills, priorisiert nach dem Rost-Modell. Der Streak zählt *Wiederholungen mit Erfolg* und nicht bloße Logins. Ein „Urlaubsschein“ (Streak Freeze) gilt 2 Tage pro Woche. Die Liga ist optional und nach Niveau gruppiert.

### 3.7 Visual Novel/Dialog (Disco Elysium light)
- **Kern:** Skills sind innere Stimmen und schalten Dialogoptionen frei. Checks sind sichtbar, Scheitern ist interessant **[sicher]**.
- **Übertragung:** **Business Partnering.** Monatsgespräch mit der Marktleiterin, Jahresgespräch mit der Bank, Konditionengespräch mit der Brauerei. Gemeisterte Skills erscheinen als Stimmen: *Zahlenblick* bei DB/Abweichung gemeistert („Die 9,99-€-Aktion liegt unter dem EK plus Pfandhandling.“), *Skepsis* bei Belegprüfung gemeistert, *Diplomatie* bei Kommunikationsmodul. Optionen ohne Mastery bleiben grau sichtbar. Das motiviert gezielt, weil der Spieler sieht, was er noch nicht kann.

### 3.8 Roguelite-Metaprogression (Hades, Slay the Spire)
- **Kern:** Kurze Runs, Scheitern ist eingeplant, zwischen den Runs bleibt dauerhafter Fortschritt **[sicher]**.
- **Übertragung:** **Ein Geschäftsjahr ist ein Run** mit neuem Seed. Variabel sind Standort (Stadtrand oder Dorf), Sommer (heiß oder verregnet), Schock (Energiepreis +30 %, Discounter eröffnet, Brauerei-Preiserhöhung, Pfandsystem-Änderung) und Startbilanz. Die Metaprogression besteht aus **Werkzeugen**: Methodenkarten, Report-Vorlagen, Notizbuch-Lehrsätze. Statusboni wie „+5 % Umsatz“ gibt es ausdrücklich nicht, sie würden Können durch Power Creep ersetzen.
- **Lernwert:** Spacing und Interleaving entstehen automatisch, weil Budget, Monatsabschlüsse und Jahresabschluss jedes Jahr wiederkehren, mit anderen Zahlen und Problemen.

### 3.9 Übersicht

| Muster | Controlling-Aufgabe | Lernfunktion | Hauptrisiko |
|---|---|---|---|
| Reigns | Tagesentscheidungen, Zielkonflikte | Konsequenzen, Wissen = Sicht | Zu grob |
| Papers, Please | Belegprüfung, Monatsabschluss | Routine, Regelaufbau | Überlast unter Zeitdruck |
| Tycoon | KPI-Steuerung, Budgets | Feedback-Loops | Blackbox |
| Obra Dinn/Her Story | Abweichungsanalyse, Datenabfrage | Analysieren, Hypothesen | Frust bei zu großem Raum |
| Zachtronics | Bestellung, Personal, Touren | Optimieren, Trade-offs | Exploit |
| Duolingo | Tägliche Wiederholung | Spacing | Extrinsischer Streak-Zwang |
| Disco Elysium | Gespräche, Business Partnering | Beraten, Kommunikation | Textmenge |
| Roguelite | Geschäftsjahre | Wiederholung, Varianz | Power Creep |

---

## 4. „Wiederholung ist Pflicht“ spielerisch machen

### 4.1 Drei Zeitskalen

| Takt | Dauer | Inhalt | Pflicht? |
|---|---|---|---|
| **Frühschicht** (Echtzeit-täglich) | 5 min | 5–8 rostige Items | Ja, sobald Skills eingerostet sind; sonst sperrt der betroffene Abschlussschritt |
| **Monat** (Spielzeit) | 15–25 min | Belegprüfung, Rohertrag, Report, Gespräch, 3–6 Entscheidungskarten, Nachbesprechung | Ja, Kern-Loop |
| **Quartal/Jahr** | 30–60 min | Forecast, Audit (Steuerberater, Bank), Budget, Jahresabschluss, Seed-Wechsel | Ja, Gate für neue Inhalte |

### 4.2 Parametrisierung (gegen Auswendiglernen)
- Jede Aufgabe ist ein **Template** mit Variablen, Wertebereichen und Plausibilitätsregeln, etwa RE-Quote 15–35 %, Endbestand ≥ 0, Pfand als ganzzahliges Vielfaches der Kastenmenge.
- **Zahlen aus der eigenen Simulation:** Die Rohertragsaufgabe im Juni nutzt *den* Juni-Wareneinsatz des eigenen Markts. Die Übung hat damit Spielrelevanz.
- **Distraktoren aus Fehlerfunktionen:** Für jedes Template laufen die Misconceptions als Funktion mit (5.3). Ein falscher MC-Wert ist also kein Zufall, sondern das Ergebnis z. B. von „Aufschlag statt Marge“.
- **Mehrere Oberflächen pro Template:** Einzelrechnung, Tabellenzeile, Fehlersuche („Finde den Fehler in Sabines Rechnung“) und Begründung.

### 4.3 Kompetenzverfall („Rost“)
Das Modell ist in 1.2 beschrieben. Sichtbar wird es im Markt (Staub, rostiges Regal) und im Kompetenzprofil (Ampel je Skill). Die Konsequenz ist **funktional statt bestrafend**: Ein eingerosteter Skill blockiert genau einen Arbeitsschritt. Zur Wahl stehen ein 2-Minuten-Auffrischer oder die Delegation an den Steuerberater, die Geld kostet (z. B. 120 € Honorar) und keine Kompetenz bringt **[Vermutung]**. Die Kostenvariante gibt Autonomie, ohne Lernen zu ersetzen.

### 4.4 Freischaltung nur bei Mastery
- Inhalte hängen an einem **Fähigkeitsgraphen**. Beispiel: „Liquiditätsplanung“ setzt „Zahlungsziele & Skonto“, „Pfandsaldo“ und „Saisonindex“ voraus.
- Neue Rollen und Orte sind sichtbar, aber gesperrt: Lieferservice, Filiale 2, Festzelt-Auftrag, Bankrating. Darauf steht ein „Was fehlt dir noch?“-Pfad.

### 4.5 Audits und Prüfungen
- **Quartalsprüfung des Steuerberaters:** Er zieht eine Stichprobe von 10 Belegen aus den *vom Spieler bearbeiteten* Vormonaten. Jeder damals übersehene Fehler wird jetzt zur Aufgabe. Das macht Konsequenz greifbar und wirkt als verzögertes Feedback.
- **Bankgespräch (jährlich):** Drei Kennzahlenfragen (Eigenkapitalquote, dynamischer Verschuldungsgrad, Kapitaldienstfähigkeit), dazu Fragen zur Erklärung von Abweichungen.
- **Brauerei-Jahresgespräch:** Bonusstaffel nachrechnen, Rückvergütungen prüfen.
- **Seltenes Ereignis „Kassen-Nachschau“** durch das Finanzamt (§ 146b AO) **[sicher]** (Rechtsinstitut): Kassenprozesse und Dokumentation werden geprüft.
- **Prüfungsfragen sind immer neu parametrisiert.** Bestehen ist Gate-Kriterium für den nächsten Geschäftsjahres-Seed.

### 4.6 Balance Pflicht/Freiheit
Pflichtwiederholung sollte ≤ 25–30 % der Spielzeit einer Session ausmachen. Mehr fühlt sich nach Schule an **[Vermutung]**. Steigt der Anteil darüber, verlangsamt der Scheduler die Einführung neuer Skills. Spieler empfinden das nicht als Strafe, eher als „ruhiger Monat“.

---

## 5. Assessment-Design

### 5.1 Aufgabentypen

| Typ | Getränkemarkt-Beispiel | Auto-Bewertung | Diagnosewert |
|---|---|---|---|
| Rechenaufgabe mit Toleranz | Wareneinsatz März ermitteln | Ja: ±0,5 % rel. bzw. ±1 € bzw. ±0,1 Pp. | Hoch, wenn Fehlerfunktionen hinterlegt |
| Mehrschritt mit Folgefehler | Rechnung → USt → Skonto → Zahlbetrag | Ja: jeder Schritt gegen eigenes Vorergebnis geprüft | Sehr hoch, Fehlerstelle lokalisierbar |
| MC mit Fehler-Distraktoren | RE-Quote: 26,0 / 35,2 / 37,8 / 23,3 % | Ja | Hoch, jeder Distraktor = Misconception |
| Zuordnung | Kostenart → fix/variabel; Beleg → Konto | Ja | Mittel |
| Tabelle ausfüllen | Liquiditätsplan 3 Monate, Budgetzeilen | Ja, zellweise mit Folgefehler | Hoch |
| Diagramm interpretieren | Saisonkurve, Wasserfall, Ampel | Ja (Auswahl, Markieren im Diagramm) | Mittel |
| Fehlersuche | „Finde den Fehler in Sabines Rechnung“ | Ja | Hoch, umgekehrte Perspektive |
| Entscheidung begründen | Kühlzelle ja/nein + 2 von 6 Gründen | Ja (Auswahl), teils Rubrik | Mittel bis hoch |
| Freitext-Kommentar | Abweichungskommentar für den Monatsreport | Satzbaustein-Builder automatisch; echter Freitext per LLM-Rubrik | Unsicher bei LLM **[Vermutung]** |
| Sicherheitsangabe | 50/70/90 % vor Abgabe | Kalibrierungsscore | Metakognition |

### 5.2 Toleranzen und Folgefehler
- **Toleranzen je Größenart:** Geldbeträge ±1 € oder ±0,5 % relativ, Quoten ±0,1 Prozentpunkte, Faktoren auf 3 Nachkommastellen. Rundungsregeln stehen sichtbar in der Aufgabe.
- **Folgefehler-Logik:** Ist Schritt 2 falsch, Schritt 3 aber mit dem falschen Wert korrekt gerechnet, gibt es Teilpunkte. Die Diagnose zeigt „Fehler nur in Schritt 2“.
- **Äquivalente Lösungswege** werden akzeptiert, z. B. ein Kapitalwert über Einzelabzinsung statt Rentenbarwertfaktor.

### 5.3 Fehlerdiagnose: Misconception-Katalog (Auszug)

| ID | Fehler | Erkennungsregel | Rückmeldung (Kern) |
|---|---|---|---|
| M1 | Aufschlag statt Spanne | Antwort ≈ RE / WE | „Du hast durch den Wareneinsatz geteilt, das ist der Aufschlag. Die Spanne bezieht sich auf den Umsatz.“ |
| M2 | Brutto statt netto | Antwort ≈ Soll × 1,19 bzw. auf Bruttoumsatz | „Die USt gehört dem Finanzamt und zählt nicht zum Umsatz.“ |
| M3 | Pfand als Umsatz/WE | Differenz = Pfandbetrag | „Pfand ist Forderung/Verbindlichkeit, kein Erlös.“ |
| M4 | Bestandsveränderung vorzeichenfalsch | WE = Zukauf + EB − AB | „Ein steigender Bestand heißt: Du hast weniger verkauft als eingekauft.“ |
| M5 | Skonto auf Pfand | Skonto = 2 % × Gesamtbrutto | „Laut Lieferbedingungen nur auf den Warenwert.“ (Spielregel) |
| M6 | Prozent vs. Prozentpunkte | Antwort = relative statt absoluter Differenz | „25,0 → 21,1 % sind −3,9 Prozentpunkte, aber −15,6 %.“ |
| M7 | Ungewichteter Quoten-Durchschnitt | Antwort = Mittel der Gruppenquoten | „Die Warengruppen haben verschiedene Umsätze, deshalb gewichten.“ |
| M8 | Gewinn = Liquidität | Zahlungszeitpunkte ignoriert | „Die Brauerei will am 10. Geld, egal wann du verkaufst.“ |
| M9 | Fixkosten in kurzfristiger Preisuntergrenze | PUG enthält Miete | „Die Miete fällt so oder so an.“ |
| M10 | Doppelzählung Mengen-/Preiseffekt | Summe der Effekte ≠ Gesamtabweichung | „Prüfe: Die Teilabweichungen müssen sich zur Gesamtabweichung addieren.“ |
| M11 | Abzinsung vergessen | Summe der Rückflüsse − I₀ | „1 € in 10 Jahren ist heute weniger wert.“ |
| M12 | Messfehler als echte Abweichung | Fehlbuchung als Ursache „Schwund“ | „Erst die Daten prüfen, dann die Ursachen.“ |

Jeder Fehler-Treffer wird gezählt. Wiederholt sich eine Misconception (≥ 2× in 7 Tagen), legt der Scheduler einen gezielten Contrast-Pair-Block ein.

### 5.4 Kompetenzprofil
- **Methodik:** *Evidence-Centered Design* (Mislevy) mit Kompetenzmodell, Evidenzmodell und Aufgabenmodell. Dazu *Stealth Assessment* (Shute): Auch Spielhandlungen gelten als Evidenz, etwa ob der Spieler vor einer Preisentscheidung den DB-Drilldown öffnet **[sicher]** (Konzepte).
- **Schätzer:** Pro Skill reicht ein einfaches Bayesian Knowledge Tracing oder Elo-Rating (Spieler gegen Item-Schwierigkeit). Die Item-Schwierigkeit wird aus den Daten aller Spieler nachkalibriert **[wahrscheinlich]**.
- **Anzeige:**
  - Netzdiagramm mit der Stufe je Controlling-Prozess,
  - Rost-Ampel je Skill,
  - Kalibrierung (Sicherheit vs. Trefferquote),
  - Top-3-Misconceptions,
  - Notizbuch-Lehrsätze.
  - Optional ein Export als PDF bzw. „Arbeitszeugnis“ für die Bewerbung **[Vermutung]**.

### 5.5 Freitext
Standard ist der **Satzbaustein-Builder**: Der Spieler wählt Ursache, Betrag, Wertung und Maßnahme aus. Das ist zuverlässig und automatisch bewertbar. Echter Freitext läuft optional mit LLM-Bewertung gegen eine Rubrik (Ursache genannt? quantifiziert? adressatengerecht? Maßnahme?). Er dient nur als Feedback und **nie als Gate**, weil Zuverlässigkeit und Kosten offen sind **[Vermutung]**.

---

## 6. Motivation

### 6.1 Self-Determination Theory
Ryan, Rigby & Przybylski (2006) zeigen: Erlebte Autonomie, Kompetenz und Eingebundenheit sagen Spielspaß und Weiterspielen vorher **[sicher]**.
- **Autonomie:** Reihenfolge der Aufgaben im Monat wählbar. Strategieprofil des Markts (Preisführer, Spezialitäten, Lieferservice). Wahl zwischen Auffrischen und Delegieren. Seed-Wahl im Roguelite-Modus.
- **Kompetenz:** Diagnostisches Feedback, sichtbarer Stabilitätszuwachs, neue Sicht durch Wissen, Freischaltung von Verantwortung.
- **Eingebundenheit:** Figuren mit Haltung und Gedächtnis; sie erinnern sich an frühere Empfehlungen. Optional Koop („Zwei Filialen, ein Konzern“) oder Klassenliga.

### 6.2 Belohnungen
- Erwartete, materielle Belohnungen für interessante Tätigkeiten untergraben die intrinsische Motivation, informatives positives Feedback stärkt sie (Deci, Koestner & Ryan 1999) **[sicher]**.
- Gamification wirkt klein bis mittel (Sailer & Homner 2020: kognitiv g = 0,49, motivational 0,36, Verhalten 0,25). Game-Fiction und soziale Interaktion verstärken die Verhaltenseffekte **[sicher]**.
- **Folgerung:** Belohnungen sind **diegetisch und informativ**: Karl überträgt mehr Verantwortung, die Bank senkt den Zinssatz, die Marktleiterin fragt von sich aus um Rat. Abzeichen nur für Mastery, nicht für Klicks. Keine Lootboxen und keine Punkte für bloßes Erscheinen.

### 6.3 Figuren (mit Lernfunktion)

| Figur | Rolle | Lernfunktion |
|---|---|---|
| **Karl Hagedorn** (61), Inhaber | Kaufmann mit Bauchgefühl, will in 5 Jahren die Nachfolge regeln | Laien-Adressat: Erklären, Entscheidungsvorlagen; Langzeitbogen bis Unternehmensbewertung/Nachfolge |
| **Sabine Kowalski**, Marktleiterin | Operativ stark, defensiv bei Abweichungen („Das Wetter!“) | Business Partnering, Abweichungsgespräch, Zielvereinbarung |
| **Dr. Matthias Brand**, Steuerberater | Mentor, BWA, Jahresabschluss, Audits | Worked Examples („über die Schulter“), Belegdisziplin, verzögertes Feedback |
| **Aylin Yilmaz**, Firmenkundenbetreuerin Bank | Kredit, Rating, Covenants | Liquidität, Kapitaldienst, Kennzahlen; Prüfungsgespräch |
| **Jens Otte**, Brauerei-Außendienst | Konditionen, WKZ, Boni, Listungen | Konditionencontrolling, Verhandlung, Interessenkonflikte |
| **Lena**, Azubi (ab Jahr 2) | Lernt vom Spieler | Lernen durch Lehren: Der Spieler erklärt, Lena macht typische Fehler, der Spieler korrigiert **[wahrscheinlich]** (Protégé-Effekt, Teachable Agents) |

### 6.4 Schwierigkeitskurve
- Ziel-Erfolgsquote je Item ca. 70–85 %. Die „85-%-Regel“ (Wilson et al. 2019) ist aus Lernalgorithmen abgeleitet, ihre Übertragbarkeit auf Menschen ist theoretisch **[wahrscheinlich]**. Die Steuerung läuft adaptiv über Elo.
- Die Makrokurve ist sägezahnförmig: Jedes Geschäftsjahr bringt einen neuen Schock und ein neues Regelset (Spitze), danach folgt Konsolidierung (Tal). Für Flow-Zustände halten Herausforderung und Können sich die Waage **[sicher]** (Konzept).

### 6.5 Session-Länge
- Kern-Session: 1 Spielmonat = 15–25 min. Frühschicht 5 min. Jahresabschluss 30–60 min, auf 2–3 Sitzungen teilbar (Speichern jederzeit).
- Mehrere kurze Sessions über Tage sind lernwirksamer als eine Marathon-Session (Spacing) **[sicher]**. Das Design belohnt sie über den Echtzeit-Rost und begrenzt deshalb, wie viele Monate pro Kalendertag als Wiederholung zählen.

---

## 7. Anti-Patterns und Gegenmittel

| Anti-Pattern | Symptom | Gegenmittel |
|---|---|---|
| **Chocolate-covered broccoli** (extrinsische Integration) | Spiel und Quiz wechseln sich ab, das Quiz ist der Preis fürs Spielen | Wissen = Sicht/Macht; Aufgaben sind die Arbeit des Controllers im Spiel |
| **Textwände** | Theorie-Seiten > 150 Wörter | Theoriekarte ≤ 90 Wörter + Worked Example; Just-in-time beim ersten Auftreten |
| **Simulation als Blackbox** | Spieler probiert Regler, ohne zu wissen warum | Glass Box: jede KPI klickbar (Formel, Werte, Quelle); Treiberbaum |
| **Optimieren ohne Verstehen** | Exploit (z. B. Preis immer max., Personal min.) | Begründungspflicht, wechselnde Seeds, Audit fragt „warum“, Modell mit Gegenkräften (Kundenabwanderung) |
| **Gaming the System** (Baker et al. 2004) | Hint-Spam, schnelles Raten | Hints kosten Mastery; Ratedetektion (Antwortzeit < 3 s bei Rechenaufgabe); MC selten; neue Zahlen bei Retry |
| **Überladung** | 12 KPIs ab Minute 1 | Wachsendes Regelwerk; Cockpit wächst mit Freischaltung |
| **Grind ohne Lerngewinn** | Gleiche Aufgaben, gleiche Zahlen | Parametrisierung, Formatwechsel, Interleaving |
| **Strafende Fehler** | Angst, Abbruch | Fehler als Fall; Übungsmodus ohne Folgen; reparierbare Konsequenzen |
| **Unrealistische Zahlen** | Fachleute verlieren Vertrauen | Referenzbetrieb mit Branchen-Benchmarks (Dok. 01); Quellenhinweise |
| **Ranglisten-Frust** | Schwächere steigen aus | Histogramme statt Ränge; Niveau-Ligen; persönliche Bestwerte |
| **Kein Debriefing** | Ergebnis gesehen, nichts gelernt | Pflicht-Nachbesprechung, Kontrafaktum, Lehrsatz |
| **Scope-Explosion** | 43 Module gleichzeitig in der Alpha | Vertical Slice: 1 Jahr, 8 Module, 3 Figuren |

---

## 8. Designprinzipien für unser Spiel (14)

1. **Die Arbeit ist das Spiel.** Jede Aufgabe ist eine echte Controller-Tätigkeit im Getränkemarkt, keine Quizpause.
2. **Wissen ist Sicht.** Gemeisterte Methoden enthüllen Effekte, Drilldowns und Dialogoptionen. Ohne Methode bleibt der Spieler im Nebel.
3. **Abrufen statt Nachlesen.** Jede Theorie endet mit Abruf, und nur unassistierte Lösungen zählen.
4. **Rost läuft in Echtzeit.** Der Scheduler plant Skills über Kalendertage, die Frühschicht ist Pflicht für eingerostete Skills.
5. **Nie dieselbe Zahl zweimal.** Alle Aufgaben sind parametrisiert, am liebsten mit den Zahlen des eigenen Markts.
6. **Gemischt üben, Methode nicht verraten.** Nach dem Ersterwerb läuft alles gemischt, die Aufgabenstellung kommt aus Sicht der Figuren.
7. **Vormachen, dann ausblenden.** Vier Fading-Stufen je Skill, adaptiv, mit Überspringen für Kundige.
8. **Regelwerk wächst.** Neue Komplexität kommt Element für Element, Zeitdruck erst nach Mastery.
9. **Fehler sind Fälle.** Jeder Fehler wird diagnostiziert, gespeichert und kommt als Wiederholung zurück. Wer sich sicher war und falsch lag, bekommt besondere Aufmerksamkeit.
10. **Mastery öffnet Türen.** Neue Verantwortung, Orte und Figuren gibt es nur bei nachgewiesener Beherrschung der Voraussetzungen.
11. **Glass Box statt Blackbox.** Jede Kennzahl ist bis zum Beleg zurückverfolgbar.
12. **Jede Runde endet mit Nachbesprechung.** Fakten, Treiber, Kontrafaktum per Replay, Lehrsatz.
13. **Belohnung ist Vertrauen.** Diegetische, informative Belohnungen; Abzeichen nur für Mastery.
14. **Kurz und oft.** Monat 15–25 min, Frühschicht 5 min, alles jederzeit speicherbar, Browser-first und offline-fähig.

---

## 9. Drei prototypische Spielszenen

### Szene A – „Der erste Monatsabschluss“ (März, ca. 20 min; Module M02, M07, M08)

**Ziel:** Belegprüfung (Papers-Please-Muster), Rohertrag mit Fading, erste Elaboration.

1. **Briefing (30 s):** Dr. Brand: „Bis zum 10. brauche ich die geprüften Belege und den Rohertrag März.“ Das Regelwerk hat an Tag 1 drei Regeln: Menge Lieferschein = Rechnung, Preis = Preisliste, rechnerische Richtigkeit.
2. **Beleg 1 – Vorgemacht (Worked Example):** Rechnung der Brauerei Nord.
   - 120 Kästen Pils × 11,20 € = 1.344,00 €
   - Pfand 120 × 3,10 € = 372,00 €
   - Netto 1.716,00 €, USt 19 % 326,04 €, Brutto 2.042,04 €
   - Der Lieferschein nennt 112 Kästen. Brand zeigt den Fehler: 8 Kästen × (11,20 + 3,10) = 114,40 € netto = 136,14 € brutto zu viel. Stempel „Rückfrage“.
   - Selbsterklärungsfrage: „Warum steht auf dem Pfand auch USt?“ Antwort: Das Pfand teilt umsatzsteuerlich das Schicksal der Hauptleistung **[wahrscheinlich]**.
3. **Beleg 2 – Spieler allein (Regel neu ab Tag 3: Skonto):** Mineralbrunnen.
   - 200 Kästen Wasser 12 × 0,7 l × 3,80 € = 760,00 €
   - Pfand 200 × (12 × 0,15 + 1,50) = 660,00 €
   - Netto 1.420,00 €, USt 269,80 €, Brutto 1.689,80 €
   - Die Aushilfe hat 2 % Skonto auf den Gesamtbetrag vorbereitet (33,80 €). Laut Lieferbedingungen (Spielannahme) gilt Skonto nur auf den Warenwert: 2 % × 760,00 × 1,19 = **18,09 €**.
   - Der Spieler muss „Korrektur“ stempeln und 15,71 € Differenz eintragen. Fehlerdiagnose bei Freigabe: M5.
4. **Rohertrag März – Fading-Stufe 2 (letzter Schritt fehlt):**
   - Anfangsbestand 150.000 €, Zukäufe Ware netto ohne Pfand 148.300 €, Endbestand 152.700 €
   - Wareneinsatz = 150.000 + 148.300 − 152.700 = **145.600 €** (vorgegeben)
   - Umsatz netto ohne Pfand 196.800 €. Der Spieler tippt: Rohertrag **51.200 €**, Quote **26,0 %**.
   - Bei falscher Eingabe diagnostiziert das Spiel: 35,2 % → M1 (Aufschlag); 37,8 % → M2 (Bruttoumsatz 234.192 €); 23,3 % → M4 (Bestandsveränderung vorzeichenfalsch: WE 151.000 €).
5. **Elaboration:** „Warum zählt das Pfand nicht in den Rohertrag?“ (Auswahl aus 4 Begründungen). Dann „Erklär’s Karl“ mit 3 Satzbausteinen.
6. **Gespräch (Mini):** Karl: „26 %, ist das gut?“ Benchmark-Karte: Plan 25,0 %, Vorjahresmonat 25,4 %. Option A „Super, über Plan!“ führt zu Vertrauen +, aber Brand hakt später nach. Option B „Über Plan. Ich prüfe aber, ob Sondereffekte drin sind“ führt zu Vertrauen + und schaltet in Szene B eine Spur frei.
7. **Nachbesprechung und Scheduling:**
   - Skill „Wareneinsatz über Bestand“ startet mit S = 1 Tag. Morgen fragt die Frühschicht eine neue Variante ab (Endbestand fehlt).
   - In 3 Tagen kommt dieselbe Logik als Tabellenzeile.
   - Im April-Abschluss folgt Fading-Stufe 3.

### Szene B – „Der Fall des verschwundenen Rohertrags“ (April, ca. 25 min; M08, M11, M15, M32, M43)

**Ziel:** Abweichungsanalyse als Deduktionsfall (Obra-Dinn/Her-Story-Muster), Messfehler vs. echte Abweichung, Business Partnering.

**Ausgangslage:**

| | Plan | Ist |
|---|---|---|
| Umsatz | 204.000 € | 209.000 € |
| RE-Quote | 25,0 % | 21,1 % |
| Rohertrag | 51.000 € | 44.128 € |

Karl: „Mehr Umsatz, weniger Geld?“

1. **Vorhersage (PF-light):** Der Spieler wählt vor jeder Datenansicht die zwei wahrscheinlichsten Ursachen aus 6 Karten: Wetter, Aktion, Einkaufspreis, Schwund, Personalkosten, Buchungsfehler. Die Wahl wird gespeichert und im Debriefing aufgedeckt.
2. **Erste Zerlegung (Stufe-III-Skill, Fading 2):**
   - Mengen-/Umsatzeffekt: +5.000 € × 25 % = **+1.250 €**
   - Margeneffekt: (21,11 % − 25,0 %) × 209.000 € = **−8.122 €**
   - Kontrolle: +1.250 − 8.122 = −6.872 € = Gesamtabweichung. Bei fehlender Summenprobe greift M10.
3. **Datenraum (Suche):** Der Spieler sucht per Stichwort in Kassenauswertung, WaWi, Kontenblatt Wareneinkauf, Inventurprotokoll, Preislisten und Wetterdaten.
   - **E1 Kassenauswertung:** Aktionsanteil 28 % statt Plan 20 %. Aktionsware-Spanne 5 %, Normalware 30 % (Plan: 0,2 × 5 + 0,8 × 30 = 25 %).
   - **E2 Preisliste Brauerei Nord:** EK +4 % seit 01.04., VK nicht angepasst. WE der betroffenen Sorten zu alten Preisen 31.350 €.
   - **E3 Inventurprotokoll:** Inventurdifferenz −1.880 €, davon Bruch dokumentiert 820 €, unerklärt 1.060 €.
   - **E4 Kontenblatt:** Am 18.04. wurden 808 € Pfandanteil einer Lieferung auf „Wareneinkauf“ gebucht statt auf das Pfandkonto.
   - **Falsche Spuren:** Wetter (Wasserumsatz −6 %, wirkt auf die Menge, kaum auf die Quote). Personalkosten +3.000 € (liegen unterhalb des Rohertrags und sind irrelevant).
4. **Fallakte füllen (4 Slots: Ursache, Betrag, Art, Maßnahme):**
   - Mix-Effekt: Ist-Mix zu Plan-Spannen = 0,28 × 5 + 0,72 × 30 = 23,0 %, also −2,0 Pp. × 209.000 = **−4.180 €** (echt; Maßnahme: Aktionssteuerung)
   - Einkaufspreis: 31.350 × 4 % = **−1.254 €** (echt; Maßnahme: VK anpassen bzw. nachverhandeln)
   - Schwund/Bruch: **−1.880 €** (echt; davon 1.060 € unerklärt → Ursachensuche)
   - Fehlbuchung: **−808 €** (**Messfehler**; Maßnahme: Umbuchung)
   - Summe: −8.122 € ✓. Das Spiel bestätigt, sobald zwei Slots vollständig korrekt sind, Toleranz ±5 %. Ohne Bestätigung darf der Spieler mit Sicherheitsangabe einreichen. Das Quartalsaudit prüft später nach.
5. **Korrektur:** Nach der Umbuchung beträgt der bereinigte Rohertrag 44.936 € (21,5 %). Lehrsatz-Kandidat: „Erst Datenqualität, dann Ursachen.“ (M12)
6. **Monatsgespräch mit Sabine (Dialog):** Sabine: „Das war das Wetter.“
   - Option „Ihre Aktion hat uns 4.180 € gekostet“ (Vorwurf) führt zu Teamstimmung −−, Sabine blockt.
   - Option *Zahlenblick* (nur mit gemeistertem DB-Skill): „Die Aktion hat Frequenz gebracht. Prüfen wir, ob die Zusatzbons den Mixverlust decken.“ Das öffnet eine Folgeaufgabe: Zusatzbons × Ø-Rohertrag je Bon vs. 4.180 €.
   - Option *Skepsis*: „Das Wetter erklärt die Menge, nicht die Quote.“ Sabine akzeptiert, Vertrauen +.
7. **Maßnahmen als Reigns-Karten:**
   - „VK Pils +0,40 €/Kasten?“ Mit gemeistertem Preis-Mengen-Skill zeigt die Karte die Effektvorschau „≈ +1.100 € RE/Monat bei −3 % Menge“ **[Vermutung]** (Modellannahme).
   - „Aktionsanteil auf 20 % deckeln?“
   - „Bruchquote als Zielgröße für Sabine?“
8. **Nachbesprechung:**
   - Vorhersage vs. Wahrheit (Kalibrierung).
   - Treiberbaum als Wasserfall: Plan 51.000 → Menge +1.250 → Mix −4.180 → EK −1.254 → Schwund −1.880 → Buchung −808 → Ist 44.128.
   - Kontrafaktum: Replay mit Aktionsanteil 20 %.
   - Die Skills „Mix-Effekt“ und „Prozent vs. Prozentpunkte“ (−3,9 Pp. = −15,6 %) gehen in den Scheduler.

### Szene C – „Kühlzelle und Bankgespräch“ (Juni, ca. 25 min; M23, M25, M43)

**Ziel:** Investitionsrechnung mit Productive Failure, Sensitivität, Liquidität ≠ Rentabilität, verzögerte Konsequenz durch Nachkalkulation.

1. **Karte von Karl:** „Die alte Kühlung ist durch. Neue Kühlzelle für 36.000 €? Ja / Nein / Prüfauftrag.“ Der Spieler wählt den Prüfauftrag, der eine Spielwoche kostet.
2. **Erst probieren:** Ohne Methode soll der Spieler einschätzen, ob sich das lohnt. Vorgaben: Stromersparnis 3.200 €/Jahr, Mehr-Rohertrag Kühlware 2.800 €/Jahr, Wartung −400 €/Jahr, Nutzungsdauer 10 Jahre. Typischer Erstansatz: Amortisation 36.000 / 5.600 = 6,4 Jahre, „lohnt sich“. Oder: 10 × 5.600 = 56.000 > 36.000. Die Auflösung zeigt, was fehlt: Zeitwert des Geldes und Finanzierung.
3. **Worked Example (Brand) → Spieler rechnet:**
   - Rentenbarwertfaktor (7 %, 10 J.) = (1 − 1,07⁻¹⁰) / 0,07 = **7,0236**
   - Kapitalwert = 5.600 × 7,0236 − 36.000 = **+3.332 €**
4. **Sensitivität (Tabelle ausfüllen):**
   - Kritischer jährlicher Überschuss = 36.000 / 7,0236 = **5.126 €**
   - Bei nur 2.000 € Stromersparnis: Überschuss 4.400 €, KW = **−5.096 €**
   - Erkenntnisfrage: „Woran hängt die Entscheidung?“ Antwort: an der Strompreis- bzw. Verbrauchsprognose. Das wird als Risiko im Register notiert (M37).
5. **Bankgespräch mit Frau Yilmaz (Dialog plus Rechnung):**
   - Kredit 30.000 €, 6,5 % (Annahme), Laufzeit 5 Jahre, Eigenanteil 6.000 €
   - Annuität = 30.000 × 0,065 / (1 − 1,065⁻⁵) = **7.219 €/Jahr**
   - Jahresüberschuss aus der Investition 5.600 €, also **Liquiditätslücke 1.619 €/Jahr** in den Jahren 1–5
   - Frau Yilmaz: „Rentabel ja, aber wie zahlen Sie das?“
   - Option *Kapitaldienst* (nur mit gemeistertem Liquiditätsskill): Laufzeit 8 Jahre, Annuität **4.927 €/Jahr**. Das ist gedeckt, mit Puffer 673 €/Jahr. Kosten: Zinsen gesamt 9.417 € statt 6.095 €, also +3.322 €.
   - Lehrsatz: „Positiver Kapitalwert heißt nicht finanzierbar.“
6. **Entscheidung (Reigns-Karte):** Investition ja, Laufzeit 5 oder 8 Jahre. Die Balken Liquidität und Vertrauen der Bank reagieren sichtbar.
7. **Verzögerte Konsequenz (Dezember, Audit „Investitionsnachrechnung“):**
   - Die tatsächliche Stromersparnis liegt bei nur 2.600 €. Der Spieler rechnet nach: Überschuss 5.000 €, KW = 5.000 × 7,0236 − 36.000 = **−882 €**.
   - Debriefing-Frage: „War die Entscheidung falsch?“ Antwort: Ex ante war sie vertretbar, ex post knapp negativ. Die Entscheidungsqualität ist vom Ergebnis zu trennen, und die Prognose sollte künftig mit Sensitivität vorgelegt werden.
8. **Scheduling:** Rentenbarwertfaktor und Annuität gehen in den Rost-Scheduler. Der Transfer kommt in der Frühschicht von Woche 3 als Lieferwagen-Leasing vs. Kauf („Zwei Fälle, ein Prinzip“).

---

## 10. Offene Designentscheidungen (Kandidaten für Entscheidungskarten)

1. Rost in Echtzeit oder in Spielzeit, und wie streng (Sperre vs. Warnung)?
2. Mastery-Kriterium: 3 Lösungen über 2 Tage oder strenger bzw. lockerer?
3. Single-Player only oder zusätzlich Klassen-/Koop-Modus mit Lehrer-Dashboard?
4. Echter Freitext mit LLM-Bewertung oder nur Satzbausteine (Kosten, Offline-Fähigkeit)?
5. Zeitdruck-Modus (Papers, Please) als Pflicht ab Mastery oder als Kür?
6. Roguelite-Seeds ab Jahr 2 oder durchgehende Kampagne mit festen Ereignissen?
7. Anteil Pflichtwiederholung je Session (Vorschlag ≤ 25–30 %)?
8. Streaks und Ligen ja/nein (Risiko extrinsischer Zwang)?
9. Tonalität der Figuren: realistisch-trocken oder humorvoll-überzeichnet?
10. Delegation an den Steuerberater als Ausweichoption bei Rost erlauben, gegen Geld?
11. Endspiel: Nachfolge bzw. Verkauf des Markts (Unternehmensbewertung) oder Transfermandat in fremder Branche?
12. Zielgruppe: Azubis/Studierende (IHK-nah) oder Quereinsteiger/Gründer? Das beeinflusst Einstufungstest und Tiefe.

---

## Quellen (abgerufen 19.10.2026, teils Sekundärquellen)

- Rowland (2014), Testing-Effekt: https://courseware.epfl.ch/assets/courseware/v1/fdde2f0aa590bf3b1324077a6bf1540c/asset-v1%3AEPFL%2BDEMO%2B2020%2Btype%40asset%2Bblock/Rowland2014-meta-analysis.pdf ; Zusammenfassung: https://studycardsai.com/blog/active-recall-statistics
- FSRS/Anki: https://docs.ankiweb.net/faqs/what-spaced-repetition-algorithm ; https://en.wikipedia.org/wiki/Anki_(software) ; https://borretti.me/article/implementing-fsrs-in-100-lines
- Brunmair & Richter (2019), Interleaving: https://www.psychologie.uni-wuerzburg.de/fileadmin/06020400/2019/Brunmair_Richter_in_press__2019_META-ANALYSIS_OF_INTERLEAVED_LEARNING.pdf
- Sinha & Kapur (2021), Productive Failure: https://www.weforum.org/stories/2021/09/students-who-productively-fail-learn-more/ ; https://www.timeshighereducation.com/campus/using-productive-failure-activate-deeper-learning
- Wouters et al. (2013), Serious Games: https://research-portal.uu.nl/en/publications/a-meta-analysis-of-the-cognitive-and-motivational-effects-of-seri/ ; https://karlkapp.com/?p=4333
- Sitzmann (2011), Simulation Games: https://karlkapp.com/?p=4333 ; https://l-ten.org/wp-content/uploads/2022/08/Games_doc.pdf
- Wisniewski, Zierer & Hattie (2020), Feedback: https://www.frontiersin.org/articles/10.3389/fpsyg.2019.03087/pdf
- Kulik & Kulik (1988), Feedback-Timing (über Smith & Kimball 2010): https://www.ou.edu/memorylab/pdfs/SmithKimball_2010_LearningFromFeedback_ms.pdf ; Hattie & Timperley (2007): https://www.uky.edu/~gmswan3/575/Hattie_Timperly_2007.pdf
- Tannenbaum & Cerasoli (2013), Debriefing: https://pubmed.ncbi.nlm.nih.gov/23516804/ ; https://cebma.org/assets/Uploads/Tannenbaum-Cerasoli.pdf
- Bloom 2-Sigma, Kritik: https://nintil.com/bloom-sigma/ ; https://justinmath.com/blooms-two-sigma-problem/ ; https://www.gwern.net/doc/psychology/1984-bloom.pdf
- Sailer & Homner (2020), Gamification: https://link.springer.com/article/10.1007/s10648-019-09498-w
- TOPSIM-Ablauf: https://fbw.h-da.de/fileadmin/Dokumente/BWL_Bachelor/Aktuelles_Semester/FBWB_PlanspielInfo_WiSe2425.pdf ; https://uol.de/accounting/studium-und-lehre/topsim ; https://lehrpfade.th-koeln.de/wp-content/uploads/2023/02/Linde-TopSim-Erfahrungsbericht-fuer-den-EZ-Simulationen-und-Lernspiele.pdf
- Celemi Apples & Oranges: https://www.kent.edu/node/822271 ; https://nexia.com.au/node/53
- Capsim/Cesim/Marketplace: https://absel-ojs-ttu.tdl.org/absel/article/view/3308/3241 ; https://accesson.kr/fir/v.1/1/31/38774 ; https://www.associationofmbas.com/about-us/our-partners-and-suppliers/cesim-business-simulations/
- IGC-Controlling-Prozessmodell 2.0: https://haufe.de/id/beitrag/das-igc-controlling-prozessmodell-20-HI2546922.html ; https://shop.lindeverlag.at/buch/grundlagen-der-finanziellen-unternehmensfuehrung-band-iv-20216/e/leseprobe/E100483.pdf
- Mindestlohn 2026/2027: https://www.etl.de/aktuelles/mindestlohn-steigt-2026-und-2027/
- Ohne Web-Verifikation, aus Fachliteratur bekannt: Dunlosky et al. 2013; Cepeda et al. 2006/2008; Sweller & Cooper 1985; Renkl & Atkinson 2003; Kalyuga et al. 2003; Bjork 1994; Kirschner/Sweller/Clark 2006; Keith & Frese 2008; Butterfield & Metcalfe 2001; Bisra et al. 2018; Barnett & Ceci 2002; Gentner et al. 2003; Sala & Gobet 2017; Anderson & Krathwohl 2001; Ryan/Rigby/Przybylski 2006; Deci/Koestner/Ryan 1999; Habgood & Ainsworth 2011; Baker et al. 2004; Wilson et al. 2019; Mislevy (ECD); Shute (Stealth Assessment, Feedback 2008).
