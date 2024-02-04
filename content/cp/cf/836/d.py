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
    # build from n n n n 
    if n % 2 == 0:
        res = []
        for i in range(n + 1):
            if i != n // 2:
                res.append(n//2 + i)
        return res
    
    # build from n n n n n
    res = [n // 2 + 3 + i for i in range(n)]
    res[0] -= 1
    res[-1] += 1
    res[-2] += 1
    return res

T = int(input())
for _ in range(T):
    n = int(input())
    res = solve(n)
    print(*res)