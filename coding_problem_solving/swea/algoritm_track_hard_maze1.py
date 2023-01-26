dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(start):
    visit = [[0]*16 for _ in range(16)]
    stack = [start]
    while stack:
        y, x = stack.pop()
        if visit[y][x] == 0:
            visit[y][x] = 1
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if data[ny][nx] == '0':
                    stack.append([ny, nx])
                elif data[ny][nx] == '3':
                    return 1
    return 0


for t in range(1, 11):
    input()
    data = [input() for i in range(16)]
    print('#{} {}'.format(t, dfs([1, 1])))