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
    #res = []
    odds = []
    evens = []
    for i, num in enumerate(nums):
        if num % 2 == 1:
            odds.append(i+1)
        else:
            evens.append(i+1)

    if len(odds) >= 3:
        return [odds[0], odds[1], odds[2]]
    elif len(odds) >= 1 and len(evens) >= 2:
        return [odds[0], evens[0], evens[1]]
    
    return []

for _ in range(ii()):
    n = ii()
    #a, b, c = ti()
    #s = si()
    nums = li()

    res = solve(n, nums)
    print("YES" if res else "NO")
    if res:
        print(*res)
    # print(*res)
    # print("YES" if res else "NO")