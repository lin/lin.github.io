from collections import Counter

n = int(input())
nums = list(map(int, input().split()))

cnt = Counter(nums)

res = [0] * n

c = 0
for key in sorted(cnt, reverse=True):
    c += 1
    res[-c] = cnt[key]

for r in res[::-1]:
    print(r)