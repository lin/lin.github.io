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
    n, a, b, c = ti()
    k = n//(a+b+c)
    base_total = (a + b + c) * k
    if base_total == n:
        print(k*3)
    elif base_total + a >= n:
        print(k*3 + 1)
    else:
        print(k*3 + 2)