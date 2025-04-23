from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n, m, h, k = map(int, input().split())
s = input().strip()

recovers = set()

for _ in range(m):
    recovers.add(tuple(map(int, input().split())))

valid = True
x, y = 0, 0

for ch in s:
    if ch == 'R':
        dx, dy = 1, 0
    elif ch == 'L':
        dx, dy = -1, 0
    elif ch == 'U':
        dx, dy = 0, 1
    elif ch == 'D':
        dx, dy = 0, -1
    # step one
    h -= 1
    x, y = x + dx, y + dy

    # step two
    if h < 0:
        valid = False

    if (x,y) in recovers and h < k:
        h = k
        recovers.remove((x,y))
    
print('Yes' if valid else 'No')