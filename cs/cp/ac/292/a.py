from sys import stdin
input = stdin.readline

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()

s = si()
print(s.upper())