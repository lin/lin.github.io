from sys import stdin
input = stdin.readline

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

n = ii()

MOD = 998244353
prev = ti()
prev_count = [1, 1]
for _ in range(n-1):
    curr = ti()
    count = [0, 0]
    for p in range(2):
        for c in range(2):
            if prev[p] != curr[c]:
                count[c] += prev_count[p]
    prev = curr
    prev_count = count

print((sum(prev_count))%MOD)