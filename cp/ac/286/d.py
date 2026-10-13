from sys import stdin
input = stdin.readline

from math import *

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()

n, x = ti()

dp = [False] * (x+1)
dp[0] = True

for _ in range(n):
    a, b = ti()
    for j in range(1,b+1):
        for k in range(x, -1, -1):
            if k + a <= x and dp[k]:
                dp[k + a] = True

print('Yes' if dp[x] else 'No')
