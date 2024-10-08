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

def solve(n):
    res = []
    i = 1
    j = n**2
    while i < j:
        res.append(i)
        res.append(j)
        i += 1
        j -= 1
    if i == j:
        res.append(i)
    return res

for _ in range(ii()):
    n = ii()
    res = solve(n)
    #print(res)
    for r in range(n):
        row = res[n*r:(n*r + n)]
        if r % 2 == 1:
            print(*row[::-1])
        else:
            print(*row)
    # print(res)
    # print(*res)
    # print("YES" if res else "NO")