n = int(input())
stack = []
for _ in range(n):
    stack.append(input().strip())


while stack:
    print(stack.pop())