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
    odds = [num for num in nums if num & 1]
    evens = [num for num in nums if not num & 1]
    if not odds or len(odds) % 2 == 0:
        return 0

    res = inf
    for odd in odds:
        count = 0
        while odd % 2 == 1:
            odd //= 2
            count +=1
        res = min(res, count)

    for even in evens:
        count = 0
        while even %2 == 0:
            even //=2
            count+=1
        res = min(res, count)
    return res

for _ in range(ii()):
    n = ii()
    #a, b, c = ti()
    nums = li()

    res = solve(n, nums)
    print(res)
    # print(*res)
    # print("YES" if res else "NO")