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

MOD = 998244353

n, m = ti()

root = [i for i in range(n)]
        
def find(x):
    if x == root[x]:
        return x
    root[x]= find(root[x])
    return root[x]

cnt = [0]
def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        remained_root, changed_root =  min(root_x, root_y), max(root_x, root_y)
        root[changed_root] = remained_root
    else:
        cnt[0] += 1


for i in range(m):
    a, b, c, d = tuple(input().split(' '))
    union(int(a)-1, int(c)-1)

groups = len(Counter([find(i) for i in range(n)]))

print(cnt[0], groups- cnt[0])
