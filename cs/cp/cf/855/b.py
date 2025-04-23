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
    s = si()

    c = Counter(s)
    res = change = 0
    for i in range(26):
        res += min(c[chr(i+65)], c[chr(i+97)])
        change += abs(c[chr(i+65)] - c[chr(i+97)]) // 2

    print(res + min(change, k))