from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n, k, x = map(int, input().split())

    if x != 1:
        print('Yes')
        print(n)
        print(*[1 for _ in range(n)])
        continue

    # x == 1, no one allowed
    # 2 4 6 8 10 12...
    if n % 2 == 0 and k >= 2:
        print('Yes')
        print(n//2)
        print(*[2 for _ in range(n//2)])
        continue
    
    # x==1 and n is odd
    # 3 2 2 2 2 
    # 3 5 7 9 11...
    if k<3:
        print('No')
    else:
        print('Yes')
        print(1 + (n-3)//2)
        res = [3] + [2 for _ in range((n-3)//2)]
        print(*res)
