def main():
    import sys
    input = sys.stdin.readline
 
    def PrimeDecomposition(N):
        ret = {}
        n = int(N ** 0.5)
        for d in range(2, n + 1):
            while N % d == 0:
                if d not in ret:
                    ret[d] = 1
                else:
                    ret[d] += 1
                N //= d
            if N == 1:
                break
        if N != 1:
            ret[N] = 1
        return ret
 
    K = int(input())
 
    P = PrimeDecomposition(K)
 
    ok = K
    ng = 1
    mid = (ok + ng) // 2
    while ok - ng > 1:
        flg = 1
        for p in P:
            cnt = 0
            M = mid
            while M:
                cnt += M // p
                M //= p
            if cnt < P[p]:
                flg = 0
                break
        if flg:
            ok = mid
        else:
            ng = mid
        mid = (ok + ng) // 2
    print(ok)
 
 
if __name__ == '__main__':
    main()
