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

def solve(n, nums):
    nums_with_index = [(num, i) for i, num in enumerate(nums)]
    nums_with_index.sort()
    #print(nums_with_index)
    min_val = nums_with_index[0][0]
    res = []
    for num, i in nums_with_index:
        #print(num, i, min_val)
        if num > min_val:
            k = ceil(num / min_val)
            res.append((i, k*min_val - num))
            min_val *= k
        elif num < min_val:
            res.append((i, min_val - num))
    #print(*res)
    return res

for _ in range(ii()):
    n = ii()
    #a, b, c = ti()
    nums = li()

    res = solve(n, nums)
    print(len(res))
    for i, val in res:
        print(i + 1, val)
    #print(res)
    # print(*res)
    # print("YES" if res else "NO")