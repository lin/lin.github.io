---
math: true
---

## Complexity

## P

1. PATH(G, s, t) is P. PATH: is there a path between s node and t node in a directed graph G.
1. COPRIME(x,y) is P.
1. CFG(G, str) is P.

## NP-complete

1. SAT(formula) is NP. Check whether a Boolean formula can return 1.
1. SUBSET-SUM(S, target) is NP. Find a set to sum to target.
1. HAM_PATH(G, s, t) is NP. A Hamiltonian path in a directed graph G is a directed path that goes through
each node exactly once.
1. 3SAT(formula) is NP.

$$
  (x_{1}\lor \lnot x_{2}\lor x_{3})
  \land
  (x_{3}\lor x_{5}\lor \lnot x_{6})
  \land
  (x_{3}\lor \lnot x_{6}\lor x_{4})
  \land
  (\lnot x_{4}\lor x_{5}\lor x_{6})
$$