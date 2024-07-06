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

def get_power(x):
    p2, p5 = 0, 0
    while x % 2 == 0 or x % 5 == 0:
        if x % 2 == 0:
            p2 += 1
            x //= 2
        if x % 5 == 0:
            p5 += 1
            x //= 5
    return [p2, p5]

def solve(n, m):
    c2, c5 = get_power(n)

    if c2 == c5:
        c2, c5 = 0, 0
    elif c2 > c5:
        c2, c5  = c2 - c5, 0
    else:
        c2, c5 = 0, c5 - c2

    k = 1
    while k < m:
        if c5 > 0 and k * 2 <= m:
            k *= 2
            c5 -= 1
        elif c2 > 0 and k * 5 <= m:
            k *= 5
            c2 -= 1
        elif k * 10 <= m:
            k *= 10
        elif (n*k) %10 == 0:
            k = m // k * k
            break
        else:
            break

    if k == 1:
        return n * m
    
    return n * k



T = int(input())
for _ in range(T):
    n, m = tuple(map(int, input().split(' ')))

    print(solve(n, m))