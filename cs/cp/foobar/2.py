def solution(n, b):
    #Your code here
    k = len(n)
    seen = []
    
    while n not in seen:
        seen.append(n)
        # prepare the next n
        str_list = list(n)
        str_list.sort()
        
        x = ''.join(str_list[::-1])
        y = ''.join(str_list)
        
        z_val = int(x, b) - int(y, b)
        
        # transform z value to digits
        z_digits = []
        while z_val:
            z_digits.append(str(z_val % b))
            z_val //= b
        
        # add padding zeroes
        z_digits = z_digits + ['0'] * (k - len(z_digits))
        
        z = ''.join(z_digits[::-1])
        
        n = z
        
    
    return len(seen) - seen.index(n)