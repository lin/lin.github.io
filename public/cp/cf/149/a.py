from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    x, k = map(int, input().split())
    if x % k != 0:
        print(1)
        print(x)
        continue

    print(2)
    print(1 - 3 * x, 4*x - 1)

