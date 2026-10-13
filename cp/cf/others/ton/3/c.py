from sys import stdin
input = stdin.readline

def get_ranges(s):
    res = []
    start = None
    end = None
    for i, ch in enumerate(s):
        if ch == '1':
            if not start:
                start = i + 1
                end = None
            if i == len(s) - 1:
                res.append([start, i + 1])
        else:
            if start and not end:
                res.append([start, i])
                start = None
                end = i
    return res

T = int(input())
for _ in range(T):
    n = int(input())
    a = input().strip()
    b = input().strip()

    temp = []
    for ch in b:
        if ch == '0':
            temp.append('1')
        else:
            temp.append('0')

    flip_b = ''.join(temp)

    ranges = get_ranges(a)
    k = len(ranges)
    if a == flip_b:
        print('YES')
        if k > 0:
            print(k if k % 2 == 1 else k + 3)
            for i in range(k):
                print(ranges[i][0], ranges[i][1])
            if k % 2 == 0:
                print(1, 1)
                print(1, n)
                print(2, n)
        else:
            print(3)
            print(1, 1)
            print(1, n)
            print(2, n)
    elif a == b:
        print('YES')
        if k > 0:
            print(k if k % 2 == 0 else k + 3)
            for i in range(k):
                print(ranges[i][0], ranges[i][1])
            if k % 2 == 1:
                print(1, 1)
                print(1, n)
                print(2, n)
        else:
            print(0)
    else:
        print('NO')