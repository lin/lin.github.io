from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

dir4 = [(-1,0),(0,1),(1,0),(0,-1)]
dir8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split(' '))) # list of nums

    psum = [0]
    for num in nums:
        psum.append(psum[-1] + num)
    
    res = 0

    count = Counter()
    max_val = 0
    for i in range(n, 0, -1):
        count[psum[i]] += 1
        if count[psum[i]] > max_val:
            max_val = count[psum[i]]
        
        if nums[i - 1] == 0:
            res += max_val
            max_val = 0
            count = Counter()
        
    print(res + count[0])