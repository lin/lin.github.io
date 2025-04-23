from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n, m = map(int, input().split())
A = list(map(int, input().split()))

a1, a2 = A[0], A[1]

A = A[2:]
A.sort()

res = inf
for i in range(n-m-2+1):
    curr = 0
    if a2 < A[i+m-1]:
        curr += A[i+m-1] - a2
    if  a1 > A[i]:
        curr += a1 - A[i]
    res = min(res, curr)

print(res)
