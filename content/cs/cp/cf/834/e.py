from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop, heapify
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

dir4 = [(-1,0),(0,1),(1,0),(0,-1)]
dir8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

def bgg(n, h, nums):
    heapify(nums)    
    green = 2
    blue = 1

    res = 0
    while h > 0 and nums:
        if h <= nums[0]:
            if blue > 0:
                blue -= 1
                h *= 3
            elif green > 0:
                green -= 1
                h *= 2
            else:
                break
        else:
            ast = heappop(nums)
            h += ast // 2
            res += 1
    return res

def ggb(n, h, nums):
    heapify(nums)    
    green = 2
    blue = 1

    res = 0
    while h > 0 and nums:
        if h <= nums[0]:
            if green > 0:
                green -= 1
                h *= 2
            elif blue > 0:
                blue -= 1
                h *= 3
            else:
                break
        else:
            ast = heappop(nums)
            h += ast // 2
            res += 1
    return res

def gbg(n, h, nums):
    heapify(nums)    
    green = 2
    blue = 1

    res = 0
    while h > 0 and nums:
        if h <= nums[0]:
            if green == 2:
                green -= 1
                h *= 2
            elif blue > 0:
                blue -= 1
                h *= 3
            elif green > 0:
                green -= 1
                h *= 2
            else:
                break
        else:
            ast = heappop(nums)
            h += ast // 2
            res += 1
    return res


def solve(n, h, nums):
    heapify(nums)    
    green = 2
    blue = 1

    res = 0
    while h > 0 and nums:
        if h <= nums[0]:
            if blue > 0:
                blue -= 1
                h *= 3
            elif green > 0:
                green -= 1
                h *= 2
            else:
                break
        else:
            ast = heappop(nums)
            h += ast // 2
            res += 1
    return res

T = int(input())
for _ in range(T):
    n, h = tuple(map(int, input().split(' ')))
    nums = list(map(int, input().split(' '))) # list of nums
    # print(ggb(n, h, nums), gbg(n, h, nums), bgg(n, h, nums))
    print(max(ggb(n, h, nums[:]), gbg(n, h, nums[:]), bgg(n, h, nums[:])))