---
title: "Gödel's Proof"
date: 2025-06-16
draft: true
math: true
---

<style>
p code {
  font-family: 'Fira Code', 'Courier New', Courier, monospace;
  font-size: 0.95em;
  background-color: #f5f5f5;
  color: #c7254e;
  padding: 0.2em 0.4em;
  border-radius: 4px;
  border: 1px solid #e1e1e8;
  white-space: pre-wrap;
  word-break: break-word;
}
    </style>

## Mathematical Statements

Following are some mathemtical statements:

$$
\begin{aligned}
\textbf{1.}\quad & \forall n \in \mathbb{N}\, \exists p > n\, p \in \mathbb{P}\newline
\textbf{2.}\quad  & \forall n > 2\, \nexists a, b, c \in \mathbb{N}^{+}\, a^n + b^n = c^n \newline
\textbf{3.}\quad & \forall n \in \mathbb{N}\, n > 2 \wedge n \bmod 2 = 0 \Rightarrow \exists p, q \in \mathbb{P}\, n = p + q 
\end{aligned}
$$

Normally we care about general statements about all numbers since they can save us computations.

## An Algorithm

Godel shows that checking a proof for a statement is an algorithm that can be run on a computer.

So if you give me a proof of Goldbach's conjecture, I can directly put it into a computer and wait for the computer to tell me whether this proof is valid or not.

## A Class of Numbers

Now we define a class of numbers as:

$$
\mathrm{isNotProvable}(x) := \neg ( \exists y\, \mathrm{isProof}(y, x) ) \newline
$$

so again, it means that there is a class of number called `isNotProvable` numbers.

## The Unprovable Statement

The true statement $\theta(\text{encode}(\theta))$ is not provable in the system, where $\theta$ is a function that is defined as $\theta(x) = \mathrm{isNotProvable}(\text {encode} ( \text {decode} (x)(x)))$

We can say there is a class of number called `theta` numbers. Then you can't prove the number encodes `theta` function is a `theta` number, even though it is true.

In JavaScript, that means if you run `(x => isNotProvable(encode(decode(x)(x))))(encode(x => isNotProvable(encode(decode(x)(x)))))`, it will loop forever, because there is no proof (a number) for this true statement.

## The Proof

$$\theta(\text{encode}(\theta))$$ 

is the same as:

$$\mathrm{isNotProvable}(\text{encode}(\text{decode}(\text{encode}(\theta))(\text{encode}(\theta))))$$

Since $\text{decode}(\text{encode}(\theta))$ means $\theta$, so

$$
 \mathrm{isNotProvable}(\text{encode}(\theta(\text{encode}(\theta))))
$$

We know $\theta(\text{encode}(\theta))$ should return `true` or `false`

If $\theta(\text{encode}(\theta))$ returns `false`, that implies $\mathrm{isNotProvable}(\text{encode}(\theta(\text{encode}(\theta))))$ returns `false`, which says it is provable, but this is a false statement. That means we have a contradiction here.

So if the system can't contain contradiction, $\theta(\text{encode}(\theta))$ has to return `true`, that implies $\mathrm{isNotProvable}(\text{encode}(\theta(\text{encode}(\theta))))$, which says it is not provable. There is a true statement you can't prove.