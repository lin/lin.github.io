from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    s1 = list(input().strip())
    s2 = list(input().strip())

    n = len(s1)

    same = set()
    diff = set()
    blocked_diff = set() # diff that have been blocked
    for i in range(n):
        if s1[i] == s2[i]:
            same.add(i)
        else:
            diff.add(i)

    t, q = map(int, input().split())

    blocked = deque()

    time = 1
    for _ in range(q):
        query = map(int, input().split())
        while blocked and blocked[0] <= time:
            _, unblocked_index = blocked.pop()
            if unblocked_index in blocked_diff:
                blocked_diff.remove(unblocked_index)

        if query[0] == 1:
            blocked_index = query[1] - 1
            blocked.append((time + t, blocked_index))
            if blocked_index in diff:
                blocked_diff.add(blocked_index)

        elif query[0] == 2:
            # update diff set
            # blocked set is not touched
            # blocked_diff is also not touched
            # only diff is touched
            # we may increase diff size or decrease diff size

            _, which1, which2, index1, index2 = query
            index1 -= 1
            index2 -= 1


            if which1 != which2:
                ch1 = s1[index1] if which1 == 1 else s2[index1]
                ch2 = s1[index2] if which2 == 1 else s2[index2]

            else:

            if ch1 == ch2:
                continue

        else:
            # I wish I can check diff is all been blocked
            # in O(1) time
            # if diff.issubset(blocked):
            if len(blocked_diff) == len(diff):
                print("YES")
            else:
                print("NO")

        time += 1

    




