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

n = ii()

data = []
for _ in range(n):
    s = [ord(i) - 97 for i in si()]
    k = len(s)

    xor_sum = 0 # even or odd
    or_sum = 0 # present or not
    for i in s:
        xor_sum ^= 1<<i
        or_sum |= 1<<i

    data.append((xor_sum, or_sum))


res = 0
# for each missing character
for i in range(26):
    curr = []
    for x, y in data:
        # consider those missing i-th character
        if (y>>i) & 1:
            continue
        curr.append(x)

    mask = (1<<26) - 1 - (1<<i)

    # two sum
    cnt = defaultdict(int)
    for x in curr:
        res += cnt[mask-x]
        cnt[x] += 1

print(res)