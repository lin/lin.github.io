from itertools import accumulate
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    
    psum = list(accumulate(A, initial=0))

    print(max([psum[n - (k - i)] - psum[i*2] for i in range(k+1)]))