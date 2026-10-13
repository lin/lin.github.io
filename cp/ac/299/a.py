from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n = int(input())
s = input().strip()

cnt = 0
res = -1
for i in range(n):
    if s[i] == '|':
        cnt += 1
    if s[i] == '*':
        res = cnt

print('in' if res == 1 else 'out')