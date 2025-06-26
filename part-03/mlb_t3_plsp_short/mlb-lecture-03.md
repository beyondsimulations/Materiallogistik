# PLSP — Ein 

Mikroperioden-Modell für das dynamische einstufige Mehrprodukt-Losgrößenproblem# Dynamische Mehrprodukt-Losgrößenplanung (PLSP) 

Univ.-Prof. Dr. Michael Manitz# Dynamische Mehrprodukt-Lösgrößenplanung (PLSP) 

Annahmen:

- Der Rüstzustand kann übernommen werden.
- Es kann in einer Periode maximal einmal umgerüstet werden.
- Es können maximal zwei verschiedene Erzeugnisse in einer Periode produziert werden.# Modell CLSP 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}+p_{k t} \cdot q_{k t}\right)
$$

u. B. d. R.:

Bedarf in Periode $t$ :

$$
y_{k, t-1}+q_{k t}-y_{k t}=d_{k t}
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
Kapazität in Periode $t$ :

$$
\sum_{k \in \mathcal{K}}\left(\operatorname{tb}_{k} \cdot q_{k t}+\operatorname{tr}_{k} \cdot \gamma_{k t}\right) \leq b_{t}
$$

für alle $t=1,2, \ldots, T$
Es muss gerüstet werden, wenn $q_{t}>0$ ist:

$$
q_{k t}-M \cdot \gamma_{k t} \leq 0
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
Wertebereich:

$$
q_{k t} \geq 0 ; y_{k t} \geq 0 ; y_{k 0}=0 ; y_{k T}=0 ; \gamma_{k t} \in\{0,1\} \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$# Modell CLSP 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}+p_{k t} \cdot q_{k t}\right)
$$

u. B. d. R.:

$$
\begin{aligned}
& y_{k, t-1}+q_{k t}-y_{k t}=d_{k t} \\
& \sum_{k \in \mathcal{K}}\left(\operatorname{tb}_{k} \cdot q_{k t}+\operatorname{tr}_{k} \cdot \gamma_{k t}\right) \leq b_{t} \\
& q_{k t}-M \cdot \gamma_{k t} \leq 0 \\
& q_{k t} \geq 0 ; y_{k t} \geq 0 ; y_{k 0}=0 ; y_{k T}=0 ; \gamma_{k t} \in\{0,1\} \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
\end{aligned}
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$

$$
\text { für alle } t=1,2, \ldots, T
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
$q_{k t} \geq 0 ; y_{k t} \geq 0 ; y_{k 0}=0 ; y_{k T}=0 ; \gamma_{k t} \in\{0,1\}$ für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$# Modell PLSP 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}+p_{k t} \cdot q_{k t}\right)
$$

u. B. d. R.:

$$
\begin{aligned}
& y_{k, t-1}+q_{k t}-y_{k t}=d_{k t} \\
& \sum_{k \in \mathcal{K}}\left(\operatorname{tb}_{k} \cdot q_{k t}+\operatorname{tr}_{k} \cdot \gamma_{k t}\right) \leq b_{t} \\
& q_{k t}-M \cdot \gamma_{k t} \leq 0
\end{aligned}
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
für alle $t=1,2, \ldots, T$
für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
Übernahme des Rüstzustands: $q_{k t} \geq 0 ; y_{k t} \geq 0 ; \gamma_{k t} \in\{0,1\}$# Modell PLSP 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}+p_{k t} \cdot q_{k t}\right)
$$

u. B. d. R.:

$$
\begin{aligned}
& y_{k, t-1}+q_{k t}-y_{k t}=d_{k t} \\
& \sum_{k \in \mathcal{K}}\left(\operatorname{tb}_{k} \cdot q_{k t}+\operatorname{tr}_{k} \cdot \gamma_{k t}\right) \leq b_{t} \\
& q_{k t}-M \cdot \gamma_{k t} \leq 0
\end{aligned}
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
für alle $t=1,2, \ldots, T$
für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
Übernahme des Rüstzustands: $q_{k t} \geq 0 ; y_{k t} \geq 0 ; \gamma_{k t} \in\{0,1\} ; \omega_{k t} \in\{0,1\}$
$\omega_{k 0}=0$
für alle $k \in \mathcal{K}$# Modell PLSP 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}+p_{k t} \cdot q_{k t}\right)
$$

u. B. d. R.:

