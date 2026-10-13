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

for _ in range(ii()):
    n = ii()
    
    no_i_lots_j = [[[] for _ in range(3)] for _ in range(3)]

    for index in range(1, n+1):
        count = [0, 0, 0]
        for ch in si():
            count[0] += 1 if ch == 'w' else 0
            count[1] += 1 if ch == 'i' else 0
            count[2] += 1 if ch == 'n' else 0

        j = count.index(max(count))
        for i, c in enumerate(count):
            if c == 0:
                no_i_lots_j[i][j].append(index)

    res = []
    for i in range(3):
        for j in range(i, 3):
            while no_i_lots_j[i][j] and no_i_lots_j[j][i]:
                res.append([no_i_lots_j[i][j].pop(), 'win'[j], no_i_lots_j[j][i].pop(), 'win'[i]])

    # 211 100 022
    if no_i_lots_j[0][1]:
        for i in range(len(no_i_lots_j[0][1])):
            res.append([no_i_lots_j[0][1][i], 'i', no_i_lots_j[2][0][i], 'w'])

        for i in range(len(no_i_lots_j[1][2])):
            res.append([no_i_lots_j[1][2][i], 'n', no_i_lots_j[2][0][i], 'i'])

    # 011 002 112
    elif no_i_lots_j[0][2]:
        for i in range(len(no_i_lots_j[0][2])):
            res.append([no_i_lots_j[0][2][i], 'n', no_i_lots_j[1][0][i], 'w'])
        for i in range(len(no_i_lots_j[2][1])):
            res.append([no_i_lots_j[2][1][i], 'i', no_i_lots_j[1][0][i], 'n'])

    print(len(res))
    for x in res:
        print(*x)