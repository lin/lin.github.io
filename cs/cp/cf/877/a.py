from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))

    A.sort()
    if A[0] < 0:
        print(A[0])
    else:
        print(A[-1])