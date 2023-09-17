---
title: "Sort"
isCJKLanguage: true
math: true
---

> Merge and Quick are more important

### Bubble, switch, forwards

```python
def bubble(nums):
    for i in range(n):
        for j in range(n - 1 - i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
```

### Insert, switch, backwords

```python
def insert(nums):
    for i in range(1, n):
        for j in range(i, 0, -1):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
    return nums

def insert(nums):
    for i in range(1, n):
        curr = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > curr:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = curr
    return nums
```

### Merge, recursive

```python
def merge(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        
        merge(left)
        merge(right)
        
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
    
    return nums
```
### Quick Sort, partition

```python
# nlogn pass, 2 pointers
def quick(nums):
    def partition(start, end):
        # out of index
        if start >= end: return
        
        pivot = nums[(start + end) // 2]
        
        l, r = start, end
        while l <= r:
            # move l to the first > pivot
            while nums[l] < pivot and l <= r:
                l += 1
                
            # move l to the first < pivot
            while nums[r] > pivot and l <= r:
                r -= 1
            
            # swap those > and <
            # until l - 1 == r + 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        # r is at the left of mid
        # l is at the right of mid
        partition(start, r)
        partition(l, end)
    
    partition(0, len(nums) - 1)
    return nums
```

# Select, insert sort

```python
def select(nums):
    for i in range(len(nums)):
        minIndex = nums[i:].index(min(nums[i:]))
        nums[i + minIndex], nums[i] = nums[i], nums[i + minIndex]
    return nums
```

### Heap

```python
import heapq

def heap(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        
    res = []
    for _ in range(len(heap)):
        res.append(heapq.heappop(heap))

    return res

def heap(nums):
    def hpush(arr, val):
        arr.append(val)

        # swap node and its parent
        n = len(arr) - 1
        p = (n - 1) // 2
        while p >= 0 and arr[n] < arr[p]:
            arr[p], arr[n] = arr[n], arr[p]
            n = p
            p = (n - 1) // 2
    
    def hpop(arr):
        top = arr[0]
        arr[0] = arr[-1]

        # swap node and its child with min value 
        p = 0
        l = 1
        r = 2
        while l < len(arr) and r < len(arr) and arr[p] > min(arr[l], arr[r]):
            m = l if arr[l] < arr[r] else r
            arr[m], arr[p] = arr[p], arr[m]
            p = m
            l = 2 * p + 1
            r = 2 * p + 2

        arr.pop()
        return top
            
    heap = []
    for num in nums:
        hpush(heap, num)

    res = []
    for _ in range(len(heap)):
        res.append(hpop(heap))

    return res
```