# PLSP - Ein 

## Mikroperioden-Modell für das dynamische einstufige

Mehrprodukt-Losgrößenproblem# Dynamische Mehrprodukt-Losgrößenplanung (PLSP) 

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement# Dynamische Mehrprodukt-Losgrößenplanung (PLSP) 

Annahmen:
Der Rüstzustand kann übernommen werden.
Es kann in einer Periode maximal einmal umgerüstet werden.
Es können maximal zwei verschiedene Erzeugnisse in einer Periode produziert werden.# Modell CLSP 

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
$$

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement# Modell CLSP 

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
für alle $t=1,2, \ldots, T$
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
& q_{k t}-M \cdot \gamma_{k t} \leq 0
\end{aligned}
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$ für alle $t=1,2, \ldots, T$
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

$$
\sum_{k \in \mathcal{K}} \omega_{k t} \leq 1
$$

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

$$
\sum_{k \in \mathcal{K}} \omega_{k t} \leq 1
$$

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

$$
\begin{aligned}
& \sum_{k \in \mathcal{K}} \omega_{k t} \leq 1 \\
& \gamma_{k t} \geq \omega_{k t}-\omega_{k, t-1}
\end{aligned}
$$

für alle $t=1,2, \ldots, T$
für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$# Dynamische Mehrprodukt-Losgrößenplanung 

## Beispiel PLSP

| Bedarfsmengen |  |  |  |  |  | Parameter |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | $h_{k}$ | $s_{k}$ | $\mathrm{tb}_{k}$ | $\operatorname{tr}_{k}$ |
| 1 | 30 | - | 80 | - | 40 | 1 | 100 | 1 | 10 |
| 2 | - | - | 30 | - | 70 | 1 | 100 | 1 | 10 |
| 3 | - | - | 40 | - | 60 | 1 | 100 | 1 | 10 |# Dynamische Mehrprodukt-Losgrößenplanung 

## Beispiel PLSP

| Bedarfsmengen |  |  |  |  |  | Parameter |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | $h_{k}$ | $s_{k}$ | $\mathrm{tb}_{k}$ | $\operatorname{tr}_{k}$ |
| 1 | 30 | - | 80 | - | 40 | 1 | 100 | 1 | 10 |
| 2 | - | - | 30 | - | 70 | 1 | 100 | 1 | 10 |
| 3 | - | - | 40 | - | 60 | 1 | 100 | 1 | 10 |
| Produktionsmengen |  |  |  |  |  |  |  |  |  |
| Erzeugnis $k$ |  |  |  |  |  |  |  |  |  |
| 1 | 30 | 80 | - | 20 | 20 |  |  |  |  |
| 2 | - | - | 30 | - | 70 |  |  |  |  |
| 3 | - | - | 40 | 60 | - |  |  |  |  |# Dynamische Mehrprodukt-Losgrößenplanung 

## Beispiel PLSP

| Bedarfsmengen |  |  |  |  |  |  | Parameter |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | $h_{k}$ | $s_{k}$ | $\mathrm{tb}_{k}$ | $\operatorname{tr}_{k}$ |  |
| 1 | 30 | - | 80 | - | 40 | 1 | 100 | 1 | 10 |  |
| 2 | - | - | 30 | - | 70 | 1 | 100 | 1 | 10 |  |
| 3 | - | - | 40 | - | 60 | 1 | 100 | 1 | 10 |  |
| Produktionsmengen |  |  |  |  |  |  |  |  |  |  |
| Erzeugnis $k$ |  |  |  |  |  |  |  |  |  |  |
| 1 | 30 | 80 | - | 20 | 20 |  |  |  |  |  |
| 2 | - | - | 30 | - | 70 |  |  |  |  |  |
| 3 | - | - | 40 | 60 | - |  |  |  |  |  |

Optimale Lösung:
![img-0.jpeg](img-0.jpeg)# Dynamische Mehrprodukt-Losgrößenplanung: PLSP 

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement# Dynamische Mehrprodukt-Losgrößenplanung: PLSP 

Annahmen:
Der Rüstzustand kann übernommen werden.
Es kann in einer Periode maximal einmal umgerüstet werden.
Es können maximal zwei verschiedene Erzeugnisse in einer Periode produziert werden.# Dynamische Mehrprodukt-Losgrößenplanung: PLSP-PM 

Annahmen:

- Der Rüstzustand kann übernommen werden.
- Es kann in einer Periode maximal einmal umgerüstet werden.
- Es können maximal zwei verschiedene Erzeugnisse in einer Periode produziert werden.
- Es können alternative Ressourcen (,,parallele Maschinen") eingesetzt werden.# Modell PLSP 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}+p_{k t} \cdot q_{k t}\right)
$$

u. B. d. R.:

$$
y_{k, t-1}+q_{k t}-y_{k t}=d_{k t}
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$

$$
\begin{aligned}
& \sum_{k \in \mathcal{K}}\left(\operatorname{tb}_{k} \cdot q_{k t}+\operatorname{tr}_{k} \cdot \gamma_{k t}\right) \leq b_{t} \\
& q_{k t}-M \cdot\left(\omega_{k, t-1}+\omega_{k t}\right) \leq 0
\end{aligned}
$$

für alle $t=1,2, \ldots, T$
für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$

Übernahme des Rüstzustands: $q_{k t} \geq 0 ; y_{k t} \geq 0 ; \gamma_{k t} \in\{0,1\} ; \omega_{k t} \in\{0,1\}$

$$
\sum_{k \in \mathcal{K}} \omega_{k t} \leq 1
$$

für alle $t=1,2, \ldots, T$
$\gamma_{k t} \geq \omega_{k t}-\omega_{k, t-1}$
für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$# Modell PLSP-PM 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{k \in \mathcal{K}} \sum_{m \in \mathcal{M}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k m t}+p_{k m t} \cdot q_{k m t}\right)
$$

u. B. d. R.:

$$
y_{k, t-1}+\sum_{m \in \mathcal{M}} q_{k m t}-y_{k t}=d_{k t} \quad \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$

$\sum_{k \in \mathcal{K}}\left(\operatorname{tb}_{k m} \cdot q_{k m t}+\operatorname{tr}_{k m} \cdot \gamma_{k m t}\right) \leq b_{m t} \quad$ für alle $m \in \mathcal{M}$ und $t=1,2, \ldots, T$
$q_{k m t}-M \cdot\left(\omega_{k, m, t-1}+\omega_{k m t}\right) \leq 0 \quad$ für alle $k \in \mathcal{K} ; m \in \mathcal{M} ; t=1,2, \ldots, T$
Übernahme des Rüstzustands: $q_{k m t} \geq 0 ; y_{k t} \geq 0 ; \gamma_{k m t} \in\{0,1\} ; \omega_{k m t} \in\{0,1\}$
$\sum_{k \in \mathcal{K}} \omega_{k m t} \leq 1$
für alle $m \in \mathcal{M}$ und $t=1,2, \ldots, T$
$\gamma_{k m t} \geq \omega_{k m t}-\omega_{k, m, t-1}$
für alle $k \in \mathcal{K} ; m \in \mathcal{M} ; t=1,2, \ldots, T$# Dynamische Mehrprodukt-Losgrößenplanung: PLSP-PM 

## Beispiel PLSP-PM

| Bedarfsmengen |  |  |  |  |  |  |  |  |  |  |  | Parameter |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | $h_{k}$ | $s_{k}$ | $\mathrm{tb}_{k}$ | $\operatorname{tr}_{k}$ |
| 1 | 30 | - | 80 | - | 40 | - | 10 | - | - | 10 | 4 | 400 | 1 | 0 |
| 2 | - | - | 30 | - | 70 | - | - | - | - | 20 | 3 | 150 | 1 | 0 |
| 3 | - | - | 40 | - | 60 | - | 50 | - | - | 100 | 2 | 100 | 1 | 0 |# Dynamische Mehrprodukt-Losgrößenplanung: PLSP-PM 

Beispiel PLSP-PM, $|\mathcal{M}|=2$

| Bedarfsmengen |  |  |  |  |  |  |  |  |  |  |  | Parameter |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | $h_{k}$ | $s_{k}$ | $\mathrm{tb}_{k}$ | $\operatorname{tr}_{k}$ |
| 1 | 30 | - | 80 | - | 40 | - | 10 | - | - | 10 | 4 | 400 | 1 | 0 |
| 2 | - | - | 30 | - | 70 | - | - | - | - | 20 | 3 | 150 | 1 | 0 |
| 3 | - | - | 40 | - | 60 | - | 50 | - | - | 100 | 2 | 100 | 1 | 0 |

Optimale Lösung: $b_{\text {Maschine } 1}=75, b_{\text {Maschine } 2}=25$
![img-1.jpeg](img-1.jpeg)

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement
58-5# Das Verfahren von Haase zur Lösung des PLSP# Ein Lösungsverfahren von Haase für das PLSP 

## Initialisierung

Erzeugnisbezogene Rüstzustände: $\omega_{k t}=0$
$(\boldsymbol{k} \in \mathcal{K} ; t=1,2, \ldots, T)$
Produktions- bzw. Beschaffungsmengen: $q_{k t}=0$
$(k \in \mathcal{K} ; t=1,2, \ldots, T)$
Kumulierte Bedarfsmengen: $D_{k t}=\sum_{\tau=t}^{T} d_{k \tau}$
$(k \in \mathcal{K} ; t=1,2, \ldots, T)$# Beispiel II PLSP 

| Bedarfsmengen |  |  |  |  |  |  |  |  |  |  |  | Parameter |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | $h_{k}$ | $s_{k}$ | $\mathrm{tb}_{k}$ | $\operatorname{tr}_{k}$ |  |
| 1 | - | 30 | - | - | - | 80 | - | - | - | 40 | 2.0 | 400 | 1 | 0 |  |
| 2 | - | - | - | - | - | 60 | - | - | - | 90 | 1.5 | 150 | 1 | 0 |  |
| 3 | - | - | - | - | - | 40 | - | - | - | 60 | 1.0 | 100 | 1 | 0 |  |
| $b_{t}$ | 50 | 50 | 50 | 50 | 50 | 50 | 50 | 50 | 50 | 50 |  |  |  |  |  |# Beispiel II PLSP 

Kumulierte Bedarfsmenge $D_{k \tau}=\max \left\{0, \sum_{t=\tau}^{T}\left(d_{k t}-q_{k t}\right)\right\}$

| Bedarfsmengen |  |  |  |  |  |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Periode $\tau$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| 1 | 150 | 150 | 120 | 120 | 120 | 120 | 40 | 40 | 40 | 40 |
| 2 | 150 | 150 | 150 | 150 | 150 | 150 | 90 | 90 | 90 | 90 |
| 3 | 100 | 100 | 100 | 100 | 100 | 100 | 60 | 60 | 60 | 60 |

Letzte Periode mit Bedarf $n_{k t}=\left\{\begin{array}{c}t \\ n_{k, t-1} \end{array}\right.$, falls $d_{k t}>0$ sonst

| Bedarfsmengen |  |  |  |  |  |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |  |
| 1 | 0 | 2 | 2 | 2 | 2 | 6 | 6 | 6 | 6 | 10 |  |
| 2 | 0 | 0 | 0 | 0 | 0 | 6 | 6 | 6 | 6 | 10 |  |
| 3 | 0 | 0 | 0 | 0 | 0 | 6 | 6 | 6 | 6 | 10 |  |# Beispiel II PLSP 

| $\omega_{k t}=$ | Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 1 | - | - | - | - | - | - | - | - | - |  |
|  | 2 | - | - | - | - | - | - | - | - | - |  |
|  | 3 | - | - | - | - | - | - | - | - | - | 1 |


| $q_{k t}=$ | Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 1 | - | - | - | - | - | - | - | - | - |  |
|  | 2 | - | - | - | - | - | - | - | - | - |  |
|  | 3 | - | - | - | - | - | - | - | - | - | 50 |


| $D_{k \tau}=$ | Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 1 | 150 | 150 | 120 | 120 | 120 | 120 | 40 | 40 | 40 | 40 |
|  | 2 | 150 | 150 | 150 | 150 | 150 | 150 | 90 | 90 | 90 | 90 |
|  | 3 | 50 | 50 | 50 | 50 | 50 | 50 | 10 | 10 | 10 | 10 |# Beispiel II PLSP 

| $\omega_{k t}=$ | Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 1 | - | - | - | - | - | - | - | - | - |  |
|  | 2 | - | - | - | - | - | - | - | - | - |  |
|  | 3 | - | - | - | - | - | - | - | 1 | 1 |  |
| $q_{k t}=$ | Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|  | 1 | - | - | - | - | - | - | - | - | - |  |
|  | 2 | - | - | - | - | - | - | - | - | - |  |
|  | 3 | - | - | - | - | - | - | - | 10 | 50 |  |
| $D_{k \tau}=$ | Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|  | 1 | 150 | 150 | 120 | 120 | 120 | 120 | 40 | 40 | 40 |  |
|  | 2 | 150 | 150 | 150 | 150 | 150 | 150 | 90 | 90 | 90 |  |
|  | 3 | 40 | 40 | 40 | 40 | 40 | 40 | 0 | 0 | 0 |  |# Beispiel II PLSP 

| $\omega_{k t}=$ | Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 1 | - | - | - | - | - | - | - | - | - |  |
|  | 2 | - | - | - | - | - | - | - | 1 | - | - |
|  | 3 | - | - | - | - | - | - | - | - | 1 | 1 |


| $q_{k t}=$ | Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 1 | - | - | - | - | - | - | - | - | - |  |
|  | 2 | - | - | - | - | - | - | - | - | 40 | - |
|  | 3 | - | - | - | - | - | - | - | - | 10 | 50 |


| $D_{k \tau}=$ | Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 1 | 150 | 150 | 120 | 120 | 120 | 120 | 40 | 40 | 40 |  |
|  | 2 | 110 | 110 | 110 | 110 | 110 | 110 | 50 | 50 | 50 |  |
|  | 3 | 40 | 40 | 40 | 40 | 40 | 40 | 0 | 0 | 0 |  |# Beispiel II PLSP 

| $\omega_{k t}=$ | Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 1 | - | - | - | - | - | - | - | - | - |  |
|  | 2 | - | - | - | - | - | - | 1 | 1 | - | - |
|  | 3 | - | - | - | - | - | - | - | - | 1 | 1 |


| $q_{k t}=$ | Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 1 | - | - | - | - | - | - | - | - | - |  |
|  | 2 | - | - | - | - | - | - | - | 50 | 40 | - |
|  | 3 | - | - | - | - | - | - | - | - | 10 | 50 |


| $D_{k \tau}=$ | Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 1 | 150 | 150 | 120 | 120 | 120 | 120 | 40 |  |  |  |
|  | 2 | 60 | 60 | 60 | 60 | 60 | 60 | 0 |  |  |  |
|  | 3 | 40 | 40 | 40 | 40 | 40 | 40 | 0 |  |  |  |# Beispiel II PLSP 

| $\omega_{k t}=$ | Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 1 | - | 1 | 1 | - | - | - | - | - | - | - |
|  | 2 | - | - | - | - | 1 | 1 | 1 | 1 | - | - |
|  | 3 | - | - | - | 1 | - | - | - | - | 1 | 1 |

$q_{k t}=$| Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | - | - | 50 | 50 | - | - | - | - | - | - |
| 2 | - | - | - | - | 10 | 50 | - | 50 | 40 | - |
| 3 | - | - | - | - | 40 | - | - | - | 10 | 50 |

$D_{k \tau}=$

| Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 50 | 50 | 20 |  |  |  |  |  |  |  |
| 2 | 0 | 0 | 0 |  |  |  |  |  |  |  |
| 3 | 0 | 0 | 0 |  |  |  |  |  |  |  |# Beispiel II PLSP 

| $\omega_{k t}=$ | Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 1 | 1 | 1 | 1 | - | - | - | - | - | - | - |
|  | 2 | - | - | - | - | 1 | 1 | 1 | 1 | - | - |
|  | 3 | - | - | - | 1 | - | - | - | - | 1 | 1 |

$q_{k t}=$| Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | - | 50 | 50 | 50 | - | - | - | - | - | - |
| 2 | - | - | - | - | 10 | 50 | - | 50 | 40 | - |
| 3 | - | - | - | - | 40 | - | - | - | 10 | 50 |


| Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 0 | 0 | 0 |  |  |  |  |  |  |  |
| 2 | 0 | 0 | 0 |  |  |  |  |  |  |  |
| 3 | 0 | 0 | 0 |  |  |  |  |  |  |  |# Das dynamische mehrstufige <br> Mehrprodukt-Losgrößenproblem# MLCLSP — Ein 

## Makroperioden-Modell für das dynamische mehrstufige

Mehrprodukt-Losgrößenproblem# Mehrstufige Mehrprodukt-Losgrößenplanung (MLCLSP) 

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement
$62-1$# Mehrstufige Mehrprodukt-Losgrößenplanung (MLCLSP) 

wegen Ressourcenkonkurrenz
arbeitsgangbezogene Betrachtung (Production Process Model (PPM)) zur Erfassung aller Ressourcenverbräuchewegen Ressourcenkonkurrenz
arbeitsgangbezogene Betrachtung (Production Process Model (PPM)) zur Erfassung aller Ressourcenverbräuche, d.h., nach jedem Arbeitsgang gilt eine neue Erzeugnisstufe als erreichtwegen Ressourcenkonkurrenz
arbeitsgangbezogene Betrachtung (Production Process Model (PPM)) zur Erfassung aller Ressourcenverbräuche, d.h., nach jedem Arbeitsgang gilt eine neue Erzeugnisstufe als erreicht, und es wird ein neues (Zwischen-)Produkt identifiziertwegen Ressourcenkonkurrenz
arbeitsgangbezogene Betrachtung (Production Process Model (PPM)) zur Erfassung aller Ressourcenverbräuche, d.h., nach jedem Arbeitsgang gilt eine neue Erzeugnisstufe als erreicht, und es wird ein neues (Zwischen-)Produkt identifiziert
mehrstufige Betrachtung zur Erfassung der Erzeugnisstrukturwegen Ressourcenkonkurrenz
arbeitsgangbezogene Betrachtung (Production Process Model (PPM)) zur Erfassung aller Ressourcenverbräuche, d.h., nach jedem Arbeitsgang gilt eine neue Erzeugnisstufe als erreicht, und es wird ein neues (Zwischen-)Produkt identifiziert
mehrstufige Betrachtung zur Erfassung der Erzeugnisstruktur
simultane Betrachtung aller Werkstätten auf Grund der Materialflussbeziehungen# Mehrstufige Mehrprodukt-Losgrößenplanung (MLCLSP) 

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement
$62-7$# Modell CLSP 

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
$$

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement
62-8# Modell MLCLSP 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}+p_{k t} \cdot q_{k t}\right)
$$

u. B. d. R.:

Bedarf in Periode $t$ :

$$
y_{k, t-1}+q_{k t}-y_{k t}=d_{k t}+\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}
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
$$

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement
62-9# Modell MLCLSP 

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
q_{k t}-M \cdot \gamma_{k t} \leq 0
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
Wertebereich:

$$
q_{k t} \geq 0 ; y_{k t} \geq 0 ; y_{k 0}=0 ; y_{k T}=0 ; \gamma_{k t} \in\{0,1\} \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement# Erzeugnisstruktur 

![img-2.jpeg](img-2.jpeg)# Erzeugnisstruktur 

![img-3.jpeg](img-3.jpeg)# Erzeugnisstruktur 

![img-4.jpeg](img-4.jpeg)

## Ressourcenbelegung

Schichtlänge $=480$ Minuten
![img-5.jpeg](img-5.jpeg)# Erzeugnisstruktur 

![img-6.jpeg](img-6.jpeg)# Modell MLCLSP 

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
q_{k t}-M \cdot \gamma_{k t} \leq 0
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
Wertebereich:

$$
q_{k t} \geq 0 ; y_{k t} \geq 0 ; y_{k 0}=0 ; y_{k T}=0 ; \gamma_{k t} \in\{0,1\} \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement# Modell MLCLSP 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}+p_{k t} \cdot q_{k t}\right)
$$

u. B. d. R.:

Bedarf in Periode $t$ :

$$
y_{k, t-1}+q_{k, t-z_{k}}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t} \quad \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$

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
$$

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement# Modell MLCLSP 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}+p_{k t} \cdot q_{k t}\right)
$$

