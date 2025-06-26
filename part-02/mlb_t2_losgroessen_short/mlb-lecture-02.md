# Bestandsmanagement unter deterministischen Bedingungen (,,Bestellmengen- bzw. Losgrößenplanung")Materialbereitstellungsprinzipien:
einsatzsynchrone Materialbereitstellung im Bedarfsfall
Einzelbeschaffung im Bedarfsfall
Vorratshaltung:
Zusammenfassung von (Netto-)Bedarfsmengen zu größeren Produkti-ons- bzw. Beschaffungslosen
$\triangleright$ um Rüstvorgänge einzusparen

- Rüstkosten (direkt zurechenbare Kosten)
- Rüstzeiten (Opportunitätskosten)
$\triangleright$ unter Inkaufnahme von Lagerkosten durch Vorausproduktion bzw. Vorabbestellung
$\triangleright$ auf Grund knapper Kapazitäten# Losgrößenplanung

Charakterisierung von Losgrößenplanungsproblemen

|  Grad der Ab-
hängigkeit | Niveau der Bedarfsmengen |   |
| --- | --- | --- |
|   | gleichbleibend | schwankend  |
|  unabhängig | statische Losgrößenproble-
me mit unabhängigem Be-
darf | dynamische Losgrößenpro-
bleme mit unabhängigem
Bedarf  |
|  abhängig | statische Losgrößenproble-
me mit abhängigem Bedarf | dynamische Losgrößenpro-
bleme mit abhängigem Be-
darf  |# Losgrößenplanung

Gemeinsame Entwicklung des Lagerbestands zweier durch direkte Input-Output-Beziehungen miteinander verbundener Erzeugnisse:

![img-0.jpeg](img-0.jpeg)

*Lagerbestand*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

*Lagerkennzweier*

# Losgrößenplanung

Gemeinsame Entwicklung des Lagerbestands zweier durch direkte Input-Output-Beziehungen miteinander verbundener Erzeugnisse:

![img-1.jpeg](img-1.jpeg)

(1) Bestand

(2) Zeit

(3) Einfache Zeit

(4) 2

(5) 1

(6) 2

Univ.-Prof. Dr. Michael Manitz

Material-Logistik: Bestandsmanagement

32-21# Losgrößenplanung

Gemeinsame Entwicklung des Lagerbestands zweier durch direkte Input-Output-Beziehungen miteinander verbundener Erzeugnisse:

![img-2.jpeg](img-2.jpeg)

(1) Bestand

(2) Zeit

(3) Einfache Zeit

(4) 1

(5) 2

Univ.-Prof. Dr. Michael Manitz

Material-Logistik: Bestandsmanagement

32-22# Dynamische Losgrößenplanung# Das dynamische 

## Einprodukt-Losgrößenproblem# Modell SIULSP 

Was muss festgelegt werden:
... Soll für das betrachtete Erzeugnis in Periode $t$ ein Los aufgelegt werden?
... Wieviel soll ggf. produziert werden?
... Wieviel Lagerbestand ist damit verbunden?# Modell SIULSP 

Was muss festgelegt werden - Entscheidungsvariable:
$\gamma_{t} \in\{0,1\}$... Binärvariable zur Kennzeichnung, ob das betrachtete Erzeugnis in Periode $t$ produziert wird

$$
\gamma_{t}= \begin{cases}1, & \text { wenn ein Los in Periode } t \text { aufgelegt wird } \\ 0 & \text { sonst }\end{cases}
$$

$q_{t} \quad$... Produktionsmenge in Periode $t$
$y_{t} \quad$... Lagerbestand am Ende von Periode $t$# Modell SIULSP 

Was ist gegeben - Daten:
$d_{t} \quad$... Bedarf in Periode $t$
$y^{(0)} \quad$... Anfangslagerbestand
$s \quad$... Rüstkostensatz
$h \quad$... Lagerkostensatz
$p_{t} \quad$... variable Produktionskosten in Periode $t$
$M$... eine große Zahl, die größer sein muss als die maximal mögliche Losgröße# Modell SIULSP 

Minimiere die Summe aus Rüst-, Lager- und variablen Produktionskosten:

