n = int(input())
s = input().strip()

for k in range(1, n):
    cnt = 0
    for j in range(n-k):
        if s[j] != s[j+k]:
            cnt +=1
        else:
            break
    print(cnt)