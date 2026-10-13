h, w = map(int, input().split())

res = [0] * w
for _ in range(h):
    s = input().strip()
    for i, ch in enumerate(s):
        if ch == '#':
            res[i] += 1
print(*res)