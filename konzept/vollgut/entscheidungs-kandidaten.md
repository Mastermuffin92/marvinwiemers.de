# VOLLGUT – Offene Designentscheidungen (vollständige Liste)

Stand 20.10.2026. Grundlage sind das finale Konzept (`konzept-final.md`), die drei Entwürfe, die beiden Gutachten und die Entscheidungslisten in 03 (Abschn. 10), 04 (9.3), 05 (8) und 06 (5). Dubletten sind zusammengeführt. Jeder Eintrag nennt Frage, Relevanz, 2–4 Optionen mit Folgen, eine Empfehlung mit Sicherheitsstufe (**[sicher]** / **[wahrscheinlich]** / **[Vermutung]**), die Priorität und die Abhängigkeiten.

**Priorität:**
- **kern** blockiert den MVP oder die Grundrichtung.
- **wichtig** ist vor Version 1.0 zu klären.
- **kür** ist Feinschliff.

Einträge mit einem Namen, der im Konzept als ⟨Entscheidung: Name⟩ vorkommt, tragen genau diesen Namen. Die Empfehlung entspricht immer dem Standardpfad des Konzepts.

**Umfang:** 143 Einträge, davon 44 kern, 85 wichtig, 14 kür. Bei höchstens 100 Entscheidungskarten zuerst die 44 kern-Fragen stellen, dann die 30 wichtig-Fragen der Gruppen D, E, G, I und J (zusammen 74 Karten); die übrigen 26 Karten nach Wahl aus den restlichen wichtig-Fragen. Die kür-Fragen kann der Standardpfad beantworten.

---

## A Zielgruppe, Anspruch, Positionierung

**A01 Grundrichtung** · kern · Abh.: –
- Frage: Welcher Spieltyp trägt das Produkt?
- Warum: Er bestimmt Kernschleife, Bauaufwand und Spielspaß; die Gutachten waren uneins (Routine 99, Prüfung 98, Kampagne 96 Punkte).
- Optionen: (a) Routine-first-Schreibtisch mit Fallmaschine und IHK-Format → Wiederholung ist die Arbeit selbst, mittlerer Aufwand; (b) Prüfungstrainer mit Spielrahmen → höchste Prüfungsnähe, wenig Spielspaß, Abbruchrisiko; (c) Story-Kampagne → stärkster Sog, Erzählaufwand skaliert schlecht für eine Person.
- Empfehlung: (a) mit Leitfragen und Szenen aus (c) **[wahrscheinlich]**.

**A02 Primäre Zielgruppe** · kern · Abh.: A03, I-Gruppe
- Frage: Für wen wird primär gebaut?
- Warum: Sie bestimmt Tiefe, Prüfungsmodus, Tonalität und Vertrieb.
- Optionen: (a) Lehrgangsteilnehmende „Geprüfte/r Controller/in“ → prüfungsnah, aber nur 80–115 Prüflinge pro Jahr; (b) Junior-Controller und Quereinsteiger im Handel → mehr Reichweite, weniger externe Motivation; (c) Azubis und Berufsschule → Schulversion, flacher, Alkoholfrage; (d) BWL-Studierende → große Gruppe, wenig Branchenbezug.
- Empfehlung: (a) primär, (b) sekundär **[wahrscheinlich]**.