$$
Z=\sum_{t=1}^{T}\left(h \cdot y_{t}+s \cdot \gamma_{t}+p_{t} \cdot q_{t}\right)
$$

u. B. d. R.:

Anfangslagerbestand:

$$
y_{0}=y^{(0)}
$$

Lagerbilanz: Anfangsbestand + Zugänge - Abgänge $=$ Endbestand

$$
y_{t-1}+q_{t}-d_{t}=y_{t}
$$

für alle $t=1,2, \ldots, T$# Modell SIULSP 

Minimiere die Summe aus Rüst-, Lager- und variablen Produktionskosten:

$$
Z=\sum_{t=1}^{T}\left(h \cdot y_{t}+s \cdot \gamma_{t}+p_{t} \cdot q_{t}\right)
$$

u. B. d. R.:

Anfangslagerbestand:

$$
y_{0}=y^{(0)}
$$

Lagerbilanz: Anfangsbestand + Zugänge - Endbestand = Abgänge

$$
y_{t-1}+q_{t}-y_{t}=d_{t}
$$

für alle $t=1,2, \ldots, T$# Modell SIULSP 

Minimiere die Summe aus Rüst-, Lager- und variablen Produktionskosten:

$$
Z=\sum_{t=1}^{T}\left(h \cdot y_{t}+s \cdot \gamma_{t}\right)
$$

u. B. d. R.:

Anfangslagerbestand:

$$
y_{0}=y^{(0)}
$$

Bedarf in Periode $t$ :

$$
y_{t-1}+q_{t}-y_{t}=d_{t}
$$

für alle $t=1,2, \ldots, T$
Es muss gerüstet werden, wenn $q_{t}>0$ ist:

$$
q_{t}-M_{t} \cdot \gamma_{t} \leq 0
$$

für alle $t=1,2, \ldots, T$
Wertebereich:

$$
q_{t} \geq 0 ; y_{t} \geq 0 ; \gamma_{t} \in\{0,1\}
$$

für alle $t=1,2, \ldots, T$# Dynamische Einprodukt-Losgrößenplanung (SIULSP) 

$$
M_{t} \geqq \sum_{j=t}^{!} d_{j}=: D_{t T}
$$

$$
(t=1,2, \ldots, T)
$$# Modell SIULSP 

Minimiere die Summe aus Rüst-, Lager- und variablen Produktionskosten:

$$
Z=\sum_{t=1}^{T}\left(h \cdot y_{t}+s \cdot \gamma_{t}+p_{t} \cdot q_{t}\right)
$$

u. B. d. R.:

Anfangslagerbestand:

$$
y_{0}=y^{(0)}
$$

Bedarf in Periode $t$ :

$$
y_{t-1}+q_{t}-y_{t}=d_{t}
$$

für alle $t=1,2, \ldots, T$
Es muss gerüstet werden, wenn $q_{t}>0$ ist:

$$
q_{t}-M_{t} \cdot \gamma_{t} \leq 0
$$

für alle $t=1,2, \ldots, T$
Wertebereich:

$$
q_{t} \geq 0 ; y_{t} \geq 0 ; y_{T} \geq 0 ; \gamma_{t} \in\{0,1\}
$$

für alle $t=1,2, \ldots, T$# Modell SIULSP 

Minimiere die Summe aus Rüst-, Lager- und variablen Produktionskosten:

$$
Z=\sum_{t=1}^{T}\left(h \cdot y_{t}+s \cdot \gamma_{t}+p_{t} \cdot q_{t}\right)
$$

u. B. d. R.:

Anfangslagerbestand:

$$
y_{0}=y^{(0)}
$$

Bedarf in Periode $t$ :

$$
y_{t-1}+q_{t}-y_{t}=d_{t}
$$

für alle $t=1,2, \ldots, T$
Es muss gerüstet werden, wenn $q_{t}>0$ ist:

$$
q_{t}-D_{t T} \cdot \gamma_{t} \leq 0
$$

für alle $t=1,2, \ldots, T$
Wertebereich:

$$
q_{t} \geq 0 ; y_{t} \geq 0 ; y_{T} \geq 0 ; \gamma_{t} \in\{0,1\}
$$

