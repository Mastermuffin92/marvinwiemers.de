# 02 – Domänenmodell deutscher Getränkemarkt (Stand Oktober 2026)

Grundlage für die Simulation „Controller im Getränkemarkt“. Sicherheitsstufen: **[sicher]** = durch amtliche Quelle oder mehrere unabhängige Quellen belegt; **[wahrscheinlich]** = einzelne Fachquelle oder starke Ableitung; **[Vermutung]** = Lücke mit Branchenlogik gefüllt (Spielannahme). Zahlen ohne Quelle sind Annahmen.

**Quellenlage:** Die Websuche lief, der Abruf ganzer Seiten (WebFetch) schlug bei allen Fachquellen fehl (DNS-Fehler). Belegt ist deshalb alles nur über Suchtreffer-Auszüge (Destatis, IHK, BMJ/gesetze-im-internet, UBA, Fachpresse Lebensmittelpraxis/LZ/Meininger/dpa). Öffentliche Betriebsvergleiche mit Rohertrags- und Kostenquoten für Getränkefachmärkte gibt es nicht. Alle Quoten zu Spannen, Kosten und Rendite sind daher **[Vermutung]**, aber aufeinander abgestimmt (siehe Abschnitt 12, der Plan ist rechnerisch geschlossen).

---

## 1. Betriebstypen und Markt

### 1.1 Marktgröße und Struktur

| Kennzahl | Wert | Stufe / Quelle |
|---|---|---|
| Getränkefachmärkte > 50 m² VK (2022) | 8.760 | [sicher] Statista |
| Getränkeabholmärkte (Trade Dimensions) | 8.954 (2018) → 7.820 (Prognose 2021) | [sicher] als Angabe, LP |
| Umsatz Abholmärkte inkl. Großhandel/Regiemärkte (Prognose 2021) | 14,9 Mrd. € | [wahrscheinlich] Nielsen/Tradedimensions, Abgrenzung unscharf |
| VDGE-Mitglieder (Filialisten), H1 2025 | 22 operative Mitglieder, 2.476 Outlets (−2,3 %), 1,446 Mrd. € Umsatz (+0,4 %) | [sicher] Lebensmittelpraxis |
| Ø Umsatz je VDGE-Outlet | ≈ 1,17 Mio. €/Jahr (2 × 1,446 Mrd. / 2.476) | [wahrscheinlich] eigene Ableitung, Saisonfehler ±5 % |
| VDGE 2025: Monatsumsatz je Markt | > +3 % nach Bereinigung des Filialnetzes; Markt gesamt NIQ −0,6 %, YouGov +0,2 % | [sicher] LZ |
| Nicht filialisierte Fachmärkte 2023 | Umsatz −18,5 % (GfK), Filialisten stabil | [sicher] als Angabe, LP |
| Getränkekäufer, die in Supermarkt/Discounter kaufen | 89 % | [wahrscheinlich] Mintel |
| Bierabsatz 2025 | 7,8 Mrd. l (−6,0 %, stärkster Rückgang seit 1993), 82,5 % Inland; 10-Jahres-Minus 18,9 % | [sicher] Destatis |
| Brauereien 2025 | 1.415 (−53 ggü. 2024) | [sicher] Destatis |
| Mehrwegquote Getränke | 34,3 % (2023), 34,5 % (2024); Ziel laut Gesetz 70 % | [sicher] UBA |

**Strukturaussage fürs Spiel:** Der Markt schrumpft bei Bier mengenmäßig. Filialisten und Verbünde gewinnen, kleine Inhabermärkte verlieren [sicher]. Industrie und Handel erhöhen Listenpreise, gleichzeitig kosten Kisten in Aktionen wieder 9,99 € (WM 2026, siehe 9). Diese Margenschere ist das zentrale Spannungsfeld für den Controller [sicher als Befund, Wirkung auf Einzelmarkt Vermutung].

### 1.2 Betriebstypen

| Typ | Fläche VK | SKUs | Umsatz/Jahr | Merkmale | Spielrelevanz |
|---|---|---|---|---|---|
| Getränkeabholmarkt (klein, inhabergeführt) | 200–600 m² | 600–1.500 | 0,4–1,2 Mio. € | Kistenware, wenig Kühlung, Kunden kommen mit dem Auto | Startszenario „Überleben“ [Vermutung] |
| Getränkefachmarkt (Filiale/Franchise) | 600–1.200 m² (trinkgut-Neueröffnungen: 740, 835, 850 m²) | 2.000–4.000 (trinkgut Köngen > 3.000; > 300 Biersorten in Neunkirchen) | 1–3,5 Mio. € (trinkgut Ø ≈ 3,3 Mio.) | Kühlung, Wein und Spirituosen, Leergutautomaten, 25 bis über 100 Parkplätze | Standardszenario [sicher für Beispiele, Spannen Vermutung] |
| LEH-Getränkemarkt (Edeka/Marktkauf/Rewe, an den Supermarkt angeschlossen) | 300–1.000 m² (Marktkauf Gütersloh: ≈ 5.000 Artikel auf 1.000 m²) | 1.500–5.000 | k. A. | profitiert von der Frequenz des Supermarkts | Konkurrent [sicher Beispiel] |
| Discounter (Aldi, Lidl, Penny, Netto) | Regalmeter im Markt | 100–300 Getränke | k. A. | vor allem Einweg, Preisführer, eigene Abfüllung | Preisdruck, Konkurrenzereignis [wahrscheinlich] |
| Getränkefachgroßhandel (GFGH) | Lager 2.000–20.000 m² | 3.000–8.000 | 5–100+ Mio. € | beliefert Gastronomie und Veranstaltungen, Fuhrpark, Kühlung, Schankanlagen-Service | Ausbaustufe [Vermutung] |
| Heimdienst des Marktes | – | Auszug | 5–15 % des Marktumsatzes | Liefergebühr 0–8 €, Mindestbestellwert | Modul mit eigener Deckungsbeitragsrechnung [Vermutung] |
| Online-Lieferdienst (flaschenpost) | Hubs | 3.000–5.000 | k. A. (Oetker nennt keine Zahlen) | Lieferung in 120 Minuten, > 40 % der Haushalte erreichbar, Düsseldorf geschlossen, 2024 Umsatzziele verfehlt | Konkurrenzereignis [sicher Fakten] |
| Veranstaltungsservice | – | Fassbier, Kommissionsware | 2–5 % | Ausschankwagen, Kühlanhänger, Garnituren, Rücknahme ungeöffneter Kommissionsware | Modul mit hoher Marge und Kapitalbindung [Vermutung] |

### 1.3 Wichtige Akteure (Stand 2025/26)

- **Getränke Hoffmann** (Radeberger Gruppe/Oetker): nennt sich „größter Getränkefacheinzelhändler“ [sicher], > 500 Filialen laut Stellenanzeige um 2022 [wahrscheinlich]. Viele Märkte führen Franchisenehmer [sicher, älterer Stand]. Hoffmann kauft künftig gemeinsam mit Edeka bei überregionalen Lieferanten ein [sicher]. Am 10.11.2025 hat Hoffmann 5 Märkte von Getränkeland Heidebrecht übernommen [sicher]. Seit 1.1.2026 vermarktet Team Beverage ≈ 120 Partnermärkte von Hoffmann gegenüber der Industrie [sicher].
- **trinkgut** (Edeka): 265 Märkte und 884,5 Mio. € Umsatz 2023 [sicher], meist von selbstständigen Kaufleuten geführt, ≈ 800 Biersorten im Gesamtsortiment [wahrscheinlich].
- **Fristo SE** (Familie Brügel): 8 Bundesländer plus Tirol, > 1.750 Mitarbeiter, 68 eigene Lkw, Umsatz in ≈ 10 Jahren verdoppelt [sicher als Selbstangabe]. Marktanzahl ≈ 200 [Vermutung].
- **Orterer** (Bayern, Märkte und GFGH), **Getränkeland**, regionale Ketten: keine belastbaren Zahlen gefunden. Größenordnung 50–150 Märkte [Vermutung].
- **Verbünde/Kooperationen:** Team Beverage, Get N Gruppe (2,1 Mrd. € Umsatz) [wahrscheinlich: Schlagzeile LP]. Sie verhandeln Konditionen, organisieren Zentralregulierung und Eigenmarken [Vermutung zu Leistungsumfang].
- **flaschenpost** (Oetker, gehört zur Radeberger Gruppe): Wachstum 2025 ohne Zahlen. Oetker-Gruppe gesamt 7,1 Mrd. € [sicher].

---

## 2. Typische Größen eines Fachmarkts

| Größe | Spanne | Wert im Beispiel | Stufe |
|---|---|---|---|
| Verkaufsfläche | 600–1.200 m² | 900 m² + 450 m² Lager/Leergut | [wahrscheinlich] trinkgut-Beispiele |
| SKUs | 2.000–4.000 | 2.800 | [wahrscheinlich] |
| Jahresumsatz netto | 1,0–3,5 Mio. € | 2,5 Mio. € inkl. Heim- und Festservice | [wahrscheinlich] VDGE-Ø 1,17 Mio., trinkgut-Ø 3,3 Mio. |
| Umsatz je m² Verkaufsfläche | 1.500–3.500 € | 2.389 € (nur Markt) | [Vermutung] |
| Kunden pro Tag | 200–500; Samstag 1,5–2 × Wochenschnitt | 327 (100.000 Bons ÷ 306 Tage) | [Vermutung]; trinkgut-Ableitung ≈ 360/Tag bei 25 € Bon |
| Ø Bon brutto (ohne Pfand) | 20–30 € | ≈ 25,50 € (netto 21,50 €) | [Vermutung] |
| Mitarbeiter | 8–15 Köpfe, davon 30–40 % Vollzeit, 40–50 % Minijob | 14 Köpfe / 8,1 Vollzeitäquivalente (VZÄ) | [wahrscheinlich] trinkgut Köngen: 10 Mitarbeiter auf 740 m² |
| Öffnungszeiten | Mo–Sa 8/9–19/20 Uhr | Mo–Sa 8–20 Uhr (72 h/Woche), 306 Öffnungstage 2027 | [sicher] Beispiele trinkgut; Tage per Kalender geprüft |
| Parkplätze | 25–100+ | 60 | [sicher] Beispiele |

