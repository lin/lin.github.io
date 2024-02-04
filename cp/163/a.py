from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())
    s = input().strip()

    first = s[0]

    found = False
    for i in range(1, len(s)):
        if s[i] > first:
            found=True
            break
    if found:
        print('Yes')
        continue

    pos = []
    for i in range(1, len(s)):
        if s[i] == first:
            pos.append(i)

    found = False
    for i in range(len(pos)):
        p = pos[i]
        if s[:p] < s[p:]:
            found = True
            break

    if found:
        print('Yes')
    else:
        print('No')