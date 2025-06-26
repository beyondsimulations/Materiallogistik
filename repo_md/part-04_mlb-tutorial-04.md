# Übung 04


## Aufgabe 1: Bestandsgrößen im Zeitverlauf

Ein Händler für hochwertige Espressomaschinen nutzt zur Steuerung seines
Lagers eine $(s, q)$-Politik mit kontinuierlicher Überwachung. Die
Politik ist wie folgt definiert:

- Bestellpunkt (Meldebestand) **$s$**: 100 Maschinen
- Bestellmenge **$q$**: 250 Maschinen
- Wiederbeschaffungszeit **$L$**: 3 Wochen (deterministisch)

Der Händler startet in Woche 0 mit den folgenden Beständen:

- Physischer Bestand $I_0^P$: 120 Maschinen
- Bestellbestand (offene Bestellungen) $I_0^O$: 0 Maschinen

**Wöchentliche Nachfragen (deterministisch für diese Aufgabe):**

| Woche (t)       |  1  |  2  |  3  |  4  |  5  |  6  |
|:----------------|:---:|:---:|:---:|:---:|:---:|:---:|
| Nachfrage $d_t$ | 30  | 40  | 50  | 45  | 60  | 55  |

**Ihre Aufgaben:**

1.  **Tabelle ausfüllen:** Füllen Sie die folgende Tabelle aus.
    Verfolgen Sie alle Bestandsgrößen über den Zeitraum von 6 Wochen.
    Eine Bestellung wird am Ende der Woche ausgelöst, in der der
    disponible Bestand den Meldebestand $s$ erreicht oder
    unterschreitet. Der Wareneingang erfolgt dann genau $L=3$ Wochen
    später zu Beginn der Woche.

| Woche (t) | Nachfrage $d_t$ | Disp. Bestand (Anfang) | Bestellung? (Menge) | Disp. Bestand (Ende) | Phys. Bestand (Ende) | Bestellbestand (Ende) | Fehlbestand (Ende) |
|----|----|----|----|----|----|----|----|
| **0** | \- | \- | \- | 120 | 120 | 0 | 0 |
| **1** | 30 | 120 | ? | ? | ? | ? | ? |
| **2** | 40 | ? | ? | ? | ? | ? | ? |
| **3** | 50 | ? | ? | ? | ? | ? | ? |
| **4** | 45 | ? | ? | ? | ? | ? | ? |
| **5** | 60 | ? | ? | ? | ? | ? | ? |
| **6** | 55 | ? | ? | ? | ? | ? | ? |

**Lösungshinweise:**

> [!TIP]
>
> ### Tipps und wichtige Formeln
>
> #### Reihenfolge der Ereignisse
>
> Beachten Sie die korrekte Reihenfolge der Aktionen **innerhalb jeder
> Woche**:
>
> 1.  **Wareneingang:** Zu Beginn der Woche kommt eine eventuell vor
>     $L=3$ Wochen getätigte Bestellung an. Dadurch steigt der physische
>     Bestand und der Bestellbestand sinkt.
> 2.  **Nachfrage-Erfüllung:** Die Nachfrage der aktuellen Woche wird
>     bedient. Dies senkt den physischen und den disponiblen Bestand.
> 3.  **Bestellentscheidung:** Am **Ende der Woche** wird geprüft, ob
>     eine neue Bestellung ausgelöst werden muss.
>
> #### Die wichtigsten Formeln
>
> - **Disponibler Bestand ($I^D$):** Die entscheidende Größe für die
>   Bestellung. Er repräsentiert die Summe aus physischem und bestelltem
>   Bestand.
>   $I^D_t(\text{vor Bestellung}) = I^D_{t-1}(\text{Ende}) - d_t$
> - **Bestellentscheidung:** Prüfe am Ende der Woche:
>   $I^D_t(\text{vor Bestellung}) \le s$?
>   - Wenn **Ja**: Löse eine Bestellung über die Menge $q$ aus. Der
>     disponible Bestand erhöht sich ***sofort***:
>     $I^D_t(\text{Ende}) = I^D_t(\text{vor Bestellung}) + q$
>   - Wenn **Nein**: Der disponible Bestand bleibt für das Ende der
>     Woche unverändert.
> - **Physischer Bestand ($I^P$):**
>   - $I^P_t(\text{Ende}) = I^P_{t-1}(\text{Ende}) + \text{Wareneingang}_t - d_t$
>     (kann nicht negativ werden)
> - **Bestellbestand ($I^O$):**
>   - $I^O_t(\text{Ende}) = I^O_{t-1}(\text{Ende}) - \text{Wareneingang}_t + \text{Neue Bestellung}_t$