u. B. d. R.:

Bedarf in Periode $t$ :

$$
y_{k, t-1}+q_{k, t-1}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t} \quad \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$

Kapazitäten in Periode $t$ :

$$
\sum_{k \in \mathcal{K}}\left(\operatorname{tb}_{k j} \cdot q_{k t}+\operatorname{tr}_{k j} \cdot \gamma_{k t}\right) \leq b_{j t} \quad \text { für alle } j \in \mathcal{J} \text { und } t=1,2, \ldots, T
$$

Es muss gerüstet werden, wenn $q_{k t}>0$ ist:

$$
q_{k t}-M \cdot \gamma_{k t} \leq 0
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
Wertebereich:

$$
q_{k t} \geq 0 ; y_{k t} \geq 0 ; y_{k 0}=0 ; y_{k T}=0 ; \gamma_{k t} \in\{0,1\} \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement# Mehrstufige Losgrößenplanung 

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement
63-1# Bewertung der Lagerbestände:# Mehrstufige Losgrößenplanung 

Bewertung der Lagerbestände:
$>$ physische Lagerbestände mit vollen Lagerkosten
Lagerkosten $_{k t}=y_{k t} \cdot h_{k}$

$$
(k \in \mathcal{K}, t=1,2, \ldots, T)
$$# Mehrstufige Losgrößenplanung 

Bewertung der Lagerbestände:
> physische Lagerbestände mit vollen Lagerkosten
Lagerkosten $_{k t}=y_{k t} \cdot h_{k}$

$$
(k \in \mathcal{K}, t=1,2, \ldots, T)
$$

- systemweite Lagerbestände mit marginalen Lagerkosten

Lagerkosten $_{k t}=E_{k t} \cdot e_{k}$

$$
(k \in \mathcal{K}, t=1,2, \ldots, T)
$$# Mehrstufige Losgrößenplanung 

Bewertung der Lagerbestände:
> physische Lagerbestände mit vollen Lagerkosten
Lagerkosten $_{k t}=y_{k t} \cdot h_{k}$

$$
(k \in \mathcal{K}, t=1,2, \ldots, T)
$$

- systemweite Lagerbestände mit marginalen Lagerkosten

Lagerkosten $_{k t}=E_{k t} \cdot e_{k}$

$$
(k \in \mathcal{K}, t=1,2, \ldots, T)
$$

## $\triangleright$ echelon stock

$$
E_{k t}=y_{k t}+\sum_{j \in \mathcal{N}_{k}^{*}} v_{k j} \cdot y_{j t}
$$

$$
(k \in \mathcal{K}, t=1,2, \ldots, T)
$$# Mehrstufige Losgrößenplanung 

Bewertung der Lagerbestände:
> physische Lagerbestände mit vollen Lagerkosten
Lagerkosten $_{k t}=y_{k t} \cdot h_{k}$
$(k \in \mathcal{K}, t=1,2, \ldots, T)$

- systemweite Lagerbestände mit marginalen Lagerkosten

Lagerkosten $_{k t}=E_{k t} \cdot e_{k}$
$(k \in \mathcal{K}, t=1,2, \ldots, T)$

## $\triangleright$ echelon stock

$$
E_{k t}=y_{k t}+\sum_{j \in \mathcal{N}_{k}^{*}} v_{k j} \cdot y_{j t}
$$

## $\triangleright$ echelon holding costs

$$
e_{k}=h_{k}-\sum_{j \in \mathcal{V}_{k}} a_{j k} \cdot h_{j}
$$

$(k \in \mathcal{K})$# Mehrstufige Losgrößenplanung 

Beispiel Erzeugnisstruktur E1 $\xrightarrow{1} \mathrm{P} 1\left(h_{\mathrm{E} 1}=6, h_{\mathrm{P} 1}=10\right)$Beispiel Erzeugnisstruktur E1 $\xrightarrow{1}$ P1 $\left(h_{\mathrm{E} 1}=6, h_{\mathrm{P} 1}=10\right)$
physische Lagerbestände mit vollen Lagerkosten

| $k$ | $h_{k}$ | Bestand am <br> Periodenanfang <br> (physisch) | Lager- <br> kosten | Bestand am <br> Periodenende <br> (physisch) | Lager- <br> kosten | Anstieg der <br> Lagerkosten |
| :-- | :-- | :--: | :--: | :--: | :--: | :--: |
| P1 | 10 | 0 | 0 | 1 | 10 | 10 |
| E1 | 6 | 1 | 6 | 0 | 0 | -6 |
|  |  |  |  |  | Summe | 4 |Beispiel Erzeugnisstruktur E1 $\xrightarrow{1}$ P1 $\left(h_{\mathrm{E} 1}=6, h_{\mathrm{P} 1}=10\right)$
physische Lagerbestände mit vollen Lagerkosten

| $k$ | $h_{k}$ | Bestand am <br> Periodenanfang <br> (physisch) | Lager- <br> kosten | Bestand am <br> Periodenende <br> (physisch) | Lager- <br> kosten | Anstieg der <br> Lagerkosten |
| :-- | :-- | :--: | :--: | :--: | :--: | :--: |
| P1 | 10 | 0 | 0 | 1 | 10 | 10 |
| E1 | 6 | 1 | 6 | 0 | 0 | -6 |
|  |  |  |  |  | Summe | 4 |

systemweite Lagerbestände mit marginalen Lagerkosten

| $k$ | $e_{k}$ | Bestand am <br> Periodenanfang <br> (systemweit) | Lager- <br> kosten | Bestand am <br> Periodenende <br> (systemweit) | Lager- <br> kosten | Anstieg der <br> Lagerkosten |
| :-- | :-- | :--: | :--: | :--: | :--: | :--: |
| P1 | 4 | 0 | 0 | 1 | 4 | 4 |
| E1 | 6 | 1 | 6 | 1 | 6 | 0 |
|  |  |  |  |  | Summe | 4 |# Lösungsverfahren für mehrstufige Mehrprodukt-Losgrößenprobleme# Lösungsverfahren für mehrstufige Mehrprodukt-Losgrößenprobleme ohne Kapazitätsbeschränkungen# NIPPA - Das Verfahren von Simpson und Erenguc# Mehrstufige Losgrößenplanung - NIPPA-Verfahren 

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement
$65-1$# Inhaltsverzeichnis 

