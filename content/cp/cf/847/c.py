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

for _ in range(ii()):
    n = ii()

    data = []
    count = Counter()
    for _ in range(n):
        row = li()
        count[row[0]] += 1
        data.append(row)

    first_val = None
    for key in count:
        if count[key] == n-1:
            first_val = key
    
    for i in range(n):
        if data[i][0] != first_val:
            print(*([first_val] + data[i]))
            break