from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    B = list(map(int, input().split()))

    res = [B[0]]
    for i in range(n-2):
        if B[i] <= B[i+1]:
            res.append(B[i])
        else:
            res.append(B[i+1])
        
    res.append(B[-1])
        
    print(*res)