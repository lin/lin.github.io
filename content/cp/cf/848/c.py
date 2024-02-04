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

def solve(n, k, a, b):
    # if continues, n(n+1)//2 pairs of l,r
    diffs = []
    for i in range(n):
        if a[i] != b[i]:
            diffs.append((i, a[i]))

    char_set = set(a) # a, b, c, d, e
    max_total = 0
    
    # O(256 * n)
    for q in combinations(char_set, min(k, len(char_set))):
        # q would be b, d, e if k == 3
        q = set(q)
        curr_total = 0
        curr = 0
        for i in range(n):
            if a[i] == b[i] or a[i] in q:
                curr += 1
            else:
                curr_total += curr*(curr+1)//2
                curr = 0
        curr_total += curr*(curr+1)//2
        max_total = max(max_total, curr_total)

    return max_total

for _ in range(ii()):
    #n = ii()
    n, k = ti()
    a = si()
    b = si()

    res = solve(n, k, a, b)
    print(res)
    # print(*res)
    # print("YES" if res else "NO")