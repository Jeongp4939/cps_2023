# 왼쪽 아래 좌표, 오른쪽 위 좌표를 입력 받아 빨강(1), 파랑(2)로 칠한다
# 겹쳐지면 보라(3)색으로 표현되고 이 경우 보라색의 넓이를 구해라
# 빈 배열을 선언하고 사각형을 그림
# 앞에 있는 삼각형이 있다면 3으로 채우기
# 그냥 숫자 더해버리면 된다..?

for tc in range(1, int(input())+1):
    arr = [[0]*10 for _ in range(10)]
    n = int(input())

    for _ in range(n):
        y1,x1,y2,x2,c = map(int,input().split())
        if c == 1:
            for i in range(y1,y2+1):
                for j in range(x1,x2+1):
                    if arr[i][j] == 2 or arr[i][j] == 3:
                        arr[i][j] = 3
                    else:
                        arr[i][j] = 1
        elif c == 2:
            for i in range(y1,y2+1):
                for j in range(x1,x2+1):
                    if arr[i][j] == 1 or arr[i][j] == 3:
                        arr[i][j] = 3
                    else:
                        arr[i][j] = 2
        cnt = 0
        for line in arr:
            for i in line:
                if i ==3:
                    cnt +=1

    print(f'#{tc} {cnt}')