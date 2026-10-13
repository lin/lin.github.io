n, q = map(int, input().split())

db = set()
for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        db.add((a,b))
    elif t == 2:
        db.discard((a,b))
    else:
        res = (a,b) in db and (b,a) in db
        print("Yes" if res else "No")