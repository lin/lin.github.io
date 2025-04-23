from collections import defaultdict
from sys import stdin
input = stdin.readline

from math import *

for _ in range(int(input())):
    # n = int(input())
    n, k, c = map(int, input().split())
    # s = input().strip()
    # nums = list(map(int, input().split()))
    graph = defaultdict(list)

    # level(node) + longest(node)