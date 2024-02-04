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

def solve(n, x):

    def get_bits(num):
        bits = []
        i = 0
        while num:
            if num & 1:
                bits.append(i) 
            num >>= 1
            i += 1
        return bits
        
    n_bits = get_bits(n)

    dic = {n: n}
    curr = n
    for n_bit in n_bits:
        curr = curr & (curr - 1)
        val = curr | (1<<(n_bit+1))
        if val >= n:
            dic[curr] = val
    
    #print(dic)
    if x in dic:
        return dic[x]
    return -1

for _ in range(ii()):
    n, x = ti()
    res = solve(n, x)
    print(res)

# curr = 52
# for i in range(20):
#     curr &= 52 + i
#     print(curr, 52+i)