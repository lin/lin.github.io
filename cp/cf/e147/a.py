from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    s = input().strip()

    res = 1
    if s[0] == '?':
        res = 9
    elif s[0] == '0':
        res = 0
    
    for i in range(1, len(s)):
        ch = s[i]
        if ch == '?':
            res *= 10
    
    print(res)