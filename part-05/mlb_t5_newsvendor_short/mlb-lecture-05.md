# Einmalige Entscheidungen über die Höhe des Lagerbestands: Das Newsvendor-ProblemWelcher Vorrat $x$ soll angelegt werden, um eine einmalige Bedarfsmenge $Y$ zu erfüllen?

Legt man sich zuviel Vorrat an, dann fallen Overage-Kosten an:
$\Longrightarrow c_{O}$ Geldeinheiten pro Mengeneinheit
Legt man sich zu wenig Vorrat an, dann fallen Underage-Kosten an:
$\Longrightarrow c_{U}$ Geldeinheiten pro Mengeneinheit
Zielfunktion: Minimiere die Summe $Z(x)$ der erwarteten Kosten!
Minimiere $Z(x)=c_{U} \cdot \mathrm{E}\{\max \{Y-x, 0\}\}+c_{O} \cdot \mathrm{E}\{\max \{x-Y, 0\}\}$Welcher Vorrat $x$ soll angelegt werden, um eine einmalige Bedarfsmenge $Y$ zu erfüllen?

Legt man sich zuviel Vorrat an, dann fallen Overage-Kosten an:
$\Longrightarrow c_{O}$ Geldeinheiten pro Mengeneinheit
Legt man sich zu wenig Vorrat an, dann fallen Underage-Kosten an:
$\Longrightarrow c_{U}$ Geldeinheiten pro Mengeneinheit
Zielfunktion: Minimiere die Summe $Z(x)$ der erwarteten Kosten!
Minimiere $Z(x)=c_{U} \cdot \mathrm{E}\left\{[Y-x]^{+}\right\}+c_{O} \cdot \mathrm{E}\left\{[x-Y]^{+}\right\}$Minimiere $Z(x)=c_{U} \cdot \mathrm{E}\left\{[Y-x]^{+}\right\}+c_{O} \cdot \mathrm{E}\left\{[x-Y]^{+}\right\}$
$Z(x)=c_{U} \cdot \int_{x}^{\infty}(y-x) \cdot f_{Y}(y) \mathrm{d} y+c_{O} \cdot \int_{0}^{x}(x-y) \cdot f_{Y}(y) \mathrm{d} y$
$=c_{U} \cdot\left(\int_{0}^{\infty}(y-x) \cdot f_{Y}(y) \mathrm{d} y-\int_{0}^{x}(y-x) \cdot f_{Y}(y) \mathrm{d} y\right)+c_{O} \cdot \int_{0}^{x}(x-y) \cdot f_{Y}(y) \mathrm{d} y$
$=c_{U} \cdot \int_{0}^{\infty}(y-x) \cdot f_{Y}(y) \mathrm{d} y+\left(c_{O}+c_{U}\right) \cdot \int_{0}^{x}(x-y) \cdot f_{Y}(y) \mathrm{d} y$
$=c_{U} \cdot\left(\int_{0}^{\infty} y \cdot f_{Y}(y) \mathrm{d} y-\int_{0}^{\infty} x \cdot f_{Y}(y) \mathrm{d} y\right)+\left(c_{O}+c_{U}\right) \cdot \int_{0}^{x}(x-y) \cdot f_{Y}(y) \mathrm{d} y$
$=c_{U} \cdot\left(\mathrm{E}\{Y\}-x \cdot \int_{0}^{\infty} f_{Y}(y) \mathrm{d} y\right)+\left(c_{O}+c_{U}\right) \cdot \int_{0}^{x}(x-y) \cdot f_{Y}(y) \mathrm{d} y$
$=c_{U} \cdot(\mathrm{E}\{Y\}-x)+\left(c_{O}+c_{U}\right) \cdot \int_{0}^{x}(x-y) \cdot f_{Y}(y) \mathrm{d} y$# Das Newsvendor-Problem: Zielfunktion 

