from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    s1 = list(input().strip())
    s2 = list(input().strip())

    diff = set()
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff.add(i)

    t, q = map(int, input().split())

    blocked = deque()

    time = 1
    for _ in range(q):
        query = list(map(int, input().split()))
        # print(time, blocked)
        while blocked and blocked[0][0] <= time:
            _, unblocked_index = blocked.popleft()
            if s1[unblocked_index] != s2[unblocked_index] :
                diff.add(unblocked_index)

        if query[0] == 1:
            blocked_index = query[1] - 1
            blocked.append((time + t, blocked_index))
            if blocked_index in diff:
                diff.remove(blocked_index)
            # print(1, diff)
        elif query[0] == 2:
            # update diff set
            _, which1, index1, which2, index2 = query
            index1 -= 1
            index2 -= 1

            # do the swap
            char1 = s1[index1] if which1 == 1 else s2[index1]
            char2 = s1[index2] if which2 == 1 else s2[index2]

            if which1 == 1:
                s1[index1] = char2
            else:
                s2[index1] = char2
            
            if which2 == 1:
                s1[index2] = char1
            else:
                s2[index2] = char1

            if index1 in diff:
                if s1[index1] == s2[index1]:
                    diff.remove(index1)
            else:
                if s1[index1] != s2[index1]:
                    diff.add(index1)
            
            if index2 in diff:
                if s1[index2] == s2[index2]:
                    diff.remove(index2)
            else:
                if s1[index2] != s2[index2]:
                    diff.add(index2)
            # print(2, diff)
            # print(2, s1, s2)
        else:
            if len(diff) == 0:
                print("YES")
            else:
                print("NO")
            # print(3, diff)

        time += 1