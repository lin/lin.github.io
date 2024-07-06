from bisect import *
from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque

n, m, d= map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()

mx = -1
for b in B:
    l = bisect_left(A, b-d)
    r = bisect_right(A, b+d)
    if l == r: # not exist
        continue
    curr = A[r-1] + b
    if mx < curr:
        mx = curr

print(mx)