from sys import stdin
input = stdin.readline

from math import *

# 1 => 4
# 2 => 2 + 2 + 1 + 1 + dp[1]  - 

for _ in range(int(input())):
    n = int(input())

    tot = 4*n
    tot += (n-1)*n//2
    tot += 1
    tot += (n-2)*(n-1)//2

    print(tot)