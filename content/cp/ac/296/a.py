from sys import stdin
input = stdin.readline

from math import *

# for _ in range(int(input())):
# n = int(input())
n, d = map(int, input().split())
# s = input().strip()
T = list(map(int, input().split()))


res = -1
for i in range(n-1):
    if T[i+1] - T[i] <= d:
        res = T[i+1]
        break
    
print(res)