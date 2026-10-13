a, x, m = tuple(map(int, input().split(' ')))

if a == 1: 
    print(x%m)
    exit()

# a/b % m == t means
# => a == b * (k * m + t) to solve t
# => a == b * k * m + b * t == k * b * m + b * t
# => a % (b*m) == b * t
# => a % (b*m) / b == t
# so a/b % m == a % (b*m) / b

m = m * (a - 1)
print((pow(a, x, m) - 1) % m // (a - 1))