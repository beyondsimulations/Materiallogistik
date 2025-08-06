# Weitere Aufgaben zu Vorlesung 01


## Aufgabe 1: Materialbedarfsermittlung für einen “Smart Speaker”

Ein Hersteller von Unterhaltungselektronik plant die Einführung eines
neuen Smart Speakers mit dem Namen “EchoSphere”. Die für die Montage
notwendigen Komponenten und ihre Beziehungen sind in der Stückliste
aufgeführt.

**Struktur des “EchoSphere” (E):**

- 1x Gehäuse (G)
- 2x Lautsprecher-Einheit (L)
- 1x Hauptplatine (P)
  - 1x CPU-Modul (C)
  - 2x RAM-Chip (R)

**Produktionsplan:**

Der Primärbedarf für den “EchoSphere” beträgt 80 Stück in Periode 9.

**Stammdaten der Komponenten:**

| Komponente       | Lagerbestand | Vorlaufzeit (Perioden) |
|------------------|--------------|------------------------|
| E (EchoSphere)   | 10           | 1                      |
| G (Gehäuse)      | 20           | 2                      |
| L (Lautsprecher) | 25           | 3                      |
| P (Hauptplatine) | 5            | 2                      |
| C (CPU-Modul)    | 15           | 2                      |
| R (RAM-Chip)     | 40           | 1                      |

**Ihre Aufgaben:**

1.  **Gozinto-Graph zeichnen:** Stellen Sie die Produktstruktur grafisch
    als Gozinto-Graph dar.
2.  **Materialbedarfsermittlung:** Führen Sie eine vollständige
    Materialbedarfsermittlung durch. Berechnen Sie für jede Komponente
    den Brutto- und Nettobedarf.
3.  **Bestellzeitpunkte:** Leiten Sie aus Ihrer Bedarfsrechnung die
    finalen Bestellzeitpunkte für alle benötigten Komponenten ab.

> [!NOTE]
>
> ### Lösung
>
> **1. Gozinto-Graph:**
>
> ``` python
> import graphviz
>
> dot = graphviz.Digraph(comment='Gozinto-Graph')
> dot.node('E', 'EchoSphere (E)')
> dot.node('G', 'Gehäuse (G)')
> dot.node('L', 'Lautsprecher (L)')
> dot.node('P', 'Hauptplatine (P)')
> dot.node('C', 'CPU-Modul (C)')
> dot.node('R', 'RAM-Chip (R)')
>
> dot.edge('G', 'E', label='1')
> dot.edge('L', 'E', label='2')
> dot.edge('P', 'E', label='1')
> dot.edge('C', 'P', label='1')
> dot.edge('R', 'P', label='2')
>
> dot
> ```
>
> <div id="fig-task1-neu">
>
> ![](new-tutorials-01_files/figure-commonmark/fig-task1-neu-output-1.svg)
>
> Figure 1: Gozinto-Graph für EchoSphere
>
> </div>
>
> **2. & 3. Materialbedarfsermittlung:**
>
> ``` python
> import pandas as pd
> import matplotlib.pyplot as plt
>
> data = {
>     'Komponente': ['CPU-Modul (C)', 'Lautsprecher (L)', 'RAM-Chip (R)', 'Gehäuse (G)', 'Hauptplatine (P)', 'EchoSphere (E)'],
>     'Bestellmenge (Nettobedarf)': [50, 115, 90, 50, 65, 70],
>     'Bestellperiode': [4, 5, 5, 6, 6, 8]
> }
> df_bestellungen = pd.DataFrame(data).sort_values('Bestellperiode')
> print(df_bestellungen.to_string(index=False))
> ```
>
>           Komponente  Bestellmenge (Nettobedarf)  Bestellperiode
>        CPU-Modul (C)                          50               4
>     Lautsprecher (L)                         115               5
>         RAM-Chip (R)                          90               5
>          Gehäuse (G)                          50               6
>     Hauptplatine (P)                          65               6
>       EchoSphere (E)                          70               8

