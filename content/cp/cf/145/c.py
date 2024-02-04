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
    # we can only consider k <= n(n+1)//4
    if k == 0:
        print(*[-(i+1) for i in range(n)])
        continue

    # print(n, k)
    p = 0 # number of positive
    for j in range(n+1):
        if j*(j+1)//2 >= k:
            p = j
            break

    # print(p)
    
    # max postion
    d = p*(p+1)//2 - k
    d = p - 1 - d
    # print(d)

    positives = [i for i in range(1, d+1)] + [p] + [i for i in range(d+1, p)]
    negatives = [-(i+1) for i in range(n-p)]

    psum = [0] + positives + negatives

    # print(psum)

    res = []
    for i in range(1, n+1):
        res.append(psum[i] - psum[i-1])
    
    print(*res)