## Stückperiodenausgleichsverfahren

(Part-Period-, Kostenausgleichsverfahren)# Inhaltsverzeichnis 

## Stückperiodenausgleichsverfahren

(Part-Period-, Kostenausgleichsverfahren)

Vergrößere ein Los, solange $h \cdot \sum_{t=\tau+1}^{j}(t-\tau) \cdot d_{t} \leq s$ !# Inhaltsverzeichnis 

## Stückperiodenausgleichsverfahren

(Part-Period-, Kostenausgleichsverfahren)

$$
h \cdot \sum_{t=\tau+1}^{j}(t-\tau) \cdot d_{t}
$$

Vergrößere ein Los, solange $\frac{t=\tau+1}{s} \leq 1$ !# In: $\sum_{t=\tau+1}^{j}(t-\tau) \cdot d_{t}$ 

Vergrößere ein Los, solange $\frac{s}{\frac{t-\tau+1}{s}} \leq 1$ !

## Mehrstufiges Stückperiodenausgleichsverfahren

(NIPPA - Non-Sequential Incremental Part Period Algorithm)# Stückperiodenausgleichsverfahren 

(Part-Period-, Kostenausgleichsverfahren)

$$
h \cdot \sum_{t=\tau+1}^{j}(t-\tau) \cdot d_{t}
$$

Vergrößere ein Los, solange $\frac{t=\tau+1}{s} \leq 1$ !

## Mehrstufiges Stückperiodenausgleichsverfahren

(NIPPA - Non-Sequential Incremental Part Period Algorithm)
Vergrößere das unmittelbar vorgelagerte Los für das kleinste

$$
\rho_{k t}=\frac{q_{k t} \cdot e_{k} \cdot n_{k t}+\sum_{j \in \mathcal{V}_{k}^{*(h)}} v_{j k} \cdot q_{k t} \cdot e_{j} \cdot n_{j t}}{s_{k}+\sum_{j \in \mathcal{V}_{k}^{*(s)}} s_{j}} \quad(k \in \mathcal{K}, t=2, \ldots, T)!
$$# Stückperiodenausgleichsverfahren 

(Part-Period-, Kostenausgleichsverfahren)

$$
h \cdot \sum_{t=\tau+1}^{j}(t-\tau) \cdot d_{t}
$$

Vergrößere ein Los, solange $\frac{t=\tau+1}{s} \leq 1$ !

## Mehrstufiges Stückperiodenausgleichsverfahren

(NIPPA - Non-Sequential Incremental Part Period Algorithm)
Vergrößere das unmittelbar vorgelagerte Los für das kleinste

$$
\rho_{k t}=\frac{q_{k t} \cdot e_{k} \cdot n_{k t}+\sum_{j \in \mathcal{V}_{k}^{*(h)}} v_{j k} \cdot q_{k t} \cdot e_{j} \cdot n_{j t}}{s_{k}+\sum_{j \in \mathcal{V}_{k}^{*(s)}} s_{j}} \quad(k \in \mathcal{K}, t=2, \ldots, T)!
$$

Lagerdauer: $n_{k t}=t-\tau_{k, t-1}$# Mehrstufige Losgrößenplanung - NIPPA-Verfahren 

Beispiel Gozintograph
![img-7.jpeg](img-7.jpeg)
$e_{1,2,3}=1, e_{4}=4, e_{5}=3$
$s_{1}=400, s_{2}=200, s_{3}=50, s_{4,5}=100$# Mehrstufige Losgrößenplanung - NIPPA-Verfahren 

## Beispiel Gozintograph

![img-8.jpeg](img-8.jpeg)
$e_{1,2,3}=1, e_{4}=4, e_{5}=3$
$s_{1}=400, s_{2}=200, s_{3}=50, s_{4,5}=100$

## Primärbedarfsmengen

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | 5 | 12 | 8 | 9 | 7 | 19 | 11 | 9 |
| 2 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |
| 3 |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4 |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 5 |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |# Mehrstufige Losgrößenplanung - NIPPA-Verfahren 

## Beispiel Gozintograph

![img-9.jpeg](img-9.jpeg)
$e_{1,2,3}=1, e_{4}=4, e_{5}=3$
$s_{1}=400, s_{2}=200, s_{3}=50, s_{4,5}=100$

## Produktionsmengen

| $k$ | $t=$ | $\mathbf{1}$ | $\mathbf{2}$ | $\mathbf{3}$ | $\mathbf{4}$ | $\mathbf{5}$ | $\mathbf{6}$ | $\mathbf{7}$ | $\mathbf{8}$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $\mathbf{1}$ |  | 5 | 12 | 8 | 9 | 7 | 19 | 11 | 9 |
| $\mathbf{2}$ |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |
| $\mathbf{3}$ |  | 43 | 57 | 42 | 49 | 49 | 67 | 46 | 47 |
| $\mathbf{4}$ |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |
| $\mathbf{5}$ |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |# Mehrstufige Losgrößenplanung - NIPPA-Verfahren 

## Beispiel Gozintograph

![img-10.jpeg](img-10.jpeg)
$e_{1,2,3}=1, e_{4}=4, e_{5}=3$
$s_{1}=400, s_{2}=200, s_{3}=50, s_{4,5}=100$

## Produktionsmengen

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | 5 | 12 | 8 | 9 | 7 | 19 | 11 | 9 |
| 2 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |
| 3 |  | 43 | 57 | 42 | 49 | 49 | 67 | 46 | 47 |
| 4 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |
| 5 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |

Prioritätsziffern

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | - | 0.060 | 0.040 | 0.045 | 0.035 | 0.095 | 0.055 | 0.045 |
| 2 |  | - | 1.013 | 0.765 | 0.900 | 0.945 | 1.080 | 0.788 | 0.855 |
| 3 |  | - | 1.140 | 0.840 | 0.980 | 0.980 | 1.340 | 0.920 | 0.940 |
| 4 |  | - | 1.800 | 1.360 | 1.600 | 1.680 | 1.920 | 1.400 | 1.520 |
| 5 |  | - | 1.350 | 1.020 | 1.200 | 1.260 | 1.440 | 1.050 | 1.140 |# Mehrstufige Losgrößenplanung - NIPPA-Verfahren 

## Beispiel Gozintograph

![img-11.jpeg](img-11.jpeg)
$e_{1,2,3}=1, e_{4}=4, e_{5}=3$
$s_{1}=400, s_{2}=200, s_{3}=50, s_{4,5}=100$

## Produktionsmengen

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | 5 | 12 | 8 | 9 | 7 | 19 | 11 | 9 |
| 2 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |
| 3 |  | 43 | 57 | 42 | 49 | 49 | 67 | 46 | 47 |
| 4 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |
| 5 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |

Prioritätsziffern

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | - | 0.060 | 0.040 | 0.045 | 0.035 | 0.095 | 0.055 | 0.045 |
| 2 |  | - | 1.013 | 0.765 | 0.900 | 0.945 | 1.080 | 0.788 | 0.855 |
| 3 |  | - | 1.140 | 0.840 | 0.980 | 0.980 | 1.340 | 0.920 | 0.940 |
| 4 |  | - | 1.800 | 1.360 | 1.600 | 1.680 | 1.920 | 1.400 | 1.520 |
| 5 |  | - | 1.350 | 1.020 | 1.200 | 1.260 | 1.440 | 1.050 | 1.140 |# Mehrstufige Losgrößenplanung - NIPPA-Verfahren 

## Beispiel Gozintograph

![img-12.jpeg](img-12.jpeg)
$e_{1,2,3}=1, e_{4}=4, e_{5}=3$
$s_{1}=400, s_{2}=200, s_{3}=50, s_{4,5}=100$

## Produktionsmengen

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | 5 | 12 | 8 | 16 | 0 | 19 | 11 | 9 |
| 2 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |
| 3 |  | 43 | 57 | 42 | 56 | 42 | 67 | 46 | 47 |
| 4 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |
| 5 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |

Prioritätsziffern

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | - | 0.060 | 0.040 | 0.045 | 0.035 | 0.095 | 0.055 | 0.045 |
| 2 |  | - | 1.013 | 0.765 | 0.900 | 0.945 | 1.080 | 0.788 | 0.855 |
| 3 |  | - | 1.140 | 0.840 | 0.980 | 0.980 | 1.340 | 0.920 | 0.940 |
| 4 |  | - | 1.800 | 1.360 | 1.600 | 1.680 | 1.920 | 1.400 | 1.520 |
| 5 |  | - | 1.350 | 1.020 | 1.200 | 1.260 | 1.440 | 1.050 | 1.140 |# Mehrstufige Losgrößenplanung - NIPPA-Verfahren 

## Beispiel Gozintograph

![img-13.jpeg](img-13.jpeg)
$e_{1,2,3}=1, e_{4}=4, e_{5}=3$
$s_{1}=400, s_{2}=200, s_{3}=50, s_{4,5}=100$

## Produktionsmengen

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | 5 | 12 | 8 | 16 | 0 | 19 | 11 | 9 |
| 2 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |
| 3 |  | 43 | 57 | 42 | 56 | 42 | 67 | 46 | 47 |
| 4 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |
| 5 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |

Prioritätsziffern

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | - | 0.060 | 0.040 | 0.080 | - | 0.190 | 0.055 | 0.045 |
| 2 |  | - | 1.013 | 0.765 | 0.900 | 0.840 | 1.080 | 0.788 | 0.855 |
| 3 |  | - | 1.140 | 0.840 | 1.120 | 0.840 | 1.340 | 0.920 | 0.940 |
| 4 |  | - | 1.800 | 1.360 | 1.600 | 1.680 | 1.920 | 1.400 | 1.520 |
| 5 |  | - | 1.350 | 1.020 | 1.200 | 1.260 | 1.440 | 1.050 | 1.140 |# Mehrstufige Losgrößenplanung - NIPPA-Verfahren 

## Beispiel Gozintograph

![img-14.jpeg](img-14.jpeg)
$e_{1,2,3}=1, e_{4}=4, e_{5}=3$
$s_{1}=400, s_{2}=200, s_{3}=50, s_{4,5}=100$

## Produktionsmengen

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | 5 | 20 | 0 | 16 | 0 | 19 | 11 | 9 |
| 2 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |
| 3 |  | 43 | 65 | 34 | 56 | 42 | 67 | 46 | 47 |
| 4 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |
| 5 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |

Prioritätsziffern

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | - | 0.100 | - | 0.160 | - | 0.190 | 0.055 | 0.045 |
| 2 |  | - | 1.013 | 0.680 | 0.900 | 0.840 | 1.080 | 0.788 | 0.855 |
| 3 |  | - | 1.300 | 0.680 | 1.120 | 0.840 | 1.340 | 0.920 | 0.940 |
| 4 |  | - | 1.800 | 1.360 | 1.600 | 1.680 | 1.920 | 1.400 | 1.520 |
| 5 |  | - | 1.350 | 1.020 | 1.200 | 1.260 | 1.440 | 1.050 | 1.140 |# Mehrstufige Losgrößenplanung - NIPPA-Verfahren 

## Beispiel Gozintograph

![img-15.jpeg](img-15.jpeg)
$e_{1,2,3}=1, e_{4}=4, e_{5}=3$
$s_{1}=400, s_{2}=200, s_{3}=50, s_{4,5}=100$

## Produktionsmengen

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | 5 | 20 | 0 | 16 | 0 | 19 | 20 | 0 |
| 2 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |
| 3 |  | 43 | 65 | 34 | 56 | 42 | 67 | 55 | 38 |
| 4 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |
| 5 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |

Prioritätsziffern

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | - | 0.100 | - | 0.160 | - | 0.190 | 0.100 | - |
| 2 |  | - | 1.013 | 0.680 | 0.900 | 0.840 | 1.080 | 0.788 | 0.760 |
| 3 |  | - | 1.300 | 0.680 | 1.120 | 0.840 | 1.340 | 1.100 | 0.760 |
| 4 |  | - | 1.800 | 1.360 | 1.600 | 1.680 | 1.920 | 1.400 | 1.520 |
| 5 |  | - | 1.350 | 1.020 | 1.200 | 1.260 | 1.440 | 1.050 | 1.140 |# Mehrstufige Losgrößenplanung - NIPPA-Verfahren 

## Beispiel Gozintograph

![img-16.jpeg](img-16.jpeg)
$e_{1,2,3}=1, e_{4}=4, e_{5}=3$
$s_{1}=400, s_{2}=200, s_{3}=50, s_{4,5}=100$

## Produktionsmengen

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | 25 | 0 | 0 | 16 | 0 | 19 | 20 | 0 |
| 2 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |
| 3 |  | 63 | 45 | 34 | 56 | 42 | 67 | 55 | 38 |
| 4 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |
| 5 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |

Prioritätsziffern

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | - | - | - | 0.240 | - | 0.190 | 0.100 | - |
| 2 |  | - | 0.900 | 0.680 | 0.900 | 0.840 | 1.080 | 0.788 | 0.760 |
| 3 |  | - | 0.900 | 0.680 | 1.120 | 0.840 | 1.340 | 1.100 | 0.760 |
| 4 |  | - | 1.800 | 1.360 | 1.600 | 1.680 | 1.920 | 1.400 | 1.520 |
| 5 |  | - | 1.350 | 1.020 | 1.200 | 1.260 | 1.440 | 1.050 | 1.140 |# Mehrstufige Losgrößenplanung - NIPPA-Verfahren 

