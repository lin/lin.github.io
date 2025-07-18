---
title: 'See A, Think B'
date: 2025-07-15
math: true
---

## $P(B\mid A)$

The equation $E=mc^2$ may be the most celebrated in science, but its practical impact on our everyday lives is limited it dazzles more than it delivers. Even Feynman’s championing of atomic theory, though fundamentally important, doesn’t always translate into direct, universal benefits. In contrast, the principle of Bayesian inference expressed as

$$
P(B\mid A) =\frac{\text{count}(A\cap B)}{\text{count}(A)}
$$

the probability of $B$ given that $A$ has occurred provides a versatile, widely applicable tool for updating beliefs and guiding decisions in countless real‑world situations.

The deductive world of logic and computation only means all $P(B\mid A)$ is always near 1 or near 0.

## Brain Counting Updates

## Bayes’ Theorem

Imagine a population divided into four groups:

1. Male, Adult
2. Female, Adult
3. Male, Child
4. Female, Child

We want to know: if a randomly chosen person is male, what is the probability that they are an adult?

1. By definition,

   $$
   P(\text{Adult}\mid \text{Male})
   = \frac{\text{number of Male Adults}}{\text{number of Males}}.
   $$

2. Similarly,

   $$
   P(\text{Male}\mid \text{Adult})
   = \frac{\text{number of Male Adults}}{\text{number of Adults}}.
   $$

3. Since

   $$
   \text{number of Male Adults}
   = P(\text{Male}\mid \text{Adult}) \times \text{number of Adults},
   $$

   we can write

   $$
   P(\text{Adult}\mid \text{Male})
   = \frac{P(\text{Male}\mid \text{Adult})\\;\times\\;\text{number of Adults}}
          {\text{number of Males}}.
   $$

4. Dividing numerator and denominator by the total population size $N$, we get

   $$
   P(\text{Adult}\mid \text{Male})
   = \frac{P(\text{Male}\mid \text{Adult})\\;\times\\;\dfrac{\text{number of Adults}}{N}}
          {\dfrac{\text{number of Males}}{N}}
   = \frac{P(\text{Male}\mid \text{Adult})\\;P(\text{Adult})}{P(\text{Male})}.
   $$

This is **Bayes’ theorem** in its classic form:

$$
\boxed{
P(\mathrm{Adult}\mid \mathrm{Male})
= \frac{
    \overset{\text{likelihood}}{P(\mathrm{Male}\mid \mathrm{Adult})}
    \\;\times\\;
    \overset{\text{prior}}{P(\mathrm{Adult})}
  }{
    \overset{\text{evidence}}{P(\mathrm{Male})}
  }
}
$$

* **Prior** $P(\text{Adult})$: your initial belief about how likely someone is an adult.
* **Likelihood** $P(\text{Male}\mid \text{Adult})$: how probable it is to observe “male” among adults.
* **Evidence** $P(\text{Male})$: the overall chance of picking a male.
* **Posterior** $P(\text{Adult}\mid \text{Male})$: your updated belief in “adult” once you know “male.”

### Why it matters

Bayes’ rule tells you exactly how to **update** your prior belief in light of new evidence. In this example:

$$
\text{posterior} \\;\longleftarrow\\; \frac{\text{likelihood}\times\text{prior}}{\text{evidence}}.
$$

The more informative your likelihood, the more your posterior shifts away from the prior.

## Class Level Observations

> All men are mortal. Socrates is a man, therefore, Socrates is mortal.

"All men are mortal" is a class property. "Socrates" is a class instance. "Socrates is mortal" means a class instance has to follow class properties.

Whenever a class A almost surely has property B in context H, any instance R of that class will also almost surely have property B in the same context.

$$
\bigl(R\subseteq A\\;\wedge\\;P(B\mid A,H)\ge1-\varepsilon\bigr)\\;\Longrightarrow\\;P(B\mid R,H)\ge1-\varepsilon.
$$

This is based on the assumption that additional information provided by R gives you no extra information about whether property B holds. 

$$
P\bigl(B \mid A,\\,H,\\,R\bigr)
\\;=\\;
P\bigl(B \mid A,\\,H\bigr)
$$

When we observe the reality, for each instance data we collect, we also gather the class level connections. When we think about instant-level priors, its class-level priors, which might be observed by a lot of times, should also be considered so that we are not losing too much the information gain by previous observations.

### Physics provides strong priors

That is why a more knowledgable person can have generally better conclusions with high class-level priors.

### The Triumph of Idiots

Class‑level observations can give us strong priors and thus high confidence but intuitively lumping data into broad categories doesn’t always lead to correct conclusions. Racism is a prime example: people reinforce the false belief that someone’s birthplace is the decisive cause of negative traits or outcomes.

### Russell’s turkey is doing its best

When the turkey’s world has only two outcomes “fed” or “not fed” each morning—and it starts with a uniform Beta (1, 1) prior, the Bayesian predictive probability of breakfast tomorrow after $k$ feedings in $n$ days is

$$
P(\text{fed tomorrow}\mid k,n)=\frac{k+1}{n+2}.
$$

This Beta–binomial formula is the optimal forecast under those assumptions.
For instance, after 100 straight days of being fed ($k=n=100$) the turkey believes

$$
P(\text{fed tomorrow})=\frac{101}{102}\approx 0.99,
$$

i.e., a 99 % chance of one more meal.
Absent any other evidence no knowledge of Thanksgiving, butcher‑shop trucks, or class‑level information this $(k+1)/(n+2)$ rule is the best the turkey can do.

### Connection to the *p‑value* and the weight of reality

A frequentist *p‑value* answers one narrowly defined question:

$$
p = P\bigl(\text{data at least this surprising}\mid H_0\bigr),
$$

the probability of seeing evidence as extreme as ours **if** the null hypothesis $H_0$ holds exactly.

When our current sample is tiny and virtually every prior observation in everyday life has agreed with $H_0$, this number can **look** like a Bayesian update in which $H_0$ carries an enormous prior weight: it merely flags that the new result would be rare under the long‑standing pattern.

But the practical question is different: Given all we already know about the world, is the alternative $H_1$ now more credible than $H_0$?

To answer that, a Bayesian compares **posterior odds**

$$
\frac{P(H_1 \mid \text{data})}{P(H_0 \mid \text{data})}
=\\;
\overset{\text{likelihood ratio}}
       {\frac{P(\text{data}\mid H_1)}{P(\text{data}\mid H_0)}}
\\;\times\\;
\overset{\text{prior odds}}
       {\frac{P(H_1)}{P(H_0)}}.
$$


* **Likelihood ratio**: How well each hypothesis explains the *limited* data we have just collected.
* **Prior odds**: The vast “reality archive” of earlier observations, most of which have already favored $H_0$.

A low p‑value signals that the new data are surprising under $H_0$; it says nothing about how plausible $H_1$ is once those towering prior odds are taken into account. Only by multiplying surprise (the likelihood ratio) by these priors do we learn whether our handful of fresh observations truly dents or merely ripples the immense body of evidence built up from everyday reality.

In short, **p‑values measure surprise, not believability**. Deciding whether $H_1$ “really works” demands folding that surprise into the giant pool of experience that has, so far, mostly vindicated $H_0$.


### Rooster's Crow and Sunrise

$$
P\bigl(\text{sunrise}\mid \text{rooster crow},\\,\text{dawn}\bigr) = 1
$$

$$
\forall t.\\, P\bigl(\text{sunrise}\mid \text{rooster crow},\\,t \bigr) = 1
$$


## Features

## Conceptual Leaps