$$
\begin{aligned}
& y_{k, t-1}+q_{k t}-y_{k t}=d_{k t} \\
& \sum_{k \in \mathcal{K}}\left(\operatorname{tb}_{k} \cdot q_{k t}+\operatorname{tr}_{k} \cdot \gamma_{k t}\right) \leq b_{t} \\
& q_{k t}-M \cdot \gamma_{k t} \leq 0
\end{aligned}
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
für alle $t=1,2, \ldots, T$
für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
Übernahme des Rüstzustands: $q_{k t} \geq 0 ; y_{k t} \geq 0 ; \gamma_{k t} \in\{0,1\} ; \omega_{k t} \in\{0,1\}$
$\sum_{k \in \mathcal{K}} \omega_{k t} \leq 1$
für alle $t=1,2, \ldots, T$# Modell PLSP 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}+p_{k t} \cdot q_{k t}\right)
$$

u. B. d. R.:

$$
\begin{aligned}
& y_{k, t-1}+q_{k t}-y_{k t}=d_{k t} \\
& \sum_{k \in \mathcal{K}}\left(\operatorname{tb}_{k} \cdot q_{k t}+\operatorname{tr}_{k} \cdot \gamma_{k t}\right) \leq b_{t} \\
& q_{k t}-M \cdot \gamma_{k t} \leq 0
\end{aligned}
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
für alle $t=1,2, \ldots, T$
für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
Übernahme des Rüstzustands: $q_{k t} \geq 0 ; y_{k t} \geq 0 ; \gamma_{k t} \in\{0,1\} ; \omega_{k t} \in\{0,1\}$
$\sum_{k \in \mathcal{K}} \omega_{k t} \leq 1$
für alle $t=1,2, \ldots, T$
$\gamma_{k t} \geq \omega_{k t}-\omega_{k, t-1}$
für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$# Modell PLSP 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}+p_{k t} \cdot q_{k t}\right)
$$

u. B. d. R.:

$$
\begin{aligned}
& y_{k, t-1}+q_{k t}-y_{k t}=d_{k t} \\
& \sum_{k \in \mathcal{K}}\left(\operatorname{tb}_{k} \cdot q_{k t}+\operatorname{tr}_{k} \cdot \gamma_{k t}\right) \leq b_{t} \\
& q_{k t}-M \cdot\left(\omega_{k, t-1}+\omega_{k t}\right) \leq 0
\end{aligned}
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
für alle $t=1,2, \ldots, T$
für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
Übernahme des Rüstzustands: $q_{k t} \geq 0 ; y_{k t} \geq 0 ; \gamma_{k t} \in\{0,1\} ; \omega_{k t} \in\{0,1\}$
$\sum_{k \in \mathcal{K}} \omega_{k t} \leq 1$
für alle $t=1,2, \ldots, T$
$\gamma_{k t} \geq \omega_{k t}-\omega_{k, t-1}$
für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$# Beispiel PLSP

|  Bedarfsmengen |  |  |  |  |  | Parameter |  |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  Periode $t$ | 1 | 2 | 3 | 4 | 5 |  |  |   |
|  Erzeugnis $k$ |  |  |  |  |  | $h_{k}$ | $s_{k}$ | $\mathrm{tb}_{k}$  |
|  1 | 30 | - | 80 | - | 40 | 1 | 100 | 1  |
|  2 | - | - | 30 | - | 70 | 1 | 100 | 1  |
|  3 | - | - | 40 | - | 60 | 1 | 100 | 1  |# Beispiel PLSP

|  Bedarfsmengen |  |  |  |  |  | Parameter |  |  |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  Periode $t$ | 1 | 2 | 3 | 4 | 5 |  |  |  |   |
|  Erzeugnis $k$ |  |  |  |  |  | $h_{k}$ | $s_{k}$ | $\mathrm{tb}_{k}$ | $\mathrm{tr}_{k}$  |
|  1 | 30 | - | 80 | - | 40 | 1 | 100 | 1 | 10  |
|  2 | - | - | 30 | - | 70 | 1 | 100 | 1 | 10  |
|  3 | - | - | 40 | - | 60 | 1 | 100 | 1 | 10  |
|  Produktionsmengen |  |  |  |  |  |  |  |  |   |
|  Erzeugnis $k$ |  |  |  |  |  |  |  |  |   |
|  1 | 30 | 80 | - | 20 | 20 |  |  |  |   |
|  2 | - | - | 30 | - | 70 |  |  |  |   |
|  3 | - | - | 40 | 60 | - |  |  |  |   |# Dynamische Mehrprodukt-Lösgrößenplanung

## Beispiel PLSP