## Beispiel Gozintograph

![img-17.jpeg](img-17.jpeg)
$e_{1,2,3}=1, e_{4}=4, e_{5}=3$
$s_{1}=400, s_{2}=200, s_{3}=50, s_{4,5}=100$

## Produktionsmengen

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | 25 | 0 | 0 | 16 | 0 | 39 | 0 | 0 |
| 2 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |
| 3 |  | 63 | 45 | 34 | 56 | 42 | 87 | 35 | 38 |
| 4 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |
| 5 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |

Prioritätsziffern

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | - | - | - | 0.240 | - | 0.390 | - | - |
| 2 |  | - | 0.900 | 0.680 | 0.900 | 0.840 | 1.080 | 0.700 | 0.760 |
| 3 |  | - | 0.900 | 0.680 | 1.120 | 0.840 | 1.740 | 0.700 | 0.760 |
| 4 |  | - | 1.800 | 1.360 | 1.600 | 1.680 | 1.920 | 1.400 | 1.520 |
| 5 |  | - | 1.350 | 1.020 | 1.200 | 1.260 | 1.440 | 1.050 | 1.140 |# Mehrstufige Losgrößenplanung - NIPPA-Verfahren 

## Beispiel Gozintograph

![img-18.jpeg](img-18.jpeg)
$e_{1,2,3}=1, e_{4}=4, e_{5}=3$
$s_{1}=400, s_{2}=200, s_{3}=50, s_{4,5}=100$

## Produktionsmengen

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | 41 | 0 | 0 | 0 | 0 | 39 | 0 | 0 |
| 2 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |
| 3 |  | 79 | 45 | 34 | 40 | 42 | 87 | 35 | 38 |
| 4 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |
| 5 |  | 38 | 45 | 34 | 40 | 42 | 48 | 35 | 38 |

Prioritätsziffern

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | - | - | - | - | - | 0.975 | - | - |
| 2 |  | - | 0.900 | 0.680 | 0.800 | 0.840 | 1.080 | 0.700 | 0.760 |
| 3 |  | - | 0.900 | 0.680 | 0.800 | 0.840 | 1.740 | 0.700 | 0.760 |
| 4 |  | - | 1.800 | 1.360 | 1.600 | 1.680 | 1.920 | 1.400 | 1.520 |
| 5 |  | - | 1.350 | 1.020 | 1.200 | 1.260 | 1.440 | 1.050 | 1.140 |# Mehrstufige Losgrößenplanung - NIPPA-Verfahren 

## Beispiel Gozintograph

![img-19.jpeg](img-19.jpeg)
$e_{1,2,3}=1, e_{4}=4, e_{5}=3$
$s_{1}=400, s_{2}=200, s_{3}=50, s_{4,5}=100$

## Produktionsmengen

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | 41 | 0 | 0 | 0 | 0 | 39 | 0 | 0 |
| 2 |  | 38 | 79 | 0 | 40 | 42 | 48 | 35 | 38 |
| 3 |  | 79 | 79 | 0 | 40 | 42 | 87 | 35 | 38 |
| 4 |  | 38 | 79 | 0 | 40 | 42 | 48 | 35 | 38 |
| 5 |  | 38 | 79 | 0 | 40 | 42 | 48 | 35 | 38 |

Prioritätsziffern

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | - | - | - | - | - | 0.975 | - | - |
| 2 |  | - | 1.580 | - | 1.600 | 0.840 | 1.080 | 0.700 | 0.760 |
| 3 |  | - | 1.580 | - | 1.600 | 0.840 | 1.740 | 0.700 | 0.760 |
| 4 |  | - | 3.160 | - | 3.200 | 1.680 | 1.920 | 1.400 | 1.520 |
| 5 |  | - | 2.370 | - | 2.400 | 1.260 | 1.440 | 1.050 | 1.140 |# Mehrstufige Losgrößenplanung - NIPPA-Verfahren 

## Beispiel Gozintograph

![img-20.jpeg](img-20.jpeg)
$e_{1,2,3}=1, e_{4}=4, e_{5}=3$
$s_{1}=400, s_{2}=200, s_{3}=50, s_{4,5}=100$

## Produktionsmengen

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | 41 | 0 | 0 | 0 | 0 | 39 | 0 | 0 |
| 2 |  | 38 | 79 | 0 | 40 | 42 | 83 | 0 | 38 |
| 3 |  | 79 | 79 | 0 | 40 | 42 | 122 | 0 | 38 |
| 4 |  | 38 | 79 | 0 | 40 | 42 | 83 | 0 | 38 |
| 5 |  | 38 | 79 | 0 | 40 | 42 | 83 | 0 | 38 |

Prioritätsziffern

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | - | - | - | - | - | 0.975 | - | - |
| 2 |  | - | 1.580 | - | 1.600 | 0.840 | 1.868 | - | 1.520 |
| 3 |  | - | 1.580 | - | 1.600 | 0.840 | 2.440 | - | 1.520 |
| 4 |  | - | 3.160 | - | 3.200 | 1.680 | 3.320 | - | 3.040 |
| 5 |  | - | 2.370 | - | 2.400 | 1.260 | 2.490 | - | 2.280 |# Mehrstufige Losgrößenplanung - NIPPA-Verfahren 

## Beispiel Gozintograph

![img-21.jpeg](img-21.jpeg)
$e_{1,2,3}=1, e_{4}=4, e_{5}=3$
$s_{1}=400, s_{2}=200, s_{3}=50, s_{4,5}=100$

## Produktionsmengen

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | 41 | 0 | 0 | 0 | 0 | 39 | 0 | 0 |
| 2 |  | 38 | 79 | 0 | 82 | 0 | 83 | 0 | 38 |
| 3 |  | 79 | 79 | 0 | 82 | 0 | 122 | 0 | 38 |
| 4 |  | 38 | 79 | 0 | 82 | 0 | 83 | 0 | 38 |
| 5 |  | 38 | 79 | 0 | 82 | 0 | 83 | 0 | 38 |

Prioritätsziffern

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | - | - | - | - | - | 0.975 | - | - |
| 2 |  | - | 1.580 | - | 3.280 | - | 3.735 | - | 1.520 |
| 3 |  | - | 1.580 | - | 3.280 | - | 4.880 | - | 1.520 |
| 4 |  | - | 3.160 | - | 6.560 | - | 6.640 | - | 3.040 |
| 5 |  | - | 2.370 | - | 4.920 | - | 4.980 | - | 2.280 |# Mehrstufige Losgrößenplanung - NIPPA-Verfahren 

## Beispiel Gozintograph

![img-22.jpeg](img-22.jpeg)
$e_{1,2,3}=1, e_{4}=4, e_{5}=3$
$s_{1}=400, s_{2}=200, s_{3}=50, s_{4,5}=100$

## Produktionsmengen

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | 80 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 |  | 38 | 79 | 0 | 82 | 0 | 83 | 0 | 38 |
| 3 |  | 118 | 79 | 0 | 82 | 0 | 83 | 0 | 38 |
| 4 |  | 38 | 79 | 0 | 82 | 0 | 83 | 0 | 38 |
| 5 |  | 38 | 79 | 0 | 82 | 0 | 83 | 0 | 38 |

Prioritätsziffern

| $k$ | $t=$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | - | - | - | - | - | - | - | - |
| 2 |  | - | 1.580 | - | 3.280 | - | 3.735 | - | 1.520 |
| 3 |  | - | 1.580 | - | 3.280 | - | 4.880 | - | 1.520 |
| 4 |  | - | 3.160 | - | 6.560 | - | 6.640 | - | 3.040 |
| 5 |  | - | 2.370 | - | 4.920 | - | 4.980 | - | 2.280 |Meta-Heuristiken# Mehrstufige Losgrößenplanung - Meta-Heuristiken 

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement
67-1# Modell MLULSP 

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
\begin{aligned}
& 0 \leq q_{k t} \leq \widehat{q}_{k t} \\
& y_{k t} \geq 0 ; y_{k 0}=0 ; y_{k T}=0 ; \gamma_{k t} \in\{0,1\}
\end{aligned}
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$# Modell MLULSP bei gegebenem Rüstmuster 

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
\begin{aligned}
& 0 \leq q_{k t} \leq \widehat{q}_{k t} \\
& y_{k t} \geq 0 ; y_{k 0}=0 ; y_{k T}=0 ; \gamma_{k t} \text { gegeben }
\end{aligned}
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$# Modell MLULSP bei gegebenem Rüstmuster 

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
\begin{aligned}
& 0 \leq q_{k t} \leq \widehat{q}_{k t} \\
& y_{k t} \geq 0 ; y_{k 0}=0 ; y_{k T}=0 ; \gamma_{k t} \text { gegeben }
\end{aligned}
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$# Modell MLULSP bei gegebenem Rüstmuster 

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
\begin{aligned}
& 0 \leq q_{k t} \leq \widehat{q}_{k t} \\
& y_{k t} \geq 0 ; y_{k 0}=0 ; y_{k T}=0 ; \gamma_{k t} \text { gegeben }
\end{aligned} \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$

[^0]
[^0]:    Univ.-Prof. Dr. Michael Manitz
    Material-Logistik: Bestandsmanagement![img-23.jpeg](img-23.jpeg)

Local Search (lokale Suchverfahren)
deterministische Suchstrategie
vorübergehendes Zulassen einer Lösungsverschlechterung
$\triangleright$ Simulated Annealing
$\triangleright$ genetische Algorithmen# Lösungsverfahren für mehrstufige 

## Mehrprodukt-

## Losgrößenplanungsprobleme unter

## Beachtung von

Kapazitätsbeschränkungen# Eine Relax\&Fix-Heuristik von Maes und van Wassenhove# MLCLSP - Verfahren von Maes 

Univ.-Prof. Dr. Michael Manitz Material-Logistik: Bestandsmanagement# Beispiel Konvergierende Erzeugnisstruktur 

![img-24.jpeg](img-24.jpeg)

- Rüstzeiten (Opportunitätskosten): $\operatorname{tr}_{1}=\operatorname{tr}_{2}=\operatorname{tr}_{3}=0$
- Stückbearbeitungszeiten: $\mathrm{tb}_{1}=\mathrm{tb}_{2}=\mathrm{tb}_{3}=1$
- Ressourcenkapazität: $b_{1}=b_{2}=b_{3}=6$
- Lagerkostensätze: $h_{1}=h_{2}=h_{3}=1$
- Rüstkostensätze: $s_{1}=s_{2}=s_{3}=100$
- Bedarfsmengen: $d_{11}=d_{12}=d_{13}=1$ (d. h., normalisiert auf $100 \%$ )
- Bedarfsmengenanteil für Produkt $k$ und Periode $t$, der durch Produktion in Periode $\tau$ gedeckt wird: $\delta_{k \tau t}$# Beispiel Konvergierende Erzeugnisstruktur 

![img-25.jpeg](img-25.jpeg)
![img-26.jpeg](img-26.jpeg)
(vgl. Tempelmeier (2008))# Beispiel Konvergierende Erzeugnisstruktur 

![img-27.jpeg](img-27.jpeg)

Produkt 1
![img-28.jpeg](img-28.jpeg)

Produkt 2
![img-29.jpeg](img-29.jpeg)

Produkt 3
![img-30.jpeg](img-30.jpeg)

## Produkt 3

![img-31.jpeg](img-31.jpeg)

## Bedarfsmenge $\delta_{k \tau t}$

(vgl. Tempelmeier (2008))
Kapazitätsbelastung:
$\sum_{k \in \mathcal{K}} \operatorname{tb}_{k} \cdot q_{k 1}=9, \sum_{k \in \mathcal{K}} \operatorname{tb}_{k} \cdot q_{k 2}=0, \sum_{k \in \mathcal{K}} \operatorname{tb}_{k} \cdot q_{k 3}=0$# Beispiel Konvergierende Erzeugnisstruktur 

![img-32.jpeg](img-32.jpeg)

Produkt 1
![img-33.jpeg](img-33.jpeg)

Produkt 2
![img-34.jpeg](img-34.jpeg)

Produkt 3
![img-35.jpeg](img-35.jpeg)

## Produkt 3

![img-36.jpeg](img-36.jpeg)

Bedarfsmenge $\delta_{k \tau t}$
(vgl. Tempelmeier (2008))
Kapazitätsbelastung:
$\sum_{k \in \mathcal{K}} \operatorname{tb}_{k} \cdot q_{k 1}=6, \sum_{k \in \mathcal{K}} \operatorname{tb}_{k} \cdot q_{k 2}=3, \sum_{k \in \mathcal{K}} \operatorname{tb}_{k} \cdot q_{k 3}=0$# Beispiel Konvergierende Erzeugnisstruktur 

![img-37.jpeg](img-37.jpeg)

Produkt 1
![img-38.jpeg](img-38.jpeg)

Produkt 2
![img-39.jpeg](img-39.jpeg)

Produkt 3
![img-40.jpeg](img-40.jpeg)

## Produkt 3

![img-41.jpeg](img-41.jpeg)

## Bedarfsmenge $\delta_{k \tau t}$

