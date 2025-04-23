from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque

for _ in range(int(input())):
    n = int(input())

    res = [i for i in range(1, n+1)]
    if n % 2 == 1:
        print(*res)
    else:
        res[0] += n//2
        print(*res)

    # print(sum(res)%n)