from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

#from sortedcontainers import SortedList

d4 = [(-1,0),(0,1),(1,0),(0,-1)]
d8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

def solve(n, k, hs, ps):
    data = [[ps[i], hs[i]] for i in range(n)]
    data.sort()

    damage = k
    i = 0
    while i < n:
        if data[i][1] <= damage:
            i += 1
            continue
        k -= data[i][0]
        if k < 0:
            return False
        damage += k
 
    return True

for _ in range(ii()):
    #n = ii()
    n, k = ti()
    #s = si()
    h = li()
    p = li()

    res = solve(n, k, h, p)
    #print(res)
    # print(*res)
    print("YES" if res else "NO")