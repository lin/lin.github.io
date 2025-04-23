from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

d4 = [(-1,0),(0,1),(1,0),(0,-1)]
d8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

class PrimeTable:
    def __init__(self, n:int) -> None:
        self.n = n
        self.primes = []
        self.min_div = [0] * (n+1)
        self.min_div[1] = 1
 
        mu = [0] * (n+1)
        phi = [0] * (n+1)
        mu[1] = 1
        phi[1] = 1
 
        for i in range(2, n+1):
            if not self.min_div[i]:
                self.primes.append(i)
                self.min_div[i] = i
                mu[i] = -1
                phi[i] = i-1
            for p in self.primes:
                if i * p > n: break
                self.min_div[i*p] = p
                if i % p == 0:
                    phi[i*p] = phi[i] * p
                    break
                else:
                    mu[i*p] = -mu[i]
                    phi[i*p] = phi[i] * (p - 1)
 
    def is_prime(self, x:int):
        if x < 2: 
            return False
        if x <= self.n: 
            return self.min_div[x] == x
        for i in range(2, int(sqrt(x))+1):
            if x % i == 0: 
                return False
        return True
 
    def prime_factorization(self, x:int):
        for p in range(2, int(sqrt(x))+1):
            if x <= self.n: break
            if x % p == 0:
                cnt = 0
                while x % p == 0: cnt += 1; x //= p
                yield p, cnt
        while (1 < x and x <= self.n):
            p, cnt = self.min_div[x], 0
            while x % p == 0: cnt += 1; x //= p
            yield p, cnt
        if x >= self.n and x > 1:
            yield x, 1
 
    def get_factors(self, x:int):
        factors = [1]
        for p, b in self.prime_factorization(x):
            n = len(factors)
            for j in range(1, b+1):
                for d in factors[:n]:
                    factors.append(d * (p ** j))
        return factors

n = ii()
nums = li()
s, e = ti()

table = PrimeTable(3 * 10 ** 5 + 1)
primes = table.primes

graph = defaultdict(list)
for i, num in enumerate(nums):
    for p, cnt in table.prime_factorization(num):
        prime_idx = n + bisect_left(primes, p)
        graph[i].append(prime_idx)
        graph[prime_idx].append(i)

q = deque([s])
visited = set([s])

found = False
res = []
prev = {s: -1}
while q:
    curr = q.popleft()

    if curr == e:
        res = curr
        found = True
        break 

    for nei in graph[curr]:
        if nei not in visited and nei != curr:
            q.append((nei))
            prev[nei] = curr
            visited.add(nei)

if found:
    path = [e]
    while prev[path[-1]] != -1:
        path.append(prev[path[-1]])
    print(len(path))
    print(*path[::-1])
else:
    print(-1)