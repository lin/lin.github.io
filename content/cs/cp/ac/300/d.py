from itertools import accumulate
from sys import stdin
input = stdin.readline

from math import sqrt
from collections import defaultdict, Counter, deque

n = int(input())

sieve = [0, 0] + [1 for _ in range(int(sqrt(n))-1)]
primes = []
for p in range(2, len(sieve)):
    if sieve[p] == 0: 
        continue
    primes.append(p)
    for j in range(p*p, len(sieve), p): 
        sieve[j] = 0

psum = list(accumulate(sieve))

res = 0
k = len(primes)
for i in range(k):
    a = primes[i]
    if a**5 >= n:
        break
    for j in range(i+1, k):
        b = primes[j]
        if a * a * b * b * b >= n:
            break
        res += psum[int(sqrt(n//(a*a*b)))] - psum[b]

print(res)