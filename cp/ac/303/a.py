from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n = int(input())
s = input().strip()
t = input().strip()

valid = True
for i in range(n):
    if s[i] == t[i] or \
        (s[i] == 'l' and t[i] == '1') or\
             (s[i] == '1' and t[i] == 'l') or \
                 (s[i] == 'o' and t[i] == '0') or \
                     (s[i] == '0' and t[i] == 'o'):
        continue
    valid = False

print('Yes' if valid else 'No')
