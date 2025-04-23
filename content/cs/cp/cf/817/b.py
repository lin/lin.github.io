from sys import stdin
input = stdin.readline


T = int(input())
for _ in range(T):
    n = int(input())
    s1 = input().strip()
    s2 = input().strip()

    def simplify(s):
        temp = []
        for ch in s:
            if ch == "G":
                temp.append("B")
            else:
                temp.append(ch)
        return ''.join(temp)

    s1 = simplify(s1)
    s2 = simplify(s2)

    print("YES" if s1 == s2 else "NO")