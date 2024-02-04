for _ in range(int(input())):
    n = int(input())
    s = input()

    cost = [0] * (n + 1)

    for i in range(n):
        if s[i] == '1':
            continue

        j = i + 1
        while j <= n and s[j - 1] == '0':
            if cost[j] == 0:
                cost[j] = i + 1
            j += i + 1

    print(sum(cost))


