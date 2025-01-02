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
    res = []
    for i in range(len(s)):
        ch = s[len(s)-i-1]
        if ch == 'p':
            res.append('q')
        elif ch == 'q':
            res.append('p')
        else:
            res.append(ch)
            
    print(''.join(res))
