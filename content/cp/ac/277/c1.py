from collections import defaultdict, deque


n = int(input())

graph = defaultdict(list)

for _ in range(n):
    a,b = tuple(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])

visited = set([1])

while q:
    node = q.popleft()

    for ch in graph[node]:
        if ch not in visited:
            q.append(ch)
            visited.add(ch)
    
print(max(visited))