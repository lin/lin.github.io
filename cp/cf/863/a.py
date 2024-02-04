from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n, d = map(int, input().split())
    x = int(input())

    s = str(x)
    res = n
    for i, ch in enumerate(s):
        if int(ch) < d:
            res = i
            break
    
    print(s[:res] + str(d) + s[res:])