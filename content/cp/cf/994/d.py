from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations, combinations
from math import *

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

MOD = 998244353

for _ in range(ii()):
    n, x, y = map(int, input().split())
    
    x -= 1
    y -= 1
    ans = [0] * n

    def get_friends(dragon_id):
        friends = []
        friends.append((dragon_id - 1 + n) % n)
        friends.append((dragon_id + 1) % n)
        if dragon_id == x:
            friends.append(y)
        elif dragon_id == y:
            friends.append(x)
        return list(set(friends))

    def mex(arr):
        seen = set(arr)
        i = 0
        while i in seen:
            i += 1
        return i

    def check(arr):
        for i in range(n):
            friends_of_i = get_friends(i)
            friend_values = [arr[f] for f in friends_of_i]
            if arr[i] != mex(friend_values):
                return False
        return True

    if n % 2 == 0:
        for i in range(n):
            ans[i] = i % 2
        print(*ans)
    else:
        for i in range(n - 1):
            ans[i] = i % 2
        ans[n - 1] = 2
        print(*ans)