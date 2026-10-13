from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())
    s = input().strip()

    res = []
    curr = None
    for i in range(n):
        if curr == None:
            curr = s[i]
            res.append(curr)
        elif s[i] == curr:
            curr = None
    
    print(''.join(res))