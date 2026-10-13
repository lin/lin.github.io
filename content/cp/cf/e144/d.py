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

def solve(a,b):
    len_a = len(a)
    len_b = len(b)
    if len_a > len_b:
        a, b = b, a
    # a is the shorter one
    for i in range(len(a)):
        j = 0
        in_same = True
        star_count = 0
        same_count = 0
        res = ''
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                i += 1
                j += 1
                same_count += 1
                res += a[i]
                in_same = True
            else:
                if in_same:
                    res += '*'
                    star_count += 1
                j += 1
                in_same = False
        if star_count <= same_count:
            return res
    return []

for _ in range(ii()):
    a = si()
    b = si()

    res = solve(a, b)
    print('Yes' if res else 'No')
    if res:
        print(*res)