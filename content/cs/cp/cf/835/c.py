from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

dir4 = [(-1,0),(0,1),(1,0),(0,-1)]
dir8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

def solve(n, nums):
    max_, sec_max = None, None
    for num in nums:
        if not max_ or num > max_:
            sec_max = max_
            max_ = num
        elif not sec_max or num > sec_max:
            sec_max = num
    # print(max_, sec_max)

    res = []
    for num in nums:
        if num < max_:
            res.append(num - max_)
        else:
            res.append(num - sec_max)
    return res

T = int(input())
for _ in range(T):
    n = int(input())
    # m, s = tuple(map(int, input().split(' ')))
    nums = list(map(int, input().split(' '))) # list of nums
    # s = input().strip()
    # words = [w.strip() for w in input().split(' ')]
    # res = solve(n, nums)
    # print(*res)
    print(*solve(n, nums))
    # print("YES" if solve(n) else "NO")