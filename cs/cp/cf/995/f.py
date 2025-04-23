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
    n,m,q = ti()
    A = li()

    def merge_intervals(intervals):
        if not intervals:
            return []
        intervals.sort()  # sort by start
        res = []
        for s, e in intervals:
            if not res or s > res[-1][1]:
                res.append([s, e])
            else:
                res[-1][1] = max(res[-1][1], e)
        return res

    intervals = [(m, m)]

    res = []
    for a in A:
        new_intervals = []

        for (L, R) in intervals:
            if min(R, a - 1) >= L:
                new_intervals.append((L, min(min(R, a - 1) + 1, n)))
            if L <= a <= R:
                new_intervals.append((1, 1))
                new_intervals.append((n, n))
            if  max(L, a + 1) <= R:
                new_intervals.append((max(1, max(L, a + 1) - 1), R))

        intervals = merge_intervals(new_intervals)

        size = 0
        for (start, end) in intervals:
            size += (end - start + 1)
        res.append(size)

    # output
    print(" ".join(map(str, res)))