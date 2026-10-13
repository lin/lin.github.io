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
    return -1

T = int(input())
for _ in range(T):
    n = int(input())
    a, b, c = tuple(map(int, input().split(' ')))
    nums = list(map(int, input().split(' '))) # list of nums
    s = input().strip()
    words = [w.strip() for w in input().split(' ')]

    res = solve(n, nums)
    print(res)
    # print(*res)
    # print("YES" if res else "NO")