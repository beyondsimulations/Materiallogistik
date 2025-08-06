# Weitere Aufgaben zu Vorlesung 03


## Aufgabe 1: Planung für einen Möbelhersteller (PLSP)

Ein Möbelhersteller fertigt auf einer Holzzuschnittmaschine zwei
Varianten von Stuhlbeinen: “Klassik” und “Modern”. Die Maschine kann pro
Woche nur für eine Variante eingerichtet werden. Der Rüstzustand kann
jedoch in die Folgewoche übernommen werden, falls dieselbe Variante
weiterproduziert wird. Ein Rüstvorgang ist nur bei einem
Variantenwechsel oder nach einer produktionsfreien Woche erforderlich.

**Gegebene Daten:**

- **Planungshorizont:** 5 Wochen
- **Wöchentliche Kapazität:** 80 Stunden

**Produktdaten:**

| Parameter             | Stuhlbein “Klassik” | Stuhlbein “Modern” |
|:----------------------|:--------------------|:-------------------|
| Rüstkosten (s)        | 300 GE              | 250 GE             |
| Lagerkosten (h)       | 4 GE/Stück          | 6 GE/Stück         |
| Bearbeitungszeit (tb) | 0,5 h/Stück         | 0,8 h/Stück        |
| Rüstzeit (tr)         | 15 h                | 12 h               |

**Nachfrage:**

| Woche (t)      |  1  |  2  |  3  |  4  |  5  |
|:---------------|:---:|:---:|:---:|:---:|:---:|
| Bedarf Klassik | 40  |  0  | 60  |  0  | 50  |
| Bedarf Modern  |  0  | 70  |  0  | 40  |  0  |

**Vorgegebener Produktionsplan:**

Analysieren Sie den folgenden, manuell erstellten Produktionsplan:

- **Woche 1:** Produziere 40 x “Klassik”.
- **Woche 2:** Produziere 70 x “Modern”.
- **Woche 3:** Produziere 110 x “Klassik”. (deckt Bedarf für Woche 3 und
  5)
- **Woche 4:** Produziere 40 x “Modern”.
- **Woche 5:** Keine Produktion.

**Ihre Aufgaben:**

1.  **Kostenberechnung:** Berechnen Sie die gesamten Rüst- und
    Lagerkosten für den vorgegebenen Plan.
2.  **Kapazitätsprüfung:** Überprüfen Sie für jede Woche, ob der Plan
    die verfügbare Kapazität von 80 Stunden einhält.
3.  **Diskussion:** Erörtern Sie, warum eine separate, unkapazitierte
    Planung (z.B. mit Wagner-Whitin für jedes Produkt) hier zu einem
    schlechteren oder unzulässigen Ergebnis führen würde.

