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

# def solve(n, nums):
#     return

# for _ in range(ii()):
# n = ii()
n, m = ti()
seen = set()
for _ in range(n):
    s = si()
    seen.add(s[3:])
res = 0
for _ in range(m):
    t = si()
    if t in seen:
        res += 1
print(res)

count = 0 # for
for _ in range(n):
    if si() == 'For':
        count += 1
if count > n // 2:
    print('Yes')
else:
    print('No')
    #a, b, c = ti()
    #s = si()
    #nums = li()

    # res = solve(n, nums)
    # print(res)
    # print(*res)
    # print("YES" if res else "NO")