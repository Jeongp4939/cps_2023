import sys
sys.stdin=open('../input.txt', 'r')

# 배열의 모든 원소에 대해 +1이 되는 지점으로 이동하며 cnt
# cnt=1 부터 시작

# 방향 배열(상(0),하(1),좌(2),우(3))
dy,dx = [-1,1,0,0],[0,0,-1,1]

# 1 더 큰 수를 탐색하는 함수 생성
def one_plus(y,x,cnt=1):
    q = [[y,x]]
    while q:
        y,x = q.pop(0)
        for d in range(4):
            ny = y+dy[d]
            nx = x+dx[d]
            if 0<=ny<n and 0<=nx<n:
                if arr[ny][nx] != arr[y][x]+1:
                    continue
                cnt+=1
                q.append([ny,nx])
    return cnt

for tc in range(1,1+int(input())):

    n = int(input())

    arr = [list(map(int,input().split())) for _ in range(n)]
    Max=0
    Max_n=0
    Max_n_lst=[]
    for i in range(n):
        for j in range(n):
            cnt = one_plus(i,j)
            if cnt>Max:
                Max=cnt
                Max_n=arr[i][j]
                Max_n_lst=[Max_n]
            elif cnt==Max:
                Max_n_lst.append(arr[i][j])

    print(f'#{tc} {min(Max_n_lst)} {Max}')