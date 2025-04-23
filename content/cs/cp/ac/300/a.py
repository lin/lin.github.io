n,a,b = map(int, input().split())

A = list(map(int, input().split()))

for i in range(1, n+1):
    if A[i-1] == a+b:
        print(i)
        exit()