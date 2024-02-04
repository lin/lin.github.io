from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    
    res = 0
    min_val = s[0]
    for i in range(1, n):
        if s[i] <= min_val:
            # print(min_val, i)
            min_val = s[i]
            res = i
    
    print(s[res] + s[:res] + s[res+1:])