from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n, d, h = map(int, input().split())
    Y = list(map(int, input().split())) # len(A) == n

    tot = n * d * h / 2

    dup = 0
    for i in range(1, n):
        dy = Y[i] - Y[i-1]
        if dy < h:
            dup += (d*(h-dy)*(h-dy))/(2*h)
    
    print(tot - dup)


