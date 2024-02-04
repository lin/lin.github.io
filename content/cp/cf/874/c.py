from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))

    A.sort()

    seen_odd = False
    seen_even = False

    # odd even
    possible = [[False, False] for _ in range(n)]

    for i, a in enumerate(A):
        if a % 2 == 0:
            possible[i][1] = True
            if seen_odd:
                possible[i][0] = True
            seen_even = True
        else:
            if seen_odd:
                possible[i][1] = True
            possible[i][0] = True
            seen_odd = True

    # print(possible)
    odd, even = True, True
    for o,e in possible:
        odd &= o
        even &= e
    
    print('Yes' if odd or even else 'No')