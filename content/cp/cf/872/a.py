from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque

for _ in range(int(input())):
    s = input().strip()

    n = len(s)

    if len(set(s)) == 1:
        print(-1)
    else:
        print(n-1)