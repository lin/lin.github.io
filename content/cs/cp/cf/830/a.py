from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

dir4 = [(-1,0),(0,1),(1,0),(0,-1)]
dir8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

# 3 6 9
# 1 2 3
# 5 10 15 20
# 1 2 3 4
# 120 60 80 40 80
# 1, 2, 1, 4, 5
# 150 90 180 120 60 30
# 1, 2, 3, 4, 5, 6
# 2 4 6 9 12 18
# 1, 2, 3, 1, 1, 6 
# 30 60 90 120 125 125
# 1, 2, 3, 4, 5, 1


def solve(n, nums):
    pgcd = 0
    for num in nums:
        pgcd = gcd(pgcd, num)
    if pgcd == 1:
        return 0
    
    if gcd(pgcd, gcd(nums[-1], n)) == 1:
        return 1
    if gcd(pgcd, gcd(nums[-2], n - 1)) == 1:
        return 2

    return 1 + 2
        
T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split(' '))) # list of nums

    print(solve(n, nums))