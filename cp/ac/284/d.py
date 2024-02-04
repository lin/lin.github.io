for _ in range(int(input())):
    n = int(input())

    for i in range(2, int(n**(1/3)) + 1):
        if n % i == 0:
            if n % i**2 == 0:
                print(i, n//(i**2))
            else:
                print(int((n//i)**(1/2)), i)