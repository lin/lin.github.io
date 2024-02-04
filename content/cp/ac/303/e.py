from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n = int(input())
degrees = [0] * (n+1)
for _ in range(n-1):
    u, v = map(int, input().split())
    degrees[u] +=1
    degrees[v] +=1

res = []
remain = n # remain edges
for i in range(n):
    if degrees[i+1] > 2:
        res.append(degrees[i+1])
        remain -= degrees[i+1] + 1

for _ in range(remain//3):
    res.append(2)

res.sort()
print(*res)
