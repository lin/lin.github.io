from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())
    chars = list(input().split())
    
    ### OOO + max(A, B) + AB AB AB
    cnt = Counter(chars)
    res = cnt['O'] + max(cnt['A'], cnt['B']) + cnt['AB']

    print(res)