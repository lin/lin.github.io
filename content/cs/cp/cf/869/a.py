from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque

for _ in range(int(input())):
    n, k = map(int, input().split())
    # A = list(map(int, input().split()))
    # n = int(input())
    res = 1
    me = input().strip()
    for i in range(1, n):
        if input().strip() == me:
            res += 1

    print(res)
