from sys import stdin
input = stdin.readline

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop,heapify
from functools import lru_cache
from itertools import accumulate, permutations
from math import *

dir4 = [(-1,0),(0,1),(1,0),(0,-1)]
dir8 = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

def solve(n, nums):
    s = ['d']

    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            s.append('d')
        elif nums[i] < nums[i + 1]:
            s.append('i')
        else:
            s.append('e')

    s.append('i')
    # print(s)    

    res = 0
    # is_valid = False
    seen_d = False
    for ch in s:
        if ch == 'd':
            if not seen_d:
                seen_d = True
        elif ch == 'i':
            if seen_d:
                res += 1
                seen_d = False
    return res == 1

T = int(input())
for _ in range(T):
    n = int(input())
    # m, s = tuple(map(int, input().split(' ')))
    nums = list(map(int, input().split(' '))) # list of nums
    # s = input().strip()
    # words = [w.strip() for w in input().split(' ')]

    # print(solve(n))
    print("YES" if solve(n, nums) else "NO")


    int find(vector<int> &ds, int i) {
        return ds[i] < 0 ? i : ds[i] = find(ds, ds[i]);
    }
    int minCostConnectPoints(vector<vector<int>>& ps) {
        int n = ps.size(), res = 0;
        vector<int> ds(n, -1);
        vector<array<int, 3>> arr;
        for (auto i = 0; i < n; ++i)
            for (auto j = i + 1; j < n; ++j) {
                arr.push_back({abs(ps[i][0] - ps[j][0]) + abs(ps[i][1] - ps[j][1]), i, j});
            }
        make_heap(begin(arr), end(arr), greater<array<int, 3>>());
        while (!arr.empty()) {
            pop_heap(begin(arr), end(arr), greater<array<int, 3>>());
            auto [dist, i, j] = arr.back();
            arr.pop_back();
            i = find(ds, i), j = find(ds, j);
            if (i != j) {
                res += dist;
                ds[i] += ds[j];
                ds[j] = i;
                if (ds[i] == -n)
                    break;
            }
        }
        return res;
    }