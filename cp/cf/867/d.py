from sys import stdin
input = stdin.readline

from math import *

for _ in range(int(input())):
    n = int(input())

    if n == 1:
        print(1)
        continue

    if n % 2 == 1:
        print(-1)
        continue

    res = [n]

    for i in range(1, n):
        if i % 2 == 1:
            res.append(n-i)
        else:
            res.append(i)
        
    print(*res)