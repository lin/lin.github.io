---
math: true
---

## 重要概念

1. **Skill** is the atom and problem is the molecular.
1. **Problem** has_many **skill_rating_weights**.
1. **Problem_container** has_many problems and has_many skill_rating_weights.
1. Player has a **player_skill_rating** for each skill.
1. Player has a calculated **score** for each problem_container
1. Problem_container has a rating based on related skills in skill_rating_weights.
1. When update player_skill_rating, the problem_skill_rating as the opponent's rating is calculated based on skill_rating_weight, time used, player_solving_history. 

```ruby
problem_skill_rating = calculate_rectified_rating(
    skill_rating_weight.rating,
    skill_rating_weight.weight,
    time_used,
    player_solving_history
)
```


## Elo Rating

Each **Player** (Student) has a **Rating** for each **Skill**.

Each **Problem** is based on several **Skill**s and for each **Skill** there is a **Rating** for its difficulty.

So the probability for a Player to solve a Problem is:


$$
p = \Pi p_i\, , \text{where}\, p_i = \frac{1}{1 + 10^{R_{\text{player}} - R_{\text{problem}}}}
$$

For each **Problemset**, there is a distribution of problems, and we can analyse their skills components, to find out the occurrence and the difficulty distribution for all related skills. And based on the skill rating of that player, we can predict their expected score.

## Battles and Kills

## Estimate Score

## 如何理解 Rating 和 Score 之间的关系

## Rating：选拔竞赛的实力

### Rating 值的估算

和IQ的估算类似，Rating是稀有度的估算，也就是人群中比例的估算。

因为CF提供官方的rating，所以这里的难度与CF接近，也就是说要比LC难度大，比AC难度小，一般的原则有：

1. 100，基本不可能做不上的题目
1. 200，需要一定计算的题目
1. 300，
1. 400，应该是初学者做上入门题目，有一半概率做对的难度
1. 500，
1. 600，
1. 700，公式法
1. 800，
1. 900，叠加法级别的难度
1. 1000，错位相减级别路题
1. 1100，圆锥曲线中韦达定理套路题
1. 1200，多个技能综合题
1. 1300，需要尝试探索的题目
1. 1400，难题，相当于选择题10题难度
1. 1500，难题，相当于选择题11题难度
1. 1600，相当于高考压轴题的难度
1. 1700，相当于竞赛难度
1. 1800，相当于竞赛难题的难度
1. 1900，
1. 2000，可以90%的概率做上高考压轴题

### Rating 的可信度

学生参加的考试越多，我们对其技能的评价就越精准，这里的贝叶斯函数暂时不采用

## Score：资格考试的标准

### Score 的计算公式

$$ s = \Sigma w_i \cdot p_i $$

$ w_i $ 指的分值比重，例如， $ w_3 = 5 / 150 $，指的是在一个150分满分的试卷中，当前的技能水平（$ w_3 $可以指代错位相减法的 $1100$ 级别的题目）考察了5分

$ p_i $ 指的是概率，也就是当前技能考察难度和考生的技能水平所求出的概率，用 $r$ 表示题目的技能评级, 用 $R$ 表示学生此技能的评级，则：

$$
p_i = \frac{1}{1 + 10^{R - r}}
$$

如果 $w_i$ 对于每一个技能不是具体的值，而是根据技能评级产生的分布，例如：

$$
f(r) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(r-\mu)^2}{2(\sigma)^2}\right)
$$

那么，我们用 $r$ 表示题目的技能评级，做上这个分布题目的概率则是：

$$
p_i = \int_0^{\infty}\frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(r-\mu)^2}{2(\sigma)^2}\right) \frac{1}{1 + 10^{R- r}} dr
$$

为了得到 $p_i$，需要求解积分：

```python
import numpy as np
from scipy.integrate import quad

def estimate_integral(sigma, mu, R):
    # Define the integrand function
    def integrand(r, sigma, mu, R):
        return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((r - mu) ** 2) / (2 * sigma ** 2)) / (1 + 10 ** (R - r))
    
    # Perform the numerical integration from 0 to infinity
    result, error = quad(integrand, 0, np.inf, args=(sigma, mu, R))
    
    return result
```

如上所述，对学生的技能估计，也是一个分布，也就是说，我们可以进一步的估算

$$
p_i = \int_0^{\infty}\int_0^{\infty}\frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(r-\mu)^2}{2(\sigma)^2}\right) \frac{1}{\sigma_0\sqrt{2\pi}} \exp\left(-\frac{(R-\mu_0)^2}{2(\sigma_0)^2}\right)\frac{1}{1 + 10^{R- r}} drdR
$$

也就是：

```python
import numpy as np
from scipy.integrate import dblquad

def integrand(r, R, mu, sigma, mu0, sigma0):
    gaussian_r = 1/(sigma*np.sqrt(2*np.pi)) * np.exp(-(r - mu)**2 / (2*sigma**2))
    gaussian_R = 1/(sigma0*np.sqrt(2*np.pi)) * np.exp(-(R - mu0)**2 / (2*sigma0**2))
    logistic = 1 / (1 + 10**(R - r))
    return gaussian_r * gaussian_R * logistic

def calculate_integral(mu, sigma, mu0, sigma0, lower_bound=0, upper_bound=np.inf):
    result, error = dblquad(
        integrand, 
        lower_bound, 
        upper_bound, 
        lambda x: lower_bound, 
        lambda x: upper_bound, 
        args=(mu, sigma, mu0, sigma0)
    )
    return result
```

| 100 分制 | 150分制 | GPA |
|:----------:|:---------:|:-------:|
| >=97     | 145.5   | A+    |
| >=93     | 139.5   | A |
| >=90     | 135     | A-|
| >=87     | 130.5   | B+|
| >=83     | 124.5   | B |
| >=80     | 120     | B- |
| >=77     | 115.5   |C+|
| >=73     | 109.5   | C|
| >=70     | 105     |C-|
| >=67     | 100.5   |D+|
| >=63     | 94.5    | D|
| >=60     | 90      |D-|




