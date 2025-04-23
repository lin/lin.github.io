from sys import stdout

left = 1
right = 1000001
 
while left < right:
    mid = (left + right) // 2

    print(mid)
    stdout.flush()

    response = input()

    if response == '<':
        right = mid
    else:
        left = mid + 1
    
print("!", right - 1)
stdout.flush()