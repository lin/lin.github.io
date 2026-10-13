from sys import stdin
input = stdin.readline

from math import *

for _ in range(int(input())):
    # n = int(input())
    n, m = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())

    def get_k(x, y):
        a = 1 if x==1 or x == n else 0
        b = 1 if y==1 or y == m else 0
        return 4-a-b
    
    print(min(get_k(x1,y1), get_k(x2,y2)))