Wochentagsindex (Anteil am Wochenumsatz): Mo 13 %, Di 13 %, Mi 14 %, Do 16 %, Fr 20 %, Sa 24 % [Vermutung].

---

## 3. Sortiment und Warengruppen

### 3.1 Warengruppen-Parameter

| Warengruppe | Umsatzanteil Fachmarkt | Rohertrag (RE) I in % vom Nettoumsatz | Aktionsintensität | Preiselastizität Marke / Kategorie | MHD | USt |
|---|---|---|---|---|---|---|
| Bier (inkl. Mischgetränke, alkoholfrei) | 30–40 % | 15–25 % (Fernsehbiere in Aktion 0–10 %) | sehr hoch: ≈ 70 % des Absatzes großer Pilsmarken in Aktion, Kasten Pils teils 80 % | −2,5 bis −4 / −0,3 bis −0,6 | 6–12 Monate, unfiltriert 3–6 | 19 % |
| Mineralwasser | 12–18 % | 25–32 % | mittel | −1,0 / −0,3 | Glas 12–24, PET 9–12 Monate | 19 % |
| Erfrischungsgetränke/Schorlen/Eistee | 15–20 % | 25–32 % (Cola in Aktion < 10 %) | hoch bei Markencola | −2 / −0,5 | 6–12 Monate | 19 % |
| Energydrinks | 2–5 % | 25–32 % (Einzeldose gekühlt höher) | mittel | −1,5 | 12–18 Monate | 19 % |
| Säfte/Nektare | 4–7 % | 28–35 % | gering | −1,0 | 12–18 Monate | 19 % |
| Wein/Sekt | 7–12 % | 30–40 % (Sekt in Aktion ≈ 12 %) | Sekt saisonal sehr hoch | −1,5 | Wein ohne MHD-Pflicht | 19 % |
| Spirituosen | 6–10 % | 18–28 % | mittel (Feiertage) | −2 | keines (> 10 % Vol.) | 19 % |
| Snacks, Grillbedarf, Eis, Non-Food | 4–8 % | 35–45 % | gering | −0,8 | variabel | 7 % Lebensmittel / 19 % Non-Food |
| Milchmischgetränke (≥ 75 % Milch) | 0,5–2 % | 28–33 % | gering | −1 | 3–9 Monate | 7 % |

Stufen: Aktionsanteile [sicher] (NIQ-Analyse 2025, dpa 14.6.2026). MHD-Befreiung für Wein und Getränke > 10 % Vol. [sicher] (Lebensmittelinformationsverordnung, LMIV). Alle Anteile, Spannen und Elastizitäten [Vermutung].

**Marke vs. Handelsmarke:** Bei Bier und Wasser zählen Marken und regionale Herkunft. Handelsmarken der Fachhändler sind vor allem Hauswein, Saft und Einweg-Wasser über Verbund-Eigenmarken. Sie liegen 5–15 Prozentpunkte über der Spanne der Markenware [Vermutung]. Discounter füllen Einweg-Wasser und -Softdrinks teils selbst ab und profitieren so selbst vom Einweg-Pfandschlupf [wahrscheinlich].

**Preisaktionen (Lockvogel-Kiste):** Zum WM-Start 2026 gab es nationale Pilsmarken für 9,99 € je Kasten, Beck's (AB InBev) „dauerhaft aggressiv“ ebenfalls 9,99 € [sicher]. Für 2025/26 nennt die Presse 10,50 € als typischen Aktionspreis großer Pilsmarken [sicher]. Krombacher und Veltins haben ihre Preise im Oktober 2025 erhöht, Radeberger zum 1.1.2026 (Fass und Teile des Mehrwegsortiments); in der Diskussion war ≈ +1 € je Kasten im Normalpreis [sicher]. Die Aktion lohnt sich nur mit einem Aktions-EK oder Werbekostenzuschuss (WKZ) der Brauerei (Rechenbeispiel in 5.2).

**Modell für Preis- und Aktionswirkung** (Spielparameter, [Vermutung]):
`Absatz_i = Basis_i × Saison × Wochentag × Wetter × (P_i/P_ref)^ε_i × Aktionslift × Event × Wettbewerb`
- Aktionslift Marken-Pils bei −35 % Preis: × 3 bis × 5 in der Aktionswoche. Davon sind 50–70 % Kannibalisierung anderer Biere. In den 2 Folgewochen −15 bis −25 %, weil Kunden vorgekauft haben.
- Wechselt die Konkurrenz in die Aktion und der eigene Markt nicht: Markenabsatz −30 bis −50 % in der Woche.

---

## 4. Pfand- und Leergutsystem

### 4.1 Pfandsätze (brutto, inkl. USt)

| Gebinde | Pfand | Stufe |
|---|---|---|
| Mehrweg-Bierflasche Glas (Euro-/NRW-Flasche, Longneck) | 0,08 € | [sicher] |
| Bügelverschlussflasche | 0,15 € | [sicher] |
| Mehrweg Wasser/Erfrischungsgetränke Glas oder PET | 0,15 € (selten 0,25 €) | [sicher] |
| Getränkekasten | 1,50 € (seit Jahrzehnten unverändert) | [wahrscheinlich]; bestätigt durch Österreich-Vergleich: 20er-Kasten dort 3,90 € höher = 20 × 0,12 + 1,50 |
| Kasten 20 × 0,5 Bier komplett | 20 × 0,08 + 1,50 = 3,10 € | abgeleitet |
| Kasten 24 × 0,33 Bier | 24 × 0,08 + 1,50 = 3,42 € | abgeleitet |
| Kasten 12 × 0,7/1,0 Wasser | 12 × 0,15 + 1,50 = 3,30 € | abgeleitet |
| Einweg (Dose, PET, inkl. Milchgetränke seit 1.1.2024) | 0,25 € je Gebinde, „einschließlich Umsatzsteuer“ | [sicher] IHK-Merkblatt/VerpackG |
| Fass 30/50 l | 30 € | [Vermutung] (Spanne 30–50 €) |
| Euro-/Brunnenpalette (Tausch oder Pfand) | 8–15 € | [Vermutung] |

**Pfanddebatte:** Der Brauer-Bund lehnt eine Erhöhung ab. Kosten für die Brauer: ≈ 280 Mio. € bei 0,15 € und ≈ 680 Mio. € bei 0,25 € auf ≈ 4 Mrd. Mehrweg-Bierflaschen, weil umlaufende Flaschen höher erstattet als vereinnahmt würden [sicher]. Riegele fordert 10 € pro 20er-Kasten [sicher]. Österreich hat zum 2.2.2025 von 0,09 € auf 0,20 € erhöht. Das führt zu Pfandtourismus an der bayerischen Grenze [sicher]. In Deutschland ist bis Oktober 2026 keine Änderung beschlossen [wahrscheinlich].

### 4.2 Prozess und Aufwand

1. **Rücknahme:** Automat für Einweg (zählt, presst), Kasten- oder Flaschenautomat für Mehrweg, manuelle Annahme von Sondergebinden. Der Kunde erhält einen Leergutbon und löst ihn an der Kasse ein. Das bucht die Kasse als Pfandrücknahme (Erlösminderung) [sicher als Praxis].
2. **Sortierung:** Fremdkästen und gemischte Kästen werden nach Abfüller bzw. Pool sortiert. Poolflaschen (z. B. die GDB-Brunnenflasche) kann man jedem Poolabfüller zurückgeben. Individualflaschen gehören einer Brauerei und gehen nur an diese zurück [wahrscheinlich].
3. **Leergutlager:** Lagerung nach Lieferant auf Paletten, 40–60 Kästen pro Palette, 1,5–2 m² pro Stellplatz inkl. Gang [Vermutung].
4. **Rückführung:** Der Lieferant tauscht „voll gegen leer“. Die Gutschrift läuft über das Leergutkonto beim Lieferanten (Saldo pro Gebindeart). Bei Differenzen reklamiert der Markt binnen x Tagen [wahrscheinlich].
5. **Einweg-Clearing:** Der Markt erhält das Pfand vom Erstinverkehrbringer über einen Clearing- bzw. Zählstellendienstleister im DPG-System. Ein gesetzliches Handling-Entgelt wie in Österreich (≈ 2,6–4 ct je Gebinde) gibt es in Deutschland nicht. Die Vergütung wird privat vereinbart, Erlöse aus dem Material verbleiben teils beim Händler [wahrscheinlich].
6. **Pfandschlupf:** Pfand für nie zurückgegebene Gebinde. Bei Mehrweg bleibt er beim Abfüller bzw. Pool, bei Einweg beim Erstinverkehrbringer. Der Händler hat praktisch keinen Schlupf. Er trägt aber das Risiko aus **Fremdleergut**: Gebinde, die sein Lieferant nicht zurücknimmt [wahrscheinlich].

**Mengen und Aufwand im Beispielmarkt** [Vermutung, aus 12 abgeleitet]: ≈ 175.000 Kästen-Äquivalente Leergut pro Jahr, also ≈ 570 pro Öffnungstag (Samstag bis 1.000). Bei 20 s Handhabung je Kasten (Annahme bis Palette) sind das ≈ 970 Personalstunden pro Jahr bzw. 0,56 VZÄ ≈ 23.000 € Personalkosten. Dazu kommen 10.800 € für Leasing und Wartung der Automaten und ≈ 90 m² Leergutfläche ≈ 9.500 € Miete und Nebenkosten (90 m² × 8,80 € × 12). Leergut kostet damit ≈ 43.000 € oder 1,7 % vom Umsatz, ohne eigene Erlöse.

### 4.3 Buchhaltung, Umsatzsteuer, Bilanz

