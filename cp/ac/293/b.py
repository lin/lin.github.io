from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations, combinations
from math import *

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

MOD = 998244353

n = ii()
nums = li()

seen = set()
for i, num in enumerate(nums):
    # id not been called out
    if i+1 not in seen:
        seen.add(num)

res = []
for i in range(n):
    if i+1 not in seen:
        res.append(i+1)
    
print(len(res))
print(*res)