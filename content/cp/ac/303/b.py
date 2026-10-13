from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n, m = map(int, input().split())
seen = set()

for _ in range(m):
    A = list(map(int, input().split()))
    for i in range(n-1):
        a, b = A[i], A[i+1]
        seen.add((a, b))
        seen.add((b, a))
    
# print(seen)
k = len(seen)

print((n*(n-1) - k)//2)