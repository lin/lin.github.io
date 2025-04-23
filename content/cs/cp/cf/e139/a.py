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

def solve(p):
    if p[0][0] == p[1][0]:
        if p[2][1] == p[0][1] or p[2][1] == p[1][1]:
            return False
    elif p[1][0] == p[2][0]:
        if p[2][1] == p[0][1] or p[1][1] == p[0][1]:
            return False
    return True

for _ in range(ii()):
    n = input()
    x1, y1 = ti()
    x2, y2 = ti()
    x3, y3 = ti()
    p = [(x1, y1), (x2, y2), (x3, y3)]
    p.sort()
    res = solve(p)
    #print(res)
    # print(*res)
    print("YES" if res else "NO")