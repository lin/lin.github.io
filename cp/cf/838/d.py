from sys import stdin
from sys import stdout

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

for _ in range(ii()):
    n = ii()
    
    first_loop = []
    for i in range(1, n):
        print('?', 1, i+1)
        stdout.flush()

        response = int(input())
        first_loop.append(response)

    if len(set(first_loop)) == n - 1:
        print('!', 1, 1)
        stdout.flush()

        response = int(input())
        if response == 1:
            continue
        else:
            break
    
    max_val = max(first_loop)
    second_loop_indexes = []
    for i in range(n):
        if first_loop[i] == max_val:
            second_loop_indexes.append(i + 1)
    
    if len(second_loop_indexes) == 1:
        print('!', second_loop_indexes[0], second_loop_indexes[0])
        stdout.flush()

        response = int(input())
        if response == 1:
            continue
        else:
            break

    second_loop = []
    for i in second_loop_indexes[1:]:
        print('!', second_loop_indexes[0], second_loop_indexes[i])
        stdout.flush()

        second_loop.append(int(input()))
    
    max_index = second_loop.index(max(second_loop))
    print('!', second_loop_indexes[0], second_loop_indexes[max_index])
    stdout.flush()

    response = int(input())
    if response == 1:
        continue
    else:
        break


    