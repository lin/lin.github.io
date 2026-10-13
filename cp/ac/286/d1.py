n, x = map(int, input().split())
s = 1 << x
for _ in range(n):
    a, b = map(int, input().split())
    for _ in range(b):
        s |= s >> a
print("Yes" if s & 1 else "No")