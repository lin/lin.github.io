from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))

    # A.sort()

    res = -1
    # have i liars, can't be n liars
    for i in range(n+1):
        cnt = 0
        for x in A:
            if x > i:
                cnt += 1
        if cnt == i:
            res = cnt

    print(res)