**A03 Anspruch „alle Facetten“** · kern · Abh.: E06
- Frage: Sind alle 56 Module Pflicht?
- Warum: „Alle Facetten × Pflichtwiederholung“ bedeutet sonst ≥ 9 Monate tägliches Üben (06 #8).
- Optionen: (a) alle Module Pflicht → sehr lange Laufzeit, hohe Abbruchgefahr; (b) IHK-Kern Pflicht (Relevanz hoch und mittel), Rest als Ausblick → ≈ 6–9 Monate; (c) freie Wahl → keine Abdeckungsgarantie.
- Empfehlung: (b), das Zeugnis weist beide Teile aus **[wahrscheinlich]**.

**A04 Lernversprechen-Schwellen** · wichtig · Abh.: I05
- Frage: Ab welcher Leistung gilt ein Versprechen als erfüllt?
- Warum: Die Schwellen steuern Zeugnis, Kapitelgates und die Außenkommunikation.
- Optionen: (a) 67 Punkte („befriedigend“) je HB → Puffer zur Bestehensgrenze; (b) 50 Punkte → minimal; (c) adaptiv nach eigenem Ziel → schwer vergleichbar.
- Empfehlung: (a) als interne Schwelle, mit echten Prüfungsergebnissen kalibrieren **[Vermutung]**.

**A05 Vorwissen, Einstufung und Schnelleinstieg** · kern · Abh.: G-Gruppe
- Frage: Wie wird Vorwissen berücksichtigt?
- Warum: Expertise-Reversal-Effekt; Worked Examples schaden Fortgeschrittenen (03, 1.4).
- Optionen: (a) kurzer Einstufungstest, der zugleich Prätest ist, mit Sprung auf Fading-Stufe 3 → präziser Start, misst Lernzuwachs; (b) Start bei null → Langeweile für Kundige; (c) nur Selbstauskunft → ungenau.
- Empfehlung: (a), mit der Option „Ich kenne mich aus“ **[wahrscheinlich]**.

**A06 Abdeckungskarte nach ContrPrV sichtbar** · wichtig · Abh.: E01, O05
- Frage: Sieht der Spieler sein Profil je HB und Lernziel mit Skriptbezug?
- Warum: Prüflinge planen nach Handlungsbereichen und Skriptkapiteln.
- Optionen: (a) sichtbar mit Skript-Anker und Countdown-Prognose → Orientierung, Motivation; (b) nur intern → weniger Transparenz.
- Empfehlung: (a), rein beschreibend ohne IHK-Branding **[wahrscheinlich]**.

**A07 „Zeugnis“ und Export** · kür · Abh.: G08, J03
- Frage: Gibt es ein exportierbares Kompetenzzeugnis?
- Warum: Nutzen für Bewerbung und Dozentengespräch.
- Optionen: (a) PDF mit HB-Profil, Pflicht- und Ausblickteil → Motivation; (b) keins → weniger Aufwand.
- Empfehlung: (a) ab 1.0, ausdrücklich ohne IHK-Bezug **[Vermutung]**.

---

## B Rolle, Erzählung, Figuren

**B01 Spielerrolle** · kern · Abh.: A02
- Frage: Welche Rolle hat der Spieler?
- Warum: Die Controllerrolle statt der Chefrolle ist der zentrale Unterschied zu Planspielen (05, L3).
- Optionen: (a) Controller/in der Gruppe als Stabsstelle → realistisch (23,7 % des EBIT); (b) Controller mit Aufstieg zum kaufmännischen Leiter → mehr Macht, weniger Beratungsrolle; (c) wählbar Inhaber → Rollenbruch.
- Empfehlung: (a); „Aufstieg“ nur als Verantwortungszuwachs (Budget, Delegation) **[wahrscheinlich]**.

**B02 Entscheidungsregel GF** · kern · Abh.: B01, H13
- Frage: Wie entscheidet der Geschäftsführer über Vorlagen?
- Warum: Ein Zufallsveto nach Stunden Arbeit wirkt unfair (Gutachten 2).
- Optionen: (a) transparente Regel: Vorlage ≥ 7/10 und Vertrauen ≥ neutral → er folgt, sonst seiner bekannten Vorliebe → fair, lernwirksam; (b) Wahrscheinlichkeit aus Vertrauen und Vorlage → realistischer, aber frustrierend; (c) der Spieler entscheidet → Rollenbruch.
- Empfehlung: (a) **[wahrscheinlich]**.

**B03 Wertbeitrag-Zähler** · wichtig · Abh.: B01
- Frage: Muss die Controllerstelle ihren Nutzen in € zeigen?
- Warum: Kosten-Nutzen des Controllings ist selbst eine Lektion (06, Karte 9).
- Optionen: (a) sichtbarer Zähler gegen 75 T€ → Meta-Ziel, Motivation; (b) nur im Jahresdebrief → ruhiger; (c) nein.
- Empfehlung: (a) **[Vermutung]**.

**B04 Figurenbudget** · kern · Abh.: N01
- Frage: Wie viele Figuren mit Dialogbaum gibt es?
- Warum: 13 voll ausgearbeitete Figuren und 150–250 Szenen sprengen ein Ein-Personen-Projekt (Gutachten 1).
- Optionen: (a) 8 Gesprächs- und 6 Korrespondenzfiguren, ≈ 90 Szenen in 1.0 → beherrschbar; (b) 13 Gesprächsfiguren → +20–30 PT; (c) 5 Figuren → dünne Konflikte.
- Empfehlung: (a); im MVP 3 Figuren **[wahrscheinlich]**.

**B05 Firmen- und Figurennamen** · kür · Abh.: O02
- Frage: Wie heißen Firma und Familie?
- Warum: Verwechslungsgefahr mit realen Unternehmen, Wiedererkennung.
- Optionen: (a) Platzhalter `{NAME}` bis zum Release → flexibel; (b) jetzt fester fiktiver Familienname → mehr Identität, Registerprüfung nötig.
- Empfehlung: (b) nach DPMA- und Webprüfung, bis dahin (a) **[Vermutung]**.

**B06 Tonalität** · wichtig · Abh.: A02
- Frage: Welcher Ton herrscht vor?
- Warum: Glaubwürdigkeit bei Fachleuten gegen Spielspaß.
- Optionen: (a) realistisch-trocken → seriös, ermüdend; (b) humorvoll-überzeichnet → unterhaltsam, weniger glaubwürdig; (c) realistisch mit Humor in den Figuren.
- Empfehlung: (c) **[Vermutung]**.

**B07 Anzahl großer Weichen** · wichtig · Abh.: B04
- Frage: Wie viele Story-Verzweigungen gibt es?
- Warum: Jede Weiche verdoppelt einen Teil des Inhalts.
- Optionen: (a) 3 Weichen (Aktion und Listung, Gastro-Politik, Make or Buy), sonst Zustandsvariablen → Wirkung bei begrenztem Aufwand; (b) 5 und mehr → Explosion; (c) keine → wenig Autonomie.
- Empfehlung: (a) **[wahrscheinlich]**.

**B08 Krisenmodus** · wichtig · Abh.: K01
- Frage: Was passiert bei Covenant-Bruch oder Liquiditätskrise?
- Warum: Strafende Fehler führen zum Abbruch (03, Kap. 7); StaRUG ist Lernstoff.
- Optionen: (a) Krisenmodus mit 13-Wochen-Plan, Bank-Workout, StaRUG-Frühwarnung → lehrreich; (b) Game Over → harte Konsequenz, Abbruch; (c) keine Folgen → unrealistisch.
- Empfehlung: (a) **[wahrscheinlich]**.

**B09 Endspiel** · kür · Abh.: E07
- Frage: Wie endet die Kampagne?
- Warum: Ein Langbogen hält die Motivation, Transfer prüft das Gelernte.
- Optionen: (a) Epilog „Übernahmeangebot eines Konzern-GFGH“ mit Bewertung (M56) und Fachgespräch; (b) Transfermandat in fremder Branche; (c) beides.
- Empfehlung: (c); Transfer läuft ohnehin über die gesamte Kampagne **[Vermutung]**.

**B10 Ethik-Dilemmata** · kür · Abh.: B02
- Frage: Gibt es Integritätskonflikte?
- Warum: Controller-Ethik und Bilanzpolitik sind Teil von M38 und M51.
- Optionen: (a) ja, mit Vertrauenskosten (Bonus-Vorkauf zum Stichtag, private Rechnung) → realistisch; (b) nein.
- Empfehlung: (a) ab Kapitel 2 **[Vermutung]**.

---

## C Setting und Referenzbetrieb

**C01 Kelterei als spätere Option** · kür · Abh.: E07
- Frage: Kommt die verworfene Kelterei je zurück?
- Warum: Sie würde Kuppelprodukte und Saisonbestände liefern, der Kunde hat sie aber abgelehnt.
- Optionen: (a) nie; (b) nur als Transferfall (Kuppelkalkulation Trester) → Industrie-KLR ohne Bauaufwand; (c) als Erweiterung nach 1.0 → +25–40 PT.
- Empfehlung: (b) **[wahrscheinlich]**.

**C02 Simulationstiefe** · kern · Abh.: M01, P01
- Frage: Wie fein wird simuliert?
- Warum: Sie ist der größte Hebel auf den Bauaufwand.
- Optionen: (a) Monatsaggregate je Gesellschaft, Segment, Kundenklasse und Kostenstelle plus benannte Einheiten, nur Markt 1 tagesgenau → −30–50 PT; (b) Tagestick der ganzen Gruppe → realistischer, teuer; (c) nur Skriptdaten ohne Engine → keine Kontrafakten.
- Empfehlung: (a) **[wahrscheinlich]**.

**C03 Großhandel nach Kundenklassen oder Einzelkunden** · wichtig · Abh.: C02
- Frage: Wie detailliert sind die 1.250 Geschäftskunden?
- Warum: Kunden-DB braucht Einzelfälle, Performance und Inhalt brauchen Aggregate.
- Optionen: (a) Klassen (60 A, 200 B, 340 C) plus 12 benannte Kunden → handhabbar; (b) alle Einzelkunden → hoher Datenaufwand; (c) nur Klassen → keine Fallfiguren.
- Empfehlung: (a); die Excel-Werkstatt bekommt 600 synthetische Gastrokunden **[wahrscheinlich]**.

**C04 Startlage** · wichtig · Abh.: C05
- Frage: Wie gesund ist die Gruppe zum Start?
- Warum: Spannung durch Knappheit gegen Frustgefahr.
- Optionen: (a) knapp: EK-Quote 28,2 %, Kapitaldienst nicht aus dem Cashflow gedeckt → Lernanlässe; (b) gesund → wenig Druck; (c) Krise → Sanierungsspiel statt Controlleralltag.
- Empfehlung: (a) **[wahrscheinlich]**.

**C05 Covenant-Höhe** · wichtig · Abh.: D07, D08
- Frage: Welche Bankauflagen gelten?
- Warum: Sie entscheiden, ob die Abfüllanlage den Covenant bricht (ND/EBITDA 3,41 bzw. 3,85).
- Optionen: (a) EK-Quote ≥ 25 %, ND/EBITDA ≤ 3,5, KDF ≥ 1,2 (08) → knapper Headroom; (b) strenger (27 % / 3,0) → früher Krisenmodus; (c) lockerer → weniger Bankthema.
- Empfehlung: (a) **[Vermutung]**.

**C06 Spieljahr und Kalender** · kern · Abh.: L07
- Frage: In welchen Jahren spielt die Kampagne?
- Warum: Gesetzesstand, Feiertage und Saison müssen stimmen.
- Optionen: (a) 2027–2029 fest mit NRW-Kalender (304 Öffnungs- und 254 Liefertage) → testbar; (b) laufendes Kalenderjahr → Pflegeaufwand; (c) fiktiv ohne Jahreszahl → weniger Realismus.
- Empfehlung: (a) **[wahrscheinlich]**.

**C07 Benchmarks als Spannen** · wichtig · Abh.: N02
- Frage: Wie werden Branchenkennzahlen gezeigt?
- Warum: Es gibt keine öffentlichen GFGH-Betriebsvergleiche, Lernende verinnerlichen sonst Scheinwerte.
- Optionen: (a) Spannen mit „Annahme“-Hinweis → ehrlich; (b) Punktwerte → einfacher, irreführend.
- Empfehlung: (a) **[wahrscheinlich]**.

**C08 Konsolidierung im Spiel** · wichtig · Abh.: E07
- Frage: Wie tief geht die Konzernrechnung?
- Warum: M40 ist prüfungsrelevant, der Konzernabschluss ist hier nur freiwillig (§ 293 HGB).
- Optionen: (a) Bankrechnung light: Schulden-, Zwischengewinn- und EAV-Konsolidierung → realistisch; (b) Pflichtabschluss-Übung mit voller Kapitalkonsolidierung → prüfungsnäher, künstlich; (c) keine.
- Empfehlung: (a), Kapitalkonsolidierung als Transferfall **[wahrscheinlich]**.

**C09 Verrechnungspreis-Startregel** · wichtig · Abh.: D05
- Frage: Mit welcher Regel beliefert die KG die Märkte?
- Warum: Die Regel ist der Kern des Kapitel-3-Konflikts (Märkte 4,1 T€, Gruppe −165,8 T€).
- Optionen: (a) „Einstand + 3 %“, historisch und nie nachkalkuliert → maximaler Lernanlass; (b) Vollkosten-VP → weniger Konflikt; (c) frei wählbar ab Start.
- Empfehlung: (a) **[wahrscheinlich]**.

---

## D Hausmarke und Abfüllbogen

**D01 Hausmarke-Produkt** · kern · Abh.: D02, D03
- Frage: Welches Produkt füllt der Lohnabfüller ab?
- Warum: Das Produkt bestimmt den Industrie-KLR-Stoff und die Echtheit des Make-or-Buy-Falls.
- Optionen: (a) Limonade → Rezepturkalkulation, Zuckersteuer als Target-Costing-Fall; (b) Apfelschorle → Konzentrat-Preisrisiko, Brix-Rechnung, nah an der verworfenen Kelterei; (c) Mineralwasser → nur am Quellort abfüllbar, also kein echter Make-Fall.
- Empfehlung: (a), (b) als Seed-Variante **[wahrscheinlich]**.

**D02 Rezeptur Hausmarke** · wichtig · Abh.: D03
- Frage: Mit wie viel Zucker startet die Limonade?
- Warum: Die Rezeptur entscheidet, ob die Zuckersteuer den Fall dominiert.
- Optionen: (a) 7,5 g/100 ml (26 ct/l, ≈ 102 T€ im Jahr) → klarer Target-Costing-Anlass, lösbar über eine Rezeptur unter 5 g; (b) 9,5 g (32 ct/l, ≈ 174 T€) → Steuer erdrückt alles; (c) unter 5 g von Anfang an → kein Fall.
- Empfehlung: (a) **[wahrscheinlich]**.

**D03 Zuckersteuer-Konvention** · kern · Abh.: L07
- Frage: Wann und wie wirkt die Zuckersteuer im Spiel?
- Warum: Es gibt nur einen Kabinettsbeschluss (14.10.2026); Termin und Höhe sind politisch offen.
- Optionen: (a) Beschluss im Spiel März 2027, in Kraft 1.1.2028 → Zeit für Target Costing in Kapitel 2; (b) 1.7.2027 laut Entwurf → Druck in Kapitel 1/2; (c) Termin und Höhe nur per Seed → Varianz, weniger Planbarkeit; (d) weglassen → Fall fehlt.
- Empfehlung: (a) mit Seed-Varianten, als fiktive Fortschreibung markiert **[Vermutung]**.

**D04 Hausmarken-Parameter** · wichtig · Abh.: N02
- Frage: Welche Kannibalisierung, Fixkosten und Pool-Größe gelten?
- Warum: Sie entscheiden, ob die Hausmarke Geld verdient (Standardpfad: ΔEBT −8,5 T€ kurzfristig, −20,4 T€ langfristig).
- Optionen: (a) 70 % Kannibalisierung, 37 T€ Markenfixkosten, Pool 107,9 T€ → „Produkt-DB ≠ Entscheidungswert“; (b) 50 % Kannibalisierung → Hausmarke nahe null; (c) per Seed.
- Empfehlung: (a), Fachreview **[Vermutung]**.

**D05 Hausmarken-Listung Märkte** · wichtig · Abh.: C09, B07
- Frage: Wird die Hausmarke in den eigenen Märkten gelistet?
- Warum: Markt- und Gruppensicht widersprechen sich (H100: Markt-db 1,39 gegen 1,83 € der Fremdmarke).
- Optionen: (a) Weiche in Kapitel 1 → Verrechnungspreis-Thema früh erlebbar; (b) von Anfang an gelistet → weniger Konflikt; (c) nie → Thema fehlt.
- Empfehlung: (a) **[wahrscheinlich]**.

**D06 Leergut der Hausmarke** · kür · Abh.: L03
- Frage: Eigene Flaschen und Kästen oder Poolflaschen des Lohnabfüllers?
- Warum: Kapitalbindung und Pfandbilanzierung als Inverkehrbringer.
- Optionen: (a) eigene Flaschen und Kästen (Festwert 107,9 T€, Nettobindung 89,4 T€) → Pool-Zins, Festwert, BFH-Lernfall; (b) Poolflaschen, nur eigene Kästen → kleiner, einfacher.
- Empfehlung: (a) **[Vermutung]**.

**D07 Parameter Abfüllanlage** · wichtig · Abh.: C05, D08
- Frage: Welche Anlage steht zur Wahl?
- Warum: Ihre Größe bestimmt Fallgewicht, Plan-BAB und Covenant-Wirkung.
- Optionen: (a) generalüberholte Gebrauchtlinie, 950 T€, Gesamtanlageneffektivität 65 %, 7 Kostenstellen → reicher Fall; (b) Neuanlage ≈ 2 Mio. € → nie wirtschaftlich; (c) Kleinanlage 260 T€ → trivialer BAB (Gutachten 2).
- Empfehlung: (a) **[wahrscheinlich]**.

**D08 Drittauftrag-Konditionen** · wichtig · Abh.: D07, D09
- Frage: Was bietet der Drittkunde Kessler?
- Warum: Die Vertragslaufzeit entscheidet den Kapitalwert (Break-even ≈ 9,1 Jahre).
- Optionen: (a) 1,0 Mio. Fl, 0,16 €/Fl, 3 Jahre → Make ehrlich unattraktiv, Lehrsatz zur Laufzeit; (b) 10 Jahre Take-or-pay → Make positiv (+50,4 T€); (c) per Seed.
- Empfehlung: (a) im Standardpfad, (b)/(c) als Seeds **[wahrscheinlich]**.

**D09 Ausgang Make-or-Buy** · kern · Abh.: B02, D08
- Frage: Wie fällt die Kaufentscheidung?
- Warum: Laufende Industrie-KLR gibt es nur bei Kauf, die Spielerautonomie verlangt eine echte Weiche.
- Optionen: (a) offene Weiche nach GF-Regel, Plan-BAB in beiden Zweigen Pflicht → Autonomie mit Abdeckungsgarantie; (b) Kauf fest → Industrie-KLR garantiert, Entscheidung wertlos; (c) Buy fest → Industrie-KLR nur als Schatten.
- Empfehlung: (a) **[wahrscheinlich]**.

**D10 Zeitpunkt des Abfüllbogens** · wichtig · Abh.: E05
- Frage: Eigenes Kapitel oder Projekt in Kapitel 3?
- Warum: Parallele Kapitel verkomplizieren die Zustandsmaschine (Gutachten 1).
- Optionen: (a) Projektstrang in Kapitel 3, Mai bis November 2028 → eine Kapitellogik; (b) Kapitel 4 parallel zu Kapitel 3 → mehr Bauaufwand; (c) erst nach Kapitel 3 → Industrie-KLR kommt spät.
- Empfehlung: (a) **[wahrscheinlich]**.

**D11 Lebensmittelrecht im Make-Fall** · wichtig · Abh.: D07
- Frage: Wie tief gehen Hygiene, Rückverfolgbarkeit und Haftung ein?
- Warum: Eigene Abfüllung macht die Gruppe zum Lebensmittelhersteller; in zwei Entwürfen fehlte das.
- Optionen: (a) K.-o.-Kriterien in der Vorlage plus Kosten in H3/F3 und Rückruf-Erwartungsschaden → vollständig; (b) nur qualitativ → unvollständig; (c) weglassen.
- Empfehlung: (a) **[wahrscheinlich]**.

---

## E Lernziele und Skript-Anbindung

**E01 Lernziel-ID-Schema** · kern · Abh.: E02, M01
- Frage: Wie sind Lernziele identifiziert und verknüpft?
- Warum: Die Skripte müssen sich 1:1 umhängen lassen, ohne das Design zu ändern.
- Optionen: (a) opake, unveränderliche IDs, n:m zu HB, Skills und Skriptkapiteln, Spielmechanik kennt nur Skills → robust bei Neuschnitt; (b) sprechende IDs mit Modulnummer und Einzelfeld `skript_ref` → bricht beim Neuschnitt (Gutachten 1); (c) Vorlagen referenzieren Lernziele direkt → Umverdrahtung nötig.
- Empfehlung: (a) **[wahrscheinlich]**.

**E02 Lernziel-Katalog jetzt oder später** · kern · Abh.: E01, O07
- Frage: Wann entsteht der Lernziel-Katalog?
- Warum: Ohne Katalog keine Abdeckungsprüfung; die Skripte kommen später.
- Optionen: (a) jetzt vorläufig aus ContrPrV § 4 und M01–M56 (≈ 150 Lernziele), beim Skriptimport abgleichen → kein Blocker; (b) auf die Skripte warten → blockiert Inhalt und MVP.
- Empfehlung: (a) **[wahrscheinlich]**.

**E03 Skript-Lesepfad** · wichtig · Abh.: O07
- Frage: Wo liegt die Theorietiefe für Verfahrensvergleiche?
- Warum: Theoriekarten mit ≤ 90 Wörtern tragen keine Vergleiche wie starre gegen flexible Plankostenrechnung.
- Optionen: (a) Verweis aufs Skriptkapitel plus Abrufaufgaben → nutzt die Skripte; (b) eigene Dossiers (≤ 600 Wörter) → Aufwand, unabhängig; (c) Dossiers bis zur Lieferung, dann Verweis.
- Empfehlung: (c) **[wahrscheinlich]**.

**E04 Lehrgangsmodus** · wichtig · Abh.: E01, G-Gruppe
- Frage: Richtet sich das Spiel nach dem Lehrgangsfahrplan?
- Warum: Kapitel nach Setting widersprechen sonst der Reihenfolge des Lehrgangs (Gutachten 1).
- Optionen: (a) `skript_map` mit Termin erhöht die Priorität und zieht Sonderaufträge vor → synchron; (b) Kapitel strikt nach Setting → Kollision mit dem Lehrgang; (c) freie Themenwahl → keine Struktur.
- Empfehlung: (a) **[wahrscheinlich]**.

**E05 Kapitelzuschnitt** · kern · Abh.: E04
- Frage: Wonach sind die Kapitel geschnitten?
- Warum: Der Zuschnitt bestimmt Erzählung und Lernreihenfolge.
- Optionen: (a) nach Setting (Markt → Großhandel → Gruppe) mit Lehrgangsmodus → Story plus Synchronität; (b) nach HB → prüfungslogisch, erzählerisch schwach; (c) frei → keine Kampagne.
- Empfehlung: (a) **[wahrscheinlich]**.

**E06 Pflichtkanon-Umfang** · kern · Abh.: A03
- Frage: Welche Lernziele sind Pflicht für Gates und Zeugnis?
- Warum: Der Umfang bestimmt Übezeit und Abbruchrisiko.
- Optionen: (a) nur IHK-Relevanz hoch → schneller, Lücken; (b) hoch und mittel (≈ 110 Lernziele, ≈ 190 Skills, ≈ 1.700 Abrufe) → realistisch; (c) alle → ≥ 9 Monate.
- Empfehlung: (b) **[wahrscheinlich]**.

**E07 Transferanteil** · wichtig · Abh.: C01
- Frage: Wie viele Fälle spielen in fremden Branchen?
- Warum: HB1 ist industriegeprägt; sonst gibt es Nahtransfer ohne Ferntransfer (06 #6).
- Optionen: (a) 0 % → Getränke-Tunnelblick; (b) 10–15 % in HB1, 5–10 % in HB3 als „Mandat eines Verbundkollegen“ → Kuppel-, Divisions- und Normalkosten-Fälle abgedeckt; (c) 25 % → Setting verwässert.
- Empfehlung: (b) **[wahrscheinlich]**.

**E08 Abdeckungsregel je Lernziel** · wichtig · Abh.: N03
- Frage: Was muss es zu jedem Lernziel mindestens geben?
- Warum: Ohne Regel entstehen Lücken, die erst in der Prüfung auffallen.
- Optionen: (a) ≥ 1 Theorie, ≥ 3 Oberflächen aus ≥ 2 Vorlagen, ≥ 1 Routine- oder Fallkontext, ≥ 1 Prüfungsformat-Item, per CI geprüft → vollständig; (b) lockerer → billiger, lückenhaft.
- Empfehlung: (a) **[wahrscheinlich]**.

**E09 Verbale Pflichtitems** · wichtig · Abh.: H05
- Frage: Muss jedes erklärende Lernziel Kurzfreitext üben?
- Warum: Die Klausuren verlangen „nennen, erläutern, beurteilen“; Argumentkarten trainieren nur Wiedererkennen.
- Optionen: (a) Pflicht ≥ 1 Kurzfreitext je Lernziel mit Operator erläutern/beurteilen → prüfungsnah; (b) optional → Lücke.
- Empfehlung: (a) **[wahrscheinlich]**.

**E10 Skript-Abweichungen bei Definitionen** · wichtig · Abh.: E02
- Frage: Wer gewinnt bei abweichenden Definitionen (z. B. Zielkostenindex Nutzen/Kosten gegen Kosten/Nutzen)?
- Warum: Prüflinge werden nach Lehrgangsdefinitionen bewertet.
- Optionen: (a) Skript gewinnt, das Spiel passt Solver und Texte an → konsistent mit Lehrgang; (b) Lehrbuchstandard → Konflikt; (c) beide Varianten zeigen → Verwirrung.
- Empfehlung: (a), Varianten als Parameter je Solver **[wahrscheinlich]**.

---

## F Spielschleifen, Zeit, Tempo

**F01 Kampagnenlänge** · wichtig · Abh.: A03
- Frage: Wie viele Spielmonate dauert die Kampagne?
- Warum: Sie bestimmt die Zahl der Budget- und Abschlusszyklen.
- Optionen: (a) 24 → nur ein eigener Jahresabschluss; (b) 36 (drei Budgets, zwei eigene Abschlüsse) → genug Wiederholung; (c) 48 → Ermüdung.
- Empfehlung: (b) mit optionalem Epilog **[wahrscheinlich]**.

**F02 Stundenbudget** · kern · Abh.: F03, J07
- Frage: Sind Controllerstunden eine knappe Ressource?
- Warum: Ohne Timer fehlt dem Schreibtisch die Spannung; zugleich trainiert das Budget Selbstorganisation (HB6).
- Optionen: (a) 160 h je Spielmonat, Routinen und Prüfaufträge kosten Stunden, Mastery spart Stunden → Spannung ohne Hektik; (b) Echtzeit-Timer → Überlast für Novizen; (c) keine Ressource → beliebig.
- Empfehlung: (a), per Playtest kalibrieren **[Vermutung]**.

**F03 Routine-Kompression** · kern · Abh.: G08
- Frage: Werden alle Routinen jeden Monat voll gespielt?
- Warum: 20 Routinen × 36 Monate sprengen Sessionzeit und Geduld (Gutachten 2).
- Optionen: (a) 3–5 Fokusvorgänge, ausgewählt nach fälligen Skills; Beherrschtes als 1-Klick-Check oder delegiert → kurz und gezielt; (b) alles voll → monoton; (c) nur Fokusvorgänge, Rest automatisch → Kontrollverlust.
- Empfehlung: (a) **[wahrscheinlich]**.

**F04 Sessionlänge** · wichtig · Abh.: F03
- Frage: Wie lang ist eine typische Sitzung?
- Warum: Viele kurze Sessions sind lernwirksamer als Marathons.
- Optionen: (a) 25–35 Min. → feierabendtauglich; (b) 15–20 Min. → schultauglich, wenig Tiefe; (c) 45+ Min. → Abbruchgefahr.
- Empfehlung: (a); Kapitel 1 mit einer Session je Monat, ab Kapitel 2 mit zwei **[Vermutung]**.

**F05 Prüfauftrag-Option** · wichtig · Abh.: F02
- Frage: Haben Entscheidungskarten eine dritte Option „Prüfauftrag“?
- Warum: Binäre Karten sind zu grob (03, 3.1).
- Optionen: (a) ja, sie kostet Stunden und öffnet eine Analyse → Controllerverhalten belohnt; (b) nur Ja/Nein → schneller, flacher.
- Empfehlung: (a) **[wahrscheinlich]**.

**F06 Zeitdruck-Modus** · kür · Abh.: G08
- Frage: Gibt es Zeitdruck im Schreibtisch?
- Warum: Unter Zeitdruck steigt die kognitive Last, er ist aber prüfungsnah.
- Optionen: (a) Kür nach Mastery → Herausforderung für Fortgeschrittene; (b) Pflicht im Prüfungsjahr → prüfungsnah, stressig; (c) nie.
- Empfehlung: (a); Pflicht nur in Probeklausuren **[wahrscheinlich]**.

**F07 Freies Spiel nach der Kampagne** · kür · Abh.: K05
- Frage: Was kommt nach 2029?
- Warum: Weiterüben bis zum Prüfungstermin.
- Optionen: (a) Prüfungsjahre mit Seeds aus allen Kapiteln → Wiederholung mit Varianz; (b) Ende → Bruch vor der Prüfung.
- Empfehlung: (a) **[wahrscheinlich]**.

**F08 FTUE-Drehbuch** · kern · Abh.: A05
- Frage: Wie sehen die ersten 20 Minuten aus?
- Warum: Ein Einstufungstest als Einstieg tötet den Spielspaß (Gutachten 2).
- Optionen: (a) Leitfrage → Worked Example → zweiter Vorgang → Werkzeug-Leihgabe → Haken für morgen → Sog und Struktur; (b) Einstufungstest zuerst → messbar, zäh; (c) Tutorial-Text → Textwand.
- Empfehlung: (a) **[wahrscheinlich]**.

**F09 Anteil Belegarbeit** · wichtig · Abh.: J07
- Frage: Wie viel Spielzeit geht in Belegprüfung?
- Warum: Sonst übt man Buchhalter statt Controller (06 #13).
- Optionen: (a) ≤ 20 % der Monatszeit, ab Kapitel 2 an Lena delegierbar → Fokus Controlling; (b) Spieler macht alles → Buchhaltungsspiel; (c) Buchhaltung macht alles → IKS-Themen fehlen.
- Empfehlung: (a) **[wahrscheinlich]**.

**F10 Leitfragen je Kapitel** · wichtig · Abh.: B04
- Frage: Bekommt jedes Kapitel eine Leitfrage einer Figur?
- Warum: Ein Mystery-Haken trägt Routinen erzählerisch (Gutachten 2).
- Optionen: (a) ja, z. B. „Früher 50 T€, jetzt 15,9“ → Ziel und Sog; (b) neutrale Kapitelziele → sachlich, schwächer.
- Empfehlung: (a) **[wahrscheinlich]**.

---

## G Wiederholung, Mastery, Gates

**G01 Echtzeit-Spacing** · kern · Abh.: G02
- Frage: Wird Vergessen in Kalendertagen oder Spielzeit gemessen?
- Warum: Spacing wirkt nur über echte Zeit (06 W10).
- Optionen: (a) Kalendertage → echtes Spacing, Binge-Wand; (b) Spielzeit → keine echte Wiederholung.
- Empfehlung: (a) **[sicher als Lernbefund]**.

**G02 Scheduler und Zielretention** · kern · Abh.: G11
- Frage: Welcher Algorithmus plant Wiederholungen?
- Warum: Er bestimmt Last und Behalten.
- Optionen: (a) ts-fsrs (FSRS v6), Zielretention 0,90 Pflicht und 0,85 Ausblick → erprobt, MIT; (b) eigenes Rost-Modell → transparenter, unerprobt; (c) Leitner → einfach, grob.
- Empfehlung: (a), Rost nur als UI **[wahrscheinlich]**.

**G03 Frühschicht-Pflicht** · kern · Abh.: G05
- Frage: Wie verbindlich ist die tägliche Wiederholung?
- Warum: Der Kunde fordert Pflichtwiederholung; ein zweites Gate frustriert (06 W11).
- Optionen: (a) fällige Items werden ins Monatsgate eingebettet, die Frühschicht räumt sie vorher ab, Lastdeckel 30 % → Pflicht ohne Doppelsperre; (b) harte Tagespflicht vor dem Spielen → streng, Abbruchgefahr; (c) freiwillig → Wiederholung bricht weg.
- Empfehlung: (a) **[wahrscheinlich]**.

**G04 Zählregel** · kern · Abh.: G01
- Frage: Wie oft zählt eine Wiederholung pro Tag?
- Warum: Sechs Spielmonate an einem Abend dürfen nicht als sechs Wiederholungen gelten.
- Optionen: (a) ein Abruf je Skill und Kalendertag, egal wo → ehrlich, Binge erlaubt; (b) höchstens zwei Spielmonate pro Tag → bremst Spieler; (c) unbegrenzt → Scheinlernen.
- Empfehlung: (a) **[wahrscheinlich]**.

**G05 Monatsgate** · kern · Abh.: G03
- Frage: Wann schließt ein Spielmonat?
- Warum: Das Gate macht Routinen und Wiederholung verbindlich.
- Optionen: (a) Pflichtvorgänge mit ≥ 50 % der Punkte, sonst Nacharbeit mit neuen Zahlen → Qualität; (b) nur bearbeitet → Durchklicken möglich; (c) kein Gate → Pflicht entfällt.
- Empfehlung: (a) **[wahrscheinlich]**.

**G06 Kapitelgate und Nichtbestehen** · kern · Abh.: G08, I04
- Frage: Was gilt am Kapitelende, und was passiert beim Durchfallen?
- Warum: Ein „Wiederholungsjahr“ (17–20 h) ist strafend (Gutachten 1/2).
- Optionen: (a) Kapitelprüfung ab „gelernt“, bei Nichtbestehen gezielte Nachprüfungsfälle im nächsten Kapitel → kein Neuspielen; (b) Wiederholungsjahr mit neuem Seed → hohe Abbruchgefahr; (c) kein Gate → keine Konsolidierung.
- Empfehlung: (a) **[wahrscheinlich]**.

**G07 Rost-Konsequenz** · kern · Abh.: G02
- Frage: Was passiert bei verblasstem Wissen?
- Warum: Sperren nach Pausen frustrieren, ganz ohne Folge wirkt Rost nicht.
- Optionen: (a) Werkzeug beschlägt und zeigt nur noch die Richtung, Handrechnung bleibt möglich → funktional, nicht strafend; (b) Sperre mit Delegation → streng; (c) nur Warnung → wirkungslos.
- Empfehlung: (a) **[wahrscheinlich]**.

**G08 Mastery-Stufen** · kern · Abh.: G02
- Frage: Wie viele Mastery-Stufen gibt es?
- Warum: 03 und 04 definieren Mastery unterschiedlich (06 W7); die Prüfung braucht eine eigene Stufe.
- Optionen: (a) zwei (gelernt, beherrscht); (b) drei mit „prüfungsfest“ (≥ 67 % unter Zeitlimit, ≤ 30 Tage alt) → Fokus aufs Behalten am Prüfungstag.
- Empfehlung: (b) **[wahrscheinlich]**.

**G09 Hilfe-Rating** · wichtig · Abh.: G02
- Frage: Wie zählen Lösungen mit Hilfe?
- Warum: Hint-Spam und Scheinkompetenz gegen Ermutigung.
- Optionen: (a) Konzepthinweis = Hard, Worked Example oder Pohls Ordner = Again, Mastery nie mit Hilfe → ehrlich; (b) jede Hilfe = Again → streng; (c) Hilfe zählt voll → Scheinlernen.
- Empfehlung: (a) **[wahrscheinlich]**.

**G10 Credit Assignment** · kern · Abh.: H04
- Frage: Welcher Skill bekommt bei Mehrschrittaufgaben welche Bewertung?
- Warum: Ohne Regel verfälscht ein Fehler in Schritt 2 alle Skills (Gutachten 1).
- Optionen: (a) fehlerhafter Schritt = Again für seinen Skill, korrekt weitergerechnete Folgeschritte = Good, nicht bearbeitete ohne Rating → präzise; (b) nur das Endergebnis zählt für alle Skills → grob.
- Empfehlung: (a) **[wahrscheinlich]**.

**G11 FSRS-Parameter** · wichtig · Abh.: G02
- Frage: Bleiben die Standardparameter?
- Warum: Sie sind für Faktenkarten kalibriert, nicht für Prozeduren.
- Optionen: (a) lokal optimieren ab ≥ 1.000 Reviews → passend; (b) fest → einfach, ungenau; (c) global aus Playtests → Datenbedarf.
- Empfehlung: (a), bis dahin die Zielretention als Stellschraube **[wahrscheinlich]**.

**G12 Rückkehrmodus und Lastdeckel** · wichtig · Abh.: G03
- Frage: Wie wird Rückstau nach Pausen abgebaut?
- Warum: Ein Berg fälliger Items nach dem Urlaub führt zum Abbruch.
- Optionen: (a) höchstens 10 Items pro Tag nach Priorität, Pflicht ≤ 30 % je Session → sanft; (b) alles sofort → Frust; (c) Rückstand verfällt → Lücken.
- Empfehlung: (a) **[wahrscheinlich]**.

**G13 Serie und Urlaubsschein** · kür · Abh.: G03
- Frage: Gibt es Streaks oder Ligen?
- Warum: Streaks motivieren, erzeugen aber Druck (03, 3.6).
- Optionen: (a) Serie nur über erfolgreiche Wiederholungen, Urlaubsschein 2 Tage pro Woche, keine Liga → mild; (b) keine Serie → weniger Anreiz; (c) Serie mit Liga → Vergleichsdruck.
- Empfehlung: (a) **[Vermutung]**.

**G14 Mini-Zyklen für Jahresroutinen** · wichtig · Abh.: F03
- Frage: Wie werden Budget, Inventur und Jahresabschluss öfter geübt?
- Warum: Einmal pro Spieljahr reicht für Behalten nicht (06 #7).
- Optionen: (a) Archivakte mit Übungsabschlüssen (Markt 2/3, Vorjahre), Quartals-Forecast, unterjährige Bankanfragen → genug Abrufe; (b) nur jährlich → Vergessen.
- Empfehlung: (a) **[wahrscheinlich]**.

**G15 Akzeptierte Gesamtdauer** · kern · Abh.: E06
- Frage: Wie lange dürfen Lernende bis „prüfungsfest“ brauchen?
- Warum: Diese Annahme bestimmt Umfang und Last.
- Optionen: (a) 3 Monate → nur Teilkanon; (b) 6–9 Monate mit 3–4 h pro Woche (≈ 100–120 h) → passt zum Lehrgang; (c) 12 Monate → Motivationsverlust.
- Empfehlung: (b) **[Vermutung]**.

---

## H Aufgaben, Bewertung, Feedback

**H01 Eingabeform** · kern · Abh.: –
- Frage: Tippen oder Ankreuzen?
- Warum: Freier Abruf wirkt stärker als Wiedererkennen (03, 1.1).
- Optionen: (a) Zahlen tippen als Standard, Auswahl selten → lernwirksam; (b) Auswahl häufig → bequem, Raten.
- Empfehlung: (a) **[sicher als Lernbefund]**.

**H02 Toleranzen** · wichtig · Abh.: H03
- Frage: Wie genau muss eine Zahl sein?
- Warum: Zu streng straft Rundung, zu locker übersieht Fehler.
- Optionen: (a) je Größenart: Geld ±1 € bzw. ±0,5 %, Quoten ±0,1 Prozentpunkte → fair; (b) ±0,01 € → frustrierend; (c) ±2 % → ungenau.
- Empfehlung: (a) **[wahrscheinlich]**.

**H03 Anzeigeregel für Musterlösungen** · kern · Abh.: N05
- Frage: Rechnet die Musterlösung mit angezeigten oder ungerundeten Werten?
- Warum: Alle drei Entwürfe hatten deshalb Fehler (Eckkneipe: DB II 1.743 gegen 1.748,7 €).
- Optionen: (a) Golden Master löst mit genau den angezeigten Werten, CI-Test → korrekte Bewertung; (b) ungerundet → richtige Antworten gelten als falsch; (c) Werte mit mehr Nachkommastellen anzeigen → unübersichtlich.
- Empfehlung: (a) **[sicher, Rechnung]**.

**H04 Folgefehler** · wichtig · Abh.: G10
- Frage: Gibt es Teilpunkte für korrektes Weiterrechnen mit falschen Vorwerten?
- Warum: IHK-Bewertungen geben Folgepunkte **[wahrscheinlich]**.
- Optionen: (a) Lösungsgraph mit eigenen Vorwerten → fair, diagnostisch; (b) nur Endergebnis → hart.
- Empfehlung: (a) **[wahrscheinlich]**.

**H05 Freitext-Bewertung** · wichtig · Abh.: M07
- Frage: Wie werden Kurzfreitexte bewertet?
- Warum: Verbale Leistung ist Prüfungsstoff, ein LLM ist nicht verlässlich bewertbar.
- Optionen: (a) Musterlösung, Rubrik zur Selbstbewertung und Regelprüfer → offline, ehrlich; (b) zusätzlich optionales LLM-Feedback → besseres Feedback, Kosten und Datenschutz; (c) nur Satzbausteine → kein echter Abruf.
- Empfehlung: (a), (b) ab 1.1, nie als Gate oder für Punkte **[wahrscheinlich]**.

**H06 Argumentkarten** · wichtig · Abh.: E09
- Frage: Wo werden Argumentkarten eingesetzt?
- Warum: Sie trainieren Wiedererkennen statt Produzieren.
- Optionen: (a) nur in Fading-Stufe 1–2 → Gerüst, dann frei; (b) als Standardformat für „beurteilen“ → leicht automatisierbar, schwach.
- Empfehlung: (a) **[wahrscheinlich]**.

**H07 Pflicht-Nachbesprechung** · wichtig · Abh.: H08
- Frage: Ist das Monatsdebrief Pflicht?
- Warum: Debriefing ist der stärkste Hebel (d ≈ 0,67, 03).
- Optionen: (a) Pflicht, 3–5 Min. → Lernmotor; (b) überspringbar → wird übersprungen.
- Empfehlung: (a) **[wahrscheinlich]**.

**H08 Kontrafaktum** · wichtig · Abh.: K04, P01
- Frage: Wie entsteht der „Was wäre wenn“-Vergleich?
- Warum: Das Replay braucht eine Engine mit Common Random Numbers, die der MVP nicht hat.
- Optionen: (a) im MVP eine vorgerechnete Alternative, ab Engine ein echtes Replay → ehrlich gestuft; (b) nur Replay → erst später verfügbar; (c) keins → Lernhebel fehlt.
- Empfehlung: (a) **[wahrscheinlich]**.

**H09 Prüfer-Stichprobe** · wichtig · Abh.: H07
- Frage: Prüft der Abschlussprüfer alte eigene Vorgänge?
- Warum: Verzögertes Feedback mit Gewicht (03, 4.5).
- Optionen: (a) quartalsweise 10 Vorgänge aus den eigenen Vormonaten → Konsequenz; (b) keine.
- Empfehlung: (a) **[wahrscheinlich]**.

**H10 Mehrdeutige Fälle** · wichtig · Abh.: H05
- Frage: Gibt es Fälle mit mehreren vertretbaren Lösungen?
- Warum: Eine Simulation mit stets genau einer wahren Ursache trainiert falsche Sicherheit (06 #12).
- Optionen: (a) ab Kapitel 2 mit Begründungsbewertung → realistisch; (b) nie → einfacher.
- Empfehlung: (a) **[wahrscheinlich]**.

**H11 Glass Box** · wichtig · Abh.: C02
- Frage: Ist jede Kennzahl bis zum Beleg klickbar?
- Warum: Die Blackbox verleitet zum Optimieren ohne Verstehen.
- Optionen: (a) Markt 1 bis zum Beleg, KG bis zur Kostenstelle → transparent; (b) nur Formel → weniger Aufwand.
- Empfehlung: (a) **[wahrscheinlich]**.

**H12 Datenraum** · wichtig · Abh.: P01
- Frage: Gibt es eine Such- und Filteransicht für Belege, Konten und Protokolle?
- Warum: Abweichungsanalyse als Deduktionsfall (Stufe „Analysieren“).
- Optionen: (a) Datenraum light im MVP, voll in 1.0 → analytisches Spiel; (b) nur feste Tabellen → flacher.
- Empfehlung: (a) **[wahrscheinlich]**.

**H13 Bewertungsbogen nach Vorgang** · wichtig · Abh.: I07
- Frage: Bekommt jeder größere Vorgang IHK-Punkte und eine Note?
- Warum: Das Prüfungsformat wird so Alltag statt Sonderfall.
- Optionen: (a) Punkte je Teilaufgabe, Prüferkommentar, Note nach Schlüssel → prüfungsnah; (b) nur richtig/falsch → spielerischer, weniger diagnostisch.
- Empfehlung: (a) **[wahrscheinlich]**.

---

## I Prüfungsformat und Prüfungsvorbereitung

**I01 Prüfungstermin-Countdown** · wichtig · Abh.: G02
- Frage: Plant das Spiel rückwärts vom Prüfungstermin?
- Warum: Zielgröße ist das Behalten am Prüfungstag.
- Optionen: (a) Countdown mit Tapering [T−21; T−3] für Skills mit R(T) < 0,90 → Behalten zur Prüfung; (b) nur FSRS → kein Termin-Fokus.
- Empfehlung: (a) **[wahrscheinlich]**.

**I02 Prüfungsmodus auf Papier** · wichtig · Abh.: I03
- Frage: Gibt es Probeklausuren zum Ausdrucken?
- Warum: Die Prüfung läuft auf Papier mit Taschenrechner; Browser-Tabellen geben das Schema vor.
- Optionen: (a) PDF mit Bewertungsbogen und Eingabe der Ergebnisse zur Auswertung → prüfungsnah; (b) nur Browser → bequem, Scaffolding.
- Empfehlung: (a) zusätzlich **[wahrscheinlich]**.

**I03 Hilfsmittel im Prüfungsmodus** · wichtig · Abh.: I06
- Frage: Was ist in Probeklausuren erlaubt?
- Warum: Realismus.
- Optionen: (a) wie die IHK-Hilfsmittelliste → realistisch, erst nach Prüfung des Verordnungstexts; (b) zusätzlich ein Formelblatt → leichter; (c) frei → unrealistisch.
- Empfehlung: (a), bis zur Klärung (b) **[Vermutung]**.

**I04 Probeklausur-Rhythmus** · wichtig · Abh.: G06
- Frage: Wann kommen Prüfungsformate unter Zeitlimit?
- Warum: Testing-Effekt gegen Prüfungsangst.
- Optionen: (a) am Kapitelende und quartalsweise 45 Min. über alle HB → regelmäßig; (b) nur im Prüfungsjahr → spät; (c) jede Woche → Belastung.
- Empfehlung: (a) **[wahrscheinlich]**.

**I05 Externe Validierung** · wichtig · Abh.: A04
- Frage: Wie wird gemessen, ob das Spiel wirkt?
- Warum: Ohne Außenmaß bleibt „führt zum Bestehen“ eine Behauptung (Gutachten 1).
- Optionen: (a) Prä-/Posttest mit Dozenten-Items, blinde Dozentenkorrektur ≥ 90 %, freiwillige Meldung echter Ergebnisse → belastbar; (b) nur spielinterne Messung → zirkulär.
- Empfehlung: (a) **[wahrscheinlich]**.

**I06 Prüfungsordnung im Volltext** · kern · Abh.: –
- Frage: Wann wird der Verordnungstext geprüft?
- Warum: Bestehensregeln, Ergänzungsprüfung, Hilfsmittel und Gewichtung 25/45/30 sind nur über Suchauszüge belegt.
- Optionen: (a) vor dem MVP-Prüfungsmodus → keine Falschlehre; (b) vor 1.0 → Risiko im MVP.
- Empfehlung: (a) **[sicher als Notwendigkeit]**.

**I07 Notenschlüssel und Zeitbudget** · wichtig · Abh.: I06
- Frage: Nach welchem Schlüssel und Takt wird bewertet?
- Warum: Die Bewertung soll sich wie eine korrigierte Klausur anfühlen.
- Optionen: (a) IHK-100-Punkte-Schlüssel, 1,8 Min. je Punkt in HB1/HB2 → vertraut; (b) eigene Skala → beliebig.
- Empfehlung: (a), Punktzahl je Klausur nach der Verordnungsprüfung anpassen **[Vermutung]**.

**I08 Leeres-Blatt-Stufe** · wichtig · Abh.: G08
- Frage: Ist das freie Rechnen ohne Schema Pflicht für „prüfungsfest“?
- Warum: Lückentabellen verraten das Lösungsschema.
- Optionen: (a) Fading-Stufe 5 mit Rechenweg-Pflicht als Voraussetzung → prüfungsnah; (b) optional → Lücke.
- Empfehlung: (a) **[wahrscheinlich]**.

---

## J Werkstätten HB4, HB5, HB6

**J01 HB4-Werkzeug** · kern · Abh.: M10
- Frage: Wie wird Tabellenkalkulation geübt?
- Warum: HB4 wird 240 Min. am echten Programm geprüft.
- Optionen: (a) Browser-Arbeitsblatt für Mikroübungen plus xlsx-Abgabe in Excel oder Calc → echter Werkzeugtransfer; (b) nur Browser → kein Excel; (c) nur Export ohne Prüfung → kein Feedback.
- Empfehlung: (a), getestet gegen Excel und LibreOffice **[wahrscheinlich]**.

**J02 Prüftiefe der xlsx-Abgaben** · wichtig · Abh.: J01
- Frage: Was wird an der hochgeladenen Datei geprüft?
- Warum: Hartkodierte Zahlen sind ein typischer HB4-Fehler.
- Optionen: (a) Werte benannter Zellen, Formeln statt Werten, Prüfsummen; Diagramme per Selbstcheck → solide; (b) nur Werte → oberflächlich.
- Empfehlung: (a) **[wahrscheinlich]**.

**J03 HB5-Transferpfad** · wichtig · Abh.: J04
- Frage: Ist die Übertragung auf den eigenen Betrieb Pflicht?
- Warum: Die echte Projektarbeit entsteht im eigenen Umfeld; HB5 zählt 45 % der Note.
- Optionen: (a) Pflicht fürs Zeugnis → realer Prüfungsnutzen; (b) optional → größter Notenanteil bleibt unvorbereitet.
- Empfehlung: (a) **[wahrscheinlich]**.

**J04 HB5-Bewertung** · wichtig · Abh.: H05
- Frage: Wer bewertet die Projektarbeit im Spiel?
- Warum: Automatisch prüfbar ist nur die Struktur.
- Optionen: (a) Struktur automatisch, Inhalt per Selbstbewertung nach Rubrik (§ 4 Abs. 5), Export für Mentor oder Dozent → ehrlich; (b) zusätzlich LLM-Feedback → hilfreich, unsicher; (c) Peer-Bewertung → braucht Gruppen.
- Empfehlung: (a), (b) optional **[wahrscheinlich]**.

**J05 HB5-Zeitmodus** · wichtig · Abh.: J03
- Frage: Laufen die 30 Tage echt oder verdichtet?
- Warum: Zeitmanagement ist Teil der Prüfung.
- Optionen: (a) 30 Kalendertage mit Meilensteinen (Tag 1/7/14/21/28/30) und Formaliatagen → realistisch; (b) 30 Spieltage an zwei Abenden → bequem, ohne Zeitmanagement.
- Empfehlung: (a) **[wahrscheinlich]**.

**J06 HB6-Übungsform** · wichtig · Abh.: H05
- Frage: Wie werden Präsentation und Fachgespräch geübt?
- Warum: Ein Dialogbaum trainiert Erkennen, nicht Auftreten.
- Optionen: (a) Dialogbaum mit drei Prüfer-Personas, lokale Audioaufnahme, druckbare Peer-Rollenkarten → umsetzbar und nah am Auftreten; (b) LLM-Rollenspiel → lebendig, unzuverlässig; (c) nur Dialogbaum → schwach.
- Empfehlung: (a), (b) optional ab 1.1 **[wahrscheinlich]**.

**J07 Teamführung und Moderation** · wichtig · Abh.: B04
- Frage: Wie wird Führen geübt, obwohl der Controller kaum führt?
- Warum: § 4 Abs. 6 nennt Teamführung ausdrücklich.
- Optionen: (a) Assistenz Lena ab Kapitel 2, Inventurteams, Projektteam Abfüllung, Moderations-Minispiel Budgetrunde → ausreichend; (b) weglassen → Lücke in HB6.
- Empfehlung: (a) **[wahrscheinlich]**.

**J08 Folienbaukasten** · kür · Abh.: J06
- Frage: Eigener Baukasten oder Export nach PowerPoint?
- Warum: Präsentationsübung gegen Bauaufwand.
- Optionen: (a) eigener Baukasten mit IBCS-Presets und PDF-Export → kontrollierbar; (b) pptx-Export → echtes Werkzeug, Aufwand.
- Empfehlung: (a) **[Vermutung]**.

---

## K Simulation, Zufall, Ereignisse

**K01 Ereignisbudget** · wichtig · Abh.: K02
- Frage: Wie werden Ereignisse dosiert?
- Warum: Zufällige Häufungen (drei Gastro-Insolvenzen plus Kistenknappheit) überfordern.
- Optionen: (a) Budget je Quartal und Schwierigkeitsband → fair; (b) frei gezogen → realistisch, unfair; (c) fest geskriptet → vorhersehbar.
- Empfehlung: (a) **[wahrscheinlich]**.

**K02 Schwierigkeitssteuerung** · wichtig · Abh.: H01
- Frage: Fest oder adaptiv?
- Warum: Zielerfolgsquote 70–85 % (03, 6.4).
- Optionen: (a) Elo-basiert adaptiv mit Zielband → Flow; (b) fest je Kapitel → einfacher, ungleich.
- Empfehlung: (a) **[wahrscheinlich]**.

**K03 Wetter mit Prognosefehler** · wichtig · Abh.: C02
- Frage: Sieht der Spieler eine unsichere Prognose?
- Warum: Disposition unter Unsicherheit (Newsvendor, Q ≈ 799).
- Optionen: (a) 7-Tage-Prognose mit Fehlerband, Ist kommt später → lehrreich; (b) nur Ist-Wetter → keine Prognoseaufgabe.
- Empfehlung: (a) **[wahrscheinlich]**.

**K04 Common Random Numbers** · wichtig · Abh.: H08
- Frage: Wie wird Zufall für Replays gezogen?
- Warum: Ohne CRN driftet das Kontrafaktum (06 W12).
- Optionen: (a) Hash aus Seed, Tag, Objekt und Zweck → stabile Replays; (b) getrennte Ströme je Teilsystem → einfacher, Drift.
- Empfehlung: (a) **[wahrscheinlich]**.

**K05 Seeds und feste Ereignisse** · wichtig · Abh.: F07
- Frage: Was ist geskriptet, was zufällig?
- Warum: Erzählung braucht feste Punkte, Wiederholung braucht Varianz.
- Optionen: (a) Story-Ereignisse fest, Umwelt (Wetter, Insolvenzen, Diesel) per Seed, Prüfungsjahre voll gezogen → beides; (b) alles per Seed ab Jahr 2 → schwache Story; (c) alles fest → keine Varianz.
- Empfehlung: (a) **[wahrscheinlich]**.

**K06 Zentraler Parametersatz** · wichtig · Abh.: N05
- Frage: Wo liegen Modellparameter?
- Warum: 01–04 hatten widersprüchliche Parameter (06 W6).
- Optionen: (a) eine Quelle (`gruppe.yaml`), aus dem Golden-Master-Skript erzeugt → konsistent; (b) verteilt je Modul → Widersprüche.
- Empfehlung: (a) **[sicher als Lehre aus 06]**.

---

## L Buchhaltung, Pfand, Steuern, Recht im Spiel

**L01 Pfand-Bilanzmodell** · kern · Abh.: C05
- Frage: Brutto- oder Nettoausweis des Pfands?
- Warum: Der Ausweis verschiebt EK-Quote (28,2 gegen 30,5 %) und Liquidität (85,8 gegen 66,6 %).
- Optionen: (a) brutto: Erstattungsanspruch und Pfandverbindlichkeit → Kreislauf sichtbar, BFH I R 36/07; (b) netto saldiert → bessere Quote, Kreislauf unsichtbar.
- Empfehlung: (a), saldiert als Vergleichskennzahl **[wahrscheinlich]**.

**L02 Pfand auf Belegen** · wichtig · Abh.: L01
- Frage: Wie steht Pfand auf Rechnungen?
- Warum: 02 und 03 widersprachen sich (06 W4).
- Optionen: (a) Sätze brutto inkl. USt, Bilanz netto (÷ 1,19), Netto je Gebinde auf Cent gerundet (2,61 €) → eine Konvention; (b) netto zuzüglich USt → abweichend vom Handel.
- Empfehlung: (a) **[wahrscheinlich]**.

**L03 Pfand eigener Gebinde** · wichtig · Abh.: D06
- Frage: Wie bilanziert die Gruppe als Inverkehrbringer die Hausmarken-Gebinde?
- Warum: Die Rechtslage (BFH I R 33/11) ist für diesen Fall ungeklärt.
- Optionen: (a) Pool als Festwert im Anlagevermögen, Kundenpfand als Verbindlichkeit → plausibel, transparent; (b) Rückstellung statt Verbindlichkeit → anderes Bilanzbild.
- Empfehlung: (a) vorläufig, WP-Prüfung vor Content-Freigabe **[Vermutung]**.

**L04 Bucht der Spieler selbst?** · wichtig · Abh.: F09
- Frage: Erfasst der Spieler Buchungssätze?
- Warum: Buchen ist Grundlage für HB3, aber nicht Controllerkern.
- Optionen: (a) in ausgewählten Vorgängen (Pfand, Abgrenzung, Konsolidierung), sonst bucht die Buchhaltung → Fokus; (b) nie → HB3-Lücke; (c) immer → Buchhaltungsspiel.
- Empfehlung: (a) **[wahrscheinlich]**.

**L05 Kalkulatorische Kosten** · wichtig · Abh.: C02
- Frage: Gibt es von Anfang an eine KLR-Schicht mit Anders- und Zusatzkosten?
- Warum: Abgrenzung (M04) ist Kapitel-1-Stoff.
- Optionen: (a) KLR-Schicht ab Start, aktiv ab der Kapitel-1-Leitfrage → konsistent; (b) erst später → Umbau.
- Empfehlung: (a) **[wahrscheinlich]**.

**L06 Steuern im Spiel** · wichtig · Abh.: C06
- Frage: Wie detailliert sind Gewerbe-, Einkommen- und Zuckersteuer?
- Warum: Steuercontrolling (M49) gegen Komplexität.
- Optionen: (a) Gewerbesteuer im Organkreis voll (Hinzurechnung, Sondervergütung), ESt-Entnahmen pauschal 45 % → lehrreich, beherrschbar; (b) alles pauschal → M49 fehlt; (c) alles exakt → Steuerberatungsspiel.
- Empfehlung: (a) **[wahrscheinlich]**.

**L07 Rechtsstand-Freeze** · wichtig · Abh.: C06, D03
- Frage: Wird der Rechtsstand eingefroren oder gepflegt?
- Warum: Mindestlohn, Pfand, Zuckersteuer und CO₂-Preis ändern sich laufend.
- Optionen: (a) Freeze am 20.10.2026, spätere Entwicklungen als fiktive Fortschreibung markiert, versioniert → stabil; (b) jährliches Update → aktuell, Pflegeaufwand.
- Empfehlung: (a) **[wahrscheinlich]**.

---

## M Technik und Plattform

**M01 Plattform und Framework** · kern · Abh.: –
- Frage: Womit wird gebaut?
- Warum: Vorwissen, Lizenzen, Offline und Barrierefreiheit (04).
- Optionen: (a) local-first PWA mit Angular 22 → passt zum Vorwissen; (b) React → größerer Talentpool; (c) Desktop (Tauri) → installierbar, mehr Aufwand; (d) Game-Engine → Tabellen auf Canvas ungeeignet.
- Empfehlung: (a), Engine frameworkfrei **[wahrscheinlich]**.

**M02 Lizenzmodell** · kern · Abh.: M10, O04
- Frage: Wird der Code offen veröffentlicht?
- Warum: Davon hängt die Formel-Engine ab (HyperFormula nur bei GPLv3).
- Optionen: (a) proprietär bzw. geschlossen → eigener Parser nötig; (b) MIT → Reichweite, eigener Parser; (c) GPLv3 → HyperFormula möglich (−4 PT).
- Empfehlung: Entscheidung offen lassen, eigener Parser hält alle Wege offen **[wahrscheinlich]**.

**M03 Sync** · wichtig · Abh.: M04
- Frage: Wie überlebt der Lernstand Gerätewechsel und Browser-Eviction?
- Warum: Bei Pflichtwiederholung über Monate ist Datenverlust ein Produktblocker.
- Optionen: (a) ab MVP Datei- und QR-Export mit Backup-Erinnerung, vor 1.0 optionaler Firebase-Sync (anonym, Pseudonym) → sicher, datensparsam; (b) nur Datei → Gerätewechsel mühsam; (c) Pflicht-Konto → DSGVO-Aufwand.
- Empfehlung: (a) **[wahrscheinlich]**.

**M04 Mobile Aufgabentypen** · wichtig · Abh.: G03
- Frage: Was läuft auf dem Smartphone?
- Warum: Die Frühschicht soll mobil gehen, Tabellen gehen auf 375 px nicht.
- Optionen: (a) Frühschicht-Typen (Zahl mit Dezimalkomma, Auswahl, Zuordnung, kurze Kette, Kurzfreitext) mobil, Tabellen ab 768 px, Scheduler wählt passend → realistisch; (b) alles mobil → schlechte Tabellen-UX; (c) nur Desktop → keine tägliche Gewohnheit.
- Empfehlung: (a) **[wahrscheinlich]**.

**M05 Klassen- und Lehrgangsmodus** · kür · Abh.: O06
- Frage: Gibt es Funktionen für Dozenten?
- Warum: Lehrgangsträger sind ein Vertriebskanal.
- Optionen: (a) nie; (b) Datei-Abgabe an ein lokales Dozenten-Dashboard → 0 €, keine Konten; (c) Server mit Klassencodes → +15–25 PT.
- Empfehlung: (b) nach 1.0 **[Vermutung]**.

**M06 Ranglisten** · kür · Abh.: M05
- Frage: Gibt es Vergleiche mit anderen Spielern?
- Warum: Ranglisten verleiten zum Exploit und frustrieren Schwächere.
- Optionen: (a) keine; (b) Histogramme statt Ränge → informativ; (c) global → Druck.
- Empfehlung: (b) für Optimierungsaufgaben, sonst (a) **[Vermutung]**.

**M07 KI-Tutor** · wichtig · Abh.: H05, J04, J06
- Frage: Kommt ein LLM zum Einsatz?
- Warum: Besseres Feedback bei Freitext gegen Kosten, Datenschutz und Zuverlässigkeit.
- Optionen: (a) nie → offline, sicher; (b) optional mit eigenem Schlüssel → keine Kosten; (c) gehostet mit Budget über Proxy → bequem, AVV nötig.
- Empfehlung: (b) und (c) als Feature-Flag ab 1.1, nie als Gate **[wahrscheinlich]**.

**M08 Entwicklerwerkzeuge** · wichtig · Abh.: P03
- Frage: Ab wann gibt es simulierte Uhr, Zeitsprung und synthetische Lernende?
- Warum: Eine Mechanik über 6–9 Monate ist sonst nicht testbar.
- Optionen: (a) ab K0 → Scheduler-Last früh prüfbar; (b) später → blinde Flecken.
- Empfehlung: (a) **[wahrscheinlich]**.

**M09 Datenschutz und Tracking** · wichtig · Abh.: M03
- Frage: Werden Nutzungsdaten erhoben?
- Warum: DSGVO, Schulen, Vertrauen.
- Optionen: (a) kein Tracking, Messung nur über freiwilligen Export → datensparsam; (b) cookielose Statistik → Reichweitenzahlen; (c) Analytics → Rechtsaufwand.
- Empfehlung: (a), (b) optional **[wahrscheinlich]**.

**M10 Rechenblatt-Engine** · wichtig · Abh.: M02
- Frage: Welche Formel-Engine nutzt das Arbeitsblatt?
- Warum: Lizenz und Bundle-Größe.
- Optionen: (a) eigener Parser plus formula.js (4–6 PT) → lizenzfrei; (b) HyperFormula → nur unter GPLv3; (c) Univer lazy nur für M28 → schwer (≈ 40 MB).
- Empfehlung: (a) **[wahrscheinlich]**.

---

## N Inhaltsproduktion und Qualität

**N01 Inhaltsproduktion** · kern · Abh.: N02, N03
- Frage: Wer erstellt ≈ 220 Vorlagen, Karten und Szenen?
- Warum: Inhalt ist der Engpass (≈ 140–160 PT in 1.0).
- Optionen: (a) KI-Entwurf, CI gegen Golden Master (50 Instanzen je Vorlage), Fachreview mit Stundenbudget → skalierbar; (b) Autor schreibt alles → langsam; (c) extern → teuer.
- Empfehlung: (a) **[wahrscheinlich]**.

**N02 Fachreview** · kern · Abh.: N01
- Frage: Wer prüft fachlich?
- Warum: Alle drei Entwürfe enthielten falsche Musterlösungen.
- Optionen: (a) GFGH-Controllerin (Branchenzahlen) plus Lehrgangsdozent (Prüfungsstil), beide mit Stundenbudget → Qualität; (b) nur Dozent → Branchenfehler bleiben; (c) keiner → Vertrauensverlust.
- Empfehlung: (a) **[wahrscheinlich]**.

**N03 KI-taugliches Vorlagenformat** · wichtig · Abh.: N01, E08
- Frage: In welchem Format entstehen Vorlagen?
- Warum: Erst ein KI-taugliches Format macht ≤ 0,5 PT je Vorlage erreichbar.
- Optionen: (a) YAML mit Solver-ID, Fehlerfunktionen, Oberflächen, Zod-Schema, automatische Instanzprüfung → reviewbar; (b) freie Texte → nicht prüfbar.
- Empfehlung: (a) **[wahrscheinlich]**.

**N04 Inhalt messen vor Planung** · kern · Abh.: P01
- Frage: Wird der Aufwand je Vorlage vor der 1.0-Planung gemessen?
- Warum: 0,3 gegen 0,8 PT je Vorlage verdoppelt das Projekt.
- Optionen: (a) ja, nach K0 mit 8 Vorlagen → belastbare Planung; (b) nein → Blindflug.
- Empfehlung: (a) **[sicher als Lehre aus 04/06]**.

**N05 Golden-Master-Pflege** · wichtig · Abh.: H03, K06
- Frage: Werden Zahlen in Inhalten generiert oder handgepflegt?
- Warum: Handgepflegte Zahlen waren die Hauptfehlerquelle (06, 2.3).
- Optionen: (a) alle Zahlen aus dem Modell generiert, Prüfungen im Skript → konsistent; (b) Handpflege → Fehler.
- Empfehlung: (a) **[sicher als Lehre aus 06]**.

**N06 Kapitelweise Veröffentlichung** · wichtig · Abh.: P04
- Frage: Erst alles oder Kapitel für Kapitel?
- Warum: 1.0 dauert im Hobbytempo 4–5,5 Jahre.
- Optionen: (a) Kapitel 1 allein spielbar veröffentlichen (≈ 120–160 PT) → früher Nutzen, Feedback; (b) erst 1.0 → spät, riskant.
- Empfehlung: (a) **[wahrscheinlich]**.

**N07 Theoriekarten-Format** · kür · Abh.: E03
- Frage: Wie lang dürfen Theorietexte sein?
- Warum: Textwände gegen Tiefe.
- Optionen: (a) Karte ≤ 90 Wörter plus Dossier oder Skriptverweis → beides; (b) längere Texte → Lesemüdigkeit.
- Empfehlung: (a) **[wahrscheinlich]**.

---

## O Recht, Marken, Vertrieb, Geld

**O01 Arbeitstitel** · wichtig · Abh.: B05
- Frage: Wie heißt das Spiel?
- Warum: Wiedererkennung, Werktitelschutz, keine IHK-Nähe.
- Optionen: (a) „VOLLGUT – Controlling in der Getränkegruppe“; (b) „Leergut kommt zurück“ (Wiederholungsmetapher); (c) „SALDO“; (d) „Prüfstand“.
- Empfehlung: (a) nach DPMA- und Steam-Prüfung **[Vermutung]**.

**O02 Marken** · kern · Abh.: B05
- Frage: Echte oder fiktive Marken?
- Warum: Das Spiel enthält Margenaussagen über Marken.
- Optionen: (a) fiktive Archetypen ohne Klangähnlichkeit → rechtssicher; (b) reale Gattungen ohne Marken → neutral; (c) echte Marken → Tatsachenbehauptungen über reale Unternehmen.
- Empfehlung: (a) **[wahrscheinlich, 05]**.

**O03 Alkoholschalter** · wichtig · Abh.: A02
- Frage: Kann der Alkoholanteil umgeschaltet werden?
- Warum: Schulen, Eltern, Werbeanschein.
- Optionen: (a) umschaltbar (Schulversion mit AfG-Fokus) → breiter einsetzbar; (b) realistisch fest → Schulausschluss; (c) dauerhaft reduziert → weniger realistisch.
- Empfehlung: (a) ab 1.0 **[Vermutung]**.

**O04 Monetarisierung** · wichtig · Abh.: M02
- Frage: Wie wird Geld verdient?
- Warum: Rechtsaufwand gegen Erlöse; der Markt bringt nur vierstellige Jahreserlöse (05).
- Optionen: (a) kostenlos als Portfolio → maximale Reichweite; (b) Freemium mit Einmalkauf 19 € → AGB, Umsatzsteuer, Support; (c) Lizenzen für Lehrgangsträger → planbare Erlöse, Vertriebsaufwand.
- Empfehlung: (a), (c) nach nachgewiesener Nutzung **[Vermutung]**.

**O05 IHK-Bezug in der Kommunikation** · kern · Abh.: A06
- Frage: Wie darf auf die Prüfung Bezug genommen werden?
- Warum: § 5 UWG, Markenrecht, Vertrauen.
- Optionen: (a) beschreibend („orientiert an der ContrPrV“) plus Disclaimer „keine Verbindung zu IHK/DIHK“ → üblich; (b) gar nicht → Zielgruppe findet das Spiel nicht; (c) „IHK-zertifiziert“ → unzulässig.
- Empfehlung: (a) **[wahrscheinlich, 05]**.

**O06 Lehrgangsträger als Partner** · kür · Abh.: M05, O04
- Frage: Wird das Spiel mit Bildungsträgern angeboten?
- Warum: Reichweite und Validierung.
- Optionen: (a) Gespräche nach dem MVP → Testgruppen, Feedback; (b) nein → Einzelvertrieb.
- Empfehlung: (a) **[Vermutung]**.

**O07 Nutzungsrechte an den Skripten** · kern · Abh.: E02, E03
- Frage: Was darf aus den gelieferten Skripten ins Spiel?
- Warum: Lehrgangsskripte sind vermutlich urheberrechtlich geschützt.
- Optionen: (a) nur Zuordnung, Kapitel- und Seitenverweise, eigene Formulierungen → rechtssicher; (b) Textübernahme mit Lizenz → Vertrag nötig; (c) Übernahme ohne Klärung → Risiko.
- Empfehlung: (a), Rechte vor der Lieferung schriftlich klären **[wahrscheinlich]**.

---

## P MVP und Roadmap

**P01 MVP-Schnitt** · kern · Abh.: C02, N04
- Frage: Was ist der kleinste Beweis?
- Warum: Er testet die riskantesten Annahmen am billigsten.
- Optionen: (a) K0-Kernbeweis (Fallmaschine, Prüfer, FSRS, 22–30 PT) plus Schreibtisch-MVP Januar bis März mit 2 Großhandels-Vorgängen (+25–35 PT) → testet Lernkern, Spielspaß und Content-Kosten; (b) nur K0 → kein Spielspaß-Test; (c) MVP mit Live-Engine (60–85 PT) → teuer; (d) Vertical Slice Kapitel 1 ohne Fallmaschine → testet den GFGH nicht.
- Empfehlung: (a) **[wahrscheinlich]**.

**P02 Großhandel im MVP** · kern · Abh.: P01
- Frage: Enthält der MVP schon Großhandels-Vorgänge?
- Warum: Der B2B-Einstieg ist laut 08 der riskanteste neue Inhalt.
- Optionen: (a) zwei Vorgänge (Saldenbestätigung Brauerei Nord, Eckkneipe) → Risiko früh getestet; (b) keiner → Überraschung später.
- Empfehlung: (a) **[wahrscheinlich]**.

**P03 Playtest-Design** · wichtig · Abh.: M08, I05
- Frage: Wie und wie lange wird getestet?
- Warum: Eine Mechanik über Monate lässt sich in zwei Wochen nicht validieren.
- Optionen: (a) MVP mit 5 Personen über 3 Wochen, vor 1.0 Längsschnitt-Kohorte ≥ 8 Wochen mit Re-Test → belastbar; (b) nur Kurz-Playtests → Fehlschlüsse.
- Empfehlung: (a) **[wahrscheinlich]**.

**P04 Release-Reihenfolge** · wichtig · Abh.: N06
- Frage: In welcher Reihenfolge wird veröffentlicht?
- Warum: Früher Nutzen gegen Gesamtbild.
- Optionen: (a) K1 → K2 → K3 mit Werkstätten je Stufe → stetiger Fortschritt; (b) Werkstätten (HB4–6) zuerst → schneller Prüfungsnutzen, weniger Spiel; (c) alles zu 1.0.
- Empfehlung: (a), Excel-Werkstatt früh als Bonus **[Vermutung]**.

**P05 Abbruch- und Kürzungskriterien** · wichtig · Abh.: N04, P03
- Frage: Wann wird der Umfang gekürzt?
- Warum: Ein Ein-Personen-Projekt braucht harte Haltepunkte.
- Optionen: (a) vorab definierte Schwellen: Vorlage > 0,8 PT → Kanon kürzen; Übereinstimmung mit Dozentenkorrektur < 80 % → Prüfer überarbeiten; < 3 von 5 Testpersonen bleiben → Schleife überarbeiten → steuerbar; (b) keine → Versanden.
- Empfehlung: (a) **[wahrscheinlich]**.
