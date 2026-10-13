from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

d4 = [(-1,0),(0,1),(1,0),(0,-1)]
d8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

def find_a(s):
    for i in range(1, len(s)-1):
        if s[i] == 'a':
            return i
    return -1

def solve(s):
    n = len(s)
    first = s[0]
    last = s[-1]

    first_a = find_a(s)

    if first_a != -1:
        return [s[:first_a], 'a', s[first_a+1:]]
    
    return [first, s[1:-1], last]

for _ in range(ii()):
    s = si()

    res = solve(s)
    if not res:
        print(":(")
    else:
        print(*res)