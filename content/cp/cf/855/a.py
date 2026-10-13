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

def solve(s):
    res = []
    for ch in s:
        if not res or res[-1] != ch:
            res.append(ch)
    return res == ['m', 'e', 'o', 'w']

for _ in range(ii()):
    n = ii()
    s = si().lower()
    
    res = solve(s)
    print("YES" if res else "NO")