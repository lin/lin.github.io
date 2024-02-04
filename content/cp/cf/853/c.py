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

#===============#
#===============#
#===============#

for _ in range(ii()):
    n, m = ti()
    nums = li()

    count = [0] * (n + m + 1)
    # assume everything appears the same
    # in the following rows
    for num in nums:
        count[num] = m + 1

    for i in range(m):
        p, v = ti()
        # old: x = nums[p-1]
        # new: y = v
        count[nums[p-1]] -= m - i
        nums[p-1] = v
        count[v] += m - i

    res = 0
    for c in count:
        res += m*(m+1)//2 - (m-c)*(m-c+1)//2

    print(res)