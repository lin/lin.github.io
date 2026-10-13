
##  Functions for Primes

The following functions are normal Python functions that work with prime numbers.

```py
def is_divisible(x, y):
    return any(x == y * z for z in range(1, x + 1))

def is_prime(x):
    for z in range(2, x):
        if is_divisible(x, z):
            return False
    return x > 1

def nth_prime_dividing_x(n, x):
    if n == 0:
        return 0
    primes = []
    for y in range(2, x + 1):
        if is_prime(y) and is_divisible(x, y):
            primes.append(y)
    return primes[n-1] if n-1 < len(primes) else None

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def nth_prime(n):
    if n == 0:
        return 0
    primes = []
    candidate = 2
    while len(primes) <= n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes[n]
```

##  Functions for Sequences

```py
def nth_element_of_x(n, x):
    """
    Example:
        # Encode [2, 0, 3] → 2^2 * 3^0 * 5^3 = 4 * 1 * 125 = 500
        x = 500
        nth_element_of_x(0, 500) => 2  
        nth_element_of_x(1, 500) => 0  
        nth_element_of_x(2, 500) => 3  
    """
    base = nth_prime_dividing_x(n, x)
    if base is None or base <= 1:
        return 0
    y = 0
    while is_divisible(x, base ** (y + 1)):
        y += 1
    return y

def len_of_elements_of_x(x):
    """
    Example:
        x = 500  # This encodes [2, 0, 3]
        len_of_elements_of_x(500) => 3
    """
    y = 0
    while True:
        if nth_prime_dividing_x(y, x) == 0:
            break
        y += 1
    return y

def encode_sequence(seq):
    result = 1
    for i in range(len(seq)):
        prime = nth_prime(i + 1)
        exponent = seq[i]
        result *= prime ** exponent
    return result

def concat(x, y):
    len_x = len_of_elements_of_x(x)
    len_y = len_of_elements_of_x(y)
    combined = []

    # Add all elements from x
    for i in range(len_x):
        combined.append(nth_element_of_x(i, x))
    
    # Add all elements from y
    for j in range(len_y):
        combined.append(nth_element_of_x(j, y))

    return encode_sequence(combined)

def convert_to_sequence(x):
    """
    Example:
        convert_to_sequence(3) => 8  (2^3)
        nth_element_of_x(0, convert_to_sequence(3)) => 3
        len_of_elements_of_x(convert_to_sequence(3)) => 1
    """
    return 2 ** x

def parens(x):
    """
    Example:
        x = encode_sequence([5, 7])
        parens(x) encodes [11, 5, 7, 13]
    """
    return concat(concat(convert_to_sequence(11), x), convert_to_sequence(13))

```

##  Functions for Sequences


