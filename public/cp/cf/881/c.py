from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())

    res = 0
    while n:
        res += n
        n //= 2
    
    print(res)