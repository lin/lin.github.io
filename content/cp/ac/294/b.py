from sys import stdin
input = stdin.readline

from math import *

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()

h, w = ti()

for _ in range(h):
    nums = li()
    s = []
    for num in nums:
        if num == 0:
            s.append('.')
        else:
            s.append(chr(num + ord('A')-1))
    print(''.join(s))