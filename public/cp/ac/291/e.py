from curses.ascii import isupper
from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations, combinations
from math import *

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

n, m = ti()
indegree = [0] * n
graph = [[] for _ in range(n)]

reqs = []
for _ in range(m):
    s, e = ti()
    s, e = s-1, e-1
    reqs.append((s,e))
    indegree[e] += 1
    graph[s].append(e)

zero_q = [i for i in range(n) if indegree[i] == 0]

res = [None] * n
cnt = 1
while zero_q:
    if len(zero_q) != 1:
        print('No')
        exit()
    curr = zero_q.pop()
    res[curr] = cnt
    cnt += 1
    for e in graph[curr]:
        indegree[e] -= 1
        if indegree[e] == 0:
            zero_q.append(e)

print('Yes')
print(*res)