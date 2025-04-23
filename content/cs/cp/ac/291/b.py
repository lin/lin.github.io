from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations, combinations
from math import *

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

#for _ in range(ii()):
n = ii()
#n, m = ti()
#s = si()
nums = li()
nums.sort()
print(sum(nums[n:-n])/(3*n))

# print(res)
# print(*res)
# print("YES" if res else "NO")