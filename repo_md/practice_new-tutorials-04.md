# Weitere Aufgaben zu Vorlesung 04


## Aufgabe 1: Simulation einer (s, q)-Politik

Ein Fachgeschäft für High-End-Grafikkarten steuert seinen Bestand
mittels einer $(s, q)$-Politik bei kontinuierlicher Überwachung die
durchgehend stattfindet. Die Eckdaten der Politik sind:

- Bestellpunkt (Meldebestand) **$s$**: 50 Grafikkarten
- Bestellmenge **$q$**: 150 Grafikkarten
- Wiederbeschaffungszeit **$L$**: 3 Wochen (deterministisch)

Zu Beginn (Ende Woche 0) sind die Bestände wie folgt:

- Physischer Bestand $I_0^P$: 70 Grafikkarten
- Bestellbestand (offene Bestellungen) $I_0^O$: 0 Grafikkarten

**Geplante wöchentliche Nachfragen:**

| Woche (t)       |  1  |  2  |  3  |  4  |  5  |  6  |
|:----------------|:---:|:---:|:---:|:---:|:---:|:---:|
| Nachfrage $d_t$ | 20  | 25  | 30  | 35  | 20  | 40  |

**Ihre Aufgaben:**

1.  **Bestandsentwicklung verfolgen:** Füllen Sie die folgende Tabelle
    aus, um die Entwicklung aller relevanten Bestandsgrößen über 6
    Wochen zu verfolgen. Eine Bestellung wird am Ende der Woche
    ausgelöst, in der der disponible Bestand den Meldebestand $s$
    erreicht oder unterschreitet. Der Wareneingang erfolgt $L=3$ Wochen
    später zu Beginn der entsprechenden Woche.

| Woche (t) | Nachfrage $d_t$ | Disp. Bestand (Anfang) | Bestellung? (Menge) | Disp. Bestand (Ende) | Phys. Bestand (Ende) | Bestellbestand (Ende) | Fehlbestand (Ende) |
|----|----|----|----|----|----|----|----|
| **0** | \- | \- | \- | 70 | 70 | 0 | 0 |
| **1** | 20 | 70 | ? | ? | ? | ? | ? |
| **2** | 25 | ? | ? | ? | ? | ? | ? |
| **3** | 30 | ? | ? | ? | ? | ? | ? |
| **4** | 35 | ? | ? | ? | ? | ? | ? |
| **5** | 20 | ? | ? | ? | ? | ? | ? |
| **6** | 40 | ? | ? | ? | ? | ? | ? |

> [!NOTE]
>
> ### Lösung
>
> ``` python
> import pandas as pd
>
> # Initialwerte
> s, q, L = 50, 150, 3
> demands = [20, 25, 30, 35, 20, 40]
> T = len(demands)
>
> # Tracking-Variablen
> disp_bestand = 70
> phys_bestand = 70
> bestell_bestand = 0
> fehl_bestand = 0
> lieferungen = {} 
>
> # Tabelle für Ergebnisse
> results = []
> # Zustand am Ende von Woche 0
> results.append({
>     'Woche (t)': 0, 'Nachfrage $d_t$': '-', 'Disp. Bestand (A)': '-', 
>     'Bestellung? (E)': 0, 'Disp. Bestand (E)': disp_bestand, 
>     'Phys. Bestand (E)': phys_bestand, 'Bestellbestand (E)': bestell_bestand, 
>     'Fehlbestand (E)': fehl_bestand
> })
>
>
> for t in range(1, T + 1):
>     disp_bestand_anfang = disp_bestand
>     
>     # 1. Wareneingang
>     wareneingang = lieferungen.get(t, 0)
>     if wareneingang > 0:
>         bestell_bestand -= wareneingang
>         phys_bestand += wareneingang
>         
>     # 2. Nachfrage bedienen
>     demand_t = demands[t-1]
>     zu_bedienen = demand_t + fehl_bestand
>     
>     if phys_bestand >= zu_bedienen:
>         phys_bestand -= zu_bedienen
>         fehl_bestand = 0
>     else:
>         fehl_bestand = zu_bedienen - phys_bestand
>         phys_bestand = 0
>     disp_bestand -= demand_t
>     
>     # 3. Bestellentscheidung
>     bestellung_getaetigt = 0
>     if disp_bestand <= s:
>         bestellung_getaetigt = q
>         bestell_bestand += q
>         disp_bestand += q
>         liefer_woche = t + L
>         lieferungen[liefer_woche] = lieferungen.get(liefer_woche, 0) + q
>         
>     results.append({
>         'Woche (t)': t,
>         'Nachfrage $d_t$': demand_t,
>         'Disp. Bestand (A)': disp_bestand_anfang,
>         'Bestellung? (E)': bestellung_getaetigt,
>         'Disp. Bestand (E)': disp_bestand,
>         'Phys. Bestand (E)': phys_bestand,
>         'Bestellbestand (E)': bestell_bestand,
>         'Fehlbestand (E)': fehl_bestand
>     })
>
> df_results = pd.DataFrame(results)
> print(df_results[['Woche (t)', 'Nachfrage $d_t$', 'Disp. Bestand (A)', 'Bestellung? (E)', 'Disp. Bestand (E)', 'Phys. Bestand (E)', 'Bestellbestand (E)', 'Fehlbestand (E)']].to_string(index=False))
> ```
>
>      Woche (t) Nachfrage $d_t$ Disp. Bestand (A)  Bestellung? (E)  Disp. Bestand (E)  Phys. Bestand (E)  Bestellbestand (E)  Fehlbestand (E)
>              0               -                 -                0                 70                 70                   0                0
>              1              20                70              150                200                 50                 150                0
>              2              25               200                0                175                 25                 150                0
>              3              30               175                0                145                  0                 150                5
>              4              35               145                0                110                110                   0                0
>              5              20               110                0                 90                 90                   0                0
>              6              40                90              150                200                 50                 150                0

