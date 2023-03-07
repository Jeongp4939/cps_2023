# n*n 보드에 n개의 퀸을 서로 다른 두 퀸이 공격하지 못하게 놓는 경우의 수
import copy
dy,dx = [-1,1,0,0,1,1,-1,-1],[0,0,-1,1,1,-1,1,-1]
def dfs(lvl,x):
    global cnt,visited

    if visited[lvl][x]:
        return
    elif lvl==n-1:
        cnt+=1
        return
    # queen의 공격 가능 범위 제거
    for d in range(8):
        for p in range(n):
            ny=lvl+dy[d]*p
            nx=x+dx[d]*p
            if 0<=ny<n and 0<=nx<n:
                visited[ny][nx]=1
    new_visited = copy.deepcopy(visited)

    # 놓을 위치 탐색
    for i in range(n):
        if not visited[lvl+1][i]:
            dfs(lvl+1,i)
            visited = copy.deepcopy(new_visited)


for tc in range(1,1+int(input())):
    n = int(input())
    cnt=0
    for i in range(n):
        arr = [[0] * n for _ in range(n)]
        visited = [[0] * n for _ in range(n)]
        dfs(0,i)
    print(f'#{tc} {cnt}')