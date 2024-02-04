from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n = int(input())
    s = input().strip()

    cnt = Counter(s)

    if cnt['('] != cnt[')']:
        print(-1)
        continue
    
    # group 1
    group1 = set()
    stack = []

    for i, ch in enumerate(s):
        if ch == ')':
            if not stack or stack[-1][0] != '(':
                stack.append((ch, i))
            else:
                group1.add(i)
                group1.add(stack.pop()[1])
        else:
            stack.append((ch, i))
    
    if len(group1) == n or len(group1) == 0:
        print(1)
        res = [1] * n
        print(*res)
        continue

    res = [None] * n
    for i in range(n):
        if i in group1:
            res[i] = 1
        else:
            res[i] = 2

    print(2)
    print(*res)

