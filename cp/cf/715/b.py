# https://leetcode.com/problems/modify-graph-edge-weights/

from sys import stdin
input = stdin.readline

from math import *
from heapq import *
from collections import defaultdict, Counter, deque

n, m, target, src, dst = map(int, input().split())

MAX = target + 1
    
# it is easy to modify w
graph = [[-1] * n for _ in range(n)]
edges = []
for _ in range(m):
    u,v,w = map(int, input().split())
    graph[u][v]  = graph[v][u] = w
    edges.append([u,v,w])

inf_dist = defaultdict(lambda :inf)
inf_dist[src] = 0

heap = [(0, src)]
while heap:
    cost, node = heappop(heap)
    if inf_dist[node] < cost:
        continue
    for neigh, weight in enumerate(graph[node]):
        if weight !=-1 and weight != 0 and weight + cost < inf_dist[neigh]:
            inf_dist[neigh] = weight + cost
            heappush(heap, (weight + cost, neigh))

# normal dijkstra is better than modified graph
if inf_dist[dst] < target:
    print('No')
    exit()

if inf_dist[dst] == target:
    res = []
    for s,d,c in edges:
        res.append([s,d,(c if c else MAX)])

    print('Yes')
    for r in res:
        print(*r)
    exit()

# -1 as 1, and start from src
one_dist = defaultdict(lambda :inf)
one_dist[src] = 0

heap = [(0, src)]
prev = {}
while heap:
    cost, node = heappop(heap)
    if one_dist[node] < cost:
        continue
    for neigh, weight in enumerate(graph[node]):
        dist = (weight if weight else 1) + cost
        if weight != -1 and dist < one_dist[neigh]:
            one_dist[neigh] = dist
            prev[neigh] = node
            heappush(heap, (dist, neigh))

if one_dist[dst] > target:
    print('No')
    exit()


curr = dst
while curr != src:
    p = prev[curr]
    if not graph[curr][p]:
        if inf_dist[p] < target:
            graph[p][curr] = graph[curr][p] = target - inf_dist[p]
            break
        graph[p][curr] = graph[curr][p] = 1
    target -= graph[curr][p]
    curr = p

res = []
for s,d,_ in edges:
    res.append([s,d,(MAX if not graph[s][d] else graph[s][d])])
    
print('Yes')
for r in res:
    print(*r)