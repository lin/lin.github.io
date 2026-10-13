from sys import stdin
input = stdin.readline

from math import *

# for _ in range(int(input())):
# n = int(input())
h, w = map(int, input().split())

res = []
for _ in range(h):
    s = input().strip()
    res.append(s.replace('TT', 'PC'))

for r in res:
    print(''.join(r))