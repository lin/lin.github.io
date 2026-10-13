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


def solve(n, s):
    flips = 0
    for i in range(1, n):
        if s[i] != s[i - 1]:
            flips += 1
    if s[0] == '0':
        flips -= 1
    return max(0, flips)
        
T = int(input())
for _ in range(T):
    n = int(input())
    #nums = list(map(int, input().split(' '))) # list of nums
    s = input().strip()
    print(solve(n, s))