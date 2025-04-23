from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())

    # to base 9
    base9 = []
    while n:
        base9.append(n%9)
        n //= 9
    
    res = 0
    for i in range(len(base9)):
        res += 10**i * (base9[i] + (base9[i] >= 4))
    
    print(res)

    
