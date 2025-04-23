from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    s = input().strip()
    print("No" if len(set([s[i] for i in range(len(s)//2)])) == 1 else "Yes")