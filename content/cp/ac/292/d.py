from collections import Counter
from sys import stdin
input = stdin.readline

from math import *

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()

n, m = ti()

root = [i for i in range(n)]
        
def find(x):
    if x == root[x]:
        return x
    root[x]= find(root[x])
    return root[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        remained_root, changed_root =  min(root_x, root_y), max(root_x, root_y)
        root[changed_root] = remained_root

edge_count = Counter()
for _ in range(m):
    a, b = ti()
    a -= 1
    b -= 1
    union(a, b)
    edge_count[a] += 1
    edge_count[b] += 1

vc = Counter()
ec = Counter()
for i in range(n):
    group = find(i)
    vc[group] += 1
    ec[group] += edge_count[i]

for key in vc:
    if vc[key] != ec[key]//2:
        print("No")
        exit()

print("Yes")