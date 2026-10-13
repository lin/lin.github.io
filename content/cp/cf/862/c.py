from sys import stdin
input = stdin.readline

from math import sqrt
from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right

# does it exist a k so that no intercepts for this parabola

# kx = ax^2 + bx+c have roots
# ax^2 + (b-k) x + x = 0 have roots
# Delta = (b-k)^2 - 4ac < 0
# b^2 - 2bk + k^2 - 4ac < 0 have solutions
# k^2 - 2bk + b^2 -4ac < 0
# DELTA has to >= 0 to have solutions
# 4b^2 - 4(b^2-4ac) >= 0 
# 16ac >= 0, so a > 0 c>=0
# k1,2 = b pm 2 sqrt(ac)

for _ in range(int(input())):
    n, m = map(int, input().split())

    ks = []
    for _ in range(n):
        ks.append(int(input()))
    ks.sort()

    # print(ks)

    for _ in range(m):
        a, b, c = map(int, input().split())
        if c <= 0:
            print("No")
            continue

        l, r = b - 2*sqrt(a * c), b + 2*sqrt(a * c)

        lk = bisect_right(ks, l)
        rk = bisect_left(ks, r)
        
        # print(l, r)
        # print(lk, rk)

        if lk != n and rk != 0 and lk != rk:
            print("Yes")
            print(ks[lk])
        else:
            print("No")

        