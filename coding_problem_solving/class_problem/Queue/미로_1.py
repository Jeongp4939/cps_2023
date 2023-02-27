from collections import deque

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(y,x):
    q = deque()
    q.append([y,x])
    while q:
        y,x = q.popleft()
        visited[y][x]=1
        for d in range(4):
            ny = y+dy[d]
            nx = x+dx[d]
            if 0<=ny<16 and 0<=nx<16:
                if arr[ny][nx]=='0' and visited[ny][nx]==0:
                    q.append([ny, nx])
                    visited[ny][nx] = 1
                if arr[ny][nx]=='3':
                    return 1
    return 0

for tc in range(1,11):
    input()
    arr = [list(input()) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    y = x = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                y, x = i, j

    result = bfs(y,x)
    print(f'#{tc} {result}')