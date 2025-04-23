from collections import deque


n, k = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

q = deque(nums)

while k:
    q.popleft()
    q.append(0)
    k -= 1

print(*q)