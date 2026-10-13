from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))

    cnt = Counter(A)

    neg = cnt[-1]
    pos = cnt[1]

    res = 0
    while cnt[1] < cnt[-1] or cnt[-1] % 2 != 0:
        cnt[-1] -= 1
        cnt[1] += 1
        res += 1

    print(res)