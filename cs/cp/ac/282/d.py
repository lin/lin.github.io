from sys import stdin
from tokenize import group
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

def bfs(node):
    levels = []
    q = deque([(node, 0)])
    seen.add(node)
    while q:
        curr, level = q.popleft()
        if len(levels) == level:
            levels.append(set())
        levels[level].add(curr)
        for nei in graph[curr]:
            if nei in levels[level]:
                return -1
            if nei not in seen:
                seen.add(nei)
                q.append((nei, level+1))

    res = [0, 0]
    for i in range(len(levels)):
        if i % 2 == 0:
            res[0] += len(levels[i])
        else:
            res[1] += len(levels[i])
    return res

n, m = ti()
edges = []
for _ in range(m):
    edges.append(ti())

graph = defaultdict(set)
for s, e in edges:
    graph[s].add(e)
    graph[e].add(s)

res = n * (n - 1) // 2  - m # C_n^2 - m
seen = set()
for i in range(1, n+1):
    if i not in seen:
        group_res = bfs(i)
        if group_res == -1:
            print(0)
            exit()
        b, w = group_res
        res -= b* (b-1)//2 + w*(w-1)//2
print(res)
