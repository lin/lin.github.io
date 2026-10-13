n, m = tuple(map(int, input().split()))
nums = set(map(int, input().split()))


res = []
start = 0
for i in range(1, n+1):
    if i not in nums:
        res += [k for k in range(i, start, -1)]
        start = i
        
print(*res)