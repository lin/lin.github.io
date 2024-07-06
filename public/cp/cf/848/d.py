from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

# d4 = [(-1,0),(0,1),(1,0),(0,-1)]
# d8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

def solve(n, nums):
    mod = 998244353
    # if n, 0 diff, return 0
    # if n, 1 diff, return 1
    # if n, 2 diff, 

    memo = {0:0}
    def dp(k):
        if k in memo:
            return memo[k]
        
        more = dp(k+1) 
        
        return dp(k+1) dp(k-1)
        

    return res % mod

for _ in range(ii()):
    n = ii()
    #a, b, c = ti()
    #s = si()
    nums = li()

    res = solve(n, nums)
    print(res)
    # print(*res)
    # print("YES" if res else "NO")