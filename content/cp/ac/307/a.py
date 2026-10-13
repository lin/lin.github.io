from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n = int(input())
A = list(map(int, input().split()))

res = []
for i in range(n):
    res.append(sum(A[i*7:(i+1)*7]))

print(*res)