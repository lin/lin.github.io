from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n, k, q = map(int, input().split())
    A = list(map(int, input().split()))

    start = 0
    res = 0
    for end in range(n):
        if A[end] > q:
            start = end + 1
        days = end - start + 1
        if days >= k:
            res += days - k + 1

    print(res) 