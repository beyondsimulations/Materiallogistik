# Übung 03


## Aufgabe 1: Planung mit Rüstzustandsübernahme (PLSP)

Ein Hersteller von Spezialgetrieben fertigt auf einer CNC-Maschine zwei
verschiedene Getriebetypen: Typ A und Typ B. Die Maschine kann pro Woche
nur für einen Typ eingerichtet sein, aber der Rüstzustand kann in die
Folgewoche übernommen werden, wenn derselbe Typ weiterproduziert wird.
Ein Rüstvorgang ist nur dann nötig, wenn von einem Typ zum anderen
gewechselt wird oder nach einer Woche ohne Produktion neu gestartet
wird.

**Gegebene Daten:**

- **Planungshorizont:** 4 Wochen
- **Wöchentliche Kapazität:** 60 Stunden

**Produktdaten:**

| Parameter             | Getriebe Typ A | Getriebe Typ B |
|:----------------------|:---------------|:---------------|
| Rüstkosten (s)        | 200 GE         | 150 GE         |
| Lagerkosten (h)       | 5 GE/Stück     | 7 GE/Stück     |
| Bearbeitungszeit (tb) | 1,0 h/Stück    | 1,2 h/Stück    |
| Rüstzeit (tr)         | 10 h           | 8 h            |

**Nachfrage:**

| Woche (t)    |  1  |  2  |  3  |  4  |
|:-------------|:---:|:---:|:---:|:---:|
| Bedarf Typ A | 20  | 55  |  0  |  0  |
| Bedarf Typ B |  0  |  0  | 35  | 20  |

**Vorgegebener Produktionsplan:**

Um das Konzept zu verstehen, analysieren Sie den folgenden, manuell
erstellten Produktionsplan:

- **Woche 1:** Produziere 50 $\times$ Typ A.
- **Woche 2:** Produziere 25 $\times$ Typ A.
- **Woche 3:** Produziere 55 $\times$ Typ B.
- **Woche 4:** Keine Produktion.

**Ihre Aufgaben:**

1.  **Kostenberechnung:** Berechnen Sie die gesamten Rüst- und
    Lagerkosten für den vorgegebenen Plan. Identifizieren Sie, in
    welcher Woche Rüstkosten eingespart werden.
2.  **Kapazitätsprüfung:** Überprüfen Sie für jede Woche, ob die
    Produktions- und Rüstzeiten die verfügbare Kapazität von 60 Stunden
    einhalten.
3.  **Diskussion:** Erläutern Sie, warum die separate Anwendung des
    Wagner-Whitin-Algorithmus für jedes Produkt hier wahrscheinlich zu
    einem unzulässigen oder suboptimalen Gesamtplan führen würde.

## Aufgabe 2: Echelon Stock

Ein Hersteller von Smart-Home-Geräten produziert zwei Endprodukte: eine
smarte Lampe (L1) und einen smarten Stecker (S1). Beide benötigen ein
universelles Wifi-Modul (W1). Die Lampe benötigt zusätzlich ein
spezifisches LED-Panel (P1).

**Ihre Aufgaben:**

1.  **Echelon Stock Berechnung:** Angenommen, am Ende von Woche 4 sind
    die physischen Lagerbestände wie folgt:
    `L1: 10, S1: 5, P1: 15, W1: 20`. Berechnen Sie für diesen Zeitpunkt
    den **Echelon Stock** (systemweiten Bestand) für das Wifi-Modul W1
    und das LED-Panel P1.

## Aufgabe 3: Rollierende Planung

Stellen Sie sich vor, Sie sind der Produktionsplaner. Der 6-Wochen-Plan
wurde am Anfang von Woche 1 erstellt. Sie befinden sich nun am Ende von
Woche 2. Die Produktion für die Wochen 1 und 2 wurde bereits freigegeben
und kann nicht mehr geändert werden.

**Produktdaten:**

| Artikel | Struktur             | Vorlaufzeit | Lagerbestand | Lagerkostensatz (h) |
|:--------|:---------------------|:------------|:-------------|:--------------------|
| L1      | Endprodukt           | 1           | 20           | 10 GE               |
| S1      | Endprodukt           | 1           | 50           | 8 GE                |
| P1      | Benötigt für L1      | 2           | 30           | 4 GE                |
| W1      | Benötigt für L1 & S1 | 3           | 100          | 5 GE                |