|  Bedarfsmengen |  |  |  |  |  | Parameter |  |  |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  Periode $t$ | 1 | 2 | 3 | 4 | 5 | $h_{k}$ | $s_{k}$ | $\mathrm{tb}_{k}$ | $\operatorname{tr}_{k}$  |
|  Erzeugnis $k$ |  |  |  |  |  |  |  |  |   |
|  1 | 30 | - | 80 | - | 40 | 1 | 100 | 1 | 10  |
|  2 | - | - | 30 | - | 70 | 1 | 100 | 1 | 10  |
|  3 | - | - | 40 | - | 60 | 1 | 100 | 1 | 10  |
|  Produktionsmengen |  |  |  |  |  |  |  |  |   |
|  Erzeugnis $k$ |  |  |  |  |  |  |  |  |   |
|  1 | 30 | 80 | - | 20 | 20 |  |  |  |   |
|  2 | - | - | 30 | - | 70 |  |  |  |   |
|  3 | - | - | 40 | 60 | - |  |  |  |   |

Optimale Lösung: 1 10+30 0+80 10+20 0+20 10+70 3 100 200 300 400 500

![img-0.jpeg](img-0.jpeg)# Dynamische Mehrprodukt-Losgrößenplanung: PLSP 

Univ.-Prof. Dr. Michael Manitz# Dynamische Mehrprodukt-Lösgrößenplanung: PLSP 

Annahmen:

- Der Rüstzustand kann übernommen werden.
- Es kann in einer Periode maximal einmal umgerüstet werden.
- Es können maximal zwei verschiedene Erzeugnisse in einer Periode produziert werden.# MLCLSP — Ein 

Makroperioden-Modell für das dynamische mehrstufige Mehrprodukt-Losgrößenproblem# Mehrstufige Mehrprodukt-Lösgrößenplanung (MLCLSP) 

wegen Ressourcenkonkurrenz

- arbeitsgangbezogene Betrachtung (Production Process Model (PPM)) zur Erfassung aller Ressourcenverbräuche, d. h., nach jedem Arbeitsgang gilt eine neue Erzeugnisstufe als erreicht, und es wird ein neues (Zwischen-)Produkt identifiziert
- mehrstufige Betrachtung zur Erfassung der Erzeugnisstruktur
- simultane Betrachtung aller Werkstätten auf Grund der Materialflussbeziehungen# Modell CLSP 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}+p_{k t} \cdot q_{k t}\right)
$$

u. B. d. R.:

Bedarf in Periode $t$ :

$$
y_{k, t-1}+q_{k t}-y_{k t}=d_{k t}
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
Kapazitäten in Periode $t$ :

$$
\sum_{k \in \mathcal{K}}\left(\operatorname{tb}_{k j} \cdot q_{k t}+\operatorname{tr}_{k j} \cdot \gamma_{k t}\right) \leq b_{j t}
$$

für alle $j \in \mathcal{J}$ und $t=1,2, \ldots, T$
Es muss gerüstet werden, wenn $q_{k t}>0$ ist:

$$
q_{k t}-M \cdot \gamma_{k t} \leq 0
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
Wertebereich:

$$
q_{k t} \geq 0 ; y_{k t} \geq 0 ; y_{k 0}=0 ; y_{k T}=0 ; \gamma_{k t} \in\{0,1\} \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$# Modell MLCLSP 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}+p_{k t} \cdot q_{k t}\right)
$$

u. B. d. R.:

Bedarf in Periode $t$ :

$$
y_{k, t-1}+q_{k t}-y_{k t}=d_{k t}+\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t} \quad \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$

Kapazitäten in Periode $t$ :

$$
\sum_{k \in \mathcal{K}}\left(\operatorname{tb}_{k j} \cdot q_{k t}+\operatorname{tr}_{k j} \cdot \gamma_{k t}\right) \leq b_{j t} \quad \text { für alle } j \in \mathcal{J} \text { und } t=1,2, \ldots, T
$$

Es muss gerüstet werden, wenn $q_{k t}>0$ ist:

$$
q_{k t}-M \cdot \gamma_{k t} \leq 0 \quad \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$

Wertebereich:

$$
q_{k t} \geq 0 ; y_{k t} \geq 0 ; y_{k 0}=0 ; y_{k T}=0 ; \gamma_{k t} \in\{0,1\} \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$# Modell MLCLSP 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}+p_{k t} \cdot q_{k t}\right)
$$

u. B. d. R.:

Bedarf in Periode $t$ :

