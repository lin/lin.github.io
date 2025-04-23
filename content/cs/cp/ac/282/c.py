from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

n = ii()
s = si()

enclosed = False
res = []
for i in range(n):
    if s[i] == '"':
        enclosed = not enclosed
        res.append(s[i])
    elif s[i] == ',':
        if enclosed:
            res.append(s[i])
        else:
            res.append('.')
    else:
        res.append(s[i])
        
print(''.join(res))