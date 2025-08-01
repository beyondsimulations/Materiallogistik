# Vorlesung 05: Bestandspolitiken
Tobias Vlćek

## 1. Das Grundsetting

Nehmen wir an, wir leiten eine kleine Brauerei.

- Jedes Jahr zu Weihnachten brauen wir ein ganz besonderes, limitiertes
  Festbier. Die Nachfrage ist riesig, aber auch ungewiss.
- Wenn wir zu viel brauen, bleiben wir auf den Flaschen sitzen und
  machen Verlust.
- Brauen wir zu wenig, sind unsere treuen Kunden enttäuscht, und uns
  entgeht ein Gewinn.
- Dies ist eine **einmalige Entscheidung**.

Ganz anders sieht es bei unserem Standard-Pils aus.

- Es wird das ganze Jahr über verkauft.
- Hier müssen wir nicht einmal, sondern **laufend** entscheiden: Wann
  bestellen wir neuen Hopfen und Malz, und wie viel davon?
- Das ist eine **mehrperiodige Entscheidung**.

Beides schauen wir uns nun genauer an.

## 2. Das Newsvendor-Problem

Das “Zeitungsverkäufer-Problem” (Newsvendor Problem) ist der Klassiker
für einmalige Bestandsentscheidungen. Der Name kommt von einem
Zeitungsjungen, der morgens entscheiden muss, wie viele Zeitungen er
kauft, ohne die genaue Nachfrage des Tages zu kennen. Abends sind die
übrigen Zeitungen wertlos.

Dieses Prinzip gilt für viele Produkte:

- Saisonale Modeartikel
- Tickets für ein Konzert oder Sportereignis
- Der Tannenbaumverkauf vor Weihnachten
- **Unser limitiertes Festbier**

Im Kern geht es immer um die Abwägung zweier Risiken:

- **Overage-Kosten ($c_O$):** Die Kosten für jede Einheit, die wir **zu
  viel** bestellt haben und die am Ende übrig bleibt.
- **Underage-Kosten ($c_U$):** Die Kosten für jede nachgefragte Einheit,
  die wir **zu wenig** bestellt haben (entgangener Gewinn).

**Beispiel: Unser Festbier**

- **Herstellungskosten pro Flasche:** 3 GE
- **Verkaufspreis pro Flasche:** 8 GE
- **Restwert:** Nicht verkaufte Flaschen können wir für 1 GE pro Stück
  an einen Restposten-Händler verkaufen.

Daraus berechnen wir die Kosten:

- **Underage-Kosten ($c_U$):** Wenn uns eine Flasche zur Bedienung der
  Nachfrage fehlt, entgeht uns der Gewinn.
  $$c_U = \text{Verkaufspreis} - \text{Herstellungskosten} = 8 - 3 = 5 \text{ GE}$$
- **Overage-Kosten ($c_O$):** Jede Flasche, die wir zu viel produzieren,
  verursacht einen Verlust.
  $$c_O = \text{Herstellungskosten} - \text{Restwert} = 3 - 1 = 2 \text{ GE}$$

### Das kritische Verhältnis (Critical Ratio)

Wir suchen die optimale Bestellmenge, die den erwarteten Gewinn
maximiert.

- Die Lösung liegt im **kritischen Verhältnis**, auch “Critical Ratio”
  genannt.
- Es gibt uns den optimalen Servicegrad vor, bei dem der **erwartete
  Gewinn maximiert wird**.

**Die Logik:**

- Wir sollten so lange eine zusätzliche Einheit auf Lager nehmen, wie
  der erwartete Gewinn aus dem Verkauf dieser Einheit größer ist als der
  erwartete Verlust, falls wir sie nicht verkaufen.
- $c_U \cdot P(\text{Nachfrage} \ge x)$ ist der erwartete Gewinn aus dem
  Verkauf dieser Einheit.
- $c_O \cdot P(\text{Nachfrage} < x)$ ist der erwartete Verlust, falls
  wir sie nicht verkaufen.
- **Das kritische Verhältnis ist der Punkt, an dem sich diese beiden die
  Waage halten.**

