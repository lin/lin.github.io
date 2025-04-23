from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n = int(input())
s = input().strip()

stack = []
balance = 0
for i, ch in enumerate(s):
    if ch == ')':
        if balance > 0:
            while stack[-1] != '(':
                stack.pop()
            stack.pop()
            balance -= 1
            continue
    elif ch == '(':
        balance += 1
    stack.append(ch)

print(''.join(stack))
    