- **Umsatzsteuer:** Pfand ist Teil des Entgelts und folgt dem Steuersatz der Ware: Bier 19 %, Milchmischgetränk 7 % [sicher laut IHK und Fachpresse]. Die Rückgabe mindert das Entgelt (§ 17 UStG) [wahrscheinlich, UStAE 10.1 nicht geprüft]. Lernfalle: Der Leergutbon eines Automaten fasst Gebinde mit 19 % und 7 % zusammen. Die Kasse muss nach Steuersatz trennen [Vermutung als Praxisproblem]. Ein BMF-Entwurf trennte Warenumschließungen (Flasche, Kasten) von Transporthilfsmitteln (Palette = eigene Leistung). Ob er in Kraft ist, wurde nicht geprüft [Vermutung].
- **Bilanz des Händlers** (vereinfachtes Spielmodell, [wahrscheinlich]):
  - Aktiva: „Leergut, Pfandgut und Paletten“ zum Netto-Pfandwert (Pfandanteil im Vollgutbestand plus Leergut im Lager) sowie „Pfandforderungen an Lieferanten“ (zurückgegeben, noch nicht gutgeschrieben).
  - Passiva: „Pfandverbindlichkeiten“ nur gegenüber bekannten Kunden: Leergutkonten von Gastronomie und Vereinen, Fasspfand, Kautionen. Für anonyme Ladenkunden entsteht keine Verbindlichkeit: Das Pfand wurde vom Kunden eingenommen und an den Lieferanten weitergereicht. Die Pfandverbindlichkeit für umlaufende Flaschen trägt der Abfüller.
- **Buchungsbeispiel** (netto, 19 %): Einkauf von 100 Kästen Pils zu 12,40 € plus 3,10 € Pfand brutto (2,61 € netto).
  Wareneingang 1.240,00 € + Pfandgut 260,50 € + Vorsteuer 285,10 € an Verbindlichkeiten L+L 1.785,60 €.
  Verkauf 1 Kasten zu 17,49 € + 3,10 €: Kasse 20,59 € an Erlös 14,70 €, Pfanderlös 2,61 € und USt 3,28 € (Rundung). Der Pfanderlös wird im Spiel mit dem Abgang des Pfandguts verrechnet.

### 4.4 Liquiditätseffekt (Lernfall)

Im Mai baut der Markt für die Saison Vollgut auf: +4.000 Kästen. Gebunden werden 4.000 × (8,50 € Ø-EK + 2,61 € Pfand) ≈ 44.400 € netto, also 52.900 € brutto inkl. Vorsteuer. Davon sind **≈ 10.400 € reines Pfandgeld**, das erst beim Abverkauf zurückfließt. Bringen Kunden im Juli mehr Leergut zurück, als sie Vollgut kaufen (Kasten-Rückstau nach Festen), zahlt der Markt Pfand aus. Das Geld liegt so lange fest, bis der Lieferant abholt (z. B. 3.000 Kästen × 3,10 € = 9.300 € an einem Wochenende). Pfand fließt im Beispiel mit ≈ 0,55–0,60 Mio. € brutto pro Jahr hinein und wieder hinaus, ≈ 23 % des Nettoumsatzes [Vermutung, Ableitung in 12.5].

### 4.5 Recht

- **Rücknahmepflicht Einweg:** Wer pfandpflichtige Einweggebinde verkauft, muss Gebinde derselben Materialart zurücknehmen. Verkaufsflächen < 200 m² müssen nur die selbst geführten Marken zurücknehmen. Am Regal muss „EINWEG“ oder „MEHRWEG“ stehen [sicher, VerpackG §§ 31, 32]. Für Mehrweg besteht keine gesetzliche Rücknahmepflicht; Fremdleergut kann der Händler ablehnen [wahrscheinlich].
- **Mehrwegangebotspflicht** (§§ 33, 34 VerpackG seit 2023): gilt für To-go-Lebensmittelverpackungen und Becher, nicht für Flaschen im Getränkehandel [sicher].
- **Pfandpflicht:** Seit 2022 gilt sie für alle Einweg-Kunststoffflaschen und Dosen, seit 1.1.2024 auch für Milchgetränke in PET [sicher]. Wein, Spirituosen und Saft in Glas sind weiter pfandfrei [wahrscheinlich].
- **EU-Verpackungsverordnung (PPWR):** gilt seit 12.8.2026 [sicher, VZ Hamburg]. Sie enthält Wiederverwendungsziele für Getränke ab 2030, nach Erinnerung ≈ 10 % [Vermutung zur Höhe]. **VerpackDG:** Regierungsentwurf 11.2.2026 (BT-Drs. 21/5346), vom Bundestag verabschiedet. Es ersetzt das VerpackG, erhält das Pfandsystem und nennt weiter 70 % Mehrwegziel (§ 44) [wahrscheinlich, Inkrafttreten nicht geprüft]. Eine Ausweitung der Mehrwegpflicht auf den ganzen Handel stand in einem früheren BMUV-Eckpunktepapier. Ob sie im Entwurf ist, ist offen [Vermutung].

---

## 5. Einkauf und Konditionen

### 5.1 Lieferantenstruktur (Spielannahme, [Vermutung])

| Lieferant | Anteil Einkauf | Bestellrhythmus | Mindestabnahme / Fracht | Zahlungsbedingung |
|---|---|---|---|---|
| 2 Großbrauereien (national) | 25 % | wöchentlich, Lkw mit 18–22 Paletten | ab 10 Paletten frei Haus, sonst 25–40 €/Palette | 10 Tage 2 % Skonto oder 30 Tage netto, Lastschrift |
| 2 Regionalbrauereien | 12 % | wöchentlich | ab 4 Paletten | 14 Tage netto |
| 2 Mineralbrunnen | 18 % | wöchentlich | ab 8 Paletten | 10 Tage 2 % |
| GFGH (Spezialitäten, Kleinmengen, Energy, Craft) | 20 % | 2–3 × pro Woche | ab 300 € Warenwert | 14 Tage netto |
| Wein- und Spirituosen-Großhandel / Verbund | 15 % | 14-tägig | ab 500 € | 30 Tage, Zentralregulierung |
| Food/Non-Food (Snacks, Kohle, Eis) | 10 % | wöchentlich bzw. saisonal | ab 250 € | 30 Tage |

Lieferzeiten 2–5 Werktage, in Engpässen (CO₂, Leergut, Hitze) bis 3 Wochen [Vermutung].

### 5.2 Konditionskaskade – Beispiel Fernsehbier-Pils, Kasten 20 × 0,5

| Stufe | €/Kasten | Kommentar |
|---|---|---|
| Listenpreis netto | 14,20 | enthält 0,94 € Biersteuer (0,1 hl × 12 °P × 0,787 €) |
| − Rechnungsrabatt 8 % | −1,14 | auf der Rechnung |
| − Mengenstaffel (≥ 10 Paletten) | −0,66 | |
| **= EK normal (Rechnung)** | **12,40** | Basis für Rohertrag I |
| − Skonto 2 % | −0,25 | Finanzierungsentscheidung |
| − Jahresbonus 2 % (rückwirkend, bei Erreichen von 12.000 Kästen) | −0,25 | Abgrenzung als Forderung zum 31.12. |
| − WKZ Handzettel 1.500 €/Jahr ÷ 12.000 Kästen | −0,13 | Gegenleistung: Werbung |
| **= Netto-netto-EK** | **11,78** | |
| Aktions-EK (Aktionsvergütung −3,80) | 8,60 | nur für vereinbarte Aktionswochen |
| VK normal 17,49 brutto → 14,70 netto | Spanne 15,6 % | |
| VK Aktion 10,99 → 9,24 netto | Spanne 6,9 % mit Aktions-EK, **−34 %** ohne | Lockvogel-Logik |

Alle Beträge [Vermutung]; Biersteuer [sicher]. Weitere Konditionsarten: Listungsgebühr für neue Artikel (z. B. 50–250 € je Artikel und Markt), Regalmiete oder Zweitplatzierungsprämie, Aktionsvergütung auf abverkaufte Menge (Abverkaufsnachweis aus dem Kassensystem!), Jahresziel-Staffeln mit Stufen (z. B. 1 % ab 90 %, 2 % ab 100 %, 3 % ab 110 % des Vorjahres), Treue- oder Exklusivboni bei Ein-Marken-Vertrag [Vermutung]. Verbundgruppen holen Zentralkonditionen und schütten sie teils als Rückvergütung aus (0,5–2 %) [Vermutung].

**Lernanker:** Rohertrag I (auf Rechnungs-EK) vs. Rohertrag II (nach nachträglichen Vergütungen). Boni und WKZ zum Jahresende abgrenzen. Rechnet sich Skonto, wenn der Kontokorrent 9 % kostet? (Skontosatz 2 % für 20 Tage früher entspricht ≈ 37 % p. a. → ja.) Leergutkonten mit Lieferanten abstimmen.

---

## 6. Logistik und Lager

| Größe | Wert / Spanne | Stufe |
|---|---|---|
| Palette Bier 20 × 0,5 | 40 Kästen (5 Lagen × 8) | [wahrscheinlich] |
| Palette Wasser 12 × 0,7 Glas | 40–60 Kästen | [Vermutung] |
| Palettenformate | Euro 1.200 × 800, Brunnenpalette 1.200 × 1.000, Halbpalette 800 × 600 | [wahrscheinlich] |
| Stellplätze im Beispiel | ≈ 200 Vollgut (Fläche und Lager) + 60 Leergut | [Vermutung] |
| Flurförderzeuge | 1 Elektro-Stapler (Leasing ≈ 350 €/Monat) + 2 Ameisen | [Vermutung] |
| Kommissionierung (Heimdienst/Gastro) | 40–80 Kästen pro Stunde | [Vermutung] |
| Bruch | 0,05–0,2 % vom Umsatz | [Vermutung] |
| Inventurdifferenz inkl. Bruch, MHD und Diebstahl | 0,3–0,8 % vom Umsatz (Beispiel 0,5 %) | [Vermutung] |
| Lagerumschlag gesamt | 10–18 × pro Jahr (Beispiel 13,7) | [Vermutung] |
| Umschlag je Warengruppe | Bier/Wasser 20–35 ×, AfG 15–25 ×, Wein 4–8 ×, Spirituosen 4–6 ×, Non-Food 3–6 × | [Vermutung] |
| Kühlung | begehbarer Kühlraum 20–40 m² (+4 bis +8 °C) für Fässer und Einzelflaschen, 6–12 Glastür-Kühlmöbel; je Möbel 2.000–4.000 kWh/Jahr | [Vermutung] |
| MHD-Regeln | FEFO bei Saft, Bier, Milchgetränken; Abschrift ab 4–6 Wochen vor MHD; Wein und Spirituosen ohne MHD | [sicher] MHD-Befreiung, Rest Vermutung |