für alle $t=1,2, \ldots, T$# Dynamische Einprodukt-Losgrößenplanung (SIULSP) 

$$
M_{t} \geqq \sum_{j=t}^{!} d_{j}=: D_{t T} \Longrightarrow q_{t}-D_{t T} \cdot \gamma_{t} \leq 0
$$

$$
(t=1,2, \ldots, T)
$$$$
M_{t} \geqq \sum_{j=t}^{!} d_{j}=: D_{t T} \Longrightarrow q_{t}-D_{t T} \cdot \gamma_{t} \leq 0
$$

Wagner-Whitin-Eigenschaft (bei unbeschränkten Kapazitäten)
$q_{t} \cdot y_{t-1}=0$

- Es wird in Periode $t$ nur dann ein neues Los aufgelegt $\left(q_{t}>0\right)$, wenn der Lagerbestand erschöpft ist $\left(y_{t-1}=0\right)$.
- Wenn Lagerbestand übernommen wird $\left(y_{t-1}>0\right)$, dann ist der Lagerbestand mindestens so groß, dass er den aktuellen Bedarf decken kann $\left(y_{t-1} \geq d_{t}\right)$. Die noch bereitzustellende Menge ist dann $q_{t}=0$.
- Überflüssige Bestände kann es nicht geben, bei denen man trotz Lagerkosten keine Rüstkosten einspart.
$\Longrightarrow$ Nur ganze Periodenbedarfsmengen werden zu Losen zusammengefasst!# Lösungsverfahren für das dynamische 

## Einprodukt-Losgrößenproblem# Exakte Lösung mit dynamischer Optimierung# Beispiele SIULSP

- Rüstkostensatz: $s=500$ GE pro Rüstvorgang
- Lagerkostensatz: $h=1$ GE pro ME und Periode
- keine entscheidungsrelevanten variablen Produktionskosten

|  Periode $t$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  Bedarfsmenge $d_{t}$ | 20 | 80 | 160 | 85 | 120 | 100  |# Beispiel SIULSP

- Rüstkostensatz: $s=500$ GE pro Rüstvorgang
- Lagerkostensatz: $h=1$ GE pro ME und Periode
- keine entscheidungsrelevanten variablen Produktionskosten

|  Periode $t$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  Bedarfsmenge $d_{t}$ | 20 | 80 | 160 | 85 | 120 | 100  |

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Kosten für den Planungszeitraum von 6 Perioden:

