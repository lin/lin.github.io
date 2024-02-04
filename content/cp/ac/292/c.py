import math

n = int(input())

res = 0
for i in range(1,n):
    X = i
    Y = n-i
    
    x = 0
    for j in range(1, int(math.sqrt(X))+1):
        if X % j == 0:
            x += 1
            if X != j*j:
                x += 1
    
    y = 0
    for j in range(1, int(math.sqrt(Y))+1):
        if Y % j == 0:
            y += 1
            if Y != j*j:
                y += 1
    res += x * y

print(res)