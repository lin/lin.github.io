for _ in range(int(input())):
    n, k = tuple(map(int, input().split()))

    scnt = ecnt = 0
    for _ in range(n):
        s, e = tuple(map(int, input().split()))
        if s == k:
            scnt += 1
        if e == k:
            ecnt += 1
        
    print("YES" if scnt >= 1 and ecnt >= 1 else "NO")