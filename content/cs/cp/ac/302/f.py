from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n, m = map(int, input().split())

dic = defaultdict(set)
ss = []

for i in range(n):
    k = int(input())
    s = set(map(int, input().split()))
    ss.append(s)
    for x in s:
        dic[x].add(i)

q = deque([(1, 0)])
seen = set([1])

while q:
    node, step = q.popleft()
    # which sets include node
    for i in dic[node]:
        for j in ss[i]:
            if j not in seen:
                if j == m:
                    print(step)
                    exit()
                q.append((j, step + 1))
                seen.add(j)

print(-1)