from collections import deque
from sys import stdin
input = stdin.readline

from math import *

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()

n, qs = ti()

q = deque()
seen = set()
cnt = 0 # the most recently called
for _ in range(qs):
    event = li()
    if event[0] == 1:
        cnt += 1
        q.append(cnt)
    elif event[0] == 2:
        seen.add(event[1])
    else:
        while q and q[0] in seen:
            q.popleft()
        print(q[0])