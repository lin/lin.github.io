from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))

    di = []
    for i in range(1, n):
        if A[i-1] > A[i]:
            di.append('d')
        elif A[i-1] < A[i]:
            di.append('i')

    remain = [di[0]] if di else []
    for i in range(1, len(di)):
        if i == 0 or di[i-1] == di[i]:
            continue
        remain.append(di[i])
    
    print(len(remain) + 1)
