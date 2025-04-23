from sys import stdin
input = stdin.readline

from math import *

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()

n, p, q, r, s = ti()
nums = li()
pq = nums[p-1:q]
rs = nums[r-1:s]

nums[p-1:q] = rs
nums[r-1:s] = pq

print(*nums)