## Aufgabe 2: ABC-Analyse für einen Medizintechnik-Großhändler

Ein Großhändler für Medizintechnik möchte sein Sortiment analysieren, um
die Lagerbewirtschaftung zu optimieren und Kosten zu senken. Die Daten
für 10 ausgewählte Artikel sind wie folgt:

| Artikel-Nr. | Artikelbezeichnung | Jahresbedarf (Stück) | Preis pro Stück (€) |
|----|----|----|----|
| 1 | Skalpelle (10er-Pack) | 20000 | 8,00 |
| 2 | Ultraschallgel (1L) | 5000 | 15,00 |
| 3 | Einweghandschuhe (100er) | 50000 | 5,00 |
| 4 | Defibrillator | 50 | 12000,00 |
| 5 | Spritzen (100er) | 40000 | 10,00 |
| 6 | Infusionsständer | 200 | 80,00 |
| 7 | Operationsmasken (50er) | 60000 | 4,00 |
| 8 | MRT-Kontrastmittel | 100 | 800,00 |
| 9 | Desinfektionsmittel (5L) | 8000 | 25,00 |
| 10 | Stethoskop | 400 | 220,00 |

**Ihre Aufgaben:**

1.  **Jährlichen Verbrauchswert berechnen:** Berechnen Sie für jeden
    Artikel den jährlichen Verbrauchswert.
2.  **Rangliste erstellen:** Erstellen Sie eine Rangliste der Artikel
    nach ihrem Verbrauchswert in absteigender Reihenfolge.
3.  **Prozentuale Anteile berechnen:** Berechnen Sie den prozentualen
    Anteil jedes Artikels am Gesamtverbrauchswert.
4.  **Kumulierte Anteile berechnen:** Berechnen Sie die kumulierten
    prozentualen Wertanteile.
5.  **ABC-Klassifizierung:** Teilen Sie die Artikel in die Klassen A, B
    und C ein. Verwenden Sie typische Grenzen (z.B. A-Güter: \>75%
    Wertanteil, B-Güter: \>90% Wertanteil, C-Güter: Rest).
6.  **Grafische Darstellung:** Stellen Sie das Ergebnis grafisch in
    einer Lorenz-Kurve dar.