(vgl. Tempelmeier (2008))
Kapazitätsbelastung:
$\sum_{k \in \mathcal{K}} \operatorname{tb}_{k} \cdot q_{k 1}=6, \sum_{k \in \mathcal{K}} \operatorname{tb}_{k} \cdot q_{k 2}=3, \sum_{k \in \mathcal{K}} \operatorname{tb}_{k} \cdot q_{k 3}=0$# Beispiel Konvergierende Erzeugnisstruktur 

![img-42.jpeg](img-42.jpeg)

Produkt 1
![img-43.jpeg](img-43.jpeg)

Produkt 2
![img-44.jpeg](img-44.jpeg)

Produkt 3
![img-45.jpeg](img-45.jpeg)

## Produkt 3

![img-46.jpeg](img-46.jpeg)

## Bedarfsmenge $\delta_{k \tau t}$

(vgl. Tempelmeier (2008))
Kapazitätsbelastung:
$\sum_{k \in \mathcal{K}} \operatorname{tb}_{k} \cdot q_{k 1}=5, \sum_{k \in \mathcal{K}} \operatorname{tb}_{k} \cdot q_{k 2}=4, \sum_{k \in \mathcal{K}} \operatorname{tb}_{k} \cdot q_{k 3}=0$# MLCLSP - Verfahren von Maes 

1. Vollständige Relaxation der Ganzzahligkeitsbedingungen# MLCLSP - Verfahren von Maes 

1. Vollständige Relaxation der Ganzzahligkeitsbedingungen
2. Fixierung von einzelnen Rüstvariablen# MLCLSP - Verfahren von Maes 

1. Vollständige Relaxation der Ganzzahligkeitsbedingungen
2. Fixierung von einzelnen Rüstvariablen
isoliert einzeln# MLCLSP - Verfahren von Maes 

1. Vollständige Relaxation der Ganzzahligkeitsbedingungen
2. Fixierung von einzelnen Rüstvariablen
isoliert einzeln
$\triangleright$ periodenbezogen vorwärts
$\triangleright$ periodenbezogen rückwärts
$\triangleright$ produktbezogen rückwärts
$\triangleright$ maximumorientiert# MLCLSP - Verfahren von Maes 

1. Vollständige Relaxation der Ganzzahligkeitsbedingungen
2. Fixierung von einzelnen Rüstvariablen
isoliert einzeln
$\triangleright$ periodenbezogen vorwärts
$\triangleright$ periodenbezogen rückwärts
$\triangleright$ produktbezogen rückwärts
$\triangleright$ maximumorientiert
$\Delta$ simultan# MLCLSP - Verfahren von Maes 

1. Vollständige Relaxation der Ganzzahligkeitsbedingungen
2. Fixierung von einzelnen Rüstvariablen
isoliert einzeln
$\triangleright$ periodenbezogen vorwärts
$\triangleright$ periodenbezogen rückwärts
$\triangleright$ produktbezogen rückwärts
$\triangleright$ maximumorientiert
$\triangleright$ simultan
3. Lösung des resultierenden LPs# MLCLSP - Verfahren von Maes 

1. Vollständige Relaxation der Ganzzahligkeitsbedingungen
2. Fixierung von einzelnen Rüstvariablen
isoliert einzeln
$\triangleright$ periodenbezogen vorwärts
$\triangleright$ periodenbezogen rückwärts
$\triangleright$ produktbezogen rückwärts
$\triangleright$ maximumorientiert
$\checkmark$ simultan
3. Lösung des resultierenden LPs
Wenn alle binären Rüstvariablen ganzzahling sind, Stop!# Eine Fix\&Optimize-Heuristik von 

Sahling# MLCLSP - Verfahren von Sahling 

Univ.-Prof. Dr. Michael Manitz Material-Logistik: Bestandsmanagement# Fix-and-Optimize-Heuristik# Modell MLCLSP 

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
q_{k t}-M \cdot \gamma_{k t} \leq 0
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
Wertebereich:

$$
q_{k t} \geq 0 ; y_{k t} \geq 0 ; y_{k 0}=0 ; y_{k T}=0 ; \gamma_{k t} \in\{0,1\} \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement# Modell MLCLSP 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}+p_{k t} \cdot q_{k t}\right)+\sum_{t=1}^{T} o_{t} \cdot O_{t}
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
q_{k t}-M \cdot \gamma_{k t} \leq 0
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
Wertebereich:

$$
q_{k t} \geq 0 ; y_{k t} \geq 0 ; y_{k 0}=0 ; y_{k T}=0 ; \gamma_{k t} \in\{0,1\} \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement# Modell MLCLSP 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}+p_{k t} \cdot q_{k t}\right)+\sum_{t=1}^{T} o_{t} \cdot O_{t}
$$

u. B. d. R.:

Bedarf in Periode $t$ :

$$
y_{k, t-1}+q_{k t}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t} \quad \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$

Kapazitäten in Periode $t$ :

$$
\sum_{k \in \mathcal{K}}\left(\operatorname{tb}_{k j} \cdot q_{k t}+\operatorname{tr}_{k j} \cdot \gamma_{k t}\right) \leq b_{j t}+O_{t} \quad \text { für alle } j \in \mathcal{J} \text { und } t=1,2, \ldots, T
$$

Es muss gerüstet werden, wenn $q_{k t}>0$ ist:

$$
q_{k t}-M \cdot \gamma_{k t} \leq 0
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
Wertebereich:

$$
q_{k t} \geq 0 ; y_{k t} \geq 0 ; y_{k 0}=0 ; y_{k T}=0 ; \gamma_{k t} \in\{0,1\} \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement# Modell MLCLSP 

Minimiere die Summe aus Rüstkosten und Lagerkosten:

$$
Z=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}+p_{k t} \cdot q_{k t}\right)+\sum_{t=1}^{T} o_{t} \cdot O_{t}
$$

u. B. d. R.:

Bedarf in Periode $t$ :

$$
y_{k, t-1}+q_{k t}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t} \quad \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$

Kapazitäten in Periode $t$ :

$$
\sum_{k \in \mathcal{K}}\left(\operatorname{tb}_{k j} \cdot q_{k t}+\operatorname{tr}_{k j} \cdot \gamma_{k t}\right)-O_{t} \leq b_{j t} \quad \text { für alle } j \in \mathcal{J} \text { und } t=1,2, \ldots, T
$$

Es muss gerüstet werden, wenn $q_{k t}>0$ ist:

$$
q_{k t}-M \cdot \gamma_{k t} \leq 0
$$

für alle $k \in \mathcal{K}$ und $t=1,2, \ldots, T$
Wertebereich:

$$
q_{k t} \geq 0 ; y_{k t} \geq 0 ; y_{k 0}=0 ; y_{k T}=0 ; \gamma_{k t} \in\{0,1\} \text { für alle } k \in \mathcal{K} \text { und } t=1,2, \ldots, T
$$

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement# Fix-and-Optimize-Heuristik# MLCLSP - Verfahren von Sahling 

Fix-and-Optimize-Heuristik in bezug auf Subprobleme:# MLCLSP - Verfahren von Sahling 

Fix-and-Optimize-Heuristik in bezug auf Subprobleme:
Produktorientierte Identifikation von Subproblemen:
Die Rüstvariablen für ein Produkt über alle Perioden werden optimiert.# MLCLSP - Verfahren von Sahling 

Fix-and-Optimize-Heuristik in bezug auf Subprobleme:
Produktorientierte Identifikation von Subproblemen:
Die Rüstvariablen für ein Produkt über alle Perioden werden optimiert.
Ressourcenorientierte Identifikation von Subproblemen:
Alle Rüstvariablen, die sich auf eine Ressource beziehen, - ggf. reduziert auf verschiedene, sich überlappende Zeitfenster - werden optimiert.# MLCLSP - Verfahren von Sahling 

Fix-and-Optimize-Heuristik in bezug auf Subprobleme:

- Produktorientierte Identifikation von Subproblemen:

Die Rüstvariablen für ein Produkt über alle Perioden werden optimiert.

- Ressourcenorientierte Identifikation von Subproblemen:

Alle Rüstvariablen, die sich auf eine Ressource beziehen, - ggf. reduziert auf verschiedene, sich überlappende Zeitfenster - werden optimiert.

- Prozessorientierte Identifikation von Subproblemen:

Die Rüstvariablen für Produkte, die durch direkte Vorgänger-Nachfol-ger-Beziehungen miteinander verbunden sind, - ggf. reduziert auf einzelne Zeitfenster - werden optimiert.# MLCLSP - Verfahren von Sahling 

Fix-and-Optimize-Heuristik in bezug auf Subprobleme:

- Produktorientierte Identifikation von Subproblemen:

Die Rüstvariablen für ein Produkt über alle Perioden werden optimiert.

- Ressourcenorientierte Identifikation von Subproblemen:

Alle Rüstvariablen, die sich auf eine Ressource beziehen, - ggf. reduziert auf verschiedene, sich überlappende Zeitfenster - werden optimiert.

- Prozessorientierte Identifikation von Subproblemen:

Die Rüstvariablen für Produkte, die durch direkte Vorgänger-Nachfol-ger-Beziehungen miteinander verbunden sind, - ggf. reduziert auf einzelne Zeitfenster - werden optimiert.

Alle nicht betrachteten Produkte und Perioden werden mit den besten gefundenen Werten für die binären Rüstvariablen vorbesetzt. Im Unterschied zu den Relax-and-Fix-Heuristiken gibt es nur ganzzahlige Lösungen für die Rüstvariablen.# Beispiel MLCLSP 

![img-47.jpeg](img-47.jpeg)

- Planungshorizont $T=10$ Perioden
- Primärbedarfsmengen für Produkt P: $d_{\mathrm{P} t}=6,11,15,7,28,7,6,12,5,15$
- Rüstzeiten (Opportunitätskosten): $\operatorname{tr}_{k}=10$
- Rüstkostensätze: $s_{k}=30$
- Lagerkostensätze: $h_{\mathrm{E}}=1.0, h_{\mathrm{B} 1}=1.1, h_{\mathrm{B} 2}=1.1, h_{\mathrm{P}}=4.0$
- Stückbearbeitungszeiten: $\mathrm{tb}_{k}=1$
$(k=\mathrm{E}, \mathrm{B} 1, \mathrm{~B} 2, \mathrm{P})$
- Ressourcenkapazität: $b=110$# MLCLSP — Fix\&Optimize-Heuristik 

## Beispiel MLCLSP

![img-48.jpeg](img-48.jpeg)
„Lot-for-lot"-Rüstmuster $\gamma_{k t}$ :

| Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| P | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| B1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| B2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| E | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |# BEispiel MLCLSP 

![img-49.jpeg](img-49.jpeg)
„Lot-for-lot"-Rüstmuster $\gamma_{k t}$ :

| Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| P | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| B1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| B2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| E | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

Zielfunktionswert $=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}\right)=1296.25$# BEispiel MLCLSP 

![img-50.jpeg](img-50.jpeg)
„Produktorientiert" optimiertes Rüstmuster für B1, $\gamma_{k t}=1$ nur noch für $k \in\{P, B 2, E\}$ :

| Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| P | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| B1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| B2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| E | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

Zielfunktionswert $=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}\right)=1169.50$# BEispiel MLCLSP 

![img-51.jpeg](img-51.jpeg)
„Produktorientiert" optimiertes Rüstmuster für E (B1 fixiert), $\gamma_{k t}=1$ nur noch für $k \in\{\mathrm{P}, \mathrm{B} 2\}$ :

| Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| P | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| B1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| B2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| E | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 |

Zielfunktionswert $=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}\right)=1129.625$# BEispiel MLCLSP 

![img-52.jpeg](img-52.jpeg)
„Produktorientiert" optimiertes Rüstmuster für B2 (B1 und E fixiert), $\gamma_{k t}=1$ nur noch für $k \in\{P\}$ :

| Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| P | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| B1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| B2 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 |
| E | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 |

Zielfunktionswert $=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}\right)=1044.10$# MLCLSP — Fix\&Optimize-Heuristik 

## Beispiel MLCLSP

![img-53.jpeg](img-53.jpeg)
„Produktorientiert" optimiertes Rüstmuster für P (B2, B1 und E):

| Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| P | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 |
| B1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| B2 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 |
| E | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 |

Zielfunktionswert $=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}\right)=1031.00$# BEispiel MLCLSP 

![img-54.jpeg](img-54.jpeg)
„Ressourcen- und periodenorientiert" optimiertes Rüstmuster $(t=5, \ldots, 10$ fixiert), $\gamma_{k t}$ :

| Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| P | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 |
| B1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| B2 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 1 |
| E | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 |

Zielfunktionswert $=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}\right)=997.10 \overline{6}$# BEispiel MLCLSP 

![img-55.jpeg](img-55.jpeg)
„Ressourcen- und periodenorientiert" optimiertes Rüstmuster ( $t=1,2$ und $t=7, \ldots, 10$ fixiert), $\gamma_{k t}$ :

| Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| P | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 |
| B1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| B2 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 |
| E | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |

Zielfunktionswert $=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}\right)=975.75$# BEispiel MLCLSP 

![img-56.jpeg](img-56.jpeg)
„Ressourcen- und periodenorientiert" optimiertes Rüstmuster $(t=1, \ldots, 4$ und $t=9, \ldots, 10$ fixiert), $\gamma_{k t}$ :

| Periode $t$ <br> Erzeugnis $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| P | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 1 |
| B1 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| B2 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 |
| E | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |

