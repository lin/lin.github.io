from sys import stdin
input = stdin.readline

from math import *

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()

n, a, b = ti()
s = si()

res = inf
for i in range(n):
    curr = s[i:] + s[:i]
    cnt = 0
    for j in range(n//2):
        if curr[j] != curr[~j]:
            cnt += 1
        
    res = min(res, i * a  + cnt * b)

print(res)