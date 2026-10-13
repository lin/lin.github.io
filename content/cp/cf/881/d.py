from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())

    edges = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
    
    cnt = defaultdict(int)

    parent_map = {1: -1}
    levels_order = []
    seen  = set()
    q = deque([(1, -1)])
    while q:
        node, parent = q.popleft()
        levels_order.append(node)
        seen.add(node)

        for child in edges[node]:
            if child != parent and child not in seen:
                parent_map[child] = node
                q.append((child, node))
    
    for node in reversed(levels_order):
        if parent_map[node] != -1 and len(edges[node]) == 1:
            cnt[node] = 1
        else:
            for child in edges[node]:
                if child != parent_map[node]:
                    cnt[node] += cnt[child]
 
    q = int(input())
    for _ in range(q):
        x, y = map(int, input().split())
        print(cnt[x] * cnt[y])



