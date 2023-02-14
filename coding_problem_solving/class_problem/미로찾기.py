dy,dx=[-1,1,0,0],[0,0,-1,1]

def bfs(ny,nx):
    stack = [[ny,nx]]
    arr[ny][nx] = '1'
    while stack:
        y, x = stack.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] != '1':
                if arr[ny][nx]=='3':
                    return '1'
                arr[ny][nx] = '1'
                stack.append([ny,nx])
    return '0'

for tc in range(1,int(input())+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

    ny=nx=0

    for i in range(n):          # 시작 좌표 구하기
        for j in range(n):
            if arr[i][j]=='2':
                ny = i
                nx = j
                break

    result = bfs(ny,nx)

    print(f'#{tc} {result}')