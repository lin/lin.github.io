from sys import stdin
input = stdin.readline

from math import *

for _ in range(int(input())):
    n, k = map(int, input().split())

    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    
    # r, c => ~r, ~c
    cnt = 0
    for r in range(n):
        for c in range(n):
            if grid[r][c] != grid[~r][~c]:
                cnt += 1
            
    cnt //= 2

    # print(cnt)
    if k < cnt:
        print('No')
        continue
    
    # we can play center piece
    if n % 2 == 1:
        print("Yes")
        continue

    print('Yes' if (k - cnt) % 2 == 0 else 'No')

