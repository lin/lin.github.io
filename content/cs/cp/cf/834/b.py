from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

dir4 = [(-1,0),(0,1),(1,0),(0,-1)]
dir8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

def solve(m, target, nums):
    max_val = max(nums)
    nums_set = set(nums)
    missing = 0
    for i in range(1, max_val + 1):
        if i not in nums_set:
            missing += i
    if target < missing:
        return False
    extra = target - missing
    k = max_val + 1
    while extra > 0:
        extra -= k
        k += 1
    return extra == 0

T = int(input())
for _ in range(T):
    m, s = tuple(map(int, input().split(' ')))
    nums = list(map(int, input().split(' '))) # list of nums

    # print(solve(n))
    print("YES" if solve(m, s, nums) else "NO")