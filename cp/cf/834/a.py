from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

dir4 = [(-1,0),(0,1),(1,0),(0,-1)]
dir8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

def solve(s):
    n = len(s)
    if s[0] == "Y":
        sub = "Yes" * ceil(n / 3)
        return sub[:n] == s

    elif s[0] == 'e':
        sub = "esY" * ceil(n / 3)
        return sub[:n] == s

    elif s[0] == 's':
        sub = "sYe" * ceil(n / 3)
        return sub[:n] == s

    return False

T = int(input())
for _ in range(T):
    # n = int(input())
    s = input().strip()

    print("YES" if solve(s) else "NO")