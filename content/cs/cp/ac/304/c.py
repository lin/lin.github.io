from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n, d = map(int, input().split())

root = [i for i in range(n)]

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(x, y):
    rx, ry = find(x), find(y)
    root[max(rx, ry)] = min(rx, ry)

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    x1, y1 = arr[i]
    for j in range(i+1, n):
        x2, y2 = arr[j]
        dist = (x1-x2)**2 + (y1-y2)**2
        if dist <= d**2:
            union(i, j)

# root = [find(i) for i in range(n)]

for i in range(n):
    if find(i) == 0:
        print('Yes')
    else:
        print('No')




