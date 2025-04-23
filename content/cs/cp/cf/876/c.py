from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))

    if A[-1] != 0:
        print('NO')
        continue

    res = []
    i = n-1
    flip = False
    while i > 0:
        while i > 0 and ((not flip and A[i-1] == 0) or (flip and A[i-1] == 1)):
            i -= 1
        res.append(i)
        flip = not flip
    
    res = [0] * (n-len(res)) + res[::-1]
    print("YES")
    print(*res)