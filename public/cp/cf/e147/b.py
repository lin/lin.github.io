from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    l, r = 0, n - 1

    while l < n and A[l] == B[l]:
        l += 1
    while r >= 0 and A[r] == B[r]:
        r -= 1
    
    i, j = l-1, r+1

    while i >= 0 and A[i] <= B[i+1]:
        i -= 1
    while j < n and A[j] >= B[j-1]:
        j += 1
    

    print(i+2, j)