**Primärbedarf:**

| Woche     |  1  |  2  |  3  |  4  |  5  |  6  |
|:----------|:---:|:---:|:---:|:---:|:---:|:---:|
| Bedarf L1 |  0  | 40  |  0  | 60  |  0  | 50  |
| Bedarf S1 | 30  |  0  | 80  |  0  | 70  |  0  |

Für die kommende Neuplanung (beginnend in Woche 3 für die nächsten 6
Wochen) erhalten Sie aktualisierte Bedarfszahlen: Der Bedarf für die
smarte Lampe (L1) in Woche 6 ist unerwartet von 50 auf 80 gestiegen.

**Ihre Aufgaben:**

Beantworten Sie die folgenden konzeptionellen Fragen:

1.  **Eingefrorener Plan:** Welcher Teil des ursprünglichen
    Produktionsplans für die Komponenten (Ihre Bestellungen aus
    Aufgabe 2) ist nun mindestens “eingefroren” und muss als gegeben
    hingenommen werden?
2.  **Planungsinstabilität:** Erklären Sie, warum der ursprüngliche Plan
    für die Wochen 3-6 wahrscheinlich nicht mehr optimal ist, selbst
    wenn sich nur ein einziger Bedarfswert in der Zukunft geändert hat.
    Beziehen Sie sich dabei auf die Losgrößenentscheidung für das
    Wifi-Modul (W1).
3.  **Definitionen:** Überlegen Sie kurz, wie die Begriffe
    “Planungsinstabilität” und “Frozen Zone” im Kontext dieses Beispiels
    definiert werden können.

## Aufgabe 4: Analyse eines Produktionsplans

Ein Produktionsplaner hat für die Produkte “Sirius” und “Vega” einen
unvollständigen Plan hinterlassen. Beide Produkte werden auf derselben
Maschine gefertigt, die pro Woche nur für **einen** Produkttyp
eingerichtet sein kann. Ein negativer Lagerbestand ist nicht zulässig.

**Gegebene Daten:**

- Anfangslagerbestand (Ende Woche 0) für beide Produkte ist 0.
- Produkt Sirius: Rüstkosten $s_S$ = 250 GE, Lagerkostensatz $h_S$ = 4
  GE/Stück/Woche.
- Produkt Vega: Rüstkosten $s_V$ = 200 GE, Lagerkostensatz $h_V$ = 5
  GE/Stück/Woche.
- Rüstkosten fallen an, wenn die Produktion für ein Produkt in einer
  Woche stattfindet, in der zuvor ein anderes Produkt (oder nichts)
  hergestellt wurde.

**Die unvollständige Tabelle:**

| Woche (t) | Prod. Typ | Bedarf Sirius | Prod. Sirius | Lager Sirius (Ende) | Bedarf Vega | Prod. Vega | Lager Vega (Ende) | Rüstk. | Lagerk. (Summe) |
|----|----|----|----|----|----|----|----|----|----|
| 0 | \- | \- | \- | 0 | \- | \- | 0 | \- | \- |
| 1 | Sirius | 20 | 50 | **(a)** | 0 | 0 | 0 | **(b)** | **(c)** |
| 2 | Vega | 10 | 0 | **(d)** | 30 | 50 | **(e)** | 200 | 180 |
| 3 | Vega | 5 | 0 | 15 | 20 | **(f)** | 20 | **(g)** | **(h)** |
| 4 | Sirius | 30 | **(i)** | 35 | 10 | 0 | **(j)** | **(k)** | **(l)** |
| 5 | \- (Keine) | 10 | 0 | **(m)** | 5 | 0 | **(n)** | **(o)** | 125 |
| **SUMME** | \- |  |  | \- |  |  | \- | **(p)** | **(q)** |

**Ihre Aufgaben:**

1.  **Schrittweise Berechnung:** Berechnen Sie schrittweise die
    fehlenden Werte (gekennzeichnet mit Buchstaben) in der Tabelle.
    Begründen Sie Ihre Berechnungen für jede Zelle kurz.
2.  **Summe der Rüst- und Lagerkosten:** Ermitteln Sie die Summe der
    Rüstkosten und der Lagerkosten für den gesamten Planungszeitraum.
