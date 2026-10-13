from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n, m = map(int, input().split())

    data = []
    for i in range(n):
        data.append([m*i + j + 1 for j in range(m)])

    res = [None] * n
    for i in range(n//2):
        res[i*2] = data[n//2 + i]
        res[i*2 + 1] = data[i]
    if n % 2 == 1:
        res[-1] = data[-1]

    for r in res:
        print(*r)