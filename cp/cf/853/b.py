from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations, combinations
from math import *

# d4 = [(-1,0),(0,1),(1,0),(0,-1)]
# d8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

def solve(n, s):
    mismatch = False
    found = False
    for i in range(n//2):
        if s[i] != s[~i]:
            if found:
                return False
            mismatch = True
        else:
            if mismatch:
                found = True
                
    return True

for _ in range(ii()):
    n = ii()
    #n, m = ti()
    s = si()
    #nums = li()

    res = solve(n, s)
    #print(res)
    # print(*res)
    print("YES" if res else "NO")