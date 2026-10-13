from sys import stdin
input = stdin.readline

from math import *
from collections import defaultdict, Counter, deque

from sys import stdout

room = int(input())

while True:
    k = 1
    print('+', k)
    stdout.flush()

    room = int(input())
    
    if k == 3:
        print("!", 1)
        stdout.flush()
        break