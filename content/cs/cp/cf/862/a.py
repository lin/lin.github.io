from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    res = 0
    for num in nums:
        res ^= num

    if n % 2 == 0:
        if res == 0:
            print(0)
        else:
            print(-1)
    else:
        print(res)