Lernanker: Bestellmenge nach Andler (Klassiker) mit Nebenbedingungen „ganze Paletten“, „Mindestabnahme“, „Leergut-Tausch“ und „begrenzte Stellplätze“. Reichweite der Leitartikel vor der Hitzewelle. ABC/XYZ-Analyse (Bier-Leitartikel A/X, Spezialitäten C/Z).

---

## 7. Kostenstruktur (in % vom Nettoumsatz)

| Kostenart | Spanne Fachmarkt | Beispiel (2,5 Mio. €) | Treiber |
|---|---|---|---|
| Wareneinsatz netto (nach Boni, inkl. Schwund) | 68–76 % | 70,0 % | Sortiment, Aktionsanteil, Konditionen |
| Personal (inkl. Lohn des Gesellschafter-Geschäftsführers) | 11–16 % | 14,2 % | Öffnungszeiten, Leergut, Heimdienst |
| Miete | 3–6 % | 4,5 % | 6–10 €/m² Fachmarktfläche Stadtrand |
| Nebenkosten | 1–1,5 % | 1,2 % | |
| Energie | 0,7–1,5 % | 1,1 % | Kühlung; Strom für kleines Gewerbe ≈ 22–27 ct/kWh |
| Fuhrpark/Stapler | 0,5–2 % | 1,5 % | Heimdienst |
| Marketing | 0,8–1,5 % | 1,1 % | Handzettel, teils über WKZ refinanziert |
| IT/Kasse/WaWi, Zahlungsverkehr, Leergutautomaten | 0,8–1,5 % | 1,2 % | |
| Versicherung, Beratung, Sonstiges | 1–2 % | 1,8 % | |
| Abschreibungen | 0,8–1,5 % | 1,0 % | |
| **EBIT** | **0–4 %** | **2,0 %** | |

Stufen: Spannen [Vermutung]. Strompreis: BDEW-Neuabschlüsse 2026 ≈ 16,7 ct (160 MWh–20 GWh), Durchschnitt kleiner Gewerbebetriebe ≈ 25 ct [wahrscheinlich]. Die Stromsteuersenkung 2026 gilt nur für produzierendes Gewerbe, nicht für den Handel [sicher].

---

## 8. Personal

| Parameter | Wert | Stufe |
|---|---|---|
| Mindestlohn | 12,82 € (2025) → **13,90 € ab 1.1.2026** → **14,60 € ab 1.1.2027** (MiLoV5 vom 5.11.2025) | [sicher] |
| Minijob-Grenze | 556 € → **603 € (2026)** → **633 € (2027)**; Formel: Mindestlohn × 130 ÷ 3, aufgerundet | [sicher] 2026; 2027 aus Formel [sicher] |
| Midijob (Übergangsbereich) | 603,01–2.000 € (2026) | [wahrscheinlich] |
| SV-Arbeitgeberanteil 2026 | KV 7,3 % + ½ Ø-Zusatzbeitrag 2,9 % = 8,75 %; RV 9,3 %; AV 1,3 %; PV 1,8 % → **21,15 %** | [sicher] Sätze; Summe abgeleitet |
| Plus Umlagen U1/U2, Insolvenzgeld (0,15 %), Berufsgenossenschaft | ≈ +3,3 % → Faktor **1,245** auf Brutto | [Vermutung] U1 und BG je Kasse und Branche verschieden |
| Minijob-Pauschalen (gewerblich) | 15 % RV + 13 % KV + 2 % Pauschsteuer + U1 0,8 % + U2 0,22 % + Insolvenzgeld 0,15 % = 31,17 % (+ BG) → Faktor **1,32** | [sicher] Sätze laut lohn-info/lohndialog |
| Kurzfristige Beschäftigung (Saisonkraft) | max. 3 Monate oder 70 Arbeitstage pro Jahr, SV-frei | [sicher] |
| Krankenstand Einzelhandel | 7,14 % (2024, AOK Rheinland/Hamburg, Höchstwert seit 2003); DAK alle Branchen 2025: 5,4 % | [sicher] |
| Brutto-Stundenlohn Verkauf/Lager | 14,60–17,00 € (2027) | [Vermutung] |

**Schichtplanung (Spielmodell):** 72 h Öffnung pro Woche. Mindestbesetzung 2 Personen (Kasse + Leergut/Fläche), Fr/Sa 3–4, dazu Warenannahme Di und Do vormittags. Bedarf ≈ 330 Personalstunden pro Woche inkl. Heimdienst und Büro [Vermutung]. Gesetzliche Pause ab 6 h, Ruhezeit 11 h, Jugendarbeitsschutz für Azubis [sicher]. Kassierer ohne Alkoholverkaufsbefugnis: unter 18-Jährige dürfen Spirituosen nicht eigenverantwortlich abgeben [Vermutung zur Praxis].

**Lernanker Mindestlohnstufe 2027:** +5,0 % auf Mindestlohnbasis. Wer knapp darüber liegt (15,00 €), will Abstand halten. Der Minijob-Deckel steigt auf 633 €, die Stunden pro Minijobber bleiben ≈ 43,4.

---

## 9. Einflussfaktoren und Ereignisse

### 9.1 Saison und Wetter

Saisonindex Monatsumsatz (% vom Jahr) [Vermutung]: Jan 6,5 – Feb 6,5 – Mär 7,5 – Apr 8,0 – Mai 9,5 – Jun 10,0 – Jul 10,5 – Aug 10,0 – Sep 8,0 – Okt 7,5 – Nov 7,0 – Dez 9,0.

Wetter: Eine belastbare Faustregel „+x % pro Grad“ war nicht auffindbar. Belegte Datenpunkte: Bierabsatz im Juni 2024 −13,5 % trotz Heim-EM, laut Brauer-Bund wegen Regens [sicher]; August 2025 −14,8 % [sicher].
Spielformel [Vermutung]: `Wetterfaktor_WG = 1 + e_WG × max(0; Tmax − 20 °C) − r_WG × Regentag`, gedeckelt bei +60 %.
e: Wasser 0,025 · AfG 0,02 · Bier 0,015 · Eis/Grill 0,04 · Wein −0,005 · Spirituosen 0.
r (Regen am Freitag oder Samstag): Bier 0,15 · Wasser 0,08 · Grill 0,4.

### 9.2 Ereigniskatalog

| Ereignis | Wahrscheinlichkeit/Jahr | Wirkung (Spielparameter) | Beleg |
|---|---|---|---|
| Hitzewelle (≥ 28 °C, 5–10 Tage) | 60 % | Wasser +25–40 %, AfG +20–35 %, Bier +10–25 %; Lieferengpass Wasser 30 %; Kühlung +20 % Strom | [Vermutung] |
| Verregneter Sommer | 30 % | Bier −10–15 % Jun–Aug, Grill −40 % | [sicher] Datenpunkt Juni 2024; Parameter Vermutung |
| Fußball-Großturnier | 2 von 4 Jahren | Bier-Aktionsabsatz +6–10 % in den Eröffnungswochen; Snacks +19 %; Gesamtmarkt nur +0,3 %; Konkurrenz senkt Kiste auf 9,99 € | [sicher] NIQ/YouGov EM 2024, dpa WM 2026 |
| Vatertag, Pfingsten, Brückentage | jährlich | Bier +50–100 % in der Woche, Bollerwagen-Gebinde | [Vermutung] |
| Silvester/Weihnachten | jährlich | Sekt × 3–5 in KW 52, Spirituosen × 2, Wein × 2 | [Vermutung] |
| Stadt-, Schützen- oder Vereinsfest | 3–6 × | Festservice +5–15 T€; Kommissionsrückläufer 10–25 % | [Vermutung] |
| Preiserhöhung Brauerei | jährlich 1–3 Lieferanten | +0,50–1,00 €/Kasten Listen-EK; Weitergabe nur in Teilen möglich | [sicher] Herbst 2025/1.1.2026 |
| Energiepreisschock | 10 % | Strom +50–100 % für 12 Monate | [wahrscheinlich] Referenz 2022 |
| CO₂-Knappheit | 5 % | Wasser mit Kohlensäure und Teile von Bier/AfG 4–8 Wochen nur 30–60 % lieferfähig; Kunden weichen auf stilles Wasser aus | [sicher] BVE Sept. 2022: 30–40 % der üblichen Mengen |
| Kasten- oder Leergutknappheit | 5 % | Lieferung nur gegen Leergut-Tausch, Fehlmengen | [sicher] Hamsterkäufe 2022 |
| Discounter oder Konkurrent eröffnet im 2-km-Radius | 10 % | Umsatz −5–15 % dauerhaft, Wasser/AfG stärker, Frequenz −8 % | [Vermutung] |
| Lieferdienst startet in der Stadt | 10 % | Heimdienst −20–30 % | [Vermutung] |
| Mindestlohnstufe | 1.1.2027 fix | +5,0 % auf Mindestlohnbasis, Lohnabstand | [sicher] |
| Pfandreform (z. B. Flasche 0,08 → 0,15 €) | 5 % (Spieloption) | Liquidität: alte Flaschen mit höherem Satz erstattet; Rücklauf +; Pfandtourismus in Grenzregionen | [sicher] Österreich 2025; DE Vermutung |
| Cyberangriff / Ausfall Kasse und WaWi | 3 % | 1–3 Tage Umsatz −30–60 %, Notbetrieb dokumentieren, Meldung an Finanzamt prüfen | [Vermutung] |
| Einbruch / Leergutdiebstahl vom Hof | 10 % | 2–8 T€ Schaden, Selbstbehalt | [Vermutung] |
| Krankheitswelle | 30 % (Q1) | Krankenstand 7 → 12 % für 4 Wochen, Überstunden | [Vermutung], Basis AOK 7,14 % |
| Regionalbrauerei insolvent | 3 % | Artikel weg, Leergut nicht mehr erstattet (Pfandverlust!) | [Vermutung]; Brauereisterben [sicher] |
| Struktureller Biertrend | jährlich | Bier −2 bis −6 % Menge pro Jahr, alkoholfrei +5–10 % | [sicher] −2,0 % (2024 Inland), −6,0 % (2025 gesamt); Alkoholfreies Vermutung |
| Kassennachschau / Betriebsprüfung | 5 % | Strafe bei TSE- oder GoBD-Mängeln, Hinzuschätzung 1–5 % vom Umsatz | [Vermutung] |

