from sys import stdin
input = stdin.readline

from math import *

for _ in range(int(input())):
    n, k = map(int, input().split())
    # s = input().strip()
    X = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # abc dddab
    # abc abc
    # abc ddddabcab eeeeeeabc
    # abc dddabcabc eeeeeeabcabc
    res = ['a', 'b',  'c']
    x1, c1 = X[0], C[0]

    for i in range(1, k+1):
        pass

    print('Yes' if res else 'No')
    if res:
        print(res)