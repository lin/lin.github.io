from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque

for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))

    res = []
    for i in range(n):
        res.append(abs(p[i]-(i+1)))

    print(gcd(*res))
    
    # res = [x for x in res if x !=0]

    # print(min(res))