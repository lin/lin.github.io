from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n = int(input())
s = input().strip()

if len(set(s)) == 1:
    print(-1)
    exit()

cnt = 0
cnts = []
for ch in s:
    if ch == 'o':
        cnt+=1
    else:
        cnts.append(cnt)
        cnt = 0

cnts.append(cnt)

print(max(cnts))