$$
y_{k, t-1}+q_{k t}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t} \quad \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$

Kapazitäten in Periode $t$ :

$$
\sum_{k \in \mathcal{K}}\left(\operatorname{tb}_{k j} \cdot q_{k t}+\operatorname{tr}_{k j} \cdot \gamma_{k t}\right) \leq b_{j t} \quad \text { für alle } j \in \mathcal{J} \text { und } t=1,2, \ldots, T
$$

Es muss gerüstet werden, wenn $q_{k t}>0$ ist:

$$
q_{k t}-M \cdot \gamma_{k t} \leq 0 \quad \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$

Wertebereich:

$$
q_{k t} \geq 0 ; y_{k t} \geq 0 ; y_{k 0}=0 ; y_{k T}=0 ; \gamma_{k t} \in\{0,1\} \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$# Mehrstufige Mehrprodukt-Losgrößenplanung (MLCLSP)

## Erzeugnisstruktur

![img-1.jpeg](img-1.jpeg)

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement
62-11# Mehrstufige Mehrprodukt-Lösgrößenplanung (MLCLSP)

![img-2.jpeg](img-2.jpeg)

## Erzeugnisstruktur

- **Ressourcenbelegung**
  - Schichtlänge = 480 Minuten

- **Ressource A**
  - 100 min
  - 270 min
  - 100 min
  - 200 min

- **Ressource B**
  - 100 min
  - 200 min

*Univ.-Prof. Dr. Michael Manitz*

*Material-Logistik: Bestandsmanagement*

*M 62-12*# Mehrstufige Mehrprodukt-Lösgrößenplanung (MLCLSP)

![img-3.jpeg](img-3.jpeg)

## Erzeugnisstruktur

- **Ressourcenbelegung**
  - Schichtlänge = 480 Minuten

- **Ressource A**
  - 1 Ressource
  - 100 min
  - 270 min
  - 200 min
  - 270 min

- **Ressource B**
  - 1 Ressource
  - 100 min
  - 200 min

Univ.-Prof. Dr. Michael Manitz

Material-Logistik: Bestandsmanagement

62-13# Mehrstufige Mehrprodukt-Losgrößenplanung (MLCLSP)

## Erzeugnisstruktur

### Ressourcenbelegung

![img-4.jpeg](img-4.jpeg)

**Schichtlänge = 480 Minuten**

- **1 Ressource A**
- **2 Ressource B**
- **3 Ressource A**
- **200 min**

**270 min**

**100 min**

*Univ.-Prof. Dr. Michael Manitz*

*Material-Logistik: Bestandsmanagement*

*62-14*# Mehrstufige Losgrößenplanung 

## Bewertung der Lagerbestände:

physische Lagerbestände mit vollen Lagerkosten
Lagerkosten ${ }_{k t}=y_{k t} \cdot h_{k}$

$$
(k \in \mathcal{K}, t=1,2, \ldots, T)
$$

systemweite Lagerbestände mit marginalen Lagerkosten
Lagerkosten ${ }_{k t}=E_{k t} \cdot e_{k}$

$$
(k \in \mathcal{K}, t=1,2, \ldots, T)
$$

## $\triangleright$ echelon stock

$$
E_{k t}=y_{k t}+\sum_{j \in \mathcal{N}_{k}^{*}} v_{k j} \cdot y_{j t}
$$

$$
(k \in \mathcal{K}, t=1,2, \ldots, T)
$$

## $\triangleright$ echelon holding costs

$$
e_{k}=h_{k}-\sum_{j \in \mathcal{V}_{k}} a_{j k} \cdot h_{j}
$$Beispiel Erzeugnisstruktur E1 $\xrightarrow{1} \mathrm{P} 1\left(h_{\mathrm{E} 1}=6, h_{\mathrm{P} 1}=10\right)$ physische Lagerbestände mit vollen Lagerkosten

|  $k$ | $h_{k}$ | Bestand am
Periodenanfang
(physisch) | Lager-
kosten | Bestand am
Periodenende
(physisch) | Lager-
kosten | Anstieg der
Lagerkosten  |
| --- | --- | --- | --- | --- | --- | --- |
|  P1 | 10 | 0 | 0 | 1 | 10 | 10  |
|  E1 | 6 | 1 | 6 | 0 | 0 | -6  |
|   |  |  |  |  | Summe | 4  |

systemweite Lagerbestände mit marginalen Lagerkosten

