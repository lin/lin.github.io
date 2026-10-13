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

def solve(n, m, times):
    sorted_times = sorted(times)

    time_used = 0
    wins_count = 0
    for i in range(n):
        time_used += sorted_times[i]
        if time_used <= m:
            wins_count = i + 1
    
    if wins_count == 0 or wins_count == n:
        return n - wins_count + 1
    
    rank = n - wins_count
    rest = sorted(times[:wins_count] + times[wins_count+1:])
 
    if sum(rest[:wins_count-1]) + times[wins_count] > m: 
        rank += 1

    return rank

for _ in range(ii()):
    #n = ii()
    n, m = ti()
    #s = si()
    nums = li()

    res = solve(n, m, nums)
    print(res)
    # print(*res)
    # print("YES" if res else "NO")