Zielfunktionswert $=\sum_{k \in \mathcal{K}} \sum_{t=1}^{T}\left(h_{k} \cdot y_{k t}+s_{k} \cdot \gamma_{k t}\right)=957.65$# Integration der Losgrößen- und Materialbedarfsplanung in ein PPS-System# MRP-Konzept 

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement![img-57.jpeg](img-57.jpeg)![img-58.jpeg](img-58.jpeg)![img-59.jpeg](img-59.jpeg)# MRP-Konzept 

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement
78-1# Praxis der Mengenplanung in Standard-PPS-SystemenPraxis der Mengenplanung in Standard-PPS-Systemen
Trennung von Materialbedarfsrechnung und LosgrößenplanungPraxis der Mengenplanung in Standard-PPS-Systemen
Trennung von Materialbedarfsrechnung und Losgrößenplanung
erzeugnisbezogen sukzessive Bedarfsermittlung mit Zusammenfassung von Nettobedarfsmengen (SIULSP)Praxis der Mengenplanung in Standard-PPS-Systemen
Trennung von Materialbedarfsrechnung und Losgrößenplanung
erzeugnisbezogen sukzessive Bedarfsermittlung mit Zusammenfassung von Nettobedarfsmengen (SIULSP)
$\Rightarrow$ Einbettung der Losgrößenplanung in die MaterialbedarfsrechnungPraxis der Mengenplanung in Standard-PPS-Systemen
Trennung von Materialbedarfsrechnung und Losgrößenplanung
erzeugnisbezogen sukzessive Bedarfsermittlung mit Zusammenfassung von Nettobedarfsmengen (SIULSP)
$\Rightarrow$ Einbettung der Losgrößenplanung in die Materialbedarfsrechnung
keine Berücksichtigung kostenmäßiger InterdependenzenPraxis der Mengenplanung in Standard-PPS-Systemen
Trennung von Materialbedarfsrechnung und Losgrößenplanung
erzeugnisbezogen sukzessive Bedarfsermittlung mit Zusammenfassung von Nettobedarfsmengen (SIULSP)
$\Rightarrow$ Einbettung der Losgrößenplanung in die Materialbedarfsrechnung
keine Berücksichtigung kostenmäßiger Interdependenzen
keine Berücksichtigung kapazitätsmäßiger InterdependenzenMRP-Konzept: Praxis der Mengenplanung

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement
79-1# MERw Konzept: Praxis der Mengenplanung 

## Beispiel

( vgl . Tempelmeier (2008))
Periodenbezogene Primärbedarfsmengen $d_{k t}$ :

| Periode $t$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :--: | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Produkt $k$ |  |  |  |  |  |  |  |  |  |  |  |  |
| 1 | - | - | - | - | 10 | - | 55 | 10 | - | 20 | 32 | 45 |
| 2 | - | - | - | - | - | 73 | 25 | - | 86 | 30 | - | 65 |# MER.SA'TOR 

## Beispiel

## Gozintograph

![img-60.jpeg](img-60.jpeg)# Beispiel 

## Gozintograph

![img-61.jpeg](img-61.jpeg)
(mit Ressourcenzuordnung)# MERw Konzept: Praxis der Mengenplanung 

## Beispiel

( vgl . Tempelmeier (2008))
Periodenbezogene Primärbedarfsmengen $d_{k t}$ :

| Periode $t$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :--: | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Produkt $k$ |  |  |  |  |  |  |  |  |  |  |  |  |
| 1 | - | - | - | - | 10 | - | 55 | 10 | - | 20 | 32 | 45 |
| 2 | - | - | - | - | - | 73 | 25 | - | 86 | 30 | - | 65 |# Beispiel 

Periodenbezogene Primärbedarfsmengen $d_{k t}$ :

| Periode $t$ <br> Produkt $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | - | - | - | - | 10 | - | 55 | 10 | - | 20 | 32 | 45 |
| 2 | - | - | - | - | - | 73 | 25 | - | 86 | 30 | - | 65 |

Stückbearbeitungszeiten: $\mathrm{tb}_{\mathrm{A}, k}=2, \mathrm{tb}_{\mathrm{B}, k}=1, \mathrm{tb}_{\mathrm{C}, k}=1 \quad(k=1, \ldots, 20)$# Beispiel 

Periodenbezogene Primärbedarfsmengen $d_{k t}$ :

| Periode $t$ <br> Produkt $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | - | - | - | - | 10 | - | 55 | 10 | - | 20 | 32 | 45 |
| 2 | - | - | - | - | - | 73 | 25 | - | 86 | 30 | - | 65 |

Stückbearbeitungszeiten: $\mathrm{tb}_{\mathrm{A}, k}=2, \mathrm{tb}_{\mathrm{B}, k}=1, \mathrm{tb}_{\mathrm{C}, k}=1 \quad(k=1, \ldots, 20)$
Technisch notwendige Vorlaufzeiten: $z_{1}=0, z_{2}=0, z_{k}=1 \quad(k=3, \ldots, 20)$# Beispiel 

Periodenbezogene Primärbedarfsmengen $d_{k t}$ :

| Periode $t$ <br> Produkt $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | - | - | - | - | 10 | - | 55 | 10 | - | 20 | 32 | 45 |
| 2 | - | - | - | - | - | 73 | 25 | - | 86 | 30 | - | 65 |

Stückbearbeitungszeiten: $\mathrm{tb}_{\mathrm{A}, k}=2, \mathrm{tb}_{\mathrm{B}, k}=1, \mathrm{tb}_{\mathrm{C}, k}=1 \quad(k=1, \ldots, 20)$
Technisch notwendige Vorlaufzeiten: $z_{1}=0, z_{2}=0, z_{k}=1 \quad(k=3, \ldots, 20)$
Rüstzeiten: $\operatorname{tr}_{k}=10 \quad(k=1, \ldots, 20)$# Beispiel 

Periodenbezogene Primärbedarfsmengen $d_{k t}$ :

| Periode $t$ <br> Produkt $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | - | - | - | - | 10 | - | 55 | 10 | - | 20 | 32 | 45 |
| 2 | - | - | - | - | - | 73 | 25 | - | 86 | 30 | - | 65 |

Stückbearbeitungszeiten: $\mathrm{tb}_{\mathrm{A}, k}=2, \mathrm{tb}_{\mathrm{B}, k}=1, \mathrm{tb}_{\mathrm{C}, k}=1 \quad(k=1, \ldots, 20)$
Technisch notwendige Vorlaufzeiten: $z_{1}=0, z_{2}=0, z_{k}=1 \quad(k=3, \ldots, 20)$
Rüstzeiten: $\operatorname{tr}_{k}=10 \quad(k=1, \ldots, 20)$
Periodenkapazität: $b_{j t}=1000 \quad(j=\mathrm{A}, \mathrm{B}, \mathrm{C} ; t=1, \ldots, 12)$# Beispiel 

Periodenbezogene Primärbedarfsmengen $d_{k t}$ :

| Periode $t$ <br> Produkt $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | - | - | - | - | 10 | - | 55 | 10 | - | 20 | 32 | 45 |
| 2 | - | - | - | - | - | 73 | 25 | - | 86 | 30 | - | 65 |

Stückbearbeitungszeiten: $\mathrm{tb}_{\mathrm{A}, k}=2, \mathrm{tb}_{\mathrm{B}, k}=1, \mathrm{tb}_{\mathrm{C}, k}=1 \quad(k=1, \ldots, 20)$
Technisch notwendige Vorlaufzeiten: $z_{1}=0, z_{2}=0, z_{k}=1 \quad(k=3, \ldots, 20)$
Rüstzeiten: $\operatorname{tr}_{k}=10 \quad(k=1, \ldots, 20)$
Periodenkapazität: $b_{j t}=1000 \quad(j=\mathrm{A}, \mathrm{B}, \mathrm{C} ; t=1, \ldots, 12)$
Rüstkosten: $s_{k}=100 \quad(k=1, \ldots, 20)$# Beispiel 

Periodenbezogene Primärbedarfsmengen $d_{k t}$ :

| Periode $t$ <br> Produkt $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | - | - | - | - | 10 | - | 55 | 10 | - | 20 | 32 | 45 |
| 2 | - | - | - | - | - | 73 | 25 | - | 86 | 30 | - | 65 |

Stückbearbeitungszeiten: $\mathrm{tb}_{\mathrm{A}, k}=2, \mathrm{tb}_{\mathrm{B}, k}=1, \mathrm{tb}_{\mathrm{C}, k}=1 \quad(k=1, \ldots, 20)$
Technisch notwendige Vorlaufzeiten: $z_{1}=0, z_{2}=0, z_{k}=1 \quad(k=3, \ldots, 20)$
Rüstzeiten: $\operatorname{tr}_{k}=10 \quad(k=1, \ldots, 20)$
Periodenkapazität: $b_{j t}=1000 \quad(j=\mathrm{A}, \mathrm{B}, \mathrm{C} ; t=1, \ldots, 12)$
Rüstkosten: $s_{k}=100 \quad(k=1, \ldots, 20)$
Lagerkostensätze $h_{k}$ :

| $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $h_{k}$ | 27 | 43 | 4 | 4 | 6 | 11 | 14 | 3 | 3 | 5 | 10 | 3 | 2 | 2 | 3 | 2 | 1 | 1 | 1 | 1 |# Beispiel Produktionsplan nach MRP-Konzept 

(vgl. Tempelmeier (2008))

| Periode $t$ <br> Produkt $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | - | - | - | - | 10 | - | 55 | 10 | - | 20 | 32 | 45 |
| 2 | - | - | - | - | - | 73 | 25 | - | 86 | 30 | - | 65 |
| 3 | - | - | - | 10 | - | 65 | - | - | 20 | 32 | 45 | - |
| 4 | - | - | - | 40 | - | 220 | 40 | - | 80 | 128 | 180 | - |
| 5 | - | - | - | 10 | 73 | 90 | - | 86 | 50 | 32 | 110 | - |
| 6 | - | - | - | - | 146 | 50 | - | 172 | 60 | - | 130 | - |
| 7 | - | - | - | - | 73 | 25 | - | 86 | 30 | - | 65 | - |
| 8 | - | - | 10 | - | 65 | - | - | 52 | - | 45 | - | - |
| 9 | - | - | 40 | - | 220 | 40 | - | 80 | 128 | 180 | - | - |
| 10 | - | - | 10 | 73 | 90 | - | 86 | 50 | 32 | 110 | - | - |
| 11 | - | - | - | 219 | 75 | - | 258 | 90 | - | 195 | - | - |
| 12 | - | - | - | 98 | - | - | 116 | - | - | 65 | - | - |
| 13 | - | 10 | - | 65 | - | - | 52 | - | 45 | - | - | - |
| 14 | - | 60 | 146 | 440 | - | 172 | 180 | 192 | 400 | - | - | - |
| 15 | - | - | 657 | 225 | - | 774 | 270 | - | 585 | - | - | - |
| 16 | - | - | 98 | - | - | 116 | - | - | 65 | - | - | - |
| 17 | 10 | - | 65 | - | - | 52 | - | 45 | - | - | - | - |
| 18 | 60 | 146 | 440 | - | 172 | 180 | 192 | 400 | - | - | - | - |
| 19 | - | 657 | 225 | - | 774 | 270 | - | 585 | - | - | - | - |
| 20 | - | 755 | 225 | - | 890 | 270 | - | 650 | - | - | - | - |

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement
79-12# Beispiel Kapazitätsbelastung nach MRP-Konzept (vgl. Tempelmeier (2008)) 

$\sum_{k \in \mathcal{K}}\left(\operatorname{tb}_{j k} \cdot q_{k t}+\operatorname{tr}_{k} \cdot \gamma_{k t}\right)$
![img-62.jpeg](img-62.jpeg)![img-63.jpeg](img-63.jpeg)![img-64.jpeg](img-64.jpeg)![img-65.jpeg](img-65.jpeg)![img-66.jpeg](img-66.jpeg)Beispiel Ressourcenbelegung nach MRP-Konzept (vgl. Tempelmeier (2008))
![img-67.jpeg](img-67.jpeg)![img-68.jpeg](img-68.jpeg)![img-69.jpeg](img-69.jpeg)![img-70.jpeg](img-70.jpeg)Fallstudie II Produktionsmengen nach MRP-Konzept (Tempelmeier (2008))

| Periode $t$ <br> Produkt $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | - | - | - | - | 10 | - | 55 | 10 | - | 20 | 32 | 45 |
| 2 | - | - | - | - | - | 73 | 25 | - | 86 | 30 | - | 65 |
| 3 | - | - | - | 10 | - | 65 | - | - | 20 | 32 | 45 | - |
| 4 | - | - | - | 40 | - | 220 | 40 | - | 80 | 128 | 180 | - |
| 5 | - | - | - | 10 | 73 | 90 | - | 86 | 50 | 32 | 110 | - |
| 6 | - | - | - | - | 146 | 50 | - | 172 | 60 | - | 130 | - |
| 7 | - | - | - | - | 73 | 25 | - | 86 | 30 | - | 65 | - |
| 8 | - | - | 10 | - | 65 | - | - | 52 | - | 45 | - | - |
| 9 | - | - | 40 | - | 220 | 40 | - | 80 | 128 | 180 | - | - |
| 10 | - | - | 10 | 73 | 90 | - | 86 | 50 | 32 | 110 | - | - |
| 11 | - | - | - | 219 | 75 | - | 258 | 90 | - | 195 | - | - |
| 12 | - | - | - | 98 | - | - | 116 | - | - | 65 | - | - |
| 13 | - | 10 | - | 65 | - | - | 52 | - | 45 | - | - | - |
| 14 | - | 60 | 146 | 440 | - | 172 | 180 | 192 | 400 | - | - | - |
| 15 | - | - | 657 | 225 | - | 774 | 270 | - | 585 | - | - | - |
| 16 | - | - | 98 | - | - | 116 | - | - | 65 | - | - | - |
| 17 | 10 | - | 65 | - | - | 52 | - | 45 | - | - | - | - |
| 18 | 60 | 146 | 440 | - | 172 | 180 | 192 | 400 | - | - | - | - |
| 19 | - | 657 | 225 | - | 774 | 270 | - | 585 | - | - | - | - |
| 20 | - | 755 | 225 | - | 890 | 270 | - | 650 | - | - | - | - |

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement
81-1# MRIP ${ }^{16}$ : Kapazitätsorientierte Losgrößenplanung 