|  $k$ | $e_{k}$ | Bestand am
Periodenanfang
(systemweit) | Lager-
kosten | Bestand am
Periodenende
(systemweit) | Lager-
kosten | Anstieg der
Lagerkosten  |
| --- | --- | --- | --- | --- | --- | --- |
|  P1 | 4 | 0 | 0 | 1 | 4 | 4  |
|  E1 | 6 | 1 | 6 | 1 | 6 | 0  |
|   |  |  |  |  | Summe | 4  |# Lösungsverfahren für mehrstufige Mehrprodukt-Losgrößenprobleme# Meta-Heuristiken# Mehrstufige Losgrößenplanung — Meta-Heuristiken

![img-5.jpeg](img-5.jpeg)

Univ.-Prof. Dr. Michael Manitz

Material-Logistik: Bestandsmanagement 67-1# Modell MLULSP 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}+p_{k t} \cdot q_{k t}\right)
$$

u. B. d. R.:

Bedarf in Periode $t$ :

$$
y_{k, t-1}+q_{k t}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t} \quad \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$

Es muss gerüstet werden, wenn $q_{k t}>0$ ist:

$$
q_{k t}-M \cdot \gamma_{k t} \leq 0
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
Wertebereich:

$$
\begin{array}{ll}
0 \leq q_{k t} \leq \widehat{q}_{k t} & \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T \\
y_{k t} \geq 0 ; y_{k 0}=0 ; y_{k T}=0 ; \gamma_{k t} \in\{0,1\} & \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
\end{array}
$$# Modell MLULSP bei gegebenem Rüstmuster 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+p_{k t} \cdot q_{k t}\right)+\text { Rüstkosten }
$$

u. B. d. R.:

Bedarf in Periode $t$ :

$$
y_{k, t-1}+q_{k t}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t} \quad \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$

Es muss gerüstet werden, wenn $q_{k t}>0$ ist:

$$
q_{k t}-M \cdot \gamma_{k t} \leq 0
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
Wertebereich:

$$
\begin{array}{ll}
0 \leq q_{k t} \leq \widehat{q}_{k t} & \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T \\
y_{k t} \geq 0 ; y_{k 0}=0 ; y_{k T}=0 ; \gamma_{k t} \text { gegeben } & \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
\end{array}
$$# Modell MLULSP bei gegebenem Rüstmuster 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+p_{k t} \cdot q_{k t}\right)+\text { Rüstkosten }
$$

u. B. d. R.:

Bedarf in Periode $t$ :

$$
y_{k, t-1}+q_{k t}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t} \quad \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$

Es darf nicht produziert werden, wenn $\gamma_{k t}=0$ ist:

$$
q_{k t}-M \cdot \gamma_{k t} \leq 0
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
Wertebereich:

$$
\begin{array}{ll}
0 \leq q_{k t} \leq \widehat{q}_{k t} & \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T \\
y_{k t} \geq 0 ; y_{k 0}=0 ; y_{k T}=0 ; \gamma_{k t} \text { gegeben } & \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
\end{array}
$$# Modell MLULSP bei gegebenem Rüstmuster 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+p_{k t} \cdot q_{k t}\right)+\text { Rüstkosten }
$$

u. B. d. R.:

Bedarf in Periode $t$ :

$$
y_{k, t-1}+q_{k t}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t} \quad \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$

Es darf nicht produziert werden, wenn $\gamma_{k t}=0$ ist:

$$
\widehat{q}_{k t}=0 \text { für alle } k \in\left\{1,2, \ldots, K \mid \gamma_{k t}=0\right\} \quad(t=1,2, \ldots, T)
$$

Wertebereich:

$$
\begin{array}{ll}
0 \leq q_{k t} \leq \widehat{q}_{k t} & \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T \\
y_{k t} \geq 0 ; y_{k 0}=0 ; y_{k T}=0 ; \gamma_{k t} \text { gegeben } & \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
\end{array}
$$![img-6.jpeg](img-6.jpeg)

# Mehrstufige Losgrößenplanung — Meta-Heuristiken

## Local Search (lokale Suchverfahren)

- deterministische Suchstrategie
- vorübergehendes Zulassen einer Lösungsverschlechterung
  - Simulated Annealing
  - genetische Algorithmen# Lösungsverfahren für mehrstufige Mehrprodukt- 

Losgrößenplanungsprobleme unter
Beachtung von
Kapazitätsbeschränkungen# Eine Relax\&Fix-Heuristik von Maes und van Wassenhove# MLCLSP — Verfahren von Maes 

