# Änderungen am Kartenstapel (Ausgangsdeck → finale `cards.json`)

Stand 20.10.2026. In dieser Datei steht „alt“ für die IDs im Ausgangsdeck und „neu“ für die IDs in `cards.json`.

## Vorab, außerhalb des Kartenstapels: Hinweis zum Repo

Im Repo `marvinwiemers.de` (Remote `github.com/Mastermuffin92/marvinwiemers.de`) sind 3.021 Dateien versioniert. Davon liegen 2.884 unter `.vscode-insiders`, 89 unter `Desktop` und 32 unter `AppData`. Mindestens 5 Dateinamen deuten auf persönliche Windows-Daten hin, darunter `ActivitiesCache.db` (Aktivitätsverlauf), ein Zertifikatsspeicher (`.sst`) und `.gitconfig`. Geprüft habe ich das mit `git ls-files` **[sicher]**, aber nur die Dateinamen, nicht die Inhalte. Ob das Repo öffentlich ist, habe ich nicht geprüft.

Empfehlung an den Kunden:
1. Sichtbarkeit prüfen und das Repo bei Bedarf sofort auf privat stellen.
2. Die Dateien entfernen und die Historie bereinigen (z. B. mit `git filter-repo`).
3. Betroffene Zugänge vorsorglich prüfen.

Diesen Hinweis bitte direkt geben. Er gehört nicht in eine Karte.

## Ergebnis

- **90 Karten:** 29 kern (Nr. 1–29, davon K001/K002 schon beantwortet), 36 wichtig (Nr. 30–65), 25 kür (Nr. 66–90).
- **Bilanz:** 9 Karten gestrichen bzw. in andere aufgegangen (alt K011, K021, K024, K025, K038, K044, K054, K065, K092), 6 Karten neu.
- **Neue Karten:** Berufsumfeld (neu K006), Wer schreibt den Code (K008), Geldbudget (K009), Zugang zu Prüfern und Testern (K010), Ausbaustand (K011), Zuckersteuer (K050).
- **Prüfung:** Alle Abhängigkeiten zeigen auf frühere Karten. Es gibt keine Zyklen und keine Textverweise auf gelöschte Karten. Alle Längenregeln sind eingehalten (Wörter nach Leerzeichen gezählt, `src/validate.py`).

**ID-Zuordnung alt → neu:** K001→K001, K002→K002, K003→K003, K008→K004, K004→K005, NEU→K006, K005→K007, NEU→K008, NEU→K009, NEU→K010, NEU→K011, K006→K012, K010→K013, K012→K014, K026→K015, K009→K016, K007→K017, K027→K018, K014→K019, K015→K020, K013→K021, K074→K022, K076→K023, K028→K024, K064→K025, K020→K026, K029→K027, K022→K028, K023→K029, K063→K030, K093→K031, K043→K032, K046→K033, K045→K034, K039→K035, K067→K036, K041→K037, K033→K038, K017→K039, K018→K040, K019→K041, K066→K042, K037→K043, K036→K044, K035→K045, K034→K046, K047→K047, K048→K048, K049→K049, NEU→K050, K050→K051, K016→K052, K031→K053, K030→K054, K032→K055, K051→K056, K052→K057, K053→K058, K042→K059, K055→K060, K059→K061, K057→K062, K060→K063, K062→K064, K061→K065, K069→K066, K070→K067, K084→K068, K071→K069, K072→K070, K073→K071, K075→K072, K077→K073, K085→K074, K086→K075, K078→K076, K079→K077, K080→K078, K040→K079, K081→K080, K082→K081, K083→K082, K087→K083, K068→K084, K088→K085, K056→K086, K089→K087, K058→K088, K090→K089, K091→K090.

## Befunde Qualität (je 1 Zeile)

