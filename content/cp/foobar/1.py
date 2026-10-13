def solution(s):
    n = len(s)
    for i in range(n):
        substr = s[:i+1]
        cnt = s.count(substr)
        if cnt * (i+1) == n:
            return cnt