## Fallstudie II Zulässiger Produktionsplan (MLCLSP) (Tempelmeier (2008))

| Periode $t$ <br> Produkt $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | - | - | - | - | 10 | - | 55 | 10 | - | 20 | 32 | 45 |
| 2 | - | - | - | - | - | 73 | 25 | - | 86 | 30 | - | 65 |
| 3 | - | - | - | 75 | - | - | - | - | 95 | 2 | - | - |
| 4 | - | - | - | 40 | - | 220 | 40 | - | 80 | 170 | 138 | - |
| 5 | - | - | - | 93 | 20 | 50 | 68 | 110 | - | - | 110 | - |
| 6 | - | - | - | 34 | 112 | 50 | - | 172 | 60 | - | 130 | - |
| 7 | - | - | - | - | 73 | 25 | - | 86 | 30 | - | 65 | - |
| 8 | - | - | 75 | - | - | - | - | 97 | - | - | - | - |
| 9 | - | - | 40 | - | 260 | - | 131 | - | 119 | 138 | - | - |
| 10 | - | - | 93 | 86 | - | 52 | 110 | - | - | 110 | - | - |
| 11 | - | - | 34 | 185 | 75 | - | 258 | 90 | - | 195 | - | - |
| 12 | - | - | - | 98 | - | - | 86 | 30 | - | 65 | - | - |
| 13 | - | 75 | - | - | - | - | 97 | - | - | - | - | - |
| 14 | - | 226 | 172 | 260 | 249 | 206 | - | 119 | 358 | - | - | - |
| 15 | - | 102 | 555 | 225 | - | 774 | 270 | - | 585 | - | - | - |
| 16 | - | - | 98 | - | - | 86 | 30 | - | 65 | - | - | - |
| 17 | 75 | - | - | - | - | 97 | - | - | - | - | - | - |
| 18 | 398 | - | 389 | 326 | - | - | 119 | 358 | - | - | - | - |
| 19 | 144 | 513 | 225 | - | 774 | 270 | - | 585 | - | - | - | - |
| 20 | 288 | 467 | 225 | 654 | 206 | 300 | 650 | - | - | - | - | - |

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement
81-2# MRP ${ }^{\text {Ic }}$ : Kapazitätsorientierte Losgrößenplanung 

## Fallstudie II Kapazitätsbelastung nach MRP-Konzept (Tempelmeier (2008))

$\sum_{k \in \mathcal{K}}\left(\operatorname{tb}_{j k} \cdot q_{k t}+\operatorname{tr}_{k} \cdot \gamma_{k t}\right)$
![img-71.jpeg](img-71.jpeg)# Fallstudie II Kapazitätsbelastung (MLCLSP) 

$\sum_{k \in \mathcal{K}}\left(\operatorname{tb}_{j k} \cdot q_{k t}+\operatorname{tr}_{k} \cdot \gamma_{k t}\right)$
![img-72.jpeg](img-72.jpeg)

| Periode $t$ <br> Ressource $j$ | 1 | 2 | 3 | 4 | 5 | 6 |
| :-- | --: | --: | --: | --: | --: | --: |
| Werkstatt A | - | - | 446 | 706 | 1000 | 1000 |
| Werkstatt B | - | 433 | 791 | 808 | 344 | 1000 |
| Werkstatt C | 945 | 1000 | 977 | 1000 | 1000 | 793 |


| Periode $t$ <br> Ressource $j$ | 7 | 8 | 9 | 10 | 11 | 12 |
| :-- | --: | --: | --: | --: | --: | --: |
| Werkstatt A | 918 | 1000 | 1000 | 1000 | 1000 | 240 |
| Werkstatt B | 751 | 269 | 963 | 280 | - | - |
| Werkstatt C | 829 | 963 | 75 | - | - | - |

(vgl. Tempelmeier (2008))

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement![img-73.jpeg](img-73.jpeg)# arbeitsgangbezogene Durchlaufzeiten 

![img-74.jpeg](img-74.jpeg)
(aus Tempelmeier (2006))# MERCATOR 

## arbeitsgangbezogene Verspätungen

![img-75.jpeg](img-75.jpeg)
(aus Tempelmeier (2006))Materialdisposition in einem Konzept der rollierenden Planung# Ro1lierende Losgrößenplanung 

![img-76.jpeg](img-76.jpeg)
(vgl. Tempelmeier (2006))# Beispiel Rollierende Planung (MLCLSP) 

![img-77.jpeg](img-77.jpeg)

Primärbedarfsmengen:

| $t$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 | 106 | 103 | 93 |
| $d_{2 t}$ | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 | 131 | 154 | 139 |

Weitere Daten:
$b_{\mathrm{At}}=350, b_{\mathrm{B} t}=500$
$s_{1}=s_{2}=s_{3}=400 ; h_{1}=h_{2}=2, h_{3}=1$
$\mathrm{tb}_{1}=\mathrm{tb}_{2}=\mathrm{tb}_{3}=1, \operatorname{tr}_{1}=\operatorname{tr}_{2}=\operatorname{tr}_{3}=0$
$z_{1}=z_{2}=0, z_{3}=2$# Mehrstufige Losgrößenplanung 

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
y_{k, t-1}+q_{k, t-z_{k}}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t} \quad\binom{k \in \mathcal{K}}{t=0+z_{k}+1, \ldots, 0+T}
$$# Mehrstufige Losgrößenplanung 

Lagerbilanzgleichungen (im Planungslauf am Ende von Periode $\tau$ )

$$
y_{k, t-1}+q_{k, t-z_{k}}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t} \quad\binom{k \in \mathcal{K}}{t=\tau+z_{k}+1, \ldots, \tau+T}
$$# Mehrstufige Losgrößenplanung 

Lagerbilanzgleichungen (im Planungslauf am Ende von Periode $\tau=n \cdot R$ )

$$
y_{k, t-1}+q_{k, t-z_{k}}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t}
$$

$$
\binom{k \in \mathcal{K}}{t=\tau+z_{k}+1, \ldots, \tau+T}
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
y_{k, t-1}+x_{k t}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}-y_{k t}=d_{k t}
$$

$$
\binom{k \in \mathcal{K}}{t=\tau+1, \ldots, \tau+z_{k}}
$$

$$
(n=0,1,2, \ldots)
$$

Beispiel Rollierende Planung zum Zeitpunkt $\tau=0: x_{31}=292, x_{32}=350$

$$
\begin{array}{ll}
y_{30}+292-q_{11}-q_{21}-y_{31}=0 & (t=1) \\
y_{31}+350-q_{12}-q_{22}-y_{32}=0 & (t=2)
\end{array}
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
$$

Beispiel Rollierende Planung zum Zeitpunkt $\tau=0: x_{31}=292, x_{32}=350$

$$
\begin{aligned}
& y_{30}+292-q_{11}-q_{21}-y_{31}=0 \\
& y_{31}+350-q_{12}-q_{22}-y_{32}=0 \\
& y_{32}+q_{31}-q_{13}-q_{23}-y_{33}=0
\end{aligned}
$$

$$
(t=1)
$$

$$
(t=2)
$$

$$
(t=3)
$$

USW.Beispiel MLCLSP für 8 Perioden (s. o.)
(vgl. Tempelmeier (2008))# Beispiel MLCLSP für 8 Perioden (s. o.) 

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :Beispiel MLCLSP für 8 Perioden (s. o.)
(vgl. Tempelmeier (2008))
Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
|  |  |  |  |  |  |  |  |  |  |  |Beispiel MLCLSP für 8 Perioden (s. o.)
(vgl. Tempelmeier (2008))
Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
| Sekundärbedarf $_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153 |# Beispiel MLCLSP für 8 Perioden (s. o.) 

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153 |
| $x_{3, t+2}$ | 292 | 350 |  |  |  |  |  |  |  |  |# Beispiel MLCLSP für 8 Perioden (s. o.) 

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153 |
| $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | - |# Beispiel MLCLSP für 8 Perioden (s. o.) 

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153 |
| $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | - |
| $y_{3 t}$ |  | 0 | 0 | 0 | 73 | 245 | 3 | 3 | 153 | 0 |# Beispiel MLCLSP für 8 Perioden (s. o.) 

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153 |
| $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | - |
| $y_{3 t}$ |  | 0 | 0 | 0 | 73 | 245 | 3 | 3 | 153 | 0 |

$y_{31}=$# Beispiel MLCLSP für 8 Perioden (s. o.) 

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153 |
| $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | - |
| $y_{3 t}$ |  | 0 | 0 | 0 | 73 | 245 | 3 | 3 | 153 | 0 |

$y_{31}=y_{30}$# Beispiel MLCLSP für 8 Perioden (s. o.) 

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153 |
| $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | - |
| $y_{3 t}$ |  | 0 | 0 | 0 | 73 | 245 | 3 | 3 | 153 | 0 |

$y_{31}=y_{30}+x_{31}$# Beispiel MLCLSP für 8 Perioden (s. o.) 

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153 |
| $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | - |
| $y_{3 t}$ |  | 0 | 0 | 0 | 73 | 245 | 3 | 3 | 153 | 0 |

$y_{31}=y_{30}+x_{31}-$ Sekundärbedarf ${ }_{31}$# Beispiel MLCLSP für 8 Perioden (s.o.) 

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153 |
| $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | - |
| $y_{3 t}$ |  | 0 | 0 | 0 | 73 | 245 | 3 | 3 | 153 | 0 |

$y_{31}=y_{30}+x_{31}-$ Sekundärbedarf $_{31}=0+292-292$# Beispiel MLCLSP für 8 Perioden (s.o.) 

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153 |
| $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | - |
| $y_{3 t}$ |  | 0 | 0 | 0 | 73 | 245 | 3 | 3 | 153 | 0 |

$y_{31}=y_{30}+x_{31}-$ Sekundärbedarf $_{31}=0+292-292=0$# Beispiel MLCLSP für 8 Perioden (s.o.) 

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153 |
| $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | - |
| $y_{3 t}$ |  | 0 | 0 | 0 | 73 | 245 | 3 | 3 | 153 | 0 |

$y_{31}=y_{30}+x_{31}-$ Sekundärbedarf $_{31}=0+292-292=0$
$y_{32}=y_{31}+x_{32}-$ Sekundärbedarf $_{32}=0+350-350=0$# Beispiel MLCLSP für 8 Perioden (s.o.) 

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153 |
| $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | - |
| $y_{3 t}$ |  | 0 | 0 | 0 | 73 | 245 | 3 | 3 | 153 | 0 |

$y_{31}=y_{30}+x_{31}-$ Sekundärbedarf $_{31}=0+292-292=0$
$y_{32}=y_{31}+x_{32}-$ Sekundärbedarf $_{32}=0+350-350=0$
$y_{33}=$# Beispiel MLCLSP für 8 Perioden (s.o.) 

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153 |
| $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | - |
| $y_{3 t}$ |  | 0 | 0 | 0 | 73 | 245 | 3 | 3 | 153 | 0 |

$y_{31}=y_{30}+x_{31}-$ Sekundärbedarf $_{31}=0+292-292=0$
$y_{32}=y_{31}+x_{32}-$ Sekundärbedarf $_{32}=0+350-350=0$
$y_{33}=y_{32}$# Beispiel MLCLSP für 8 Perioden (s.o.) 

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153 |
| $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | - |
| $y_{3 t}$ |  | 0 | 0 | 0 | 73 | 245 | 3 | 3 | 153 | 0 |

$y_{31}=y_{30}+x_{31}-$ Sekundärbedarf $_{31}=0+292-292=0$
$y_{32}=y_{31}+x_{32}-$ Sekundärbedarf $_{32}=0+350-350=0$
$y_{33}=y_{32}+q_{31}$# Beispiel MLCLSP für 8 Perioden (s.o.) 

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153 |
| $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | - |
| $y_{3 t}$ |  | 0 | 0 | 0 | 73 | 245 | 3 | 3 | 153 | 0 |

$y_{31}=y_{30}+x_{31}-$ Sekundärbedarf $_{31}=0+292-292=0$
$y_{32}=y_{31}+x_{32}-$ Sekundärbedarf $_{32}=0+350-350=0$
$y_{33}=y_{32}+q_{31}-$ Sekundärbedarf $_{33}$# Beispiel MLCLSP für 8 Perioden (s.o.) 

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153 |
| $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | - |
| $y_{3 t}$ |  | 0 | 0 | 0 | 73 | 245 | 3 | 3 | 153 | 0 |

