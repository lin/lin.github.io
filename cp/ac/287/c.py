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

s = si()
t = si()

postfix = s[len(s)-len(t):]
k = 0
for i in range(len(t)):
    if (postfix[~i] == '?' or t[~i] == '?') or postfix[~i] == t[~i]:
        k+=1
    else:
        break

print('Yes' if k == len(t) else 'No')

prefix = True
for i in range(len(t)):
    prefix = prefix and ((s[i] == '?' or t[i] == '?') or s[i] == t[i])
    if prefix and i >= len(t) - k - 1:
        print("Yes")
    else:
        print("No")