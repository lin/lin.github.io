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
    nums.sort()
    res = 0 if nums[0] == 0 else 1
    i = 0
    while i <= n - 1:
        if nums[i] <= i:
            i += 1
            while i <= n - 1 and nums[i] <= i:
                i += 1
            res += 1
        else:
            i += 1
        #print(i, res)
    return res

for _ in range(ii()):
    n = ii()
    #a, b, c = ti()
    #s = si()
    nums = li()

    res = solve(n, nums)
    print(res)
    # print(*res)
    # print("YES" if res else "NO")