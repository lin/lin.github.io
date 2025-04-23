# 18:29
import math

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    gcd_val = math.gcd(*nums)
    max_val = max(nums)
    
    print(max_val // gcd_val)