for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))

    if max(A) == 0:
        print("No")
        continue

    pos = []
    neg = []
    for a in A:
        if a >= 0:
            pos.append(a)
        else:
            neg.append(a)

    res = []
    psum = 0
    for _ in range(n):
        if psum <= 0:
            res.append(pos.pop())
        else:
            res.append(neg.pop())
        psum += res[-1]

    print("Yes")
    print(' '.join(list(map(str, res))))