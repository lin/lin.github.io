n = int(input())

vs = set([0])
path = []
for _ in range(n):
    a, b = tuple(map(int, input().split()))
    vs.add(a-1)
    vs.add(b-1)
    path.append((a-1,b-1))

root = [i for i in range(len(vs))]

rank = {v:i for i, v in enumerate(sorted(list(vs)))}

def find(x):
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]

def union(x, y):
    rx, ry = find(x), find(y)
    if rx != ry:
        root[max(rx, ry)] = min(rx, ry)

for a,b in path:
    union(rank[a],rank[b])

print(max([v for v in vs if find(rank[v]) == 0]) +1)