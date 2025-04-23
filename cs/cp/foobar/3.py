def solution(pegs):
    # Your code here
    # let x be the radius of the last gear
    # 2*x will be the radius of the first gear
    
    n = len(pegs)
    
    deltas = []
    
    for i in range(1, n):
        deltas.append(pegs[i] - pegs[i-1])
    
    # d0 - d1 + d2 - d3
    deltas_sum = 0
    for i, d in enumerate(deltas):
        deltas_sum += d if i % 2 == 0 else -d

    # check if the condition is valid
    x = deltas_sum if n & 1 else deltas_sum / 3
    
    # we can't solve x, so not possible
    if x < 1:
        return [-1, -1]
    
    prev_radius = 2*x
    for d in deltas:
        if d < prev_radius + 1:
            return [-1, -1]
        prev_radius = d - prev_radius
        
    # n is odd so len(delta) is even, e.g. d0 d1
    if n & 1:
        return [deltas_sum * 2, 1]
    
    # make it simplest form
    if deltas_sum % 3 == 0:
        return [deltas_sum*2//3, 1]
        
    return [deltas_sum*2, 3]

print(solution([4, 30, 50]))
print(solution([4, 17, 50]))