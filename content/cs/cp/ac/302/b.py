from sys import stdin
input = stdin.readline

from math import *

h,w = map(int, input().split())

data = []
for _ in range(h):
    data.append(input().strip())

target = 'snuke'
dirs = [(0,-1),(0,1), (1,0), (-1,0), (-1,1), (1,-1), (1,1), (-1, -1)]
            
for r in range(h):
    for c in range(w):
        if data[r][c] == 's':
            for dr, dc in dirs:
                valid = True
                for i in range(5):
                    if r+ dr*i<0 or r+dr*i>= h or c+dc*i<0 or c+dc*i>=w or data[r+dr*i][c+dc*i] != target[i]:
                            valid = False

                if valid:
                    for i in range(5):
                        print(r+dr*i+1,c+dc*i+1) 
                    exit()
