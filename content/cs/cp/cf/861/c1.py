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


def solve(a, b):
    a, b = str(a), str(b)

    if a == b:
        return a

    len_a, len_b = len(a), len(b)
    
    if len_b > len_a:
        return '9' * len_a
    
    n = len_a

    if n == 1:
        return a

    a0, b0 = int(a[0]), int(b[0])

    if b0 - a0 > 1:
        return str(a0 + 1) * len_a  # right
    
    next_a = int(str(a)[1])
    next_b = int(str(b)[1])


for _ in range(ii()):
    a, b = ti()

    res = solve(a,b)
    print(res)