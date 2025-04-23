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
    n, x, y = map(int, input().split())
    
    x -= 1
    y -= 1

    res = [0] * n
    if n % 2 == 0:
        res = [i % 2 for i in range(n)]
    else:
        res = [i % 3 for i in range(n)]

    left_x = res[(x-1) % n]
    right_x = res[(x+1) % n]

    left_y = res[(y-1) % n]
    right_y = res[(y+1) % n]

    found = False

    def mex(v):
        s = set(v)
        m = 0
        while m in s:
            m += 1
        return m

    # brute force
    for ax in range(7):
        for ay in range(7):
            if ax == mex([left_x, right_x, ay]):
                if ay == mex([left_y, right_y, ax]):
                    res[x] = ax
                    res[y] = ay
                    found = True
                    break
        if found:
            break

    print(' '.join(map(str, res)))
