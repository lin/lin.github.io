s = input().strip()

n = len(s)

cnt = 0
zzcnt = 0
for ch in s:
    if ch == '0':
        cnt += 1
    else:
        zzcnt += cnt // 2
        cnt = 0
    
zzcnt += cnt // 2

print(n-zzcnt)