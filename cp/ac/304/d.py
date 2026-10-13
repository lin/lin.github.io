from bisect import bisect
from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

w, h = map(int, input().split())
n = int(input())

sb = []
for _ in range(n):
    sb.append(list(map(int, input().split())))


a = int(input())
A = list(map(int, input().split()))
A.sort()

b = int(input())
B = list(map(int, input().split()))
B.sort()

cnt = Counter()

for x, y in sb:
    ai = bisect(A, x)
    bi = bisect(B, y)
    cnt[(ai, bi)] += 1

vals = cnt.values()
mx, mn = max(vals), min(vals)
if len(cnt) != (a+1) *(b+1):
    mn = 0
print(mn, mx)