> [!NOTE]
>
> ### Lösung
>
> ``` python
> import pandas as pd
>
> # Daten
> demands_k = [40, 0, 60, 0, 50]
> demands_m = [0, 70, 0, 40, 0]
> s_k, s_m = 300, 250
> h_k, h_m = 4, 6
> tb_k, tb_m = 0.5, 0.8
> tr_k, tr_m = 15, 12
> capacity = 80
> weeks = range(1, 6)
>
> # Gegebener Plan
> q = {
>     'K': [40, 0, 110, 0, 0],
>     'M': [0, 70, 0, 40, 0]
> }
>
> # 1. Kostenberechnung
> inventory_k, inventory_m = 0, 0
> total_setup_costs = 0
> total_inventory_costs = 0
> last_prod = None
>
> print("1. Kostenberechnung:\n")
> for i, week in enumerate(weeks):
>     prod_k = q['K'][i]
>     prod_m = q['M'][i]
>     
>     current_prod = None
>     setup_cost = 0
>     if prod_k > 0:
>         current_prod = 'K'
>         if last_prod != 'K':
>             setup_cost = s_k
>             print(f"Woche {week}: Rüstung für Klassik (Kosten: {s_k} GE)")
>     elif prod_m > 0:
>         current_prod = 'M'
>         if last_prod != 'M':
>             setup_cost = s_m
>             print(f"Woche {week}: Rüstung für Modern (Kosten: {s_m} GE)")
>             
>     if setup_cost == 0 and current_prod is not None:
>         print(f"Woche {week}: Rüstzustand für {current_prod} übernommen.")
>         
>     last_prod = current_prod
>     total_setup_costs += setup_cost
>
>     inventory_k += prod_k - demands_k[i]
>     inventory_m += prod_m - demands_m[i]
>     
>     inv_cost = inventory_k * h_k + inventory_m * h_m
>     total_inventory_costs += inv_cost
>     print(f"  Bestand Ende Woche {week}: {inventory_k}x K, {inventory_m}x M. Lagerkosten: {inv_cost} GE\n")
>
> print(f"Gesamte Rüstkosten: {total_setup_costs} GE")
> print(f"Gesamte Lagerkosten: {total_inventory_costs} GE")
> print(f"Gesamtkosten: {total_setup_costs + total_inventory_costs} GE")
>
>
> # 2. Kapazitätsprüfung
> print("\n2. Kapazitätsprüfung:\n")
> capacity_data = []
> last_prod_cap = None
> for i, week in enumerate(weeks):
>     cap_used, setup_time = 0, 0
>     prod_k, prod_m = q['K'][i], q['M'][i]
>     current_prod_cap = None
>     
>     if prod_k > 0:
>         current_prod_cap = 'K'
>         cap_used += prod_k * tb_k
>         if last_prod_cap != 'K': setup_time = tr_k
>     elif prod_m > 0:
>         current_prod_cap = 'M'
>         cap_used += prod_m * tb_m
>         if last_prod_cap != 'M': setup_time = tr_m
>         
>     last_prod_cap = current_prod_cap
>     total_cap_used = cap_used + setup_time
>     
>     capacity_data.append({
>         'Woche': week,
>         'Bedarf Kapazität (h)': total_cap_used,
>         'Limit (h)': capacity,
>         'Einhaltung': 'Ja' if total_cap_used <= capacity else 'NEIN'
>     })
>
> print(pd.DataFrame(capacity_data).to_string(index=False))
> ```
>
>     1. Kostenberechnung:
>
>     Woche 1: Rüstung für Klassik (Kosten: 300 GE)
>       Bestand Ende Woche 1: 0x K, 0x M. Lagerkosten: 0 GE
>
>     Woche 2: Rüstung für Modern (Kosten: 250 GE)
>       Bestand Ende Woche 2: 0x K, 0x M. Lagerkosten: 0 GE
>
>     Woche 3: Rüstung für Klassik (Kosten: 300 GE)
>       Bestand Ende Woche 3: 50x K, 0x M. Lagerkosten: 200 GE
>
>     Woche 4: Rüstung für Modern (Kosten: 250 GE)
>       Bestand Ende Woche 4: 50x K, 0x M. Lagerkosten: 200 GE
>
>       Bestand Ende Woche 5: 0x K, 0x M. Lagerkosten: 0 GE
>
>     Gesamte Rüstkosten: 1100 GE
>     Gesamte Lagerkosten: 400 GE
>     Gesamtkosten: 1500 GE
>
>     2. Kapazitätsprüfung:
>
>      Woche  Bedarf Kapazität (h)  Limit (h) Einhaltung
>          1                  35.0         80         Ja
>          2                  68.0         80         Ja
>          3                  70.0         80         Ja
>          4                  44.0         80         Ja
>          5                   0.0         80         Ja
>
> **3. Diskussion:**
>
> Eine separate Planung mit einem Algorithmus wie Wagner-Whitin würde
> scheitern, weil dieser zwei zentrale Aspekte des Problems ignoriert:
>
> 1.  **Rüstkopplung:** WW kann das Konzept der Rüstzustandsübernahme
>     nicht abbilden. Er würde für jeden Produktionslauf Rüstkosten
>     ansetzen, obwohl in einem gekoppelten Plan (z.B. Produktion von
>     “Modern” in Woche 2 und 3) Rüstkosten eingespart werden könnten.
>     Der Plan wäre also suboptimal.
> 2.  **Kapazitätskonkurrenz:** WW optimiert jedes Produkt isoliert. Er
>     würde für Woche 3 sowohl für “Klassik” als auch “Modern”
>     möglicherweise eine Produktion planen. Die Summe der benötigten
>     Kapazitäten würde das Wochenlimit von 80 Stunden überschreiten,
>     was den Plan unzulässig macht. Das PLSP-Verfahren löst genau
>     diesen Trade-off zwischen Rüstkosten, Lagerkosten und knapper,
>     geteilter Kapazität.

## Aufgabe 2: Analyse eines Produktionsplans für Lösungsmittel

Ein Planer hat einen unvollständigen Produktionsplan für die
Lösungsmittel “Alpha” und “Gamma” hinterlassen. Beide werden in einem
Reaktor gefertigt, der pro Woche nur für **einen** Typ eingerichtet sein
kann. **Ein negativer Lagerbestand ist nicht zulässig.**

**Gegebene Daten:**

