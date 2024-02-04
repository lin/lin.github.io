from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):

    x_a, y_a = map(int, input().split())
    x_b, y_b = map(int, input().split())
    x_c, y_c = map(int, input().split())

    res = 1
    if x_b > x_a and x_c > x_a:
        res += min(x_b-x_a, x_c-x_a)
    elif x_b < x_a and x_c < x_a:
        res += min(x_a - x_b, x_a-x_c)

    if y_b > y_a and y_c > y_a:
        res += min(y_b-y_a, y_c-y_a)
    elif y_b < y_a and y_c < y_a:
        res += min(y_a - y_b, y_a-y_c)
    
    print(res)