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
    s = si()

    first_p = -1
    last_s = -1

    for i in range(n):
        if s[i] == 'p':
            if first_p == -1:
                first_p = i
        elif s[i] == 's':
            last_s = i

    found_p = False
    res = 'YES'
    for i in range(n):
        if s[i] == 'p':
            found_p = True
        if s[i] == 's':
            if found_p:
                res = 'NO'
                break
    
    # if has s
    if last_s != -1 and last_s != 0:
        if first_p!=-1 and first_p != n-1:
            res = 'NO'
    
    print(res)