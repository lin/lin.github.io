for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split(' ')))
    
    z = nums.count(0)
    o = nums.count(1)

    if 2*z - n <= 1: # 01020
        print(0)
    elif o == 0 or o != n - z: # 00021 / 000000
        print(1)
    else:
        print(2) # 010100