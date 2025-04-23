from sys import stdin
input = stdin.readline

ii = lambda: int(input())
ti = lambda: tuple(map(int, input().split(' ')))
li = lambda: list(map(int, input().split(' ')))
si = lambda: input().strip()
wi = lambda: [w.strip() for w in input().split(' ')]

s = si()
t = si()

def solve(s, t):

    for i in range(len(s)):
        if s[i] != t[i]:
            return i + 1

    return len(s) + 1

print(solve(s, t))