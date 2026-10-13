from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque

for _ in range(int(input())):
    n = int(input())
    s = input().strip()

    st = set()
    for i in range(n-1):
        curr = s[i:i+2]
        st.add(curr)
      
    print(len(st))