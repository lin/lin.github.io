from collections import defaultdict

n, m = map(int, input().split())

graph = defaultdict(set)

for _ in range(m):
    lst = list(map(int, input().split()))
    k = lst[0]
    for i in range(1, k+1):
        for j in range(i+1, k+1):
            graph[lst[i]].add(lst[j])
            graph[lst[j]].add(lst[i])

for i in range(n):
    if len(graph[i+1]) != n- 1:
        print("No")
        exit()
print("Yes")

