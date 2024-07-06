from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations, combinations
from math import *

# d4 = [(-1,0),(0,1),(1,0),(0,-1)]
# d8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

def solve(n, nums):
    return

for _ in range(ii()):
    x, y = ti()

    print((x - y) * 2)
    res = []
    for i in range(x, y, -1):
        res.append(i)
    for i in range(y, x):
        res.append(i)
    print(*res)