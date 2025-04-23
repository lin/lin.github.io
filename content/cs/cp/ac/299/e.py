from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n = int(input())

sieve = [0, 0] + [1 for _ in range(isqrt(n)-1)]
primes = []
for p in range(2, len(sieve)):
    if sieve[p] == 0: 
        continue
    primes.append(p)
    for j in range(p*p, len(sieve), p): 
        sieve[j] = 0

psum = [0]
for x in sieve:
    psum.append(psum[-1] + x)

res = 0
k = len(primes)
for i in range(k):
    a = primes[i]
    for j in range(i+1, k):
        b = primes[j]
        res += psum[isqrt(n//(a*a*b))] - psum[b]

print(res)
# ans=0
# for i in range(len(P)):
#     a=P[i]
#     if a**5>=N: break
#     for j in range(i+1, len(P)):
#         b=P[j]
#         if a*a*b*b*b>=N: break
#         ans += S[isqrt(N//(a*a*b))]-S[b]
 
# print(ans)


