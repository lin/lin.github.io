from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations, combinations
from math import *

# d4 = [(-1,0),(0,1),(1,0),(0,-1)]
# d8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

n, m = ti()
edges = []
for _ in range(m):
    edges.append(ti())
# graph = defaultdict(list)
# for _ in range(m):
#     s, e = ti()
#     graph[s].append(e)
#     graph[e].append(s)

root = [i for i in range(n + 1)]
        
def find(x):
    if x == root[x]:
        return x
    root[x]= find(root[x])
    return root[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    
    if root_x == root_y:
        return False

    if root_x < root_y:
        root[root_y] = root_x
    else:
        root[root_x] = root_y
        
    return True

res = 0
for s,t in edges:
    if not union(s, t):
        res += 1

print(res)