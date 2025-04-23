from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

A = list(map(int, input().split()))

res = 0
for i in range(64):
    res += A[i] * 2**i

print(res)