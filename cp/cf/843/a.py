from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

d4 = [(-1,0),(0,1),(1,0),(0,-1)]
d8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

# def find(s, ch):
#     for i in range(1, len(s)-1):
#         if ch == 'a' and s[i] == ch:
#             return i
#         if ch == 'b' and s[i] == ch:
#             return i
        
#     return -1
def find_a(s):
    for i in range(1, len(s)-1):
        if s[i] == 'a':
            return i
    return -1

def solve(s):
    n = len(s)
    first = s[0]
    last = s[-1]

    first_a = find_a(s, 'a')

    if first_a != -1:
        return [s[:first_a], 'a', s[first_a+1:]]
    
    return [first, s[1:-1], last]
    

    # first_b = find(s, 'b')
    
    # if first == 'a' and last == 'a':
    #     return [s[0], s[1:-1], s[-1]] # a<=b c<=b
    
    # if first == 'a' and last == 'b':
    #     if first_a != -1:
    #         return [s[:first_a], 'a', s[first_a+1:]]
    #     if first_b != -1:
    #         return [s[:first_b], s[first_b:-1], 'b']
    # elif first == 'b' and last == 'a':
    #     if first_a != -1:
    #         return [s[:first_a], 'a', s[first_a+1:]]
    #     if first_b != -1:
    #         return ['b', s[first_b:-1], 'a']
    # elif first == 'b' and last == 'b':
    #     if first_a != -1:
    #         return [s[:first_a], 'a', s[first_a+1:]]
    #     if first_b != -1:
    #         return ['b', s[first_b:-1], 'a']


    # return []

for _ in range(ii()):
    s = si()

    res = solve(s)
    if not res:
        print(":(")
    else:
        print(*res)