---

## 10. Steuern und Recht mit Controlling-Bezug

**Umsatzsteuer:** Getränke grundsätzlich 19 %, auch Mineralwasser [sicher]. 7 % gelten für Milch und Milchmischgetränke mit ≥ 75 % Milchanteil sowie Leitungswasser. Pflanzendrinks und Milchgetränke mit Alkohol: 19 % [sicher]. Lebensmittel (Chips, Speiseeis) 7 % [sicher], Grillkohle 19 % [wahrscheinlich]. Pfand folgt dem Satz der Ware [sicher].

**Verbrauchsteuern** stecken im EK, und die USt fällt auch auf sie an (Steuer auf Steuer) [sicher]:

| Steuer | Satz | Pro Gebinde | Stufe |
|---|---|---|---|
| Biersteuer | 0,787 €/hl je °Plato (Regelsatz); Staffel für kleine Brauereien | 12 °P: 9,44 €/hl → 0,047 €/Flasche 0,5 l → 0,94 €/Kasten | [sicher] |
| Schaumweinsteuer | 136 €/hl | 1,02 €/Flasche 0,75 l | [wahrscheinlich] |
| Alkoholsteuer (Branntwein) | 1.303 €/hl reiner Alkohol | Wodka 0,7 l, 37,5 %: 0,2625 l r. A. × 13,03 = 3,42 € | [wahrscheinlich] |
| Alkopopsteuer | 5.550 €/hl r. A. (zusätzlich) | 0,275 l, 5,5 %: ≈ 0,84 € | [wahrscheinlich] |
| Wein | 0 € | – | [sicher] |

Alkoholfreies Bier < 0,5 % Vol. ist biersteuerfrei [sicher]. Ab 2031 zählen beim Grad Plato alle Zutaten mit, auch nach der Gärung zugesetzte [sicher].

**Jugendschutz (§ 9 JuSchG):** Bier, Wein und Sekt ab 16, Spirituosen und spirituosenhaltige Mischgetränke ab 18 Jahren. Bußgeld bis 50.000 € [sicher]. Spielmechanik: Testkäufe, Kassenabfrage „Alter geprüft“.

**Kasse:** Pflicht zu zertifizierter technischer Sicherheitseinrichtung (TSE) und Belegausgabe seit 2020 [sicher]. Kassen sind über ELSTER zu melden (§ 146a AO). Altgeräte bis 31.7.2025, Neugeräte ab 1.7.2025 binnen 1 Monat nach Anschaffung oder Außerbetriebnahme [sicher]. Kassennachschau jederzeit möglich [sicher].

**GoBD:** Vollständig, unveränderbar, zeitgerecht. Kassenbuch und Z-Bons sind kassensturzfähig zu führen [sicher]. Buchungsbelege seit 2025 noch 8 statt 10 Jahre aufbewahren (Bürokratieentlastungsgesetz IV) [wahrscheinlich].

**E-Rechnung:** Empfangspflicht seit 1.1.2025. Ausstellungspflicht ab 1.1.2027 bei Vorjahresumsatz > 800.000 €, ab 1.1.2028 für alle. Kleinbeträge ≤ 250 € sind ausgenommen [sicher]. Für das Beispiel mit 2,5 Mio. € heißt das: Ab 2027 muss jede Gastro- und Festservice-Rechnung als E-Rechnung raus.

**Ladenöffnung:** Ländersache. In vielen Ländern werktags bis 22 oder 24 Uhr, in Bayern und im Saarland restriktiver (bis 20 Uhr). Sonntags geschlossen, verkaufsoffene Sonntage nur aus Anlass [wahrscheinlich].

**Ertragsteuern GmbH:** Körperschaftsteuer 15 % + Soli = 15,825 %. Gewerbesteuer 3,5 % × Hebesatz (400 % = 14 %), zusammen 29,825 % [sicher]. Hinzurechnung: 25 % auf (Zinsen + 50 % Immobilienmiete + 20 % Leasing beweglicher Güter) über einem Freibetrag von 200.000 € [sicher]. Im Beispiel ≈ 71 T€ (7,7 + 56,7 + 6,1), also keine Hinzurechnung.

---

## 11. KPIs mit Benchmark-Spannen

| KPI | Formel | Benchmark | Beispiel | Stufe |
|---|---|---|---|---|
| Rohertragsquote I | (Umsatz − Wareneinsatz zu Rechnungs-EK) ÷ Umsatz | 24–30 % | 28,6 % | [Vermutung] |
| Rohertragsquote II | inkl. Boni, WKZ, Skonto, nach Schwund | 27–33 % | 30,0 % | [Vermutung] |
| Personalkostenquote | Personal ÷ Umsatz | 11–16 % | 14,2 % | [Vermutung] |
| Raumkostenquote | (Miete + Nebenkosten) ÷ Umsatz | 4–7 % | 5,7 % | [Vermutung] |
| EBIT-Marge | EBIT ÷ Umsatz | 0–4 % | 2,0 % | [Vermutung] |
| Lagerumschlag | Wareneinsatz ÷ Ø Bestand | 10–18 × | 13,7 × | [Vermutung] |
| Reichweite | 365 ÷ Umschlag | 20–36 Tage | 27 Tage | [Vermutung] |
| Schwundquote (Inventurdifferenz) | ÷ Umsatz | 0,3–0,8 % | 0,5 % | [Vermutung] |
| Ø Bon netto | Marktumsatz ÷ Bons | 18–28 € | 21,50 € | [Vermutung] |
| Kunden pro Tag | Bons ÷ Öffnungstage | 200–500 | 327 | [wahrscheinlich] trinkgut-Ableitung ≈ 360 |
| Flächenproduktivität | Marktumsatz ÷ m² VK | 1.500–3.500 € | 2.389 € | [Vermutung] |
| Umsatz je VZÄ | | 220–350 T€ | 308 T€ | [Vermutung] |
| Leergut-Rücklaufquote | Pfand zurück ÷ Pfand ausgegeben | 95–105 % | 98 % | [Vermutung] |
| Fremdleergutquote | nicht rückführbare Gebinde ÷ Rücknahme | 1–5 % | 2 % | [Vermutung] |
| Aktionsanteil Bier | Aktionsabsatz ÷ Absatz | 50–80 % | 75 % (Leitartikel L01) | [sicher] NIQ ≈ 70 % |
| Out-of-Stock Leitartikel | Fehltage ÷ Öffnungstage | < 2 % | – | [Vermutung] |
| Krankenquote | Ausfallstunden ÷ Sollstunden | 5–8 % | 7 % | [sicher] AOK 7,14 % |
| Forderungslaufzeit (DSO) Gastro/Fest | Forderungen ÷ Kreditumsatz × 365 | 20–40 Tage | 38 Tage | [Vermutung] |
| Break-even-Abstand | (Umsatz − BEP) ÷ Umsatz | 3–10 % | 6,0 % | [Vermutung] |

---

## 12. Beispielunternehmen (Startzustand)

Alle Werte in diesem Abschnitt sind **Annahmen** [Vermutung]. Sie sind an die Spannen aus 1–11 angelehnt und mit einem Skript auf Summen geprüft.

### 12.1 Steckbrief

**„{MARKTNAME} Getränke GmbH“**, Fachmarkt am Stadtrand einer Kreisstadt mit 45.000 Einwohnern in NRW. 900 m² Verkaufsfläche, 450 m² Lager und Leergut, 60 Parkplätze. Mo–Sa 8–20 Uhr, 306 Öffnungstage 2027. Dazu Heimdienst mit 1 Transporter und Festservice: Ausschankwagen, Kühlanhänger, 80 Garnituren. Mitglied einer Einkaufskooperation.
Inhaber und Gesellschafter-Geschäftsführer: 100 %, zugleich Marktleiter. Der Spieler übernimmt Büro, Buchhaltungsvorbereitung und Controlling (Teilzeit). **Planjahr 2027 = Spieljahr 1.** Der Plan entsteht im Oktober 2026; Mindestlohn 14,60 € und Minijob-Grenze 633 € sind eingerechnet.

### 12.2 Eröffnungsbilanz zum 01.01.2027 (€)

| Aktiva | | Passiva | |
|---|---|---|---|
| **A. Anlagevermögen** | **156.000** | **A. Eigenkapital** | **126.000** |
| Mietereinbauten (Kühlraum, Leergutannahme), Rest-Nutzungsdauer 6 J. | 24.000 | Gezeichnetes Kapital | 25.000 |
| Betriebs- und Geschäftsausstattung (Regale, 10 Kühlmöbel, 2 Kassen), 6 J. | 96.000 | Gewinnrücklagen | 60.000 |
| Festservice-Inventar (Ausschankwagen, Kühlanhänger, Garnituren, Zapfanlagen), 6 J. | 36.000 | Gewinnvortrag | 41.000 |
| **B. Umlaufvermögen** | **291.000** | **B. Rückstellungen** | **20.000** |
| Handelswaren (Vollgut ≈ 8.000 Kästen 68 T€, Wein/Sekt/Spirituosen 42 T€, Snacks/Non-Food 10 T€, Sonstiges 8 T€) | 128.000 | Steuerrückstellungen | 9.000 |
| Leergut, Pfandgut, Paletten (Pfand im Vollgut 20,9 T€, 2.500 Kästen Leergut 6,5 T€, Einweg-Pfand 1,6 T€, 250 Paletten 5,0 T€) | 34.000 | Sonstige (Urlaub, Abschluss, Aufbewahrung) | 11.000 |
| Forderungen L+L (Gastro, Vereine, Feste) | 21.000 | **C. Verbindlichkeiten** | **305.000** |
| Pfand- und Leergutforderungen an Lieferanten | 14.000 | Bankdarlehen (4,9 %, Tilgung 30 T€/Jahr) | 140.000 |
| Sonstige VG (Bonus- und WKZ-Forderungen 2026: 24 T€; Sonstiges 3 T€) | 27.000 | Verbindlichkeiten L+L | 118.000 |
| Kasse | 7.000 | Pfandverbindlichkeiten (Leergutkonten Gastro, Fasspfand, Kautionen) | 12.000 |
| Bank | 60.000 | Sonstige Verbindlichkeiten (USt Nov./Dez., Lohnsteuer, SV) | 35.000 |
| **C. Rechnungsabgrenzung** | **4.000** | | |
| **Summe** | **451.000** | **Summe** | **451.000** |

