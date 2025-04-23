from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n, m = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    tA = sum(A)
    tB = sum(B)

    if tA == tB:
        print('Draw')
    elif tA > tB:
        print('Tsondu')
    else:
        print('Tenzing')

