from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())

    edges = []
    for _ in range(n-1):
        u, v =  map(int, input().split())
        edges.append((u, v))
    
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    tree = defaultdict(list)
    parents = {}
    parents[1] = -1

    q = deque([(1, -1)])

    while q:
        node, parent = q.popleft()
        for neigh in graph[node]:
            if neigh != parent:
                parents[neigh] = node
                q.append((neigh, node))

    tree = defaultdict(list)

    seen = set()
    for u, v in edges:
        if parents[u] == v:
            u, v = v, u
        if u in seen:
            tree[parents[u]].append(v)
            parents[v] = parents[u]
        else:
            tree[u].append(v)
        seen.add(v)

    q = deque([(1, 0)])
 
    res = 1
    seen = set([1])
    while q:
        node, level = q.popleft()
 
        res = max(res, level)
 
        for child in tree[node]:
            if child not in seen:
                q.append((child, level+1))
                seen.add(child)
        
    print(res)