Kennzahlen: EK-Quote 27,9 %; Anlagendeckung I 81 %, II 171 %. Liquidität 1. Grades 33 %, 2. Grades 63 %; im Nenner kurzfristige Verbindlichkeiten von 204 T€ inkl. Tilgungsrate. AfA-Plan 2027: 24.000/6 + 96.000/6 + 36.000/6 = 26.000 €; die Ersatzinvestition (Kühlmöbel, 20.000 €) erfolgt Ende Dezember und wird erst ab 2028 abgeschrieben. Für den Handel üblich, weil Ware schneller zu Geld wird als die Lieferanten fällig sind [Vermutung].

### 12.3 Plan-GuV 2027 (€)

| Position | € | % Umsatz |
|---|---|---|
| Umsatz Markt | 2.150.000 | 86,0 |
| Umsatz Heimdienst (Ware 220.000 + Liefergebühren 30.000) | 250.000 | 10,0 |
| Umsatz Festservice (Ware 70.000 + Vermietung 30.000) | 100.000 | 4,0 |
| **Umsatzerlöse netto (ohne Pfand)** | **2.500.000** | **100,0** |
| Wareneinsatz zu Rechnungs-EK | −1.784.915 | 71,4 |
| **Rohertrag I** | **715.085** | **28,6** |
| Inventurdifferenz, Bruch, MHD-Abschriften | −12.500 | 0,5 |
| Nachträgliche Konditionen (Jahresboni, WKZ, Skonto; 2,6 % des Wareneinsatzes) | +46.733 | 1,9 |
| **Rohertrag II** | **749.318** | **30,0** |
| Personalaufwand | −355.430 | 14,2 |
| Sachaufwand (Details in 12.7) | −317.360 | 12,7 |
| **EBITDA** | **76.528** | **3,1** |
| Abschreibungen | −26.000 | 1,0 |
| **EBIT** | **50.528** | **2,0** |
| Zinsaufwand (Darlehen ≈ 6.500 + Kontokorrent in der Saison ≈ 1.200) | −7.700 | 0,3 |
| **EBT** | **42.828** | **1,7** |
| KSt + Soli + GewSt (29,825 %) | −12.773 | 0,5 |
| **Jahresüberschuss** | **30.055** | **1,2** |

**Rohertrag I nach Warengruppen (Markt):**

| WG | Anteil | Umsatz | RE-Quote | RE |
|---|---|---|---|---|
| Bier | 36 % | 774.000 | 20 % | 154.800 |
| Wasser | 14 % | 301.000 | 30 % | 90.300 |
| AfG | 17 % | 365.500 | 29 % | 105.995 |
| Energy | 4 % | 86.000 | 28 % | 24.080 |
| Säfte | 5 % | 107.500 | 32 % | 34.400 |
| Wein/Sekt | 9 % | 193.500 | 36 % | 69.660 |
| Spirituosen | 8 % | 172.000 | 24 % | 41.280 |
| Snacks/Non-Food | 6 % | 129.000 | 38 % | 49.020 |
| Milchgetränke | 1 % | 21.500 | 30 % | 6.450 |
| **Markt** | 100 % | **2.150.000** | **26,8 %** | **575.985** |

Heimdienst: RE 28 % auf Ware + 100 % auf Gebühren = 91.600. Festservice: 25 % auf Ware + 100 % auf Vermietung = 47.500. Zusammen ergibt das den Rohertrag I von 715.085 €.

**Plan-Cashflow 2027:** JÜ 30.055 + AfA 26.000 = 56.055 − Tilgung 30.000 − Ersatzinvestition Kühlmöbel 20.000 = **+6.055 € Bank**. Engpass Jan–Apr: kumulierter EBIT bis −15 T€, dazu Bestandsaufbau Mai (≈ +45 T€). Ein Kontokorrentrahmen von 60 T€ ist nötig.

### 12.4 Monatsverteilung (€)

Vereinfacht ist die RE-II-Quote in allen Monaten gleich. Saisonaushilfen fallen Mai–Aug an, Sonderzahlungen im November. Energie ist im Sommer (Kühlung) und im Winter (Heizung) höher, Marketing Mai–Jul und Dezember.

| Monat | Saison | Umsatz | RE II | Personal | Sachkosten | EBITDA | AfA | EBIT | EBIT kum. |
|---|---|---|---|---|---|---|---|---|---|
| Jan | 6,5 % | 162.500 | 48.706 | 28.286 | 25.768 | −5.348 | 2.167 | −7.515 | −7.515 |
| Feb | 6,5 % | 162.500 | 48.706 | 28.286 | 25.658 | −5.238 | 2.167 | −7.405 | −14.920 |
| Mär | 7,5 % | 187.500 | 56.199 | 28.286 | 25.886 | 2.027 | 2.167 | −140 | −15.060 |
| Apr | 8,0 % | 200.000 | 59.945 | 28.286 | 26.225 | 5.434 | 2.167 | 3.267 | −11.793 |
| Mai | 9,5 % | 237.500 | 71.185 | 31.161 | 27.236 | 12.788 | 2.167 | 10.621 | −1.172 |
| Jun | 10,0 % | 250.000 | 74.932 | 31.161 | 27.458 | 16.313 | 2.167 | 14.146 | 12.974 |
| Jul | 10,5 % | 262.500 | 78.678 | 31.161 | 27.454 | 20.063 | 2.167 | 17.896 | 30.870 |
| Aug | 10,0 % | 250.000 | 74.932 | 31.161 | 26.893 | 16.878 | 2.167 | 14.711 | 45.581 |
| Sep | 8,0 % | 200.000 | 59.945 | 28.286 | 25.886 | 5.773 | 2.167 | 3.606 | 49.187 |
| Okt | 7,5 % | 187.500 | 56.199 | 28.286 | 25.775 | 2.138 | 2.167 | −29 | 49.158 |
| Nov | 7,0 % | 175.000 | 52.452 | 32.786 | 26.000 | −6.334 | 2.167 | −8.501 | 40.657 |
| Dez | 9,0 % | 225.000 | 67.439 | 28.284 | 27.121 | 12.034 | 2.163 | 9.871 | 50.528 |
| **Summe** | 100 % | **2.500.000** | **749.318** | **355.430** | **317.360** | **76.528** | **26.000** | **50.528** | |

Hinweis für Version 2 des Spiels: Im Dezember steigt die Rohertragsquote (mehr Wein und Spirituosen), im Juni sinkt sie (Bier-Aktionen). Ein Warengruppen-Mix je Monat macht die Verteilung realistischer.

### 12.5 Leitartikel (24 Artikel, Preise 2027)

VK = Verkaufspreis brutto inkl. USt ohne Pfand; EK = netto nach Rechnungsrabatt; Akt.-Anteil = Anteil des Absatzes zum Aktionspreis; MW/EW = Mehrweg/Einweg.