Die Logik ist wie folgt:

1.  **Disponibler Bestand (Anfang):** Ist der disponible Bestand vom
    Ende der Vorwoche.
2.  **Bestellung?:** Prüfe am Ende der Woche:
    `Disponibler Bestand (Anfang) - Nachfrage <= s?` Wenn ja, löse
    Bestellung über `q` aus.
3.  **Disponibler Bestand (Ende):**
    `Disponibler Bestand (Anfang) - Nachfrage`.
4.  **Physischer Bestand / Fehlbestand:**
    `Physischer Bestand (Anfang) + Wareneingang - Nachfrage`.
5.  **Bestellbestand:**
    `Bestellbestand (Anfang) + Neue Bestellung - Wareneingang`.

``` python
import pandas as pd

# Initialwerte
s, q, L = 100, 250, 3
demands = [30, 40, 50, 45, 60, 55]
T = len(demands)

# Tracking-Variablen
disp_bestand = 120
phys_bestand = 120
bestell_bestand = 0
fehl_bestand = 0

# Lieferungen (Woche, Menge)
lieferungen = {} 

# Tabelle für Ergebnisse
results = []

print("Berechnung Schritt für Schritt:")
for t in range(1, T + 1):
    # Zustand zu Beginn der Woche t
    disp_bestand_anfang = disp_bestand
    bestell_bestand_anfang = bestell_bestand
    
    # Wareneingang prüfen
    wareneingang = lieferungen.get(t, 0)
    if wareneingang > 0:
        print(f"Woche {t}: Wareneingang von {wareneingang} Stück.")
        bestell_bestand -= wareneingang
        phys_bestand += wareneingang
        
    # Nachfrage bedienen
    demand_t = demands[t-1]
    zu_bedienen = demand_t + fehl_bestand
    
    if phys_bestand >= zu_bedienen:
        phys_bestand -= zu_bedienen
        fehl_bestand = 0
    else:
        fehl_bestand = zu_bedienen - phys_bestand
        phys_bestand = 0
        
    disp_bestand -= demand_t
    
    # Bestellentscheidung am Ende der Woche
    bestellung_getaetigt = 0
    if disp_bestand <= s:
        print(f"Woche {t}: Meldebestand unterschritten ({disp_bestand} <= {s}). Bestellung ausgelöst.")
        bestellung_getaetigt = q
        bestell_bestand += q
        disp_bestand += q
        liefer_woche = t + L
        lieferungen[liefer_woche] = lieferungen.get(liefer_woche, 0) + q
        
    results.append({
        'Woche (t)': t,
        'Nachfrage $d_t$': demand_t,
        'Disp. Bestand (A)': disp_bestand_anfang,
        'Bestellung? (E)': bestellung_getaetigt,
        'Disp. Bestand (E)': disp_bestand,
        'Phys. Bestand (E)': phys_bestand,
        'Bestellbestand (E)': bestell_bestand,
        'Fehlbestand (E)': fehl_bestand
    })

df_results = pd.DataFrame(results)
print("\nVervollständigte Tabelle:")
print(df_results.to_string(index=False))
```

    Berechnung Schritt für Schritt:
    Woche 1: Meldebestand unterschritten (90 <= 100). Bestellung ausgelöst.
    Woche 4: Wareneingang von 250 Stück.
    Woche 6: Meldebestand unterschritten (90 <= 100). Bestellung ausgelöst.

    Vervollständigte Tabelle:
     Woche (t)  Nachfrage $d_t$  Disp. Bestand (A)  Bestellung? (E)  Disp. Bestand (E)  Phys. Bestand (E)  Bestellbestand (E)  Fehlbestand (E)
             1               30                120              250                340                 90                 250                0
             2               40                340                0                300                 50                 250                0
             3               50                300                0                250                  0                 250                0
             4               45                250                0                205                205                   0                0
             5               60                205                0                145                145                   0                0
             6               55                145              250                340                 90                 250                0

