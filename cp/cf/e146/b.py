from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    res = float('inf')
    for m in range(1, 10 ** 5 * 2):
        res = min(res, m - 1 + (a + m - 1) // m + (b + m - 1) // m)
    print(res)