$$
\text{Kritisches Verhältnis} = F(x_{opt}) = \frac{c_U}{c_O + c_U}
$$

Für unser Festbier bedeutet das:

$$
\text{Kritisches Verhältnis} = \frac{5}{2 + 5} = \frac{5}{7} \approx 0.714
$$

Das bedeutet: Wir sollten so viele Flaschen brauen, dass die
Wahrscheinlichkeit, die gesamte Nachfrage zu decken, bei ca. 71,4%
liegt.

### Die optimale Bestellmenge finden

Jetzt, da wir das Ziel kennen (71,4% Servicegrad), müssen wir nur noch
die passende Bestellmenge finden. Wie wir das tun, hängt von der Art der
Nachfrageverteilung ab.

#### Fall 1: Diskrete Nachfrage

Stellen wir uns einen Food-Truck vor, der an einem einzigen Tag auf
einem Festival ein spezielles, teures Gericht anbietet.

- Die Herstellungskosten liegen bei 8 GE.
- Der Verkaufspreis beträgt 20 GE.
- Reste sind wertlos ($c_O = 8, c_U = 12$).
- Das kritische Verhältnis ist $12 / (8 + 12) = 0.6$.

Die Erfahrung zeigt folgende Nachfrageverteilung:

| Nachfrage (x) | P(x) | Kumulierte P(Y\<=x) |
|:--------------|:----:|:-------------------:|
| 10 Gerichte   | 0.20 |        0.20         |
| 11 Gerichte   | 0.25 |        0.45         |
| 12 Gerichte   | 0.30 |      **0.75**       |
| 13 Gerichte   | 0.15 |        0.90         |
| 14 Gerichte   | 0.10 |        1.00         |

**Regel:**

Wir suchen die **kleinste Bestellmenge x**, für die die kumulierte
Wahrscheinlichkeit $F(x) = P(Y \le x)$ **größer oder gleich** dem
kritischen Verhältnis ist.

- $F(10) = 0.20 < 0.6$
- $F(11) = 0.45 < 0.6$
- $F(12) = 0.75 \ge 0.6$ –\> **STOPP!**

Die optimale Bestellmenge ist **12 Gerichte**. Obwohl die
Wahrscheinlichkeit für 12 verkaufte Gerichte nur bei 30% liegt, ist das
die beste Entscheidung, um den erwarteten Gewinn zu maximieren.

#### Fall 2: Stetige (Normalverteilte) Nachfrage

Zurück zu unserem Beispiel mit dem Festbier unserer Brauerei.

- Bei Tausenden von Kunden ist die Nachfrage eher eine stetige,
  glockenförmige Kurve.
- Nehmen wir an, die Nachfrage ist **normalverteilt**.
- Wir haben einen Erwartungswert von $\mu=2000$ Flaschen.
- Ferner schätzen wir eine Standardabweichung von $\sigma=300$ Flaschen.

Hier nutzen wir die Formel:

$$
x_{opt} = \mu + z \cdot \sigma
$$

- Der **Sicherheitsfaktor z** ist die Brücke zwischen unserem kritischen
  Verhältnis und der Bestellmenge.
- Wir finden ihn, indem wir die **inverse Standardnormalverteilung** für
  unser kritisches Verhältnis von 0.714 berechnen. Je höher der
  angestrebte Servicegrad (das kritische Verhältnis), desto
  überproportional größer wird der notwendige Sicherheitsfaktor.

**Z-Werte für gängige Servicegrade (Kritisches Verhältnis)**

| $\alpha$-Servicegrad | z-Wert | Bedeutung                               |
|:---------------------|:------:|:----------------------------------------|
| 50%                  | 0.000  | Exakt der Erwartungswert (kein Puffer). |
| 55%                  | 0.126  | 0.126 Standardabweichungen als Puffer.  |
| 60%                  | 0.253  | 0.253 Standardabweichungen als Puffer.  |
| 65%                  | 0.385  | 0.385 Standardabweichungen als Puffer.  |
| 70%                  | 0.524  | 0.524 Standardabweichungen als Puffer.  |
| 75%                  | 0.674  | 0.674 Standardabweichungen als Puffer.  |
| 80%                  | 0.842  | 0.842 Standardabweichungen als Puffer.  |
| 85%                  | 1.036  | 1.036 Standardabweichungen als Puffer.  |
| 90%                  | 1.282  | 1.282 Standardabweichungen als Puffer.  |
| 95%                  | 1.645  | 1.645 Standardabweichungen als Puffer.  |
| 99%                  | 2.326  | 2.326 Standardabweichungen als Puffer.  |

