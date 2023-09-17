---
title: "DP Bitmask"
isCJKLanguage: true
math: true
---

```python
mask & (1<<j) # check
mask ^ (1<<j) # remove
mask | (1<<j) # set
```

#### Arrangements max/min/cnt

- [Min XOR sum](https://leetcode.com/contest/biweekly-contest-53/problems/minimum-xor-sum-of-two-arrays/)

```python
def dp(mask, i):
    if i == n: 
        return 0
    
    res = inf
    for j in range(n):
        if mask & (1<<j):
            res = min(res, dp(mask ^ (1<<j), i + 1) + (nums1[i] ^ nums2[j]))
    return res

return dp((1<<n) - 1, 0)
```

- [Count](https://leetcode.com/contest/weekly-contest-350/problems/special-permutations/)

```python
def dfs(mask, prev):
    if mask == 0: 
        return 1
    
    res = 0
    for i in range(n):
        if mask & (1 << i) and (nums[i] % prev == 0 or prev % nums[i] == 0):
            res += dfs(mask ^ (1 << i), nums[i],)
    return res

return dfs((1 << n) - 1, 1)
```

- [Count](https://leetcode.com/problems/beautiful-arrangement/)

```python
def dp(mask, cnt):
    if mask == (1 << n) - 1: 
        return 1
    
    res = 0
    for i in range(n):
        if not (mask & (1 << i)) and (cnt % (i+1) == 0 or (i+1) % cnt == 0):
            res += dp(mask | (1 << i), cnt + 1)
            
    return res

return dp(0, 1)
```