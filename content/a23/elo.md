---
math: true
---

## Elo Rating

Each **Player** (Student) has a **Rating** for each **Skill**.

Each **Problem** is based on several **Skill**s and for each **Skill** there is a **Rating** for its difficulty.

So the probability for a Player to solve a Problem is:


$$
p = \Pi p_i\\, , \text{where}\\, p_i = \frac{1}{1 + 10^{R_{\text{player}} - R_{\text{problem}}}}
$$

For each **Problemset**, there is a distribution of problems, and we can analyse their skills components, to find out the occurrence and the difficulty distribution for all related skills. And based on the skill rating of that player, we can predict their expected score.

## Battles and Kills



