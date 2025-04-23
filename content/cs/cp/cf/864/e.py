from sys import stdin
input = stdin.readline

from math import *

def primefactors(x):
    res = set()
    for i in range(2, int(sqrt(x)) + 1):
        while x % i == 0:
            res.add(i)
            x //= i
    if x > 1:
        res.add(x)
    return list(res)

# prod(1-1/pf)
def coprimes(a):
    pf = primefactors(a)
    res = a
    for el in pf:
        res //= el
        res *= (el-1)
    return res

for _ in range(int(input())):
    x = int(input())
    print(coprimes(x))
    # n, m = map(int, input().split())
    # nums = list(map(int, input().split()))

    # for _ in range(m):
    #     t, l, r = map(int, input().split())