## Aufgabe 2: Sicherheitsbestand und Servicegrade

Ein Online-Händler für ein populäres Smartphone-Modell möchte seinen
Lagerbestand optimieren. Die wöchentliche Nachfrage ist annähernd
normalverteilt mit einem **Mittelwert von 50 Stück** und einer
**Standardabweichung von 15 Stück**. Die Wiederbeschaffungszeit vom
Hersteller beträgt konstant **4 Wochen**. Der Händler nutzt eine Politik
der kontinuierlichen Überprüfung.

**Ihre Aufgaben:**

1.  **Mittelwert und Standardabweichung:** Berechnen Sie den Mittelwert
    und die Standardabweichung der Nachfrage während der
    Wiederbeschaffungszeit (dem Risikozeitraum).
2.  **Bestellpunkt und Sicherheitsbestand:** Der Händler strebt einen
    $\alpha$-Servicegrad (Zyklus-Servicegrad) von 99% an. Das bedeutet,
    die Wahrscheinlichkeit eines Fehlbestands während eines
    Bestellzyklus soll nur 1% betragen. Welcher Bestellpunkt (reorder
    point) $s$ muss gewählt werden? Wie hoch ist der resultierende
    Sicherheitsbestand?
3.  **Erwartete Fehlmenge:** Gegeben der Bestellpunkt $s$ aus Teil 2:
    Berechnen Sie die erwartete Fehlmenge pro Bestellzyklus $E(B)$.
    Nutzen Sie dafür die standardisierte Einheiten-Verlustfunktion, die
    approximiert werden kann als $\phi(z) - z(1 - \Phi(z))$, wobei $z$
    der Sicherheitsfaktor ist und $\phi(z)$ bzw. $\Phi(z)$ die Dichte-
    bzw. Verteilungsfunktion der Standardnormalverteilung sind.
4.  **Servicegrad:** Wenn der Händler eine feste Bestellmenge von
    $q=500$ Stück verwendet, welchen $\beta$-Servicegrad
    (Mengen-Servicegrad) erreicht er mit seiner Politik?

**Lösungshinweise:**

