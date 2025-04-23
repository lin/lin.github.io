from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque

MOD = 10**9 + 7

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    res = 1
    j = 0
    for i in range(n):
        while j < n and B[j] < A[i]:
            j += 1
        res = (res*(j-i)) % MOD
    print(res%MOD)
    
    