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

# T = int(input())
# for _ in range(T):
n, k = list(map(int, input().split(' ')))
nums = list(map(int, input().split(' '))) # list of nums

psum = [0]
for num in nums:
    psum.append(psum[-1] + num)

res = 0
start = 0
for end in range(n):
    while psum[end + 1] - psum[start] > k:
        start += 1
    res = max(res, end - start + 1)

print(res)