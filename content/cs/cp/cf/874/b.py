from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque

for _ in range(int(input())):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    sorted_A = sorted([(a,i) for i, a in enumerate(A)])
    sorted_B = sorted(B, reverse=True)

    res = [None] * n
    for a, i in sorted_A:
        res[i] = sorted_B.pop()
      
    print(*res)

    