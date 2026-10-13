import math
 
for _ in range(int(input())):
    n = int(input())
    sticks = list(map(int,input().split()))
    sticks.sort()
    res = math.inf
    for i in range(1, n - 1):
        res = min(res, sticks[i + 1] - sticks[i - 1])
    print(res)