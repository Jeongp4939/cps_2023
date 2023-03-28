# https://www.acmicpc.net/problem/7576

from collections import deque

m,n = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

q = deque()
dy,dx = [-1,1,0,0],[0,0,-1,1]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i,j))

Max = 1

while q:
    y,x = q.popleft()
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<n and 0<=nx<m:
            if arr[ny][nx]==0:
                arr[ny][nx] = arr[y][x]+1
                Max = max(Max, arr[ny][nx])
                q.append((ny,nx))

flag = 1

for i in range(n):
    for j in range(m):
        if not arr[i][j]:
            flag=0

if flag:
    print(Max-1)
else:
    print(-1)