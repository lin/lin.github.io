---
math: true
---

## Bell's Inequality

{{<youtube ZuvK-od647c>}}

## Hidden Variable

### Alice and Bobs has eight possible plans

1. ↑↑↑ & ↓↓↓
1. ↑↑↓ & ↓↓↑
1. ↑↓↑ & ↓↑↓
1. ↑↓↓ & ↓↑↑
1. ↓↑↑ & ↑↓↓ 
1. ↓↑↓ & ↑↓↑
1. ↓↓↑ & ↑↑↓
1. ↓↓↓ & ↑↑↑

### Plan 1

|                           |  Bob 1 ↓  |  Bob 2 ↓ |  Bob 3 ↓ |
| :-----------------------: | :-: | :-: | :-: |
|           Alice    1 ↑          |  ✓  |  ✓  |  ✓  |
|            Alice   2 ↑          |  ✓  |  ✓  |  ✓  |
|            Alice   3 ↑          |  ✓  |  ✓  |  ✓  |

### Plan 2

|                           |  Bob 1 ↓  |  Bob 2 ↓ |  Bob 3 ↑ |
| :-----------------------: | :-: | :-: | :-: |
|           Alice    1 ↑          |  ✓  |  ✗  |  ✓  |
|            Alice   2 ↑          |  ✗  |  ✓  |  ✗  |
|            Alice   3 ↓          |  ✓  |  ✗  |  ✓  |

### Plan 3

|           | Bob 1 ↓ | Bob 2 ↑ | Bob 3 ↓ |
| :-------: | :-----: | :-----: | :-----: |
| Alice 1 ↑ |    ✓    |    ✗    |    ✓    |
| Alice 2 ↓ |    ✗    |    ✓    |    ✗    |
| Alice 3 ↑ |    ✓    |    ✗    |    ✓    |

### Plan 4

|           | Bob 1 ↓ | Bob 2 ↑ | Bob 3 ↑ |
| :-------: | :-----: | :-----: | :-----: |
| Alice 1 ↑ |    ✓    |    ✗    |    ✗    |
| Alice 2 ↓ |    ✗    |    ✓    |    ✓    |
| Alice 3 ↓ |    ✗    |    ✓    |    ✓    |


### Plan 5

|           | Bob 1 ↑ | Bob 2 ↓ | Bob 3 ↓ |
| :-------: | :-----: | :-----: | :-----: |
| Alice 1 ↓ |    ✓    |    ✗    |    ✗    |
| Alice 2 ↑ |    ✗    |    ✓    |    ✓    |
| Alice 3 ↑ |    ✗    |    ✓    |    ✓    |


### Plan 6

|           | Bob 1 ↑ | Bob 2 ↓ | Bob 3 ↑ |
| :-------: | :-----: | :-----: | :-----: |
| Alice 1 ↓ |    ✓    |    ✗    |    ✓    |
| Alice 2 ↑ |    ✗    |    ✓    |    ✗    |
| Alice 3 ↓ |    ✓    |    ✗    |    ✓    |


### Plan 7

|           | Bob 1 ↑ | Bob 2 ↑ | Bob 3 ↓ |
| :-------: | :-----: | :-----: | :-----: |
| Alice 1 ↓ |    ✓    |    ✓    |    ✗    |
| Alice 2 ↓ |    ✓    |    ✓    |    ✗    |
| Alice 3 ↑ |    ✗    |    ✗    |    ✓    |


### Plan 8

|           | Bob 1 ↑ | Bob 2 ↑ | Bob 3 ↑ |
| :-------: | :-----: | :-----: | :-----: |
| Alice 1 ↓ |    ✓    |    ✓    |    ✓    |
| Alice 2 ↓ |    ✓    |    ✓    |    ✓    |
| Alice 3 ↓ |    ✓    |    ✓    |    ✓    |

There are 48 ✓ and 24 ✗ above, total is 8*9 = 72 possibilities.

So the expected fraction of difference is:

$$
\frac{2}{3}
$$

