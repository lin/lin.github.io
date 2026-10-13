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

def solve(n, nums):
    # if -1 -1, total += 4
    # if 1, -1, or -1, 1, total += 0
    # if no -1, total -= 4

    last = None
    has_two = False
    has_one = False
    for i, num in enumerate(nums):
        if num == -1:
            has_one = True
            if last is not None and i - last == 1:
                has_two = True
            last = i
    total = sum(nums)

    if has_two:
        return total + 4
    if has_one:
        return total
    
    return total - 4

for _ in range(ii()):
    n = ii()
    #a, b, c = ti()
    #s = si()
    nums = li()

    res = solve(n, nums)
    print(res)
    # print(*res)
    # print("YES" if res else "NO")