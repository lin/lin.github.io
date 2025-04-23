n = int(input())

def dp(x):
    if x == 0:
        return 1
    return x * dp(x-1)

print(dp(n))