1. Vollständige Relaxation der Ganzzahligkeitsbedingungen
2. Fixierung von einzelnen Rüstvariablen
$\checkmark$ isoliert einzeln
$\triangleright$ periodenbezogen vorwärts
$\triangleright$ periodenbezogen rückwärts
$\triangleright$ produktbezogen rückwärts
$\triangleright$ maximumorientiert
$\checkmark$ simultan
3. Lösung des resultierenden LPs
$\checkmark$ Wenn alle binären Rüstvariablen ganzzahling sind, Stop!# Eine Fix\&Optimize-Heuristik von Sahling# MLCLSP — Verfahren von Sahling

**Fix-and-Optimize-Heuristik** in bezug auf Subprobleme:

- **Produktorientierte** Identifikation von Subproblemen:
  Die Rüstvariablen für ein Produkt über alle Perioden werden optimiert.

- **Ressourcenorientierte** Identifikation von Subproblemen:
  Alle Rüstvariablen, die sich auf eine Ressource beziehen, – ggf. reduziert auf verschiedene, sich überlappende Zeitfenster – werden optimiert.

- **Prozessorientierte** Identifikation von Subproblemen:
  Die Rüstvariablen für Produkte, die durch direkte Vorgänger-Nachfolger-Beziehungen miteinander verbunden sind, – ggf. reduziert auf einzelne Zeitfenster – werden optimiert.

Alle nicht betrachteten Produkte und Perioden werden mit den besten gefundenen Werten für die binären Rüstvariablen vorbesetzt. Im Unterschied zu den Relax-and-Fix-Heuristiken gibt es nur ganzzahlige Lösungen für die Rüstvariablen.# Integration der Losgrößen- und Materialbedarfsplanung in ein PPS-System# MRP-Konzept: Grundstruktur

## Hauptproduktionsprogrammplanung

![img-7.jpeg](img-7.jpeg)

- **Mengenplanung** („MRP-Lauf“)
  - Erzeugnis *k* + 2, ... (nach Dispositionsstufen sortiert)
  - Erzeugnis *k* + 1
  - Erzeugnis *k*

- **Nettobedarfsrechnung**
  - Bestellmengen- bzw. Losgrößenrechnung

- **Terminplanung**
  - Durchlaufterminierung
  - Netzplantechnik
  - Kapazitätsbelastungsausgleich
  - zeitliche Verschiebung oder Kapazitätsanpassung

- **Feinplanung und -steuerung** („Scheduling“)

(vgl. Günther/Tempelmeier (2009))

Univ.-Prof. Dr. Michael Manitz

Material-Logistik: Bestandsmanagement

77-3![img-8.jpeg](img-8.jpeg)

# MRP™-Konzept

## Hauptproduktionsprogrammplanung

- **Muster Production Scheduling**
- **Rough-Cut Capacity Planning**
- **Zulässigkeitsprüfung**

## Mehrstufige, kapazitätsorientierte Mehrprodukt-Losgrößenplanung (MLCLSP)

- **Kapazitätsorientierte Ressourceneinsatzplanung (RCPSP)**
- **Feinplanung und -steuerung**

(vgl. Günther/Tempelmeier (2009))

Univ.-Prof. Dr. Michael Manitz

Material-Logistik: Bestandsmanagement

80-2# Materialdisposition in einem Konzept der rollierenden Planung# Mehrstufige Losgrößenplanung

## Rollierende Losgrößenplanung

![img-9.jpeg](img-9.jpeg)

*Univ.-Prof. Dr. Michael Manitz*

*Material-Logistik: Bestandsmanagement*

*84-1*# Mehrstufige Losgrößenplanung

## Beispiel Rollierende Planung (MLCLSP)

## Erzeugnisstruktur:

![img-10.jpeg](img-10.jpeg)

Primärbedarfsmengen:

|  $t$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  $d_{1 t}$ | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 | 106 | 103 | 93  |
|  $d_{2 t}$ | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 | 131 | 154 | 139  |

Weitere Daten: $b_{\mathrm{A} t}=350, b_{\mathrm{B} t}=500$ $s_{1}=s_{2}=s_{3}=400 ; h_{1}=h_{2}=2, h_{3}=1$ $\mathrm{tb}*{1}=\mathrm{tb}*{2}=\mathrm{tb}*{3}=1, \mathrm{tr}*{1}=\mathrm{tr}*{2}=\mathrm{tr}*{3}=0$ $z_{1}=z_{2}=0, z_{3}=2$# Mehrstufige Losgrößenplanung 

