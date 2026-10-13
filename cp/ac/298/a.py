from collections import Counter
from sys import stdin
input = stdin.readline

from math import *

# for _ in range(int(input())):
n = int(input())
# n, m = map(int, input().split())
s = input().strip()
# nums = list(map(int, input().split()))

cnt = Counter(s)

res = cnt['o'] > 0 and cnt['x'] == 0

print("Yes" if res else 'No')