> [!TIP]
>
> ### Tipps und wichtige Formeln
>
> #### 1. Nachfrage während der Wiederbeschaffungszeit (WBZ)
>
> Der Risikozeitraum ist die Wiederbeschaffungszeit $L$. Wir müssen die
> Kennzahlen der Nachfrageverteilung für diesen längeren Zeitraum
> berechnen. Für unabhängige Perioden gilt:
>
> - Erwartungswert der Nachfrage während WBZ:
>   $\mu_L = L \cdot \mu_{\text{wöchentlich}}$
> - Varianz der Nachfrage während WBZ:
>   $\sigma_L^2 = L \cdot \sigma_{\text{wöchentlich}}^2$
> - Standardabweichung der Nachfrage während WBZ:
>   $\sigma_L = \sqrt{L} \cdot \sigma_{\text{wöchentlich}}$
>
> #### 2. Bestellpunkt und Sicherheitsbestand
>
> Der Bestellpunkt $s$ deckt die erwartete Nachfrage während der WBZ ab
> und enthält zusätzlich einen Puffer für Unsicherheit.
>
> - **Bestellpunkt ($s$):** $s = \mu_L + SS$
> - **Sicherheitsbestand ($SS$):** $SS = z \cdot \sigma_L$
> - **Sicherheitsfaktor ($z$):** Dieser Wert hängt vom gewünschten
>   $\alpha$-Servicegrad (Zyklus-Servicegrad) ab und wird aus der
>   Standardnormalverteilung abgelesen:
>   - $z = \Phi^{-1}(\alpha)$, wobei $\Phi^{-1}$ die inverse kumulative
>     Verteilungsfunktion ist (auch Quantilfunktion genannt).
>
> #### 3. Erwartete Fehlmenge ($E(B)$)
>
> Dies ist die durchschnittliche Anzahl an Einheiten, die pro Zyklus
> aufgrund von zu hoher Nachfrage nicht geliefert werden können.
>
> - **Formel:** $E(B) = \sigma_L \cdot G_u(z)$
> - **Standardisierte Verlustfunktion ($G_u(z)$):**
>   $G_u(z) = \phi(z) - z(1 - \Phi(z))$
>   - $\phi(z)$: Dichtefunktion der Standardnormalverteilung.
>   - $\Phi(z)$: Kumulative Verteilungsfunktion der
>     Standardnormalverteilung. Beachten Sie, dass $1 - \Phi(z)$ genau
>     der Fehlbestandswahrscheinlichkeit $(1-\alpha)$ entspricht.
>
> #### 4. $\beta$-Servicegrad (Fill Rate)
>
> Dieser Servicegrad misst den prozentualen Anteil der Gesamtnachfrage,
> der direkt aus dem Lager bedient wird.
>
> - **Formel:** $\beta = 1 - \frac{E(B)}{q}$

``` python
import numpy as np
from scipy.stats import norm

# Gegebene Daten
mu_d_weekly = 50
sigma_d_weekly = 15
L = 4 # Wochen
q = 500

# 1. Momente der Nachfrage während der WBZ
mu_L = L * mu_d_weekly
sigma_L = np.sqrt(L) * sigma_d_weekly
print(f"1. Nachfrage während der WBZ:")
print(f"   - Erwartungswert (mu_L): {mu_L:.2f} Stück")
print(f"   - Standardabweichung (sigma_L): {sigma_L:.2f} Stück\n")

# 2. Bestellpunkt und Sicherheitsbestand für alpha-Servicegrad
alpha_target = 0.99
# Finde den z-Wert (Sicherheitsfaktor) für 99%
z = norm.ppf(alpha_target)

# Sicherheitsbestand = z * sigma_L
safety_stock = z * sigma_L
# Bestellpunkt s = mu_L + Sicherheitsbestand
s = mu_L + safety_stock

print(f"2. Bestellpunkt für alpha = {alpha_target*100}%:")
print(f"   - Benötigter z-Wert (Sicherheitsfaktor): {z:.3f}")
print(f"   - Sicherheitsbestand: {z:.3f} * {sigma_L:.2f} = {safety_stock:.2f} Stück")
print(f"   - Bestellpunkt s: {mu_L:.2f} + {safety_stock:.2f} = {s:.2f} Stück (gerundet: {np.ceil(s)})")
print(f"   -> Der Meldebestand sollte auf {np.ceil(s)} Stück gesetzt werden.\n")

# 3. Erwartete Fehlmenge E(B)
# E(B) = sigma_L * (phi(z) - z * (1 - Phi(z)))
phi_z = norm.pdf(z)
one_minus_Phi_z = 1 - norm.cdf(z) # Ist 1 - alpha_target
E_B = sigma_L * (phi_z - z * one_minus_Phi_z)

print(f"3. Erwartete Fehlmenge pro Zyklus E(B):")
print(f"   - phi(z={z:.3f}) = {phi_z:.4f}")
print(f"   - E(B) = {sigma_L:.2f} * ({phi_z:.4f} - {z:.3f} * {1-alpha_target:.2f}) = {E_B:.4f} Stück\n")

# 4. beta-Servicegrad
# beta = 1 - E(B) / q
beta = 1 - (E_B / q)
print(f"4. Resultierender beta-Servicegrad:")
print(f"   - beta = 1 - ({E_B:.4f} / {q}) = {beta:.4f} oder {beta*100:.2f}%")
```

    1. Nachfrage während der WBZ:
       - Erwartungswert (mu_L): 200.00 Stück
       - Standardabweichung (sigma_L): 30.00 Stück

    2. Bestellpunkt für alpha = 99.0%:
       - Benötigter z-Wert (Sicherheitsfaktor): 2.326
       - Sicherheitsbestand: 2.326 * 30.00 = 69.79 Stück
       - Bestellpunkt s: 200.00 + 69.79 = 269.79 Stück (gerundet: 270.0)
       -> Der Meldebestand sollte auf 270.0 Stück gesetzt werden.

    3. Erwartete Fehlmenge pro Zyklus E(B):
       - phi(z=2.326) = 0.0267
       - E(B) = 30.00 * (0.0267 - 2.326 * 0.01) = 0.1017 Stück

    4. Resultierender beta-Servicegrad:
       - beta = 1 - (0.1017 / 500) = 0.9998 oder 99.98%