| ID | Artikel | Pfand € | VK normal | VK Aktion | Akt.-Anteil | EK normal | EK Aktion | Absatz/Jahr | Umsatz netto € | RE % |
|---|---|---|---|---|---|---|---|---|---|---|
| L01 | Fernsehbier-Pils A 20 × 0,5 MW | 3,10 | 17,49 | 10,99 | 75 % | 12,40 | 8,60 | 12.000 | 127.210 | 9,9 |
| L02 | Regionales Pils/Helles 20 × 0,5 MW | 3,10 | 15,99 | 13,99 | 20 % | 10,40 | 9,90 | 7.000 | 91.706 | 21,4 |
| L03 | Premium-Pils B 24 × 0,33 MW | 3,42 | 17,99 | 12,99 | 60 % | 12,60 | 9,90 | 4.000 | 50.387 | 12,8 |
| L04 | Hefeweizen 20 × 0,5 MW | 3,10 | 18,99 | 14,99 | 40 % | 12,30 | 10,60 | 3.000 | 43.840 | 20,5 |
| L05 | Pils alkoholfrei 20 × 0,5 MW | 3,10 | 16,99 | 12,99 | 50 % | 11,30 | 9,40 | 2.500 | 31.492 | 17,8 |
| L06 | Radler 20 × 0,5 MW | 3,10 | 15,99 | 12,99 | 40 % | 10,70 | 9,40 | 2.000 | 24.857 | 18,1 |
| L07 | Dosenpils 24 × 0,5 EW | 6,00 | 13,99 | – | 0 % | 9,60 | – | 1.200 | 14.108 | 18,3 |
| L08 | Partyfass Pils 30 l (Festservice) | 30,00 | 119,00 | – | 0 % | 78,00 | – | 250 | 25.000 | 22,0 |
| L09 | Regionales Mineralwasser 12 × 0,7 Glas MW | 3,30 | 5,99 | 4,99 | 30 % | 3,50 | 3,20 | 20.000 | 95.630 | 28,7 |
| L10 | Markenwasser 12 × 1,0 PET-MW | 3,30 | 7,99 | 5,99 | 40 % | 4,90 | 4,10 | 8.000 | 48.336 | 24,2 |
| L11 | Wasser 6 × 1,5 PET EW | 1,50 | 2,49 | – | 0 % | 1,45 | – | 6.000 | 12.555 | 30,7 |
| L12 | Cola 12 × 1,0 PET-MW | 3,30 | 13,99 | 9,99 | 55 % | 9,40 | 7,60 | 6.000 | 59.445 | 15,1 |
| L13 | Regionale Limonade 12 × 0,7 Glas MW | 3,30 | 8,49 | 6,99 | 25 % | 4,90 | 4,40 | 5.000 | 34.097 | 30,0 |
| L14 | Apfelschorle 12 × 1,0 PET-MW | 3,30 | 8,99 | 6,99 | 30 % | 5,30 | 4,60 | 4.000 | 28.202 | 27,8 |
| L15 | Energydrink 24 × 0,25 Dose EW | 6,00 | 32,99 | 24,99 | 40 % | 21,60 | 17,90 | 1.000 | 25.034 | 19,6 |
| L16 | Orangensaft 6 × 1,0 Glas MW | 2,40 | 11,99 | 9,99 | 25 % | 6,90 | 6,30 | 2.000 | 19.311 | 30,1 |
| L17 | Sekt 0,75 Marke | – | 5,49 | 3,99 | 50 % | 3,40 | 2,95 | 7.000 | 27.882 | 20,3 |
| L18 | Hauswein 0,75 (Eigenmarke Verbund) | – | 5,99 | – | 0 % | 3,05 | – | 5.000 | 25.168 | 39,4 |
| L19 | Wodka 0,7 l 37,5 % | – | 10,99 | 8,99 | 50 % | 7,40 | 6,60 | 3.000 | 25.185 | 16,6 |
| L20 | Kräuterlikör 0,7 l 35 % | – | 16,99 | 13,99 | 40 % | 11,10 | 10,00 | 1.800 | 23.884 | 19,7 |
| L21 | Grillkohle 10 kg (19 %) | – | 9,99 | – | 0 % | 5,10 | – | 1.500 | 12.592 | 39,2 |
| L22 | Kartoffelchips 175 g (7 %) | – | 1,99 | 1,49 | 30 % | 1,10 | 0,95 | 6.000 | 10.318 | 38,6 |
| L23 | Bierzeltgarnitur, Miete pro Wochenende | Kaution 20 | 15,00 | – | 0 % | – | – | 1.200 | 15.126 | 100 |
| L24 | Eiskaffee 0,5 PET EW (≥ 75 % Milch, 7 %) | 0,25 | 1,69 | – | 0 % | 1,05 | – | 4.000 | 6.318 | 33,5 |

**Abgleich mit den Warengruppen:** Die Leitartikel bringen 877.682 € Umsatz (35 % vom Gesamtumsatz) bei 22,5 % RE. Bier-Leitartikel liegen bei 49,6 % des Bierumsatzes und 15,7 % RE. Damit die Warengruppe auf 20 % kommt, muss das restliche Biersortiment (Spezialitäten, Craft, Kühlware) ≈ 24 % erzielen. Ebenso: AfG-Rest ≈ 32 %, Wein-Rest ≈ 38 %, Spirituosen-Rest ≈ 26 %. Diese Mischkalkulation ist der eingebaute Lerninhalt.
**Pfandvolumen:** Die Leitartikel tragen 273.230 € Pfand. Hochgerechnet auf das ganze Sortiment ≈ 0,58 Mio. € Pfand pro Jahr, ≈ 1.900 € pro Öffnungstag.

### 12.6 Personalstamm 2027

| Nr. | Rolle | Vertrag | Stundenlohn / Monatsbrutto | AG-Faktor | Kosten/Jahr € | VZÄ |
|---|---|---|---|---|---|---|
| 1 | Gesellschafter-GF und Marktleiter | beherrschend, SV-frei | 5.000 € | BG | 60.600 | 1,00 |
| 2 | Stellv. Marktleitung | Vollzeit 40 h | 3.100 € × 12 + 1.000 € Weihnachtsgeld | 1,245 | 47.559 | 1,00 |
| 3 | Verkauf/Lager (Staplerschein) | Vollzeit | 15,50 €/h + 500 € | 1,245 | 40.754 | 1,00 |
| 4 | Verkauf/Lager | Vollzeit | 15,50 €/h + 500 € | 1,245 | 40.754 | 1,00 |
| 5 | Fahrer Heimdienst/Fest (Führerschein B/BE) | Vollzeit | 16,00 €/h + 500 € | 1,245 | 42.048 | 1,00 |
| 6 | Kasse | Teilzeit 25 h | 15,00 €/h | 1,245 | 24.270 | 0,63 |
| 7 | Büro/Controlling (**Spielerrolle**) | Teilzeit 20 h | 20,00 €/h | 1,245 | 25.906 | 0,50 |
| 8 | Azubi Kaufmann/-frau im Einzelhandel, 2. Lehrjahr | Ausbildung | 1.100 € | 1,22 | 16.104 | 0,50 |
| 9–13 | 5 Minijobber (Fr/Sa, Leergut, Kasse) | Minijob | Ø 580 € ≈ 39,7 h × 14,60 € | 1,32 | 45.936 | 1,15 |
| 14 | Saisonaushilfen (2 Pers., Mai–Aug) | kurzfristig | 14,60–15,00 €/h | 1,0 | 11.500 | 0,35 |
| | **Summe** | 14 Stammköpfe + Saison | | | **355.430** | **8,12** |

### 12.7 Fixkostenblock und Break-even

| Sachkosten | €/Jahr | | Sachkosten | €/Jahr |
|---|---|---|---|---|
| Miete 1.350 m² × 7,00 € | 113.400 | | Zahlungsverkehr/Kartengebühren | 8.400 |
| Nebenkosten 1,80 €/m² | 29.160 | | Versicherungen | 7.200 |
| Energie (85 MWh × 0,26 € + Wärme 4.500) | 26.600 | | Steuerberatung/Abschluss/Lohn | 15.000 |
| Fuhrpark (2 Transporter Leasing 15.600, Kraftstoff 9.000, Steuer/Versicherung 4.200, Wartung 3.200) + Stapler 5.000 | 37.000 | | Entsorgung | 4.200 |
| Marketing (Handzettel, Social Media, Verkostungen) | 27.000 | | Instandhaltung | 8.000 |
| IT/Kasse/WaWi/TSE | 9.600 | | Büro/Telefon/Porto | 3.000 |
| Leergutautomaten (Leasing/Wartung) | 10.800 | | Verbundbeitrag 6.000 · Sonstiges 9.000 · Pfanddifferenzen 3.000 | 18.000 |
| | | | **Summe Sachkosten** | **317.360** |

Variable Kosten außer Ware: Saisonaushilfen 11.500, Kartengebühren 8.400, Kraftstoff 9.000, Pfanddifferenzen 3.000 = 31.900 € (1,28 %).
**Deckungsbeitragsquote** = 29,97 % − 1,28 % = **28,70 %**.
**Fixkosten** inkl. AfA und Zinsen = **674.590 €**.
**Break-even-Umsatz = 2.350.735 €**. Der Sicherheitsabstand beträgt nur **6,0 %**: Ein Konkurrent, der 6 % Umsatz abzieht, bringt den Markt auf ein EBT von null.

**Heimdienst-Deckungsbeitrag pro Stopp** (Lernfall): ≈ 4.900 Lieferungen pro Jahr, Ø 45 € Ware netto, Ø 6,12 € Gebühr. Fahrer und Fahrzeug kosten anteilig ≈ 58 T€, also 11,80 € pro Stopp. DB = 12,60 € (28 % RE) + 6,12 € − 11,80 € = **6,92 € pro Stopp** vor Gemeinkosten. Kippt bei Ø-Bestellwert < 20 € oder kostenloser Lieferung.

### 12.8 Eingebaute Lernanlässe im Startzustand

1. **L01 ist ein Margenloch:** 12.000 Kästen erzielen nur 9,9 % RE. Ohne Aktions-EK wäre jede Aktionskiste mit −3,16 € ein Verlust. Frage für den Spieler: Frequenzbringer oder Wertvernichter? (Verbundkauf messen.)
2. **Saisonverlust Jan–Apr:** −15 T€ kumuliert. Liquiditätsplanung und Kontokorrent sind Pflicht.
3. **24 T€ Bonusforderungen** aus 2026 sind noch nicht eingegangen. Abgrenzung und Mahnwesen gegenüber Lieferanten.
4. **Pfandbindung** von ≈ 34 T€ und Fremdleergut-Verluste (3 T€) als blinde Flecken.
5. **Personalquote 14,2 %** bei Mindestlohnstufe 2027: Deckungslücke, wenn Preise nicht folgen.
6. **E-Rechnungspflicht ab 2027** (Umsatz > 800 T€) für Gastro und Festservice.
7. **Sicherheitsabstand 6 %** gegenüber einem drohenden Discounter- oder Lieferdienst-Ereignis.

---

## 13. Datenmodell-Skizze für die Simulation

- **Artikel** (EAN, WG, Gebinde, Pfandart → Pfandbetrag, USt-Satz, Verbrauchsteueranteil, EK-Konditionen, VK, MHD-Tage, Palettenfaktor, Kühlpflicht, Jugendschutzstufe 16/18).
- **Gebinde/Pfandart** (MW-Pool, MW-individuell + Eigentümer, EW-DPG, Fass, Palette).
- **Lieferant** (Konditionsstaffeln, Bonusziele, WKZ-Verträge, Bestellrhythmus, Mindestabnahme, Lieferzeit-Verteilung, Leergutkonto-Saldo, Zahlungsziel/Skonto).
- **Kunde/Segment** (Laufkunde, Stammkunde, Heimdienst, Gastro, Verein/Fest mit Kreditlimit und Leergutkonto).
- **Bestand** (Vollgut je Artikel, Leergut je Pfandart und Lieferant, Paletten, Stellplätze).
- **Mitarbeiter** (Vertragstyp, Stundenlohn, Sollstunden, Qualifikation Stapler/Kasse/Führerschein, Krankheitswahrscheinlichkeit).
- **Anlage** (AHK, Nutzungsdauer, Energiebedarf, Ausfallrisiko).
- **Kostenstelle** (Markt, Leergut, Heimdienst, Festservice, Verwaltung) als Basis für die Deckungsbeitragsrechnung.
- **Ereignis** (Auslöser, Wahrscheinlichkeit, Wirkvektor auf Absatz, EK, Kosten oder Liquidität, Dauer).
- **Buchungsjournal** (Konten nach SKR 03/04 vereinfacht, USt-Schlüssel 19/7, Pfandkonten). GuV, Bilanz und Cashflow sind daraus ableitbar, nicht frei gesetzt.