### Simulation

```python
import random

# Define the eight deterministic plans as dicts mapping axis→outcome
PLANS = [
    {1:+1, 2:+1, 3:+1},  # Plan 1: (↑↑↑)
    {1:+1, 2:+1, 3:-1},  # Plan 2: (↑↑↓)
    {1:+1, 2:-1, 3:+1},  # Plan 3: (↑↓↑)
    {1:+1, 2:-1, 3:-1},  # Plan 4: (↑↓↓)
    {1:-1, 2:+1, 3:+1},  # Plan 5: (↓↑↑)
    {1:-1, 2:+1, 3:-1},  # Plan 6: (↓↑↓)
    {1:-1, 2:-1, 3:+1},  # Plan 7: (↓↓↑)
    {1:-1, 2:-1, 3:-1},  # Plan 8: (↓↓↓)
]

def simulate_hidden_variable(runs=10000):
    mismatches = 0
    for _ in range(runs):
        plan = random.choice(PLANS)
        # randomly pick measurement axes i, j ∈ {1,2,3}
        i = random.randint(1,3)
        j = random.randint(1,3)
        a = plan[i]  # Alice’s outcome
        b = -plan[j]  # Bob’s outcome is opposite on same-axis
        if a != b:
            mismatches += 1
    return mismatches / runs

print(simulate_hidden_variable())  # ≳0.56 (never reaches 0.50)
```

## Quantum

Give $\uparrow$, 

$$
p(\downarrow) = \cos^2(\frac{\theta}{2})
$$

Give $\downarrow$, 

$$
p(\uparrow) = \cos^2(\frac{\theta}{2})
$$

When $\theta=0$, $p=1$ and when $\theta=120^{\circ}$, $p=\dfrac{3}{4}$

### Situation 1

|                  | Bob 1 ↓  |  Bob 2 ↓ |  Bob 3 ↓ |
| :--------------: | :------------: | :------------: | :------------: |
| **Alice 1 ↑**       |     100 % ✓    |     75 % ✓     |     75 % ✓     |
| **Alice 2 ↑**      |     75 % ✓     |     100 % ✓    |     75 % ✓     |
| **Alice 3 ↑**       |     75 % ✓     |     75 % ✓     |     100 % ✓    |

### Situation 2

|               | Bob 1 ↓ | Bob 2 ↓ | Bob 3 ↑ |
| :-----------: | :-----: | :-----: | :-----: |
| **Alice 1 ↑** | 100 % ✓ |  75 % ✓ |  75 % ✓ |
| **Alice 2 ↑** |  75 % ✓ | 100 % ✓ |  75 % ✓ |
| **Alice 3 ↓** |  75 % ✓ |  75 % ✓ | 100 % ✓ |

### Situation 3

|               | Bob 1 ↓ | Bob 2 ↑ | Bob 3 ↓ |
| :-----------: | :-----: | :-----: | :-----: |
| **Alice 1 ↑** | 100 % ✓ |  75 % ✓ |  75 % ✓ |
| **Alice 2 ↓** |  75 % ✓ | 100 % ✓ |  75 % ✓ |
| **Alice 3 ↑** |  75 % ✓ |  75 % ✓ | 100 % ✓ |

### Situation 4

|               | Bob 1 ↓ | Bob 2 ↑ | Bob 3 ↑ |
| :-----------: | :-----: | :-----: | :-----: |
| **Alice 1 ↑** | 100 % ✓ |  75 % ✓ |  75 % ✓ |
| **Alice 2 ↓** |  75 % ✓ | 100 % ✓ |  75 % ✓ |
| **Alice 3 ↓** |  75 % ✓ |  75 % ✓ | 100 % ✓ |

### Situation 5

|               | Bob 1 ↑ | Bob 2 ↓ | Bob 3 ↓ |
| :-----------: | :-----: | :-----: | :-----: |
| **Alice 1 ↓** | 100 % ✓ |  75 % ✓ |  75 % ✓ |
| **Alice 2 ↑** |  75 % ✓ | 100 % ✓ |  75 % ✓ |
| **Alice 3 ↑** |  75 % ✓ |  75 % ✓ | 100 % ✓ |

