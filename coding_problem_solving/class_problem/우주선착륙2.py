dy = [-1,1,0,0,1,-1,1,-1]
dx = [0,0,-1,1,1,1,-1,-1]

for tc in range(1,int(input())+1):

    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    result = 0

    for y in range(n):
        for x in range(m):
            cnt = 0
            for d in range(8):
                ny = y + dy[d]
                nx = x + dx[d]
                if 0<=ny<n and 0<=nx<m:
                    if arr[ny][nx] < arr[y][x]:
                        cnt+=1
            if cnt>=4:
                result+=1
    print(f'#{tc} {result}')