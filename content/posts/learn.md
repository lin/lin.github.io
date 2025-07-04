---
title: 'Human Cognitive Learning'
date: 2025-07-04
math: true
---

<style>
strong {
  font-weight: bold;
  color: black;
  background-color: #fff200;
  padding: 0 4px;
}
</style>

## Words: Compressed Associations

1. **$P(t \mid p)$**, given a prompt $p$, the distribution of the generated tokens
1. $h^{(l)}_i$, means the $i$-th word (feature) in $l$-th layer of abstraction.

Markov Blanket as you can assign a symbol to a compression of some class of information.

## Features

1. If you can't see enough examples, it is hard to mine out a deeper level pattern. 

## Free Energy Principle

The Free Energy Principle is a mathematical framework that explains how biological systems resist disorder and maintain their structure by minimizing free energy.

$$
\mathcal{F}[q(s)] = \mathrm{D}_{\mathrm{KL}}\left( q(s) \\,\|\\, p(s\mid o) \right) - \mathbb{E} _{q(s)} \left[ \log p(o \mid s) \right]
$$

The first term relates to complexity, is information-seeking and relates to epistemic value.

The second term relates to accuracy, is goal-directed behavior and relates to pragmatic value.

The brain tries to minimize this free energy, and if the system expects a sharp drop in free energy from action $a$, it will treat that action as highly desirable.

$$
\text{Motivation}(a) \propto -\mathbb{E}_ {q(s', o' \mid a)}\left[ \mathcal{F}(s', o') \right]
$$

We can analyze the motivation as four parts:

1. **Epistemic Gain**: How informational appealing the situation is. What the percieved epistemic gain (resolving uncertainty, updating its beliefs) is. How curious the agent under this situation. 
1. **Epistemic Cost**: The cognitive cost to reach desired level of resolution. How much efforts needed to obtain the desired information.
1. **Pragmatic Gain**: The non-intellectual benefits (staying alive, getting food). Get rewarded.
1. **Pragmatic Cost**: The non-intellectual efforts (workload, spending money).

The agent might additive to the situation with small investment with high return.

## Models

1. $D_{\mathrm{KL}}(T\\|L)$, KL divergence of a learner's probability distribution from a testing set true probability distribution.

## Training Data

$\theta' = \theta - \eta \nabla_\theta \mathcal{L}(f_\theta(x), y)$

## Reading a Learning Material

## Retention

> Repeated exposure to a pattern leads to better retention

1. $$

> High emotional level can increase the retention efficiency in one exposure.

When an agent has a high combined perceived epistemic and pragmatic gain, the agent will open the gate for memorization wider for better retention.

It can be seen as an analogy for heat transmission, as high energy can permeate deeper. The brain may also revisited the association by replay or self-exposure the event, like a fond memory you active or subconsciously repeatly revisits.

A well explain video or lecture, only count for a reasonable perceived epistemic gain, not too much shock and not too much randomness or no new information available.

So that only account for a low level of exposure.

But by doing exercise, it will increase the agent perceived pragmatic value when the correct answer exposed especially they can see the benefits of solving the problem correctly and the discrepency of required level of resolution of the problem answer.

### Spaced Repetition

The whole idea of efficiency learning is to increase the exposures of high utility associations.

Greater surprise or informational gain for the learner.

If the information is presented in a short time of period, that surprise or free energy can be reduced too much.

as the adjancent occurs will be compressed with little update urgency.

## Epistemical Kinetic Energy

Human is attracted by situations that a low cognitive cost can lead to a boost in knowledge acquisition.

## Pragmatical Potential Energy

## Self-evaluation as a Pragmatical Gain

Since people tend to protect their ego and self-worth, 

## Presumptions

I believe:

1. all things can be explained by associations.
1. 

## Agent

I don't know the cause of these effects, but they are facts observed in reality.

> Some agents can achieve desired retention with less exposures.

Some agents can find high abstract associations in a few exposures which we normally call it **insightful**.

## Thermodynamics

1. **Work** is an agent's action to change the environment.
1. **Entropy** is how confused you are.
1. **Energy** is how motivated you are.
1. **Kinetic Energy** is how an agent is epistemically motivated.
1. **Potential Energy** is how an agent is pragmatically motivated.
1. Both low and high entropy systems can be low in complexity. The most interesting, complex systems often lie between pure order and pure randomness.

## Learning as a High Return Exploration

Normally, if you do research, you try out new exploration or exploitation current situations.

But learning in human sense is basically remembering the compressed, high confidence asscociations that is proved to be useful in real world challenges.

It doesn't matter the association is right or not, maybe the school teachs you the earth is flat, but you don't have the resources to really disproof this.


There is no system 1 and system 2, it only means fluent words and inarticulate fresh situations.