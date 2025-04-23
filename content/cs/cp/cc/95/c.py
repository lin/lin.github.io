for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    
    mx = max(A)
    mx_bit = 60
    while mx & 1<<mx_bit == 0:
        mx_bit -= 1
    
    cnt = 0
    for a in A:
        if a & 1<<mx_bit:
            cnt += 1
    
    print((cnt+1)//2)