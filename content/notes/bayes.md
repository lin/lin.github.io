---
title: 'Bayes’ Theorem'
date: 2025-07-20
math: true
---

Imagine a population divided into four groups:

1. Male, Gamer
2. Female, Gamer
3. Male, Non-Gamer
4. Female, Non-Gamer

We want to know: if a randomly chosen person is male, what is the probability that they are an Gamer?

1. By definition,

   $$
   P(\text{Male}\mid \text{Gamer})
   = \frac{\text{number of Male Gamers}}{\text{number of Gamers}}.
   $$

2. Similarly,

   $$
   P(\text{Gamer}\mid \text{Male})
   = \frac{\text{number of Male Gamers}}{\text{number of Males}}.
   $$

3. Since

   $$
   \text{number of Male Gamers}
   = P(\text{Gamer}\mid \text{Male}) \times \text{number of Males},
   $$

   we can write

   $$
   P(\text{Male}\mid \text{Gamer})
   = \frac{P(\text{Gamer}\mid \text{Male})\;\times\;\text{number of Males}}
          {\text{number of Gamers}}.
   $$

4. Dividing numerator and denominator by the total population size $N$, we get

   $$
   P(\text{Male}\mid \text{Gamer})
   = \frac{P(\text{Gamer}\mid \text{Male})\;\times\;\dfrac{\text{number of Males}}{N}}
          {\dfrac{\text{number of Gamers}}{N}}
   = \frac{P(\text{Gamer}\mid \text{Male})\;P(\text{Male})}{P(\text{Gamer})}.
   $$

This is **Bayes’ theorem** in its classic form:

$$
\boxed{
P(\mathrm{Male}\mid \mathrm{Gamer})
= \frac{
    \overset{\text{likelihood}}{P(\mathrm{Gamer}\mid \mathrm{Male})}
    \;\times\;
    \overset{\text{prior}}{P(\mathrm{Male})}
  }{
    \overset{\text{evidence}}{P(\mathrm{Gamer})}
  }
}
$$

* **Prior** $P(\text{Male})$: your initial belief about how likely someone is an Male.
* **Likelihood** $P(\text{Gamer}\mid \text{Male})$: how probable it is to observe “Gamer” among Males.
* **Evidence** $P(\text{Gamer})$: the overall chance of picking a Gamer.
* **Posterior** $P(\text{Male}\mid \text{Gamer})$: your updated belief in “Male” once you know “Gamer.”

### With Numbers

Here’s the same survey broken down again:

|            | Gamer | Non‑Gamer | Total |
| ---------: | ----: | --------: | ----: |
|   **Male** |    30 |        70 |   100 |
| **Female** |    50 |        50 |   100 |
|  **Total** |    80 |       120 |   200 |

We now want

$$
P(\text{Male}\mid \text{Gamer}).
$$

---

## 1. Direct calculation

By definition of conditional probability,

$$
P(\text{Male}\mid \text{Gamer})
= \frac{\text{Male \\& Gamer}}{\text{Gamer}}
= \frac{30}{80}
= 0.375
$$

---

## 2. Via Bayes’ theorem

Bayes says

$$
P(A\mid B)
= \frac{P(B\mid A)\,P(A)}{P(B)}.
$$

Let

* $A=\{\text{Male}\}$,
* $B=\{\text{Gamer}\}$.

So

$$
P(\text{Male}\mid \text{Gamer})
= \frac{P(\text{Gamer}\mid \text{Male})\,P(\text{Male})}{P(\text{Gamer})}.
$$

We already know:

* $P(\text{Gamer}\mid \text{Male}) = \dfrac{30}{100} = 0.30.$
* $P(\text{Male}) = \dfrac{100}{200} = 0.50.$

### 2.1. Computing the evidence $P(\text{Gamer})$

Using the law of total probability over Male/Female:

$$
P(\text{Gamer})
= P(\text{Gamer}\mid \text{Male})\,P(\text{Male})
  +P(\text{Gamer}\mid \text{Female})\,P(\text{Female}).
$$

We have

* $P(\text{Gamer}\mid \text{Female}) = \dfrac{50}{100} = 0.50,$
* $P(\text{Female}) = 0.50.$

Hence

$$
P(\text{Gamer})
= 0.30\times0.50 + 0.50\times0.50
= 0.15 + 0.25
= 0.40.
$$

### 2.2. Plug in and finish

$$
P(\text{Male}\mid \text{Gamer})
= \frac{0.30 \times 0.50}{0.40}
= \frac{0.15}{0.40}
= 0.375.
$$

---

## 3. Conclusion

Whether by direct counting or by Bayes’ theorem (with the evidence computed via male/female breakdown), we get

$$
\boxed{P(\text{Male}\mid \text{Gamer}) = 0.375.}
$$


### Why it matters

Bayes’ rule tells you exactly how to **update** your prior belief in light of new evidence. In this example:

$$
\text{posterior} \;\longleftarrow\; \frac{\text{likelihood}\times\text{prior}}{\text{evidence}}.
$$

The more informative your likelihood, the more your posterior shifts away from the prior.
