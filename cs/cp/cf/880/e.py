from sys import stdin
input = stdin.readline

class SEG:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * 2 * self.n
       
    def query(self, l, r):
        l += self.n
        r += self.n
        res = 0
        while l <= r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if r & 1 == 0:
                res += self.tree[r]
                r -= 1
            l >>= 1
            r >>= 1
        return res
    
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]


from math import *
from collections import defaultdict, Counter, deque

for _ in range(int(input())):
    n, k = map(int, input().split())
    n = int(input())
    A = list(map(int, input().split()))
    s = input().strip()

