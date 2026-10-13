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

# max(sum(l, r) - xor(l, r))

def solve(n, nums):
    psum = [0]
    for num in  nums:
        psum.append(psum[-1] + num)
    # sum(l, r) = psum[l+1] - psum[r]
    # xor(l, r) = pxor
    res = 0
    for i in range(n):
        
        res = max(res, curr)
    return res
        
T = int(input())
for _ in range(T):
    n, q = list(map(int, input().split(' ')))
    nums = list(map(int, input().split(' '))) # list of nums
    L, R = list(map(int, input().split(' ')))

    print(solve(n, nums))