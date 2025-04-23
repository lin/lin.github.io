from collections import defaultdict
from sys import stdin
input = stdin.readline

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

m, n = ti() # h, w

grid = [[0] * n for _ in range(m)]

for r in range(m):
    s = si()
    for c, ch in enumerate(s):
        grid[r][c] = 0 if ch == 'x' else 1

dic = defaultdict(set)
for r in range(m):
    for c in range(n):
        if grid[r][c] == 1:
            dic[r].add(c)
res = 0
for r1 in range(m):
    for r2 in range(r1+1, m):
        if len(dic[r1] | dic[r2]) == n:
            res += 1
            
print(res)