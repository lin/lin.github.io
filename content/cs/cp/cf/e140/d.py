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

n = ii()
s = si()

res = deque([i+1 for i in range(2**n)])
#print(res)
c0 = 0
c1 = 0
for ch in s:
    if ch == '1':
        for _ in range(2**c1):
            res.popleft()
        c1 += 1
    else:
        for _ in range(2**c0):
            res.pop()
        c0 += 1
    #print(ch, res)

print(*res)