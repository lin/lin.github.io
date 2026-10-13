from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n = int(input())

if n < 1000:
    print(n)
    exit()

k = int(log(n, 10))



# print(k) # 1000 9999 => k==3, remove 1s

r = k - 2

while r:
    n //= 10**r
    n *= 10**r
    r -= 1

print(n)
