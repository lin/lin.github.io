from re import L


n, q = tuple(map(int, input().split(' ')))
arr = list(map(int, input().split(' ')))

for _ in range(q):
    l, r = tuple(map(int, input().split(' ')))
    print(l, r)
    i = l
    res = 0
    while i < r:

        curr = 0
        while not curr:
            curr ^= arr[i] + arr[i+1]
            i += 2