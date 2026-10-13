from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right

n = int(input())

graph = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dist = defaultdict(int)
height = defaultdict(int)

def dfs1(cur, par):
    for u in graph[cur]:
        if (u != par):
            dfs1(u, cur)
            height[cur] = max(height[cur], height[u])
    height[cur] += 1

def dfs2(cur, par):
    max1 = 0
    max2 = 0

    for u in graph[cur]:
        if (u != par):
            if (height[u] >= max1):
                max2 = max1
                max1 = height[u]
            elif (height[u] > max2):
                max2 = height[u]

    for u in graph[cur]:
        if (u != par):
            if (max1 == height[u]):
                dist[u] = 1 + max(1 + max2, dist[cur])
            else:
                dist[u] = 1 + max(1 + max1, dist[cur])
            dfs2(u, cur)

dfs1(1, 0)
dfs2(1, 0)

max_dist = []
for i in range(1, n+1):
    max_dist.append(max(dist[i], height[i]) - 1)

max_dist.sort()

res = []
for k in range(n):
    k += 1
    i = bisect_left(max_dist, k)
    res.append(i + (1 if i != n else 0))

print(*res)