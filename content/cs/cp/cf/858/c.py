for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split(' ')))

    max_val = max(nums)
    abs_sum = lambda a, x: sum([abs(i-x) for i in a])
    all_zero = abs_sum(nums, 0)
    all_two = abs_sum(nums, 2)
    minus_one = abs_sum(nums, -1) + abs(max_val-n) - abs(max_val+1) 

    if n == 1:
        print(abs(nums[0] - nums[1]))
    elif n == 2:
        print(min(all_zero, all_two, minus_one))
    elif n & 1:
        print(all_zero)
    else:
        print(min(all_zero, minus_one))