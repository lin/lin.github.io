from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n = int(input())

arr = []
for _ in range(n):
    arr.append(input().strip())


min_val = inf
min_index = -1
for i, val in enumerate(arr):
    name, age = val.split()
    age = int(age)
    if age < min_val:
        min_val = age
        min_index = i

for i in range(n):
    print(arr[(min_index+i)%n].split()[0])