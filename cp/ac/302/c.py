from sys import stdin
input = stdin.readline

from math import *
from itertools import *

n, m = map(int, input().split())

data = []

for _ in range(n):
    data.append(input().strip())


for perm in permutations([i for i in range(n)]):
    valid = True
    for i in range(n-1):
        curr = data[perm[i]]
        nxt = data[perm[i+1]]
        cnt = 0
        for j in range(m):
            if curr[j] != nxt[j]:
                cnt += 1
        if cnt > 1:
            valid = False
    if valid:
        print('Yes')
        exit()
        
print('No')


