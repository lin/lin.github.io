from sys import stdin
input = stdin.readline

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

from math import *
from collections import defaultdict,deque,Counter

k = ii()

def solve(k): # 3^k => n!
    res = 1
    for p in range(2, int(sqrt(k))+1):
        count = 0
        while k % p == 0:
            k //= p
            count += 1
        n = 0
        while count > 0:
            n += p
            curr = n
            while curr % p == 0:
                curr //= p
                count -= 1
        res = max(res, n)
    res = max(res, k)
    return res

print(solve(k))