x,y,z = map(int, input().split())

if 0< y< x:
    # need hammer
    if z > y:
        print(-1)
    else:
        print(abs(z) + abs(z-x))
elif x < y <0:
    if z < y:
        print(-1)
    else:
        print(abs(z) + abs(z-x))
else:
    print(abs(x))
