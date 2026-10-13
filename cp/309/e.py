from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n, m = map(int, input().split())
P = list(map(int, input().split()))

max_dict = defaultdict(lambda:-inf)
for _ in range(m):
    x, y = map(int, input().split())
    max_dict[x] = max(max_dict[x], y)

tree = defaultdict(list)
for i in range(n-1):
    tree[P[i]].append(i + 2)

q = deque([(1, 0, max_dict[1])])

seen = set([1])

cnt = 0
while q:
    node, level, mx_level = q.popleft()

    if level <= mx_level:
        cnt += 1

    for child in tree[node]:
        if child not in seen:
            seen.add(child)
            q.append((child, level+1, max(mx_level, max_dict[child] + level+1)))

print(cnt)