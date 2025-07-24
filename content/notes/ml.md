---
title: 'Machine Learning Terms'
date: 2025-07-20
math: true
---

## $f(x; \theta)$

### Model's Prediction

The function $f(x; \theta)$ represents the model's output given input $x$ and parameters $\theta$. It defines how the model maps an input to a prediction.

- $x$ is the input
- $\theta$ is the model’s parameters

**Example:**  
If $f(x; \theta) = \theta_1 x + \theta_0$, with $\theta_1 = 2$, $\theta_0 = 1$, and $x = 3$, then:  
$f(3; \theta) = 2 \cdot 3 + 1 = 7$

---

## $x$

### Input Features

$x$ is the input to the model. It can be a scalar, vector, or tensor depending on the task.

**Example:**  
$x = 4$ may represent 4 hours studied for a test.

---

## $\theta$

### Model Parameters

$\theta$ represents the parameters of the model, which are learned from data.

**Example:**  
In a linear model $f(x) = \theta_1 x + \theta_0$, if $\theta_1 = 5$, $\theta_0 = -2$, then:  
$f(2; \theta) = 5 \cdot 2 - 2 = 8$

---

## $\hat{y}$

### Predicted Output

$\hat{y} = f(x; \theta)$ is the model's predicted value for input $x$.

**Example:**  
If $f(x; \theta) = 3x + 1$ and $x = 2$, then $\hat{y} = 7$

---

## $y$

### Observed (True) Output

$y$ is the actual label from the dataset.

**Example:**  
If a student studied 2 hours and scored 9 points:  
$x = 2$, $y = 9$

---

## $\ell(y, \hat{y})$

### Per-sample Loss Function

$\ell(y, \hat{y})$ measures the difference between predicted output $\hat{y}$ and the true label $y$ for a single data point.

**Example:**  
Using squared loss:  
$\ell(y, \hat{y}) = (y - \hat{y})^2$  
If $y = 9$, $\hat{y} = 7$, then:  
$\ell = (9 - 7)^2 = 4$

---

## $\mathcal{L}(\theta)$

### Empirical Risk / Total Loss

$\mathcal{L}(\theta)$ is the total loss across the dataset. It aggregates the per-sample losses:

$$
\mathcal{L}(\theta) \triangleq \frac{1}{N} \sum_{n=1}^{N} \ell(y_n, f(x_n; \theta))
$$

- $N$ is the number of training examples
- $\ell(y_n, f(x_n; \theta))$ is the loss for the $n$-th example

**Example:**  
Let’s say $N=3$, and the model gives:

- $f(x_1) = 2$, $y_1 = 3$
- $f(x_2) = 5$, $y_2 = 4$
- $f(x_3) = 7$, $y_3 = 6$

Then:

$$
\mathcal{L}(\theta) = \frac{1}{3}\left[(3-2)^2 + (4-5)^2 + (6-7)^2\right] = \frac{1}{3}(1 + 1 + 1) = 1
$$

---

## $p(y \mid f(x; \theta))$

### Likelihood of Observed Label

$p(y \mid f(x; \theta))$ gives the probability of observing label $y$ given the model’s prediction. Often used in probabilistic and Bayesian frameworks.

**Example:**  
In logistic regression:

- $f(x; \theta) = \sigma(\theta^\top x)$
- If $f(x; \theta) = 0.8$, then:

$$
p(y = 1 \mid f(x; \theta)) = 0.8, \quad p(y = 0 \mid f(x; \theta)) = 0.2
$$

This means the model is 80% confident the true label is 1.

---

## $\hat{\theta}$

### Optimal Parameters

$\hat{\theta}$ is the parameter setting that minimizes the total loss $\mathcal{L}(\theta)$ on the training set. It represents the best-fit model under empirical risk minimization.

Formally:

$$
\hat{\theta} = \arg\min_{\theta} \mathcal{L}(\theta) = \arg\min_{\theta} \frac{1}{N} \sum_{n=1}^{N} \ell(y_n, f(x_n; \theta))
$$

**Example:**  
If $\theta$ is a single weight and $\mathcal{L}(\theta)$ reaches its minimum at $\theta = 2.4$, then:  
$\hat{\theta} = 2.4$

---

## $p(y \mid x; \theta)$

### Predictive Distribution (Probabilistic View)

$p(y \mid x; \theta)$ represents the probability of label $y$ given input $x$ and model parameters $\theta$. It’s the **predictive distribution** used in probabilistic models, often derived from $f(x; \theta)$.

- In many models, $f(x; \theta)$ outputs parameters (like logits or means) used to compute this probability.

**Example (Binary Classification):**  
If $f(x; \theta) = 0.8$ is the probability that $y = 1$, then:

$$
p(y = 1 \mid x; \theta) = 0.8,\quad p(y = 0 \mid x; \theta) = 0.2
$$

This term is used extensively in maximum likelihood estimation and Bayesian inference frameworks.

Compare with $p(y \mid f(x; \theta))$, $p(y \mid x; \theta)$ is more general:

```python
# p(y | x; θ)
def likelihood(y, x, theta):
    return full_distribution(y, x, theta)  # could be anything

# p(y | f(x; θ))
def likelihood(y, x, theta):
    z = f(x, theta)         # prediction or feature
    return dist_y_given_z(y, z)  # e.g., softmax(z)
```
---
## $\nabla_\theta \mathcal{L}(\theta)$

### Gradient of the Loss Function

$\nabla_\theta \mathcal{L}(\theta)$ is the gradient of the total loss $\mathcal{L}$ with respect to the parameters $\theta$. It tells us how to adjust $\theta$ to reduce the loss.

**Example:**  
If $\mathcal{L}(\theta) = (\theta - 2)^2$, then  
$\nabla_\theta \mathcal{L}(\theta) = 2(\theta - 2)$  
When $\theta = 3$, the gradient is $2(3 - 2) = 2$

---

## $H(Y)$

### Entropy

$H(Y)$ measures the uncertainty or randomness of a random variable $Y$. It quantifies how unpredictable $Y$ is.

$$
H(Y) = - \sum_{y} p(y) \log p(y)
$$

**Example:**  
If $Y$ is a fair coin: $p(H) = p(T) = 0.5$, then  
$H(Y) = -[0.5 \log 0.5 + 0.5 \log 0.5] = \log 2 \approx 0.693$

---

## $I(X; Y)$

### Mutual Information

$I(X; Y)$ measures how much information $X$ and $Y$ share. It quantifies the reduction in uncertainty of one variable given the other.

$$
I(X; Y) = H(Y) - H(Y \mid X)
$$

**Example:**  
If $X$ and $Y$ are independent, $I(X; Y) = 0$  
If $Y = X$, then knowing $X$ fully determines $Y$, and $I(X; Y) = H(Y)$

---

## $D_{\mathrm{KL}}(P \Vert Q)$

### KL Divergence (Kullback–Leibler)

$D_{\mathrm{KL}}(P \Vert Q)$ measures how one probability distribution $P$ diverges from another distribution $Q$. It is asymmetric and non-negative.

$$
D_{\mathrm{KL}}(P \Vert Q) = \sum_x P(x) \log \frac{P(x)}{Q(x)}
$$

**Example:**  
Let $P = [0.8, 0.2]$, $Q = [0.5, 0.5]$  
Then  
$D_{\mathrm{KL}}(P \Vert Q) = 0.8 \log \frac{0.8}{0.5} + 0.2 \log \frac{0.2}{0.5} \approx 0.257$
