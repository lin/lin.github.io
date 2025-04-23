from re import I
from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n, k, g = map(int, input().split())

    # round(x/g) * g
    tot = k * g

    half = (g - 1) // 2

    # everyone recieve zero gold
    if n * half >= tot:
        print(tot)
        continue

    def get(x):
        r = x % g
        if r >= g/2:
            return x+(g-r)
        return x-r

    # n-1 people recieve zero gold
    res = (n-1) * half
    remain = tot - res
    res += remain - get(remain)

    print(res)



