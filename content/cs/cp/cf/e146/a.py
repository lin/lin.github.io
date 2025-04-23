from sys import stdin
input = stdin.readline

from math import *

for _ in range(int(input())):
    n, k = map(int, input().split())

    res = 'Yes'
    if n % 2 != 0 and k % 2 == 0:
        res = 'No'
    
    print(res)