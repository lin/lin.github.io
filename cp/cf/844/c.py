from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

d4 = [(-1,0),(0,1),(1,0),(0,-1)]
d8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

# based on @asdsasd https://codeforces.com/contest/1782/submission/189316756
def solve(n, s):
    ords = [ord(ch) - ord('a') for ch in s]
    count = [0] * 26
    for a in ords:
        count[a] += 1
    sorted_count_with_index = sorted([(c, i) for i, c in enumerate(count)], reverse=True)

    min_diff = n + 1
    min_size = -1
    # size means how many diff chars in s
    # k is how many chars for each dist char
    for size in range(1, 27):
        if n % size == 0:
            k = n // size
            diff = 0

            for j in range(size):
                diff += max(0, sorted_count_with_index[j][0] - k)

            for j in range(size, 26):
                diff += sorted_count_with_index[j][0]

            if diff < min_diff:
                min_diff = diff
                min_size = size

    min_k = n // min_size
    move = [0] * 26
    to = []
    for i in range(min_size):
        c, j = sorted_count_with_index[i]
        if c >= min_k:
            move[j] = c - min_k
        else:
            to += [j] * (min_k - c)

    for i in range(min_size, 26):
        c, j = sorted_count_with_index[i]
        move[j] = c

    for i, a in enumerate(ords):
        if move[a] > 0:
            move[a] -= 1
            ords[i] = to.pop()
 
    return min_diff, ''.join([chr(a + ord('a')) for a in ords])

for _ in range(ii()):
    n = ii()
    #a, b, c = ti()
    s = si()
    #nums = li()

    res = solve(n, s)
    print(res[0])
    print(res[1])
    # print(*res)
    # print("YES" if res else "NO")