## Aufgabe 3: Diskrete Nachfrage und Faltung

Ein kleiner Kiosk verkauft eine spezielle importierte Limonade. Die
tägliche Nachfrage ist nicht normalverteilt, sondern folgt einer
einfachen diskreten Verteilung:

| Nachfrage (D) pro Tag   | 0 Flaschen | 1 Flasche | 2 Flaschen |
|:------------------------|:-----------|:----------|:-----------|
| Wahrscheinlichkeit P(D) | 0.2        | 0.6       | 0.2        |

Die Wiederbeschaffungszeit beträgt genau **2 Tage**.

**Ihre Aufgaben:**

1.  **Wahrscheinlichkeitsverteilung:** Leiten Sie die
    Wahrscheinlichkeitsverteilung für die Gesamtnachfrage $Y_2$ über den
    Risikozeitraum von 2 Tagen her. (Tipp: Nutzen Sie die Faltung der
    Verteilung mit sich selbst).
2.  **Fehlbestandswahrscheinlichkeit:** Wenn der Kioskbesitzer einen
    Bestellpunkt von $s=3$ Flaschen festlegt, wie hoch ist die
    Wahrscheinlichkeit, dass es zu einem Fehlbestand kommt (d.h. der
    $\alpha$-Servicegrad *nicht* eingehalten wird)?
3.  **Erwartete Fehlmenge:** Berechnen Sie die erwartete Fehlmenge
    $E(B)$ für den Bestellpunkt $s=3$.

**Lösungshinweise:**

> [!TIP]
>
> ### Tipps und wichtige Formeln
>
> #### 1. Faltung von Wahrscheinlichkeitsverteilungen
>
> Wenn Sie die Verteilung der Summe von zwei unabhängigen, diskreten
> Zufallsvariablen $D_1$ und $D_2$ (hier die Nachfrage an zwei
> aufeinanderfolgenden Tagen) finden wollen, müssen Sie deren
> Verteilungen “falten”. Für die Gesamtnachfrage $Y_2 = D_1 + D_2$
> berechnen Sie die Wahrscheinlichkeit $P(Y_2=k)$ wie folgt:
> $P(Y_2=k) = \sum_{j} P(D_1=j) \cdot P(D_2=k-j)$
>
> **Beispiel:** Um die Wahrscheinlichkeit für eine Gesamtnachfrage von 2
> zu finden ($k=2$), summieren Sie die Wahrscheinlichkeiten aller
> möglichen Kombinationen auf, die 2 ergeben:
> $P(Y_2=2) = P(D_1=0, D_2=2) + P(D_1=1, D_2=1) + P(D_1=2, D_2=0)$ Da
> die Tage unabhängig sind, ist $P(D_1=a, D_2=b) = P(D=a) \cdot P(D=b)$.
>
> #### 2. Fehlbestandswahrscheinlichkeit ($1-\alpha$)
>
> Ein Fehlbestand tritt ein, wenn die Nachfrage während der
> Wiederbeschaffungszeit ($Y_2$) den Bestellpunkt ($s$) übersteigt.
> $P(\text{Fehlbestand}) = P(Y_2 > s)$
>
> #### 3. Erwartete Fehlmenge ($E(B)$)
>
> Die erwartete Fehlmenge ist die Summe aller möglichen Fehlmengen,
> gewichtet mit ihren jeweiligen Eintrittswahrscheinlichkeiten.
> $E(B) = \sum_{y} \max(0, y - s) \cdot P(Y_2=y)$ Sie müssen also für
> jeden möglichen Nachfragewert $y$ die Fehlmenge $(y-s)$ berechnen
> (falls diese positiv ist) und mit der Wahrscheinlichkeit $P(Y_2=y)$
> multiplizieren.

