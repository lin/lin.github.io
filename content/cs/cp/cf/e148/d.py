from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque

for _ in range(int(input())):
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    s = input().strip()