1. **alt K024 streichen:** übernommen. „Neues Repo“ ist Standard, der Sicherheitshinweis steht oben außerhalb des Decks, und neu K086 hängt nicht mehr von K024 ab.
2. **alt K054 Sync falsch:** übernommen. Die Formulierung lautet jetzt „Kopplungscode oder freiwilliges Konto [vermutung]“. Die Karte ist in neu K029 (Plattform) aufgegangen, die Pflichtkonto-Doppelung entfällt.
3. **alt K015 Wochenstunden falsch:** übernommen. Der Text nennt jetzt ≈ 1,5–2,5 h Spiel bzw. ≈ 3–4 h mit Werkstätten. Betroffen ist neu K020; die Sitzungslänge regelt nur noch neu K052.
4. **alt K035 „17–20 h“ falsch:** übernommen. Der Text nennt jetzt ≈ 2 h (Kapitel 1) bis ≈ 23 h (Kapitel 3), und die Hilfe-Regel steht vor dem Kapitelgate (neu K044 vor K045).
5. **alt K047 Widerspruch Pfand/Boni:** übernommen (Linie 2). Im Kontext steht jetzt: Methoden sind Prüfungsstoff, Branchendetails kaum. In neu K016 A ersetzt „Unternehmensbewertung“ das „Bonuscontrolling“. Im Lernziel-Katalog zählen M44/M48 nur mit ihrem Methodenteil als Pflicht.
6. **alt K045 Prämisse:** übernommen. A hat jetzt einen Pflichthinweis auf die Lehrbuchvariante, Sicherheit vermutung, der Kontext ist geändert, und eine Notizfrage an den Dozenten ist ergänzt (neu K034).
7. **alt K059 Erlöse:** übernommen. Die D-Folgen sind korrigiert, Kontext und alt K003 C ebenfalls auf „höchstens niedrig vierstellig“ gebracht (neu K061).
8. **alt K011 streichen:** übernommen. Die Größe steht im Kontext von K001, die Abhängigkeiten zeigen auf K001.
9. **KI viermal im Deck:** übernommen. Die KI-Optionen in alt K018, K019 und K041 sind gestrichen, dort steht nur noch der Verweis „siehe K059“. Neu K059 steht hinter den Karten, von denen sie abhängt.
10. **alt K042 Empfehlung:** übernommen. Empfehlung ist jetzt A (vorerst kein Einbau, KI-Chat direkt nutzen), Sicherheit vermutung.
11. **alt K064/K092 zusammenlegen:** übernommen. Neu K025 hat jetzt A selbst, B 5 Personen, C Längsschnitt und D Dozentenkorrektur plus Prüfungsergebnisse; „3–5“ ist zu „5“ korrigiert.
12. **alt K065 streichen:** übernommen. Der Standard „Führung über Lena, Inventurteams, Projektteam, Budgetrunde“ steht in den Kontexten von neu K013 und K041.
13. **alt K038 streichen:** übernommen. Der Countdown-Standard steht im Kontext von neu K005, die Abhängigkeiten zeigen auf neu K005.
14. **alt K044 streichen:** übernommen. Den Standard siehe unten.
15. **alt K025 streichen:** übernommen. Den Standard siehe unten.
16. **alt K007 C Doppelung:** übernommen. Zusätzlich ist A umformuliert („Skriptreihenfolge steuert alle Fälle“), weil „Skriptkapitel als Spielkapitel“ der Kapitelfolge aus K001 widersprochen hätte (neu K017).
17. **alt K031 B Strohmann:** übernommen, aber ersetzt statt nur gestrichen. Neue Option B lautet „Stundenbudget erst ab Kapitel 2“, und die Karte steht vor der Zeitdruck-Karte (neu K053 vor K054).
18. **alt K051 Epilog doppelt:** übernommen. Der Epilog steht nur noch in neu K074.
19. **alt K036 zwei Achsen:** übernommen. Die drei Lernstufen und ihre Schwellen sind Standard, die Karte fragt nur noch die Hilfe-Regel ab (A abgestuft, B streng; neu K044).
20. **alt K034 C Strohmann:** übernommen. Die Zählregel ist Standard, die Karte fragt nur noch „Deckel ja/nein“ (neu K046).
21. **alt K040 umschreiben:** übernommen. Teil- und Folgepunkte sind Standard, die Karte fragt nur noch „Note oder nur Punkte“, Priorität kür. Die Notizfrage steht jetzt in neu K032 B. Empfehlung A (Standardpfad) mit Sicherheit vermutung.
22. **alt K073 D:** übernommen. Die Anlagengröße ist im Kontext gesetzt (Gebrauchtlinie 950 T€) (neu K071).
23. **alt K049 D:** übernommen. Der Kontext nennt Limonade aus K002 als Standard. Die Zuckersteuer bekommt eine eigene kurze Karte (neu K050) statt einer Notiz, weil sie in der Kandidatenliste als kern (D03) geführt ist und eine echte Abwägung darstellt.
24. **alt K027 C andere Achse:** übernommen. C ist gestrichen. Der Kontext nennt jetzt eine Sicherheitsstufe und weist darauf hin, dass der Lehrgangsvertrag die Weitergabe an Dritte und an KI-Dienste einschränken kann (neu K018).
25. **alt K074 Priorität:** übernommen. Die Karte ist jetzt kern und steht vor der MVP-Karte. Die Abhängigkeit von alt K049 ist entfernt, weil die Hausmarke Limonade über K002 gesetzt ist (neu K022).
26. **alt K076 Priorität:** übernommen. Die Karte ist jetzt kern, der Fakt ist korrigiert (304/254 Tage gelten nur für 2027) (neu K023).
27. **alt K058/K086 Empfehlung:** übernommen. Beide empfehlen jetzt A, K058 ist kür (neu K088, K075).
28. **alt K056 Priorität:** übernommen. Die Karte ist jetzt kür, die B-Folge ist präzisiert, sie steht hinter der Namenskarte, und der Verweis auf die gelöschte alt K054 ist ersetzt (neu K086).
29. **alt K006 Sicherheit:** übernommen. Sicherheit ist jetzt vermutung, der Verweis auf K012 in der Begründung ist ersetzt (neu K012).
30. **alt K068 Registerrisiko:** übernommen. Das Risiko steht jetzt auch bei A (neu K084).
31. **alt K005 D andere Achse:** übernommen. Mitstreiter sind jetzt Option D in neu K008.
32. **NEU „Wer baut?“:** übernommen, zusammengeführt mit dem gleichen Vollständigkeitsbefund (neu K008, kern).
33. **Einheiten:** übernommen. PT ist in K001 und neu K007 definiert, „Arbeitstage“ und „Personentage“ sind durchgehend durch PT ersetzt, und neu K007 gibt die Wochenzeit in Stunden an.
34. **NEU Zugang zu Fachleuten/Testern:** übernommen (neu K010, kern, mehrfach). Die Notizfragen in neu K024 und K025 sind entfernt.
35. **NEU Berufsumfeld:** übernommen, zusammengeführt mit dem Vollständigkeitsbefund (neu K006, kern).
36. **NEU Geldbudget:** übernommen, aber als kern statt wichtig, damit neu K024 nicht von einer späteren Karte abhängt. Die Optionen folgen dem Vollständigkeitsvorschlag (neu K009).
37. **Vorwärtsabhängigkeiten:** übernommen. Alle sechs sind aufgelöst, und alt K057 hängt jetzt an alt K059, mit Satz zum geringen Risiko bei privater Nutzung (neu K062).
38. **Jargon:** übernommen. Ersetzt sind Fading-Stufe → Hilfestufe, Mastery → Lernstufe, Skill → Fertigkeit, Rubrik → Bewertungsraster, Debrief → Nachbesprechung und Open-Book → „mit Einblick in die Kosten des Abfüllers“. Modulnummern und Effektstärke sind gestrichen, außerdem „Gate“ → Sperre/Abschluss, „Signals“, „Repository“ und „Formel-Engine“.
39. **alt K078 „stärkster Hebel“:** übernommen. Die Formulierung ist auf die Metaanalyse korrigiert, „d ≈ 0,67“ ist gestrichen (neu K076).
40. **alt K077 Doppelung mit K014/K067:** übernommen. Die Werkzeuge sind gesetzt, die Karte fragt nur noch Zusatzbelohnungen ab. Empfehlung „Verantwortung in der Geschichte“, Sicherheit vermutung (neu K073).
41. **alt K019 Folienbaukasten fest:** übernommen. A sagt jetzt „Präsentationsübung, Werkzeug siehe K083“ (neu K041).

