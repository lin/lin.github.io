---
title: "Computation"
math: true
---

## DFA / Regular

A finite automaton is a 5-tuple  
$$
M = (Q, \Sigma, \delta, q_{0}, F),
$$  
where:

1. $Q$ is a finite set called the set of states,  
2. $\Sigma$ is a finite set called the input alphabet,  
3. $\delta: Q \times \Sigma \to Q$ is the transition function,  
4. $q_{0}\in Q$ is the start state,  
5. $F \subseteq Q$ is the set of accepting states.  

## NFA / Regular

A nondeterministic finite automaton is a 5-tuple  
$$
M = (Q, \Sigma, \delta, q_{0}, F),
$$  
where:

1. $Q$ is a finite set of states,  
2. $\Sigma$ is a finite alphabet,  
3. $\delta: Q \times \Sigma_{\varepsilon} \to \mathcal{P}(Q)$ is the transition function,  
4. $q_{0}\in Q$ is the start state,  
5. $F \subseteq Q$ is the set of accepting states.  

$P(Q)$ to be the collection of all subsets of $Q$.

## PDA / CFG

A pushdown automaton is a 6-tuple  
$$
M = (Q, \Sigma, \Gamma, \delta, q_{0}, F),
$$  
where:

1. $Q$ is a finite set called the set of states,  
2. $\Sigma$ is a finite set called the input alphabet,  
3. $\Gamma$ is a finite set called the stack alphabet,  
4. $\delta: Q \times \Sigma_{\varepsilon} \times \Gamma_{\varepsilon} \to \mathcal{P}(Q \times \Gamma_{\varepsilon})$ is the transition function,  
5. $q_{0}\in Q$ is the start state,  
6. $F \subseteq Q$ is the set of accepting states.  

## DPDA / DCFG

A deterministic pushdown automaton is a 6-tuple  
$$
M = (Q, \Sigma, \Gamma, \delta, q_{0}, F),
$$  
where:

1. $Q$ is the set of states,  
2. $\Sigma$ is the input alphabet,  
3. $\Gamma$ is the stack alphabet,  
4. $\delta: Q \times \Sigma_{\varepsilon} \times \Gamma_{\varepsilon} \to (Q \times \Gamma_{\varepsilon}) \cup \{\emptyset\}$ is the transition function,  
5. $q_{0}\in Q$ is the start state,  
6. $F \subseteq Q$ is the set of accept states.  

The transition function $\delta$ must satisfy the following condition:  
for every $q\in Q$, $a\in \Sigma$, and $x\in \Gamma$, exactly one of  
$$
\delta(q, a, x),\quad
\delta(q, a, \varepsilon),\quad
\delta(q, \varepsilon, x),\quad
\delta(q, \varepsilon, \varepsilon)
$$  
is not $\emptyset$.  

## Turing Machine

A Turing machine is a 7-tuple  
$$
M = (Q, \Sigma, \Gamma, \delta, q_{0}, q_{\mathrm{accept}}, q_{\mathrm{reject}}),
$$  
where:

1. $Q$ is the set of states,  
2. $\Sigma$ is the input alphabet not containing the blank symbol $␣$,  
3. $\Gamma$ is the tape alphabet, where $␣ \in \Gamma$ and $\Sigma \subseteq \Gamma$,  
4. $\delta: Q \times \Gamma \to Q \times \Gamma \times \{L, R\}$ is the transition function,  
5. $q_{0}\in Q$ is the start state,  
6. $q_{\mathrm{accept}}\in Q$ is the accept state,  
7. $q_{\mathrm{reject}}\in Q$ is the reject state, where $q_{\mathrm{reject}} \neq q_{\mathrm{accept}}$.  

### Properties

1. Every non-deterministic Turing machine has an equivalent deterministic Turing
machine.
1. Every multitape Turing machine has an equivalent single-tape Turing machine.

## Examples

**Regular languages (DFA/NFA)**

1. $L_{1} = \{w\in\\{0,1\\}^* \mid w\text{ has an even number of 1’s}\}$
2. $L_{2} = (0\mid1)^*0(0\mid1)^*$
3. $L_{3} = \{0^n1^m \mid n,m\ge0\}$
4. $L_{4} = \{w\in\\{a,b\\}^* \mid \text{the third symbol from the right of }w\text{ is }a\}$

**Context-free languages but not regular (CFG/PDA)**

1. $L_{5} = \{a^n b^n \mid n\ge0\}$
2. $L_{6} = \{ww^R \mid w\in\\{0,1\\}^*\}$  (palindromes)
3. $L_{7} = \{\text{balanced parentheses over “(” and “)”}\}$
4. Arithmetic expressions, e.g.

   $$
   E \to E + E \mid E * E \mid (E) \mid \mathit{id}
   $$

**Non-context-free languages (not CFG/PDA)**

1. $L_{8} = \{a^n b^n c^n \mid n\ge0\}$
2. $L_{9} = \{ww \mid w\in\\{0,1\\}^*\}$  (tandem repeats)
3. $L_{10} = \{a^p \mid p\text{ is prime}\}$
4. $L_{11} = \{a^n b^n c^m d^m \mid n,m\ge0\}$