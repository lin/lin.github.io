n, m = tuple(map(int, input().split()))

data = []
for _ in range(m):
    c = int(input())
    data.append(set(map(int, input().split())))

cnt = 0
for i in range(1, 1<<m):
    s = set()
    for j in range(m):
        if (1<<j) & i:
            s |= data[j]
    if len(s) == n:
        cnt += 1 
    
print(cnt)
