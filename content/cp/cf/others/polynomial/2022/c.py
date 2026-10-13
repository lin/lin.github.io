from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

d4 = [(-1,0),(0,1),(1,0),(0,-1)]
d8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

def solve(n, s):

    res = []
    count = 0
    di = None
    for i, ch in enumerate(s):
        if i == 0:
            di = ch
            count = 1
            res.append(1)
        else:
            if ch == di:
                count += 1
            else:
                count = 1
                di = ch
            res.append(i+2-count)
    return res

for _ in range(ii()):
    n = ii()
    #a, b, c = ti()
    s = si()
    #nums = li()

    res = solve(n, s)
    print(*res)
    # print(*res)
    # print("YES" if res else "NO")