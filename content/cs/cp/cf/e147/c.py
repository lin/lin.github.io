from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    s = input().strip()
    n = len(s)

    res = inf
    for i in range(26):
        curr_char = chr(ord('a') + i)
        
        cnt = max_len = 0
        for ch in s:
            if ch != curr_char:
                cnt +=1
            else:
                max_len = max(max_len, cnt)
                cnt = 0
        max_len = max(max_len, cnt)

        if max_len == 0:
            res = 0
            break

        ops = 0
        while 1<<ops <= max_len:
            ops += 1
        res = min(res, ops)

    print(res)