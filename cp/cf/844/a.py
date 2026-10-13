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


for _ in range(ii()):
    #n = ii()
    w, d, h = ti()
    a, b, f, g = ti()
    #s = si()
    #nums = li()

    #res = h
    west = a + f + abs(b - g)
    east = w-a + w-f + abs(b-g)

    south = b + g + abs(a - f)
    north = d-b + d-g + abs(a - f)

    print(min(west, east, south, north) + h)

    # res = solve(n, nums)
    # print(res)
    # print(*res)
    # print("YES" if res else "NO")