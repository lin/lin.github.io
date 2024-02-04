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

def solve(n, m, d, p, a):
    # try every pair and find the minimum move
    # two possibilities: switch positions or move one far away
    dic = {}
    for i, num in enumerate(p):
        dic[num] = i
    
    prev = dic[a[0]]
    min_val = inf
    for i in range(1, len(a)):
        num = a[i]
        curr = dic[num]
        if curr < prev:
            return 0
        if curr - prev > d:
            return 0
        # now curr < prev and curr - prev <= d
        curr_val = curr-prev # swap two positions
        # make two further away
        diff = d - (curr-prev) + 1
        if prev + n - 1 - curr >= diff:
            curr_val = min(curr_val, diff)
        min_val = min(min_val, curr_val)
        prev = curr

    return min_val

for _ in range(ii()):
    #n = ii()
    n, m, d = ti()
    #s = si()
    p = li()
    a = li()

    res = solve(n, m, d, p, a)
    print(res)
    # print(*res)
    # print("YES" if res else "NO")