from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations, combinations
from math import *

# d4 = [(-1,0),(0,1),(1,0),(0,-1)]
# d8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

def solve(n, nums):
    next_greater = [-1] * n
    stack = []
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            next_greater[stack.pop()] = i
        stack.append(i)

    next_smaller = [-1] * n
    stack = []
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] > num:
            next_smaller[stack.pop()] = i
        stack.append(i)

    prev_greater = [n] * n
    stack = []
    for i in range(n - 1, -1, -1):
        num = nums[i]
        while stack and nums[stack[-1]] < num:
            prev_greater[stack.pop()] = i
        stack.append(i)

    prev_smaller = [n] * n
    stack = []
    for i in range(n - 1, -1, -1):
        num = nums[i]
        while stack and nums[stack[-1]] > num:
            prev_smaller[stack.pop()] = i
        stack.append(i)

    left = 0
    right = n - 1
    while left < right:
        l, r = left, right
        left_condition = next_smaller[l] == -1 or next_greater[l] == -1 or next_smaller[l] >= r or next_greater[l] >= r
        right_condition = prev_smaller[r] == n or prev_greater[r] == n or prev_greater[r] <= l or prev_smaller[r] <= l
        if left_condition:
            left += 1
        if right_condition:
            right -= 1
        if not left_condition and not right_condition:
            return [left + 1, right + 1]

    return []

for _ in range(ii()):
    n = ii()
    nums = li()

    res = solve(n, nums)
    if not res:
        print(-1)
    else:
        print(*res)
    # print(*res)
    # print("YES" if res else "NO")