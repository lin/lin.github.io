from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n = int(input())
strs = []
for i in range(n):
    s = input().strip()
    strs.append(s)

found = False
for i in range(n):
    for j in range(n):
        if i != j:
            sub = strs[i] + strs[j]
            valid = True
            for k in range(len(sub)//2):
                if sub[k] != sub[~k]:
                    valid=False
                    break
            if valid:
                found = True

print('Yes' if found else 'No')