from sys import stdin
input = stdin.readline


MOD = 998244353
ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

from math import *
from collections import defaultdict,deque,Counter

n, k = ti()

def solve(n, p):
    each = 0.01 * p + 1
    k = n / each
    print(k)
    return MOD % k

print(solve(n, k))