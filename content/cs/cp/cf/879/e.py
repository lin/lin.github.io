from sys import stdin
input = stdin.readline

from math import *

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    
    seen = set()

    lcms = []

    for a in A:
        curr = []
        last = 0
        for i in range(len(lcms) - 1, -1, -1):
            x = lcm(lcms[i], a)
            if x > n * (n + 1) // 2: 
                break
            if last != x: 
                curr.append(x)
                last = x
        curr.reverse()

        if len(curr) == 0 or curr[-1] != a:
            curr.append(a)

        lcms = curr
        for val in lcms:
            seen.add(val)
            
    mex = 1
    while mex in seen:
        mex += 1
    print(mex)