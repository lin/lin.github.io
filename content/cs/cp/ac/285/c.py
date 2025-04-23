s = input().strip()

res = 0
for i, ch in enumerate(s[::-1]):
    res += 26**i * (ord(ch) - ord('A') + 1)
print(res)