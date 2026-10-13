from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations, combinations
from math import *

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

MOD = 998244353

for _ in range(ii()):
    n, m = ti()

    data = []

    for _ in range(n):
        data.append(li())
    
    if n == 1:
        print(0)
        continue
    
    if n == 2:
        res = 0
        for i in range(m):
            res += abs(data[0][i] - data[1][i])
        print(res)
        continue

    # n >= 3
    cols = [[] for _ in range(m)]

    for r in range(n):
        for c in range(m):
            cols[c].append(data[r][c])

    res = 0
    for c in range(m):
        col = cols[c]
        col.sort()

        for i in range(1, n):
            res += (col[i] - col[i-1]) * i * (n- i)
        
    print(res)



