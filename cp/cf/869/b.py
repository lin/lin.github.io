from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque

for _ in range(int(input())):
    n = int(input())

    if n == 1:
        print(1)
        continue

    # tot == n*(n+1)//2
    # if n is an odd number
    # tot is always divisible by n
    if n % 2 == 1:
        print(-1)
        continue

    # if n is even, let n == 2k
    # tot == k*(2k+1) will never be divisible by 2k

    # for odd index
    # tot == (2k+1)(k+1) + 1 
    # tot % 2k+1 will always be 1
    half = n//2
    res = []
    for i in range(1, half+1):
        res.append(2*i)
        res.append(2*i - 1)
    print(*res)

