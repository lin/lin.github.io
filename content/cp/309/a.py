from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

a, b = map(int, input().split())

s = [(1,2), (2,3), (4,5), (5,6), (7,8),(8,9)]

if (a,b)in s:
    print("Yes")
else:
    print("No")