import re
from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    t = input().strip()

    # alice change, bob reverse
    
    diff = set()
    for i in range(n):
        if s[i] != t[i]:
            diff.add(i)

    rev_diff = set()
    for i in range(n):
        if s[i] != t[~i]:
            rev_diff.add(i) 
    
    k = len(diff)
    rev_k = len(rev_diff)

    if k == 0:
        print(0)
        continue
    if rev_k == 0:
        print(2)
        continue

    cnt = k*2 if k % 2 ==0 else k*2 - 1

    rev_cnt = rev_k*2 - 1 if rev_k % 2 ==0 else rev_k*2

    print(min(cnt, rev_cnt))

