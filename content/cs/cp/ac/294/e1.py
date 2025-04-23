from bisect import bisect_left, bisect_right

l, n1, n2 = map(int, input().split())
V1, V2, L1, L2 = [], [], [], []

for _ in range(n1):
    v, l = map(int, input().split())
    V1.append(v)
    L1.append(l)

for _ in range(n2):
    v, l = map(int, input().split())
    V2.append(v)
    L2.append(l)
 
psum1, psum2 = [0], [0]
for l in L1:
    psum1.append(psum1[-1] + l) 
for l in L2:
    psum2.append(psum2[-1] + l) 


res = 0
for i in range(n1):
    start1, end1 = psum1[i],  psum1[i + 1]

    left_index = bisect_right(psum2, start1)
    right_index = bisect_left(psum2, end1)
    
    for j in range(left_index, right_index + 1):
        if V1[i] == V2[j - 1]:
            res += min(psum2[j], end1) - max(psum2[j - 1], start1)
            
print(res)