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
    m = ii()
    seen = [set() for _ in range(m)]
    
    data = []
    for i in range(m):
        ni = ii()
        data.append(li())
    
    s = set()

    res = []
    flag = False
    for i in range(m-1, -1, -1):
        # remain = set(data[i]) - seen[i+1]
        remain = set(data[i]) - s
        if remain:
            res.append(list(remain)[0])
        else:
            flag = True
        s.update(data[i])
        # seen[i] = s.copy()

    # res = []
    # flag = False
    # for i in range(m-1):
    #     remain = set(data[i]) - seen[i+1]
    #     if remain:
    #         res.append(list(remain)[0])
    #     else:
    #         flag = True

    if flag:
        print(-1)
    else:
        # res.append(data[m-1][0])
        print(*res[::-1])