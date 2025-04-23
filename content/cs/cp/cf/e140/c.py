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

def solve(n, nums):
    MOD = 998244353
    
    return True

# n == ii()
for j in range(ii()):
    reqs = ti() # requirements
    curr = 1
    for i, req in enumerate(reqs): # n - i + 1
        if i == 0:
            if req == 2:
                print(0)
                continue
            curr = 2
        else:
            if req == 0:
                curr *= 2
            elif req == 1:



    res = solve(n, nums)
    print(res)
    # print(*res)
    # print("YES" if res else "NO")