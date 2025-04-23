from collections import Counter


n, m = tuple(map(int, input().split()))

root = [i for i in range(n)]

def find(x):
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]

def union(x, y):
    root_x, root_y = find(x), find(y)

    if root_x != root_y:
        root[max(root_x, root_y)] = min(root_x, root_y)

for _ in range(m):
    a, b = tuple(map(int, input().split()))
    union(a-1, b-1)

print(len(Counter([find(i) for i in range(n)])))
