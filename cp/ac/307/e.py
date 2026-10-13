MOD = 998244353

from functools import lru_cache
from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n, m = map(int, input().split())

dp = [m, (m*(m-1)) % MOD, (m*(m-1)*(m-2)) % MOD]

for i in range(3, n):
    dp.append(((m-2)* dp[i-1] + (m-1)*dp[i-2]) % MOD)

print(dp[n-1])