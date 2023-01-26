# 가로 길이는 항상 1000이하로 주어진다.
# 맨 왼쪽 두 칸과 맨 오른쪽 두 칸에는 건물이 지어지지 않는다. (예시에서 빨간색 땅 부분)
# 각 빌딩의 높이는 최대 255이다.
# 4<=N<=1000
# 0<=height<=255
# 맨 왼쪽, 맨 오른쪽 2칸은 높이가 0

for tc in range(1,11):
    N = int(input())
    heights=list(map(int,input().split()))
    cnt = 0
    for i in range(2,N-2):
        view = min(heights[i]-max(heights[i-1],heights[i-2]),heights[i]-max(heights[i+1],heights[i+2]))
        if view >= 0:
            cnt+=view   
    
    print(f'#{tc} {cnt}')