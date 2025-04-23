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
s = si()
#nums = li()

seen =set([(0,0)])
x = 0
y = 0
is_yes = False
for ch in s:

    if ch == 'R':
        x += 1
    elif ch  == 'L':
        x -= 1
    elif ch =='U':
        y += 1
    else:
        y -= 1

    if (x, y) in seen:
        is_yes = True
        print("Yes")
        break
    seen.add((x,y))

if not is_yes:
    print("No")
# print(res)
# print(*res)
# print("YES" if res else "NO")