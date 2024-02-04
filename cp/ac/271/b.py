n, q = map(int, input().split())

data = [[] for _ in range(n)]
for i in range(n):
    data[i] = list(map(int, input().split()))

for _ in range(q):
    s, t = map(int, input().split())
    print(data[s-1][t]) 