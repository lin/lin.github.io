from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())
    P = list(map(int, input().split()))

    i1 = P.index(1) + 1
    i2 = P.index(2) + 1
    imx = P.index(n) + 1

    if i1 < imx < i2 or i2 < imx < i1:
        print(1, 1)
    elif imx > i1 > i2 or imx < i1 < i2:
        print(i1, imx)
    else:
        print(i2, imx)