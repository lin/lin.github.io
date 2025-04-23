for _ in range(int(input())):
    n = int(input())
    print("1")
    for i in range(2, n + 1):
        print("1" + " 0" * (i - 2) +" 1")