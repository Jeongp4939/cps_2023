# 색종이 체크하는 함수
def check(row, col, n):
    global blue, white
    curr = graph[row][col]

    for i in range(row, row+n):
        for j in range(col, col+n):
            if graph[i][j] != curr:
                next_n = n//2
                check(row, col, next_n)
                check(row + next_n, col, next_n)
                check(row, col + next_n, next_n)
                check(row + next_n, col + next_n, next_n)
                return
    if curr == 1:
        blue += 1
    elif curr == 0:
        white += 1


# n은 2의 제곱수 2, 4, 6, 8, 16, 32, 64, 128
N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

blue = 0
white = 0

check(0,0,N)

print(white)
print(blue)