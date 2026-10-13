from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    a, b, c, k = map(int, input().split())

    low_c = 10**(c - 1)
    high_c = 10**c - 1

    low_b = 10**(b - 1)
    high_b = 10**b - 1

    for A in range(10**(a-1), 10**a):
        b1, b2 = max(low_b, low_c - A), min(high_b, high_c - A)

        if b1 <= b2:
            if k > b2 - b1 + 1:
                k -= b2 - b1 + 1
            else:
                B = b1 + k - 1
                C = A + B
                print(str(A) + ' + ' + str(B) + ' = ' + str(C))
                break
    else:
        print(-1)