

T = int(input())
for _ in range(T):
    n = int(input())

    if n % 2 == 0:
        print(n // 2)
    else:
        print(n // 2 + 1)

    if n == 1:
        print(1, 2)
        continue
    
    for i in range(n // 2):
        print(3 * i + 2, 3 * (n // 2 * 2- 1 - i) + 3)

    # for odd
    if n % 2:
        print(3 * (n // 2) + 2, 3 * n)
