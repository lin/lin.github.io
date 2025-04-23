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


def solve(a, b):
    if a == b:
        return str(a) # right

    len_a = len(str(a))
    len_b = len(str(b))
    
    # 23456 2345
    if len_b > len_a:
        return '9' * len_a # right
    
    if len_a == 1:
        return str(a) # right

    first_a = str(a)[0]
    first_b = str(b)[0]

    if int(first_b) - int(first_a) > 1:
        return str(int(first_a) + 1) * len_a  # right
    
    next_a = int(str(a)[1])
    next_b = int(str(b)[1])

    cand = []

    # 33333
    if a <= int(first_a * len_a) <= b:
        cand.append(first_a * len_a)

    # 44444
    if a <= int(first_b * len_b) <= b:
        cand.append(first_b * len_b)

    # 34444 / 32222
    if a <= int(first_a + str(next_a) * (len_a-1)) <= b:
        cand.append(first_a + str(next_a) * (len_a-1))
    
    # 42222 / 45555
    if a <= int(first_b + str(next_b) * (len_a-1)) <= b:
        cand.append(first_b + str(next_b) * (len_a-1))

    # 40000
    if a <= int(first_b + '0' * (len_a - 1)) <= b:
        cand.append(first_b + '0' * (len_a - 1))

    # 30000
    if a <= int(first_a + '0' * (len_a - 1)) <= b:
        cand.append(first_a + '0' * (len_a - 1))
    
    # 49999
    if a <= int(first_a + '9' * (len_a - 1)) <= b:
        cand.append(first_a + '9' * (len_a - 1))
    
    # 39999
    if a <= int(first_a + '9' * (len_a - 1)) <= b:
        cand.append(first_a + '9' * (len_a - 1))
    
    # 34444
    if next_a != 9 and a <= int(first_a + str(next_a + 1)* (len_b-1)) <= b:
        cand.append(first_a + str(next_a + 1)* (len_b-1))

    # 42222
    if next_b != 0 and a <= int(first_b + str(next_b - 1)* (len_b-1)) <= b:
        cand.append(first_b + str(next_b - 1)* (len_b-1))

    # print(cand)
    min_cand, min_val = None, inf
    for c in cand:
        d = abs(int(c[0]) - int(c[1]))
        if d < min_val:
            min_val = d
            min_cand = c
        
    return min_cand or a

for _ in range(ii()):
    a, b = ti()

    res = solve(a,b)
    print(res)