## Befunde Vollständigkeit (je 1 Zeile)

1. **NEU Ausbaustand:** übernommen (neu K011, kern). Darauf verweisen jetzt K026, K030, K031 und K056.
2. **NEU Wer programmiert:** übernommen und mit Qualität Nr. 32 zusammengeführt. Abweichung: Mitstreiter sind Option D dort, nicht in K005.
3. **alt K029 Industrie-Vorstudie:** übernommen (neu K027). Die vorgeschlagene Abhängigkeit von alt K046 habe ich nicht übernommen: Sie wäre eine Vorwärtsabhängigkeit einer Kernkarte, und die Vorstudie nutzt eigene Referenzzahlen, keine Transferfälle.
4. **alt K002 Zeitplanfolge:** übernommen (Kontext ergänzt, plus Sicherheitsstufe bei „industriegeprägt“).
5. **NEU Berufsumfeld:** übernommen. Die Optionen mischen beide Vorschläge (Industrie / Handel oder Dienstleistung / andere Rolle / kein Betrieb).
6. **alt K011 streichen:** übernommen.
7. **alt K021 streichen:** übernommen. Die Kapitelfolge steht in den Kontexten von K001 und neu K017, die Zeitplanfolge in K002 und neu K027.
8. **alt K029 → kern:** übernommen.
9. **alt K040 → kern:** verworfen. Teil- und Folgepunkte sind jetzt Standard (Qualität Nr. 21), die übrige Frage (Note oder Punkte) ändert den MVP nicht.
10. **alt K064 → kern:** übernommen. Die Karte steht aber **vor** der MVP-Karte (neu K025 vor K026), weil K026 von ihr abhängt. So wie vorgeschlagen wäre eine Vorwärtsabhängigkeit bzw. ein Zyklus entstanden.
11. **alt K092 zusammenlegen:** übernommen.
12. **alt K054 zusammenlegen:** übernommen.
13. **alt K043 neue Optionen (Rahmenplan):** übernommen, Empfehlung C (neu K032). Die Priorität bleibt wichtig, die Karte ist die erste Inhaltskarte im wichtig-Block statt direkt hinter K018, damit der Kernblock nicht über 29 Karten wächst.
14. **alt K044 streichen:** übernommen.
15. **NEU Geldbudget:** übernommen, aber kern statt wichtig (Abhängigkeit von neu K024). Empfehlung B statt C: Bei der empfohlenen Eigennutzung wäre C derselbe Widerspruch wie bei alt K058.
16. **alt K017 → wichtig:** übernommen.
17. **alt K018 → wichtig:** übernommen, plus Abhängigkeit vom Berufsumfeld. Der Hinweis „bei K004 C zuerst beantworten“ fehlt, weil die Karten ohnehin der Reihe nach beantwortet werden.
18. **alt K019 → wichtig:** übernommen (Hinweis wie bei Nr. 17 nicht übernommen).
19. **alt K024 → wichtig:** hinfällig, weil die Karte gestrichen ist (Qualität Nr. 1). Den Sicherheitshinweis habe ich übernommen.
20. **alt K025 → wichtig:** hinfällig, weil die Karte gestrichen ist (Qualität Nr. 15).
21. **alt K016 → wichtig:** übernommen. Die Sitzungslänge ist aus alt K015 A entfernt.
22. **alt K093 → wichtig:** übernommen (neu K031, direkt hinter K030).
23. **alt K056 → kür:** übernommen.
24. **Neue Reihenfolge:** übernommen, mit Abweichungen:
    - Budget und Zugang stehen im Kern.
    - alt K074 und K076 stehen im Kern.
    - K064 steht vor K020.
    - K043 ist die erste wichtig-Inhaltskarte.
    - Die Zuckersteuer-Karte steht hinter der Hausmarke.
