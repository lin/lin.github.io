from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n = int(input())
s = input().strip()

MOD = 998244353

required = set()
for i, ch in enumerate(s):
    if ch == '.':
        required.add(i)

for i in range(1, n+1):
    # if is divisor
    if n % i == 0:






