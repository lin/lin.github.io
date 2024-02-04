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

def solve(n, s, r):
    avg, mod = r // (n-1), r % (n-1)
    remain = [avg] * (n-1)
    for i in range(mod):
        remain[i] += 1
    return [s - r] + remain

for _ in range(ii()):
    #n = ii()
    n, s, r = ti()
    #s = si()
    #nums = li()

    res = solve(n, s, r)
    print(*res)
    # print(*res)
    # print("YES" if res else "NO")