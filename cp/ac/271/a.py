n = int(input())

d, m = divmod(n, 16)

def d2x(d):
    if d <= 9:
        return str(d)
    return chr(ord('A') + d - 10)

print(d2x(d) + d2x(m))