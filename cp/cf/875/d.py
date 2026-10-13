for _ in range(int(input())):
    n = int(input())
    
    ta = list(map(int, input().split()))
    tb = list(map(int, input().split()))    
    a = sorted([(x, y) for x, y in zip(ta, tb)])

    A = [pair[0] for pair in a]
    B = [pair[1] for pair in a]
    

    cnt = [0] * (2 * n + 1)
    pr = 0
    res = 0
    
    for i in range(n):
        if pr != A[i]:
            pr = A[i]
            
            # is a_i * a_i > 2*n
            # no solution for b_i
            # this cut the O(n^2) to O(n*sqrt(n))
            if pr * pr > 2 * n:
                break
            
            # brute force to find good b[i]
            cnt = [0] * (2 * n + 1)
            for j in range(i + 1, n):
                target = A[i] * A[j] - B[j]
                if target >= 0 and target <= 2 * n:
                    cnt[target] += 1
        
        res += cnt[B[i]]
        
        # this is for same a_i values
        # if not same cnt value will be emptied.
        # this target is counted prev
        if i < n - 1:
            target = A[i] * A[i+1] - B[i+1]
            if target >= 0 and target <= 2 * n:
                cnt[target] -= 1
    
    print(res)
