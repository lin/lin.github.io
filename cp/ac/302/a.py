from sys import stdin
input = stdin.readline

from math import *

from collections import Counter, deque

n, k = map(int, input().split())

div, mod = n//k, n%k
if mod == 0:
    print(div)
else:
    print(div+1)