- $C_{6}=C_{5}+c_{66}$
- $C_{6}=C_{4}+c_{56}$
- $C_{6}=C_{3}+c_{46}$
- $C_{6}=C_{2}+c_{36}$
- $C_{6}=C_{1}+c_{26}$
- $C_{6}=c_{16}$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Kosten für den Planungszeitraum von $T$ Perioden: $C_{T}=C_{i}+c_{i+1, T} \quad(i=1,2, \ldots, T-1)$ Minimale Kosten einer Lospolitik für die ersten $i$ Planungsperioden: $f_{i}=\min *{1 \leq \tau \leq i}\left{f*{\tau-1}+c_{\tau i}\right} \quad(i=1,2, \ldots, T)$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 1:# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 1: $f_{1}=c_{11}=500$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 1: $f_{1}=c_{11}=500 \Longrightarrow P_{1}^{\text {opt }}=\left(p_{11}\right)$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 2:# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 2: $f_{2}=\min \left{c_{12}, f_{1}+c_{22}\right}$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 2: $f_{2}=\min \left{ c_{12}, f_{1}+c_{22}\right}=\min {580,500+500}$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 2: $f_{2}=\min \left{c_{12}, f_{1}+c_{22}\right}=\min {580,500+500}=580$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 2: $f_{2}=\min \left{c_{12}, f_{1}+c_{22}\right}=\min {580,500+500}=580 \Longrightarrow P_{2}^{\text {opt }}=\left(p_{12}\right)$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 3:# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 3: $f_{3}=\min \left{c_{13}, f_{1}+c_{23}, f_{2}+c_{33}\right}$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 3: $f_{3}=\min \left{c_{13}, f_{1}+c_{23}, f_{2}+c_{33}\right}=\min {900,500+660,580+500}$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 3: $f_{3}=\min \left{c_{13}, f_{1}+c_{23}, f_{2}+c_{33}\right}=\min {900,500+660,580+500}=900$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 3: $f_{3}=\min \left{c_{13}, f_{1}+c_{23}, f_{2}+c_{33}\right}=\min {900,500+660,580+500}=900$ $\Longrightarrow P_{3}^{\text {opt }}=\left(p_{13}\right)$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 4:# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 4: $f_{4}=\min \left{c_{14}, f_{1}+c_{24}, f_{2}+c_{34}, f_{3}+c_{44}\right}$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 4: $f_{4}=\min {1155,500+830,580+585,900+500}$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 4: $f_{4}=\min {1155,500+830,580+585,900+500}=1155$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 4: $f_{4}=\min {1155,500+830,580+585,900+500}=1155$ $\Longrightarrow P_{4}^{\text {opt }}=\left(p_{14}\right)$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 5:# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 5: $f_{5}=\min \left{c_{15}, f_{1}+c_{25}, f_{2}+c_{35}, f_{3}+c_{45}, f_{4}+c_{55}\right}$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 5: $f_{5}=\min {1635,500+1190,580+825,900+620,1155+500}$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 5: $f_{5}=\min {1635,500+1190,580+825,900+620,1155+500}=1405$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 5: $f_{5}=\min {1635,500+1190,580+825,900+620,1155+500}=1405$ $\Longrightarrow P_{5}^{\text {opt }}=\left(P_{2}^{\text {opt }}, p_{35}\right)$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 5: $f_{5}=\min {1635,500+1190,580+825,900+620,1155+500}=1405$ $\Longrightarrow P_{5}^{\text {opt }}=\left(P_{2}^{\text {opt }}, p_{35}\right)=\left(p_{12}, p_{35}\right)$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 6:# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 6: $f_{6}=\min \left{c_{16}, f_{1}+c_{26}, f_{2}+c_{36}, f_{3}+c_{46}, f_{4}+c_{56}, f_{5}+c_{66}\right}$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 6: $f_{6}=\min {2135,500+1590,580+1125,900+820,1155+600,1405+500}$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 6: $f_{6}=\min {2135,500+1590,580+1125,900+820,1155+600,1405+500}=1705$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 6: $f_{6}=\min {2135,500+1590,580+1125,900+820,1155+600,1405+500}=1705$ $\Longrightarrow P_{6}^{\text {opt }}=\left(P_{2}^{\text {opt }}, p_{36}\right)$# Beispiel SIULSP

Kosten $c_{\tau j}$ einer (ökonomisch sinnvollen) Teilpolitik $p_{\tau j}$ (eines Loses), die die Bedarfsmengen $d_{\tau}$ bis $d_{j}$ abdeckt $\quad(\tau=1,2, \ldots, 6, j=\tau, \tau+1, \ldots, 6)$

|  letzte Bedarfsperiode $(j)$
Bereitstellungsperiode $(\tau)$ | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 500 | 580 | 900 | 1155 | 1635 | 2135  |
|  2 | - | 500 | 660 | 830 | 1190 | 1590  |
|  3 | - | - | 500 | 585 | 825 | 1125  |
|  4 | - | - | - | 500 | 620 | 820  |
|  5 | - | - | - | - | 500 | 600  |
|  6 | - | - | - | - | - | 500  |

Minimale Kosten einer Lospolitik bis zur Periode 6: $f_{6}=\min {2135,500+1590,580+1125,900+820,1155+600,1405+500}=1705$ $\Longrightarrow P_{6}^{\text {opt }}=\left(P_{2}^{\text {opt }}, p_{36}\right)=\left(p_{12}, p_{36}\right)$# Vom klassischen Losgrößenmodell inspirierte Praxisheuristiken# Dynamische Einprodukt-Losgrößenplanung (SIULSP) 

Heuristische Lösungsverfahren:

- Stückkostenverfahren (Least-Unit-Cost-Verfahren)

Vergrößere $j$, solange die durchschnittlichen Stückkosten sinken!# Dynamische Einprodukt-Losgrößenplanung (SIULSP) 

