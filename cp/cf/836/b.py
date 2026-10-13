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

def solve(n):
    if n % 2 == 1:
        return [2] * n
    res = []
    for i in range(n//2):
        if i == 0:
            res.append(1)
            res.append(3)
        else:
            res.append(2)
            res.append(2)
    return res

T = int(input())
for _ in range(T):
    n = int(input())
    # a, b, c = tuple(map(int, input().split(' ')))
    # nums = list(map(int, input().split(' '))) # list of nums
    # s = input().strip()
    # words = [w.strip() for w in input().split(' ')]

    res = solve(n)
    print(*res)
    # print(*res)
    # print("YES" if res else "NO")