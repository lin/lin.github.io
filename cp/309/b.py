from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n = int(input())

s = []
res = []
for _ in range(n):
    s.append(input().strip())
    res.append([ch for ch in s[-1]])

# top
for i in range(n-1):
    res[0][i+1] = s[0][i]
# right
for i in range(n-1):
    res[i+1][-1] = s[i][-1]
# bottom
for i in range(n-1, 0, -1):
    res[-1][i-1] = s[-1][i]
# left
for i in range(n-1, 0, -1):
    res[i-1][0] = s[i][0]

for r in res:
    print(''.join(r))
