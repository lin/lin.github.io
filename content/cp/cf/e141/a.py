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
    res = []
    if nums[0] == nums[-1]:
        return []

    i = 0
    j = n - 1
    while i < j:
        res.append(nums[i])
        res.append(nums[j])
        i += 1
        j -= 1
    if i == j:
        res.append(nums[i])

    return res

for _ in range(ii()):
    n = ii()
    #a, b, c = ti()
    #s = si()
    nums = li()

    res = solve(n, nums)
    if not res:
        print("NO")
    else:
        print("YES")
        print(*res)
    # print(*res)
    # print("YES" if res else "NO")