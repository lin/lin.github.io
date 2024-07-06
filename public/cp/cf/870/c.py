from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque

MAX = 10**6 + 10
sieve = [0 for i in range(MAX+1)]
for i in range(2, MAX+1):
    for j in range(i, MAX+1, i):
        if sieve[j] == 0:
            sieve[j] = i

for _ in range(int(input())):
    n, m = map(int, input().split())

    if n == 1 or m == 1:
        print("Yes")
        continue

    print('No' if m >= sieve[n] else 'Yes')