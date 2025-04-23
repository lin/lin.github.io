from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n, k = map(int, input().split())

    if k == 1:
        print(n)
        continue

    res = ceil(n/k)
    res += 1 if n%k!=1 else 0
    print(res)


    # res = [0] * n
    # cnt = 0
    # for i in range(n):
    #     if ceil((i+1)/k) < cnt:
    #         res[i] = 1
    #         cnt += 1

    # cnt = 0
    # for i in range(n-1, -1, -1):
    #     if res[i] == 1:
    #         cnt += 1
    #     elif ceil((n-i)/k) < cnt and res[i] == 0:
    #         res[i] = 1
    #         cnt += 1
    
    # print(*res)


    # if n % 2==0:
    #     half = n//2
    #     print(ceil(half/k)*2)
    # else:
    #     half = n//2
    #     res = ceil(half/k)*2
    #     res += 1 if half % k == 0 else 0
    #     print(res)