Wir gehen wie folgt vor:

1.  **z-Wert finden:** $\Phi(z) = 0.714 \implies z \approx 0.565$ [^1]
2.  **Optimale Menge berechnen:**
    $x_{opt} = 2000 + 0.565 \cdot 300 \approx 2000 + 170 = 2170$
    Flaschen.
3.  **Sicherheitsbestand:** Der Teil über dem Erwartungswert ist unser
    Puffer gegen Unsicherheit. Sicherheitsbestand =
    $x_{opt} - \mu = 2170 - 2000 = 170$ Flaschen.

Wir sollten also 2170 Flaschen brauen, um unseren erwarteten Gewinn zu
maximieren.

## 3. Die (s, q)-Politik mit Undershoot

Für Produkte, die wir kontinuierlich führen, brauchen wir eine laufende
Strategie. Hier ist die **(s, q)-Politik**, die wir bereits in der
letzten Vorlesung kennengelernt haben, eine oft verwendete Strategie.

Zur Erinnerung:

- Wir überwachen den Lagerbestand **kontinuierlich**.
- Fällt der *disponible Bestand* auf oder unter den **Bestellpunkt
  (s)**, lösen wir eine Bestellung aus.
- Die **Bestellmenge (q)** ist immer fest.

Ein Problem dabei ist das “Unterschießen” des Bestellpunkts, der
sogenannte **Undershoot**. Wenn wir den Bestand nur täglich prüfen, kann
eine große Nachfrage den Bestand weit unter `s` drücken, bevor wir
überhaupt bestellen. Dieser Undershoot ($U$) ist eine zusätzliche
Zufallsgröße, die wir berücksichtigen müssen.

Für eine normalverteilte Tagesnachfrage $D \sim N(\mu_D, \sigma_D^2)$
können wir den Undershoot so abschätzen:

- **Erwarteter Undershoot:**
  $E\{U\} \approx \frac{\sigma_D^2 + \mu_D^2}{2 \mu_D}$
- **Varianz des Undershoots:**
  $\operatorname{Var}\{U\} \approx \frac{\sigma_D^2}{2} \left(1 - \frac{\sigma_D^2}{2\mu_D^2}\right) + \frac{\mu_D^2}{12}$

### Den Bestellpunkt `s` bestimmen

Der **Risikozeitraum** ist die Wiederbeschaffungszeit $L$. Die Nachfrage
$Y$, die unser Bestellpunkt abdecken muss, ist die Summe aus der
Nachfrage während der WBZ ($Y^{(L)}$) und dem Undershoot ($U$).

- Erwartungswert: $\mu_Y = \mu_L + E\{U\} = (L \cdot \mu_D) + E\{U\}$
- Varianz:
  $\sigma_Y^2 = \sigma_L^2 + \operatorname{Var}\{U\} = (L \cdot \sigma_D^2) + \operatorname{Var}\{U\}$

Um den optimalen Bestellpunkt $s_{opt}$ für einen angestrebten
**$\beta$-Servicegrad** (Fill Rate) zu finden, nutzen wir wieder eine
Formel, die auf der Einheiten-Verlustfunktion $G_Z^{(1)}(v)$ basiert.

**Zielbedingung:** Finde den kleinsten Sicherheitsfaktor $v$, für den
gilt: $$
G_Z^{(1)}(v) \leq \frac{(1-\beta) \cdot q}{\sigma_Y}
$$ Der optimale Bestellpunkt ist dann:
$s_{opt} = \mu_Y + v_{opt} \cdot \sigma_Y$.

