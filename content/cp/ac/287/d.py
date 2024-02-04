from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

# d4 = [(-1,0),(0,1),(1,0),(0,-1)]
# d8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

n, m = ti()
edges = defaultdict(list)
for _ in range(m):
    s, e = ti()
    edges[s].append(e)
    edges[e].append(s)
#print(edges)

if n != m+1:
    print('No')
    exit()

root = None
for key in edges:
    if len(edges[key]) == 1:
        root = key
        break

if not root:
    print('No')
    exit()

curr, parent = root, None
k = 0
while curr:
    children = edges[curr]
    if len(children) > 2:
        print("No")
        exit()
    # if len(children) == 1:
    #     curr = None
    # elif len(children) == 2:
    prev = curr
    for child in children:
        if child != parent:
            curr, parent = child, curr
            k += 1
            break
    #print(prev, curr, parent)
    if prev == curr:
        k+=1
        break
#print(k)
if k == n:
    print("Yes")
else:
    print("No")