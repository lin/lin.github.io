from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    mat = []
    for _ in range(3):
        mat.append(input().strip())
    
    res = None
    for i in range(3):
        row = mat[i]
        if len(set(row)) == 1 and row[0] != '.':
            res = row[0]
            break
    
    if res != None:
        print(res)
        continue

    for i in range(3):
        col = mat[0][i] + mat[1][i] + mat[2][i]
        if len(set(col)) == 1 and col[0] != '.':
            res = col[0]
            break
    
    if res != None:
        print(res)
        continue

    diag = mat[0][0] + mat[1][1] + mat[2][2]
    if len(set(diag)) == 1 and diag[0] != '.':
        res = diag[0]

    if res != None:
        print(res)
        continue

    adiag = mat[0][2] + mat[1][1] + mat[2][0]
    if len(set(adiag)) == 1 and adiag[0] != '.':
        res = adiag[0]
    
    if res != None:
        print(res)
        continue

    print("DRAW")


