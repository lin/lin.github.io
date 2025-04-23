N = int(input())
S = [(input(), i) for i in range(N)]
 
S.sort()
S.append(("", N))
 
def LCP(S1, S2):
    rtn = 0
    for i in range(min(len(S1), len(S2))):
        if S1[i] != S2[i]:
            break
        rtn += 1
    return rtn
 
A = [0 for i in range(N)]
for i in range(N):
    A[S[i][1]] = max(LCP(S[i - 1][0], S[i][0]), LCP(S[i][0], S[i + 1][0]))
 
print(*A, sep="\n")