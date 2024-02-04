n = int(input())
W = list(input().split())

words = set(["and", "not", "that", "the", "you"])

for w in W:
    if w in words:
        print("Yes")
        exit()

print("No")