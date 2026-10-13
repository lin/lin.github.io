from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n, k = map(int, input().split())

    if log(n, 2) >= k:
        print(2**k)
    else:
        print(n + 1)