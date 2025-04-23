from bisect import bisect_right
from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque
from bisect import *

n, q = map(int, input().split())
A = list(map(int, input().split()))

arr = []
prev = 0
p = -1
prev_start = -1
for i, a in enumerate(A):
    if a > prev:
        p += 1
        if prev_start != i-1:
            arr[-1] = 1
        arr.append(1)
        prev_start = i
    else:
        arr.append(0)
    prev = a
arr[-1] == 1

psum = [0]
for x in arr:
    psum.append(psum[-1] + x)
# print(arr)
# print(psum)
for _ in range(q):
    l, r = map(int, input().split())
    if l == r:
        print(1)
        continue

    res = int(arr[l-1]==0) + int(arr[r-1]==0)
    res += psum[r] - psum[l-1]
    print(res)
