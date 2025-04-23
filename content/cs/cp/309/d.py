from sys import stdin
input = stdin.readline

from collections import defaultdict, Counter, deque

n1, n2, m = map(int, input().split())


graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# bfs for 1
q1 = deque([(1, 0)])
seen1 = set([1])
max1 = 0
while q1:
    node, level = q1.popleft()
    max1 = max(max1, level)

    for neigh in graph[node]:
        if neigh not in seen1:
            seen1.add(neigh)
            q1.append((neigh, level+1))

q2 = deque([(n1+n2, 0)])
seen2 = set([n1+n2])
max2 = 0
while q2:
    node, level = q2.popleft()
    max2 = max(max2, level)

    for neigh in graph[node]:
        if neigh not in seen2:
            seen2.add(neigh)
            q2.append((neigh, level+1))

print(max1 + max2 + 1)


