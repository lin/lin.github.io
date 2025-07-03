---
title: "Free Energy Principle"
type: "page"
math: true
---

## The Free Energy Principle

$$
a, \mu, m = \arg\min F(\tilde{s}, \mu \mid m)
$$


Where:

1. $F(\tilde{s}, \mu \mid m)$ is the variational free energy, a quantity that bounds surprise.
1. $\tilde{s}$: sensory inputs (possibly generalized coordinates of sensations).
1. $\mu$: internal states (like beliefs or expectations).
1. $m$: the model or structure used to generate predictions.
1. $a$: actions that can influence the sensory input.
1. $\arg\min$: denotes the values of $a, \mu, m$ that minimize the free energy.

This means that an agent (e.g. a brain) is constantly trying to:

1. Perceive the causes of its sensations correctly (update beliefs $\mu$),
1. Act to bring the world in line with its expectations (change $a$),
1. Adapt its generative model of the world $m$ to better predict future inputs.


## The Bayesian brain hypothesis

$$
\mu = \arg\min_{\mu} \\, D_{\mathrm{KL}} \left( q(\vartheta) \\,\\|\\, p(\vartheta \mid \tilde{s}) \right)
$$

## The Infomax principle

$$
\mu = \arg\max \left\\{ I(\tilde{s}, \mu) - H(\mu) \right\\}
$$

1. $\tilde{s}$: sensory data (observed input)
1. $\mu$: internal representation (e.g. neural encoding or beliefs)
1. $I(\tilde{s}, \mu)$: mutual information between sensory input and internal representations — how much knowing $\mu$ reduces uncertainty about  $\tilde{s}$
1. $H(\mu)$: entropy of the internal representation — how complex or redundant $\mu$ is
1. Minimizing free energy is equivalent to maximizing mutual information (like Infomax), while penalizing complex beliefs (entropy or KL divergence).
