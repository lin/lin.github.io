import sys
sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

n,x,y = map(int, input().split())

graph = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

path = [x]
def backtrack(node, parent):
    if node == y:
        print(*path)
        exit(0)
    
    for child in graph[node]:
        if child != parent:
            path.append(child)
            backtrack(child, node)
            path.pop()
        
backtrack(x, 0)