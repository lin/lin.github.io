from math import *

a, b = tuple(map(int, input().split()))

x = (a/(2*b))**(2/3) - 1
f = lambda x: b*x + a/sqrt(x+1)

if x <= 0:
    min_val = f(0)
else:
    min_val = min(f(floor(x)), f(ceil(x)))
print(min_val)