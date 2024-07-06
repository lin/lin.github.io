from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    N = int(input())
    if N == 2:
        print("No")
        continue

    res = []
    for n in range(N-1):
        res.append((n+1)*(n+2))

    if N not in res: # 1/2 + 1/6 + 1/12 + 1/N
        res.append(N)
        print("Yes")
        print(*res)
    else:
        res =[2]
        for n in range(N-2):
            res.append(2*(n+1)*(n+2))
        res.append(2*(N-1))
        print("Yes")
        print(*res)