## Heuristische Lösungsverfahren:

- Stückkostenverfahren (Least-Unit-Cost-Verfahren)

Vergrößere $j$, solange $c_{\tau j}=\frac{s+h \cdot \sum_{t=\tau}^{j}(t-\tau) \cdot d_{t}}{\sum_{t=\tau}^{j} d_{t}}$ sinkt!# Dynamische Einprodukt-Losgrößenplanung (SIULSP) 

Heuristische Lösungsverfahren:

- Stückkostenverfahren (Least-Unit-Cost-Verfahren)

Vergrößere $j$, solange $c_{\tau j}=\frac{s+h \cdot \sum_{t=\tau}^{j}(t-\tau) \cdot d_{t}}{\sum_{t=\tau}^{j} d_{t}}$ sinkt!

- Stückperiodenausgleichsverfahren (Part-Period-Verfahren)

Vergrößere $j$, solange Lagerkosten $\leq$ Rüstkosten!# Dynamische Einprodukt-Losgrößenplanung (SIULSP) 

Heuristische Lösungsverfahren:

- Stückkostenverfahren (Least-Unit-Cost-Verfahren)

Vergrößere $j$, solange $c_{\tau j}=\frac{s+h \cdot \sum_{t=\tau}^{j}(t-\tau) \cdot d_{t}}{\sum_{t=\tau}^{j} d_{t}}$ sinkt!

- Stückperiodenausgleichsverfahren (Part-Period-Verfahren)

Vergrößere $j$, solange $\sum_{t=\tau}^{j}(t-\tau) \cdot d_{t} \leq \frac{s}{h}$ !# Dynamische Einprodukt-Losgrößenplanung (SIULSP) 

Heuristische Lösungsverfahren:

- Stückkostenverfahren (Least-Unit-Cost-Verfahren)

Vergrößere $j$, solange $c_{\tau j}=\frac{s+h \cdot \sum_{t=\tau}^{j}(t-\tau) \cdot d_{t}}{\sum_{t=\tau}^{j} d_{t}}$ sinkt!

- Stückperiodenausgleichsverfahren (Part-Period-Verfahren)

Vergrößere $j$, solange $\sum_{t=\tau}^{j}(t-\tau) \cdot d_{t} \leq \frac{s}{h}$ !

- Silver-Meal-Verfahren

Vergrößere $j$, solange die durchschnittlichen Kosten pro ZE sinken!# Dynamische Einprodukt-Losgrößenplanung (SIULSP) 

Heuristische Lösungsverfahren:

- Stückkostenverfahren (Least-Unit-Cost-Verfahren)

Vergrößere $j$, solange $c_{\tau j}=\frac{s+h \cdot \sum_{t=\tau}^{j}(t-\tau) \cdot d_{t}}{\sum_{t=\tau}^{j} d_{t}}$ sinkt!

- Stückperiodenausgleichsverfahren (Part-Period-Verfahren)

Vergrößere $j$, solange $\sum_{t=\tau}^{j}(t-\tau) \cdot d_{t} \leq \frac{s}{h}$ !

- Silver-Meal-Verfahren

Vergrößere $j$, solange $c_{\tau j}=\frac{s+h \cdot \sum_{t=\tau}^{j}(t-\tau) \cdot d_{t}}{j-\tau+1}$ sinkt!# Das dynamische einstufige Mehrprodukt-Losgrößenproblem# Modell SIULSP 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{t=1}^{T}\left(h \cdot y_{t}+s \cdot \gamma_{t}+p_{t} \cdot q_{t}\right)
$$

u. B. d. R.:

Bedarf in Periode $t$ :

$$
y_{t-1}+q_{t}-y_{t}=d_{t}
$$

für alle $t=1,2, \ldots, T$
Es muss gerüstet werden, wenn $q_{t}>0$ ist:

$$
q_{t}-M \cdot \gamma_{t} \leq 0
$$

für alle $t=1,2, \ldots, T$
Wertebereich:

$$
q_{t} \geq 0 ; y_{t} \geq 0 ; y_{0}=0 ; y_{T}=0 ; \gamma_{t} \in\{0,1\}
$$

