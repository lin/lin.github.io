for _ in range(int(input())):
    a, b = map(int, input().split())
    a, b = abs(a), abs(b)
    diff = abs(a-b)
    total = a + b
    print(total + max(diff - 1, 0))