from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
 
    res = 0

    # O(n^2)
    for i in range(n):
        stack = []
        cnt = 0
        for j in range(i,n):
            mx_so_far = A[j]
            delta = 0
            while stack and A[j] < stack[-1][0]:
                prev_mx, prev_delta = stack.pop()
                mx_so_far = max(mx_so_far, prev_mx)
                delta += prev_delta + 1
                cnt -= prev_delta
            stack.append((mx_so_far, delta))
            cnt += delta
            res += cnt
        
    print(res)