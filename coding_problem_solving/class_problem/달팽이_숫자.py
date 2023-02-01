dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    snail = [[0] * n for _ in range(n)]
    y, x = 0, 0
    direction = 0
    for i in range(1, n * n + 1):
        snail[y][x] = i
        y += dy[direction]
        x += dx[direction]

        if x < 0 or y < 0 or x >= n or y >= n or snail[y][x] != 0:
            y -= dy[direction]
            x -= dx[direction]
            direction = (direction + 1) % 4
            y += dy[direction]
            x += dx[direction]
    print(f'#{tc}')

    for line in snail:
        print(*line)