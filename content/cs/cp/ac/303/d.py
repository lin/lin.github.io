from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

x,y,z = map(int, input().split())
s = input().strip()

n = len(s)

# [OFF, ON]
dp = [[0,0] for _ in range(n+1)]

dp[0][1] = z

for i in range(n):
    ch = s[i]
    
    if ch == 'a':
        # if we leave it as off
        dp[i+1][0] = min(dp[i][0] + x, dp[i][1] + z + y)
        dp[i+1][1] = min(dp[i][1] + y, dp[i][0] + z + x)
    else:
        # if we leave it as off
        dp[i+1][1] = min(dp[i][1] + x, dp[i][0] + z + y)
        dp[i+1][0] = min(dp[i][0] + y, dp[i][1] + z + x)

print(min(dp[-1]))



