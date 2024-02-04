from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))

    if n == 1:
        print(*A)
        continue

    mx = max(A[1:])
    mxi = A.index(mx)

    res = [0] * n
    for l in range(mxi-1, -1,-1):
        # i don't realize we can compare arr like this
        # and try to solve this problem in O(N) T_T
        res = max(res, A[mxi:] + A[l:mxi][::-1] + A[:l])
    
    if mxi == n-1:
        for l in range(n-1, -1,-1):
            res = max(res, A[l:][::-1] + A[:l])

    print(*res)