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

def solve(l, r, x, a, b):
    
    if a == b:
        return 0

    if a > b:
        return solve(l, r, x, b, a)

    if b - a >= x:
        return 1

    la, ra = a - l, r - a
    lb, rb = b - l, r - b

    lr = r - l

    if lr < x:
        return -1
    
    if la < x and ra < x:
        return -1

    if lb < x and rb < x:
        return -1


    if ra >= x and rb >= x:
        return 2
    
    if la >= x and lb >= x:
        return 2

    if ra >= x and lb >= x:
        return 3

    if la >= x and rb >= x:
        return 3
    
    return -1

T = int(input())
for _ in range(T):
    l, r, x = tuple(map(int, input().split(' ')))
    a, b = tuple(map(int, input().split(' ')))
    # print(solve(n))

    print(solve(l, r, x, a, b))