- Anfangslagerbestand (Ende Woche 0): Produkt Alpha = **10**, Produkt
  Gamma = **50**.
- Produkt Alpha: Rüstkosten $s_A$ = 400 GE, Lagerkostensatz $h_A$ = 8
  GE/Stück/Woche.
- Produkt Gamma: Rüstkosten $s_G$ = 350 GE, Lagerkostensatz $h_G$ = 10
  GE/Stück/Woche.
- Rüstkosten fallen an, wenn die Produktion für ein Produkt in einer
  Woche stattfindet, in der zuvor ein anderes Produkt (oder nichts)
  hergestellt wurde.

**Die unvollständige Tabelle:**

Der Planer hat den folgenden Produktionsplan sowie die Bedarfe
hinterlassen. Ihre Aufgabe ist es, die fehlenden Werte zu berechnen.

| Woche (t) | Prod. Typ | Bedarf Alpha | Prod. Alpha | Lager Alpha (Ende) | Bedarf Gamma | Prod. Gamma | Lager Gamma (Ende) | Rüstk. | Lagerk. (Summe) |
|----|----|----|----|----|----|----|----|----|----|
| 0 | \- | \- | \- | 10 | \- | \- | 50 | \- | \- |
| 1 | Alpha | 30 | 70 | **(a)** | 20 | 0 | **(b)** | **(c)** | **(d)** |
| 2 | Gamma | 40 | 0 | **(e)** | 30 | 60 | **(f)** | **(g)** | **(h)** |
| 3 | Gamma | 10 | 0 | **(i)** | 40 | 10 | **(j)** | **(k)** | **(l)** |
| 4 | Alpha | 20 | 30 | **(m)** | 20 | 0 | **(n)** | **(o)** | **(p)** |
| **SUMME** | \- |  |  | \- |  |  | \- | **(q)** | **(r)** |

**Ihre Aufgaben:**

1.  **Fehlende Werte berechnen:** Berechnen Sie schrittweise die
    fehlenden Werte (a) bis (r) in der Tabelle. Stellen Sie sicher, dass
    kein Lagerbestand negativ wird.
2.  **Gesamtkosten:** Ermitteln Sie die Summe der Rüst- und Lagerkosten
    für den gesamten Planungszeitraum.

> [!NOTE]
>
> ### Lösung
>
> **1. Schrittweise Berechnung:**
>
> - **Woche 1:**
>   - 1)  `Lager Alpha`: $10 + 70 - 30 = 50$
>   - 2)  `Lager Gamma`: $50 + 0 - 20 = 30$
>   - 3)  `Rüstkosten`: Produktionsstart für Alpha $\rightarrow 400$ GE.
>   - 4)  `Lagerkosten`:
>         $(50 \cdot 8) + (30 \cdot 10) = 400 + 300 = 700$ GE.
> - **Woche 2:**
>   - 5)  `Lager Alpha`: $50 + 0 - 40 = 10$
>   - 6)  `Lager Gamma`: $30 + 60 - 30 = 60$
>   - 7)  `Rüstkosten`: Wechsel von Alpha auf Gamma $\rightarrow 350$
>         GE.
>   - 8)  `Lagerkosten`: $(10 \cdot 8) + (60 \cdot 10) = 80 + 600 = 680$
>         GE.
> - **Woche 3:**
>   - 1)  `Lager Alpha`: $10 + 0 - 10 = 0$
>   - 10) `Lager Gamma`: $60 + 10 - 40 = 30$
>   - 11) `Rüstkosten`: Gamma -\> Gamma $\rightarrow 0$ GE.
>   - 12) `Lagerkosten`: $(0 \cdot 8) + (30 \cdot 10) = 300$ GE.
> - **Woche 4:**
>   - 13) `Lager Alpha`: $0 + 30 - 20 = 10$
>   - 14) `Lager Gamma`: $30 + 0 - 20 = 10$
>   - 15) `Rüstkosten`: Wechsel von Gamma auf Alpha $\rightarrow 400$
>         GE.
>   - 16) `Lagerkosten`: $(10 \cdot 8) + (10 \cdot 10) = 80 + 100 = 180$
>         GE.
> - **Summen:**
>   - 17) `Summe Rüstkosten`: $400 + 350 + 0 + 400 = 1150$ GE.
>   - 18) `Summe Lagerkosten`: $700 + 680 + 300 + 180 = 1860$ GE.
>
> **2. Gesamtkosten:**
>
> - **Gesamtkosten (Rüstung + Lager):** $1150 + 1860 = 3010$ GE.
