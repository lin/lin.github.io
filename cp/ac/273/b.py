x, k = map(int, input().split())

for i in range(k):
    d, m = divmod(x, 10**(i+1))
    if m/(10**i) >= 5:
        d += 1
    x = d * (10**(i+1))
 
print(x)