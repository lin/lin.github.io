from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

dir4 = [(-1,0),(0,1),(1,0),(0,-1)]
dir8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

def solve(n, target, days, coins):
    # max_val = max(coins)
    # k = 0 will always work
    # if days * max_val < target:
    #     return 'Impossible'

    # Infinity check
    coins.sort(reverse=True)
    psum = [0]
    for coin in coins:
        psum.append(psum[-1] + coin)

    # if psum[min(days, n)] >= target:
    #     return 'Infinity'


    def check(k):
        size = k + 1
        remain = days % size
        total = psum[min(size, n)] * (days // size) # psum
        total += psum[min(remain, n)]
        # print(k, total)
        return total < target

    left = 0
    right = days + 1

    while left < right:
        mid = (left + right) // 2

        if check(mid):
            right = mid
        else:
            left = mid + 1
        
    if right == days + 1:
        return 'Infinity'
    if right == 0:
        return 'Impossible'
    return right - 1 

T = int(input())
for _ in range(T):
    n, c, d = tuple(map(int, input().split(' ')))
    nums = list(map(int, input().split(' '))) # list of nums

    print(solve(n, c, d, nums))