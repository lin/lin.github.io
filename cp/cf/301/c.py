from sys import stdin
input = stdin.readline

from math import *
from collections import Counter, deque


s = input().strip()
t = input().strip()

cnt_s = Counter(s)
cnt_t = Counter(t)

at_s = cnt_s['@']
at_t = cnt_t['@']

for i in range(26):
    ch = chr(ord('a') + i)
    # print(ch, cnt_s[ch], cnt_t[ch], at_s, at_t)
    if cnt_s[ch] != cnt_t[ch]:
        if ch not in 'atcoder':
            print('No')
            exit()

        if cnt_s[ch] > cnt_t[ch]:
            if at_t < cnt_s[ch] - cnt_t[ch]:
                print('No')
                exit()
            at_t -= cnt_s[ch] - cnt_t[ch]
        else:
            if at_s < cnt_t[ch] - cnt_s[ch]:
                print('No')
                exit()
            at_s -= cnt_t[ch] - cnt_s[ch]
        
print("Yes")

