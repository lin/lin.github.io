from sys import stdin
input = stdin.readline

from math import *

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))

    es = sum([A[i] for i in range(n) if i % 2 == 0])
    os = sum([A[i] for i in range(n) if i % 2 == 1])

    if n % 2 == 0:
        print("Yes" if os >= es else "No")
    else:
        print("Yes")

