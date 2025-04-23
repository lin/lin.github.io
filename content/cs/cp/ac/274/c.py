n = int(input())
A = list(map(int, input().split()))

res = [0] * (2*n+1)

for i, a in enumerate(A):
    curr = res[a-1]
    res[2*i+1] = curr + 1
    res[2*i+2] = curr + 1

for r in res:
    print(r)