für alle $t=1,2, \ldots, T$# Modell SIULSP 

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
Es muss gerüstet werden, wenn $q_{k t}>0$ ist:

$$
q_{k t}-M \cdot \gamma_{k t} \leq 0
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
Wertebereich:

$$
q_{k t} \geq 0 ; y_{k t} \geq 0 ; y_{k 0}=0 ; y_{k T}=0 ; \gamma_{k t} \in\{0,1\} \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$# Modell SIULSP 

Was ist gegeben - Indexmengen:
$\mathcal{K} \ldots$ die Menge der betrachteten Produkte

Was ist gegeben - Daten:
$d_{k t} \quad \ldots$ Bedarf für Produkt $k$ in Periode $t$
$y_{k}^{(0)} \quad \ldots$ Anfangslagerbestand für Produkt $k$
$s_{k} \quad \ldots$ Rüstkostensatz für Produkt $k$
$h_{k} \quad \ldots$ Lagerkostensatz für Produkt $k$
$p_{k t} \quad \ldots$ variable Produktionskosten für Produkt $k$ in Periode $t$# Modell SIULSP 

Was ist gegeben - Indexmengen:
$\mathcal{K}$... die Menge der betrachteten Produkte
$\mathcal{J}$... die Menge der gemeinsam genutzten Ressourcen

Was ist gegeben - Daten:
$d_{k t} \quad$... Bedarf für Produkt $k$ in Periode $t$
$y_{k}^{(0)} \quad$... Anfangslagerbestand für Produkt $k$
$s_{k} \quad$... Rüstkostensatz für Produkt $k$
$h_{k} \quad$... Lagerkostensatz für Produkt $k$
$p_{k t} \quad$... variable Produktionskosten für Produkt $k$ in Periode $t$# Modell CLSP 

Was ist gegeben - Indexmengen:
$\mathcal{K}$... die Menge der betrachteten Produkte
$\mathcal{J}$... die Menge der gemeinsam genutzten Ressourcen

Was ist gegeben - Daten:
$d_{k t} \quad$... Bedarf für Produkt $k$ in Periode $t$
$y_{k}^{(0)} \quad$... Anfangslagerbestand für Produkt $k$
$s_{k} \quad$... Rüstkostensatz für Produkt $k$
$h_{k} \quad$... Lagerkostensatz für Produkt $k$
$p_{k t} \quad$... variable Produktionskosten für Produkt $k$ in Periode $t$
$\mathrm{tb}_{j k} \quad$... Stückbearbeitungszeit für Produkt $k$ auf Ressource $j$
$\operatorname{tr}_{j k} \quad$... Rüstzeit für Produkt $k$ auf Ressource $j$
$b_{j t} \quad$... Kapazität der Ressource $j$ in Periode $t$# Modell CLSP 

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
Es muss gerüstet werden, wenn $q_{k t}>0$ ist:

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

Bedarf in Periode $t$ :

$$
y_{k, t-1}+q_{k t}-y_{k t}=d_{k t}
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$

Es muss gerüstet werden, wenn $q_{k t}>0$ ist:

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

Bedarf in Periode $t$ :

$$
y_{k, t-1}+q_{k t}-y_{k t}=d_{k t}
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
Kapazitäten in Periode $t$ :

$$
\sum_{k \in \mathcal{K}}\left(\operatorname{tb}_{j k} \cdot q_{k t}+\operatorname{tr}_{j k} \cdot \gamma_{k t}\right) \leq b_{j t}
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
$$# Das dynamische einstufige Mehrprodukt-Losgrößenproblem mit Rüstzustandsübernahme# Übernahme des Rüstzustands von Periode $t$ nach $t+1$ 

- Ein Erzeugnis wird als letztes in Periode $t$ und als erstes in Periode $t+1$ produziert.
- Am Ende der Periode $t$ wird Leerzeit der Maschine genutzt, um für das erste in Periode $t+1$ zu produzierende Produkt umzurüsten

Falls in der Periode $t$ überhaupt nicht produziert wird,

- kann gerüstet und der Rüstzustand in die nächste Periode übertragen werden.
- kann der aus der Vorperiode übernommene Rüstzustand in die nächste Periode übertragen werden.