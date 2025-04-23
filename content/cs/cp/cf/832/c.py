T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split(' ')))

    if arr[0] == min(arr):
        print('Bob')
    else:
        print('Alice')
