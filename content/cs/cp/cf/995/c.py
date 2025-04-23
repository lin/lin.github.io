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
    n, m, k = ti()
    a = li()
    q = set(li())

    f = {i for i in range(1, n + 1) if i not in q}

    if not f:
        print('1' * m)
    elif len(f) == 1:
        print(''.join('1' if a[i] == next(iter(f)) else '0' for i in range(m)))
    else:
        print('0' * m)
        


