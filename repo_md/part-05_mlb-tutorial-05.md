# Übung 05


## Aufgabe 1: Das Newsvendor-Problem

Ein Event-Veranstalter plant den Verkauf von T-Shirts für ein einmaliges
Open-Air-Konzert. Die Nachfrage nach den T-Shirts ist unsicher und wird
als normalverteilt mit einem Erwartungswert von 800 Stück und einer
Standardabweichung von 150 Stück geschätzt.

**Kostendaten:**

- **Einkaufspreis pro T-Shirt:** 10 GE
- **Verkaufspreis pro T-Shirt:** 25 GE
- **Rückkaufpreis (Restwert) pro nicht verkäuflichem T-Shirt:** 4 GE
  (Der Lieferant nimmt unverkäufliche Ware zurück)

**Ihre Aufgaben:**

1.  **Underage- und Overage-Kosten:** Bestimmen Sie die Underage-Kosten
    ($c_U$) und die Overage-Kosten ($c_O$).
    - $c_U$: Kosten pro Einheit, die man zu wenig bestellt hat
      (entgangener Gewinn).
    - $c_O$: Kosten pro Einheit, die man zu viel bestellt hat (Verlust
      pro übrig gebliebenem T-Shirt).
2.  **Kritisches Verhältnis:** Berechnen Sie das kritisches Verhältnis
    (Critical Ratio).
3.  **Optimale Bestellmenge:** Bestimmen Sie die optimale Bestellmenge
    ($x_{opt}$), die der Veranstalter ordern sollte, um den erwarteten
    Gewinn zu maximieren.
4.  **Sicherheitsbestand:** Wie hoch ist der resultierende
    Sicherheitsbestand?

## Aufgabe 2: Newsvendor mit diskreter Nachfrage

Ein Bäcker muss morgens entscheiden, wie viele eines speziellen Kuchens
er für den Tag backen soll. Die Herstellungskosten pro Kuchen betragen 5
GE, der Verkaufspreis liegt bei 12 GE. Nicht verkaufte Kuchen können am
Ende des Tages nicht mehr verkauft werden und haben einen Restwert von 0
GE.

Die Nachfrage nach diesem Kuchen ist erfahrungsgemäß wie folgt verteilt:

| Nachfrage (Y)           | 8 Kuchen | 9 Kuchen | 10 Kuchen | 11 Kuchen | 12 Kuchen |
|:------------------------|:--------:|:--------:|:---------:|:---------:|:---------:|
| Wahrscheinlichkeit P(Y) |   0.10   |   0.20   |   0.35    |   0.25    |   0.10    |

**Ihre Aufgaben:**

1.  **Underage- und Overage-Kosten:** Berechnen Sie die Underage-
    ($c_U$) und Overage-Kosten ($c_O$).
2.  **Kritisches Verhältnis:** Berechnen Sie das kritische Verhältnis.
3.  **Tabelle der kumulierten Wahrscheinlichkeiten:** Erstellen Sie eine
    Tabelle mit der kumulierten Wahrscheinlichkeit $F(x)$ für jede
    mögliche Bestellmenge $x$.
4.  **Optimale Bestellmenge:** Bestimmen Sie die optimale Bestellmenge
    $x_{opt}$, die der Bäcker backen sollte.

## Aufgabe 3: Periodische Lagerhaltungspolitik (r, S)

Ein Fachgeschäft für Wander-Ausrüstung verkauft einen speziellen Typ
Wanderstiefel. Die Nachfrage ist annähernd normalverteilt. Der Bestand
wird alle 4 Wochen (r=4) überprüft. Die Lieferzeit vom Hersteller
beträgt konstant 2 Wochen (L=2).

**Daten zur wöchentlichen Nachfrage:**

- **Erwartungswert ($\mu_D$):** 20 Paar
- **Standardabweichung ($\sigma_D$):** 8 Paar

Das Geschäft strebt einen $\beta$-Servicegrad von 98% an. Das bedeutet,
dass 98% der gesamten Nachfrage direkt aus dem Lager bedient werden
soll.

**Ihre Aufgaben:**

1.  **Risikozeitraum:** Bestimmen Sie den Risikozeitraum für diese
    $(r, S)$-Politik.
2.  **Nachfrageparameter:** Berechnen Sie den Erwartungswert und die
    Standardabweichung der Nachfrage während des gesamten
    Risikozeitraums.
3.  **Optimales Bestellniveau:** Bestimmen Sie das optimale
    Bestellniveau $S_{opt}$, analog zur Vorlesung.

## Aufgabe 4: Bestellpunkt-Politik (s, q) mit Undershoot

Ein Händler für Elektronikbauteile verwendet für ein bestimmtes Bauteil
eine $(s, q)$-Politik. Die tägliche Nachfrage $D$ ist normalverteilt mit
$\mu_D = 100$ und $\sigma_D = 20$. Die Wiederbeschaffungszeit beträgt
$L=5$ Tage. Es wird eine feste Bestellmenge von $q=800$ Stück verwendet.

Das Unternehmen möchte einen $\beta$-Servicegrad von 99% erreichen.

**Ihre Aufgaben:**

1.  **Undershoot:** Berechnen Sie den Erwartungswert $\mathrm{E}\{U\}$
    und die Varianz $\operatorname{Var}\{U\}$ des Undershoots. Nehmen
    Sie an, dass die Nachfrageverteilung normalverteilt ist.
2.  **Nachfrage im Risikozeitraum:** Berechnen Sie den Erwartungswert
    $\mu_Y$ und die Varianz $\sigma_Y^2$ der Nachfrage im gesamten
    Risikozeitraum ($Y = Y^{(L)} + U$).
3.  **Optimaler Bestellpunkt:** Bestimmen Sie den optimalen Bestellpunkt
    $s_{opt}$, der für den angestrebten Servicegrad nötig ist. Nehmen
    Sie an, dass der Fehlbestand am Anfang eines Zyklus vernachlässigbar
    klein ist ($G_Y^{(1)}(s+q) \approx 0$).
