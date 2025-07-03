---
title: "Linear Algebra Notes"
date: 2025-06-16
math: true
---

## Vector

Each vector is an object with many features values.

## Matrix

Rows are an object with many features, Alice's age gender height weight. Columns are Features for many objects, age of Alice Bob Chris David.

$$
A = \begin{bmatrix}
\vec{c}_1 & \vec{c}_2 & \cdots & \vec{c}_n
\end{bmatrix}
$$

$\vec{c}_1, \vec{c}_2, \cdots, \vec{c}_n$ are the base vectors after transformation described in current axis.

Apply matrix to a vector $\vec{v}$ means you get what $\vec{v}$ means in current axis.

So $A$ is information in current, $\vec{v}$ is information in transformed, $A\vec{v}$ is information in current.

So $\vec{v}$ is `hola` and $A\vec{v}$ is `hello`.

$$
A = U\Sigma V^{T}
$$

So any matrix is: Rotate → Scale → Rotate

It means that we transform information to something we are familiar with, to somewhere many fluent tools are available, then goes back to another encoding system.

## Determinate

$$
\det(A) = \prod_{i=1}^{n} \lambda_i
$$

determinant tells you how much a matrix scales space

if $\det(A)=0$, the transformation will squish all of the space into a lower dimension. This means some information is destroyed in the process. And some of the axis are redundant information.

All columns are linearly independent.



## Inverse

$$\mathrm{rank}(A) = n$$

## Rank

## Non-square

$$A \in \mathbb{R}^{m \times n}, \quad B \in \mathbb{R}^{p \times q}$$


the number of columns in $A$ must equal the number of rows in $B$, that is.

$$
n = p
$$

and then

$$
AB \in \mathbb{R}^{m \times q}
$$


## Eigenvector

$$
A\vec{v} = \lambda \vec{v}
$$

A pure rotation matrix doesn't have eigenvectors.

$$
\text{det}(A -\lambda I) = 0
$$

so it squish to a lower dimension.