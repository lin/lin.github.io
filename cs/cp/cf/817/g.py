from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

T = int(input())
for _ in range(T):
    n = int(input())
    res = []

    x = 0
    for i in range(n - 3):
        res.append(i)
        x ^= i
    x ^= 1 << 30
    x ^= 1 << 29
    res.append(1<<30)
    res.append(1<<29)
    res.append(x)

    print(*res)