### Situation 6

|               | Bob 1 ↑ | Bob 2 ↓ | Bob 3 ↑ |
| :-----------: | :-----: | :-----: | :-----: |
| **Alice 1 ↓** | 100 % ✓ |  75 % ✓ |  75 % ✓ |
| **Alice 2 ↑** |  75 % ✓ | 100 % ✓ |  75 % ✓ |
| **Alice 3 ↓** |  75 % ✓ |  75 % ✓ | 100 % ✓ |

### Situation 7

|               | Bob 1 ↑ | Bob 2 ↑ | Bob 3 ↓ |
| :-----------: | :-----: | :-----: | :-----: |
| **Alice 1 ↓** | 100 % ✓ |  75 % ✓ |  75 % ✓ |
| **Alice 2 ↓** |  75 % ✓ | 100 % ✓ |  75 % ✓ |
| **Alice 3 ↑** |  75 % ✓ |  75 % ✓ | 100 % ✓ |

### Situation 8

|               | Bob 1 ↑ | Bob 2 ↑ | Bob 3 ↑ |
| :-----------: | :-----: | :-----: | :-----: |
| **Alice 1 ↓** | 100 % ✓ |  75 % ✓ |  75 % ✓ |
| **Alice 2 ↓** |  75 % ✓ | 100 % ✓ |  75 % ✓ |
| **Alice 3 ↓** |  75 % ✓ |  75 % ✓ | 100 % ✓ |


So the expected fraction of difference is:

$$
\frac{1}{2}
$$

### Simulation

```python
import random
import math

def simulate_singlet(runs=10000):
    mismatches = 0
    for _ in range(runs):
        # pick axes i, j ∈ {1,2,3}, represented by angles θ_i=0°,120°,240°
        angles = {1:0, 2:120, 3:240}
        i, j = random.randint(1,3), random.randint(1,3)
        θ = abs(angles[i] - angles[j]) % 360
        if θ > 180:
            θ = 360 - θ
        # Probability of “different” for singlet: P = ½(1 + cos θ)
        p_diff = 0.5 * (1 + math.cos(math.radians(θ)))
        if random.random() < p_diff:
            mismatches += 1
    return mismatches / runs

print(simulate_singlet())  # ≃0.50
```

## Why

No local hidden-variable theory can reproduce the quantum correlations.

All eight of those “quantum-tables” look identical because, unlike the eight hidden-variable plans, quantum mechanics doesn’t pick one deterministic instruction set at each run—instead it gives one singlet-state rule for all runs.

Mathematically, the Bell-inequality violation tells us that **no joint probability model** of the form

$$
P(A,B \mid a,b)
\\;=\\;
\int d\lambda\\;\rho(\lambda)\\;
P(A\mid a,\lambda)\\;P(B\mid b,\lambda)
$$

* $a,b$ are freely chosen measurement settings,
* $A,B\in\{+1,-1\}$ are the outcomes, and
* $\lambda$ is some “hidden” variable with distribution $\rho(\lambda)$

can reproduce the quantum predictions

$$
P_{\rm QM}(A\neq B\mid a,b)
=\cos^2 \frac{\theta}{2}
$$


```python
def simulate(runs=10000):
    mismatches = 0
    for _ in range(runs):
        plan = random.choice(PLANS)
        # randomly pick measurement axes i, j ∈ {1,2,3}
        i = random.randint(1,3)
        j = random.randint(1,3)
        if is_diff(i, j):
            mismatches += 1
    return mismatches / runs

def is_diff_hidden(i, j):
    plan = generate_plan_from_distribution(random.random())
    return plan[i] != plan[j]

def is_diff_quantum(i, j):
    # simple math function of i and j 
    p_diff = 0.5 * (1 + cos(angles[i] - angles[j]))
    return random.random() < p_diff
```