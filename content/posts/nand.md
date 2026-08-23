---
math: true
---

## From Nand To Turing Complete

## 电磁效应

## NAND

## 

我们用 $\theta$ 表示 异或门，我们尝试去实现简单的其他情景。

$$
\mathrm{NAND}(x_1, x_2) \equiv \theta(x_1,x_2)
$$

我们知道异或门对00,01,10,11是1110，观察可以看出

$$
\mathrm{NOT}(x) = \theta(x,x)
$$

$$
\mathrm{AND}(x_1, x_2) = \mathrm{NOT}(\mathrm{NAND}(x_1, x_2))
$$

$$
\mathrm{AND}(x_1, x_2) = \theta(\theta(x_1,x_2),\theta(x_1,x_2))
$$

$$
\mathrm{OR}(x_1, x_2) = \mathrm{NAND}(\mathrm{NOT}(x_1), \mathrm{NOT}(x_2))
$$

$$
\mathrm{OR}(x_1, x_2) = \theta(\theta(x_1,x_1),\theta(x_2,x_2))
$$

$$
\mathrm{NOR}(x_1, x_2) = \theta(\theta(\theta(x_1,x_1),\theta(x_2,x_2)),\theta(\theta(x_1,x_1),\theta(x_2,x_2)))
$$


$$
\mathrm{ON}(x) = \theta(\theta(x,x),\theta(\theta(x,x),\theta(x,x)))
$$

$$
\mathrm{ANDNOT}(x_1, x_2) = \theta(\theta(x_1,\theta(x_2,x_2)),\theta(x_1,\theta(x_2,x_2)))
$$

$$
\begin{aligned}
\mathrm{XOR}(x_1, x_2) = \theta(\theta(\theta(\theta(x_1,\theta(x_2,x_2)),\theta(x_1,\theta(x_2,x_2))),\\
\theta(\theta(x_1,\theta(x_2,x_2)),\theta(x_1,\theta(x_2,x_2)))),\\
\theta(\theta(\theta(x_2,\theta(x_1,x_1)),\theta(x_2,\theta(x_1,x_1))),\\
\theta(\theta(x_2,\theta(x_1,x_1)),\theta(x_2,\theta(x_1,x_1)))))
\end{aligned}
$$

$$
\begin{aligned}
\mathrm{XNOR}(x_1, x_2) = \theta( \theta(\theta(\theta(\theta(x_1,\theta(x_2,x_2)),\theta(x_1,\theta(x_2,x_2))),\\
\theta(\theta(x_1,\theta(x_2,x_2)),\theta(x_1,\theta(x_2,x_2)))),\\
\theta(\theta(\theta(x_2,\theta(x_1,x_1)),\theta(x_2,\theta(x_1,x_1))),\\
\theta(\theta(x_2,\theta(x_1,x_1)),\theta(x_2,\theta(x_1,x_1))))),\\
 \theta(\theta(\theta(\theta(x_1,\theta(x_2,x_2)),\theta(x_1,\theta(x_2,x_2))),\\
\theta(\theta(x_1,\theta(x_2,x_2)),\theta(x_1,\theta(x_2,x_2)))),\\
\theta(\theta(\theta(x_2,\theta(x_1,x_1)),\theta(x_2,\theta(x_1,x_1))),\\
\theta(\theta(x_2,\theta(x_1,x_1)),\theta(x_2,\theta(x_1,x_1))))))
\end{aligned}
$$