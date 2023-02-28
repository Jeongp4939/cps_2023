# https://www.acmicpc.net/problem/2775

# a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b 호까지
# 사람들의 수의 합만큼사람들을 데려와 살아야 한다
# 아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때,
# 주어지는 양의 정수 k와 n에 대해 k층에 n 호에는 몇 명이 살고 있는지 출력하라.
# 0층의 i호 : i명
# 1<=k,n<=14

arr = [[1]*15 for _ in range(15)]
for i in range(1,15):
    arr[0][i] += i
for i in range(1,15):
    for j in range(1,15):
        arr[i][j] = arr[i-1][j]+arr[i][j-1]

T = int(input())
for tc in range(T):
    k = int(input())
    n = int(input())

    print(arr[k][n-1])