$y_{31}=y_{30}+x_{31}-$ Sekundärbedarf $_{31}=0+292-292=0$
$y_{32}=y_{31}+x_{32}-$ Sekundärbedarf $_{32}=0+350-350=0$
$y_{33}=y_{32}+q_{31}-$ Sekundärbedarf $_{33}=0$# Beispiel MLCLSP für 8 Perioden (s.o.) 

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153 |
| $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | - |
| $y_{3 t}$ |  | 0 | 0 | 0 | 73 | 245 | 3 | 3 | 153 | 0 |

$y_{31}=y_{30}+x_{31}-$ Sekundärbedarf $_{31}=0+292-292=0$
$y_{32}=y_{31}+x_{32}-$ Sekundärbedarf $_{32}=0+350-350=0$
$y_{33}=y_{32}+q_{31}-$ Sekundärbedarf $_{33}=0+377$# Beispiel MLCLSP für 8 Perioden (s.o.) 

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153 |
| $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | - |
| $y_{3 t}$ |  | 0 | 0 | 0 | 73 | 245 | 3 | 3 | 153 | 0 |

$y_{31}=y_{30}+x_{31}-$ Sekundärbedarf $_{31}=0+292-292=0$
$y_{32}=y_{31}+x_{32}-$ Sekundärbedarf $_{32}=0+350-350=0$
$y_{33}=y_{32}+q_{31}-$ Sekundärbedarf $_{33}=0+377-304$# Beispiel MLCLSP für 8 Perioden (s.o.) 

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153 |
| $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | - |
| $y_{3 t}$ |  | 0 | 0 | 0 | 73 | 245 | 3 | 3 | 153 | 0 |

$y_{31}=y_{30}+x_{31}-$ Sekundärbedarf $_{31}=0+292-292=0$
$y_{32}=y_{31}+x_{32}-$ Sekundärbedarf $_{32}=0+350-350=0$
$y_{33}=y_{32}+q_{31}-$ Sekundärbedarf $_{33}=0+377-304=73$# Beispiel MLCLSP für 8 Perioden (s.o.) 

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153 |
| $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | - |
| $y_{3 t}$ |  | 0 | 0 | 0 | 73 | 245 | 3 | 3 | 153 | 0 |

$y_{31}=y_{30}+x_{31}-$ Sekundärbedarf $_{31}=0+292-292=0$
$y_{32}=y_{31}+x_{32}-$ Sekundärbedarf $_{32}=0+350-350=0$
$y_{33}=y_{32}+q_{31}-$ Sekundärbedarf $_{33}=0+377-304=73$
$y_{34}=y_{33}+q_{32}-$ Sekundärbedarf $_{34}=73+500-328=245$# Beispiel MLCLSP für 8 Perioden (s.o.) 

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153 |
| $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | - |
| $y_{3 t}$ |  | 0 | 0 | 0 | 73 | 245 | 3 | 3 | 153 | 0 |

$y_{31}=y_{30}+x_{31}-$ Sekundärbedarf $_{31}=0+292-292=0$
$y_{32}=y_{31}+x_{32}-$ Sekundärbedarf $_{32}=0+350-350=0$
$y_{33}=y_{32}+q_{31}-$ Sekundärbedarf $_{33}=0+377-304=73$
$y_{34}=y_{33}+q_{32}-$ Sekundärbedarf $_{34}=73+500-328=245$
$y_{35}=y_{34}+q_{33}-$ Sekundärbedarf $_{35}=245+0-242=3$# Beispiel MLCLSP für 8 Perioden (s.o.) 

Optimale Lösung beim ersten Planungslauf im Zeitpunkt $\tau=0$ :

| $t$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $d_{1 t}$ |  |  | 111 | 110 | 103 | 118 | 104 | 106 | 101 | 111 |
| $q_{1 t}$ |  |  | 126 | 198 | 0 | 328 | 0 | 0 | 212 | 0 |
| $y_{1 t}$ |  | 0 | 15 | 103 | 0 | 210 | 106 | 0 | 111 | 0 |
| $d_{2 t}$ |  |  | 166 | 152 | 148 | 156 | 125 | 116 | 139 | 153 |
| $q_{2 t}$ |  |  | 166 | 152 | 304 | 0 | 242 | 0 | 138 | 153 |
| $y_{2 t}$ |  | 0 | 0 | 0 | 156 | 0 | 117 | 1 | 0 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 292 | 350 | 304 | 328 | 242 | 0 | 350 | 153 |
| $x_{3, t+2}$ bzw. $q_{3 t}$ | 292 | 350 | 377 | 500 | 0 | 0 | 500 | 0 | - | - |
| $y_{3 t}$ |  | 0 | 0 | 0 | 73 | 245 | 3 | 3 | 153 | 0 |

$y_{31}=y_{30}+x_{31}-$ Sekundärbedarf $_{31}=0+292-292=0$
$y_{32}=y_{31}+x_{32}-$ Sekundärbedarf $_{32}=0+350-350=0$
$y_{33}=y_{32}+q_{31}-$ Sekundärbedarf $_{33}=0+377-304=73$
$y_{34}=y_{33}+q_{32}-$ Sekundärbedarf $_{34}=73+500-328=245$
$y_{35}=y_{34}+q_{33}-$ Sekundärbedarf $_{35}=245+0-242=3$
usw.# Beispiel MLCLSP für 8 Perioden (s. o.) 

Optimale Lösung beim zweiten Planungslauf im Zeitpunkt $\tau=3$ :

| $t$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $t^{\prime}$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| $d_{1 t}$ |  |  | 118 | 104 | 106 | 101 | 111 | 106 | 103 | 93 |
| $q_{1 t}$ |  |  | 328 | 0 | 0 | 212 | 0 | 209 | 0 | 93 |
| $y_{1 t}$ |  | 0 | 210 | 106 | 0 | 111 | 0 | 103 | 0 | 0 |
| $d_{2 t}$ |  |  | 156 | 125 | 116 | 139 | 153 | 131 | 154 | 139 |
| $q_{2 t}$ |  |  | 0 | 242 | 0 | 138 | 284 | 0 | 293 | 0 |
| $y_{2 t}$ |  | 156 | 0 | 117 | 1 | 0 | 131 | 0 | 139 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 328 | 242 | 0 | 350 | 284 | 209 | 293 | 93 |
| $x_{3, t+2}$ | 500 | 0 | - | - | - | - | - | - | - | - |
| $q_{3 t}$ | - | - | 0 | 347 | 493 | 0 | 386 | 0 | - | - |
| $y_{3 t}$ |  | 73 | 245 | 3 | 3 | 0 | 209 | 0 | 93 | 0 |# Beispiel MLCLSP für 8 Perioden (s. o.) 

Optimale Lösung beim zweiten Planungslauf im Zeitpunkt $\tau=3$ :

| $t$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $t^{\prime}$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| $d_{1 t}$ |  |  | 118 | 104 | 106 | 101 | 111 | 106 | 103 | 93 |
| $q_{1 t}$ |  |  | 328 | 0 | 0 | 212 | 0 | 209 | 0 | 93 |
| $y_{1 t}$ |  | 0 | 210 | 106 | 0 | 111 | 0 | 103 | 0 | 0 |
| $d_{2 t}$ |  |  | 156 | 125 | 116 | 139 | 153 | 131 | 154 | 139 |
| $q_{2 t}$ |  |  | 0 | 242 | 0 | 138 | 284 | 0 | 293 | 0 |
| $y_{2 t}$ |  | 156 | 0 | 117 | 1 | 0 | 131 | 0 | 139 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 328 | 242 | 0 | 350 | 284 | 209 | 293 | 93 |
| $x_{3, t+2}$ | 500 | 0 | - | - | - | - | - | - | - | - |
| $q_{3 t}$ | - | - | 0 | 347 | 493 | 0 | 386 | 0 | - | - |
| $y_{3 t}$ |  | 73 | 245 | 3 | 3 | 0 | 209 | 0 | 93 | 0 |

Reaktionsmöglichkeiten auf einen Anstieg der Primärbedarfsmenge $d_{11}$ für Produkt 1 in Periode 1:
$>$ Anstieg $\leq 3: 118 \leq d_{11} \leq 118+3=121$ q $_{11} \nearrow 331, y_{31} \searrow 242, q_{22}=242$# Beispiel MLCLSP für 8 Perioden (s. o.) 

Optimale Lösung beim zweiten Planungslauf im Zeitpunkt $\tau=3$ :

| $t$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $t^{\prime}$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| $d_{1 t}$ |  |  | 118 | 104 | 106 | 101 | 111 | 106 | 103 | 93 |
| $q_{1 t}$ |  |  | 328 | 0 | 0 | 212 | 0 | 209 | 0 | 93 |
| $y_{1 t}$ |  | 0 | 210 | 106 | 0 | 111 | 0 | 103 | 0 | 0 |
| $d_{2 t}$ |  |  | 156 | 125 | 116 | 139 | 153 | 131 | 154 | 139 |
| $q_{2 t}$ |  |  | 0 | 242 | 0 | 138 | 284 | 0 | 293 | 0 |
| $y_{2 t}$ |  | 156 | 0 | 117 | 1 | 0 | 131 | 0 | 139 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 328 | 242 | 0 | 350 | 284 | 209 | 293 | 93 |
| $x_{3, t+2}$ | 500 | 0 | - | - | - | - | - | - | - | - |
| $q_{3 t}$ | - | - | 0 | 347 | 493 | 0 | 386 | 0 | - | - |
| $y_{3 t}$ |  | 73 | 245 | 3 | 3 | 0 | 209 | 0 | 93 | 0 |

Reaktionsmöglichkeiten auf einen Anstieg der Primärbedarfsmenge $d_{11}$ für Produkt 1 in Periode 1:
$3<$ Anstieg $\leq 109: 121 \leq d_{11} \leq 118+109=227 q_{11} \nearrow 331, y_{31} \searrow 242, q_{13}>0$# Beispiel MLCLSP für 8 Perioden (s. o.) 

Optimale Lösung beim zweiten Planungslauf im Zeitpunkt $\tau=3$ :

| $t$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $t^{\prime}$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| $d_{1 t}$ |  |  | 118 | 104 | 106 | 101 | 111 | 106 | 103 | 93 |
| $q_{1 t}$ |  |  | 328 | 0 | 0 | 212 | 0 | 209 | 0 | 93 |
| $y_{1 t}$ |  | 0 | 210 | 106 | 0 | 111 | 0 | 103 | 0 | 0 |
| $d_{2 t}$ |  |  | 156 | 125 | 116 | 139 | 153 | 131 | 154 | 139 |
| $q_{2 t}$ |  |  | 0 | 242 | 0 | 138 | 284 | 0 | 293 | 0 |
| $y_{2 t}$ |  | 156 | 0 | 117 | 1 | 0 | 131 | 0 | 139 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 328 | 242 | 0 | 350 | 284 | 209 | 293 | 93 |
| $x_{3, t+2}$ | 500 | 0 | - | - | - | - | - | - | - | - |
| $q_{3 t}$ | - | - | 0 | 347 | 493 | 0 | 386 | 0 | - | - |
| $y_{3 t}$ |  | 73 | 245 | 3 | 3 | 0 | 209 | 0 | 93 | 0 |

Reaktionsmöglichkeiten auf einen Anstieg der Primärbedarfsmenge $d_{11}$ für Produkt 1 in Periode 1:
$109<$ Anstieg $\leq 226: 227 \leq d_{11} \leq 118+226=344 q_{11} \nearrow 448, y_{31} \searrow 125, q_{22} \searrow 125$Beispiel MLCLSP für 8 Perioden (s. o.)
(vgl. Tempelmeier (2008))
Optimale Lösung beim zweiten Planungslauf im Zeitpunkt $\tau=3$ :

| $t$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $t^{\prime}$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| $d_{1 t}$ |  |  | 118 | 104 | 106 | 101 | 111 | 106 | 103 | 93 |
| $q_{1 t}$ |  |  | 328 | 0 | 0 | 212 | 0 | 209 | 0 | 93 |
| $y_{1 t}$ |  | 0 | 210 | 106 | 0 | 111 | 0 | 103 | 0 | 0 |
| $d_{2 t}$ |  |  | 156 | 125 | 116 | 139 | 153 | 131 | 154 | 139 |
| $q_{2 t}$ |  |  | 0 | 242 | 0 | 138 | 284 | 0 | 293 | 0 |
| $y_{2 t}$ |  | 156 | 0 | 117 | 1 | 0 | 131 | 0 | 139 | 0 |
| Sekundärbedarf ${ }_{3 t}$ |  |  | 328 | 242 | 0 | 350 | 284 | 209 | 293 | 93 |
| $x_{3, t+2}$ | 500 | 0 | - | - | - | - | - | - | - | - |
| $q_{3 t}$ | - | - | 0 | 347 | 493 | 0 | 386 | 0 | - | - |
| $y_{3 t}$ |  | 73 | 245 | 3 | 3 | 0 | 209 | 0 | 93 | 0 |

Reaktionsmöglichkeiten auf einen Anstieg der Primärbedarfsmenge $d_{11}$ für Produkt 1 in Periode 1:

Anstieg $>226: d_{11}>344$ Keine zulässige Lösung!