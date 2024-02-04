from collections import deque
from sys import stdin, stdout
input = stdin.readline

from math import *

for _ in range(int(input())):
    n = int(input())

    # print('+', n+1)
    # print('+', n)
    # stdout.flush()

    dist = {}
    q = deque([i for i in range(1, n+1)])

    for i in range(n):
        if i % 2 == 0:
            c = q.pop()
        else:
            c = q.popleft() 
        dist[c] = i
    
    print(dist)

    
