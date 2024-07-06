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
    if a[0] == b[0]:
        return a[0] + '*'
    if a[-1] == b[-1]:
        return '*' + a[-1]
    
    for i in range(len(a)-1):
        pattern = a[i:i+2]
        if pattern in b:
            return '*' + pattern + '*'

    return ''

for _ in range(ii()):
    a = si()
    b = si()

    res = solve(a, b)
    print('Yes' if res else 'No')
    if res:
        print(res)