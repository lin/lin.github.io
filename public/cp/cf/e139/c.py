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

def solve(m, grid):
    #print(grid)
    def helper(r, c):
        if grid[r][c] == 0:
            return False

        while c < m - 1:
            # go same col first, then to next col
            if r == 0:
                if grid[1][c] == 1:
                    if grid[1][c+1] != 1:
                        return False
                    r, c = 1, c+1
                else:
                    if grid[0][c+1] != 1:
                        return False
                    r, c = 0, c+1
            else:
                if grid[0][c] == 1:
                    if grid[0][c+1] != 1:
                        return False
                    r, c = 0, c+1
                else:
                    if grid[1][c+1] != 1:
                        return False
                    r, c = 1, c+1

        return True

    return helper(0, 0) or helper(1, 0)

for _ in range(ii()):
    m = ii()

    grid = [[0]*m for _ in range(2)]
    # a, b, c = ti()
    s = si()
    for i in range(m):
        grid[0][i] = 0 if s[i] == 'W' else 1

    s = si()
    for i in range(m):
        grid[1][i] = 0 if s[i] == 'W' else 1

    res = solve(m, grid)
    # print(res)
    # print(*res)
    print("YES" if res else "NO")