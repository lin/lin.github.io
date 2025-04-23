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

def solve(s):
    res = 0
    for ch in s:
        res = max(res, ord(ch) - ord('a') + 1)
    return res

T = int(input())
for _ in range(T):
    n = int(input())
    # m, s = tuple(map(int, input().split(' ')))
    # nums = list(map(int, input().split(' '))) # list of nums
    s = input().strip()
    # words = [w.strip() for w in input().split(' ')]

    print(solve(s))
    # print("YES" if solve(n) else "NO")