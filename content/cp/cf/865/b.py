from collections import deque
from sys import stdin
input = stdin.readline

from math import *

for _ in range(int(input())):
    n = int(input()) # even number
    hf = n//2

    es = []

    # eq1 = deque([2*i for i in range(1, hf+1)])
    eq1 = [2*i for i in range(1, hf+1)]
    eq2 = [2*(i+hf) for i in range(1, hf)]

    max_flag = True
    for i in range(hf):
        if max_flag:
            es.append(eq1[~(i//2)])
        else:
            es.append(eq1[i//2])
        if i == hf-1:
            es.append(2*n)
        else:
            es.append(eq2[~i])
        max_flag = not max_flag

    
    os = []

    oq1 = [2*i-1 for i in range(1, hf+1)]
    oq2 = [2*(i+hf)-1 for i in range(1, hf+1)]

    max_flag = True
    for i in range(hf):
        os.append(oq2[~i])
        if max_flag:
            os.append(oq1[~(i//2)])
        else:
            os.append(oq1[i//2])
        max_flag = not max_flag

    print(*es[::-1])
    print(*os[::-1])

    # os = []
    # es = []
    # for i in range(n//2):
    #     os.append(2*i+1)
    #     os.append((i+n//2)*2+1)
    #     es.append((n//2-i)*2)
    #     es.append((i+n//2+1)*2)
    
    # print(*es[::-1])
    # print(*os)


    
