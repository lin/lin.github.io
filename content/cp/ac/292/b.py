from sys import stdin
input = stdin.readline

from math import *

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()


n, q = ti()
states = [0] * n
for _ in range(q):
    t, x = ti()
    x -= 1
    if t == 1:
        if states[x] == 1:
            states[x] = 2
        elif states[x] == 0:
            states[x] = 1
    elif t == 2:
        if states[x] == 0 or states[x] == 1:
            states[x] = 2
    else:
        print("Yes" if states[x] == 2 else "No")