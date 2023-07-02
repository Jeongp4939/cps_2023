n = int(input())
arr = list(map(int,input().split()))

dp = [1]*n

# 1번 인덱스로부터 시작
for i in range(1,n):
    # 앞에 있는 인덱스들을 비교
    for j in range(0,i):
        # 현재 인덱스의 수보다 작은 수이면
        # 해당 인덱스에 해당하는 dp의 수+1 과 현재 위치의 dp중 더 큰수를 삽입
        if arr[j] < arr[i]:
            dp[i] = max(dp[i],dp[j]+1)

result = max(dp)
print(result)
