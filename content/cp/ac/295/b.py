r, c = map(int, input().split())

B = []

for _ in range(r):
    B.append(list(input().strip()))

exploded = [[False] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        ch = B[i][j]

        if ch.isdigit():
            p = int(ch)
            for pi in range(r):
                for pj in range(c):
                    if abs(i-pi) + abs(j-pj) <= p:
                        exploded[pi][pj] = True

for i in range(r):
    for j in range(c):
        if exploded[i][j]:
            B[i][j] = '.'
        
for b in B:
    print(''.join(b))