```py
def is_variable_of_type(n, x):
    """
    Checks if x is a variable of n-th type, meaning:
    x = z^n for some prime z ≥ 13
    
    Args:
        n: positive integer
        x: Gödel number
    
    Returns:
        True if x is the n-th power of some prime z ≥ 13
    """
    if n == 0:
        return False
    for z in range(13, x + 1):
        if is_prime(z) and z ** n == x:
            return True
    return False

def is_variable(x):
    """
    Checks if x is a variable (of any n-th type).
    
    Returns:
        True if there exists n such that is_variable_of_type(n, x) is True.
    """
    for n in range(1, x + 1):
        if is_variable_of_type(n, x):
            return True
    return False

def negate_formula(x):
    """
    Negates the formula encoded by x.
    R(5) is Gödel number for the "¬" symbol.
    
    Returns:
        Gödel encoding of [5] + parens(x)
    """
    return concat(convert_to_sequence(5), parens(x))

def disjunction(x, y):
    """
    Logical disjunction of formulas x and y.
    R(7) is Gödel code for "∨"
    
    Returns:
        Gödel encoding of parens(x) + [7] + parens(y)
    """
    return concat(concat(parens(x), convert_to_sequence(7)), parens(y))

def generalize(x, y):
    """
    Generalization of formula y with respect to variable x.
    R(9) is Gödel code for the ∀ quantifier.
    
    Returns:
        Gödel encoding of [x] + [9] + parens(y)
    """
    return concat(concat(convert_to_sequence(x), convert_to_sequence(9)), parens(y))


def prefix_f(n, x):
    """
    Returns the result of prefixing 'f' (Gödel code 3) n times before x.

    nth successor of x
    """
    result = x
    for _ in range(n):
        result = concat(convert_to_sequence(3), result)
    return result

def number_sign(n):
    """
    Returns the Gödel number representing the numeral for n.
    Defined as: prefix_f(n, convert_to_sequence(1))
    """
    return prefix_f(n, convert_to_sequence(1))

def is_first_type_symbol(x):
    """
    Returns:
        True if x is of the form: [3, 3, ..., 3] + [m] for valid m.

    Example:
        convert_to_sequence(1) = 2^1 = 2
        prefix_f(2, convert_to_sequence(1)) = [3, 3] + [1] → encodes: convert_to_sequence(3), convert_to_sequence(3), convert_to_sequence(1)

        x = prefix_f(2, convert_to_sequence(1))  # ≈ 2^3 * 3^3 * 5^1 = 270
        is_first_type_symbol(270) => True

        # m can also be a variable of type 1
        m = 13  # a prime ≥ 13, so x = 13^1 = 13 is a variable of type 1
        convert_to_sequence(m) = 2^13 = 8192
        prefix_f(1, convert_to_sequence(m)) = convert_to_sequence(3) * 8192
        is_first_type_symbol(convert_to_sequence(3) * 8192) => True
    """
    for m in range(1, x + 1):
        if m != 1 and not is_variable_of_type(1, m):
            continue
        for n in range(0, x + 1):
            if prefix_f(n, convert_to_sequence(m)) == x:
                return True
    return False


def is_symbol_of_type(n, x):
    """
    Determines whether x is a symbol of the n-th type.

    - If n == 1: same as is_first_type_symbol(x)
    - If n > 1: x must equal convert_to_sequence(v) for some v where v is a variable of type n

    Example:
        n = 1
        x = prefix_f(1, convert_to_sequence(1)) => x = convert_to_sequence(3) * convert_to_sequence(1)
        is_symbol_of_type(1, x) => True

        n = 2
        v = 13  # 13 is prime ≥ 13 → variable of type 2 if x = 13^2 = 169
        x = convert_to_sequence(169)  # => 2^169
        is_symbol_of_type(2, 2**169) => True
    """
    if n == 1:
        return is_first_type_symbol(x)
    for v in range(1, x + 1):
        if is_variable_of_type(n, v) and convert_to_sequence(v) == x:
            return True
    return False
```


## is_proof_of

```py

def is_inference_from(previous_proof, formula):
    if not previous_proof:
        return False

    last_formula = previous_proof[-1]
    expected_formula_str = f"S({last_formula})"
    expected_code = formula_to_code.get(expected_formula_str)
    return expected_code == formula

def is_proof_of(proof_sequence, target_formula):
    # Validate each line
    for i, formula in enumerate(proof_sequence):
        if is_axiom(formula):
            continue
        if not is_inference_from(proof_sequence[:i], formula):
            return False
    
    # Check that the proof ends in the target formula
    return proof_sequence[-1] == target_formula_code
```


## R(n)

```py
def R(n):
    def is_even(v): 
        return v % 2 == 0

    def is_odd(v): 
        return v % 2 == 1

    def greater_than_one(v): 
        return v > 1

    def 
    
    return [is_even, is_odd, greater_than_one][n-1]

# R(1)(4) => True, because we choose is_even, and call is_even(4)
# R(2)(4) => False, because we choose is_odd, and call is_odd(4)
```

```py
K = [n for n in [1,2,3] if not R(n)(n)]
# K => [1, 2]
# R(1)(1) => 1 is not even
# R(2)(2) => 2 is not odd
# R(3)(3) => 3 is greater_than_one

def S(n):
    return n in K
     
# S(1) => True
# S(3) => False
```