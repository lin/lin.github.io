from math import *

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    min_val, max_val = 10**9, 0
    for i in range(n-1):
        half = (nums[i] + nums[i+1])/2
        if nums[i] > nums[i+1]:
            max_val = max(max_val, ceil(half))
        if nums[i] < nums[i+1]:
            min_val = min(min_val, floor(half))
    
    if max_val <= min_val:
        print(max_val)
    else:
        print(-1)