---
title: "Hopfield Networks Example"
math: true
---

_Generated from GPT-4o_

It converges to a stable situation that is pre-defined.

## Step-by-Step Example

Let’s say we want to store **two 4-bit patterns**:

$$
\text{Pattern A: } \xi^1 = [+1, -1, +1, -1] \newline
\text{Pattern B: } \xi^2 = [-1, +1, -1, +1]
$$

### Step 1: Compute the Weight Matrix

Using the Hebbian learning rule:

$$
w_{ij} = \frac{1}{N} \sum_{\mu=1}^P \xi_i^\mu \xi_j^\mu \quad \text{for } i \ne j
$$

Here, $N = 4$, $P = 2$

We ignore diagonal elements $w_{ii} = 0$

We compute:

$$
W = \frac{1}{4} (\xi^1 (\xi^1)^T + \xi^2 (\xi^2)^T)
$$

Let’s compute $\xi^1 (\xi^1)^T$:

$$
\xi^1 (\xi^1)^T =
\begin{bmatrix}
+1 \newline
-1 \newline
+1 \newline
-1
\end{bmatrix}
\begin{bmatrix}
+1 & -1 & +1 & -1
\end{bmatrix}
\newline
= \begin{bmatrix}
+1 & -1 & +1 & -1 \newline
-1 & +1 & -1 & +1 \newline
+1 & -1 & +1 & -1 \newline
-1 & +1 & -1 & +1 \newline
\end{bmatrix}
$$

Same for $\xi^2 (\xi^2)^T$, and then we average.

Final result:

$$
W =
\frac{1}{4} \left(
\begin{bmatrix}
 0 & -2 & 2 & -2 \newline
-2 & 0 & -2 & 2 \newline
 2 & -2 & 0 & -2 \newline
-2 & 2 & -2 & 0 \newline
\end{bmatrix}
\right)
$$

$$
= \begin{bmatrix}
0 & -0.5 & 0.5 & -0.5 \newline
-0.5 & 0 & -0.5 & 0.5 \newline
0.5 & -0.5 & 0 & -0.5 \newline
-0.5 & 0.5 & -0.5 & 0 \newline
\end{bmatrix}
$$

### 🧪 Step 2: Recall from a noisy input

Let’s input a **noisy version of Pattern A**:

$$
x = [+1, -1, -1, -1] \quad \text{(flipped one bit)}
$$

We update each unit $i$ by:

$$
x_i^{\text{new}} = \text{sign}\left(\sum_{j \ne i} w_{ij} x_j \right)
$$

Do this **iteratively** until convergence.

#### Example: Update $x_3$

$$
x_3^{\text{new}} = \text{sign}(w_{31} x_1 + w_{32} x_2 + w_{34} x_4) \newline
= \text{sign}(0.5 \cdot 1 + (-0.5) \cdot (-1) + (-0.5) \cdot (-1)) \newline
= \text{sign}(0.5 + 0.5 + 0.5) = \text{sign}(1.5) = +1
$$

Eventually, the network converges to:

$$
x = [+1, -1, +1, -1] = \xi^1
$$

🎉 **It correctly recalled Pattern A!**

---

## 🧠 What this reveals

* The **network stores memories in its weight matrix**.
* It can **recover full memories** from **partial or corrupted inputs**.
* Each memory is an **attractor** in the energy landscape.
* This is an example of **associative memory**, showing how the brain might complete patterns from fragments.
