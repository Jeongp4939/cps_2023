dy,dx=[1,0],[0,1]

def bfs(level=0,y=0,x=0,Sum=0):
    global Min
    if Sum>Min:
        return
    if y==n-1 and x==n-1:
        Min = min(Sum,Min)
        return
    for d in range(2):
        ny=y+dy[d]
        nx=x+dx[d]
        if 0<=ny<n and 0<=nx<n:
            bfs(level+1,ny,nx,Sum+arr[ny][nx])

for tc in range(1,1+int(input())):
    n = int(input())
    Min = int(28e8)
    arr=[list(map(int,input().split())) for _ in range(n)]
    bfs(Sum=arr[0][0])

    print(f'#{tc} {Min}')