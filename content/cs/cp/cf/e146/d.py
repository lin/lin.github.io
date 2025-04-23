from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    n, m = map(int, input().split())
    s = input().strip()
    nums = list(map(int, input().split()))