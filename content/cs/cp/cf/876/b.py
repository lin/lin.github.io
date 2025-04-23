from sys import stdin
from heapq import *
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())

    heap = []
    for _ in range(n):
        a, b = map(int, input().split())
        heappush(heap, (a, -b))

    cnt = 0
    min_cnt = 0
    res = 0
    q = deque([])
    seen = set()
    while heap:
        a, b = heappop(heap)
        while q and q[0] <= len(q):
            seen.add(q.popleft())
            cnt -= 1

        if cnt < a and a not in seen:
            res += -b
            cnt += 1
            q.append(a)
        
    
    print(res)





