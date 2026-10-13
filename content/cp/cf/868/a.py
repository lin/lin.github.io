from sys import stdin
input = stdin.readline

from math import *

for _ in range(int(input())):
    n, k = map(int, input().split())

    # how many -1 we have:
    res = []
    for i in range(n):
        cnt = comb(n-i, 2) + comb(i, 2)
        if cnt == k:
            res = [1] * (n-i) + [-1] * i
            break
    
    print("Yes" if res else "No")
    if res:
        print(*res)