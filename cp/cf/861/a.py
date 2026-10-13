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
    a, b = ti()

    delta = b - a

    if delta < 1000:
        max_val, max_luk = a, 0
        for x in range(a, b+1):
            chars = list(str(x))
            mn, mx = min(chars), max(chars)
            if int(mx)-int(mn) > max_luk:
                max_val, max_luk = x, int(mx)-int(mn)
        print(max_val)
    else:
        # b > 110
        # make it XXX09
        # print(b // 100 * 100 )
        if b // 100 * 100 + 9 <= b:
            print(b // 100 * 100 + 9)
        else:
            print((b-100) // 100 * 100 + 9)

        #print(max_val)

    # print(max_val)

