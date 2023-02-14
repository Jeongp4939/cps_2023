# 1 흑돌, 2 백돌
# T가 첫줄에 주어지고 다음줄에 N ,M이 주어짐
# N은 판의 크기, M은 돌을 놓는 횟수

# 상하좌우, 양방향 대각선을 기준으로 모든 방향 검사
dy=[-1,1,0,0,-1,1,-1,1]
dx=[0,0,-1,1,1,1,-1,-1]
b_cnt=w_cnt=2

def othello(y,x,c):
    global b_cnt, w_cnt

    if c == 1:
        b_cnt += 1
    else:
        w_cnt += 1

    board[y][x]=c
    for i in range(8):
        ny=y+dy[i]
        nx=x+dx[i]

        # 수정 필요

        # if 0<ny<=n and 0<nx<=n:
        #     if board[ny][nx] == c and board[ny-ny//2][nx-nx//2]!=c:
        #         board[ny-dy[i]][nx-dx[i]] = c
        #         if c == 1:
        #             b_cnt += 1
        #             w_cnt -= 1
        #         else:
        #             b_cnt -= 1
        #             w_cnt += 1
        #         break


for tc in range(1,int(input())+1):
    n,m = map(int,input().split())
    board = [[0]*(n+2) for _ in range(n+2)]   # (n+2)*(n+2) 게임판 (패딩) 만들기
    board[n//2][n//2]=board[n//2+1][n//2+1]=2
    board[n//2+1][n//2] = board[n//2][n//2+1] = 1


    for _ in range(m):
        y,x,c = map(int,input().split())
        othello(y,x,c)
    print(f'#{tc} {b_cnt} {w_cnt}')