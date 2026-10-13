from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, defaultdict, deque

n, Q = map(int, input().split())

graph = defaultdict(set)
degrees = [0] * n
cnt = n
# O(Q)
for i in range(Q):
    q = list(map(int, input().split()))

    # O(1)
    if q[0] == 1:
        _, u, v = q
        u-=1
        v-=1
        graph[u].add(v)
        graph[v].add(u)
        if not degrees[v]:
            cnt -= 1
        if not degrees[u]:
            cnt -= 1
        degrees[u] += 1
        degrees[v] += 1
    else:
        _, u = q
        u-=1
        if degrees[u] != 0:
            cnt += 1
        degrees[u] = 0
        # Can't be larger than Q
        for neigh in graph[u]:
            degrees[neigh] -= 1
            graph[neigh].remove(u)
            if degrees[neigh] == 0:
                cnt += 1
        graph[u] = set()

    print(cnt)
