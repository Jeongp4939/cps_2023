# 입력은 네 줄이며, 각 줄은 직사각형의 위치를 나타내는 네 개의 정수로 주어진다.
# 첫 번째와 두 번째의 정수는 사각형의 왼쪽 아래 꼭짓점의 x좌표, y좌표이고 세 번째와 네 번째의 정수는 사각형의 오른쪽 위 꼭짓점의 x좌표, y좌표이다.
# 모든 x좌표와 y좌표는 1이상이고 100이하인 정수이다.
def make_ractangle(arr,x1,y1,x2,y2):
    for i in range(min(x1,x2),max(x1,x2)):
        for j in range(min(y1,y2),max(y1,y2)):
            arr[i][j]=1
    return arr

arr = [[0]*100 for _ in range(100)]
for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    make_ractangle(arr,x1,y1,x2,y2)

area = 0
for line in arr:
    area+=sum(line)
print(area)