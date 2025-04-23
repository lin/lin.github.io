from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))

    max_l = []
    max_v = -inf
    for i in range(n):
        max_v = max(max_v, A[i] + (i+1))
        max_l.append(max_v)

    max_r = []
    max_v = -inf
    for i in range(n-1, -1, -1):
        max_v = max(max_v, A[i] - (i+1))
        max_r.append(max_v)
    max_r = max_r[::-1]

    res = -inf
    for i in range(1, n-1):
        curr = A[i] + max_l[i-1] + max_r[i+1]
        res = max(res, curr)

    print(res)