---

## 14. Quellen (abgerufen über Websuche, Oktober 2026)

- [MiLoV5 – gesetze-im-internet.de](https://www.gesetze-im-internet.de/milov5/BJNR10C0A0025.html); [IHK Hannover Mindestlohn 2026](https://www.ihk.de/hannover/hauptnavigation/recht/aktuell3/mindestlohn-steigt-zum-1-januar-2026-6790426); [IHK Magdeburg Minijob 603 €](https://www.ihk.de/magdeburg/recht/allgemeine-rechtsauskuenfte-1/arbeitsrecht-ordner/gesetze/anhebung-des-gesetzlichen-mindestlohns-4303334)
- [Haufe SV-Beitragssätze 2026](https://www.haufe.de/personal/entgelt/beitragssaetze-zur-sozialversicherung_78_493770.html); [lohn-info Minijob](https://lohn-info.de/minijobzentrale.html); [lohndialog Minijob 2026](https://www.lohndialog.de/minijob-lohnabrechnung-2026/)
- [AOK Rheinland/Hamburg Krankenstand Einzelhandel](https://www.aok.de/pp/fileadmin/bereiche/rheinland-hamburg/Dokumente/Pressemitteilungen/2025/20251218_PM_Einzelhandel.pdf)
- [Destatis Brauereien 2025](https://www.destatis.de/DE/Presse/Pressemitteilungen/Zahl-der-Woche/2026/PD26_32_p002.html); [Tageskarte Bierabsatz 2025](https://www.tageskarte.io/industrie/detail/historischer-tiefstand-beim-deutschen-bierabsatz-im-jahr-2025.html); [evangelisch.de Bierabsatz −6 %](https://www.evangelisch.de/inhalte/252451/02-02-2026/absatz-von-bier-sinkt-um-sechs-prozent)
- [Biersteuer – service.bremen.de](https://www.service.bremen.de/dienstleistungen/biersteuer-bezahlen-176154); [§ 2 BierStG – buzer](https://www.buzer.de/2_BierStG.htm)
- [Lebensmittelpraxis VDGE H1 2025](https://lebensmittelpraxis.de/handel-aktuell/45559-getraenkebranche-getraenke-einzelhandel-steigert-umsatz-leicht.html); [LZ VDGE-Bilanz 2025](https://www.lebensmittelzeitung.net/handel/nachrichten/vdge-bilanz-getraenkefachhandel-trotz-minus-zufrieden-189684); [LP Filialen als Umsatzgarant](https://lebensmittelpraxis.de/handel-aktuell/39527-getraenkefachmaerkte-filialen-als-umsatzgarant.html); [LP Sterben der kleinen Getränkehändler](https://lebensmittelpraxis.de/handel-aktuell/30762-getraenkeabholmaerkte-das-sterben-der-kleinen-getraenkehaendler.html); [Statista Getränkefachmärkte](https://de.statista.com/statistik/daten/studie/479562/umfrage/getraenkefachmaerkte-in-deutschland-nach-regionen); [Mintel Getränkehandel](https://store.mintel.com/de/reports/deutschland-getraenkehandel-markt-report)
- [Edeka trinkgut 2024](https://verbund.edeka/verbund/rr/presse/2024-04_trinkgut.pdf); [trinkgut Köngen](https://verbund.edeka/verbunds-website/regionsseiten_ez/sw/presse/pressemitteilungen/2025_10_21_trinkgut_köngen.pdf); [trinkgut Neunkirchen](https://verbund.edeka/verbunds-website/regionsseiten_ez/sw/presse/pressemitteilungen/2026_03_13_neu_trinkgut-kohler_neunkirchen.pdf); [trinkgut Wolfskehlen](https://verbund.edeka/verbunds-website/regionsseiten_ez/sw/presse/pressemitteilungen/2026_06_11_trinkgut-winkler_wolfskehlen.pdf); [Marktkauf Getränkemarkt](https://verbund.edeka/verbund/rr/presse/2021-09-27_pressemitteilung_marktkauf-getränkemarkt-eröffnet-mit-noch-mehr-sortimentsvielfalt.pdf)
- [Meininger Hoffmann/Heidebrecht](https://www.meininger.de/handel/getraenke-einzelhandel-geh/hoffmann-erweitert-filialnetz-dank-heidebrecht); [Getränke Hoffmann Stellenanzeige](https://www.getraenke-hoffmann.de/sites/default/files/2022-10/Verkauf_Hof.pdf); [Fristo AWM 04/2026](https://www.sigridleger.de/wp-content/uploads/2026/08/AWM_04_2026_Fristo.pdf); [LP Get N Gruppe](https://lebensmittelpraxis.de/handel-aktuell/43438-getraenkehandel-get-n-gruppe-erzielt-2-1-milliarden-euro-umsatz.html)
- [Meininger Oetker/flaschenpost 2025](https://www.meininger.de/bier/brauereien/oetker-gruppe-steigert-umsatz-erneut); [LP Oetker 7,1 Mrd.](https://lebensmittelpraxis.de/industrie-aktuell/48732-nahrungsmittelkonzern-oetker-gruppe-steigert-umsatz-auf-7-milliarden-euro.html)
- [echo24 Pfandübersicht](https://www.echo24.de/leben/verbraucher/produkte-tabelle-pfand-regeln-uebersicht-milch-kakao-kaffee-zr-92762064.html); [Bayerischer Landtag Pfand](https://www.bayern.landtag.de/www/ElanTextAblage_WP18/Drucksachen/Basisdrucksachen/0000011000/0000011494.pdf); [Tageskarte Mehrwegdebatte](https://www.tageskarte.io/industrie/detail/debatte-ueber-mehrwegsystem-in-der-brauwirtschaft.html); [LP Pfandtourismus](https://lebensmittelpraxis.de/industrie-aktuell/43228-pfandtourismus-an-grenze-hoeheres-bierpfand-in-oesterreich-belastet-deutsche-brauereien.html); [IHK Merkblatt Pfandpflicht](https://www.ihk.de/blueprint/servlet/resource/blob/5350772/508e0907cceb4da2915d85028de4ba92/merkblatt-pfandpflicht-data.pdf); [WKO Handling Fee AT](https://www.recycling-pfand.at/downloads/handling-fee-information.pdf)
- [UBA Mehrwegquote](https://www.umweltbundesamt.de/themen/mehrwegquote-bei-getraenken-verfehlt-gesetzliches-0); [VZ Hamburg PPWR](https://www.vzhh.de/print/pdf/node/6033); [ZDH VerpackDG](https://www.zdh.de/fachbereiche/wirtschaft-energie-umwelt/umweltpolitik-nachhaltigkeit/das-neue-verpackungsgesetz/); [PRO MEHRWEG Stellungnahme](https://www.bundestag.de/resource/blob/1173970/Stellungnahme-PRO-MEHRWEG.pdf); [Meininger Getränkeverpackungen](https://www.meininger.de/getraenke/getraenkeverpackungen)
- [Tageskarte USt Milch](https://www.tageskarte.io/gastronomie/detail/umsatzsteuer-bei-milch-milchmischgetraenken-sowie-leitungswasser-in-der-gastronomie.html); [IHK Bonn Kassenmeldepflicht](https://ihk-bonn.de/recht-und-steuern/steuern/informationen-zur-praxis/meldepflicht-fuer-elektronische-kassensysteme-und-zertifizierte-technische-sicherheitseinrichtungen-tse-ab-juli-2025); [IHK Magdeburg E-Rechnung](https://www.ihk.de/magdeburg/recht/allgemeine-rechtsauskuenfte-1/steuerrecht/obligatorische-e-rechnungen-ab-2025-6195316)
- [Tarifcheck Gewerbestrom](https://www.tarifcheck.de/gewerbestrom/); [Strom-Report Gewerbe](https://www.strom-report.com/strompreis-gewerbe/); [preisvergleich.de Gewerbestrom 2026](https://strom.preisvergleich.de/news/41407/industrie-gewerbestrom-2026/)
- [LP CO₂-Mangel](https://lebensmittelpraxis.de/industrie-aktuell/34878-getraenkeindustrie-deutschland-geht-die-kohlensaeure-aus.html); [LP Leergut-Knappheit](https://lebensmittelpraxis.de/industrie-aktuell/34881-brauereien-bier-hamsterkaeufe-fuehren-zu-leergut-knappheit.html)
- [dpa/boerse-online Preiserhöhungen](https://www.boerse-online.de/dpa-afx/roundup-von-bier-bis-cola-viele-getraenke-werden-teurer-477274.html); [Schwäbische 9,99-€-Kasten](https://www.schwaebische.de/wirtschaft/die-zeiten-in-denen-ein-bierkasten-noch-9-99-euro-kostet-werden-wohl-seltener-4191456); [dpa WM-Sonderangebote 2026](https://www.boerse-online.de/dpa-afx/wdh-grosse-biere-im-sonderangebot-droht-ein-schnaeppchenrausch-531530.html); [LP Preiskampf WM-Start](https://lebensmittelpraxis.de/handel-aktuell/48974-preiskampf-im-biermarkt-haendler-senken-bierpreise-zum-wm-start-auf-unter-zehn-euro-je-kasten.html); [LP YouGov WM](https://lebensmittelpraxis.de/handel-aktuell/48698-yougov-analyse-fussball-wm-treibt-den-absatz-von-chips-und-bier-aber-nicht-den-gesamtmarkt.html); [LP Bierabsatz trotz EM](https://lebensmittelpraxis.de/industrie-aktuell/42996-getraenkeindustrie-bierabsatz-in-deutschland-faellt-auf-historischen-tiefstand.html)
