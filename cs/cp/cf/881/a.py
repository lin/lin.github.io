from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()

    res = 0
    for i in range(n//2):
        res += A[~i] - A[i]

    print(res)