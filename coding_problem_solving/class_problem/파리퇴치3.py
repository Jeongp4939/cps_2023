dy =[[0,-1,1,0,0],[0,1,1,-1,-1]]
dx =[[0,0,0,-1,1],[0,1,-1,1,-1]]

def spray(y,x,m):
    Max=0
    for i in range(2):
        sum = 0
        for j in range(5):
            if j == 0:
                ny = y
                nx = x
                sum += arr[ny][nx]
            else:
                for power in range(1,m):
                    ny = y+dy[i][j]*power
                    nx = x+dx[i][j]*power
                    if 0<=ny<n and 0<=nx<n:
                        sum+=arr[ny][nx]
        Max=max(Max,sum)
    return Max

for tc in range(1,1+int(input())):
    # n : 배열의 크기, m: 노즐의 세기
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    M = 0
    for i in range(n):
        for j in range(n):
            M = max(M,spray(i,j,m))
    print(f'#{tc} {M}')