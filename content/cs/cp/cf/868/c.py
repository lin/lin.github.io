from collections import Counter
from sys import stdin
input = stdin.readline

from math import *

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))

    # O(N^2)

    # if a number is product of two primes or a single prime
    # it is not strongly composite

    cnt = Counter()

    def factors(x):
        for i in range(2, int(sqrt(x)) + 1):
            while x % i == 0:
                cnt[i] += 1
                x //= i
        if x > 1:
            cnt[x] += 1

    for a in A:
        factors(a)

    res = 0
    ones = 0
    for val in cnt.values():
        res += val // 2
        ones += val % 2
    
    res += ones // 3

    print(res)