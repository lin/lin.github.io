from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    l, r = map(int, input().split())
    ls, rs = str(l).zfill(100), str(r).zfill(100)
    
    no_diff = True
    no_first = True
    res = 0
    for i in range(100):
        char_l, char_r = ls[i], rs[i]
        if char_l == char_r and no_diff:
            continue
        no_diff = False
        if no_first:
            res += int(char_r) - int(char_l)
            no_first = False
        else:
            res += 9
    
    print(res)
        

            # 09 53 no need to change 1
            # if int(char_l) != 0:
            #     res += int(char_r) - int(char_l)
            # else: # edge cases
            #     # 002 344
            #     if i != 99 and int(ls[i+1]) == 0:
            #         res += int(char_r)
            #     # 023 344
            #     else:
            #         res += int(char_r)


