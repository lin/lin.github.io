"""
    Author : Afsan Habib
    Mail   : afsan.uct@gmail.com
    GitHub : https://github.com/afsanhabib
"""
import sys
import os
import collections
from random import randint, shuffle
from io import BytesIO, IOBase
from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
from functools import lru_cache
from itertools import accumulate, permutations
import math,cmath,time

#_______________________________________________
MOD=10**9+7
MAX_INT=9223372036854775807
MIN_INT=-9223372036854775807
yes="YES"
no="NO"

#_____________Some Necessary Functions___________

def seive_of_eratosthenes(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(n**0.5)+1):
        for j in range(2*i, n+1, i):
            is_prime[j] = False

    return is_prime

def bubbleSort(arr):
    n=len(arr)
    for i  in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def counter(a):
    q = [0] * max(a)
    for i in range(len(a)):
        q[a[i] - 1] = q[a[i] - 1] + 1
    return(q)


def prefix_sums(a):
    p = [0]
    for x in a:
        p.append(p[-1] + x)
    return p
 
def counter_elements(a):
    q = dict()
    for i in range(len(a)):
        if a[i] not in q:
            q[a[i]] = 0
        q[a[i]] = q[a[i]] + 1
    return(q)
 
def string_counter(a):
    q = [0] * 26
    for i in range(len(a)):
        q[ord(a[i]) - 97] = q[ord(a[i]) - 97] + 1
    return(q)

def factorial(n,m = 1000000007):
    q = 1
    for i in range(n):
        q = (q * (i + 1)) % m
    return(q)
 
def factors(n):
    q = []
    for i in range(1,int(n ** 0.5) + 1):
        if n % i == 0: q.append(i); q.append(n // i)
    return(list(sorted(list(set(q)))))
 
def prime_factors(n):
    q = []
    while n % 2 == 0: q.append(2); n = n // 2
    for i in range(3,int(n ** 0.5) + 1,2):
        while n % i == 0: q.append(i); n = n // i
    if n > 2: q.append(n)
    return(list(sorted(q)))
 
def transpose(a):
    n,m = len(a),len(a[0])
    b = [[0] * n for i in range(m)]
    for i in range(m): 
        for j in range(n): 
            b[i][j] = a[j][i]
    return(b)

def Sub_Array_Max_Sum(arr, k):
    n = len(arr)
    if n < k:
        print("Invalid")
        return -1
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)
    return max_sum

def inversePermutation(arr, size):
 for i in range(0, size):
    for j in range(0, size):
        if (arr[j] == i + 1):
            print(j + 1, end = " ")
            break

#_____________End Necessary Functions________________________


#_____________Start Fast Input Output Functions________________


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        import os
        self.os = os
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
        self.BUFSIZE = 8192

    def read(self):
        while True:
            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, self.BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, self.BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            self.os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")


def input_int_num():
    return (int(input()))

def input_int_list():
    return list(map(int, input().split()))
 
def input_string_list():
    return list(map(str, input().split()))
 
def input_int_map():
    return(map(int,input().split()))

def input_strip_string():
    return (input().strip())

#______________End Fast Input Output Functions_________________


#______________________Start Solve Functions_______________________


def solve():
    n=int(input())
    lst=list(map(int, input().split()))

    mini=min(lst)
    indx=lst.index(mini)

    fist=lst[:indx+1]
    last=lst[indx:]


    if last==sorted(last) and fist==sorted(fist,reverse=True):
        print("YES")
    else:
        print("NO")

    



''' input





'''

#___________End Solve Functions___________#
 


#___________Start Main Functions___________#

def main():
    # solve()
    # return

    Test_Case=int(input())
    while Test_Case:
        solve()
        Test_Case -= 1
    return

 
if __name__ == "__main__":
    main()
#___________End Main Functions___________#