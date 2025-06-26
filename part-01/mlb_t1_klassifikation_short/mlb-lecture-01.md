# Material-Logistik: Bestandsmanagement in Supply Chains 

Univ.-Prof. Dr. Michael Manitz

Tel.: (0203) 379 - 1443
E-Mail: michael.manitz@uni-due.de
Universität Duisburg/Essen
Fakultät für Betriebswirtschaftslehre
(Mercator School of Management)
Lehrstuhl für Betriebswirtschaftslehre, insbesondere
Produktionswirtschaft und Supply Chain Management
Lotharstr. 65
47057 Duisburg
www.scm.msm.uni-due.de# Modul Produktionswirtschaft und Supply Chain Management 

- Einblick in einige wichtige Fragestellungen der Strukturierung und des Betriebs von Produktionssystemen
- Verwendung quantitativer Optimierungsmodelle
- Darstellung der Bedeutung der Berücksichtigung knapper Kapazitäten
- Darstellung tatsächlich existierender, praxisrelevanter Problemstellungen
- Übung an Hand von kleinen Anwendungsbeispielen


## Vorlesung Material-Logistik (Bestandsmanagement in Supply Chains)

- Dynamische Losgrößenplanung und Materialbederfsermittlung (Operative Produktionsplanung)
- Berücksichtigung von Unsicherheit (Sicherheitsbestandsplanung)Günther, H.-O., und H. Tempelmeier, Supply Chain Analytics Operations Management und Logistik ehemals Produktion und Logistik - Supply Chain \& Operations Management (13. Aufl.), Norderstedt (Books on Demand), 2020

Helber, S., Operations Management Tutorial - Grundlagen der Modellierung und Analyse der betrieblichen Wertschöpfung (2. Aufl.), Hildesheim (Stefan Helber), 2020Tempelmeier, H., Material-Logistik (7. Aufl.), Berlin, Heidelberg (Springer), 2008

Tempelmeier, H., Production Analytics - Modelle und Algorithmen zur Produktionsplanung ehemals Produktionsplanung in Supply Chains (6. Aufl.), Norderstedt (Books on Demand), 2020

Tempelmeier, H., Analytics im Bestandsmanagement ehemals Bestandsmanagement in Supply Chains (7. Aufl.), Norderstedt (Books on Demand), 2020

Tempelmeier, H., Analytics in Supply Chain Management und Produktion - Übungen und Mini-Fallstudien (7. Aufl.), Norderstedt (Books on Demand), 2020![img-0.jpeg](img-0.jpeg)

# Material-Logistik: Bestandsmanagement in Supply Chains

## Logistik

### Material-Logistik

- **Materialbeschaffung**
- **Produktionslogistik**
- **Distribution**
- **Bestandsmanagement**
- **Transport- und Tourenplanung**
- **Materialhandhabung und Verpackung**

(vgl. Tempelmeier (2008))

### Gegenstand der Veranstaltung:

- (dynamische) Bestellmengen- bzw. Losgrößenplanung
- Bestandsmanagement (Lagerhaltungsplanung)

### Materialdisposition

Univ.-Prof. Dr. Michael Manitz

Material-Logistik: Bestandsmanagement

4-9![img-1.jpeg](img-1.jpeg)

# Material-Logistik: Bestandsmanagement in Supply Chains

## Logistik

### Material-Logistik

- **Materialbeschaffung**
- **Produktionslogistik**
- **Distribution**
- **Bestandsmanagement**
- **Transport- und Tourenplanung**
- **Materialhandhabung und Verpackung**

(vgl. Tempelmeier (2008))

### "Material" (= Verbrauchsfaktoren)

- **Vorprodukte**
  - Roh-, Hilfs- und Betriebsstoffe
  - bezogene Teile: Einzelteile, Baugruppen
- **Handelswaren**# Material-Logistik: Bestandsmanagement in Supply Chains

![img-2.jpeg](img-2.jpeg)

|  **Prognosen** | **Produktionsplanungs- und -steuerungssystem** | **Hauptproduktionsprogrammplanung** | **Losgrößen- und Ressourceneinsatzplanung** | **Feinplanung und -steuerung**  |
| --- | --- | --- | --- | --- |
|  Baustellenproduktion | Werkstattproduktion | Fließproduktion | Zentrenproduktion | JIT-Produktion  |

(vgl. Drexl/Fleischmann/Günther/Stadtler/Tempelmeier (1993), Tempelmeier (2008))

Univ.-Prof. Dr. Michael Manitz

Material-Logistik: Bestandsmanagement 4-19# Vorlesung Material-Logistik 

