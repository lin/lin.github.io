from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())

    if n <= 4:
        print('Bob')
    else:
        print('Alice')