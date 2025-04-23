n = int(input())
nums = list(map(int, input().split()))

odds = []
evens = []
for num in nums:
    if num & 1:
        odds.append(num)
    else:
        evens.append(num)
    
odds.sort()
evens.sort()

res = -1
if len(odds) >= 2:
    res = max(res, odds[-1]+odds[-2])
if len(evens) >= 2:
    res = max(res, evens[-1]+evens[-2])

print(res)