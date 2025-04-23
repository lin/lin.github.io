from collections import Counter
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = input().strip()

    if n % 2 == 1 or max(Counter(s).values())>n//2:
        print(-1)
        continue
    
    cnt = Counter()
    mx = tot = 0
    for i in range(n//2):
        if s[i] == s[~i]:
            cnt[s[i]] += 1
            mx = max(mx, cnt[s[i]])
            tot += 1

    # AA AAA BCD XY
    # AA BCD AAA YX
    # there has to be a ch we can exchange A
    # otherwise we have more than half A

    # A AAABB BCCCD
    # =>
    # A BCCCD AAABB
    # => 
    # A AAABCCCDBB
    # A BCCAAABBCD
    # there has to be a ch we can exchange A
    # otherwise we have more than half A

    print(mx if mx > tot//2 else (tot+1)//2)

    






        
    