# Übung 02


## Einleitung

Wer noch Schwierigkeiten mit dem CLSP und der Lagerbilanzgleichung hat,
kann sich gerne folgendes Video aus der Vorlesung Grundlagen des
Operations Research ansehen:

<https://www.youtube.com/embed/mJtf-RR9Dvk>

## Aufgabe 1: Exakte Losgrößenplanung für Saisonbier

Die lokale Traditionsbrauerei “Duisburger Perle” plant die Produktion
ihres beliebten Saisonbiers “Frühlings-Helles” für die kommenden 6
Wochen. Da die Nachfrage schwankt und das Aufsetzen eines neuen
Brauvorgangs (Rüsten) mit erheblichen Kosten verbunden ist, soll ein
kostenoptimaler Produktionsplan gefunden werden.

Die Brauerei hat die folgenden Daten ermittelt:

- **Rüstkosten ($s$):** 250 GE pro Brauvorgang (Los)
- **Lagerkostensatz ($h$):** 2 GE pro Kasten und Woche

**Wöchentliche Nachfrage ($d_t$):**

| Woche (t)          | 1   | 2   | 3   | 4   | 5   | 6   |
|:-------------------|:----|:----|:----|:----|:----|:----|
| Nachfrage (Kästen) | 30  | 50  | 20  | 70  | 80  | 40  |

Um die Gesamtkosten zu minimieren, soll das exakte Verfahren von
**Wagner und Whitin** (Dynamische Optimierung) angewendet werden. Es
wird angenommen, dass zu Beginn kein Lagerbestand vorhanden ist und am
Ende der 6. Woche ebenfalls kein Bestand verbleiben soll.

**Ihre Aufgaben:**

1.  **Kostenmatrix erstellen:** Berechnen Sie die Kosten $c_{\tau j}$
    für jedes mögliche Los, das in Woche $\tau$ produziert wird, um die
    Nachfrage bis einschließlich Woche $j$ zu decken.
2.  **Wagner-Whitin-Algorithmus anwenden:** Ermitteln Sie rekursiv die
    minimalen Gesamtkosten $f_i$ für einen Planungszeitraum von
    $i = 1, \ldots, 6$ Wochen. Notieren Sie sich bei jedem Schritt,
    welche Entscheidung zur minimalen Kosten führt.
3.  **Optimalen Produktionsplan ableiten:** Bestimmen Sie durch
    Rückverfolgung (Backtracking) aus den Ergebnissen von Schritt 2, in
    welchen Wochen eine Produktion stattfinden soll und wie groß die
    jeweilige Losgröße ist. Wie hoch sind die minimalen Gesamtkosten?

## Aufgabe 2: Heuristische Losgrößenplanung

Die Geschäftsführung der “Duisburger Perle” ist mit dem optimalen Plan
sehr zufrieden, findet das Wagner-Whitin-Verfahren jedoch recht
aufwändig für die schnelle, wöchentliche Planung. Ein findiger
Braumeister schlägt vor, einfachere Heuristiken zu verwenden, die
“ziemlich gute” Ergebnisse liefern, aber schneller zu berechnen sind.

Sie erhalten den Auftrag, drei gängige Heuristiken auf die Daten aus
Aufgabe 1 anzuwenden und die Ergebnisse mit der optimalen Lösung zu
vergleichen.

**Daten (wie in Aufgabe 1):**

- **Rüstkosten ($s$):** 250 GE
- **Lagerkostensatz ($h$):** 2 GE pro Kasten und Woche
- **Wöchentliche Nachfrage ($d_t$):** `[30, 50, 20, 70, 80, 40]`

**Ihre Aufgaben:**

1.  **Stückkostenverfahren (Least-Unit-Cost):** Bilden Sie Lose, indem
    Sie so lange Periodenbedarfe zusammenfassen, wie die
    durchschnittlichen Stückkosten des Loses sinken.
2.  **Stückperiodenausgleichsverfahren (Part-Period-Balancing):** Bilden
    Sie Lose, indem Sie so lange Periodenbedarfe zusammenfassen, wie die
    kumulierten Lagerkosten des Loses die Rüstkosten nicht übersteigen.
3.  **Silver-Meal-Verfahren:** Bilden Sie Lose, indem Sie so lange
    Periodenbedarfe zusammenfassen, wie die durchschnittlichen Kosten
    pro Periode sinken.
4.  **Vergleich:** Stellen Sie die Produktionspläne und Gesamtkosten der
    drei Heuristiken der optimalen Lösung aus Aufgabe 1 gegenüber. Wie
    gut schlagen sich die Heuristiken?

## Aufgabe 3: Losgrößenplanung mit Kapazitätsgrenzen (CLSP)

Die “Duisburger Perle” stellt fest, dass die Gär- und Lagertanks einen
Engpass darstellen. Es kann nicht unbegrenzt viel Bier pro Woche
produziert werden. Zusätzlich zum “Frühlings-Hellen” wird nun ein
zweites Saisonbier, das “Maibock”, geplant. Beide Biere konkurrieren um
die gleiche, begrenzte wöchentliche Kapazität.

**Neue & Gegebene Daten:**

- **Produkt 1: Frühlings-Helles** (Daten wie gehabt)
  - Nachfrage: `[30, 50, 20, 70, 80, 40]`
  - Rüstkosten $s_{helles}$: 250 GE, Lagerkosten $h_{helles}$: 2 GE
  - Kapazitätsbedarf pro Kasten $tb_{helles}$: 1,0 KE
  - Kapazitätsbedarf für Rüstvorgang $tr_{helles}$: 20 KE
- **Produkt 2: Maibock** (Neue Daten)
  - Nachfrage: `[20, 30, 60, 40, 30, 50]`
  - Rüstkosten $s_{bock}$: 200 GE, Lagerkosten $h_{bock}$: 2.5 GE
  - Kapazitätsbedarf pro Kasten $tb_{bock}$: 1,2 KE
  - Kapazitätsbedarf für Rüstvorgang $tr_{bock}$: 15 KE
- **Wöchentliche Gesamtkapazität ($b_t$):** 150 KE (Kapazitätseinheiten)

**Ihre Aufgaben:**

1.  **Unabhängige Planung:** Ermitteln Sie den kostenoptimalen,
    *unkapazitierten* Produktionsplan für das neue “Maibock”-Bier mit
    dem Wagner-Whitin-Algorithmus.
2.  **Kapazitätsprüfung:** Überlagern Sie den optimalen Plan für
    “Frühlings-Helles” (aus Aufgabe 1) mit dem neuen Plan für “Maibock”.
    Berechnen Sie für jede Woche die gesamte Kapazitätsauslastung durch
    Produktion und Rüstvorgänge beider Biersorten. Identifizieren Sie
    alle Wochen, in denen die Gesamtkapazität von 150 KE überschritten
    wird.
3.  **Heuristische Anpassung:** Schlagen Sie eine einfache, plausible
    Anpassung für den kombinierten Produktionsplan vor, um die
    Kapazitätsverletzungen zu beheben (z.B. durch Vorziehen oder
    Aufteilen einer Produktion). Berechnen Sie die neuen Gesamtkosten
    (Summe der Kosten beider Pläne) für Ihren angepassten,
    kapazitätskonformen Plan.
4.  **Diskussion:** Erläutern Sie kurz, warum das separate Anwenden des
    Wagner-Whitin-Algorithmus und anschließende Anpassen keine
    garantiert optimale Lösung für das kapazitierte Problem (CLSP)
    liefert.
