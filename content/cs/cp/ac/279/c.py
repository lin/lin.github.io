h, w = map(int,input().split())

s = [input().strip() for _ in range(h)]
t = [input().strip() for _ in range(h)]
 
sx = [[s[j][i] for j in range(h)] for i in range(w)]
tx = [[t[j][i] for j in range(h)] for i in range(w)]
 
sx.sort()
tx.sort()
 
print("Yes" if sx == tx else "No")