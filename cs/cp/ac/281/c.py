n, t = tuple(map(int, input().split()))

nums = list(map(int, input().split()))
t = t%sum(nums)

psum = 0
for i, num in enumerate(nums):
    if t > psum + num:
        psum += num
    else:
        print(i+1, t-psum)
        exit()