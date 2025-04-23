from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

# d4 = [(-1,0),(0,1),(1,0),(0,-1)]
# d8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

def solve(x):
    if x % 2 == 1:
        return []

    andstr = bin(x // 2)[2:] # a & b

    a = []
    b = []
    for i in range(len(andstr) + 1):
        and_ch = andstr[~i] if i < len(andstr) else '0'
        xor_ch = andstr[~(i-1)] if i > 0 else '0'
        #print(and_ch, xor_ch)
        if and_ch == '1' and xor_ch == '1':
            return []
        if and_ch == '0' and xor_ch == '0':
            a.append('0')
            b.append('0')
        elif and_ch == '1' and xor_ch == '0':
            a.append('1')
            b.append('1')
        elif and_ch == '0' and xor_ch == '1':
            a.append('1')
            b.append('0')

    #print(''.join(a[::-1]), ''.join(b[::-1]))
    a_num = int(''.join(a[::-1]), 2)
    b_num = int(''.join(b[::-1]), 2)

    return [a_num, b_num]

for _ in range(ii()):
    x = ii()
    res = solve(x)
    if not res:
        print(-1)
    else:
        print(*res)