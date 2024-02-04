# from collections import * # defaultdict, Counter, deque, OrderedDict
# from sortedcontainers import SortedList
# from heapq import *
# from functools import lru_cache
# from bisect import *
# from itertools import accumulate, permutations, combinations


from math import *

T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split(' '))) # list of nums
    
    psum = [0]
    for num in nums:
        psum.append(psum[-1] + num)
    
    res = -inf
    for i in range(n + 1):
        a = abs(psum[i])
        b = abs(psum[-1] - psum[i])
        res = max(res, a - b)
    
    print(res)