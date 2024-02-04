from sys import stdin
input = stdin.readline

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

n = ii()
nums = li()

res = [nums[0]]
for i in range(1, n):
    res.append(nums[i] - nums[i-1])
print(*res)