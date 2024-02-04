from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter

T = int(input())
for _ in range(T):
    n = int(input())

    data = [[None] * n for _ in range(3)]
    count = Counter()
    for i in range(3):
        data[i] = [w.strip() for w in input().split(' ')]
        for word in data[i]:
            count[word] += 1

    res = []
    for i in range(3):
        score = 0
        for j in range(n):
            k = count[data[i][j]]
            if k == 1:
                score += 3
            elif k == 2:
                score += 1
        res.append(score)
        
    print(*res)