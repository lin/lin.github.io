for _ in range(int(input())):
    k, n = tuple(map(int, input().split()))
    
    d = 0
    res = [1]
    while len(res) < k:
        if res[-1] + d + k - len(res) <= n:
            d += 1
        else:
            d = 1
        res.append(res[-1] + d)

    print(*res)