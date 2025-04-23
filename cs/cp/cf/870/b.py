from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque

for _ in range(int(input())):
    # n, k = map(int, input().split())
    n = int(input())
    A = list(map(int, input().split()))
    res = 0
    for i in range(n//2):
        diff = abs(A[i] - A[~i])
        res = gcd(res, diff)
    print(res)