## Lagerbilanzgleichungen

$$
y_{k, t-1}+q_{k t}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t}
$$

$$
\binom{k \in \mathcal{K}}{t=1, \ldots, T}
$$# Mehrstufige Losgrößenplanung 

## Lagerbilanzgleichungen

$$
y_{k, t-1}+q_{k, t-z_{k}}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t}
$$

$$
\binom{k \in \mathcal{K}}{t=z_{k}+1, \ldots, T}
$$# Mehrstufige Losgrößenplanung 

Lagerbilanzgleichungen (im Planungslauf zum Zeitpunkt 0)

$$
y_{k, t-1}+q_{k, t-z_{k}}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t} \quad\left(\begin{array}{l}
k \in \mathcal{K} \\
t=0+z_{k}+1, \ldots, 0+T
\end{array}\right)
$$# Mehrstufige Losgrößenplanung 

Lagerbilanzgleichungen (im Planungslauf am Ende von Periode $\tau$ )

$$
y_{k, t-1}+q_{k, t-z_{k}}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t} \quad\binom{k \in \mathcal{K}}{t=\tau+z_{k}+1, \ldots, \tau+T}
$$# Mehrstufige Losgrößenplanung 

Lagerbilanzgleichungen (im Planungslauf am Ende von Periode $\tau=n \cdot R$ )

$$
y_{k, t-1}+q_{k, t-z_{k}}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t} \quad\binom{k \in \mathcal{K}}{t=\tau+z_{k}+1, \ldots, \tau+T}
$$# Mehrstufige Losgrößenplanung 

Lagerbilanzgleichungen (im Planungslauf am Ende von Periode $\tau=n \cdot R$ )

$$
y_{k, t-1}+q_{k, t-z_{k}}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t} \quad\binom{k \in \mathcal{K}}{t=\tau+z_{k}+1, \ldots, \tau+T}
$$

Lagerbilanzgleichungen mit aus dem vorherigen Planungslauf übernommenen Zugangsmengen $x_{k t}$

$$
y_{k, t-1}+x_{k t}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t}
$$

$$
\binom{k \in \mathcal{K}}{t=\tau+1, \ldots, \tau+z_{k}}
$$# Mehrstufige Losgrößenplanung 

Lagerbilanzgleichungen (im Planungslauf am Ende von Periode $\tau=n \cdot R$ )

$$
y_{k, t-1}+q_{k, t-z_{k}}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t} \quad\binom{k \in \mathcal{K}}{t=\tau+z_{k}+1, \ldots, \tau+T}
$$

Lagerbilanzgleichungen mit aus dem vorherigen Planungslauf übernommenen Zugangsmengen $x_{k t}$

$$
y_{k, t-1}+x_{k t}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t}
$$

$$
\binom{k \in \mathcal{K}}{t=\tau+1, \ldots, \tau+z_{k}}
$$

$$
(n=0,1,2, \ldots)
$$# Mehrstufige Losgrößenplanung 

Lagerbilanzgleichungen (im Planungslauf am Ende von Periode $\tau=n \cdot R$ )

$$
y_{k, t-1}+q_{k, t-z_{k}}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t} \quad\binom{k \in \mathcal{K}}{t=\tau+z_{k}+1, \ldots, \tau+T}
$$

Lagerbilanzgleichungen mit aus dem vorherigen Planungslauf übernommenen Zugangsmengen $x_{k t}$

$$
\begin{aligned}
& y_{k, t-1}+x_{k t}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t} \\
& \binom{k \in \mathcal{K}}{t=\tau+1, \ldots, \tau+z_{k}} \\
& (n=0,1,2, \ldots)
\end{aligned}
$$

Beispiel Rollierende Planung zum Zeitpunkt $\tau=0: x_{31}=292, x_{32}=350$

$$
\begin{aligned}
& y_{30}+292-q_{11}-q_{21}-y_{31}=0 \\
& y_{31}+350-q_{12}-q_{22}-y_{32}=0 \\
& y_{32}+q_{31}-q_{13}-q_{23}-y_{33}=0
\end{aligned}
$$

USW.# 8 Beispiel MLCLSP für 8 Perioden (s.o.)

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

|  $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111  |
|  $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0  |
|  $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0  |
|  $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153  |
|  $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153  |
|  $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0  |
|  |   |   |   |   |   |   |   |   |   |   |# 8 Beispiel MLCLSP für 8 Perioden (s.o.)

(vii. Tempelmeier (2008)) Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

