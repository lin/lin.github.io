from functools import reduce
from itertools import *

import operator

# for bits use 30 is good enough
# log(10*8, 2) == 26

nums = [2, 1, 4]

gcd_initial = 0
xor_initial = 0
add_initial = 0

# when use %, you save time
# result = result * max(geq_count - i, 0) % MOD

# The thumb rule says that for a question with a 1-sec time limit
# your algorithm must perform at most a 10^8 number of operations. 


#      Input                Accepted Time Complexity
# 1) Around 10                   O(n!)
# 2) 15 - 25                     O(2 ^ n)
# 3) 100                         O(n ^ 4) 
# 4) 400.                        O(n ^ 3) 
# 5) 1000 (10 ^ 3)               O(n ^ 2) 
# 6) 10 ^ 5 or 10 ^ 6            O(n) and also O(n * log n)
# 8) 10 ^ 7                      O(n)
# 7) 10 ^ 9 or more              O(log n)

# I hope it gives you an rough idea :)


# reduce
reduce(operator.xor, nums) # 2 ^ 1 ^ 4
reduce(operator.add, nums) # 2 + 1 + 4
reduce(operator.add_, nums) # 2 & 1 & 4
reduce(operator.sub, nums) # 2 - 1 - 4
reduce(operator.or_, nums) # 2 | 1 | 4

# accumulate
accumulate(nums) # psum[1:], [2,3,7]
accumulate(nums, initial=0) # psum, [0,2,3,7] 


# product
product('ABCD', repeat=2)
product('ABCD', 'ABCD')
product([1,2,3,5], [1,4,5])

# permutations
permutations('ABCD', 2)

# combinations
combinations('ABCD', 2)