25. **Einheit PT:** übernommen (siehe Qualität Nr. 33).

## Weitere eigene Änderungen

- **neu K081:** „11 Lkw“ ist zu „15 Fahrzeuge“ geändert (11 Lkw + 4 Transporter), einheitlich mit K021.
- **neu K005 B:** „Fallmaschine und Frühschicht“ heißt jetzt „Aufgabengenerator und tägliche Kurzwiederholung“, weil beide Begriffe erst später erklärt werden.
- **neu K028 A:** Patch-Versionsnummer und „Signals“ sind entfernt, der React-Titel nennt Vite nicht mehr.
- **neu K029:** Den Safari-Löschhinweis aus alt K054 habe ich in den Kontext übernommen, die Backup-Erinnerung nach 14 Tagen in A.

## Bewusst nicht als Karte aufgenommen (mit Standardannahme)

| Frage | Standardannahme |
|---|---|
| Größe der Gruppe (alt K011) | Durch K001 A gesetzt: Großhandel 17,6 Mio. €, drei Märkte 4,5 Mio. €, Konzern ≈ 22 Mio. € |
| Kapitelreihenfolge (alt K021) | Pilotmarkt Jan.–Apr. 2027 → Großhandel Mai 2027–Apr. 2028 → Gruppe mit Abfüllprojekt Mai 2028–Dez. 2029; der Lehrgangsmodus zieht Themen als Sonderauftrag vor |
| Repo für das Spiel (alt K024) | Neues, sauberes Repo mit Angular 22; das Website-Repo bleibt unberührt und wird separat bereinigt |
| Einstieg und Einstufung (alt K025) | Story-Einstieg. Nach 3 Min. kommen drei Einstufungsaufgaben oder „Ich kenne mich aus“ (Sprung auf Hilfestufe 3); die Einstufung dient zugleich als Vortest |
| Countdown zum Prüfungstag (alt K038) | Aktiv, sobald ein Termin eingetragen ist. Fertigkeiten unter 90 % prognostiziertem Behalten am Prüfungstag bekommen 21–3 Tage vorher eine Zusatzwiederholung; der Termin ist jederzeit änderbar oder löschbar |
| Lernziel-Katalog jetzt oder später (alt K044) | Jetzt vorläufig aus § 4 ContrPrV und den 56 Modulen bzw. aus dem Rahmenplan, falls geliefert (neu K032 C). Kommen die Skripte binnen weniger Wochen, wird zunächst nur der MVP-Stoff katalogisiert. IDs bleiben unveränderlich |
| Speicherung und Gerätewechsel (alt K054) | Lokal im Browser mit Persistenz-Anfrage; Export und Import per Datei/QR ab MVP, Backup-Erinnerung nach 14 Tagen; Geräteabgleich vor 1.0 optional (in neu K029) |
| Führung und Moderation HB6 (alt K065) | Lena ab Kapitel 2 (Delegation, Stichprobe, Feedback), drei Inventurteams, Projektteam Abfüllung, Budgetrunde als Moderationsübung, Konfliktgespräch |
| Wirksamkeitsmessung (alt K092) | In neu K025 aufgegangen |
| Zahl der Lernstufen und Schwellen | Gelernt, beherrscht, prüfungsfest mit den Schwellen aus neu K044, als Startwerte für den Playtest |
| Bewertungslogik | Punkte je Teilaufgabe nach Operator, Folgepunkte, Toleranzen: Geld ±1 € bzw. ±0,5 %, Quoten ±0,1 Prozentpunkte |
| Zählregel | Je Fertigkeit zählt ein Abruf pro Kalendertag |
| Werkzeuge als Belohnung | Gelerntes schaltet Werkzeuge frei, Vergessenes lässt sie beschlagen (über neu K019) |
| Lernziel-ID-Schema (E01) | Opake, unveränderliche IDs, n:m zu HB, Fertigkeiten und Skriptkapiteln; die Spielmechanik kennt nur Fertigkeiten |
| Wiederholungsplaner (G01/G02) | Echtzeit-Abstände mit FSRS, Zielbehalten 90 % |
| Monatsabschluss als Sperre (G05) | Pflichtvorgänge müssen mit ≥ 50 % der Punkte bearbeitet sein, sonst kommen sie mit neuen Zahlen zurück |
| Gutschrift auf Fertigkeiten (G10) | Jede Teilaufgabe schreibt den beteiligten Fertigkeiten getrennt gut |
| Eingabeform (H01) | Zahlen tippen statt ankreuzen [sicher als Lernbefund] |
| Musterlösungen (H03) | Keine handgepflegten Zahlen; Anzeigeregel und 50 Varianten je Vorlage als automatischer Test, Ablenker nie gleich der Lösung |
| Verordnungstext (I06) | Der Volltext der ContrPrV wird vor dem ersten Prüfungsmodus gelesen (Bestehensregeln, Hilfsmittel, Gewichtung). Das ist eine Aufgabe für uns, keine Kundenentscheidung |
| Pfand in der Bilanz (L01) | Bruttoausweis, saldiert nur als Vergleichskennzahl |
| IHK-Bezug in der Kommunikation (O05) | Nur beschreibend („orientiert an der ContrPrV“), Disclaimer „keine Verbindung zu IHK/DIHK“, kein „IHK“ im Namen |
| Großhandel im MVP (P02) | Zwei Vorgänge (Saldenbestätigung Brauerei, Eckkneipe) |
| Vorlagenkosten messen (N04) | Nach dem Kernbeweis mit 8 Vorlagen messen; Ziel ≤ 0,5 PT inklusive Review |
| Erste 20 Minuten (F08) | Drehbuch laut Konzept 5.6 |
| Abfüllanlage und Projektlage (D07, D10, D11) | Gebrauchtlinie 950 T€ mit 7 Kostenstellen; Projekt Mai–Nov. 2028 in Kapitel 3; Lebensmittelrecht als K.-o.-Kriterium der Vorlage |
| Leergut der Hausmarke (D06) | Eigene Flaschen und Kästen |
| Branchenkennzahlen (C07) | Spannen mit „Annahme“-Hinweis statt Punktwerten |
| Pfand-/Bonusmodule M44/M48 | Pflicht nur im Methodenteil (Abstimmung, Abgrenzung, Liquidität), Branchendetails als Ausblick |

**Kürzungsreserve:** Soll das Deck kürzer werden, kann der Standardpfad zuerst neu K085 (Ton), K066 (Spielfigur) und K086 (Hosting) beantworten.
