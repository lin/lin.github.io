from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

d4 = [(-1,0),(0,1),(1,0),(0,-1)]
d8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

def solve(n, s):
    MOD = 998244353
    res = 0
    count = 1
    curr = s[0]
    for i in range(1, n):
        ch = s[i]
    # for ch in s[1:]:
        if curr == ch:
            count += 1
        else:
            #print(i, res, count)
            res += (2**count -1) % MOD 
            curr = ch
            count = 1
    res += (2**count -1) % MOD
    # res = 1
    # curr = s[0]
    # count = 1
    # for i in range(1, n):
    #     if s[i] == curr:
    #         res += (2**count) % MOD 
    #         count += 1
    #     else:
    #         count = 1
    #         curr = s[i]
    #         res += 1
        
    return res % MOD

for _ in range(ii()):
    n = ii()
    s = si()
    #a, b, c = ti()
    #nums = li()

    res = solve(n, s)
    print(res)
    # print(*res)
    # print("YES" if res else "NO")