---
title: "Gödel's Proof"
date: 2025-06-16
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

Gödel shows that checking a proof for a statement is an algorithm that can be run on a computer.

So if you give me a proof of Goldbach's conjecture, I can directly put it into a computer and wait for the computer to tell me whether this proof is valid or not. This can be decided in bounded time.

## A Class of Numbers

Now we define a class of numbers as:

$$
\mathrm{isNotProvable}(x) := \neg ( \exists y\, \mathrm{isProof}(y, x) ) \newline
$$

There is a class of number called `isNotProvable` numbers, just like prime numbers. There is a statement about a property of `isNotProvable` numbers that is true but can't be proved.

## The Unprovable Statement

The true statement $\theta(\text{encode}(\theta))$ is not provable in the system,

where $\theta$ is defined as:

$$\theta(x) = \mathrm{isNotProvable}(\text {encode} ( \text {decode} (x)(x)))$$

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

---

Note 1: To avoid a function call error, the input $x$ in $\theta (x)$ has to be a Gödel number that encodes a formula with exactly one free variable. So $\theta (x)$ should really be:

$$
 \mathrm{isGodelNumberOfOneFreeVariableFormula}(x) \\, \\& \\, \mathrm{isNotProvable}(\text {encode} ( \text {decode} (x)(x)))
$$

Since $\text{encode}(\theta (x))$ indeed is a Gödel number that encodes a formula with exactly one free variable, the following arguments are not affected.

Note 2: Why introduce $\theta (x)$, because $\mathrm{isNotProvable}(x)$ is not taken a Gödel number that encodes a formula with exactly one free variable as the argument, so it can't talk things about itself.