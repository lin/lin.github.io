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
    n, k = ti()
    a = li()
    b = li()

    a.sort()
    b.sort()

    candidates = set()
    for i in range(n):
        candidates.add(a[i])
        candidates.add(b[i])

    res = 0
    for p in candidates:
        pos = n - bisect_left(a, p)
        tot = n - bisect_left(b, p)
        neg = tot - pos
        
        if neg <= k:
            revenue = p * tot
            if revenue > res:
                res = revenue
    
    print(res)