---
title: "How Duolingo works?"
isCJKLanguage: true
date: 2025-05-29
---


<style>
table {
  overflow-x: auto;
  white-space: nowrap;
}
</style>

## Streaks

- **gainedXp** (number): Total XP earned on the calendar day.
- **frozen** (boolean): Whether a Streak Freeze protected the streak on that day (i.e., no qualifying activity but streak not lost).
- **streakExtended** (boolean): Whether this day counted toward maintaining/extending the streak.
- **date** (number): Unix epoch seconds at day boundary (UTC). Consecutive entries typically differ by 86,400 seconds.
- **userId** (number): Duolingo user identifier.
- **repaired** (boolean): Whether the streak was later repaired for this day (e.g., post hoc repair product).
- **dailyGoalXp** (number): XP threshold required to meet the daily goal on that day.
- **numSessions** (number): Count of learning sessions completed.
- **totalSessionTime** (number): Sum of session durations in seconds for the day.

## Containers

- course/section/unit/lesson/lexeme
- 30 lexemes per unit
- 60 lexemes per 1 duolingo score
- 3.5 lexemes per word
- 15 exercises in each lesson
- each unit have 24 lessons

## Time Cost 

- 60 minutes per unit
- each exercises takes 10 seconds to solve
- each lesson takes 2.5 minutes to solve
- each lexeme costs 2 minutes to retain
- 5 minutes per lexeme for total learning time.

| CEFR, Sec, Lex    | total  |3m/d (1Ls)     | 15m/d (6Ls)     | 10h/w (1u)          | 50h/w (7u)    |
|:------------------|:-------|:------------|:------------------|:---------------|:--------|
| A1, 3, 1600       | 55h    |  3 years    |7 months           |  1.5 months    | 1 week    |
| A2, 4, 3200       | 105h   |  6 years    |14 months          |  2.5 months    | 2 weeks    |
| B1, 6, 6400       | 205h   |  11 years   |2.5 years         |  5 months    | 1 month    |
| B2, 8, 8500       | 275h   |  15 years   |3 years            |  6 months    | 1.5 months    |

## Spanish from EN

```python
units_in_each_section = [8,26,28,52,50,50,36,36]
```

| Section    | Units  | Lexemes             | Duo / CEFR     | Cost    |
|:-----------|:-------|:------------------|:---------------|:--------|
| Section 1  | 8      |  240 / 240        |  10 (A1)       | 8h    |
| Section 2  | 26      |  780 / 1020      |  20 (A1)       | 34h    |
| Section 3  | 28      |  840 / 1860      |  30 (A1)       | 62h / 100h   |
| Section 4  | 52      |  1560 / 3420     |  60 (A2)       | 114h / 200h   |
| Section 5  | 50      |  1500 / 4920     |  80 (B1)       | 164h    |
| Section 6  | 50      |  1500 / 6420     |  100 (B1)      | 214h / 400h    |
| Section 7  | 36      |  1080 / 7500     |  115 (B2)      | 250h    |
| Section 8  | 36      |  1080 / 8580     |  130 (B2)      | 286h / 600h   |


## French from EN

```python
units_in_each_section = [10,22,21,46,51,49,36,37]
```
|Section     | Units  | Lexemes             | Duo / CEFR     | Cost    |
|:-----------|:-------|:------------------|:---------------|:--------|
| Section 1  | 10     |  300 / 300        |  10 (A1)       | 10h    |
| Section 2  | 22     |  760 / 960       |  20 (A1)       | 32h    |
| Section 3  | 21     |  840 / 1590      |  30 (A1)       | 53h / 100h   |
| Section 4  | 46     |  1560 / 2970     |  60 (A2)       | 99h / 200h   |
| Section 5  | 51     |  1500 / 4500     |  80 (B1)       | 150h    |
| Section 6  | 49     |  1500 / 5970     |  100 (B1)      | 199h / 400h    |
| Section 7  | 36     |  1080 / 7050     |  115 (B2)      | 235h    |
| Section 8  | 37     |  1080 / 8160     |  130 (B2)      | 272h / 600h   |

## English from ES

```python
units_in_each_section = [10,26,20,48,50,52,36,36]
```
|Section     | Units  | Lexemes             | Duo / CEFR     | Cost    |
|:-----------|:-------|:------------------|:---------------|:--------|
| Section 1  | 10     |  300 / 300        |  10 (A1)       | 10h    |
| Section 2  | 22     |  780 / 1080       |  20 (A1)       | 36h    |
| Section 3  | 21     |  600 / 1680      |  30 (A1)       | 56h / 100h   |
| Section 4  | 46     |  1440 / 3120     |  60 (A2)       | 104h / 200h   |
| Section 5  | 51     |  1500 / 4620     |  80 (B1)       | 154h    |
| Section 6  | 49     |  1560 / 6180     |  100 (B1)      | 206h / 400h    |
| Section 7  | 36     |  1080 / 7260     |  115 (B2)      | 242h    |
| Section 8  | 37     |  1080 / 8340     |  130 (B2)      | 278h / 600h   |

## Improvement

1. 15 lexemes 30 minutes 15 lessons per unit (4443)
1. 10 units 5 scores 5 hours per section
1. 5 sections 25 hours 1500 lexemes per level or course
1. 5 courses to reach CEFR B2
1. each hour of learning, you may expose to 15-20 valuable lexemes
1. each week in university, you learn 50-65 lexemes
1. each semester in university, you learn 800-1000 lexemes
1. score 300 to reach A2, 6 lexemes per score, 1800 lexemes
1. score 600 to reach B1, 6 lexemes per score, 3600 lexemes
1. score 900 to reach B2, 8 lexemes per score, 6000 lexemes
1. score 1200 to reach C1, 8 lexemes per score, 8400 lexemes
1. score 1500 to reach C2, 10 lexemes per score, 11400 lexemes