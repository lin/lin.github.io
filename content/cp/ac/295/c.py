from collections import Counter


n = int(input())

A = list(map(int, input().split()))

cnt = Counter(A)

res = 0 
for key in cnt:
    res += cnt[key] // 2

print(res)