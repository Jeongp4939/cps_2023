# import sys
# sys.stdin=open('input.txt','r')
#
# # 방향 배열(상(0),하(1),좌(2),우(3))
# dy,dx = [-1,1,0,0],[0,0,-1,1]
# # 파이브의 진행 가능 방향을 나타내는 딕셔너리
# dirDic={0:[],1:[0,1,2,3],2:[0,1],3:[2,3],
#         4:[0,3],5:[1,3],6:[1,2],7:[0,2]}
#
# # 시작지점은 미리 횟수에 넣어 놓고 진행
# def dfs(y,x,time):
#     # 시간이 0이 되면 종료
#     if time==0:
#         return
#     # 해당 위치의 값에 해당하는 방향들에 대해
#     for d in dirDic[arr[y][x]]:
#         ny = y+dy[d]
#         nx = x+dx[d]
#         if 0<=ny<n and 0<=nx<m:
#             for d2 in dirDic[arr[ny][nx]]:
#                 # 서로 이동 가능한 경우 dx와 dy 값이 정 반대
#                 # 즉, 합하면 0,0 이 됨
#                 if dy[d]+dy[d2]==0 and dx[d]+dx[d2]==0:
#                     if not visited[ny][nx]:
#                         visited[ny][nx]=1
#                     dfs(ny, nx, time - 1)
#
#
# for tc in range(1,1+int(input())):
#     # n : 세로, m : 가로, 맨홀 위치 : (r,c), 소요시간 :l
#     n,m,r,c,l = map(int,input().split())
#
#     # n*m 크기의 배열 입력받기
#     arr = [list(map(int,input().split())) for _ in range(n)]
#     # 지나온 곳을 표시하기 위한 배열
#     visited = [[0]*m for _ in range(n)]
#     cnt=0
#
#     # dfs를 이용해서 시간 내로 갈수 있는 분기 전부 탐색
#     dfs(r,c,l-1)
#
#     for li in visited:
#         for i in li:
#             cnt+=i
#
#     print(f'#{tc} {cnt}')
#
#
# import sys
# sys.stdin=open('input.txt','r')

# 방향 배열(상(0),하(1),좌(2),우(3))
dy,dx = [-1,1,0,0],[0,0,-1,1]
# 파이브의 진행 가능 방향을 나타내는 딕셔너리
dirDic={0:[],1:[0,1,2,3],2:[0,1],3:[2,3],
        4:[0,3],5:[1,3],6:[1,2],7:[0,2]}

# 시작지점은 미리 횟수에 넣어 놓고 진행
def bfs(y,x,time):
    cnt = 1
    q = []
    q.append([y,x])
    # 시간만큼 반복
    for i in range(time):
        tmp = []
        while q:
            y,x = q.pop(0)
            visited[y][x]=1
            for d in dirDic[arr[y][x]]:
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < n and 0 <= nx < m:
                    for d2 in dirDic[arr[ny][nx]]:
                        # 서로 이동 가능한 경우 dx와 dy 값이 정 반대
                        # 즉, 합하면 0,0 이 됨
                        if dy[d] + dy[d2] == 0 and dx[d] + dx[d2] == 0:
                            if not visited[ny][nx]:
                                visited[ny][nx] = 1
                                cnt+=1
                                # q가 아닌 tmp에 다음 이동할 좌표값을 저장
                                tmp.append([ny,nx])
        q=tmp
    return cnt


for tc in range(1,1+int(input())):
    # n : 세로, m : 가로, 맨홀 위치 : (r,c), 소요시간 :l
    n,m,r,c,l = map(int,input().split())

    # n*m 크기의 배열 입력받기
    arr = [list(map(int,input().split())) for _ in range(n)]
    # 지나온 곳을 표시하기 위한 배열
    visited = [[0]*m for _ in range(n)]
    cnt=0

    # bfs를 이용해서 시간 내로 갈수 있는 분기 전부 탐색
    cnt = bfs(r,c,l-1)

    print(f'#{tc} {cnt}')