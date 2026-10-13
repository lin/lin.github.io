from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n, m, h = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort(reverse=True)
    B.sort(reverse=True)

    res = 0
    for i in range(min(n, m)):
        a, b = A[i], B[i]
        res += min(a, b*h)
      
    print(res)


