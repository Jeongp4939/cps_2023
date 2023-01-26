# X=0인 출발점에서 출발하는 사례에 대해서 화살표로 표시한 바와 같이, 아래 방향으로 진행하면서 좌우 방향으로 이동 가능한 통로가 나타나면 방향 전환을 하게 된다.
# 방향 전환 이후엔 다시 아래 방향으로만 이동하게 되며, 바닥에 도착하면 멈추게 된다.
# 문제의 X표시에 도착하려면 X=4인 출발점에서 출발해야 하므로 답은 4가 된다. 해당 경로는 별도로 표시하였다.
# 100 x 100 크기의 2차원 배열로 주어진 사다리에 대해서, 지정된 도착점에 대응되는 출발점 X를 반환하는 코드를 작성하라
# 1이 사다리 0은 못가는 곳, 도착점은 2 DFS

dy,dx = [0,0,1],[-1,1,0]    # 좌 우 아래


def ladder_dfs(start):
    visit = [[0]*100 for _ in range(100)]
    stack = [start]
    while stack:
        y,x = stack.pop()
        if visit[y][x] == 1:    # 방문 지점 0으로 변경
            visit[y][x] = 0
        for i in range(2):      # 좌우를 먼저 확인
            ny=y+dy[i]
            nx=x+dx[i]
            if ladder[ny][nx]=='1':
                stack.append([ny,nx])
            elif ladder[ny][nx]=='0':
                ny=y+dy[2]              # 아래로 향하는 이동
                nx=x+dx[2]
                if ladder[ny][nx]=='1':   
                    stack.append([ny,nx])
                elif ladder[ny][nx]=='2':
                    return 1
    return 0
                

for tc in range(1,11):
    input()
    ladder = [input() for _ in range(100)]
    for i in range(100):
        if ladder[0][i]=='1':
            if ladder_dfs([0,i]):
                print(f'#{tc} {i}')
                break
    
    
    
    
