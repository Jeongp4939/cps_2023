# 설탕 배달
import sys
input = sys.stdin.readline
# 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
dp=[-1]*5001 # 0번은 인덱스를 맞추기 위해 무시 5000개 +1개의 리스트 생성
dp[3] = dp[5] = 1   # 3과 5는 사용되는 봉지이므로 1으로 초기화
n = int(input())

for i in range(6,n+1):  # 5 이하 일 떄 3, 5를 제외 하고 -1이므로 6부터 검사
    if i % 5 ==0:
        dp[i] = dp[i-5] + 1 # 5를 빼는 연산, 횟수 +1
    elif i % 3 == 0:
        dp[i] = dp[i-3] + 1 # 3을 빼는 연산, 횟수 +1
    elif dp[i-3] > 0 and dp[i-5] > 0:   # 3이나 5로 나누어 떨어지지 않는 인덱스 중 3과 5를 빼면 인덱스가 양수인 것 
        dp[i] = min(dp[i-3],dp[i-5])+1
print(dp[n])