T = int(input())
for _ in range(T):
    n = int(input())
    # nums = list(map(int, input().split(' '))) # list of nums
    s = input().strip()

    s = ''.join(sorted(s))
    if s == "Timru":
        print("YES")
    else:
        print("NO")