Den Wert für $v_{opt}$ findet man, indem man den Zielwert für die
Verlustfunktion in einer Tabelle nachschlägt oder einfach in einer
Software berechnet.

**Tabelle der Standard-Verlustfunktion $G_Z^{(1)}(v)$**

|  v  | $G_Z^{(1)}(v)$ |    v     | $G_Z^{(1)}(v)$ |
|:---:|:--------------:|:--------:|:--------------:|
| 0.0 |     0.399      |   1.1    |     0.069      |
| 0.1 |     0.359      |   1.2    |     0.056      |
| 0.2 |     0.323      | **1.25** |   **0.051**    |
| 0.3 |     0.291      |   1.3    |     0.046      |
| 0.4 |     0.262      |   1.4    |     0.038      |
| 0.5 |     0.235      |   1.5    |     0.031      |
| 0.6 |     0.211      |   1.6    |     0.026      |
| 0.7 |     0.189      |   1.7    |     0.021      |
| 0.8 |     0.169      |   1.8    |     0.017      |
| 0.9 |     0.148      |   1.9    |     0.014      |
| 1.0 |     0.083      |   2.0    |     0.011      |

**Beispiel:**

- Ein Bauteil hat eine tägliche Nachfrage von $\mu_D=20, \sigma_D=5$.
- Die WBZ ist $L=10$ Tage, die feste Bestellmenge $q=300$.
- Wir streben $\beta=97\%$ an.

1.  **Undershoot berechnen:**
    $E\{U\} \approx (5^2 + 20^2) / (2 \cdot 20) = 10.625$
    $\operatorname{Var}\{U\} \approx 5^2/2 \cdot (1 - 5^2/(2 \cdot 20^2)) + 20^2/12 \approx 45.42$
2.  **Nachfrage im Risikozeitraum:**
    $\mu_Y = (10 \cdot 20) + 10.625 = 210.625$
    $\sigma_Y^2 = (10 \cdot 5^2) + 45.42 = 295.42 \implies \sigma_Y \approx 17.19$
3.  **Zielwert für Verlustfunktion:** Target
    $G_Z^{(1)}(v) = (1 - 0.97) \cdot 300 / 17.19 \approx 0.523$
4.  **$v_{opt}$ finden:**
    - Wir suchen `v`, sodass $G_Z^{(1)}(v) \le 0.523$. Dies geschieht
      durch Nachschlagen in einer Tabelle der Standard-Verlustfunktion
      oder mittels Software.
    - Die Funktion $G_Z^{(1)}(v)$ hat für $v=0$ einen Wert von ca.
      0.399. Für alle $v>0$ ist der Funktionswert kleiner.
    - Da unser Zielwert von $0.523$ größer ist als $0.399$, ist die
      Bedingung bereits für $v=0$ erfüllt.
    - In der Praxis wird in diesem Fall der Sicherheitsfaktor auf 0
      gesetzt, da kein positiver Puffer benötigt wird.
    - Daher: $v_{opt} \approx 0.0$.
5.  **Bestellpunkt $s_{opt}$:**
    $s_{opt} = 210.625 + 0.0 \cdot 17.19 \approx 211$ Stück. Der
    Bestellpunkt sollte auf 211 Stück gesetzt werden.

## 4. Die periodische Politik (r, S)

Nicht für jedes Produkt lohnt sich eine ständige Überwachung. Für
Joghurt im Supermarkt ist es effizienter, nur einmal pro Woche
(periodisch) nachzusehen und aufzufüllen. Hierfür eignet sich die **(r,
S)-Politik**.

- Wir prüfen den Bestand nur in festen Intervallen, z.B. alle **r=7
  Tage**.
- Wir bestellen dann eine variable Menge, um den Bestand auf ein festes
  **Bestellniveau (S)** aufzufüllen.

### Der längere Risikozeitraum: r + L

Hier müssen wir umdenken: Der **Risikozeitraum ist jetzt $r+L$**! Warum?
Eine Bestellung, die wir heute aufgeben, muss die Nachfrage so lange
decken, bis die *nächste* Lieferung eintrifft. Die nächste Bestellung
lösen wir erst in $r$ Tagen aus, und diese braucht dann nochmal $L$
Tage, um anzukommen.

