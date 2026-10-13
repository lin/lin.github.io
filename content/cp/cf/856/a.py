from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations, combinations
from math import *

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

MOD = 998244353

for _ in range(ii()):
    n = ii()
    words = wi()

    cand = []
    for i in range(2*n-2):
        s = words[i]
        if len(s) == n - 1:
            cand.append(s)
    
    #print(cand)
    if cand[0][1:] == cand[1][:-1]:
        if cand[0][0] == cand[1][-1] and cand[0][1:] == cand[0][1:][::-1]:
            print("Yes")
            continue
    else:
        if cand[0][-1] == cand[1][0] and cand[0][:-1] == cand[0][:-1][::-1]:
            print("Yes")
            continue

    print("No")

    # print(res)
    # print(*res)
    # print("YES" if res else "NO")