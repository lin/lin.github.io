from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

n, m = map(int, input().split())

root = [i for i in range(n)]

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(x, y):
    rx, ry = find(x), find(y)
    root[max(rx, ry)] = min(rx, ry)

for _ in range(m):
    u, v = map(int, input().split())
    union(u-1, v-1)

# print(root)

group_dic = {}
for i in range(n):
    group_dic[i] = find(i)

groups = Counter([group_dic[i] for i in range(n)])

group_keys = groups.keys()
group_key_dic = {}

for i, key in enumerate(sorted(group_keys)):
    group_key_dic[key] = i

banned = set()
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    gx, gy = group_key_dic[group_dic[x-1]], group_key_dic[group_dic[y-1]]
    banned.add((gx, gy))
    banned.add((gy, gx))

q = int(input())
for _ in range(q):
    p, q = map(int, input().split())
    gp, gq = group_key_dic[group_dic[p-1]], group_key_dic[group_dic[q-1]]
    if (gp, gq) in banned: 
        print('No')
    else:
        print('Yes')