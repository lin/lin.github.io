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

def get_factors(n):
    result = []
    for i in range(2,n+1): # test all integers between 2 and n
        s = 0;
        while n/i == floor(n/float(i)): # is n/i an integer?
            n = n/float(i)
            s += 1
        if s > 0:
            for k in range(s):
                result.append(i) # i is a pf s times
        if n == 1:
            return result

def solve(n, x):
    res = [i+1 for i in range(n)]
    if x == n:
        res[0], res[-1] = res[-1], res[0]
        return  res
    else:
        if n % x != 0:
            return []

        factors = get_factors(n // x)
        res[0] = x # 1 => x
        res[-1] = 1 # n => 1
        curr = x
        for factor in factors:
            res[curr - 1] = curr * factor
            curr *= factor
    return res

T = int(input())
for _ in range(T):
    n, x = tuple(map(int, input().split(' ')))

    res = solve(n, x)
    if res:
        print(*res)
    else:
        print(-1)