from collections import deque

dy,dx = [-1,1,0,0],[0,0,-1,1]

def bfs(y,x):
    q=deque()
    q.append((y,x))

    while q:
        y,x = q.popleft()
        V[y][x] = 1
        for d in range(4):
            ny = y+dy[d]
            nx = x+dx[d]
            if 0<=ny<N and 0<=nx<M:
                if MAP[ny][nx] and not V[ny][nx]:
                    V[ny][nx] = 1
                    q.append((ny,nx))

T=int(input())
for i in range(T):
    M,N,K = map(int,input().split())
    MAP = [[0]*M for _ in range(N)]
    V = [[0]*M for _ in range(N)]

    for _ in range(K):
        x,y = map(int,input().split())
        MAP[y][x] = 1
    cnt=0
    for i in range(N):
        for j in range(M):
            if MAP[i][j]==1 and not V[i][j]:
                bfs(i,j)
                cnt+=1

    print(cnt)


