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

for _ in range(ii()):
    n = ii()
    nums = li()

    cnt = 0
    for num in nums:
        if num < 0:
            cnt += 1
    
    max_res = []
    min_res = []

    for i in range(n-cnt):
        max_res.append(i+1)
    
    for i in range(cnt):
        max_res.append(n-cnt-i-1)
    
    for i in range(cnt):
        min_res.append(1)
        min_res.append(0)
    
    for i in range(n-2*cnt):
        min_res.append(i+1)

    print(*max_res)
    print(*min_res)
