from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations, combinations
from math import *

# d4 = [(-1,0),(0,1),(1,0),(0,-1)]
# d8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

def solve(n, nums):
    # should reduce to 
    # 111122233444555555
    nums.sort()
    curr = 0
    res = 0
    for i in range(n):
        num = nums[i]
        if num == curr:
            continue
        if num == curr + 1:
            curr += 1
        else:
            curr += 1
            res += num - curr
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