> [!NOTE]
>
> ### Lösung
>
> ``` python
> import pandas as pd
> import numpy as np
> import matplotlib.pyplot as plt
> import matplotlib.ticker as mtick
>
> plt.rcdefaults()
> plt.style.use('tableau-colorblind10')
>
> # Daten
> data_task = {
>     'Artikel-Nr.': range(1, 11),
>     'Bezeichnung': [
>         'Skalpelle', 'Ultraschallgel', 'Handschuhe', 'Defibrillator', 
>         'Spritzen', 'Infusionsständer', 'Masken', 'Kontrastmittel', 
>         'Desinfektion', 'Stethoskop'
>     ],
>     'Jahresbedarf': [20000, 5000, 50000, 50, 40000, 200, 60000, 100, 8000, 400],
>     'Preis': [8, 15, 5, 12000, 10, 80, 4, 800, 25, 220]
> }
> df = pd.DataFrame(data_task)
>
> # 1. Verbrauchswert
> df['Wert'] = df['Jahresbedarf'] * df['Preis']
>
> # 2. Rangliste
> df_sorted = df.sort_values(by='Wert', ascending=False).reset_index(drop=True)
>
> # 3. Prozentuale Anteile
> total_wert = df_sorted['Wert'].sum()
> df_sorted['Wertanteil (%)'] = (df_sorted['Wert'] / total_wert) * 100
>
> # 4. Kumulierte Anteile
> df_sorted['Kum. Wertanteil (%)'] = df_sorted['Wertanteil (%)'].cumsum()
> df_sorted['Kum. Artikelanteil (%)'] = (np.arange(len(df_sorted)) + 1) / len(df_sorted) * 100
>
> # 5. ABC-Klassifizierung
> def abc_klassifizierung(kum_wertanteil):
>     if kum_wertanteil <= 75:
>         return 'A'
>     elif kum_wertanteil <= 95:
>         return 'B'
>     else:
>         return 'C'
>
> df_sorted['ABC-Klasse'] = df_sorted['Kum. Wertanteil (%)'].apply(abc_klassifizierung)
>
> print("Tabelle zur ABC-Analyse:")
> print(df_sorted[['Bezeichnung', 'Wert', 'Wertanteil (%)', 'Kum. Wertanteil (%)', 'ABC-Klasse']].round(2).to_string())
>
> # 6. Grafische Darstellung (Lorenz-Kurve)
> fig, ax1 = plt.subplots(figsize=(7, 4))
>
> ax1.set_xlabel('Anteil der Artikelpositionen (%)')
> ax1.set_ylabel('Kumulierter Wertanteil (%)')
> ax1.plot(df_sorted['Kum. Artikelanteil (%)'], df_sorted['Kum. Wertanteil (%)'], marker='o', label='Kum. Wertanteil')
> ax1.yaxis.set_major_formatter(mtick.PercentFormatter())
> ax1.xaxis.set_major_formatter(mtick.PercentFormatter())
>
> # Grenzen für ABC
> a_grenze_wert = 75
> b_grenze_wert = 95
> ax1.axhline(y=a_grenze_wert, color='gray', linestyle='--', linewidth=0.8)
> ax1.axhline(y=b_grenze_wert, color='gray', linestyle='--', linewidth=0.8)
>
> a_grenze_artikel = df_sorted[df_sorted['ABC-Klasse'] == 'A']['Kum. Artikelanteil (%)'].max()
> b_grenze_artikel = df_sorted[df_sorted['ABC-Klasse'] == 'B']['Kum. Artikelanteil (%)'].max()
> ax1.axvline(x=a_grenze_artikel, color='gray', linestyle='--', linewidth=0.8)
> ax1.axvline(x=b_grenze_artikel, color='gray', linestyle='--', linewidth=0.8)
>
> # Text für Zonen
> ax1.text(a_grenze_artikel/2, 50, 'A-Güter', fontsize=15, ha='center', va='center', bbox=dict(boxstyle='round,pad=0.3', fc='aliceblue', ec='none', alpha=0.8))
> ax1.text((a_grenze_artikel + b_grenze_artikel)/2, 85, 'B-Güter', fontsize=12, ha='center', va='center', bbox=dict(boxstyle='round,pad=0.3', fc='aliceblue', ec='none', alpha=0.8))
> ax1.text((b_grenze_artikel + 100)/2, 97.5, 'C-Güter', fontsize=10, ha='center', va='center', bbox=dict(boxstyle='round,pad=0.3', fc='aliceblue', ec='none', alpha=0.8))
>
> plt.title('ABC-Analyse (Lorenz-Kurve)')
> fig.tight_layout()
> plt.grid(True)
> plt.show()
> ```
>
>     Tabelle zur ABC-Analyse:
>             Bezeichnung    Wert  Wertanteil (%)  Kum. Wertanteil (%) ABC-Klasse
>     0     Defibrillator  600000           28.45                28.45          A
>     1          Spritzen  400000           18.97                47.42          A
>     2        Handschuhe  250000           11.85                59.27          A
>     3            Masken  240000           11.38                70.65          A
>     4      Desinfektion  200000            9.48                80.13          B
>     5         Skalpelle  160000            7.59                87.72          B
>     6        Stethoskop   88000            4.17                91.89          B
>     7    Kontrastmittel   80000            3.79                95.69          C
>     8    Ultraschallgel   75000            3.56                99.24          C
>     9  Infusionsständer   16000            0.76               100.00          C
>
> <div id="fig-task2-neu">
>
> ![](new-tutorials-01_files/figure-commonmark/fig-task2-neu-output-2.png)
>
> Figure 2: ABC-Analyse für Medizintechnik-Sortiment
>
> </div>
