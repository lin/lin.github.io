s = input().strip()

n = len(s)

sets = [set() for _ in range(n)]

seen = [False for _ in range(26)]

curr = 0
for ch in s:
    if ch == '(':
        curr += 1
    elif ch == ')':
        for c in sets[curr]:
            seen[ord(c) - ord('a')] = False
        sets[curr] = set()
        curr -= 1
    else:
        if seen[ord(ch) - ord('a')]:
            print('No')
            exit()
        seen[ord(ch) - ord('a')] = True
        sets[curr].add(ch)
    
print("Yes")