- Klassifikation von Verbrauchsfaktoren („Material")
$\triangleright \ldots$ nach ihrer wertmäßigen Bedeutung (ABC-Analyse)
$\triangleright \ldots$ nach ihrem Bedarfsverlauf (Materialbereitstellungprinzipien)
- Materialbedarfsermittlung
$\triangleright$ „Verbrauchsorientierte Materialbedarfsermittlung": Bedarfsprognose
$\triangleright$ „Programmorientierte Materialbedarfsermittlung": Materialbedarfsrechnung
- Bestandsmanagement
$\triangleright \ldots$ unter deterministischen Bedingungen: Dynamische Losgrößenplanung
- einstufige Modelle
- mehrstufige Modelle
$\triangleright \ldots$ unter stochastischen Bedingungen: Sicherheitsbestandsplanung# Klassifikation der 

Verbrauchsfaktoren („Material")
nach ihrer wertmäßigen Bedeutung
(ABC-Analyse)# ABC-Analyse

Klassifikation der zu disponierenden Verbrauchsfaktoren (Materialarten) nach ihrer wertmäßigen Bedeutung

Beispiel ABC-Klassifikation von Erzeugnissen

|  Erzeugnis | Verbrauchswert  |
| --- | --- |
|  1 | 10  |
|  2 | 130  |
|  3 | 5  |
|  4 | 780  |
|  5 | 20  |
|  6 | 30  |
|  7 | 450  |
|  8 | 25  |
|  $#=8$ | $\Sigma=1450$  |

(vgl. Günther und Tempelmeier (2012))# ABC-Analyse

Klassifikation der zu disponierenden Verbrauchsfaktoren (Materialarten) nach ihrer wertmäßigen Bedeutung

Beispiel ABC-Klassifikation von Erzeugnissen

|  Erzeugnis | Verbrauchswert  |
| --- | --- |
|  4 | 780  |
|  7 | 450  |
|  2 | 130  |
|  6 | 30  |
|  8 | 25  |
|  5 | 20  |
|  1 | 10  |
|  3 | 5  |
|  $#=8$ | $\Sigma=1450$  |

(vgl. Günther und Tempelmeier (2012))# ABC-Analyse

Klassifikation der zu disponierenden Verbrauchsfaktoren (Materialarten) nach ihrer wertmäßigen Bedeutung

Beispiel ABC-Klassifikation von Erzeugnissen

|  Erzeugnis | Verbrauchswert | kumulierter Anteil an
der Anzahl Erzeugnisse
$[\%]$ | kumulierter Anteil
am Verbrauchswert
$[\%]$  |
| --- | --- | --- | --- |
|  4 | 780 | 12.5 | 53.79  |
|  7 | 450 | 25.0 | 84.83  |
|  2 | 130 | 37.5 | 93.79  |
|  6 | 30 | 50.0 | 95.86  |
|  8 | 25 | 62.5 | 97.59  |
|  5 | 20 | 75.0 | 98.97  |
|  1 | 10 | 87.5 | 99.66  |
|  3 | 5 | 100.0 | 100.00  |
|  $#=8$ | $\Sigma=1450$ |  |   |

(vgl. Günther und Tempelmeier (2012))# ABC-Analyse

Klassifikation der zu disponierenden Verbrauchsfaktoren (Materialarten) nach ihrer wertmäßigen Bedeutung

![img-3.jpeg](img-3.jpeg)# ABC-Analyse

Klassifikation der zu disponierenden Verbrauchsfaktoren (Materialarten) nach ihrer wertmäßigen Bedeutung

![img-4.jpeg](img-4.jpeg)

|  Beispiel | ABC-Klassifikation von Erzeugnissen  |
| --- | --- |
|  100 | Verbrauchswert, kumuliert (in %)  |
|  90 | Anteil an allen Erzeugnisarten, kumuliert (in %)  |
|  80 | 12.5 / 25.0  |
|  70 | 37.5 / 50.0  |
|  60 | 62.5 / 75.0  |
|  50 | 87.5 / 100.0  |
|  40 | Anteil an allen Erzeugnisarten, kumuliert (in %)  |
|  30 | (vgl. Günther und Tempelmeier (2012))  |

Univ.-Prof. Dr. Michael Manitz Material-Logistik: Bestandsmanagement 7-11# ABC-Analyse

Klassifikation der zu disponierenden Verbrauchsfaktoren (Materialarten) nach ihrer wertmäßigen Bedeutung

![img-5.jpeg](img-5.jpeg)# ABC-Analyse

Klassifikation der zu disponierenden Verbrauchsfaktoren (Materialarten) nach ihrer wertmäßigen Bedeutung

![img-6.jpeg](img-6.jpeg)# ABC-Analyse 

Klassifikation der zu disponierenden Verbrauchsfaktoren (Materialarten) nach ihrer wertmäßigen Bedeutung

Klasseneinteilung:
Gruppe A:
Güter mit hohem Anteil am gesamten Materialverbrauchswert
Gruppe B:
Güter mit mittlerem Anteil am gesamten Materialverbrauchswert
Gruppe C:
Güter mit niedrigem Anteil am gesamten Materialverbrauchswert# Klassifikation der Verbrauchsfaktoren („Material") nach ihrem Bedarfsverlauf (RSU/XYZ-Analyse)![img-7.jpeg](img-7.jpeg)

# Unreaching Bost - Bedarf

![img-8.jpeg](img-8.jpeg)

![img-9.jpeg](img-9.jpeg)

![img-10.jpeg](img-10.jpeg)

![img-11.jpeg](img-11.jpeg)

![img-12.jpeg](img-12.jpeg)

![img-13.jpeg](img-13.jpeg)

![img-14.jpeg](img-14.jpeg)

Univ.-Prof. Dr. Michael Manitz

Material-Logistik: Bestandsmanagement# Anorgadischer Bedarf

![img-15.jpeg](img-15.jpeg)

|  **Bedarf** | **Profil**  |
| --- | --- |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
|  128 | 128  |
# Sporadischer Bedarf (ohne Nullbedarfsperioden)

![img-16.jpeg](img-16.jpeg)

|  0 | 25 | 50 | 75 | 100 | 125 | 150 | 175 | 200 | Zeit  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  0 | 25 | 50 | 75 | 100 | 125 | 150 | 175 | 200 |   |

*Univ.-Prof. Dr. Michael Manitz*

*Material-Logistik: Bestandsmanagement*# Regelmäßiger Bedarf

![img-17.jpeg](img-17.jpeg)

|  **Bedarf** | 0 | 25 | 50 | 75 | 100 | 125 | 150 | 175 | 200  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  0 | 0 | 25 | 50 | 75 | 100 | 125 | 150 | 175 | 200  |

*Univ.-Prof. Dr. Michael Manitz*

*Material-Logistik: Bestandsmanagement*# Regelmäßiger Bedarf mit Trend

![img-18.jpeg](img-18.jpeg)

|  **Bedarf** | **25** | **50** | **75** | **100** | **125** | **150** | **175** | **200** | **Zeit**  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  **0** | 25 | 50 | 75 | 100 | 125 | 150 | 175 | 200 |   |

*Univ.-Prof. Dr. Michael Manitz*

*Material-Logistik: Bestandsmanagement*# **Regelmäßiger Bedarf mit Trend und Saison**

![img-19.jpeg](img-19.jpeg)

|  Jahr | 2000 | 2001 | 2002 | 2003 | 2004 | 2005 | 2006 | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  **Bezirksland** | 125 | 100 | 75 | 50 | 25 | 50 | 75 | 100 | 125 | 150 | 175 | 200 | 25 | 20 | 15 | 10 | 15 | 15 | 15 | 15  |

*Univ.-Prof. Dr. Michael Manitz*

*Material-Logistik: Bestandsmanagement*# Typen von Bedarfsverläufen 

- nichtstationär
- stationär
$\triangleright$ unregelmäßig
- stark schwankend
- sporadisch
$\triangleright$ regelmäßig
- um ein konstantes Niveau
- ohne Saisoneinfluss
- mit Saisoneinfluss
- trendförmig
- ohne Saisoneinfluss
- mit Saisoneinfluss# Mittelwert der Zeitreihe $\left(y_{t}\right)$ der Bedarfsmengen über $T$ Perioden 

$$
\mu=\frac{1}{T} \sum_{t=1}^{T} y_{t}
$$

## mittlere absolute Abweichung

$$
M A D=\frac{1}{T} \sum_{t=1}^{T}\left|y_{t}-\mu\right|
$$

## Störpegel

$$
S P=\frac{M A D}{\mu}
$$

Unregelmäßigen (stark schwankenden) Bedarf vermutet man bei $\mathrm{SP}>0.5$.# Stark schwankender vs. sporadischer Bedarf

Sporadischen Bedarf vermutet man bei einem Anteil Nullbedarfsperioden von größer als 0.3 oder 0.4 .

Beispiel Stark schwankender Bedarf

|  $t$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  $y_{t}$ | 0 | 50 | 390 | 140 | 0 | 20 | 0 | 200 | 750 | 70 | 50 | 1000 | 355 | 0  |# Stark schwankender vs. sporadischer Bedarf

Sporadischen Bedarf vermutet man bei einem Anteil Nullbedarfsperioden von größer als 0.3 oder 0.4 .

Beispiel Stark schwankender Bedarf

|  $t$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  $y_{t}$ | 0 | 50 | 390 | 140 | 0 | 20 | 0 | 200 | 750 | 70 | 50 | 1000 | 355 | 0  |

$S P=1.0782$ Anteil Nullbedarfsperioden $=\frac{4}{14}=0.2857=28.57 \%$# Verlaufsmuster bei regelmäßigen Bedarf 

## Autokorrelationskoeffizient

(bezüglich einer Zeitverschiebung von $\tau$ Perioden)

$$
\rho(\tau)=\frac{\sum_{t=1}^{T-\tau} y_{t} \cdot y_{t+\tau}-\frac{1}{T-\tau} \cdot \sum_{t=1}^{T-\tau} y_{t} \cdot \sum_{t=1+\tau}^{T} y_{t}}{\sqrt{\left(\sum_{t=1}^{T-\tau} y_{t}^{2}-\frac{1}{T-\tau} \cdot\left(\sum_{t=1}^{T-\tau} y_{t}\right)^{2}\right) \cdot\left(\sum_{t=1+\tau}^{T} y_{t}^{2}-\frac{1}{T-\tau} \cdot\left(\sum_{t=1+\tau}^{T} y_{t}\right)^{2}\right)}}
$$# Verlaufsmuster bei regelmäßigen Bedarf

**Autokorrelogramm** für eine Zeitreihe mit saisonalem Verlauf

![img-20.jpeg](img-20.jpeg)

Die Autokorrelationsfunktion $$ \rho(\tau) $$ schwankt um 0, weicht aber in regelmäßigen Abständen systematisch davon ab.# Verlaufsmuster bei regelmäßigen Bedarf

**Autokorrelogramm** für eine Zeitreihe mit trendförmigem Verlauf

![img-21.jpeg](img-21.jpeg)

Die Autokorrelationsfunktion $$ \rho(\tau) $$ verläuft im positiven Bereich, wenngleich fallend, d. h. mit abnehmender Korrelation.# (Grob-)Zuordnung von Materialbereitstellungsprinzipien zum Bedarfsverlaufmuster# RSU-/XYZ-Analyse 

Klassifikation der zu disponierenden Verbrauchsfaktoren (Materialarten) nach ihrem Bedarfsverlauf

Klasseneinteilung:
Gruppe R:
Güter mit gleichbleibendem Bedarf bei nur gelegentlichen Niveauveränderungen (regelmäßiger Bedarf auf hohem Niveau)
Gruppe S:
Güter mit veränderlichem, insb. trendförmigem und/oder saisonalem Bedarf

- Gruppe U:

Güter mit sehr unregelmäßigem, sporadischem Bedarf# Materialbereitstellungsprinzipien 

- einsatzsynchrone Beschaffung
$\Longrightarrow$ Just-in-time-Prinzip (R-Produkte)
$\triangleright$ geringe Lagerkosten
$\triangleright$ ggf. starke Schwankungen der Bestellmengen und des Kapazitätsbedarfs für die Produktion
- Vorratshaltung (S-Produkte)
$\triangleright$ hohe Lagerkosten
$\triangleright$ optimale Bestellmengen und gleichbleibende Kapazitätsauslastung erreichbar
- Einzelbeschaffung im Bedarfsfall (U-Produkte)
$\triangleright$ geringe Lagerkosten
$\triangleright$ u. U. lange DurchlaufzeitenDifferenzierte Zuordnung der Materialbereitstellungsprinzipien:

|   | A | B | C  |
| --- | --- | --- | --- |
|  R | RA | RB | RC  |
|  S | SA | SB | SC  |
|  U | UA | UB | UC  |

bzw.

|   | A | B | C  |
| --- | --- | --- | --- |
|  X | XA | XB | XC  |
|  Y | YA | YB | YC  |
|  Z | ZA | ZB | ZC  |

bzw.

|   | A | B | C  |
| --- | --- | --- | --- |
|  X | AX | BX | CX  |
|  Y | AY | BY | CY  |
|  Z | AZ | BZ | CZ  |# MaterialbedarfsermittlungPrinzipien:

- programmorientiert (Material Requirements Planning - MRP)
- „verbrauchsorientiert" (vergangenheitsbedarfsorientiert)
$\longrightarrow$ Bedarfsprognose
Bedarfsarten:
- Primärbedarf
- Sekundärbedarf
- Tertiärbedarf

Ziel/Planungsaufgabe: (für alle Verbrauchsfaktoren $k$ und Perioden $t$ )
Bestimmung des Materialbedarfs $r_{k t}$
$\triangleright$ in der richtigen Menge: $r_{\text {. }}$.
$\triangleright$ zum richtigen Zeitpunkt: $t$
$\triangleright$ am richtigen Ort: $k$# „Verbrauchsorientierte" bzw. 

vergangenheitsbedarfsorientierte Materialbedarfsermittlung
(Bedarfsprognose)# Bedarfsprognose 

- s. Produktionswirtschaft II (Operative Produktionsplanung und -steuerung)# Programmorientierte Materialbedarfsermittlung (,,Materialbedarfsrechnung")# Materialbedarfsrechnung 

## Informationsquellen (Daten):

## (für alle Verbrauchsfaktoren $k$ )

## Hauptproduktionsprogramm bzw. Primärbedarfsmengen

Primärbedarfsmenge $d_{k}$
unmittelbar absatzbestimmter Bedarf eines Verbrauchsfaktors $k$

## Direktbedarfskoeffizienten

## Direktbedarfskoeffizient $a_{k j}$

Anzahl Mengeneinheiten eines Verbrauchsfaktors $k$, die für jede Mengeneinheit eines übergeordneten Erzeugnisses $j$ direkt benötigt wird

## Vorlaufzeiten

## Vorlaufzeit $z_{k}$

technisch bedingte, reine Produktionszeit bzw. unvermeidliche Transport- oder Lieferzeit für einen Verbrauchsfaktor $k$ (ohne Sicherheitsvorlaufzeiten oder geplante Warte- und Liegezeiten)

## fortgeschriebene Lagerbestände

disponibler Lagerbestand $y_{k t}$ in Periode $t$
physisch vorhandener oder ausstehender, in Periode $t$ aber verfügbarer Bestand eines Verbrauchsfaktors $k$ (ohne Vormerk- oder Sicherheitsbestand)# Lineares Gleichungssystem zur Materialbedarfsrechnung 

Gesamtbedarf für ein Erzeugnis $k$

$$
r_{k}=d_{k}+\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot r_{j}
$$

## Gesamtbedarfsvektor

$$
\begin{aligned}
& \mathbf{r}=\mathbf{d}+\mathbf{A} \cdot \mathbf{r} \\
& \mathbf{E} \cdot \mathbf{r}-\mathbf{A} \cdot \mathbf{r}=\mathbf{d} \\
& (\mathbf{E}-\mathbf{A}) \cdot \mathbf{r}=\mathbf{d} \quad \text { (Produktionsfunktion) } \\
& \Longrightarrow \text { Technologiematrix } \mathbf{E}-\mathbf{A} \\
& \mathbf{r}=(\mathbf{E}-\mathbf{A})^{-1} \cdot \mathbf{d} \\
& \Longrightarrow \text { Verflechtungsbedarfsmatrix }(\mathbf{E}-\mathbf{A})^{-1}
\end{aligned}
$$# Lineares Gleichungssystem zur Materialbedarfsrechnung

## Beispiel Materialbedarfsermittlung

![img-22.jpeg](img-22.jpeg)

$$r_k = d_k + \sum_{j \in \mathcal{N}_k} a_{kj} \cdot r_j$$

(vgl. Tempelmeier (2008))

Univ.-Prof. Dr. Michael Manitz

Material-Logistik: Bestandsmanagement 29-13# Lineares Gleichungssystem zur Materialbedarfsrechnung

## Beispiel Materialbedarfsermittlung

![img-23.jpeg](img-23.jpeg)

$$r_{\text{E1}} = 0 \cdot r_{\text{E1}} + 0 \cdot r_{\text{E2}} + 0 \cdot r_{\text{E3}} + 6 \cdot r_{\text{B1}} + 0 \cdot r_{\text{B2}} + 0 \cdot r_{\text{P1}} + 0 \cdot r_{\text{P2}} + 0$$

$$r_{\text{E2}} = 0 \cdot r_{\text{E1}} + 0 \cdot r_{\text{E2}} + 0 \cdot r_{\text{E3}} + 3 \cdot r_{\text{B1}} + 5 \cdot r_{\text{B2}} + 0 \cdot r_{\text{P1}} + 0 \cdot r_{\text{P2}} + 0$$

$$r_{\text{E3}} = 0 \cdot r_{\text{E1}} + 0 \cdot r_{\text{E2}} + 0 \cdot r_{\text{E3}} + 0 \cdot r_{\text{B1}} + 1 \cdot r_{\text{B2}} + 0 \cdot r_{\text{P1}} + 4 \cdot r_{\text{P2}} + 0$$

$$r_{\text{B1}} = 0 \cdot r_{\text{E1}} + 0 \cdot r_{\text{E2}} + 0 \cdot r_{\text{E3}} + 0 \cdot r_{\text{B1}} + 0 \cdot r_{\text{B2}} + 2 \cdot r_{\text{P1}} + 3 \cdot r_{\text{P2}} + 20$$

$$r_{\text{B2}} = 0 \cdot r_{\text{E1}} + 0 \cdot r_{\text{E2}} + 0 \cdot r_{\text{E3}} + 2 \cdot r_{\text{B1}} + 0 \cdot r_{\text{B2}} + 0 \cdot r_{\text{P1}} + 1 \cdot r_{\text{P2}} + 40$$

$$r_{\text{P1}} = 0 \cdot r_{\text{E1}} + 0 \cdot r_{\text{E2}} + 0 \cdot r_{\text{E3}} + 0 \cdot r_{\text{B1}} + 0 \cdot r_{\text{B2}} + 0 \cdot r_{\text{P1}} + 0 \cdot r_{\text{P2}} + 100$$

$$r_{\text{P2}} = 0 \cdot r_{\text{E1}} + 0 \cdot r_{\text{E2}} + 0 \cdot r_{\text{E3}} + 0 \cdot r_{\text{B1}} + 0 \cdot r_{\text{B2}} + 0 \cdot r_{\text{P1}} + 0 \cdot r_{\text{P2}} + 80$$

(ivgl. Tempelmeier (2008))

Univ.-Prof. Dr. Michael Manitz

Material-Logistik: Bestandsmanagement

29-14# Lineares Gleichungssystem zur Materialbedarfsrechnung

![img-24.jpeg](img-24.jpeg)

$$r = d + A \cdot r$$

(vgl. Tempelmeier (2008))

Univ.-Prof. Dr. Michael Manitz

Material-Logistik: Bestandsmanagement 29-15# Lineares Gleichungssystem zur Materialbedarfsrechnung

## Beispiel Materialbedarfsermittlung

![img-25.jpeg](img-25.jpeg)

$$(vgl. \, \text{Tempelmeier (2008))}$$

Primärbedarfsvektor = $$d = \begin{pmatrix} 0 & E1 \\ 0 & E2 \\ 0 & E3 \\ 20 & B1 \\ 40 & B2 \\ 100 & P1 \\ 80 & P2 \end{pmatrix}$$

Univ.-Prof. Dr. Michael Manitz

Material-Logistik: Bestandsmanagement

29-16# Lineares Gleichungssystem zur Materialbedarfsrechnung

## Beispiel Materialbedarfsermittlung

![img-26.jpeg](img-26.jpeg)

$$(vgl. \, \text{Tempelmeier (2008))}$$

$$ \text{Direktbedarfsmatrix} = A = \begin{pmatrix} 0 & 0 & 0 & 6 & 0 & 0 & 0 \\ 0 & 0 & 0 & 3 & 5 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 & 4 \\ 0 & 0 & 0 & 0 & 0 & 2 & 3 \\ 0 & 0 & 0 & 2 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 \end{pmatrix} \tag{E1} $$

$$ \text{Direktbedarfsmatrix} = A = \begin{pmatrix} 0 & 0 & 0 & 6 & 0 & 0 & 0 \\ 0 & 0 & 0 & 3 & 5 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 & 4 \\ 0 & 0 & 0 & 0 & 0 & 2 & 3 \\ 0 & 0 & 0 & 2 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 \end{pmatrix} \tag{B1} $$

$$ \text{Univ.-Prof. Dr. Michael Manitz Material-Logistik: Bestandsmanagement} \tag{P9-17} $$# **Beispiel Materialbedarfsermittlung**

![img-27.jpeg](img-27.jpeg)

$$(vgl. \, \text{Tempelmeier (2008))}$$

$$(vgl. \, \text{Tempelmeier (2008))}$$

Technologiematrix = $$E - A = \begin{pmatrix}
1 & 0 & 0 & -6 & 0 & 0 & 0 \\
0 & 1 & 0 & -3 & -5 & 0 & 0 \\
0 & 0 & 1 & 0 & -1 & 0 & -4 \\
0 & 0 & 0 & 1 & 0 & -2 & -3 \\
0 & 0 & 0 & -2 & 1 & 0 & -1 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1
\end{pmatrix}$$

$$E1$$

$$E2$$

$$E3$$

$$B1$$

$$B2$$

$$P1$$

$$P2$$# Lineares Gleichungssystem zur Materialbedarfsrechnung

## Beispiel Materialbedarfsermittlung

![img-28.jpeg](img-28.jpeg)

$$(vgl. \, \text{Tempelmeier (2008))}$$

Verflechtungsbedarfsmatrix = $$(E - A)^{-1}$$ = $$\begin{pmatrix}
1 & 0 & 0 & 6 & 0 & 12 & 18 \\
0 & 1 & 0 & 13 & 5 & 26 & 44 \\
0 & 0 & 1 & 2 & 1 & 4 & 11 \\
0 & 0 & 0 & 1 & 0 & 2 & 3 \\
0 & 0 & 0 & 2 & 1 & 4 & 7 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1
\end{pmatrix}$$

E1

E2

E3

B1

B2

P1

P2

Univ.-Prof. Dr. Michael Manitz

Material-Logistik: Bestandsmanagement

29-19![img-29.jpeg](img-29.jpeg)

Verflechtungsbedarfskoeffizient von E2 in bezug auf P2

Univ.-Prof. Dr. Michael Manitz
Material-Logistik: Bestandsmanagement
29-20![img-30.jpeg](img-30.jpeg)

Verflechtungsbedarfskoeffizient von E2 in bezug auf P2

$$v_{\text{E2,P2}} = a_{\text{E2,B1}} \cdot a_{\text{B1,P2}}$$

$$= 3 \cdot 3$$![img-31.jpeg](img-31.jpeg)

Verflechtungsbedarfskoeffizient von E2 in bezug auf P2

$$v_{\text{E2,P2}} = a_{\text{E2,B1}} \cdot a_{\text{B1,P2}} + a_{\text{E2,B2}} \cdot a_{\text{B2,B1}} \cdot a_{\text{B1,P2}}$$

$$= 3 \cdot 3 + 5 \cdot 2 \cdot 3$$![img-32.jpeg](img-32.jpeg)

Verflechtungsbedarfskoeffizient von E2 in bezug auf P2

$$
v_{\text{E2,P2}} = a_{\text{E2,B1}} \cdot a_{\text{B1,P2}} + a_{\text{E2,B2}} \cdot a_{\text{B2,B1}} \cdot a_{\text{B1,P2}} + a_{\text{E2,B2}} \cdot a_{\text{B2,P2}}
$$

$$
= 3 \cdot 3 + 5 \cdot 2 \cdot 3 + 5 \cdot 1
$$![img-33.jpeg](img-33.jpeg)

Verflechtungsbedarfskoeffizient von E2 in bezug auf P2

$$
v_{\text{E2,P2}} = a_{\text{E2,B1}} \cdot a_{\text{B1,P2}} + a_{\text{E2,B2}} \cdot a_{\text{B2,B1}} \cdot a_{\text{B1,P2}} + a_{\text{E2,B2}} \cdot a_{\text{B2,P2}}
$$

$$
= 3 \cdot 3 + 5 \cdot 2 \cdot 3 + 5 \cdot 1 = 44
$$![img-34.jpeg](img-34.jpeg)

Menge der Wege/Pfade von einem Erzeugnis *i* nach *j*:

$$
\mathcal{P}_{ij} = \{\ldots, p_{ij}, \ldots\} \text{ mit } p_{ij} = \{i = i_1, i_2, \ldots, i_s = j\}
$$

Verflechtungsbedarfskoeffizient von E2 in bezug auf P2

$$
v_{\text{E2, P2}} = a_{\text{E2, B1}} \cdot a_{\text{B1, P2}} + a_{\text{E2, B2}} \cdot a_{\text{B2, B1}} \cdot a_{\text{B1, P2}} + a_{\text{E2, B2}} \cdot a_{\text{B2, P2}}
$$

$$
= 3 \cdot 3 + 5 \cdot 2 \cdot 3 + 5 \cdot 1 = 44
$$![img-35.jpeg](img-35.jpeg)

Menge der Wege/Pfade von einem Erzeugnis *i* nach *j*:

$$
\mathcal{P}_{ij} = \{\ldots, p_{ij}, \ldots\} \text{ mit } p_{ij} = \{i = i_1, i_2, \ldots, i_s = j\}
$$

### Verflechtungsbedarfskoeffizient

$$
v_{ij} = \sum_{p_{ij} \in \mathcal{P}_{ij}} \prod_{m=1}^{s-1} a_{i_m, i_{m+1}}
$$

Univ.-Prof. Dr. Michael Manitz

Material-Logistik: Bestandsmanagement 29-26# Lineares Gleichungssystem zur Materialbedarfsrechnung

![img-36.jpeg](img-36.jpeg)

**(vgl. Tempelmeier (2008))**

Univ.-Prof. Dr. Michael Manitz

Material-Logistik: Bestandsmanagement

29-27# **Beispiel Materialbedarfsermittlung**

![img-37.jpeg](img-37.jpeg)

(vgl. Tempelmeier (2008))

### Gesamtbedarfsvektor

$$\mathbf{r} = (\mathbf{E} - \mathbf{A})^{-1} \cdot \mathbf{d} = \begin{pmatrix}
1 & 0 & 0 & 6 & 0 & 12 & 18 \\
0 & 1 & 0 & 13 & 5 & 26 & 44 \\
0 & 0 & 1 & 2 & 1 & 4 & 11 \\
0 & 0 & 0 & 1 & 0 & 2 & 3 \\
0 & 0 & 0 & 2 & 1 & 4 & 7 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1
\end{pmatrix} \cdot \begin{pmatrix}
0 \\
0 \\
0 \\
20 \\
40 \\
100 \\
80
\end{pmatrix} = \begin{pmatrix}
2760 \\
6580 \\
1360 \\
460 \\
1040 \\
100 \\
80
\end{pmatrix} \cdot \begin{pmatrix}
2760 \\
6580 \\
1360 \\
460 \\
1040 \\
100 \\
80
\end{pmatrix} \cdot \begin{pmatrix}
2760 \\
6580 \\
1360 \\
460 \\
1040 \\
100 \\
80
\end{pmatrix}$$

Univ.-Prof. Dr. Michael Manitz Material-Logistik: Bestandsmanagement 29-28# **Materialbedarfsrechnung**

**Gesamtbedarf** für ein Erzeugnis *k*

$$r_k = d_k + \sum_{j \in \mathcal{N}_k} a_{kj} \cdot r_j$$

*Univ.-Prof. Dr. Michael Manitz*

*Material-Logistik: Bestandsmanagement*

*M 20-2*# Materialbedarfsrechnung 

## Bruttobedarf für ein Erzeugnis $k$ zum Zeitpunkt $t$

$$
r_{k t}=d_{k t}+\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot r_{j t}
$$# Materialbedarfsrechnung 

Bruttobedarf für ein Erzeugnis $k$ zum Zeitpunkt $t$

$$
r_{k t}=d_{k t}+\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot r_{j t}
$$

Nettobedarf für ein Erzeugnis $k$ zum Zeitpunkt $t$

$$
q_{k t}=d_{k t}+\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot r_{j t}-y_{k, t-1}
$$# Materialbedarfsrechnung 

Bruttobedarf für ein Erzeugnis $k$ zum Zeitpunkt $t$

$$
r_{k t}=d_{k t}+\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot r_{j t}
$$

Nettobedarf für ein Erzeugnis $k$ zum Zeitpunkt $t$

$$
q_{k t}=d_{k t}+\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot \underline{q}_{j t}-y_{k, t-1}
$$# Materialbedarfsrechnung 

Bruttobedarf für ein Erzeugnis $k$ zum Zeitpunkt $t$

$$
r_{k t}=d_{k t}+\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot r_{j t}
$$

Nettobedarf für ein Erzeugnis $k$ zum Zeitpunkt $t$

$$
q_{k t}=d_{k t}+\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot \underline{q}_{j t}-y_{k, t-1}+y_{k t}
$$

$\mathbf{r}=f($ Erzeugnisstruktur)
$\mathbf{q}=f($ Erzeugnisstruktur, Kosten, Kapazitäten)# Materialbedarfsrechnung 

Bruttobedarf für ein Erzeugnis $k$ zum Zeitpunkt $t$

$$
r_{k t}=d_{k t}+\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot r_{j t}
$$

Nettobedarf für ein Erzeugnis $k$ zum Zeitpunkt $t$

$$
q_{k t}=d_{k t}+\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot \underline{q}_{j t}-y_{k, t-1}+y_{k t}
$$

$\mathbf{r}=f($ Erzeugnisstruktur)
$\mathbf{q}=f($ Erzeugnisstruktur, Kosten, Kapazitäten)
Als das eigentliche, übergeordnete Entscheidungsproblem erweist sich die optimale Bestimmung von

$$
\mathbf{y}=f(\text { Kosten, Kapazitäten })
$$# Bruttobedarf für ein Erzeugnis $k$ zum Zeitpunkt $t$ 

$$
r_{k t}=d_{k t}+\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot r_{j t}
$$

Nettobedarf für ein Erzeugnis $k$ zum Zeitpunkt $t$

$$
q_{k t}=d_{k t}+\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot \underline{q}_{j t}-y_{k, t-1}+y_{k t}
$$

$\mathbf{r}=f($ Erzeugnisstruktur)
$\mathbf{q}=f($ Erzeugnisstruktur, Kosten, Kapazitäten)
Als das eigentliche, übergeordnete Entscheidungsproblem erweist sich die optimale Bestimmung von

$$
\mathbf{y}=f(\text { Kosten, Kapazitäten })
$$

## u. B. d. Lagerbilanzgleichungen

$$
y_{k t}=y_{k, t-1}+q_{k t}-d_{k t}-\sum_{j \in \mathcal{N}_{k}} a_{k j} \cdot q_{j t}
$$

Das System der Lagerbilanzgleichungen liefert als Nebenbedingung(en) für o. a. Optimierungsproblem eine eindeutige Lösung für die mit den optimalen Lagerbeständen verbundenen Nettobedarfsmengen, d. h. Beschaffungs- bzw. Produktionsmengen (Losgrößen $q_{k t}$ ).