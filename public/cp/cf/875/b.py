from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # same order 
    cnt1 = defaultdict(int)
    curr, cnt = A[0], 1
    for i in range(1, n):
        if A[i] == A[i-1]:
            cnt +=1
        else:
            cnt1[curr] = max(cnt1[curr], cnt)
            curr = A[i]
            cnt = 1
    cnt1[curr] = max(cnt1[curr], cnt)


    cnt2 = defaultdict(int)
    curr, cnt = B[0], 1
    for i in range(1, n):
        if B[i] == B[i-1]:
            cnt +=1
        else:
            cnt2[curr] = max(cnt2[curr], cnt)
            curr = B[i]
            cnt = 1
    cnt2[curr] = max(cnt2[curr], cnt)

    res = 1
    for k in cnt1:
        res = max(res, cnt1[k] + cnt2[k])
    for k in cnt2:
        res = max(res, cnt1[k] + cnt2[k])
    

    print(res)


