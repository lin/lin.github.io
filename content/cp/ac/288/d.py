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

N, K = map(int, input().split())
A = list(map(int, input().split()))
if N % K > 0:
    for _ in range(N - N % K):
        A.append(0)

accu_sums = [[0] for _ in range(K)]
for idx, value in enumerate(A):
    accu_sums[idx % K].append(accu_sums[idx % K][-1] + value)
    
for _ in range(int(input())):
    left, right = map(lambda n: int(n)-1, input().split())
    accu_sum_partial = set()
    for diff in range(K):
        if (left-diff) % K == 0:
            start_idx = (left-diff) // K
        else:
            start_idx = (left-diff) // K + 1

        end_idx = (right-diff) // K + 1

        accu_sum_partial.add(
            accu_sums[diff][end_idx] - accu_sums[diff][start_idx])

    if len(accu_sum_partial) == 1:
        print("Yes")
    else:
        print("No")