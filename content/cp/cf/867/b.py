from sys import stdin
input = stdin.readline

from math import *

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))

    A.sort()

    a, b = A[0], A[1]

    c, d = A[-2], A[-1]

    # if a < 0 and b < 0:
    print(max(a*b, c*d))


