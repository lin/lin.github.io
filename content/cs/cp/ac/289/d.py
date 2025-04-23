from functools import lru_cache

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = set(map(int, input().split()))

x = int(input())

@lru_cache(None)
def dp(s):
    if s == 0:
        return True

    for a in A:
        curr = s - a
        if curr not in B and curr >= 0:
            if dp(curr):
                return True
    return False

print("Yes" if dp(x) else 'No')