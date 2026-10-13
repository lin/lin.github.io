from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

dir4 = [(-1,0),(0,1),(1,0),(0,-1)]
dir8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

def solve(n, a, b, graph):
    possibles = set([0])
    q = deque([(a, 0)])
    seen = set([a])
    while q:
        node, val = q.popleft()
        for neigh, weight in graph[node]:
            if neigh not in seen:
                if neigh == b:
                    if val ^ weight == 0:
                        return True
                else:
                    possibles.add(val ^ weight)
                    seen.add(neigh)
                    q.append((neigh, val ^ weight))

    q = deque([(b, 0)])
    seen = set([b])
    while q:
        node, val = q.popleft()
        for neigh, weight in graph[node]:
            if neigh not in seen:
                if val ^ weight in possibles:
                    return True
                seen.add(neigh)
                q.append((neigh, val ^ weight))

    return False

T = int(input())
for _ in range(T):
    n, a, b = tuple(map(int, input().split(' ')))

    graph = defaultdict(list)
    for _ in range(n - 1):
        u, v, w = tuple(map(int, input().split(' ')))
        graph[u].append((v, w))
        graph[v].append((u, w))
    # print(*res)
    print("YES" if solve(n, a, b, graph) else "NO")