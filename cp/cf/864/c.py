from sys import stdin
from sys import stdout
input = stdin.readline

from math import *

for _ in range(int(input())):
    n, m = map(int, input().split())

    print('?', 1, 1)
    stdout.flush()
    k1 = int(input())

    r1, c1 = min(1+k1, n), min(1+k1, m)
    print('?', r1, c1)
    stdout.flush()
    k2 = int(input())

    print('?', r1, c1-k2)
    stdout.flush()
    k3 = int(input())

    if k1 == 0:
        print('!', 1, 1)
        stdout.flush()
    elif k2 == 0:
        print('!',r1, c1)
        stdout.flush()
    elif k3 == 0:
        print('!', r1, c1-k2)
        stdout.flush()
    else:
        print('!', r1-k2, c1)
        stdout.flush()

    stdout.flush()