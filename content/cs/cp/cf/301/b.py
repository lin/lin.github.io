from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque

n = int(input())
A = list(map(int, input().split()))
res = [A[0]]

for i in range(1, n):
    if A[i] > A[i-1]:
        for x in range(A[i-1]+1, A[i]+1):
            res.append(x)
    else:
        for x in range(A[i-1]-1, A[i]-1, -1):
            res.append(x)
        
print(*res)