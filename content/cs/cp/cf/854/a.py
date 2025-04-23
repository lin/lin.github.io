# 16m45s
for _ in range(int(input())):
    n, m = tuple(map(int, input().split()))
    nums = list(map(int, input().split()))

    seen = set()
    res = [-1] * n
    curr = n
    for i, num in enumerate(nums):
        if num not in seen and curr > 0:
            res[curr-1] = i + 1
            curr -= 1
        seen.add(num)

    print(*res)