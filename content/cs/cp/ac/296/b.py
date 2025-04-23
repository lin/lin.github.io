from sys import stdin
input = stdin.readline

from math import *

# for _ in range(int(input())):
# n = int(input())
# n, m = map(int, input().split())
s = input().strip()
# nums = list(map(int, input().split()))

bs = []
rs = []
k =None
for i, ch in enumerate(s):
    if ch == 'B':
        bs.append(i)
    elif ch == 'R':
        rs.append(i)
    elif ch == 'K':
        k = i

    
cond1 = bs[0]%2 != bs[1] %2

cond2 = rs[0] < k < rs[1]

res = cond1 & cond2

print("Yes" if res else 'No')

