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

def solve(n, m, grid):
    # n cols m rows

    # cols with ones
    rows_has_one_for_col = [[] for i in range(m)]

    # cols with zeroes
    rows_has_zero_for_col = [[] for i in range(m)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                rows_has_one_for_col[j].append(i)
            else:
                rows_has_zero_for_col[j].append(i)
    
    sums = [sum(i) for i in grid]
    if sum(sums) % n != 0:
        return -1
    target = sum(sums) // n

    # print(rows_has_one_for_col)
    # print(rows_has_zero_for_col)
 
    res = []
    # for each col
    for i in range(m):
        one_rows = rows_has_one_for_col[i]
        zero_rows = rows_has_zero_for_col[i]

        # sort rows with more ones
        one_rows.sort(key=lambda r: -sums[r])

        one_row_index = 0
        zero_row_index = 0
        while one_row_index < len(one_rows) and sums[one_rows[one_row_index]] > target:
            if zero_row_index >= len(zero_rows): 
                break
            
            if sums[zero_rows[zero_row_index]] < target:
                res.append([one_rows[one_row_index]+1, zero_rows[zero_row_index]+1, i+1])
                sums[zero_rows[zero_row_index]] += 1
                sums[one_rows[one_row_index]] -= 1
                one_row_index += 1
            zero_row_index += 1

    return res

for _ in range(ii()):
    n, m = ti()
    grid = [[0] * m for _ in range(n)]
    for r in range(n):
        nums = li()
        for c in range(m):
            grid[r][c] = nums[c]

    res = solve(n, m, grid)
    if res == -1:
        print(-1)
    else:
        print(len(res))
        for row in res:
            print(*row)