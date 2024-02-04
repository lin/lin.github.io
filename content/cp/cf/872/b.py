from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    B = list(map(int, input().split()))
    B.sort()

    mx = (n*m-1)*B[-1] - (min(n, m)-1)*B[1] - (n*m - min(n,m)) * B[0]
    mn = -(n*m-1)*B[0] + (min(n, m)-1)*B[-2] + (n*m - min(n,m)) * B[-1]

    print(max(mx, mn))