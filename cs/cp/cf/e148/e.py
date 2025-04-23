# CORE LOGIC
n,a,x,y,m,k = map(int,input().split())

B = [0] * (k+1)
for i in range(k, n+1):
    B[0] += a[i]
    for j in range(1, k+1):
        B[j] += B[j-1]

###############
#####
###############



from sys import stdin
input = stdin.readline
 
MOD = 998244353
 
from math import *
from collections import Counter, deque
 
n,a,x,y,m,k = map(int,input().split())
 
B = [0] * (k+1)
 
res = 0
for i in range(k, n+1):
    B[0] += a
    B[0] %= MOD
 
    for j in range(1, k+1):
        B[j] += B[j-1]
        B[j] %= MOD
 
    res ^= B[-1] * i
 
    # new a value
    a = (a*x + y) % m
    
print(res)

