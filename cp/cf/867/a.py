from sys import stdin
input = stdin.readline

from math import *

for _ in range(int(input())):
    # n = int(input())
    n, t = map(int, input().split())
    # s = input().strip()
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_val = 0
    res = None
    for i in range(n):
        if i+A[i] <= t:
            if B[i] > max_val:
                max_val = B[i]
                res = i+1
    print(res if res else -1)
        
    