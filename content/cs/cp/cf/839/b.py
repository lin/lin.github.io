for _ in range(int(input())):
    a, b = tuple(map(int, input().split()))
    c, d = tuple(map(int, input().split()))
    mi = min(a,b,c,d)
    ma = max(a,b,c,d)
    if (a == mi and d == ma) or (b == mi and c == ma) \
        or (c == mi and b == ma) or (d == mi and a == ma):
        print("Yes")
    else:
        print("No")
