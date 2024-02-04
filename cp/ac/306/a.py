from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n = int(input())
s = input().strip()

res = ''
for ch in s:
    res += ch
    res += ch

print(res)