from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    s = input().strip()
    # if there are same 1s, group them together

    res = []
    s = '0' + s + '1'

    curr = '0'
    for i, ch in enumerate(s):
        if ch == '?':
            res.append(curr)
        else:
            res.append(ch)
            curr = ch
    res = res[1:-1]

    print(''.join(res))
