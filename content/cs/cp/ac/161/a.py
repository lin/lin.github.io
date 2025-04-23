from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n = int(input())
A = list(map(int, input().split()))

A.sort()
res = [0] * n
for i in range(0, n, 2):
    res[i] = A[i//2]
for i in range(1, n, 2):
    res[i] = A[n//2+i//2+1]

# print(*res)
valid = True
for i in range(1, n, 2):
    if res[i] <= res[i-1] or res[i] <= res[i+1]:
        valid=False
        break

print('Yes' if valid else 'No')