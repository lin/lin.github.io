# Fibonacci

from sys import stdin
input = stdin.readline

fib = [1] * 46
for i in range(2, 46):
    fib[i] = fib[i-1] + fib[i-2]

for _ in range(int(input())):
    n, x, y = map(int, input().split())

    res = True
    for i in range(n, 1, -1):
        if (n-i) % 2 == 0:
            if y > fib[i]:
                y -= fib[i]
            elif y > fib[i-1]:
                res = False
                break
        else:
            if x > fib[i]:
                x -= fib[i]
            elif x > fib[i-1]:
                res = False
                break

    print("Yes" if res else "No")
