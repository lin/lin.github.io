from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n, x = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    banned = set()

    for i in range(30):
        if 1<<i & x == 0:
            banned.add(i)
    
    val = 0
    for a in A:
        valid = True
        for i in range(30):
            if 1<<i & a and i in banned:
                valid = False
                break
        if valid:
            val |= a
        else:
            break
    
    for a in B:
        valid = True
        for i in range(30):
            if 1<<i & a and i in banned:
                valid = False
                break
        if valid:
            val |= a
        else:
            break

    for a in C:
        valid = True
        for i in range(30):
            if 1<<i & a and i in banned:
                valid = False
                break
        if valid:
            val |= a
        else:
            break
    
    print('Yes' if val==x else 'No')
        
