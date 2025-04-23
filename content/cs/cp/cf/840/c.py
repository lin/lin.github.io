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
        total = sum(nums)
        if n==2:
            return max(total, abs(nums[0]-nums[1])*2)
        if n==3:
            return max(total, nums[0]*3, nums[2]*3, abs(nums[0]-nums[1])*3, abs(nums[1]-nums[2])*3)

        return n*max(nums)

    for _ in range(ii()):
        n = ii()
        #a, b, c = ti()
        #s = si()
        nums = li()

        res = solve(n, nums)
        print(res)
        # print(*res)
        # print("YES" if res else "NO")