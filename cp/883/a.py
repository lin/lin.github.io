from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())

    cnt = 0
    for _ in range(n):
        a, b = map(int, input().split())
        if a > b:
            cnt += 1
    
    print(cnt)

