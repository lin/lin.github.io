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
    n = ii()

    A = []
    B = []
    for _ in range(n):
        a, b = ti()
        A.append(a)
        B.append(b)
    
    gcd_ab = A[0] * B[0]
    lcm_b = B[0]

    res = 1
    for i in range(1, n):
        a, b = A[i], B[i]
        lcm_b = lcm(lcm_b, b)
        gcd_ab = gcd(gcd_ab, a * b)
        
        if gcd_ab % lcm_b != 0:
            res += 1
            gcd_ab = a * b
            lcm_b = b
        
    print(res)

