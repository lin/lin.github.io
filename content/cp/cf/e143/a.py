# 10m 3s
for _ in range(int(input())):
    n, m = tuple(map(int, input().split()))

    s = input().strip()
    t = input().strip()

    a = s + t[::-1]

    cnt = 0
    for i in range(n+m-1):
        if a[i] == a[i+1]:
            cnt += 1
    
    print("YES" if cnt <= 1 else "NO")