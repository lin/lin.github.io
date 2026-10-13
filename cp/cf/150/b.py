from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    q = int(input())
    X = list(map(int, input().split()))

    start = q - 1
    res = [1]
    prev = X[0]
    for i in range(1, q):
        if X[i] >= prev:
            res.append(1)
            prev = X[i]
        else:
            if X[i] <= X[0]:
                res.append(1)
                start = i
                break
            else:
                res.append(0)
    
    if start != q - 1:
        prev = X[start]
        for i in range(start + 1, q):
            if X[i] >= prev and X[i] <= X[0]:
                res.append(1)
                prev = X[i]
            else:
                res.append(0)
        
    print(''.join([str(i) for i in res]))


