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

def solve(n,m,guests,tables):
    count = Counter(guests)
    # count value desc
    heap = [-v for v in count.values()]
    heapify(heap)
    tables.sort(reverse=True)

    res = 0
    for cap in tables:
        if heap:
            curr_guest_count = -heappop(heap)
            if curr_guest_count <= cap:
                res += curr_guest_count
            else:
                res += cap
                heappush(heap, cap - curr_guest_count)
    
    return res



for _ in range(ii()):
    #n = ii()
    n, m = ti()
    #s = si()
    guests = li()
    tables = li()

    res = solve(n,m,guests,tables)
    print(res)
    # print(*res)
    # print("YES" if res else "NO")