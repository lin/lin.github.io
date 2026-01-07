import inspect

def encode(input_data):
    if callable(input_data):
        text = inspect.getsource(input_data)
    else:
        text = input_data
    return int(text.encode('utf-8').hex(), 16)

def decode(number):
    byte_count = (number.bit_length() + 7) // 8
    decoded_text = number.to_bytes(byte_count, 'big').decode('utf-8')

    try:
        local_scope = {}
        exec(decoded_text, {}, local_scope)
    
        for value in local_scope.values():
            if callable(value):
                return value
                
    except Exception:
        pass

    return decoded_text

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def isOdd(n):
    return n % 2 != 0

def isProof(y, x):
    target = decode(x)
    proof = decode(y)
    
    
print(encode(isOdd))

print(decode(encode(isPrime))(encode(isOdd)))