## Aufgabe 2: Sicherheitsbestand für Laufschuhe

Ein Sportartikelhändler verkauft ein beliebtes Modell von Laufschuhen.
Die wöchentliche Nachfrage ist annähernd normalverteilt mit einem
**Mittelwert von 100 Paaren** und einer **Standardabweichung von 30
Paaren**. Die Wiederbeschaffungszeit vom Hersteller beträgt konstant **2
Wochen**. Es wird eine kontinuierliche Bestandsüberwachung angewendet.

**Ihre Aufgaben:**

1.  **Nachfrage im Risikozeitraum:** Berechnen Sie den Erwartungswert
    und die Standardabweichung der Nachfrage während der
    Wiederbeschaffungszeit.
2.  **Sicherheitsbestand und Bestellpunkt:** Der Händler strebt einen
    Zyklus-Servicegrad ($\alpha$-Servicegrad) von 98% an. Bestimmen Sie
    den dafür notwendigen Sicherheitsfaktor $z$, den Sicherheitsbestand
    $SS$ und den Bestellpunkt $s$.
3.  **Erwartete Fehlmenge:** Wie hoch ist die erwartete Fehlmenge pro
    Bestellzyklus ($E(B)$) bei dem in Teil 2 ermittelten Bestellpunkt?
4.  **Mengen-Servicegrad:** Wenn der Händler eine fixe Bestellmenge von
    $q=500$ Paaren verwendet, welchen Mengen-Servicegrad
    ($\beta$-Servicegrad oder “Fill Rate”) erreicht er damit?

> [!NOTE]
>
> ### Lösung
>
> ``` python
> import numpy as np
> from scipy.stats import norm
>
> # Gegebene Daten
> mu_d_weekly = 100
> sigma_d_weekly = 30
> L = 2 # Wochen
> q = 500
> alpha_target = 0.98
>
> # 1. Momente der Nachfrage während der WBZ
> mu_L = L * mu_d_weekly
> sigma_L = np.sqrt(L) * sigma_d_weekly
> print(f"1. Nachfrage während der WBZ:")
> print(f"   - Erwartungswert (mu_L): {mu_L:.2f} Paare")
> print(f"   - Standardabweichung (sigma_L): {sigma_L:.2f} Paare\n")
>
> # 2. Bestellpunkt und Sicherheitsbestand für alpha-Servicegrad
> # Finde den z-Wert für 98%
> z = norm.ppf(alpha_target)
> safety_stock = z * sigma_L
> s = mu_L + safety_stock
>
> print(f"2. Bestellpunkt für alpha = {alpha_target*100}%:")
> print(f"   - Benötigter z-Wert (Sicherheitsfaktor): {z:.3f}")
> print(f"   - Sicherheitsbestand (SS): {z:.3f} * {sigma_L:.2f} = {safety_stock:.2f} Paare")
> print(f"   - Bestellpunkt (s): {mu_L:.2f} + {safety_stock:.2f} = {s:.2f} Paare")
> print(f"   -> Der Meldebestand sollte auf {np.ceil(s)} Paare gesetzt werden.\n")
>
> # 3. Erwartete Fehlmenge E(B)
> # Standardisierte Einheiten-Verlustfunktion G_u(z) = phi(z) - z * (1 - Phi(z))
> phi_z = norm.pdf(z)
> one_minus_Phi_z = 1 - alpha_target
> E_B = sigma_L * (phi_z - z * one_minus_Phi_z)
>
> print(f"3. Erwartete Fehlmenge pro Zyklus E(B):")
> print(f"   - G_u(z={z:.3f}) = {phi_z:.4f} - {z:.3f} * {one_minus_Phi_z:.2f} = {(phi_z - z * one_minus_Phi_z):.4f}")
> print(f"   - E(B) = {sigma_L:.2f} * {(phi_z - z * one_minus_Phi_z):.4f} = {E_B:.4f} Paare\n")
>
> # 4. beta-Servicegrad
> beta = 1 - (E_B / q)
> print(f"4. Resultierender beta-Servicegrad:")
> print(f"   - beta = 1 - ({E_B:.4f} / {q}) = {beta:.4f} oder {beta*100:.2f}%")
> print(f"\nMit dieser Politik werden {beta*100:.2f}% der gesamten Nachfrage direkt aus dem Lager bedient.")
> ```
>
>     1. Nachfrage während der WBZ:
>        - Erwartungswert (mu_L): 200.00 Paare
>        - Standardabweichung (sigma_L): 42.43 Paare
>
>     2. Bestellpunkt für alpha = 98.0%:
>        - Benötigter z-Wert (Sicherheitsfaktor): 2.054
>        - Sicherheitsbestand (SS): 2.054 * 42.43 = 87.13 Paare
>        - Bestellpunkt (s): 200.00 + 87.13 = 287.13 Paare
>        -> Der Meldebestand sollte auf 288.0 Paare gesetzt werden.
>
>     3. Erwartete Fehlmenge pro Zyklus E(B):
>        - G_u(z=2.054) = 0.0484 - 2.054 * 0.02 = 0.0073
>        - E(B) = 42.43 * 0.0073 = 0.3115 Paare
>
>     4. Resultierender beta-Servicegrad:
>        - beta = 1 - (0.3115 / 500) = 0.9994 oder 99.94%
>
>     Mit dieser Politik werden 99.94% der gesamten Nachfrage direkt aus dem Lager bedient.
