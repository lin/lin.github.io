from sys import stdin
input = stdin.readline

from math import *

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()

n = ii()
nums = li()

res = []
for num in nums:
    if not num & 1:
        res.append(num)

print(*res)