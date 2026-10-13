from functools import lru_cache
from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n = int(input())

ts = []
for _ in range(n):
    x, y = map(int, input().split())
    ts.append((x, y))

dp = [[0, 0] for _ in range(n+1)]

for i in range(n-1, -1, -1):

    for state in [0, 1]:
        cx, cy = ts[i]
        res = 0

        if cx == 0:
            res = max([res, dp[i+1][0] + cy, dp[i+1][state]])
        else:
            if state == 0:
                res = max([res, dp[i+1][1] + cy, dp[i+1][0]])
            else:
                res = max(res, dp[i+1][1])

        dp[i][state] = res

print(dp[0][0])
