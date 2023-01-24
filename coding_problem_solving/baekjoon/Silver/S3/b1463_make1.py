# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

# DP - BottomUp(for)

n = int(input())
d = [0]*(n+1)       # d[1] = 0 1이 1이 되는데 필요한 연산은 0번

for i in range(2,n+1):  # 2부터 n까지 반복
    d[i]=d[i-1]+1       # 1을 빼는 연산 -> 1회 진행
    if i%2==0:          # 2로 나누어 떨어질 때, 2로 나누는 연산 vs 1을 빼는 연산
        d[i]=min(d[i],d[i//2]+1)
    if i%3==0:          # 3으로 나누어 떨어질 떄, 3으로 나누는 연산 vs 1을 빼는 연산
        d[i]=min(d[i],d[i//3]+1)
print(d[n])

# DP - TopDown(재귀)

# n = int(input())
# dp={1:0}
# def rec(n):
#     if n in dp.keys():
#         return dp[n]
#     if(n%3==0) and (n%2==0):
#         dp[n]=min(rec(n//3)+1, rec(n//2)+1)
#     elif n%3==0:
#         dp[n]=min(rec(n//3)+1, rec(n-1)+1)
#     elif n%2==0:
#         dp[n] = min(rec(n//2)+1, rec(n-1)+1)
#     else:
#         dp[n]=rec(n-1)+1
#     return dp[n]
# print(rec(n))