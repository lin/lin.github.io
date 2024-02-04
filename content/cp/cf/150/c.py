# https://codeforces.com/contest/1841/submission/209512659

from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    s = input().strip()
    n = len(s)
    
    # first is unchanged, second is changed
    # max val seen so far
    prev = [[0] * 2 for _ in range(5)]
    
    for p in range(n - 1, -1, -1):
        v = ord(s[p]) - ord('A')

        curr = [[-inf] * 2 for _ in range(5)]

        # if no change
        for i in range(5):
            for j in range(2):
                if v < i: 
                    curr[i][j] = max(curr[i][j], prev[i][j] - 10**v)
                else: 
                    curr[v][j] = max(curr[v][j], prev[i][j] + 10**v)
        
        # now change to another val
        for nv in range(5):
            for i in range(5):
                if nv < i: 
                    curr[i][1] = max(curr[i][1], prev[i][0] - 10**nv)
                else: 
                    curr[nv][1] = max(curr[nv][1], prev[i][0] + 10**nv)
        prev = curr

    print(max(max(x) for x in prev))

    # def to_num(char):
    #     k = ord(char) - ord('A')
    #     return 10**k

    # ng = [n] * n
    # stack = []
    # for i in range(n):
    #     while stack and s[stack[-1]] < s[i]:
    #         ng[stack.pop()] = i
    #     stack.append(i)

    # pre = [[0] * 5 for _ in range(n)]
    # for i in range(n):
    #     if i != 0:
    #         for j in range(5):
    #             pre[i][j] = pre[i-1][j]
    #     pre[i][ord(s[i]) - ord('A')] += 1
    
    # post = [[0] * 5 for _ in range(n)]
    # for i in range(n-1, -1, -1):
    #     if i != n-1:
    #         for j in range(5):
    #             post[i][j] = post[i+1][j]
    #     post[i][ord(s[i]) - ord('A')] += 1

    # base_val = 0
    # for i, ch in enumerate(s):
    #     if ng[i] != n:
    #         base_val -= to_num(ch)
    #     else:
    #         base_val += to_num(ch)

    # max_delta = 0
    # for i in range(n):
        
    #     for t in range(5):
    #         if ord(s[i]) - ord('A') == t:
    #             continue

    #         delta = to_num(s[i])

    #         curr = ord(s[i]) - ord('A')

    #         is_negative_prev = False
    #         if i != n-1:
    #             for j in range(curr+1, 5):
    #                 if post[i+1][j] > 0:
    #                     is_negative_prev = True
    #                     break
    
    #         if is_negative_prev:
    #             delta += to_num(s[i])
    #         else:
    #             delta -= to_num(s[i])

    #         if i != 0:
    #             for j in range(t):
    #                 delta -= cnt[i-1][j] * (10**j)
    #                 delta -= cnt[i-1][j] * (10**j)

    #         max_delta = max(max_delta, delta)
        
    # print(max_delta + base_val)
            
