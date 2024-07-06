# sys.setrecursionlimit(10**9)

#####################
### BASIC
###
#####################

from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n, k = map(int, input().split())
    n = int(input())
    A = list(map(int, input().split()))
    s = input().strip()

#=======================

from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n, k = map(int, input().split())
A = list(map(int, input().split()))
n = int(input())
s = input().strip()

#####################
### INTERACTIVE
###
#####################

from sys import stdout

left = 1
right = 1000001
 
while left < right:
    mid = (left + right) // 2

    print('?', mid)
    stdout.flush()

    response = input()

    if response == '<':
        right = mid
    else:
        left = mid + 1
    
print("!", right - 1)
stdout.flush()

#####################
### DSU / LOG(N)
###
#####################

from collections import Counter

root = [i for i in range(n)]

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(x, y):
    rx, ry = find(x), find(y)
    root[max(rx, ry)] = min(rx, ry)

[find(i) for i in range(n)]

len(Counter([find(i) for i in range(n)]))

#####################
### DSU / FAST
###
#####################

from collections import Counter

root = [i for i in range(n)]

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(x, y):
    rx, ry = find(x), find(y)
    root[max(rx, ry)] = min(rx, ry)

[find(i) for i in range(n)]

len(Counter([find(i) for i in range(n)]))

#####################
### TOPO SORT
###
#####################

def topological_sort(graph, indegree):
    queue = deque()
    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return result

#####################
### PRIME NUMBER
###
#####################

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def prime_factors_with_count(x):
    res = Counter()
    for i in range(2, int(sqrt(x)) + 1):
        while x % i == 0:
            res[i] += 1
            x //= i
    if x > 1:
        res[x] += 1
    return res
    # return list(res.keys())

def prime_factors(x):
    res = set()
    for i in range(2, int(sqrt(x)) + 1):
        while x % i == 0:
            res.add(x)
            x //= i
    if x > 1:
        res.add(x)
    return list(res)

# prod(1-1/pf)
def get_coprimes_count(a):
    pf = prime_factors(a)
    res = a
    for el in pf:
        res //= el
        res *= (el-1)
    return res

def prime_decomposition(N):
    ret = {}
    n = int(N ** 0.5)
    for d in range(2, n + 1):
        while N % d == 0:
            if d not in ret:
                ret[d] = 1
            else:
                ret[d] += 1
            N //= d
        if N == 1:
            break
    if N != 1:
        ret[N] = 1
    return ret

#########################
### SIEVE OF ERATOSTHENES
###
#########################

# n*log(n) to get factors
MAX = 10 ** 7 + 10
sieve = [0 for i in range(MAX)]
for i in range(2, MAX):
    if sieve[i] == 0: # 
        sieve[i] = i
        for j in range(i * i, MAX, i):
            sieve[j] = i
nums = [12, 3, 14]
for num in nums:
    factors = []
    while num != sieve[num]:
        factor = sieve[num]
        factors.append(factor)
        num //= factor
    factors.append(num)

def factorization(x):
    res = set()
    while x != 1:
        res.add(sieve[x])
        x = x // sieve[x]
    return res

# get primes under MAX, nlogn
# 1 is maybe prime, 0 is not prime
sieve = [0, 0] + [1 for _ in range(range(isqrt(MAX)-1))]
primes = []
for p in range(2, len(sieve)):
    if sieve[p] == 0: 
        continue
    primes.append(p)
    for j in range(p*p, len(sieve), p): 
        sieve[j] = 0

#####################
### DIJKSTRA
###
#####################

from heapq import *

src, dst = 0, 1
graph = defaultdict(list)

dist = defaultdict(lambda :inf)
dist[src] = 0

heap = [(0, src)]
prev = {}
while heap:
    cost, node = heappop(heap)
    if dist[node] < cost:
        continue

    for neigh, weight in graph[node]:
        dist = weight + cost
        if dist < dist[neigh]:
            dist[neigh] = dist
            prev[neigh] = node
            heappush(heap, (dist, neigh))