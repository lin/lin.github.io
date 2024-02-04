h, w = map(int, input().split())

A = []
for _ in range(h):
    A.append(input().strip())

B = []
for _ in range(h):
    B.append(input().strip())

def transform(M, s, t):
    res = [[] for _ in range(h)]
    for i in range(h):
        res[(i+s)%h] = A[i]
    
    for i in range(h):
        row = [''] * w
        for c in range(w):
            row[(c+t)%w] = res[i][c]
        res[i] = ''.join(row)
    
    # print(s, t, res)
    return res

for s in range(0, h):
    for t in range(0, w):
        C = transform(A, s,t)
        valid = True
        for r in range(h):
            if C[r] != B[r]:
                valid=False
                break
        if valid:
            print('Yes')
            exit()

print('No')
