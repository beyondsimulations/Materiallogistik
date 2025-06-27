# Übung 01


## Aufgabe 1: Materialbedarfsermittlung

Ein Fahrradhersteller in Münster plant die Produktion seines neuen
E-Bike-Modells “UrbanCruiser”. Die Endmontage des Fahrrads erfordert
verschiedene Komponenten, deren Beziehungen in der folgenden Stückliste
dargestellt sind.

**Struktur des “UrbanCruiser” (E):**

- 1x Rahmen-Set (R)
  - 1x Hauptrahmen (H)
  - 1x Gabel (G)
- 2x Rad (W)
- 1x Antriebs-Set (A)

**Produktionsplan:**

Der Produktionsplan (Primärbedarf) sieht vor, in Periode 10 genau 50
“UrbanCruiser” fertigzustellen.

**Stammdaten der Komponenten:**

| Komponente       | Lagerbestand | Vorlaufzeit (Perioden) |
|------------------|--------------|------------------------|
| E (UrbanCruiser) | 5            | 1                      |
| R (Rahmen-Set)   | 10           | 2                      |
| W (Rad)          | 30           | 3                      |
| A (Antriebs-Set) | 15           | 2                      |
| H (Hauptrahmen)  | 20           | 2                      |
| G (Gabel)        | 8            | 1                      |

**Ihre Aufgaben:**

1.  **Gozinto-Graph zeichnen:** Zeichnen Sie die Produktstruktur als
    Gozinto-Graph.
2.  **Materialbedarfsermittlung:** Führen Sie eine
    Materialbedarfsermittlung durch. Berechnen Sie den Brutto- und
    Nettobedarf für jede Komponente.
3.  **Bestellzeitpunkte:** Bestimmen Sie die Bestellzeitpunkte für die
    Komponenten, um den Produktionsplan einzuhalten.

## Aufgabe 2: Analyse von Bedarfsmustern

Ein Online-Shop für Kaffeebohnen möchte das Verbrauchsmuster einer
speziellen Sorte analysieren, um die Lagerhaltung zu optimieren.

Die Verkaufszahlen (in kg) der letzten 12 Wochen liegen vor:

`[5, 8, 6, 25, 7, 4, 9, 5, 30, 6, 7, 8]`

**Ihre Aufgaben:**

1.  **Grafische Darstellung:** Stellen Sie die Zeitreihe grafisch dar.
2.  **Durchschnittlicher Bedarf:** Berechnen Sie den durchschnittlichen
    wöchentlichen Bedarf.
3.  **Mittlere absolute Abweichung:** Berechnen Sie die mittlere
    absolute Abweichung (MAD), um die Prognosegüte bei Annahme eines
    konstanten Verbrauchs (Mittelwert) zu bewerten.
4.  **Störpegel:** Berechnen Sie den Störpegel (Variationskoeffizient).
5.  **Klassifizierung:** Klassifizieren Sie das Bedarfsmuster basierend
    auf Ihren Berechnungen. Handelt es sich um einen konstanten,
    trendförmigen, sporadischen oder unregelmäßigen Bedarf? Begründen
    Sie Ihre Entscheidung.

## Aufgabe 3: ABC-Analyse

Ein Unternehmen aus Duisburg möchte seine Lagerartikel klassifizieren,
um die Management-Anstrengungen zu priorisieren. Die folgenden Daten für
10 Artikel sind verfügbar:

| Artikel-Nr. | Jahresbedarf (Stück) | Preis pro Stück (€) |
|-------------|----------------------|---------------------|
| 1           | 1.000                | 50,00               |
| 2           | 500                  | 300,00              |
| 3           | 12.000               | 5,00                |
| 4           | 400                  | 450,00              |
| 5           | 8.000                | 2,00                |
| 6           | 300                  | 10,00               |
| 7           | 2.500                | 25,00               |
| 8           | 15.000               | 1,00                |
| 9           | 700                  | 150,00              |
| 10          | 5.000                | 8,00                |

**Ihre Aufgaben:**

1.  **Jährlichen Verbrauchswert berechnen:** Berechnen Sie für jeden
    Artikel den jährlichen Verbrauchswert.
2.  **Rangliste erstellen:** Erstellen Sie eine Rangliste der Artikel
    nach ihrem Verbrauchswert in absteigender Reihenfolge.
3.  **Prozentuale Anteile berechnen:** Berechnen Sie den prozentualen
    Anteil jedes Artikels am Gesamtverbrauchswert und an der Gesamtmenge
    aller Artikel.
4.  **Kumulierte Anteile berechnen:** Berechnen Sie die kumulierten
    prozentualen Anteile am Wert und an der Menge.
5.  **ABC-Klassifizierung:** Teilen Sie die Artikel in die Klassen A, B
    und C ein. Verwenden Sie typische Grenzen (z.B. A-Güter: ~80%
    Wertanteil, B-Güter: ~15% Wertanteil, C-Güter: ~5% Wertanteil).
6.  **Grafische Darstellung:** Stellen Sie das Ergebnis grafisch in
    einem Diagramm dar (Lorenz-Kurve).
