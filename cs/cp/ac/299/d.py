from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n, t = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

max_rank = 0
max_index = -1
for i in range(n):
    if C[i] == t and R[i] > max_rank:
        max_rank = R[i]
        max_index = i+1

if max_index != -1:
    print(max_index)
    exit()

t = C[0]
for i in range(n):
    if C[i] == t and R[i] > max_rank:
        max_rank = R[i]
        max_index = i+1

print(max_index)

