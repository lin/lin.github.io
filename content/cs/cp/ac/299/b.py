from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n = int(input())

from sys import stdout

left = 1
right = n
 
seen = {}
while left <= right:
    mid = (left + right) // 2

    print('?', mid)
    stdout.flush()

    response = input().strip()
    seen[mid] = response
    if mid - 1 in seen and seen[mid-1] != seen[mid]:
        print("!", mid-1)
        exit()
    if mid + 1 in seen and seen[mid] != seen[mid+1]:
        print("!", mid)
        exit()
    # there is one valid to the left
    if response == '1':
        right = mid
    # there is one valid to the right
    else:
        left = mid + 1