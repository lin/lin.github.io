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
    s = si()

    k = len(set(s))

    if k == 4 or k == 3:
        print(4)
    elif k == 2:
        cnt = 0
        for ch in s:
            if ch == s[0]:
                cnt += 1
        if cnt == 2:
            print(4)
        else:
            print(6)
    elif k == 2:
        print(4)
    else:
        print(-1)