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

# smallest prime factor
# spf
# https://www.geeksforgeeks.org/prime-factorization-using-sieve-olog-n-multiple-queries/
sieve = [0 for i in range(10 ** 7 + 10)]
for i in range(2, 10 ** 7 + 10):
    if sieve[i] == 0:
        sieve[i] = i
        for j in range(i * i, 10 ** 7 + 10, i):
            sieve[j] = i

def factorization(x):
    res = set()
    while x != 1:
        res.add(sieve[x])
        x = x // sieve[x]
    return res

def solve(x, y):
    if gcd(x,y)!=1:
        return 0
    if y - x ==1:
        return -1

    diff = y - x
    res = 1000000000

    factors = factorization(diff)
    for factor in factors:
        res = min(res, factor - x % factor)

    return res if res != 1000000000 else -1

for _ in range(ii()):

    x, y = ti()

    res = solve(x,y)
    print(res)