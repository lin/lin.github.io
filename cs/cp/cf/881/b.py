from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))

    tot = sum(abs(a) for a in A)

    cnt = 0
    in_neg = False
    for i in range(n):
        if A[i] > 0 and in_neg:
            in_neg = False
        elif A[i] < 0:
            if not in_neg:
                cnt += 1
                in_neg = True
    
    print(tot, cnt)
            