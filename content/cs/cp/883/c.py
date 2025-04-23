from bisect import bisect_right, bisect_left
from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n, m, h = map(int, input().split())

    data = []
    for i in range(n):
        # m cols
        A = list(map(int, input().split()))
        A.sort()

        psum = [0]
        ppsum = [0]
        for a in A:
            psum.append(psum[-1] + a)
            ppsum.append(ppsum[-1] + psum[-1])

        cnt = bisect_right(psum, h)-1
        pen = ppsum[cnt]
        data.append((-cnt, pen))

    rudolf = data[0]

    data.sort()

    res = bisect_left(data, rudolf)+1
    print(res)





    


    
