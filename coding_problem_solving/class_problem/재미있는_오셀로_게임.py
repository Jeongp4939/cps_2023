# 1 흑돌, 2 백돌
# T가 첫줄에 주어지고 다음줄에 N ,M이 주어짐
# N은 판의 크기, M은 돌을 놓는 횟수

# 상하좌우, 양방향 대각선을 기준으로 모든 방향 검사
dy=[-1,1,0,0,-1,1,-1,1]
dx=[0,0,-1,1,1,1,-1,-1]


def othello(y,x,c,n):
    global b_cnt, w_cnt

    if c == 1:          # 놓은 돌의 개수 +1
        b_cnt += 1
    else:
        w_cnt += 1

    board[y][x]=c
    for i in range(8):          # 8방향 검사
        point = 1
        while point < n+1:        # 같은 색의 돌의 위치 확인(검색범위 : 패딩까지, c나 0을 만나면 break)
            ny= y + dy[i]*point
            nx= x + dx[i]*point
            if board[ny][nx] == 0:  # 0을 만나면 없으므로 point는 놔두고 탈출
                point = 1
                break
            elif board[ny][nx] == c:
                break
            else:
                point+=1
        for j in range(1,point):
            ny = y + dy[i] * j
            nx = x + dx[i] * j
            if 0 < ny <= n and 0 < nx <= n and board[ny][nx] not in [0,c]:
                board[ny][nx] = c
                if c == 1:          # 뒤집은 돌의 개수 변화 적용
                    b_cnt += 1
                    w_cnt -= 1
                else:
                    b_cnt -= 1
                    w_cnt += 1


for tc in range(1,int(input())+1):
    n,m = map(int,input().split())
    b_cnt = w_cnt = 2

    board = [[0]*(n+2) for _ in range(n+2)]   # (n+2)*(n+2) 게임판 + 패딩(상하좌우 1) 만들기
    board[n//2][n//2]=board[n//2+1][n//2+1]=2
    board[n//2+1][n//2] = board[n//2][n//2+1] = 1



    for _ in range(m):
        y,x,c = map(int,input().split())
        othello(y,x,c,n)
    print(f'#{tc} {b_cnt} {w_cnt}')