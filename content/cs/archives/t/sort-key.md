---
title: "Sort Key"
isCJKLanguage: true
math: true
---

### cmp_to_key

```python
# https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        comp = lambda a, b: 1 if a + b < b + a else -1 if a + b > b + a else 0
        largest_num = ''.join(sorted(map(str, nums), key=cmp_to_key(comp)))
        return '0' if largest_num[0] == '0' else largest_num
```

### Complicated Key

```python
# https://leetcode.com/problems/reorder-data-in-log-files/

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        for log in logs:
            if log.split()[1].isnumeric():
                digits.append(log)
            else:
                letters.append(log)
                
        def letter_sort_key(log):
            identifier, content = log.split(" ", 1)
            return (content, identifier)
        
        letters.sort(key=letter_sort_key)

        return letters + digits
```

```python
# https://leetcode.com/problems/rank-teams-by-votes/description/

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        teams = list(votes[0])

        count = [[0 for _ in range(len(votes[0]))] + [-i-1] for i in range(26)]

        for vote in votes:
            for index,element in enumerate(vote):
                count[ord(element)-ord('A')][index] += 1

        teams.sort(key=lambda x:count[ord(x)-ord('A')],reverse = True)

        return "".join(teams)
```