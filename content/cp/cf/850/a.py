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

def solve(n):
    k = 1
    a, b = 0, 0
    total = 0
    while total < n:
        to_add = k if total + k <= n else n - total
        if k % 4 == 0 or k % 4 == 1:
            a += to_add
        else:
            b += to_add
        total += k
        k += 1
    k -= 1

    return a, b

for _ in range(ii()):
    n = ii()
    #a, b, c = ti()
    #s = si()
    #nums = li()

    res = solve(n)
    print(*res)
    # print(*res)
    # print("YES" if res else "NO")