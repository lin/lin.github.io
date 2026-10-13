h, m = map(int, input().split())

def confusing(h, m):
    a, b = h//10, h % 10
    c, d = m//10, m % 10
    return 0 <= a*10 + c <= 23 and 0 <= b*10 + d <= 59

while not confusing(h, m):
    m += 1
    
    if m == 60:
        h += 1
        m = 0
    
    if h == 24:
        h = 0

print(h, m)