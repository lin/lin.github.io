---
title: "结婚要挑个吉日？"
date: 2021-03-22
math: true
---

本文意图证明如下观点：

**无论结婚选择什么日期，都不会对婚后的幸福程度造成很大影响**

### 1 数学证明

本文讨论的结婚后的幸福程度，主要指的是婚姻幸福程度，例如，经常吵架表示幸福程度低，离婚表示幸福程度极度低。

这里讨论的问题就是，选择了一个特定的结婚日期，对婚后幸福程度的影响，也就是：

$$ p(婚后幸福程度 | 结婚日期) $$

的概率密度分布。接下来可能简写成：

$$ p(婚后 | 婚期) $$

根据贝叶斯公式，显然有：

$$ p(婚后 | 婚期)  = \frac{ p(婚期 | 婚后) \cdot p(婚后) }{p(婚期)}$$

因为婚期是日期，符合均匀分布，有

$$ p(婚后 | 婚期)  \propto p(婚期|婚后) \cdot p(婚后) $$

对于：

$$p(结婚日期|婚后幸福程度)$$

上式的意思就是，如果明确了（知道了）婚后幸福程度，那么这些人结婚日期的分布是什么样的。例如，在所有最后离婚的夫妻中，结婚日期的分布如何。

因为当前的情况下，几乎所有新人都会把结婚日期定在所谓吉日。我们假设，所有新人婚期的确定都是依据吉日而定。那么，无论婚后幸福程度如何，我们都可以认为结婚日期的分布就是婚期吉日程度的分布，也就是：

$$p(婚期|婚后) = p(婚期吉日程度)$$

可知：

$$p(婚后|婚期) \propto p(吉日)\cdot p(婚后)$$


假设对于一个固定的地区，吉日的分布是一定的，那么有：

$$p(婚后幸福|婚期) \propto p(婚后幸福)$$

从而可以知道，无论婚期选择什么日期，都不会对婚后的幸福程度造成（显著）影响，证毕。

### 2 如何否定上述结论

如果观察到下列事实，可以否定上述结论：

1. 离婚的群体当中，有大量没有选择吉日
1. 经常吵架的夫妻，有大量没有选择吉日
1. 没有选择吉日的新人，很多人都离婚了
1. 没有选择吉日的新人，很多人经常吵架

### 3 更为直接的佐证

大家都选择了吉日作为标准，但离婚率却稳步提升。**如果选择好日子对婚后幸福有很大影响，难道不应该离婚率显著下降吗？**

如果选择吉日有效，为什么没有文明国家或地区制定标准化的结婚日期指南呢？（如果有效，民政局就应该领证时发个小日历）

很难找到没选择吉日而导致的婚姻不幸福；却很容易找到 **虽然选择了吉日，却依旧要离婚或者婚姻不幸福的例子**

如果你看到夫妻离婚，几乎没有人会去问哪天结的婚，是不是婚期没选好。（大概大家也知道，婚期导致离婚的说法很扯淡）

### 结束语

盲目的轻信和服从，确实省劲，但要为此付出没必要的经济代价，还是动动脑子更加实惠。