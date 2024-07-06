from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))

    last_seen = [-10**15] * (n+1)
    dp = [0] * (n + 1)
    for i, a in enumerate(A):
        dp[i + 1] = max(dp[i], last_seen[a] + i + 1)
        last_seen[a] = max(last_seen[a], dp[i] - i)
    
    print(dp[-1])