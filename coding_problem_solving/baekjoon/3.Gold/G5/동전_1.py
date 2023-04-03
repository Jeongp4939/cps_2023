# import sys
# sys.setrecursionlimit(10000)
# 시간 초과
# 
# def dfs(m,sum=0):
#     global cnt
#     if sum > m:
#         return
#     if sum==m:
#         if tuple(coin_use) not in used:
#             used.add(tuple(coin_use))
#             cnt+=1
#         return
#     for i in range(n):
#         coin_use[i]+=1
#         dfs(m,sum+coin[i])
#         coin_use[i]-=1
# 
# 
# n,m = map(int,input().split())
# coin = []
# coin_use = [0]*n
# used = set()
# 
# cnt = 0
# 
# for _ in range(n):
#     coin.append(int(input()))
# dfs(m)
# print(cnt)

# DP
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k+1)
dp[0] = 1

for coin in coins:
    for j in range(coin, k+1):
        dp[j] += dp[j-coin]

print(dp[k])
