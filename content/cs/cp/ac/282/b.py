from sys import stdin
input = stdin.readline

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

m, n = ti() # h, w
res = 0
for r in range(m):
    s = si()
    for c in range(n):
        if s[c] == '#':
            res += 1
    
print(res)