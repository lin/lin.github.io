from sys import stdin
input = stdin.readline

from math import *

for _ in range(int(input())):
    n, k = map(int, input().split())
    P = list(map(int, input().split()))

    mismatch = []
    for i in range(1, n+1):
        if i% k != P[i-1] %k:
            mismatch.append([i%k, P[i-1]%k])
        
    if not mismatch:
        print(0)
        continue

    if len(mismatch)!=2:
        print(-1)
        continue

    # 2 mismatches
    if mismatch[0] == mismatch[1][::-1]:
        print(1)
    else:
        print(-1)

    # print(*mismatch)


