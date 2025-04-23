from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n, m = map(int, input().split())

    ranges = []
    for _ in range(m):
        l, r = map(int, input().split())
        ranges.append((l-1, r-1))

    q = int(input())
    Q = [int(input()) - 1 for _ in range(q)]

    left = 0
    right = q

    # O(max(n, m))
    def check(x):
        A = [0] * n
        for i in Q[:x]:
            A[i] = 1

        psum = [0]
        for a in A:
            psum.append(psum[-1] + a)
            
        for l, r in ranges:
            k  = r - l + 1
            cnt = psum[r + 1] - psum[l]
            if k - cnt < cnt:
                return True
            
        return False

    while left < right:
        mid = (left +right) //2 
        if check(mid):
            right = mid
        else:
            left = mid + 1
    
    print(right if check(right) else -1)

        


    