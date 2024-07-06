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

def get_aver(arr):
    res = 0
    count = 0
    for num in arr[::-1]:
        if num == 0:
            count += 1
        else:
            res += count
    return res

def solve(n, nums):
    if n == 1:
        return 0

    first_zero = None
    last_one = None
    for i, num in enumerate(nums):
        if num == 0 and first_zero == None:
            first_zero = i
        if num == 1:
            last_one = i
    
    res = get_aver(nums)
    if first_zero != None:
        nums[first_zero] = 1
        res = max(res, get_aver(nums))
        nums[first_zero] = 0

    if last_one != None:
        nums[last_one] = 0
        res = max(res, get_aver(nums))
        nums[last_one] = 1
    return res

T = int(input())
for _ in range(T):
    n = int(input())
    # m, s = tuple(map(int, input().split(' ')))
    nums = list(map(int, input().split(' '))) # list of nums
    # s = input().strip()
    # words = [w.strip() for w in input().split(' ')]

    print(solve(n, nums))
    # print("YES" if solve(n) else "NO")