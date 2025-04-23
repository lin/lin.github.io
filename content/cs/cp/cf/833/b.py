from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

dir4 = [(-1,0),(0,1),(1,0),(0,-1)]
dir8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

T = int(input())
for _ in range(T):
    n = int(input())
    # nums = list(map(int, input().split(' '))) # list of nums
    s = input().strip()
    # words = [w.strip() for w in input().split(' ')]
    # k = len(set(s))

    # count = Counter()

    res = 0
    for i in range(n): # O(N)
        count = [0] * 10
        max_ch = -1
        k = 0
        for j in range(i, min(n, i + 100)): # O(100)
            ch = int(s[j])
            if count[ch] == 0:
                k += 1
            count[ch] += 1
            if count[ch] > max_ch:
                max_ch = count[ch]
            if max_ch <= k: # O(10)
                res += 1
    print(res)