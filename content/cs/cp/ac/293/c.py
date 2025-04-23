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

h, w = ti()

mat = [[0] * w for _ in range(h)]

for i in range(h):
    row = li()
    for j in range(w):
        mat[i][j] = row[j]

def dp(r,c,seen):
    if r == h-1 and c == w-1:
        return 1
    
    res = 0
    if r + 1 < h and mat[r+1][c] not in seen:
        res += dp(r+1, c, seen + [mat[r+1][c]])

    if c + 1 < w and mat[r][c+1] not in seen:
        res += dp(r, c+1, seen + [mat[r][c+1]])
    
    return res

print(dp(0,0,[mat[0][0]]))