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
    l, r = ti()
 
    max_size = floor(log(r / l, 2)) + 1
    max_num = 2**(max_size -1)
 
    count = r // max_num - l + 1
    if r // (3 * max_num // 2) - l + 1 > 0:
        count += (r // (3 * max_num // 2) - l + 1) * (max_size - 1)
 
    print(max_size, count)