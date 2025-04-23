for _ in range(int(input())):
    n = int(input())
    if n < 7:
        print(-1)
        continue

    while 3 > bin(n).count('1'):
        n -= 1

    if  bin(n).count('1') > 3:
        for _ in range(bin(n).count('1') - 3):
            n = n & (n-1)

    print(n)
