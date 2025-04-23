from collections import defaultdict

n = int(input())

vs = set()
path = []
for _ in range(n):
    a, b = tuple(input().split())
    vs.add(a)
    vs.add(b)
    path.append((a,b))

root = [i for i in range(len(vs))]

rank = {v:i for i, v in enumerate(sorted(list(vs)))}

def find(x):
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]

def union(x, y):
    root_x, root_y = find(x), find(y)

    if root_x == root_y:
        return False
    
    old_root, new_root = min(root_x, root_y), max(root_x, root_y)
    root[new_root] = old_root

    return True

for a, b in path:
    if not(union(rank[a], rank[b])):
        print("No")
        exit()

print("Yes")