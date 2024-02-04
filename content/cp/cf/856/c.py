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
    n = ii()
    nums = li()

    res = []
    for k in range(n):
        l, r = 0, k
        while l < r:
            m = (l+r) // 2
            if nums[m]/(k+1-m) >= 1:
                r = m
            else:
                l = m + 1

        res.append(k+1-r)
    
    print(*res)
