from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())
    s = input().strip()

    curr = 0
    seen = set([0])
    for ch in s:
        if ch == '<':
            curr += 1
        else:
            curr -= 1
        seen.add(curr)

    
    print(len(seen))

