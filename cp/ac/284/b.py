for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    for num in nums:
        if num & 1:
            cnt += 1
    
    print(cnt)