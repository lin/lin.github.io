from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    cnt = Counter(A)
    mx = max(cnt.keys())

    res = True
    prev = None
    for p in range(mx+1):
        if p == 0:
            if cnt[0] == 0:
                res = False
                break
            prev = cnt[0]
        else:
            if cnt[p] > prev:
                res = False
                break
            prev = cnt[p]
    print('Yes' if res else 'No')