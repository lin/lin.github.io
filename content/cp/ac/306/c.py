from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n = int(input())
A = list(map(int, input().split()))

pos = defaultdict(list)

for i in range(3*n):
    pos[A[i]].append(i)

arr = []
for i in range(n):
    arr.append([pos[i+1][1], i+1])

arr.sort()
res = []
for p, x in arr:
    res.append(x)

print(*res)
