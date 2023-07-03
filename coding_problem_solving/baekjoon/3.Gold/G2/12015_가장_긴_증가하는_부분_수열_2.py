import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
dp = [arr[0]]

for i in arr:
    if dp[-1] < i:
        dp.append(i)
    else:
        idx = bisect_left(dp,i)
        dp[idx] = i

print(len(dp))