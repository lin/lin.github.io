from bisect import bisect_left, bisect_right
from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n, k = map(int, input().split())
data = []
for _ in range(n):
    a, b = map(int, input().split())
    data.append((a,b))

data.sort(key=lambda x:(x[0], -x[1]))

psum = [0]
for i in range(n-1, -1, -1):
    psum.append(psum[-1] + data[i][1])

res = None
for i in range(n):
    # valid for this day
    if psum[~i] <= k:
        if i == 0:
            res = 1
        else:
            res = data[i-1][0] + 1
        break

if res == None:
    res = data[-1][0] + 1

print(res)
        

# print(psum)

# i = bisect_left(psum, k)
# print(data[i-1][0])
 
    