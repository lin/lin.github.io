from math import *

for _ in range(int(input())):
    l, r = tuple(map(int, input().split(' ')))

    max_size = floor(log(r / l, 2)) + 1
    max_num = 2**(max_size -1)

    # if the first num is different
    # then it can be calculated the max first num
    # max_first * 2**(max_size-1) <= r
    # max_first == floor(r / 2**(max_size-1))
    first = floor(r / 2**(max_size-1)) - l + 1

    # if we can increase the second num by multiplying 3
    # but we can't increase further by 4
    print(r // (3 * max_num // 2) - l + 1)
    second = max_size - 1 if r >= l*3*2**(max_size - 2) else 0
    print(max_size, first + second)