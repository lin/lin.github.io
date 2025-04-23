for _ in range(int(input())):
    s = list(input().strip())
    n = len(s)
    s.sort()

    front = []
    rear = []

    i = 0
    while i < n - 1:
        if s[i] != s[i+1]:
            break
        front.append(s[i])
        rear.append(s[i])
        i += 2
    
    if i >= n - 2: 
        # EF / EE / E / F
        mid = ''.join(s[i:][::-1])
    else:
        if s[i+1] != s[-1]:
            # EFGGGGG / EFGGHHHIIIII
            mid = ''.join(s[i+1:]) + s[i]
        else:
            # EFFFF / EFFFFF
            half_count = (n - i) // 2
            mid = ''.join(s[i+1:i+1+half_count]) + s[i] + ''.join(s[i+1+half_count:])

    print(''.join(front) + mid + ''.join(rear[::-1]))