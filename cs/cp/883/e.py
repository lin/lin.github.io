from sys import stdin
input = stdin.readline

from collections import defaultdict, Counter, deque


for _ in range(int(input())):
    n = int(input())

    found = False
    for m in range(3, n.bit_length()+1):
        k = int(pow(n, 1 / (m - 1)))
        if n == (pow(k, m) - 1) // (k - 1):
            found = True
            break

    print("YES" if found else "NO")


