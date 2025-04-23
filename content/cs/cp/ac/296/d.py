from sys import stdin
input = stdin.readline

from math import *

a, b = map(int, input().split())

res = 0
while b:
    if a > b:
        res +=(a //b) if a%b!=0 else (a//b -1)
    a, b = b, a%b

print(res)