from bisect import bisect_left, bisect_right
from collections import defaultdict
from sys import stdin
input = stdin.readline

from math import *

ii = lambda: int(input())
li = lambda: list(map(int, input().split()))
ti = lambda: map(int, input().split())
si = lambda: input().strip()

n, n1, n2 = ti()

starts = defaultdict(list)
ends = defaultdict(list)
gaps_psum = defaultdict(list)

curr = 0 # curr end position is the start of the next
for _ in range(n1):
    v, l = ti()

    # calc gap
    prev_end = ends[v][-1] if ends[v] else curr
    prev_psum = gaps_psum[v][-1] if gaps_psum[v] else 0
    gaps_psum[v].append(prev_psum + curr - prev_end)

    # save data
    starts[v].append(curr+1)
    ends[v].append(curr+l)
    curr=curr+l

res = 0
curr = 0
for _ in range(n2):
    v, l = ti()
    s, e = curr+1, curr+l
    curr = e
    if starts[v]:
        si = bisect_right(starts[v], s)
        ei = bisect_right(ends[v], e)

        gaps_len = gaps_psum[v][ei if ei != len(ends[v]) else ei-1] - gaps_psum[v][si-1]

        start_missing = starts[v][0] - s if si == 0 else 0
        start_missing -= max(s - ends[v][si-1]-1, 0)
        end_missing = e - ends[v][-1] if ei == len(ends[v]) else 0
        end_missing -= max(starts[v][ei-1]-e-1, 0)
        missing = gaps_len + start_missing + end_missing
        

        res += l - missing

print(res)

