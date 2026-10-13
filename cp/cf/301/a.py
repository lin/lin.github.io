from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque

n = int(input())
s = input().strip()

cnt = Counter(s)

if cnt['A'] > cnt['T']:
    print('A')
elif cnt['A'] < cnt['T']:
    print('T')
else:
    if s[-1] == 'A':
        print('T')
    else:
        print("A")