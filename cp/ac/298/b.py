n = int(input())

A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

B = []
for r in range(n):
    B.append(list(map(int, input().split())))

def rotate(M):
    res = []
    for c in zip(*M):
        res.append(c[::-1])
    return res

for i in range(4):
    A = rotate(A)
    valid = True
    for r in range(n):
        for c in range(n):
            if A[r][c] == 1 and B[r][c] != 1:
                valid = False
                break
    if valid:
        print('Yes')
        exit()
        
print('No')

