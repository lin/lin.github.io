from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
from functools import lru_cache
from itertools import accumulate, permutations
import math

T = int(input())
for _ in range(T):
    n = int(input())
    s = input().strip()

    changes = []
    score = 0
    for i in range(n):
        l, r = i, n - 1 - i
        if s[i] == 'L':
            changes.append(max(r - l, 0))
            score += l
        else:
            changes.append(max(l - r, 0))
            score += r
            
    changes.sort(reverse=True)
    res = []
    for i in range(n):
        score += changes[i]
        res.append(score)
    
    print(*res)

