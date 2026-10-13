from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations, combinations
from math import *

# d4 = [(-1,0),(0,1),(1,0),(0,-1)]
# d8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

n = ii()
p = li()
q = li()

# same min between l and r
stack_p = []
stack_q = []

start = 0
for end in range(n):
    p_num = p[end]
    q_num = q[end]

    # mono increase stack
    while stack_p and stack_p[-1] > p_num:
        stack_p.pop()
    stack_p.append(p_num)

    while stack_q and stack_q[-1] > q_num:
        stack_q.pop()
    stack_q.append(q_num)


