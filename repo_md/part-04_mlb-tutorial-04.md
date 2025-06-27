# Übung 04


## Aufgabe 1: Bestandsgrößen im Zeitverlauf

Ein Händler für hochwertige Espressomaschinen nutzt zur Steuerung seines
Lagers eine $(s, q)$-Politik mit kontinuierlicher Überwachung. Die
Politik ist wie folgt definiert:

- Bestellpunkt (Meldebestand) **$s$**: 80 Maschinen
- Bestellmenge **$q$**: 200 Maschinen
- Wiederbeschaffungszeit **$L$**: 2 Wochen (deterministisch)

Der Händler startet in Woche 0 mit den folgenden Beständen:

- Physischer Bestand $I_0^P$: 100 Maschinen
- Bestellbestand (offene Bestellungen) $I_0^O$: 0 Maschinen

**Wöchentliche Nachfragen (deterministisch für diese Aufgabe):**

| Woche (t)       |  1  |  2  |  3  |  4  |  5  |  6  |
|:----------------|:---:|:---:|:---:|:---:|:---:|:---:|
| Nachfrage $d_t$ | 40  | 35  | 50  | 40  | 55  | 60  |

**Ihre Aufgaben:**

1.  **Tabelle ausfüllen:** Füllen Sie die folgende Tabelle aus.
    Verfolgen Sie alle Bestandsgrößen über den Zeitraum von 6 Wochen.
    Eine Bestellung wird am Ende der Woche ausgelöst, in der der
    disponible Bestand den Meldebestand $s$ erreicht oder
    unterschreitet. Der Wareneingang erfolgt dann genau $L=2$ Wochen
    später zu Beginn der Woche.

| Woche (t) | Nachfrage $d_t$ | Disp. Bestand (Anfang) | Bestellung? (Menge) | Disp. Bestand (Ende) | Phys. Bestand (Ende) | Bestellbestand (Ende) | Fehlbestand (Ende) |
|----|----|----|----|----|----|----|----|
| **0** | \- | \- | \- | 100 | 100 | 0 | 0 |
| **1** | 40 | 100 | ? | ? | ? | ? | ? |
| **2** | 35 | ? | ? | ? | ? | ? | ? |
| **3** | 50 | ? | ? | ? | ? | ? | ? |
| **4** | 40 | ? | ? | ? | ? | ? | ? |
| **5** | 55 | ? | ? | ? | ? | ? | ? |
| **6** | 60 | ? | ? | ? | ? | ? | ? |

## Aufgabe 2: Sicherheitsbestand und Servicegrade

Ein Online-Händler für ein populäres Smartphone-Modell möchte seinen
Lagerbestand optimieren. Die wöchentliche Nachfrage ist annähernd
normalverteilt mit einem **Mittelwert von 60 Stück** und einer
**Standardabweichung von 20 Stück**. Die Wiederbeschaffungszeit vom
Hersteller beträgt konstant **3 Wochen**. Der Händler nutzt eine Politik
der kontinuierlichen Überprüfung.

**Ihre Aufgaben:**

1.  **Mittelwert und Standardabweichung:** Berechnen Sie den Mittelwert
    und die Standardabweichung der Nachfrage während der
    Wiederbeschaffungszeit (dem Risikozeitraum).
2.  **Bestellpunkt und Sicherheitsbestand:** Der Händler strebt einen
    $\alpha$-Servicegrad (Zyklus-Servicegrad) von 95% an. Das bedeutet,
    die Wahrscheinlichkeit eines Fehlbestands während eines
    Bestellzyklus soll nur 5% betragen. Welcher Bestellpunkt (reorder
    point) $s$ muss gewählt werden? Wie hoch ist der resultierende
    Sicherheitsbestand?
3.  **Erwartete Fehlmenge:** Gegeben der Bestellpunkt $s$ aus Teil 2:
    Berechnen Sie die erwartete Fehlmenge pro Bestellzyklus $E(B)$.
    Nutzen Sie dafür die in der Vorlesung vorgestellte **standardisierte
    Einheiten-Verlustfunktion $G_u(z)$**. Die benötigten Werte für
    $G_u(z)$ finden Sie in den Tabellen der Vorlesung oder in den
    Lösungshinweisen zu dieser Aufgabe.
4.  **Servicegrad:** Wenn der Händler eine feste Bestellmenge von
    $q=450$ Stück verwendet, welchen $\beta$-Servicegrad
    (Mengen-Servicegrad) erreicht er mit seiner Politik?

## Aufgabe 3: Diskrete Nachfrage und Faltung

Ein Comic-Laden verkauft eine beliebte wöchentliche Manga-Ausgabe. Die
tägliche Nachfrage ist nicht normalverteilt, sondern folgt dieser
diskreten Verteilung:

| Nachfrage (D) pro Tag   | 0 Hefte | 1 Heft | 2 Hefte | 3 Hefte |
|:------------------------|:--------|:-------|:--------|:--------|
| Wahrscheinlichkeit P(D) | 0.3     | 0.4    | 0.2     | 0.1     |

Die Wiederbeschaffungszeit beträgt genau **2 Tage**.

**Ihre Aufgaben:**

1.  **Wahrscheinlichkeitsverteilung:** Leiten Sie die
    Wahrscheinlichkeitsverteilung für die Gesamtnachfrage $Y_2$ über den
    Risikozeitraum von 2 Tagen her. (Tipp: Nutzen Sie die Faltung der
    Verteilung mit sich selbst).
2.  **Fehlbestandswahrscheinlichkeit:** Wenn der Ladenbesitzer einen
    Bestellpunkt von $s=4$ Heften festlegt, wie hoch ist die
    Wahrscheinlichkeit, dass es zu einem Fehlbestand kommt (d.h. der
    $\alpha$-Servicegrad *nicht* eingehalten wird)?
3.  **Erwartete Fehlmenge:** Berechnen Sie die erwartete Fehlmenge
    $E(B)$ für den Bestellpunkt $s=4$.
