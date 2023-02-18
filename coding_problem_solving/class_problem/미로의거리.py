from collections import deque

dy,dx = [-1,1,0,0],[0,0,-1,1]
# def maze_bfs(y,x):
#     q = deque()
#     q.append([y,x])
#     cnt = 0
#     while q:
#         y,x = q.popleft()
#         visited[y][x] = 1
#
#         for d in range(4):
#             ny=y+dy[d]
#             nx=x+dx[d]
#             if 0<=ny<n and 0<=nx<n and arr[ny][nx]!=1 and visited[ny][nx]==0:
#                 if arr[ny][nx]==3:
#                     return cnt
#                 q.append([ny,nx])
#                 cnt+=1
#     return 0


def maze_run(y,x, cnt = 0):
    global Min
    if arr[y][x]==3:
        if Min>cnt:
            Min=cnt
        return

    for d in range(4):
        ny=y+dy[d]
        nx=x+dx[d]
        if 0<=ny<n and 0<=nx<n and arr[ny][nx]!=1:
            if arr[ny][nx] == 3:
                if Min > cnt:
                    Min = cnt
                return
            arr[ny][nx]=1
            maze_run(ny,nx,cnt+1)
            arr[ny][nx]=0

def find_st_idx(arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j]==2:
                return i,j

for tc in range(1,int(input())+1):

    n = int(input())
    arr = [list(map(int,input())) for _ in range(n)]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[0]*n for _ in range(n)]
    Min=int(28e10)
    y,x = find_st_idx(arr)
    maze_run(y,x)

    if Min==28e10:
        Min=0

    print(f'#{tc} {Min}')
