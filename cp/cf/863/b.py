from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n, x1,y1,x2,y2 = map(int, input().split())

    mn1, mx1 = min(x1, y1), max(x1, y1)
    mn2, mx2 = min(x2, y2), max(x2, y2)

    c1 = min(mn1, n - mx1 + 1)
    c2 = min(mn2, n - mx2 + 1)

    print(abs(c2 - c1))