- Nachfrage im Risikozeitraum: $\mu_{r+L} = (r+L) \cdot \mu_d$
- Standardabweichung: $\sigma_{r+L} = \sqrt{r+L} \cdot \sigma_d$

### Das Bestellniveau `S` bestimmen

Auch hier können wir das optimale Bestellniveau $S_{opt}$ für einen
Ziel-**$\beta$-Servicegrad** bestimmen. Die Logik ist sehr ähnlich zur
(s,q)-Politik, aber die Formel für die Zielbedingung ist leicht anders,
da die erwartete Fehlmenge ins Verhältnis zur erwarteten Nachfrage im
Bestellintervall ($r \cdot \mu_d$) gesetzt wird.

**Zielbedingung (vereinfacht):**[^2] Finde den kleinsten
Sicherheitsfaktor $v$, für den gilt: $$
G_Z^{(1)}(v) \leq \frac{(1-\beta) \cdot r \cdot \mu_d}{\sigma_{r+L}}
$$ Das optimale Bestellniveau ist dann:
$S_{opt} = \mu_{r+L} + v_{opt} \cdot \sigma_{r+L}$.

**Beispiel:** Ein Supermarkt verkauft Frischmilch.

- Bestand wird alle **r=3 Tage** geprüft.
- Die Lieferzeit beträgt **L=1 Tag**.
- Tägliche Nachfrage: $\mu_d=50$ Packungen, $\sigma_d=15$.
- Angestrebter Servicegrad: $\beta=99\%$.

1.  **Risikozeitraum:** $r+L = 3 + 1 = 4$ Tage.
2.  **Nachfrage im Risikozeitraum:** $\mu_{r+L} = 4 \cdot 50 = 200$
    $\sigma_{r+L} = \sqrt{4} \cdot 15 = 30$
3.  **Zielwert für Verlustfunktion:** Target
    $G_Z^{(1)}(v) = (1-0.99) \cdot 3 \cdot 50 / 30 = 0.05$
4.  **$v_{opt}$ finden:**
    - Wir suchen den `v`-Wert, für den $G_Z^{(1)}(v) \leq 0.05$ ist.
5.  **Bestellniveau $S_{opt}$:**
    $S_{opt} = 200 + 1.25 \cdot 30 = 237.5 \approx 238$ Packungen. Jeden
    dritten Tag wird so viel Milch bestellt, dass der verfügbare Bestand
    wieder auf 238 Packungen ansteigt.

## 5. Welche Politik für welches Problem?

- **Newsvendor-Modell:** Perfekt für **einmalige Bestellentscheidungen**
  bei saisonalen oder verderblichen Produkten. Es balanciert elegant die
  Kosten von “zu viel” und “zu wenig”.
- **(s, q)-Politik:** Ideal für **wichtige oder teure Produkte**, bei
  denen sich eine **kontinuierliche Überwachung** lohnt. Sie arbeitet
  mit einem festen Sicherheitsbestand und einer festen Bestellmenge.
- **(r, S)-Politik:** Die richtige Wahl für **Standardprodukte** mit
  geringerem Wert, bei denen eine **periodische Überprüfung** ausreicht.
  Sie ist einfacher zu handhaben, erfordert aber einen höheren
  Sicherheitsbestand, da der Risikozeitraum länger ist.

[^1]: Mit Excel `NORM.S.INV(0.714)`, Python `norm.ppf(0.714)` oder aus
    einer Tabelle ablesen.

[^2]: Die Formel ist exakt unter der Annahme, dass die durchschnittliche
    Bestellmenge genau $r \cdot \mu_d$ ist. In einem System mit
    Fehlbeständen (Backorders) ist die durchschnittliche Bestellmenge
    jedoch leicht höher als die durchschnittliche Nachfrage, da in
    Zyklen nach einem Fehlbestand nicht nur die Nachfrage der aktuellen
    Periode, sondern auch der aufgestaute Fehlbestand aus der Vorperiode
    bedient werden muss.
