from sys import stdin
input = stdin.readline

from math import *

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()

n,m= ti()

A = li()
B = li()

C = A + B
C.sort()
rank = {x:i+1 for i, x in enumerate(C)}

print(*[rank[a] for a in A])
print(*[rank[b] for b in B])
    