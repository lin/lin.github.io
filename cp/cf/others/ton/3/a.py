T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split(' '))) # list of nums

    if nums[0] == min(nums):
        print("Yes")
    else:
        print("No")