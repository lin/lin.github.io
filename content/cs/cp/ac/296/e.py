from sys import stdin
input = stdin.readline

from math import *
from heapq import *

n, k = map(int, input().split())

A = list(map(int, input().split()))

seen = set()
 
heap = [0]
heapify(heap)
 
res = []
while len(res) <= k:
    min_val = heappop(heap)
    res.append(min_val)
    for a in A:
        new_val = min_val + a
        if new_val not in seen:
            seen.add(new_val)
            heappush(heap, new_val)

print(res[k])