$Z(x)=c_{U} \cdot(\mathrm{E}\{Y\}-x)+\left(c_{O}+c_{U}\right) \cdot \int_{0}^{x}(x-y) \cdot f_{Y}(y) \mathrm{d} y$
$\frac{\mathrm{d} Z(x)}{\mathrm{d} x}=-c_{U}+\left(c_{O}+c_{U}\right) \cdot F_{Y}(x)=0 \Longleftrightarrow x=x_{\text {opt }}$
Optimalitätsbedingung:
$F_{Y}\left(x_{\text {opt }}\right)=\frac{c_{U}}{c_{O}+c_{U}}=\text { „Critical Ratio" }$
Optimale Höhe des Vorrats $x$ :
$x_{\text {opt }}=F_{Y}^{-1}\left(\frac{c_{U}}{c_{O}+c_{U}}\right)$
Konvexität:
$\left(\frac{\mathrm{d} Z(x)}{\mathrm{d} x}\right)^{\prime}=\left(c_{O}+c_{U}\right) \cdot f_{Y}(x)>0$# Beispiel Fußball-Weltmeisterschaft 2014 

- Nachfragemenge $Y$ ist normalverteilt
- Erwartete Nachfragemenge: 50 Mengeneinheiten
- Standardabweichung: 50 Mengeneinheiten
- Underage Costs: $69.95-42.00=27.95$ Geldeinheiten
- Overage Costs: $42.00-19.99=22.01$ Geldeinheiten

Critical Ratio $=\frac{27.95}{22.01+27.95}=0.559447558$
Optimaler Vorrat (Ziellagerbestand): $x_{\text {opt }}=57.47843628 \approx 58$
Sicherheitsbestand $=58-50=8$
$\alpha$-Servicegrad $=1-\mathrm{P}[Y>58]=\mathrm{P}[Y \leq 58]=0.56355946=56.356 \%$# Mehrperiodige Entscheidungen über die Höhe des Lagerbestands: Lagerhaltungspolitiken# (r, s, q)-Lagerhaltungspolitik

!![img-0.jpeg](img-0.jpeg)

*Lagerhaltungspolitik*

*Lageratursystem*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

*Verwaltungspolitik*

# (r, S)-Lagerhaltungspolitik

![img-1.jpeg](img-1.jpeg)

*Lagerhaltungspolitik*

*Univ.-Prof. Dr. Michael Manitz*

*Material-Logistik: Bestandsmanagement*

*110*# Lagerhaltungspolitiken/Bestellstrategien 

## $=(\mathrm{r}, \mathrm{s}, \mathrm{q})$-Politik

Überwache den Lagerbestand alle $r$ Perioden und löse eine Bestellung mit der Bestellmenge $q$ aus, wenn der disponible Lagerbestand den Melde-/Restbestand („Bestellpunkt") erreicht oder unterschritten hat! $\Longrightarrow$ Regelfall: $(r=1, s, q)$-Politik, z. B. tägliche Bestandsüberwachung

## $=(\mathrm{r}, \mathrm{S})$-Politik

Überwache den Lagerbestand alle $r$ Perioden und löse eine Bestellung aus, die ausreicht, den disponiblen Lagerbestand auf ein maximales Niveau („Bestellniveau") anzuheben!

## $=(\mathrm{r}, \mathrm{s}, \mathrm{S})$-Politik

Überwache den Lagerbestand alle $r$ Perioden und löse - wenn der disponible Lagerbestand den Melde-/Restbestand („Bestellpunkt") erreicht oder unterschritten hat - eine Bestellung aus, die ausreicht, den disponiblen Lagerbestand auf ein maximales Niveau („Bestellniveau") anzuheben!
$\Longrightarrow$ Spezialfall: $(r=1, S-1, S)$-Politik (= „Base-Stock-Politik")Minimiere (für ein gegebenes $q$ bzw. $r$ ) die Bestandsgrößen $s$ bzw. $S$
unter Beachtung einer der folgenden Restriktionen:
$P\left[\begin{array}{l}\text { Fehlmenge in bezug auf die Nach- } \\ \text { fragemenge } Y \text { im Risikozeitraum }\end{array}\right] \leq 1-\alpha$
$E\left\{\begin{array}{l}\text { Fehlmenge in bezug auf die Nach- } \\ \text { fragemenge } Y \text { im Risikozeitraum }\end{array}\right\} \leq(1-\beta) \cdot E\left\{\begin{array}{l}\text { Nachfragemenge } \\ \text { im Bestellzyklus }\end{array}\right\}$
$E\left\{\begin{array}{l}\text { periodenbezogene Fehlbestände im } \\ \text { Bestellzyklus }\end{array}\right\} \leq(1-\gamma) \cdot E\left\{\begin{array}{l}\text { Nachfragemenge } \\ \text { im Bestellzyklus }\end{array}\right\}$
$E\left\{\begin{array}{l}\text { Reichweite des Anfangsbestands } \\ \text { im Vergleich zur Nachfragemen- } \\ \text { ge } Y \text { im Risikozeitraum }\end{array}\end{array}\right\} \geq$ VorgabewertMinimiere (für ein gegebenes $q$ bzw. $r$ ) die Bestandsgrößen $s$ bzw. $S$
unter Beachtung einer der folgenden Restriktionen:
$P\left[\begin{array}{l}\text { Fehlmenge in bezug auf die Nach- } \\ \text { fragemenge } Y \text { im Risikozeitraum }\end{array}\right] \leq 1-\alpha$
$E\left\{\begin{array}{l}\text { Fehlmenge in bezug auf die Nach- } \\ \text { fragemenge } Y \text { im Risikozeitraum }\end{array}\right\} \leq(1-\beta) \cdot E\left\{\begin{array}{l}\text { Nachfragemenge } \\ \text { im Bestellzyklus }\end{array}\right\}$
$E\left\{\begin{array}{l}\text { periodenbezogene Fehlbestände im } \\ \text { Bestellzyklus }\end{array}\right\} \leq(1-\gamma) \cdot E\left\{\begin{array}{l}\text { Nachfragemenge } \\ \text { im Bestellzyklus }\end{array}\right\}$
$P\left[\begin{array}{l}\text { Reichweite des Anfangsbestands } \\ \text { im Vergleich zur Nachfragemen- } \geq \text { Vorgabe }\end{array}\right] \geq$ Vorgabewert
ge $Y$ im Risikozeitraum
$P\left[\begin{array}{l}\text { lagerbedingte Lieferzeit der Nach- } \\ \text { fragemenge } Y \text { im Risikozeitraum }\end{array} \leq\right.$ Vorgabe $] \geq$ Vorgabewert# Analyse von ausgewählten Lagerhaltungspolitiken# $(r=1, s, q)$-Lagerhaltungspolitik# Nachfrage-/Bedarfsmenge im Risikozeitraum bei einer 

$$
(r=1, s, q)-\text { Politik }
$$$Y=$ Summe von $L$ Periodennachfragemengen $D+$ Defizit/Undershoot $U$ $(r=1, s, q)$-Politik, $L=\ell$, diskret-verteilte Nachfrage-/Bedarfsmengen
Risikozeitraum $=\ell$ Tage Wiederbeschaffungszeit ( +1 Tag Defizit)

- $Y=\sum_{i=1}^{\ell} D+U=Y^{(\ell)}+U$
- $\mathrm{P}\left[Y^{(\ell)}=y\right]=\mathrm{P}\left[\sum_{i=1}^{\ell} D=y\right] \Longrightarrow \ell$-fache Faltung der Verteilung von $D$
$(r=1, s, q)$-Politik, $L=\ell$, kontinuierlich-verteilte Nachfrage-/Bedarfsmengen
Risikozeitraum $=\ell$ Tage Wiederbeschaffungszeit ( +1 Tag Defizit)
- $Y=\sum_{i=1}^{\ell} D+U=Y^{(\ell)}+U$
- $f_{Y^{(\ell)}}(y)=f_{\sum_{i=1}^{\ell} D}(y) \Longrightarrow \ell$-fache Faltung der Verteilung von $D$# Das mögliche Defizit (,,Undershoot") bei bestandsorientierter DispositionDefizit $U$ (Undershoot) (wenn die Nachfragemenge $D$ diskret ist)

$$
\begin{aligned}
& \mathrm{P}[\text { Bestellung }]=\frac{1}{q} \cdot \sum_{x=1}^{q} \mathrm{P}[D \geq x] \\
& \mathrm{P}[U=u] \approx \lim _{q \rightarrow \infty} \frac{\sum_{x=1}^{q} \mathrm{P}[D=x+u]}{\sum_{x=1}^{q} \mathrm{P}[D \geq x]}=\frac{\mathrm{P}[D>u]}{\mathrm{E}\{D\}} \quad(u=0,1,2, \ldots)
\end{aligned}
$$

Defizit $U$ (Undershoot) (wenn die Nachfragemenge $D$ kontinuierlich ist)

$$
\begin{aligned}
& \mathrm{E}\{U\}=\frac{\mathrm{E}\{D\}^{2}+\operatorname{Var}\{D\}}{2 \cdot \mathrm{E}\{D\}} \\
& \operatorname{Var}\{U\}=\frac{\mathrm{E}\left\{(D-\mathrm{E}\{D\})^{3}\right\}}{3 \cdot \mathrm{E}\{D\}}+\frac{\operatorname{Var}\{D\}}{2} \cdot\left(1-\frac{\operatorname{Var}\{D\}}{2 \cdot \mathrm{E}\{D\}^{2}}\right)+\frac{\mathrm{E}\{D\}^{2}}{12}
\end{aligned}
$$# Defizit $U$ (Undershoot) 

$$
\begin{aligned}
& \mathrm{E}\{U\}=\frac{\mathrm{E}\{D\}^{2}+\operatorname{Var}\{D\}}{2 \cdot \mathrm{E}\{D\}} \\
& \operatorname{Var}\{U\}=\frac{\mathrm{E}\left\{(D-\mathrm{E}\{D\})^{3}\right\}}{3 \cdot \mathrm{E}\{D\}}+\frac{\operatorname{Var}\{D\}}{2} \cdot\left(1-\frac{\operatorname{Var}\{D\}}{2 \cdot \mathrm{E}\{D\}^{2}}\right)+\frac{\mathrm{E}\{D\}^{2}}{12}
\end{aligned}
$$

Es wird üblicherweise angenommen, dass

$$
\begin{aligned}
& \mathrm{E}\{Y\}=\mathrm{E}\left\{Y^{(\ell)}\right\}+\mathrm{E}\{U\} \\
& \operatorname{Var}\{Y\}=\operatorname{Var}\left\{Y^{(\ell)}\right\}+\operatorname{Var}\{U\}
\end{aligned}
$$# Spezialfall: Normalverteilte Nachfrage-/Bedarfsmengen und Defizit bei einer $(r=1, s, q)$-Politik$D$ sei normalverteilt mit den Parametern $\left(\mu_{D}, \sigma_{D}\right)$, zumindest aber die Summe $Y^{(\ell)}$ von ausreichend vielen aufeinanderfolgenden, beliebig verteilten, täglichen Nachfrage-/Bedarfsmengen $D$ mit $\mathrm{E}\{D\}=\mu_{D}$ und $\operatorname{Var}\{D\}=\sigma_{D}^{2}$.

Dann ist:

$$
\begin{aligned}
& Y^{(\ell)}=D+D+\cdots D=\sum_{i=1}^{\ell} D \quad \sim \text { normalverteilt mit }\left(\mu_{Y^{(\ell)}}, \sigma_{Y^{(\ell)}}\right) \\
& \mathrm{E}\left\{Y^{(\ell)}\right\}=\ell \cdot \mathrm{E}\{D\}=\ell \cdot \mu_{D}=\mu_{Y^{(\ell)}} \\
& \operatorname{Var}\left\{Y^{(\ell)}\right\}=\ell \cdot \operatorname{Var}\{D\}=\ell \cdot \sigma_{D}^{2}=\sigma_{Y^{(\ell)}}^{2} \Longleftrightarrow \sigma_{Y^{(\ell)}}=\sqrt{\ell} \cdot \sigma_{D}
\end{aligned}
$$

Dann wird üblicherweise angenommen, dass bei bestandsabhängiger Disposition auch die Nachfrage-/Bedarfsmenge im Risikozeitraum, $Y=Y^{(\ell)}+U$, normalverteilt ist mit $\mu_{Y}=\mathrm{E}\{Y\} \approx \mathrm{E}\left\{Y^{(\ell)}\right\}+\mathrm{E}\{U\}$ und $\sigma_{Y}^{2}=\operatorname{Var}\{Y\} \approx \operatorname{Var}\left\{Y^{(\ell)}\right\}+\operatorname{Var}\{U\}$.# Die $\beta$-Servicegradrestriktion bei einer $(r=1, s, q)$-Politik# Fehlmengenerwartungswert und $\beta$-Servicegrad 

Tatsächlich erreichter zyklusbezogener $\beta$-Servicegrad:

$$
\beta=1-\frac{\mathrm{E}\left\{B_{Y}(s)\right\}}{q}
$$

Fehlbestand am Ende eines Bestellzyklus:

$$
\mathrm{E}\{\max \{Y-s, 0\}\}=: \mathrm{E}\left\{[Y-s]^{+}\right\}=: G_{Y}^{(1)}(s)
$$

Fehlbestand am Anfang eines Bestellzyklus:

$$
\mathrm{E}\{\max \{Y-(s+q), 0\}\}=: \mathrm{E}\left\{[Y-(s+q)]^{+}\right\}=: G_{Y}^{(1)}(s+q)
$$

Zyklusbezogene Fehlmenge:

$$
\mathrm{E}\left\{B_{Y}(s)\right\}=G_{Y}^{(1)}(s)-G_{Y}^{(1)}(s+q)
$$

Zyklusbezogene $\beta$-Servicegradrestriktion (mit Vorgabewert $\widehat{\beta}$ ):

$$
\beta=1-\frac{\mathrm{E}\left\{B_{Y}(s)\right\}}{q} \stackrel{!}{\geq} \widehat{\beta} \Longleftrightarrow \mathrm{E}\left\{B_{Y}(s)\right\} \stackrel{!}{\leq}(1-\widehat{\beta}) \cdot q
$$Zyklusbezogene $\beta$-Servicegradrestriktion (mit Vorgabewert $\widehat{\beta}$ ):

$$
\beta=1-\frac{\mathrm{E}\left\{B_{Y}(s)\right\}}{q} \stackrel{!}{=} \widehat{\beta} \Longleftrightarrow \mathrm{E}\left\{B_{Y}(s)\right\} \stackrel{!}{\leq}(1-\widehat{\beta}) \cdot q
$$

Optimaler Bestellpunkt:

$$
s_{\mathrm{opt}}=\min \left\{s \mid \mathrm{E}\left\{B_{Y}(s)\right\} \leq(1-\widehat{\beta}) \cdot q\right\}
$$

Standardisierung (bei normalverteilten Nachfrage-/Bedarfsmengen):

$$
\begin{aligned}
& \mathrm{E}\left\{B_{Y}(s)\right\}=\sigma_{Y} \cdot \mathrm{E}\left\{B_{Z}(v)\right\} \Longleftrightarrow \mathrm{E}\left\{B_{Z}(v)\right\}=\frac{1}{\sigma_{Y}} \cdot \mathrm{E}\left\{B_{Y}(s)\right\} \text { mit } Z=\frac{Y-\mu_{Y}}{\sigma_{Y}} \\
& \mathrm{E}\left\{B_{Z}(v)\right\}:=\mathrm{E}\{\max \{Z-v, 0\}\}=: \mathrm{E}\left\{[Z-v]^{+}\right\}=: G_{Z}^{(1)}(v)=G_{Z}^{(1)}\left(\frac{s-\mu_{Y}}{\sigma_{Y}}\right) \\
& \text { mit } v=\frac{s-\mu_{Y}}{\sigma_{Y}}
\end{aligned}
$$Zyklusbezogene $\beta$-Servicegradrestriktion (mit Vorgabewert $\widehat{\beta}$ ):

$$
\beta=1-\frac{\mathrm{E}\left\{B_{Y}(s)\right\}}{q} \stackrel{!}{\geq} \widehat{\beta} \Longleftrightarrow \mathrm{E}\left\{B_{Y}(s)\right\} \stackrel{!}{\leq}(1-\widehat{\beta}) \cdot q
$$

Optimaler Bestellpunkt:

$$
s_{\mathrm{opt}}=\min \left\{s \mid \mathrm{E}\left\{B_{Y}(s)\right\} \leq(1-\widehat{\beta}) \cdot q\right\}
$$

Zyklusbezogene $\beta$-Servicegradrestriktion (standardisiert):

$$
\beta=1-\frac{\mathrm{E}\left\{B_{Y}(s)\right\}}{q} \stackrel{!}{\geq} \widehat{\beta} \Longleftrightarrow \frac{\mathrm{E}\left\{B_{Y}(s)\right\}}{\sigma_{Y}}=\mathrm{E}\left\{B_{Z}(v)\right\} \leq \frac{(1-\widehat{\beta}) \cdot q}{\sigma_{Y}}
$$

Optimaler (standardisierter) Bestellpunkt:

$$
v_{\mathrm{opt}}=\min \left\{v \mid \mathrm{E}\left\{B_{Z}(v)\right\} \leq \frac{(1-\widehat{\beta}) \cdot q}{\sigma_{Y}}\right\} \text { mit } v=\frac{s-\mu_{Y}}{\sigma_{Y}}
$$

Optimaler Bestellpunkt:

$$
s_{\mathrm{opt}}=v_{\mathrm{opt}} \cdot \sigma_{Y}+\mu_{Y}
$$# Vorgehen bei normalverteilten Bedarfsmengen 

Zusammenhang:
$Y \sim \mathrm{~N}\left(\mu_{Y}, \sigma_{Y}\right)$
Standardisierung
$Z=\frac{Y-\mu_{Y}}{\sigma_{Y}} \sim \mathrm{~N}(0,1)$
standardisierte Fehlmenge: $\mathrm{E}\left\{B_{Z}(v)\right\}=\int_{v}^{\infty}(z-v) \cdot f_{Z}(z) \mathrm{d} x$
Optimierung $\Downarrow$
$s_{\text {opt }}=v_{\text {opt }} \cdot \sigma_{Y}+\mu_{Y} \quad \stackrel{\text { Rückstandardisierung }}{\Longleftarrow} \quad v_{\text {opt }}=\min \left\{v \mid \mathrm{E}\left\{B_{Z}(v)\right\} \leq \frac{(1-\beta) \cdot q}{\sigma_{Y}}\right\}$
Für normalverteilte Nachfrage-/Bedarfsmengen kann man eine Beziehung zwischen der Verlustfunktion erster Ordnung und ihrer Inversen analytisch formulieren (vgl. Tijms (1994)):

$$
G_{Z}^{(1)}(v)=\mathrm{E}\left\{B_{Z}(v)\right\}=\int_{v}^{\infty}(z-v) \cdot \phi(z) \mathrm{d} z \approx \phi(v)-v \cdot(1-\Phi(v))
$$# Beispiel $(s, q)$-Lagerhaltungspolitik 

Die tägliche Nachfragemenge $D$ nach der Tiefkühl-Pizza „Salami" in einem Supermarkt ist mit dem Mittelwert $\mu_{D}=50$ und der Standardabweichung $\sigma_{D}=8$ normalverteilt. Die fixen Bestellkosten betragen 80 GE. Der Lagerkostensatz beträgt 0.05 .

Wie hoch ist der optimale Bestellpunkt in einer $(s, q)$-Politik, wenn bei einer Wiederbeschaffungszeit $L$ von 4 Tagen der erwartete Fehlbestand am Ende eines Bestellzyklus 1\% der durchschnittlichen Nachfrage in einem Bestellzyklus nicht überschreiten darf?

- Optimale Bestellmenge: $q_{\text {opt }}=\sqrt{\frac{2 \cdot \mu_{D} \cdot s}{h}}=\sqrt{\frac{2 \cdot 50 \cdot 80}{0.05}}=400$Beispiel $(s, q=400)$-Politik: $D \sim N\left(\mu_{D}=50, \sigma_{D}=8\right), \beta \geq 0.99, L=4, r=1$
Nachfragemenge im Risikozeitraum ( $=$ Wiederbeschaffungszeit $\ell=4$ ):

$$
\mu_{Y(\ell)}=4 \cdot 50=200, \sigma_{Y(\ell)}=\sqrt{4 \cdot 8^{2}}=2 \cdot 8=16
$$

Berücksichtigung des Defizits:

$$
\begin{aligned}
& \mu_{Y}=\mu_{Y(\ell)}+\mathrm{E}\{U\}=200+\frac{50^{2}+8^{2}}{2 \cdot 50}=200+25.64=225.64 \\
& \sigma_{Y}^{2}=\sigma_{Y(\ell)}^{2}+\operatorname{Var}\{U\}=16^{2}+\frac{8^{2}}{2} \cdot\left(1-\frac{8^{2}}{2 \cdot 50^{2}}\right)+\frac{50^{2}}{12}=256+239.924=495.924
\end{aligned}
$$

Erwarteter Fehlbestand am Ende des Bestellzyklus:

$$
\mathrm{E}\{\max \{Y-s, 0\}\}=G_{Y}^{(1)}(s) \Longleftrightarrow \sigma_{Y} \cdot G_{Z}^{(1)}(v)=\sigma_{Y} \cdot G_{Z}^{(1)}\left(\frac{s-\mu_{Y}}{\sigma_{Y}}\right)
$$

Erwarteter Fehlbestand am Anfang des Bestellzyklus:

$$
\begin{aligned}
& \mathrm{E}\{\max \{Y-(s+q), 0\}\}=G_{Y}^{(1)}(s+q) \Longleftrightarrow \sigma_{Y} \cdot G_{Z}^{(1)}(v)=\sigma_{Y} \cdot G_{Z}^{(1)}\left(\frac{s+q-\mu_{Y}}{\sigma_{Y}}\right) \\
& G_{Z}^{(1)}\left(\frac{s+q-\mu_{Y}}{\sigma_{Y}}\right)=G_{Z}^{(1)}\left(\frac{s+400-225.64}{22.2693}\right)=G_{Z}^{(1)}\left(\frac{s}{22.2693}+7.82961\right) \approx 0
\end{aligned}
$$Beispiel $(s, q=400)$-Politik: $D \sim N\left(\mu_{D}=50, \sigma_{D}=8\right), \beta \geq 0.99, L=4, r=1$
Nachfragemenge im Risikozeitraum ( $=$ Wiederbeschaffungszeit $\ell=4$ ):

$$
\mu_{Y(\ell)}=4 \cdot 50=200, \sigma_{Y(\ell)}=\sqrt{4 \cdot 8^{2}}=2 \cdot 8=16
$$

Berücksichtigung des Defizits:

$$
\begin{aligned}
& \mu_{Y}=\mu_{Y(\ell)}+\mathrm{E}\{U\}=200+\frac{50^{2}+8^{2}}{2 \cdot 50}=200+25.64=225.64 \\
& \sigma_{Y}^{2}=\sigma_{Y(\ell)}^{2}+\operatorname{Var}\{U\}=16^{2}+\frac{8^{2}}{2} \cdot\left(1-\frac{8^{2}}{2 \cdot 50^{2}}\right)+\frac{50^{2}}{12}=256+239.924=495.924
\end{aligned}
$$

Fehlmengenrestriktion:

$$
\mathrm{E}\left\{B_{Z}(v)\right\}=\sigma_{Y} \cdot G_{Z}^{(1)}\left(\frac{s-\mu_{Y}}{\sigma_{Y}}\right) \leq 0.01 \cdot q \Longleftrightarrow G_{Z}^{(1)}\left(\frac{s-\mu_{Y}}{\sigma_{Y}}\right) \leq 0.179619
$$

Optimaler (standardisierter) Bestellpunkt:

$$
v_{\text {opt }}=\min \{v \mid \phi(v)-v \cdot(1-\Phi(v)) \leq 0.179619\}=0.31555
$$

Optimaler Bestellpunkt:

$$
s_{\text {opt }}=v_{\text {opt }} \cdot \sigma_{Y}+\mu_{Y}=0.31555 \cdot 22.2693+225.64=232.667 \Longrightarrow \mathrm{SB}=7.02708
$$# $(r, s)$-Lagerhaltungspolitik# Nachfrage-/Bedarfsmenge im Risikozeitraum bei einer $(r, s)$-Politik$Y=$ Summe von $r+L$ Periodennachfragemengen $D$
$(r, S)$-Politik, $L=\ell$, diskret-verteilte Nachfrage-/Bedarfsmengen
Risikozeitraum $=r+\ell$ Tage Wiederbeschaffungszeit

- $Y=\sum_{i=1}^{r+\ell} D=Y^{(r+\ell)}$
- $\mathrm{P}\left[Y^{(r+\ell)}=y\right]=\mathrm{P}\left[\sum_{i=1}^{r+\ell} D=y\right] \Longrightarrow(r+\ell)$-fache Faltung der Verteilung von $D$
$(r, S)$-Politik, $L=\ell$, kontinuierlich-verteilte Nachfrage-/Bedarfsmengen
- Risikozeitraum $=r+\ell$ Tage Wiederbeschaffungszeit
- $Y=\sum_{i=1}^{r+\ell} D=Y^{(r+\ell)}$
- $f_{Y^{(r+\ell)}}(y)=f_{\sum_{i=1}^{r+\ell} D}(y) \Longrightarrow(r+\ell)$-fache Faltung der Verteilung von $D$# Normalverteilte Nachfrage-/Bedarfsmengen bei einer $(r, s)$-Politik# Spezialfall: Normalverteilte Nachfrage-/Bedarfsmengen 

$D$ sei normalverteilt mit den Parametern $\left(\mu_{D}, \sigma_{D}\right)$, zumindest aber die Summe $Y^{(r+\ell)}$ von ausreichend vielen aufeinanderfolgenden, beliebig verteilten, täglichen Nachfrage-/Bedarfsmengen $D$ mit $\mathrm{E}\{D\}=\mu_{D}$ und $\operatorname{Var}\{D\}=\sigma_{D}^{2}$.

Dann ist:

$$
\begin{aligned}
& Y^{(r+\ell)}=D+D+\cdots D=\sum_{i=1}^{r+\ell} D \quad \sim \text { normalverteilt mit }\left(\mu_{Y^{(r+\ell)}}, \sigma_{Y^{(r+\ell)}}\right) \\
& \mathrm{E}\left\{Y^{(r+\ell)}\right\}=(r+\ell) \cdot \mathrm{E}\{D\}=(r+\ell) \cdot \mu_{D}=\mu_{Y^{(r+\ell)}} \\
& \operatorname{Var}\left\{Y^{(r+\ell)}\right\}=(r+\ell) \cdot \operatorname{Var}\{D\}=(r+\ell) \cdot \sigma_{D}^{2}=\sigma_{Y^{(r+\ell)}}^{2} \\
& \sigma_{Y^{(r+\ell)}}=\sqrt{r+\ell} \cdot \sigma_{D}
\end{aligned}
$$# Die $\beta$-Servicegradrestriktion bei einer $(r, S)$-Politik# Fehlmengenerwartungswert und $\beta$-Servicegrad 

Tatsächlich erreichter zyklusbezogener $\beta$-Servicegrad:

$$
\beta=1-\frac{\mathrm{E}\left\{B_{Y}(S)\right\}}{r \cdot \mathrm{E}\{D\}}
$$

Fehlbestand am Ende eines Bestellzyklus:

$$
\mathrm{E}\left\{\max \left\{Y^{(r+\ell)}-S, 0\right\}\right\}=: \mathrm{E}\left\{\left[Y^{(r+\ell)}-S\right]^{+}\right\}=: G_{Y}^{(1)}(S)
$$

Fehlbestand am Anfang eines Bestellzyklus:

$$
\mathrm{E}\left\{\max \left\{Y^{(\ell)}-S, 0\right\}\right\}=: \mathrm{E}\left\{\left[Y^{(\ell)}-S\right]^{+}\right\}=: G_{Y^{(\ell)}}^{(1)}(S)
$$

Zyklusbezogene Fehlmenge:

$$
\mathrm{E}\left\{B_{Y}(S)\right\}=G_{Y}^{(1)}(S)-G_{Y^{(\ell)}}^{(1)}(S)
$$

Zyklusbezogene $\beta$-Servicegradrestriktion (mit Vorgabewert $\widehat{\beta}$ ):

$$
\beta=1-\frac{\mathrm{E}\left\{B_{Y}(S)\right\}}{r \cdot \mathrm{E}\{D\}} \stackrel{!}{\geq} \widehat{\beta} \Longleftrightarrow \mathrm{E}\left\{B_{Y}(S)\right\} \stackrel{!}{\leq}(1-\widehat{\beta}) \cdot r \cdot \mathrm{E}\{D\}
$$Zyklusbezogene $\beta$-Servicegradrestriktion (mit Vorgabewert $\widehat{\beta}$ ):

$$
\beta=1-\frac{\mathrm{E}\left\{B_{Y}(S)\right\}}{r \cdot \mathrm{E}\{D\}} \stackrel{!}{=} \widehat{\beta} \Longleftrightarrow \mathrm{E}\left\{B_{Y}(S)\right\} \stackrel{!}{\leq}(1-\widehat{\beta}) \cdot r \cdot \mathrm{E}\{D\}
$$

Optimales Bestellniveau:

$$
S_{\mathrm{opt}}=\min \left\{S \mid \mathrm{E}\left\{B_{Y}(S)\right\} \leq(1-\widehat{\beta}) \cdot r \cdot \mathrm{E}\{D\}\right\}
$$

Standardisierung (bei normalverteilten Nachfrage-/Bedarfsmengen):

$$
\begin{aligned}
& \mathrm{E}\left\{B_{Y}(S)\right\}=\sigma_{Y} \cdot \mathrm{E}\left\{B_{Z}(v)\right\} \Longleftrightarrow \mathrm{E}\left\{B_{Z}(v)\right\}=\frac{1}{\sigma_{Y}} \cdot \mathrm{E}\left\{B_{Y}(S)\right\} \text { mit } Z=\frac{Y-\mu_{Y}}{\sigma_{Y}} \\
& \mathrm{E}\left\{B_{Z}(v)\right\}:=\mathrm{E}\{\max \{Z-v, 0\}\}=: \mathrm{E}\left\{[Z-v]^{+}\right\}=: G_{Z}^{(1)}(v)=G_{Z}^{(1)}\left(\frac{S-\mu_{Y}}{\sigma_{Y}}\right) \\
& \text { mit } v=\frac{S-\mu_{Y}}{\sigma_{Y}}
\end{aligned}
$$Zyklusbezogene $\beta$-Servicegradrestriktion (mit Vorgabewert $\widehat{\beta}$ ):

$$
\beta=1-\frac{\mathrm{E}\left\{B_{Y}(S)\right\}}{r \cdot \mathrm{E}\{D\}} \stackrel{!}{=} \widehat{\beta} \Longleftrightarrow \mathrm{E}\left\{B_{Y}(S)\right\} \stackrel{!}{\leq}(1-\widehat{\beta}) \cdot r \cdot \mathrm{E}\{D\}
$$

Optimales Bestellniveau:

$$
S_{\mathrm{opt}}=\min \left\{S \mid \mathrm{E}\left\{B_{Y}(S)\right\} \leq(1-\widehat{\beta}) \cdot r \cdot \mathrm{E}\{D\}\right\}
$$

Zyklusbezogene $\beta$-Servicegradrestriktion (standardisiert):

$$
\beta=1-\frac{\mathrm{E}\left\{B_{Y}(S)\right\}}{r \cdot \mathrm{E}\{D\}} \stackrel{!}{=} \widehat{\beta} \Longleftrightarrow \frac{\mathrm{E}\left\{B_{Y}(S)\right\}}{\sigma_{Y}}=\mathrm{E}\left\{B_{Z}(v)\right\} \stackrel{!}{\leq} \frac{(1-\widehat{\beta}) \cdot r \cdot \mathrm{E}\{D\}}{\sigma_{Y}}
$$

Optimales (standardisiertes) Bestellniveau:

$$
v_{\mathrm{opt}}=\min \left\{v \mid \mathrm{E}\left\{B_{Z}(v)\right\} \leq \frac{(1-\widehat{\beta}) \cdot r \cdot \mathrm{E}\{D\}}{\sigma_{Y}}\right\} \text { mit } v=\frac{S-\mu_{Y}}{\sigma_{Y}}
$$

Optimales Bestellniveau:

$$
S_{\mathrm{opt}}=v_{\mathrm{opt}} \cdot \sigma_{Y}+\mu_{Y}
$$# Vorgehen bei normalverteilten Bedarfsmengen 

Zusammenhang:
$Y \sim \mathrm{~N}\left(\mu_{Y}, \sigma_{Y}\right)$
Standardisierung
$Z=\frac{Y-\mu_{Y}}{\sigma_{Y}} \sim \mathrm{~N}(0,1)$
standardisierte Fehlmenge: $\mathrm{E}\left\{B_{Z}(v)\right\}=\int_{v}^{\infty}(z-v) \cdot f_{Z}(z) \mathrm{d} x$
Optimierung $\Downarrow$
$S_{\text {opt }}=v_{\text {opt }} \cdot \sigma_{Y}+\mu_{Y} \stackrel{\text { Rückstandardisierung }}{\Longleftarrow} v_{\text {opt }}=\min \left\{v \mid \mathrm{E}\left\{B_{Z}(v)\right\} \leq \frac{(1-\beta) \cdot r \cdot \mu_{D}}{\sigma_{Y}}\right\}$
(mit $Y=Y^{(r+\ell)}$ )
Für normalverteilte Nachfrage-/Bedarfsmengen kann man eine Beziehung zwischen der Verlustfunktion erster Ordnung und ihrer Inversen analytisch formulieren (vgl. Tijms (1994)):

$$
G^{(1) Z(v)}=\mathrm{E}\left\{B_{Z}(v)\right\}=\int_{v}^{\infty}(z-v) \cdot \phi(z) \mathrm{d} z=\phi(v)-v \cdot(1-\Phi(v))
$$# Spezialfall: Normalverteilte Nachfrage-/Bedarfsmengen 

Beispiel $(r=1, S)$-Politik
tägliche Nachfragemenge $D$ ist normalverteilt mit $\mu_{D}=10, \sigma_{D}=5$
Servicegradvorgabe: $\beta \stackrel{!}{\geq} 95 \%$
Wiederbeschaffungszeit: $\ell=3$ Tage# Spezialfall: Normalverteilte Nachfrage-/Bedarfsmengen 

Beispiel $(r=1, S)$-Politik: $D \sim N\left(\mu_{D}=10, \sigma_{D}=2\right), \beta \geq 0.95, \ell=3$
Nachfrage-/Bedarfsmenge in der Wiederbeschaffungszeit $(\ell=3)$ :

$$
Y^{(\ell)} \sim N\left(\mu_{Y^{(\ell)}}=10+10+10=30, \sigma_{Y^{(\ell)}}=\sqrt{2^{2}+2^{2}+2^{2}}=3.4641\right)
$$

Nachfrage-/Bedarfsmenge im Risikozeitraum $(=r+\ell=1+3=4)$ :

$$
Y^{(r+\ell)} \sim N\left(\mu_{Y^{(r+\ell)}}=10+10+10+10=40, \sigma_{Y^{(r+\ell)}}=\sqrt{2^{2}+2^{2}+2^{2}+2^{2}}=4\right)
$$

Fehlmengenerwartungswert:

$$
\sigma_{Y^{(r+\ell)}} \cdot G_{Z}^{(1)}\left(\frac{S-\mu_{Y^{(r+\ell)}}}{\sigma_{Y^{(r+\ell)}}}\right)-\sigma_{Y^{(\ell)}} \cdot G_{Z}^{(1)}\left(\frac{S-\mu_{Y^{(\ell)}}}{\sigma_{Y^{(\ell)}}}\right) \leq(1-0.95) \cdot 1 \cdot 10=0.5
$$

Optimales Bestellniveau:

$$
\begin{aligned}
& S_{\text {opt }}=\min \left\{S \mid 4 \cdot G_{Z}^{(1)}\left(\frac{S-40}{4}\right)-3.4641 \cdot G_{Z}^{(1)}\left(\frac{S-30}{3.4641}\right) \leq 0.5\right\} \\
& \Longleftrightarrow \\
& S_{\text {opt }}=\min \{S \mid 0.500063-0.000063=0.500000\}=43.110586
\end{aligned}
$$# Stochastische Wiederbeschaffungszeiten$Y=$ Summe von Periodennachfragemengen $D+$ Defizit/Undershoot $U$
$(r=1, s, q)$-Politik, $L$ stochastisch, diskret-verteilte Nachfrage-/Bedarfsmengen
Risikozeitraum $=L$ Tage Wiederbeschaffungszeit + Defizit

- $Y=Y^{(L)}+U=\sum_{i=1}^{L} D+U$
- $\mathrm{P}\left[Y^{(L)}=y\right]=\sum_{\ell=\ell_{\min }}^{\ell_{\max }} \mathrm{P}\left[\sum_{i=1}^{\ell} D=y\right] \cdot \mathrm{P}[L=\ell]$
$(r, S)$-Politik, $L$ stochastisch, diskret-verteilte Nachfrage-/Bedarfsmengen
- Risikozeitraum $=r+L$ Tage Wiederbeschaffungszeit
- $Y=Y^{(r+L)}=\sum_{i=1}^{r+L} D$
- $\mathrm{P}\left[Y^{(r+L)}=y\right]=\sum_{\ell=\ell_{\min }}^{\ell_{\max }} \mathrm{P}\left[\sum_{i=1}^{r+\ell} D=y\right] \cdot \mathrm{P}[L=\ell]$# Dynamische Entscheidungen über die Höhe des Lagerbestands unter stochastischen Bedingungen# Bestellmengenplanung unter stochastischen Bedingungen 

- „Dynamic uncertainty strategy" (Bookbinder/Tan (1988))
$\triangleright$ dynamische Anpassung der Lagerhaltungspolitiken
$\triangleright$ hohe Planungsnervosität
- „Static-dynamic uncertainty strategy" (Bookbinder/Tan (1988))
$\triangleright$ dynamische Festlegung der Bestellmengen bzw. Losgrößen
$\triangleright$ immer noch (zu) starke Schwankungen der Bestellmengen
- „Static uncertainty strategy" (Bookbinder/Tan (1988))
$\triangleright$ vorab ausreichend dimensionierte Produktions-/Bestellmengen bei vorgegebenem Auflagemuster
$\Longrightarrow$ Die dynamischen Mengenvariationen sind nicht mehr (nur) Reaktion auf vergangene stochastische Bedarfsmengen, sondern beinhalten auch Sicherheitsbestand.

Keine dieser „Strategien" kann knappe Kapazitäten berücksichtigen.