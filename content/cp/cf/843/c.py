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
    n = ii()
    count = Counter()
    sets = []
    for _ in range(n):
        bits = li()[1:]
        sets.append(bits)
        for bit in bits:
            count[bit] += 1

    res = False
    for num in sets:
        curr = True
        for bit in num:
            if count[bit] == 1:
                curr = False
        if curr:
            res = True
    
    print("YES" if res else "NO")
