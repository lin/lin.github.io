from sys import stdin
input = stdin.readline

n, k = tuple(map(int, input().split(' ')))

s = input().strip()

res = []
cnt = 0
for i, ch in enumerate(s):
    if ch == 'o':
        cnt += 1
        res.append('o' if cnt <= k else 'x')
    else:
        res.append('x')
    
print(''.join(res))
