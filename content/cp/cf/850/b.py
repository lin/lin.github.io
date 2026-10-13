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

def solve(n, w, h, cakes, dispensers):
    gt, lt = -inf, inf
    # suppose we move dx for cakes
    for i in range(n):
        dispenser = dispensers[i]
        dl, dr = dispenser - h, dispenser + h
        # print(gt, lt)
        # print(dl, dr)

        cake = cakes[i]
        new_gt = dr - w - cake
        new_lt = dl + w - cake

        # print(i, new_gt, new_lt)
        if new_gt > new_lt or new_lt < gt or new_gt > lt:
            return False
        gt, lt = max(new_gt, gt), min(new_lt, lt)

    return True

for _ in range(ii()):
    #n = ii()
    n, w, h = ti()
    #s = si()
    a = li()
    b = li()

    res = solve(n, w, h, a, b)
    #print(res)
    # print(*res)
    print("YES" if res else "NO")