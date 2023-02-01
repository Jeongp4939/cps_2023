dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    snail = [[0] * n for _ in range(n)]
    y, x = 0, 0
    dir = 0
    for i in range(1, n * n + 1):
        snail[y][x] = i
        y += dy[dir]
        x += dx[dir]

        if x < 0 or y < 0 or x >= n or y >= n or snail[y][x] != 0:
            y -= dy[dir]
            x -= dx[dir]
            dir = (dir + 1) % 4
            y += dy[dir]
            x += dx[dir]
    print(f'#{tc}')

    for line in snail:
        print(*line)