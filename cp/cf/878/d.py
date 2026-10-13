from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))

    if n <= 3:
        print(0)
        continue

    A.sort()
    left = 0
    right = A[-1]

    def check(x):
        cnt = 1
        curr_min = A[0]
        for i in range(1, n):
            if (A[i] - curr_min + 1) // 2 > x:
                cnt += 1
                if cnt > 3:
                    return False
                curr_min = A[i]
        return True

    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    
    print(right)