s = input().strip()

if len(s) != 8:
    print('No')
    exit()

a, b = s[0], s[-1]

if not a.isupper() or not b.isupper():
    print('No')
    exit()

num = s[1:-1]
if not num.isdigit() or int(num) < 100000:
    print('No')
    exit()

print("Yes")