|  $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111  |
|  $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0  |
|  $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0  |
|  $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153  |
|  $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153  |
|  $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0  |
|  Sekundärbedarf $_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153  |# 8 Beispiel MLCLSP für 8 Perioden (s.o.)

(vii. Tempelmeier (2008)) Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

|  $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111  |
|  $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0  |
|  $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0  |
|  $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153  |
|  $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153  |
|  $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0  |
|  Sekundärbedarf $_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153  |
|  $x_{3, t+2}$ | 292 | 350 |  |  |  |  |  |  |  |   |# 8 Beispiel MLCLSP für 8 Perioden (s.o.)

(vii. Tempelmeier (2008)) Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

|  $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111  |
|  $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0  |
|  $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0  |
|  $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153  |
|  $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153  |
|  $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0  |
|  Sekundärbedarf $_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153  |
|  $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | -  |# 8 Beispiel MLCLSP für 8 Perioden (s.o.)

(vii. Tempelmeier (2008)) Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

|  $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111  |
|  $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0  |
|  $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0  |
|  $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153  |
|  $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153  |
|  $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0  |
|  Sekundärbedarf $_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153  |
|  $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | -  |
|  $y_{3 t}$ |  | 0 | 0 | 0 | 73 | 245 | 3 | 3 | 153 | 0  |# 8 Beispiel MLCLSP für 8 Perioden (s.o.)

(vii. Tempelmeier (2008)) Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

|  $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111  |
|  $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0  |
|  $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0  |
|  $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153  |
|  $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153  |
|  $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0  |
|  Sekundärbedarf $_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153  |
|  $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | -  |
|  $y_{3 t}$ |  | 0 | 0 | 0 | 73 | 245 | 3 | 3 | 153 | 0  |

$y_{31}=y_{30}+x_{31}-$ Sekundärbedarf $_{31}=0+292-292=0$ $y_{32}=y_{31}+x_{32}-$ Sekundärbedarf $_{32}=0+350-350=0$# Beispiel MLCLSP für 8 Perioden (s.o.)

(vii. Tempelmeier (2008))

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

|  $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111  |
|  $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0  |
|  $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0  |
|  $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153  |
|  $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153  |
|  $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0  |
|  Sekundärbedarf $_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153  |
|  $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | -  |
|  $y_{3 t}$ |  | 0 | 0 | 0 | 73 | 245 | 3 | 3 | 153 | 0  |

$y_{31}=y_{30}+x_{31}-$ Sekundärbedarf $_{31}=0+292-292=0$ $y_{32}=y_{31}+x_{32}-$ Sekundärbedarf $_{32}=0+350-350=0$ $y_{33}=y_{32}+q_{31}-$ Sekundärbedarf $_{33}=0+377-304=73$ $y_{34}=y_{33}+q_{32}-$ Sekundärbedarf $_{34}=73+500-328=245$ $y_{35}=y_{34}+q_{33}-$ Sekundärbedarf $_{35}=245+0-242=3$ usw.# 8 Beispiel MLCLSP für 8 Perioden (s.o.)

(vii. Tempelmeier (2008)) Optimale Lösung beim zweiten Planungslauf im Zeitpunkt $\tau=3$ :

|  $t$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  $t^{\prime}$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8  |
|  $d_{1 t}$ |  |  | 118 | 104 | 106 | 101 | 111 | 106 | 103 | 93  |
|  $q_{1 t}$ |  |  | 328 | 0 | 0 | 212 | 0 | 209 | 0 | 93  |
|  $y_{1 t}$ |  | 0 | 210 | 106 | 0 | 111 | 0 | 103 | 0 | 0  |
|  $d_{2 t}$ |  |  | 156 | 125 | 116 | 139 | 153 | 131 | 154 | 139  |
|  $q_{2 t}$ |  |  | 0 | 242 | 0 | 138 | 284 | 0 | 293 | 0  |
|  $y_{2 t}$ |  | 156 | 0 | 117 | 1 | 0 | 131 | 0 | 139 | 0  |
|  Sekundärbedarf $_{3 t}$ |  |  | 328 | 242 | 0 | 350 | 284 | 209 | 293 | 93  |
|  $x_{3, t+2}$ | 500 | 0 | - | - | - | - | - | - | - | -  |
|  $q_{3 t}$ | - | - | 0 | 347 | 493 | 0 | 386 | 0 | - | -  |
|  $y_{3 t}$ |  | 73 | 245 | 3 | 3 | 0 | 209 | 0 | 93 | 0  |