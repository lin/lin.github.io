# 11m 12s
from heapq import *
from math import ceil

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    ni = [[num, i] for i, num in enumerate(nums)]

    ni.sort()

    if ni[0][0] == ni[-1][0]:
        print(0)
        continue

    if ni[0][0] == 1:
        print(-1)
        continue

    res = []
    while True:
        if ni[0][0] == ni[-1][0]:
            break

        while ni[0][0] < ni[-1][0]:
            ni[-1][0] = ceil(ni[-1][0]/ni[0][0])
            res.append([ni[-1][1]+1, ni[0][1]+1])

        ni.sort()

    print(len(res))
    for pair in res:
        print(*pair)