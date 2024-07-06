from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque

s = input().strip()
n = int(input())

size = 60

str_s = '0' * (size-len(s)) + s
str_n = bin(n)[2:]
str_n = '0' * (size-len(str_n)) + str_n

k = len(s)

has_10 = [False] * size

last_10 = -1
last_01 = -1
for i in range(size-1, -1, -1):
    s_ch, n_ch = str_s[i], str_n[i]
    if s_ch == '1' and n_ch == '0':
        last_10 = i
    if s_ch == '0' and n_ch == '1':
        last_01 = i
    if s_ch == '?' and n_ch == '1':
        # has_10[i] = True if last_10 != -1 and (last_10 < last_01) else False
        # print(i, last_10, last_01)
        if last_10 != -1:
            if last_01 == -1:
                has_10[i] = True
            elif last_01 > last_10:
                has_10[i] = True
        # has_10[i] = True if last_10 != -1 and (last_10 < last_01) else False
        last_10 = -1
        last_01 = -1

res = []
found = False # first 0/? in s and 1 in n
for i in range(size):
    s_ch, n_ch = str_s[i], str_n[i]
    # not sure s< n
    if not found:
        if s_ch == n_ch:
            res.append(s_ch)
        elif s_ch== '1' and  n_ch == '0':
            print(-1)
            exit()
        elif s_ch== '0' and  n_ch == '1':
            found=True
            res.append(s_ch)
        elif s_ch == '?' and n_ch == '0':
            res.append('0')
        elif s_ch == '?' and n_ch == '1':
            if has_10[i]:
                found=True
                res.append('0')
            else:
                res.append('1')
    else: # found
        if s_ch != '?':
            res.append(s_ch)
        else:
            res.append('1')

res = int(''.join(res), 2)
print(res)