**1. Wahrscheinlichkeitsverteilung der Gesamtnachfrage über 2 Tage
(Y2):**

Wir müssen alle möglichen Kombinationen der Nachfrage an Tag 1 ($D_1$)
und Tag 2 ($D_2$) betrachten. Die Gesamtnachfrage ist $Y_2 = D_1 + D_2$.

- **P(Y2 = 0):** Nur wenn $D_1=0$ und $D_2=0$.
  - $P(Y2 = 0) = 0.2 \cdot 0.2 = 0.04$
- **P(Y2 = 1):** Wenn ($D_1=0, D_2=1$) oder ($D_1=1, D_2=0$).
  - $P(Y2 = 1) = 0.2 \cdot 0.6 + 0.6 \cdot 0.2 = 0.12 + 0.12 = 0.24$
- **P(Y2 = 2):** Wenn ($D_1=0, D_2=2$), ($D_1=1, D_2=1$), oder
  ($D_1=2, D_2=0$).
  - $P(Y2 = 2) = 0.2 \cdot 0.2 + 0.6 \cdot 0.6 + 0.2 \cdot 0.2 = 0.04 + 0.36 + 0.04 = 0.44$
- **P(Y2 = 3):** Wenn ($D_1=1, D_2=2$) oder ($D_1=2, D_2=1$).
  - $P(Y2 = 3) = 0.6 \cdot 0.2 + 0.2 \cdot 0.6 = 0.12 + 0.12 = 0.24$
- **P(Y2 = 4):** Nur wenn $D_1=2$ und $D_2=2$.
  - $P(Y2 = 4) = 0.2 \cdot 0.2 = 0.04$

**Zusammenfassung der Verteilung für Y2:**

| $Y_2$    | 0    | 1    | 2    | 3    | 4    |
|:---------|:-----|:-----|:-----|:-----|:-----|
| P($Y_2$) | 0.04 | 0.24 | 0.44 | 0.24 | 0.04 |

**2. Wahrscheinlichkeit eines Fehlbestands für s=3:**

Ein Fehlbestand tritt auf, wenn die Nachfrage $Y_2$ den Bestellpunkt
$s=3$ übersteigt. $P(\text{Fehlbestand}) = P(Y_2 > 3) = P(Y_2 = 4)$
$P(\text{Fehlbestand}) = 0.04$ oder 4%.

Der $\alpha$-Servicegrad wäre demnach $1 - 0.04 = 0.96$ oder 96%.

**3. Erwartete Fehlmenge E(B) für s=3:**

Die Fehlmenge $B$ ist $\max(0, Y_2 - s)$. Wir berechnen den
Erwartungswert, indem wir jede mögliche Fehlmenge mit ihrer
Wahrscheinlichkeit multiplizieren.

- Wenn $Y_2 \le 3$, ist die Fehlmenge 0.
- Wenn $Y_2 = 4$, ist die Fehlmenge $4 - 3 = 1$.

$E(B) = \sum \max(0, y - s) \cdot P(Y_2=y)$
$E(B) = (0 \cdot P(Y_2=0)) + (0 \cdot P(Y_2=1)) + (0 \cdot P(Y_2=2)) + (0 \cdot P(Y_2=3)) + ((4-3) \cdot P(Y_2=4))$
$E(B) = 1 \cdot 0.04 = 0.04$

Die erwartete Fehlmenge pro Bestellzyklus beträgt 0.04 Flaschen.
